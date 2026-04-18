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
- Preceded by `GET /foods/search` per candidate to resolve product name → fdcId
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
| Blood-sugar control | Added sugar, net carbs | Fiber (↑) |
| Kidney disease (CKD) | Sodium, potassium, phosphorus | Protein (moderate) |

## API Quirks

- **Batch `POST /foods` is cheaper than 2-3 parallel GETs** in terms of API quota (one quota hit vs N hits). Prefer the batch call.
- **`POST /foods` returns a bare array**, no envelope. Parse indices as the same order as the input fdcIds.
- **Per-100g vs per-serving:** `labelNutrients` is per serving and matches the printed box. `foodNutrients` is per 100 g. Use **labelNutrients for display and comparison** — users compare what they'll eat, not per-100 g.
- **`labelNutrients` sub-objects are `{value: number}`** — `.labelNutrients.calories.value` is the number; guard against missing keys (older Branded entries may lack `addedSugar`).
- **If one product is Branded and another is SR Legacy (no labelNutrients)**, the comparison becomes lopsided — use foodNutrients × servingSize/100 for the SR Legacy item and disclose the basis.
- Always state the **serving size** each candidate was measured at — "per 100 g" comparisons are misleading if user-perceived servings differ. If Halo Top's serving is 2/3 cup and Ben & Jerry's is 1/2 cup, disclose both.
- **Tie breakers:** when the two candidates are nutritionally close, fall back to ingredient cleanliness (count commas in the `ingredients` string; fewer is simpler).
- Always supply a **third "even-stronger-strategy" option** (e.g. "Fage Total 0% yogurt with fresh fruit" for an ice-cream comparison) so the user sees a better alternative beyond the binary choice.

## Common Mistakes

(to be populated during the refinement loop)
