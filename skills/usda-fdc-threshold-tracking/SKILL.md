---
name: usda-fdc-threshold-tracking
description: Use when a user names their current intake of a constrained nutrient and a candidate next food, and asks whether the candidate keeps them under their daily target — fetches the candidate's contribution, projects the running total, returns pass/fail with tight-margin warnings and same-category alternatives on fail.
---

# USDA FDC — Running-Total Threshold Projection

## When to Use

The user has a daily nutrient budget (e.g. 25 g added sugar), reports their current day's intake (e.g. "I've had 15 g already"), and names a candidate food to possibly eat next. The skill fetches the candidate's nutrient contribution, projects `current + candidate` vs the daily target, returns pass/fail with margin. If over, suggests same-category alternatives.

## API Surface

- **Primary endpoint:** `GET /food/{fdcId}?format=full` on the candidate (single fetch)
- Preceded by `GET /foods/search` if the candidate is named but fdcId is unknown. **Verify the top hit's `description` and `brandedOwner` contain the brand tokens from the user's query before fetching `/food/{id}`.** FDC fuzzy-search will happily return an unrelated product (e.g. a Yoplait yogurt for a query of "RXBar Blueberry"), and a generic/FNDDS match (e.g. fdcId 170335 for "Chipotle burrito steak") will lack `labelNutrients` entirely. **Add `&dataType=Branded` to the search URL when the user named a specific brand** — this filters out SR Legacy / FNDDS hits at the source (e.g. fdcId 170912 was an SR Legacy Chobani entry with no added-sugar field). If the top hit's dataType is `Foundation`/`SR Legacy`/`Survey (FNDDS)` and a `Branded` match exists further down, prefer the Branded one.
- Optional follow-up: `POST /foods/search` for same-category alternatives when the projection fails
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read:** `labelNutrients.<tracked>.value`, fallback to `foodNutrients` per-100g × `servingSize/100`, `description`, `brandedFoodCategory`

## Minimal Happy Path

```bash
# User: "15g added sugar so far, can I have Yoplait Original Strawberry Yogurt?"
curl -s "https://api.nal.usda.gov/fdc/v1/food/2587575?format=full&api_key=${USDA_FDC_API_KEY}" > /tmp/food.json
# Step 1: try labelNutrients (per-serving, matches the box)
jq '.labelNutrients.addedSugar.value' /tmp/food.json
# Step 2: if null/missing, ALWAYS fall back — DO NOT return NO DATA yet.
# Extract per-100g from foodNutrients by nutrient number, multiply by servingSize/100.
jq '(.foodNutrients[] | select(.nutrient.number=="539") | .amount) as $p100
    | ($p100 * (.servingSize // 100) / 100)' /tmp/food.json
# Project: 15 + 12 = 27 g, target 25 g, overage = 2 g → tight overage warning
```

**Mandatory three-step lookup — DO NOT SHORT-CIRCUIT.** (1) `labelNutrients.<key>.value`. (2) `foodNutrients[]` by nutrient.number × `servingSize/100`. (3) **If both miss on fdcId #1, you MUST re-issue `/foods/search` and fetch fdcId #2 before emitting `NO DATA`.** Branded catalog coverage is spotty; pick the next Branded hit whose `description` contains the brand tokens, or broaden the query (drop the flavor word, keep the brand; if still empty, drop the brand) and retry. `NO DATA` is only legal after at least TWO distinct fdcIds both miss on both fields, and the answer MUST disclose both fdcIds tried. **An answer citing one fdcId and saying NO DATA is invalid output** — this failed on Yoplait (760432, 2233965) and Ritz Bits (2089463) in the transcript.

## Tracked-nutrient + typical target cheat-sheet

| Nutrient | `labelNutrients.<k>.value` | `foodNutrients` nutrient.number fallback | **Output unit** | Typical daily target |
|---|---|---|---|---|
| Added sugar | `addedSugar.value` | `"539"` (NOT `"269"` total sugar) | **g** | 25 g WHO / 36 g AHA M |
| Sodium | `sodium.value` | `"1093"` (mg) | **mg** | 2,300 mg FDA / 1,500 mg AHA |
| Saturated fat | `saturatedFat.value` | `"1258"` (g) | **g** | < 13 g on 2,000 kcal |
| Total carbs | `carbohydrates.value` | `"1005"` (g) | **g** | varies (keto ≤ 50 g/day) |
| Calories | `calories.value` | `"1008"` (kcal, Energy) | **kcal** | user-supplied |

