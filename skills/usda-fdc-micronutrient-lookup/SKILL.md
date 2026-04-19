---
name: usda-fdc-micronutrient-lookup
description: Use when a user asks how much of a specific micronutrient (iron, Vitamin B12, calcium, magnesium, zinc, vitamin D, folate, potassium, etc.) is in a particular food — fetches the FDC detail record and extracts the per-serving value for the requested nutrient, comparing to the adult RDA.
---

# USDA FDC — Micronutrient Lookup

## When to Use

The user has a doctor-diagnosed deficiency or wants to verify a supplement-worthy nutrient amount in a specific food. Examples: "Is this pasta a good source of iron?", "How much Vitamin B12 does this yogurt have?", "Does this cereal cover my daily calcium?". The question names **one or two** specific micronutrients — handle both in a single call by passing a comma-separated list to `?nutrients=` (e.g. `nutrients=303,1114` for iron + vitamin D) and report each with its own %RDA. Only route to `usda-fdc-macro-alignment` / `usda-fdc-recipe-breakdown` when the user asks for a full macro or multi-nutrient breakdown (3+ nutrients or "all nutrients").

## API Surface

- **Discovery:** `GET /foods/search?query=<name>&pageSize=10&api_key=...` → read `foods[0].fdcId` (prefer `dataType` Foundation/SR Legacy for generic foods, Branded for brand-name products).
- **Detail endpoint:** `GET /food/{fdcId}?format=full&nutrients=<comma-separated nutrient numbers>` (the `nutrients` filter trims payload; optional but cheaper)
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read:** `foodNutrients[].nutrient.number`, `foodNutrients[].amount`, `foodNutrients[].nutrient.unitName`, `servingSize`, `servingSizeUnit`, `labelNutrients` (Branded only)

## Key nutrient numbers (USDA canonical)

| Nutrient | Number |
|---|---|
| Iron (Fe) | `"303"` |
| Calcium (Ca) | `"301"` |
| Vitamin B-12 | `"418"` |
| Vitamin D (D2 + D3), IU | `"324"` (fallback if 1114 absent; × 0.025 → µg) |
| Vitamin D (D2 + D3), µg | `"1114"` (preferred; often missing on Foundation/SR Legacy — request BOTH) |
| Magnesium | `"304"` |
| Zinc | `"309"` |
| Potassium | `"306"` |
| Folate (total) | `"417"` |
| Vitamin C | `"401"` |
| Vitamin A (RAE) | `"320"` |

## Answer Pipeline (MANDATORY order)

1. Fetch detail record → read nutrient amount + unitName.
2. **Unit-normalize** (IU→µg for vit D; print `mcg` not µg).
3. **Portion-convert** (see rule below) — if user named a cup/oz/piece/tbsp/medium, convert from per-100g using the household table; if user named a Branded product, use `servingSize`.
4. **Validate** (retry if 0/implausible for a food that clearly contains it).
5. Compute %RDA (ALWAYS — never emit a qualitative label like "meaningful" / "good source" without the numeric %RDA in the same sentence), apply significance label, emit answer WITH UNIT.

**Do not skip step 3.** A per-100g figure is NEVER the final answer when the user specified a different portion. This also applies when the user names a generic food with NO explicit portion (e.g. "yogurt", "lentils", "kale"): default to a standard household serving (yogurt 1 cup ≈ 245 g; milk 1 cup = 240 ml; juice 1 cup = 240 ml; cooked lentils 1 cup ≈ 198 g; raw leafy greens 1 cup ≈ 30 g) and STATE the gram/ml weight in the answer. A per-100g answer without a portion conversion is a defect even when the user didn't explicitly say "per cup".

## Minimal Happy Path

```bash
# Get ONLY iron (303) + calcium (301) for fdcId 1750340, full format
curl -s "https://api.nal.usda.gov/fdc/v1/food/1750340?format=full&nutrients=303,301&api_key=${USDA_FDC_API_KEY}" \
  | jq '.foodNutrients[] | {num: .nutrient.number, name: .nutrient.name, amount: .amount, unit: .nutrient.unitName}'
```

## Discovery & candidate selection

- After `/foods/search`, verify the chosen hit actually matches the user's food (check `description`, `brandOwner`, `dataType`). If the top hit's description is off-category (e.g. user asked strawberries, hit is a strawberry-flavored snack), scan the next few results or add a `dataType=Foundation,SR Legacy` filter. If `foods` is empty OR no hit's `description` + `brandOwner` plausibly matches the user's named brand/product, say "not found in FDC" — do NOT answer "Product found in FDC" from the search call alone, and NEVER skip the `/food/{fdcId}` detail call: the search hit is only a candidate until the detail record is fetched and the nutrient amount is read.
- Before answering, confirm the requested nutrient's `amount` is present AND non-zero. If it is `0`, `null`, missing, or implausibly low for a food that clearly contains it, **you MUST retry with a different fdcId before answering**. Implausibility examples (memorize these magnitudes): canned salmon vitamin D ≥ 10 mcg/100g; trail mix with nuts/seeds iron ≥ 2 mg/100g (0.17 mg is a red flag — retry); strawberries vitamin C ≥ 50 mg/100g; fortified dairy/cereal B-12 or vit D non-zero (Activia / Yoplait / Dannon flavored yogurts are fortified — 0 mcg B-12 means wrong fdcId, retry); granola folate > 20 mcg/100g; almonds magnesium ≥ 250 mg/100g (0 mg means wrong fdcId); romaine/spinach/kale folate ≥ 100 mcg/100g (0 mcg means wrong fdcId). Retry order: another Foundation/SR Legacy hit, then another Branded hit. After 2 failed retries, answer "FDC record incomplete for <nutrient>" — NEVER return `0.0 mcg`, `0 mg`, or a flagged low value as the final answer.

