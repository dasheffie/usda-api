---
name: usda-fdc-cart-optimization
description: Use when a user lists multiple packaged items in a proposed meal or grocery cart and asks whether the combination fits a daily nutrient limit (sodium, added sugar, saturated fat) — batch-fetches, aggregates the constraint nutrient, flags per-item offenders, and suggests 1:1 swaps via a follow-up search.
---

# USDA FDC — Cart / Meal Threshold Optimization

## When to Use

The user presents 2+ branded items together (a meal plan, a grocery cart, a school-lunch plan) and asks whether the combined nutrient total fits a daily ceiling. Different from `usda-fdc-daily-intake-tally` because here the skill must **also** suggest a lower-impact 1:1 swap for the worst offender. Examples: "Does this meal fit my low-sodium diet — Campbell's soup + Oscar Mayer turkey + Lay's chips?", "Is this grocery cart under my added-sugar ceiling?".

## API Surface

Two-stage flow:

1. **`POST /foods`** batch on the cart's fdcIds, `format: "full"` — aggregate the tracked nutrient.
2. **`POST /foods/search`** with `dataType: ["Branded"]` for each offender's category — find 1-2 lower-impact alternatives.

- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read:** `foodNutrients`, `labelNutrients`, `description`, `brandOwner`, `brandedFoodCategory`, `servingSize`

## Minimal Happy Path

```bash
# Aggregate sodium across 3 cart items
curl -s -X POST "https://api.nal.usda.gov/fdc/v1/foods?api_key=${USDA_FDC_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"fdcIds":[2346393,1954907,2700929],"format":"full"}' \
  | jq '[.[] | {desc: .description, sodium_per_serving_mg: (.labelNutrients.sodium.value // null)}]'

# Follow-up: low-sodium canned soup alternatives
curl -s -X POST "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=${USDA_FDC_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"query":"low sodium chicken noodle soup","dataType":["Branded"],"pageSize":10}'
```

## API Quirks

- **Two response shapes to handle:** `POST /foods` → bare array. `POST /foods/search` → `{totalHits, foods: [...]}` envelope.
- **Batch cap = 20** on `POST /foods`. If the cart has more items, chunk.
- **Prefer `labelNutrients` (per serving) over `foodNutrients` (per 100 g) when available** — the user's mental model is "per serving as eaten", and labelNutrients matches the box.
- `labelNutrients` sub-objects are `{value: number}` — access as `.labelNutrients.sodium.value`, and guard against missing keys.
- **Offender detection:** rank cart items descending by their contribution to the constraint nutrient. The top 1-2 are the offenders to swap.
- **Swap search:** the query keyword comes from the offender's `brandedFoodCategory` — e.g. offender category "Canned Soup" → search `"low sodium {category}"`. Filter candidates where `labelNutrients.<tracked>.value < offender_value`.
- Always return the arithmetic: "total = X mg, limit = Y mg, overage = X − Y, driven by item Z (W mg alone)". Users benefit from seeing the math.
- Confidence scoring matters — if `labelNutrients` is missing on one item and you fall back to `foodNutrients × servingSize / 100`, disclose the estimate's lower confidence.

## Common Mistakes

(to be populated during the refinement loop)