**Always label arithmetic with the unit from the "Output unit" column — never default to `g`.** Sodium is `mg`, calories are `kcal`. The arithmetic line MUST read `1500 mg + 480 mg = 1980 mg` (not `1500g + 480g = 1980g`). Unit-mismatched output was the single most common transcript failure (8 of 20 answers mislabeled).

## Pass/fail verdict structure

The skill's output must always include:

1. **Arithmetic:** `current <unit> + candidate <unit> = projected <unit>` — unit comes from the cheat-sheet Output-unit column (`mg` for sodium, `kcal` for calories, `g` for sugars/fat/carbs). Do NOT hard-code `g`.
2. **Verdict:** `PASS` / `TIGHT_OVER` / `CLEAR_OVER` based on margin
3. **Guidance:**
   - PASS with margin > 10 % of target → approve with remaining-budget note
   - **TIGHT_PASS (margin ≤ 10 % of target, still under)** → approve but warn "this lands you within 10 % of your limit; leave headroom for the rest of the day" (e.g. 1489.9 mg vs 1500 mg target = 0.7 % headroom → tight-margin warning required)
   - TIGHT_OVER (≤ 10 % over) → "acceptable once but not a daily habit" **AND name 2 cleaner same-category swaps**
   - CLEAR_OVER (> 10 % over) → **MUST name 2 cleaner same-category swaps** (e.g. Chobani Zero Sugar Strawberry instead of Yoplait Original). The swap list is not optional — omitting it is a verdict-structure failure.
4. **Confidence:** `labelNutrients` present → 90-95 %; fallback to `foodNutrients × servingSize/100` → 70-80 %; missing data → disclose

## API Quirks

- **Prefer `labelNutrients` per-serving over `foodNutrients × servingSize/100`** — the user's mental model is "this serving", and labelNutrients matches the printed box.
- `labelNutrients` sub-objects are `{value: number}` — `.labelNutrients.addedSugar.value`. Older Branded entries, Foundation/SR-Legacy, and FNDDS entries **routinely omit the labelNutrients key**. Missing-key is the COMMON case, not the edge case — always run the foodNutrients fallback using the nutrient-number column in the cheat-sheet before emitting `NO DATA`. Only emit `NO DATA` if both paths return null/absent, and in that case disclose which nutrient number was searched.
- **Nutrient numbers are strings.** Added sugar = `"539"`, total sugar = `"269"` — they are DIFFERENT metrics. The user almost always cares about added sugar (539) when tracking blood-sugar impact.
- **404 on nonexistent fdcId returns an empty body** (no JSON). Check `status == 404` before parsing.
- Serving-size conversions are only safe when `servingSizeUnit == "g"` or `"ml"`. For household units (e.g. `"TBSP"`) without a gram weight, disclose the approximation.
- Same-category swap search: use `brandedFoodCategory` as the search keyword with a "low sugar" or "zero sugar" prefix — e.g. category "Yogurts & Cultured Dairy" + offender's added-sugar value → search `"zero sugar yogurt"`.
- **Swap search fires on ANY non-PASS verdict, including `TIGHT_OVER`.** Do not gate alternatives behind `CLEAR_OVER` — the user asked for them on any fail, and a one-gram overage still warrants naming 2 cleaner options.
- Always quote both the user's **current** intake and the candidate's **projected** total so they can verify the math.

## Common Mistakes

- **Bailing on `NO DATA` after only checking `labelNutrients`.** The fallback to `foodNutrients` by nutrient number (see cheat-sheet) is mandatory, not optional. 14 of 17 probe failures were this single mistake.
- **Bailing on `NO DATA` after only ONE fdcId.** If both `labelNutrients` and the `foodNutrients`-by-number fallback are absent on the first fdcId, retry with the next ranked Branded hit (or a broadened query that drops the flavor/sub-variant token). Starbucks, KIND, and Chobani entries in the transcript had at least one fdcId with the field and one without — picking the wrong one and stopping is the failure mode, not missing data globally.
- **Trusting the first search hit.** Fuzzy search can return a completely different brand — always confirm the brand/product tokens appear in the hit's `description` before calling `/food/{id}`.
- **Forgetting multi-nutrient questions.** When the user names two tracked nutrients (e.g. added sugar AND saturated fat for ice cream), fetch once and report both projections; do not stop after the first.
- **Skipping swap search on `TIGHT_OVER`.** Alternatives are requested on any fail verdict, not just `CLEAR_OVER`.
