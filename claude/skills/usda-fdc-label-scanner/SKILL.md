---
name: usda-fdc-label-scanner
description: Use when a user with a chronic condition (prediabetes, hypertension, PCOS, CKD, high cholesterol) asks whether a specific packaged food is a safe choice — fetches FDC detail, cross-references added-sugar/fiber/net-carbs/sodium/saturated-fat against the condition's clinical thresholds, returns plain-language verdict + confidence + ranked alternatives.
---

# USDA FDC — Smart Label Scanner (Health-Condition Risk)

## When to Use

The user discloses a chronic condition and asks a go/no-go question about a packaged product. Examples: "I'm prediabetic — are Nature Valley Oats 'n Honey bars a good snack?", "I have hypertension, is this canned soup OK?", "PCOS-friendly: Chobani flip yogurts yes or no?". The user wants a plain-language verdict, not just nutrient numbers.

## API Surface

- **Endpoint:** `GET /food/{fdcId}?format=full` (optionally preceded by `GET /foods/search` to resolve product name)
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read:** `labelNutrients.{sugars, addedSugars, fiber, sodium, saturatedFat, transFat, carbohydrates, calories, protein}` (note: `addedSugars` is PLURAL; `transFat`/`potassium`/`phosphorus` are frequently absent even on Branded records), `foodNutrients` per-100g backstop, `servingSize`, `servingSizeUnit`, `householdServingFullText`, `ingredients`

## Condition rule sets (per serving)

| Condition | Watch-out thresholds | Curated alternatives (pick 2–3, rank by fit) |
|---|---|---|
| Prediabetes / type-2 risk | added sugar > 6 g → red; fiber < 3 g AND net carbs > 20 g → red; ratio (net_carbs / fiber) > 10 → amber | Kashi GOLEAN Original cereal; Fage Total 0% plain Greek yogurt; KIND Dark Chocolate Nuts & Sea Salt bar; Magic Spoon cereal |
| Hypertension (DASH-aligned) | sodium > 400 mg/serving → red (NO downgrade for marketing claims like 'Low Sodium'); 230–400 mg/serving → amber | Amy's Low Sodium Lentil Soup; Health Valley No Salt Added Minestrone; unsalted almonds; fresh fruit |
| PCOS / insulin-resistance | added sugar > 8 g → red; saturated fat > 5 g → amber; trans fat > 0 → red | Siggi's 4% plain Icelandic yogurt; Fage Total 2% plain; Bob's Red Mill steel-cut oats |
| High cholesterol | saturated fat > 5 g → red; trans fat > 0 → red; dietary fiber ≥ 5 g → green signal | Quaker Old-Fashioned Oats; Fage Total 0%; Cheerios (original); raw almonds |
| CKD stage 3+ | sodium > 200 mg → red; potassium > 300 mg → amber; phosphorus > 150 mg → amber | Low-sodium homemade broth; white rice; apples; cucumber slices |

**Verdict arbitration (multi-condition questions):** compute each condition's verdict independently, then the overall verdict is the WORST across conditions using strict ordering RED > AMBER > UNKNOWN > GREEN. State each per-condition verdict, then the combined. Never emit hybrid strings (`GREEN-AMBER`, `AMBER-UNKNOWN`, etc.).

**Threshold discipline:** when a measured value crosses a RED threshold, the verdict is RED. Marketing claims ('Low Sodium', 'Light', 'Reduced'), product category norms, or proximity-to-threshold narrative are NEVER grounds to downgrade RED → AMBER.

## Minimal Happy Path

```bash
# Fetch full Branded detail and extract per-serving label nutrients
curl -s "https://api.nal.usda.gov/fdc/v1/food/1955793?format=full&api_key=${USDA_FDC_API_KEY}" \
  | jq '{serving: .servingSize, unit: .servingSizeUnit, label: .labelNutrients}'
```

## API Quirks

