---
name: usda-fdc-product-comparison
description: Use when a user is choosing between 2-3 specific packaged products (e.g. Halo Top vs Ben & Jerry's) and asks which is better for a named goal (weight loss, muscle gain, heart health) — fetches each candidate's profile in parallel and compares key metrics, explaining the dominant nutritional lever.
---

# USDA FDC — Best Option Side-by-Side Comparison

## When to Use

The user names 2-3 specific packaged products by brand and product name and asks "which is better for [my goal]?". Different from `usda-fdc-healthy-swap` (which searches for alternatives); here the candidates are explicitly supplied. The skill fetches each one in parallel, compares the relevant metrics for the user's goal, and picks a winner with one-sentence reasoning ("Halo Top wins because calorie density is the primary lever for fat loss").

## API Surface

- **Primary endpoint:** `GET /food/{fdcId}?format=full` on each candidate (run in parallel — 2-3 concurrent calls)
- **Optional batch alternative:** `POST /foods` with `{"fdcIds": [id1, id2, id3], "format": "full"}` — single request, no concurrency needed
- Preceded by `GET /foods/search` per candidate to resolve product name → fdcId. **Validate each hit BEFORE batch-fetching**: check that the top hit's `description` contains the expected product-form noun (e.g. 'peanut butter', 'yogurt', 'cereal', 'burger patty', 'protein bar', 'beef stick', 'almond butter') — not a lookalike (Teddie PB → 'Teddy Grahams', Dr. Praeger's burger → 'Veggie Littles', Chomps → 'Bacon and beef sticks', RXBAR → 'CHOCOLATE SEA SALT ALMONDS', Trader Joe's cereal → 'multigrain high fiber cookie', All-Bran → 'Roll, bran', Noosa yogurt → 'Rhubarb'). If the form-noun mismatches, trigger the recovery ladder BEFORE spending the batch quota. **Search recovery ladder (MANDATORY — never accept a form-mismatched top hit):** (1) add `dataType=Branded&brandOwner=<brand>` to force a branded hit; (2) drop the brand and search `<form-noun> <flavor>` (e.g. `RXBAR Chocolate Sea Salt` → `protein bar chocolate`, `Quest Cookie Dough` → `protein bar cookie dough`, `Teddie Peanut Butter` → `peanut butter natural`, `Justin's Almond Butter` → `almond butter`, `Halo Top` → `ice cream light`, `Quaker Instant Oatmeal` → `oatmeal instant`, `Purely Elizabeth` → `granola` or `oatmeal`); (3) try `dataType=Foundation,SR Legacy` for generics; (4) use a category synonym (e.g. `FreshMarket Greek Yogurt` → `greek yogurt plain`, `Sargento Reduced Fat Cheddar` → `cheddar reduced fat`). **Hard reject patterns: ingredient-as-product (RXBAR → 'CHOCOLATE SEA SALT ALMONDS'), beverage-as-food (Halo Top → 'ENLIGHTEN MINT LITE MATCHA TEA'), commodity-as-product (Nature Valley → 'Crackers', granola → 'Prune puree'), brand-collision (Sargento → 'KRAFT FREE Singles'). If the resolved description's brandOwner does not match the requested brand AND the form-noun mismatches, REJECT and ladder — do NOT proceed with the comparison even if numbers come back.** **Deduplicate fdcIds before the batch call** — if two candidate searches resolve to the same id (seen on Justin's/Artisana → 2707533, Clif flavors → 2708118, 365/Oatly → 2705412), re-search the dupe with a tighter flavor/variant qualifier or substitute the closest distinct branded entry and disclose. Never stop at <N distinct candidates — substitute a generic same-category entry and disclose the substitution in the answer. **Never silently accept a wrong-brand/wrong-form hit as a candidate.** Validation pseudocode: `if expected_brand and expected_brand.lower() not in (hit.brandOwner or '').lower() and expected_brand.lower() not in hit.description.lower(): REJECT`; `if expected_form_noun not in hit.description.lower(): REJECT`. A REJECT triggers the ladder, not a proceed.
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read:** `description`, `brandOwner`, `labelNutrients`, `servingSize`, `servingSizeUnit`, `foodNutrients[]` (for anything not in labelNutrients)

## Minimal Happy Path

```bash
# Compare 2 ice creams in one batch call
curl -s -X POST "https://api.nal.usda.gov/fdc/v1/foods?api_key=${USDA_FDC_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"fdcIds":[2705988,2705994],"format":"full"}' \
  | jq '[.[] | {desc: .description, brand: .brandOwner, serving: .servingSize, cal: .labelNutrients.calories.value, protein: .labelNutrients.protein.value, sugar: .labelNutrients.sugars.value, satFat: .labelNutrients.saturatedFat.value}]'
```

## Goal → primary lever mapping

| User goal | Primary lever | Secondary levers |
|---|---|---|
| Weight loss / fat loss | Calories per serving | Sugar, saturated fat, protein (higher = satiety) |
| Muscle gain | Protein per serving | Calories, carbs (timing) |
| Heart health | Saturated fat, sodium | Fiber (↑), added sugar (↓) |
| Blood-sugar control | Total sugar (proxy for added) + net carbs | Fiber (↑) |
| Kidney disease (CKD) | Sodium, potassium, phosphorus | Protein (moderate) |
| Kids / kid-friendly | Ingredient simplicity (≤5 items, no artificial colors/HFCS) | Calories per serving, added sugar, sodium |
| User-named custom metric (e.g. 'per 100 kcal') | Compute the requested ratio (nutrient ÷ calories × 100) | Note ratio basis + serving-size asymmetry |

**Added-sugar caveat:** FDC's `labelNutrients.addedSugar` is missing on most Branded entries and absent on all SR Legacy/Survey entries. For blood-sugar control, use total sugars (nutrient 2000) as the proxy and disclose 'total sugars used; added-sugar not in FDC for this entry'.

**Note:** `labelNutrients` does NOT expose potassium or phosphorus on most Branded entries — for CKD comparisons, read `foodNutrients[]` (nutrient numbers 1092=K, 1091=P) directly and rescale by servingSize/100. Do not return "missing nutrient" without checking foodNutrients[] first.

**servingSize=0 handling:** SR Legacy / Survey / commodity entries (plain oats, generic yogurt, 'Oat milk', 'Roll, bran', raw Quaker oats) frequently have `servingSize=0` and no `labelNutrients`. Treat `foodNutrients` as per-100 g and **report values per 100 g explicitly** — do NOT invent a serving and do NOT abort with 'insufficient data'. If BOTH sides have servingSize=0, just compare per-100g directly using foodNutrients (this is the simplest case, not the hardest). If the paired product has a real label serving, normalize BOTH sides to per 100 g for the comparison and state 'compared per 100 g because [product] is an SR Legacy entry with no label serving'. If `foodNutrients` itself is empty/None for the required nutrient (seen on bare-oat commodity entries for calories/sugar/fiber), explicitly report 'FDC entry lacks [nutrient] data' and swap in a Branded equivalent via the recovery ladder rather than comparing against null.

## API Quirks

- **Batch `POST /foods` is cheaper than 2-3 parallel GETs** in terms of API quota (one quota hit vs N hits). Prefer the batch call.
- **`POST /foods` returns a bare array**, no envelope. Parse indices as the same order as the input fdcIds.
- **Per-100g vs per-serving:** `labelNutrients` is per serving and matches the printed box. `foodNutrients` is per 100 g. Use **labelNutrients for display and comparison** — users compare what they'll eat, not per-100 g.
- **`labelNutrients` sub-objects are `{value: number}`** — `.labelNutrients.calories.value` is the number; guard against missing keys (older Branded entries may lack `addedSugar`).
- **labelNutrients is sparse and unreliable** — many Branded entries omit `protein`, `sodium`, `saturatedFat`, `sugars`, `fiber`, `calories`, etc. Never abort on a missing label key. Always fall back to `foodNutrients[]` (per 100 g) and rescale: `value_per_serving = nutrient.amount * servingSize / 100`. Map common nutrient numbers: 1003=Protein, 1004=Total Fat, 1005=Carbs, 1008=Calories(kcal), 1079=Fiber, 1087=Calcium, 1089=Iron, 1092=Potassium, 1091=Phosphorus, 1093=Sodium, 1253=Cholesterol, 1258=SatFat, 2000=Sugars.
- **If one product is Branded and another is SR Legacy (no labelNutrients)**, the comparison becomes lopsided — normalize BOTH sides to per-100 g (use foodNutrients directly on the SR Legacy item; divide Branded labelNutrients by servingSize/100) and disclose the basis. This is the ONLY honest apples-to-apples when servingSize=0 on one side.
- Always state the **serving size** each candidate was measured at — "per 100 g" comparisons are misleading if user-perceived servings differ. If Halo Top's serving is 2/3 cup and Ben & Jerry's is 1/2 cup, disclose both.
- **Tie breakers:** when the two candidates are nutritionally close, fall back to ingredient cleanliness (count commas in the `ingredients` string; fewer is simpler). If `ingredients` is empty/missing on one or both sides (common on SR Legacy, store-brand, and some Branded entries like Kraft Singles, Goldfish, Siggi's, Nancy's), state 'ingredient comparison skipped — FDC ingredient field empty for [product]' and decide on the primary-lever nutrient delta alone rather than silently inferring cleanliness.
- Always supply a **third "even-stronger-strategy" option** (e.g. "Fage Total 0% yogurt with fresh fruit" for an ice-cream comparison) so the user sees a better alternative beyond the binary choice.

## Common Mistakes

- **Reporting a winner whose `description`/`brandOwner` does not match the user's requested product.** If the answer string would name a different brand or a different food category than the user asked about (e.g. user said 'Sargento' and winner is 'KRAFT', user said 'Halo Top' and winner is 'matcha tea', user said 'Nature Valley' and winner is 'Crackers', user said 'granola' and winner is 'Prune puree'), STOP — re-run search with the recovery ladder. Never let the answer string contain a brand/category the user did not ask for.
- **Aborting on missing label nutrient.** `labelNutrients.protein/sodium/sugars/saturatedFat/fiber` are often absent on Branded entries. Always fall back to `foodNutrients[]` (per 100 g) × `servingSize/100` before reporting "missing nutrient". Saw this on protein bars (Quest/Clif/RXBAR/Kirkland), oat milks (Chobani/Elmhurst/Califia/Oatly/365), nut butters (Jif/Justin/Once Again/Nutella), crackers (Triscuit/Wheat Thins/Keebler/Mary's Gone), frozen meals (Evol/Amy's), milks (Silk/Fairlife/Horizon/Organic Valley), oats (Quaker/Bob's/Kodiak), and chips (Kettle/Popchips/Boom Chicka). **'Insufficient nutrient data' is FORBIDDEN as a final answer when foodNutrients[] has the required nutrient.** If you computed a value via the per-100g fallback (even if labeled 'may be inaccurate'), REPORT IT with the disclosure ('computed from foodNutrients per-100g; not from on-label panel') — the user wants a comparison, not an abort. The only legitimate 'insufficient data' is when foodNutrients[] itself lacks the nutrient on BOTH sides; in that case substitute via the recovery ladder before giving up.
- **Stopping when one of N candidates returns no search hit.** Apply the search-recovery ladder (drop brand → loosen dataType → category synonym) and substitute a generic same-category entry, disclosing the swap.
- **Per-100-calorie protein density** for muscle-gain bar comparisons requires both `protein` and `calories`; if either is label-absent, compute from `foodNutrients` 1003 and 1008 — do not refuse the question.
- **Confidence disclosure for store-brand entries.** When a 365/Kirkland/Costco-style entry has sparse nutrients, state the confidence gap explicitly ("365 entry only reported calories and fat; sodium estimated from foodNutrients per-100g") rather than failing silently.
- **Store-brand vs name-brand collision.** FDC's commodity aggregation (e.g. 'Oat milk' id 2705412) often serves BOTH the store brand and the name brand from the same entry, making brand-level comparison impossible. When the two candidate searches resolve to the same id, refuse the brand comparison and say 'FDC aggregates [category] across brands at id [X]; no per-brand formulation data available — compare the actual Nutrition Facts panels on-pack'. Do not fabricate a differential.
