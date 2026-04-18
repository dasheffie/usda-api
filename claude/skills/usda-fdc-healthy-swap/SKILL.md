---
name: usda-fdc-healthy-swap
description: Use when a user loves a specific branded product but wants a 1:1 healthier replacement that preserves the eating experience — fetches the original's profile, then searches Branded foods in the same category for cleaner-ingredient or better-macro alternatives and ranks them.
---

# USDA FDC — Healthy Swap Engine (1:1 Branded Replacement)

## When to Use

The user names a specific commercial product they enjoy (Doritos, Oreos, Cheez-Its, Haagen-Dazs, Coca-Cola, etc.) and asks for a healthier replacement that still scratches the same itch. Examples: "I love Doritos but want something cleaner — what should I switch to?", "Healthier version of Oreos?", "Alternative to seed-oil potato chips?". The output is 2-3 ranked 1:1 swaps with an explicit "here's what improves" summary.

## API Surface

Two-endpoint flow:

1. **`GET /food/{fdcId}`** on the original product — to learn the food category, ingredient profile, and target nutrient baselines.
2. **`POST /foods/search`** with `dataType: ["Branded"]` + a query keyword inferred from the original's `brandedFoodCategory` or `foodCategory` — to find candidates.

- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read on original:** `description`, `brandOwner`, `brandedFoodCategory`, `ingredients`, `labelNutrients`, `servingSize`
- **Key fields read on candidates:** same, plus `foodNutrients` for cross-comparison

## Minimal Happy Path

```bash
# 1. Fetch the Doritos Nacho Cheese profile
curl -s "https://api.nal.usda.gov/fdc/v1/food/2705988?api_key=${USDA_FDC_API_KEY}" \
  | jq '{category: .brandedFoodCategory, ingredients, label: .labelNutrients}'

# 2. Search Branded "tortilla chips" for candidates
curl -s -X POST "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=${USDA_FDC_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"query":"tortilla chips","dataType":["Branded"],"pageSize":30}' \
  | jq '.foods[] | {fdcId, description, brand: .brandOwner}'
```

## API Quirks

- **Ingredient cleanliness** is a substring check on `ingredients` — e.g. candidates containing `"SOYBEAN OIL"`, `"SUNFLOWER OIL"` are worse (seed oils) than `"AVOCADO OIL"` or `"OLIVE OIL"`. Substring matches must be case-insensitive.
- **Same-category search keyword** should come from the original's `brandedFoodCategory` string, lower-cased, stripped of brand-specific tokens. E.g. original category `"Tortilla & Corn Chips"` → search keyword `"tortilla chips"`.
- Filter candidates to **exclude the original brand**: drop results where `brandOwner` matches the original's brandOwner (unless the user wants "healthier from same brand").
- **Rank by a composite score:** lower added sugar (539), higher protein (203), higher fiber (291), absence of seed-oil ingredients, fewer total ingredients (count commas in ingredients string). Disclose the ranking rule in the answer.
- `labelNutrients` is per-serving — when comparing originals to candidates, use labelNutrients for both so the basis matches.
- **Portion-control warning:** the skill should always add "portion control still matters" — a cleaner product eaten in excess can still be worse than a small serving of the original.

## Common Mistakes

(to be populated during the refinement loop)