- **`labelNutrients` is Branded-only AND per serving.** `foodNutrients` is per 100 g on Foundation/SR Legacy/Survey and ALSO stored per 100 g on Branded. If the user's question is about a Branded packaged food, prefer `labelNutrients` — it matches the printed nutrition-facts panel the user is actually reading.
- **Rate limits.** The FDC API returns `429 OVER_RATE_LIMIT` under bursty usage (observed ~once per 4–6 calls). On 429: sleep 60 s then retry once; on a second 429, sleep 120 s and retry once more; on a third, abort with `UNKNOWN` + confidence 0% citing rate-limit exhaustion. Never infer nutrient values from priors when a 429 blocks the fetch.
- `labelNutrients` sub-objects are shaped `{value: number}` — e.g. `labelNutrients.sugars.value`. The added-sugar key is `addedSugars` (plural), NOT `addedSugar`. Missing keys are common: `addedSugars`, `transFat`, `potassium`, `phosphorus` are frequently absent and `sodium`/`saturatedFat`/`fiber` may also be missing on older Branded entries.
- `labelNutrients.calories` vs `foodNutrients[208]` may differ slightly due to rounding — prefer the labelNutrients value for display, foodNutrients for calculation.
- **Net carbs** for the prediabetes rule = `labelNutrients.carbohydrates.value − labelNutrients.fiber.value`. If fiber is missing, say so explicitly. **Round EVERY numeric value shown to the user to exactly 1 decimal place** — BOTH raw nutrients (`0.424` → `0.4`, `7.68` → `7.7`, `2.99` → `3.0`, `40.8` → `40.8`) AND derived values (net-carbs `24.01` → `24.0`, ratio `8.03` → `8.0`, `4.47` → `4.5`, `8.99` → `9.0`). No exceptions for 2nd/3rd decimals that 'look precise'. Format `None` as `unknown` — never `Noneg`/`Nonemg`. When a value IS 0, show `0.0 g` or `0 mg` with a space — never bare `0g`.
- 404 on a nonexistent fdcId returns an **empty body** (not JSON). Check `status == 404` before parsing.
- **Missing-nutrient fallback.** When a required `labelNutrients.<field>.value` is null/absent, fall back to `foodNutrients[]` per-100g and scale by `servingSize` (grams) before applying the rule. For Branded records with NO `labelNutrients` at all (older entries), use `foodNutrients` per-100g scaled by `servingSize`. Relevant nutrient numbers: sodium=1093, potassium=1092, phosphorus=1091, saturated fat=1258, trans fat=1257, fiber=1079, added sugars=1235, total sugars=2000, carbohydrates=1005.
- **Modern-record missing-field caveat.** Even 2023–2024 Branded records (Clif Bar 2507658, Tropicana 2501658, Kashi GOLEAN 760154, Nature Valley, KIND) routinely lack `addedSugars` — do NOT treat this as surprising or a data-quality red flag; apply the total-sugars-upper-bound rule silently and cap confidence at 65%.
- **MANDATORY output envelope (every response, no exceptions — even GREEN, even single-product, even comparative/dual-condition):** (1) `VERDICT: {GREEN|AMBER|RED|UNKNOWN}` — exactly one token from that set, NEVER hybrids like `AMBER-GREEN`, `GREEN-AMBER`, `AMBER-UNKNOWN`; (2) `Confidence: NN%` (0–100); (3) `Alternatives:` a ranked list of 2–3 specific named products from the curated table below, NEVER generic advice like 'air-popped popcorn' or 'check the manufacturer'. Omission of any of the three is a skill failure.
- **Abstain-on-null policy.** If ALL nutrients required by the user's condition rule are missing after the per-100g fallback, return verdict `UNKNOWN` (NOT `GREEN`) with confidence ≤ 30%, and state which fields were unrecoverable. If ≥1 but not all required nutrients are recoverable, cap confidence at 60% and LIST the specific missing `labelNutrients.<field>` names in the response body. Never issue `GREEN` when every rule input is `None`. **Per-condition per-nutrient abstain (hard rule):** if ANY single required nutrient for a condition is `None` after fallback, that condition's branch is `UNKNOWN` and overall confidence is capped at 60% — NOT GREEN, regardless of how safe the other nutrients look. Specifically: CKD branch with phosphorus OR potassium missing → UNKNOWN (not GREEN even with sodium 144 mg); high-cholesterol with transFat unknown AND no hydrogenated-oil ingredient signal → UNKNOWN; PCOS/prediabetes branches where addedSugars is null fall under the total-sugars-upper-bound rule below, not abstain.
- **Ingredient-text inspection.** Scan `ingredients` (case-insensitive) for trans-fat signals: `partially hydrogenated`, `interesterified`, `hydrogenated` → treat as `trans fat > 0` (red for PCOS / high cholesterol) even when `labelNutrients.transFat.value == 0`.
- **Total-sugars-as-upper-bound for addedSugars.** When `labelNutrients.addedSugars` is null but `labelNutrients.sugars` (total sugars) is present, use total sugars as a conservative UPPER BOUND for added sugars: if total sugars already exceeds the condition's added-sugar red threshold (6 g prediabetes, 8 g PCOS), return RED with confidence capped at 65%. If total sugars is BELOW the threshold, you cannot conclude GREEN from that alone — state the distinction is unknown and cap confidence at 60%. Exception: records whose description/ingredients indicate a plain/unsweetened product (e.g., 'plain', 'unsweetened', no sugar in ingredients list) — total sugars is lactose/fructose from the base food, NOT added; treat addedSugars as 0 with a note.

## Common Mistakes

- Reading `labelNutrients.addedSugar` (singular) — the real key is `addedSugars` (plural).
- Returning `GREEN` when every rule-input nutrient is `None`; correct behavior is `UNKNOWN` verdict with ≤30% confidence.
- Rendering missing values as `Noneg` / `Nonemg` by concatenating the unit onto `None` — use `unknown` instead.
- Displaying ANY numeric (raw or derived) at more than 1 decimal — `0.424`, `7.68`, `2.99`, `8.03`, `24.01`, `4.47` must all round to 1 decimal before display.
- Ignoring `ingredients` text for trans-fat cues (`partially hydrogenated`, `interesterified`).
- Not falling back to `foodNutrients[]` per-100g × servingSize when `labelNutrients` fields are absent or the record predates labelNutrients entirely.
