---
name: usda-fdc-recipe-breakdown
description: Use when a user types a homemade recipe (ingredient list with quantities) and wants an exact macronutrient + micronutrient breakdown — resolves each ingredient to an SR Legacy / Foundation fdcId, batch-fetches the details, scales by user portion, and sums across ingredients.
---

# USDA FDC — Exact Homemade Recipe Breakdown

## When to Use

The user describes a meal they made from scratch with specific ingredients and quantities (e.g. "1 cup spinach + 1 banana + 1 cup whole milk", "4 oz chicken breast + 1 tbsp olive oil + 1 cup brown rice") and wants the exact nutritional profile. The skill maps each raw ingredient to its best FDC whole-food record, scales by the user's portion, and sums.

## API Surface

Two-endpoint flow:

1. **`GET /foods/search`** per ingredient to resolve name → fdcId. Prefer `dataType=["Foundation"]` or `["SR Legacy"]` for whole foods; avoid Branded unless the user specified a brand.
2. **`POST /foods`** to batch-fetch full nutrient detail for all resolved fdcIds in one call (cap: 20 items).

- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Request body (batch):** `{"fdcIds": [171706, 173944, ...], "format": "full"}`
- **Key fields read:** `foodNutrients[]` nested full-format entries for nutrient numbers `"208"`, `"203"`, `"204"`, `"205"`, `"291"`, `"539"`, `"307"`, plus micros (`"303"`, `"301"`, `"418"`, etc.)

## Minimal Happy Path

```bash
# Resolve "spinach, raw" to fdcId
curl -s "https://api.nal.usda.gov/fdc/v1/foods/search?query=spinach+raw&dataType=SR+Legacy&pageSize=3&api_key=${USDA_FDC_API_KEY}"

# Batch-fetch full details for 3 ingredients (spinach, banana, whole milk)
curl -s -X POST "https://api.nal.usda.gov/fdc/v1/foods?api_key=${USDA_FDC_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"fdcIds":[168462,173944,171265],"format":"full"}' \
  | jq '.[0] | {fdcId, description, energy: (.foodNutrients[] | select(.nutrient.number=="208") | .amount)}'
```

## API Quirks

- **`POST /foods` returns a BARE ARRAY** `[FoodItem, ...]`, not a `{foods: [...]}` envelope. Do not destructure `.foods`.
- **Batch cap = 20 fdcIds.** If the recipe has more than 20 ingredients, chunk.
- **`foodNutrients` in full format is NESTED:** `{nutrient: {number: "208", name: "Energy"}, amount: 42.5}`. Search result nutrient shape is FLAT (`{nutrientNumber, value}`) — don't mix them.
- **Values are per 100 g.** To scale by the user's portion: `portion_value = amount_per_100g × user_grams / 100`.
- **Unit conversion table** (from common recipe units):
  - 1 cup raw spinach ≈ 30 g (loose-packed)
  - 1 medium banana ≈ 118 g
  - 1 cup whole milk ≈ 244 g
  - 1 tbsp olive oil ≈ 13.5 g
  - 1 large egg ≈ 50 g
  - 4 oz chicken breast = 113 g
  - Disclose the conversion in the answer so the user can correct you.
- `"SR Legacy"` spelling has a space — `"SRLegacy"` returns 0 results.
- Some ingredients (e.g. "garlic clove") have many FDC matches — pick the most-generic SR Legacy / Foundation entry. If unsure, ask the user whether they meant "raw" vs "cooked".
- Category-header entries in `foodNutrients` have no `amount` — filter them out before summing.
- Sum ACROSS ingredients: total_protein = Σ(ingredient_protein_per_100g × ingredient_grams / 100).

## Common Mistakes

(to be populated during the refinement loop)