## API Quirks

- **Nutrient numbers are STRINGS, not integers.** `foodNutrients[].nutrient.number === "303"`, never `=== 303`.
- **Unit strings contain the micro-sign `µ` (U+00B5).** Ensure UTF-8 when printing `nutrient.unitName`; if you see `Âµg` / `Â µg` mojibake, your pipeline decoded bytes as latin-1. **In the final answer ALWAYS emit the ASCII spelling `mcg` instead of `µg`** — this sidesteps every codepage/latin-1 round-trip bug. Normalize `"UG"`, `"ug"`, `"µg"`, `"Âµg"` all to `mcg` in the user-facing string.
- **Basis differs by dataType.** Foundation / SR Legacy / Survey foodNutrients are **per 100 g**. Branded foodNutrients are also stored per 100 g (LCCS-derived), but **`labelNutrients` is per serving** as printed on the nutrition-facts panel.
- To convert per-100 g → per-serving, multiply by `servingSize / 100`. Check `servingSizeUnit` — only safe to do this math when it is `"g"` or `"ml"` (density ≈ 1 g/ml for most liquids).
- **Branded per-serving shortcut.** When `dataType == "Branded"`: try `labelNutrients.<key>.value` FIRST (matches printed panel; keys: `calcium`, `iron`, `vitaminD`, `potassium`, `vitaminA`, `vitaminB12`, `zinc`, `folate`, `magnesium`). **If that key is absent or null, you MUST compute `foodNutrients[<num>].amount * servingSize / 100` before declaring the record incomplete** — NEVER answer "Label nutrient data unavailable" after reading only labelNutrients. The fallback is mandatory, not optional. Only after BOTH paths return missing/zero may you say "FDC record incomplete". State in the answer when the value is panel-verified vs foodNutrients-derived.
- **labelNutrients vs foodNutrients divergence.** When BOTH are present and differ by >10%, trust `labelNutrients` (matches the printed nutrition panel the consumer sees) and note the per-100g-derived value in parentheses. When labelNutrients is absent on a Branded record, compute per-serving as `foodNutrients.amount * servingSize / 100` and state that it is derived (not panel-verified).
- **`foodNutrients` shape differs between `?format=full` and `?format=abridged`.** Full: nested `{nutrient: {number, name, unitName}, amount, ...}`. Abridged: flat `{number, name, amount, unitName}`. When you pick a format, parse consistently.
- Category-header entries (e.g. `{"nutrient": {"number": "951", "name": "Proximates"}, ...}`) have no `amount` field. Filter them out.
- RDA reference (adult, IOM 2023 baseline): iron 18 mg (women) / 8 mg (men), calcium 1000 mg, B-12 2.4 µg, vitamin D 15 µg (= 600 IU; 1 µg = 40 IU), magnesium 400 mg, zinc 11 mg, potassium 3400 mg, folate 400 µg DFE, vitamin C 90 mg, vitamin A 900 µg RAE.
- **Household-portion reference (REQUIRED when user names piece/cup/oz/tbsp and FDC gives per-100g):** raw leafy greens 1 cup ≈ 30 g; cooked leafy greens 1 cup ≈ 130 g; berries 1 cup ≈ 150 g; cooked beans/lentils/chickpeas 1 cup ≈ 180 g (lentils ~198 g, chickpeas ~164 g); cooked quinoa/rice 1 cup ≈ 185 g; tempeh 1 cup ≈ 166 g; nuts/seeds 1 oz = 28.35 g; 3 oz meat/fish = 85 g; 1 medium kiwi ≈ 75 g; 1 medium apple/orange ≈ 180 g; 1 medium banana ≈ 120 g; 1 tbsp solid spread ≈ 14 g; 1 cup liquid = 240 ml. **Conversion formula: per_portion = per_100g_amount * grams_in_portion / 100.** You MUST apply this and state the assumed gram weight in the answer. Emitting a per-100g value when the user asked per-cup/oz/medium is a defect.
- **Always trust `nutrient.unitName` over assumed units.** For vitamin D, check unit before computing %RDA: if `unitName == "IU"` divide by 600; if `"µg" / "UG"` divide by 15. A value like "99 µg vitamin D per serving of milk" is implausible — you likely read nutrient 324 (IU) and mislabeled the unit.

## Common Mistakes

- Reporting `0 mg` or `0 µg` as a real answer, or answering from a `/foods/search` hit alone without a `/food/{fdcId}` detail call. A zero for a nutrient the food is known to contain (fortified dairy → B-12, fortified cereal → vitamin D / iron) means the chosen fdcId is an incomplete record — search again or pick a different dataType; if no candidate resolves, say "FDC record incomplete" rather than 0.
- Calling a 0% RDA result "significant" / "meaningful," OR emitting any qualitative label ("meaningful contribution", "good source", "covers daily") without the numeric %RDA printed in the same sentence. Gate the significance label on the computed %RDA (<10% low, 10–20% contributes, ≥20% significant / "good source") and ALWAYS show the %RDA number.
- **Omitting the unit in the final answer.** Always print `<amount> <unit>` (e.g. `521 mg`, `15 mcg`, `8.2 mg`). A bare number like "Provides 521.0 (15% RDA)" is a defect — the unit is part of the answer.
- **Bailing with "Label nutrient data unavailable" after reading only labelNutrients.** The foodNutrients*servingSize/100 fallback is mandatory before declaring a record incomplete.
- Mixing IU and µg for vitamin D. Always read `unitName`; convert with 1 µg = 40 IU before comparing to RDA.
- Trusting the first `/foods/search` hit without checking `description` + `dataType` matches the user's food.
