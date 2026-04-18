---
name: usda-fdc-low-sugar-snack
description: Use when a user asks for a lower-sugar packaged alternative to a favorite snack (cookies, bars, yogurt, cereal, ice cream, candy) — searches FDC Branded foods by product category and ranks candidates ascending by total sugar or added sugar per serving.
---

# USDA FDC — Low-Sugar Snack Discovery

## When to Use

The user names a snack category they crave and asks for a commercially-available, lower-sugar alternative to what they currently eat. Examples: "I want a chocolate chip cookie with less sugar than Chips Ahoy!", "Which packaged yogurt has the least added sugar?", "Lowest-sugar granola bar I can buy at a grocery store?". Always returns Branded results so the user can actually purchase the suggestion.

## API Surface

- **Primary endpoint:** `POST /foods/search` with `dataType: ["Branded"]`
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Request body:** `{"query": "<snack keyword>", "dataType": ["Branded"], "pageSize": 25, "sortBy": "dataType.keyword"}` — then client-side sort ascending by sugars
- **Key fields read:** `description`, `brandOwner`, `foodCategory`, `foodNutrients[]` (flat, look for `nutrientNumber == "269"` total sugars and `"539"` added sugars), `servingSize`
- **Optional follow-up:** `GET /food/{fdcId}?format=full` for accurate `labelNutrients.sugars.value` + `labelNutrients.addedSugar.value` per serving

## Minimal Happy Path

```bash
# Find Branded chocolate chip cookies, pull top 25 hits, then client-side sort by sugars
curl -s -X POST "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=${USDA_FDC_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"query":"chocolate chip cookies","dataType":["Branded"],"pageSize":25}' \
  | jq '.foods | map({
      fdcId, description, brand: .brandOwner,
      sugars_per_100g: (.foodNutrients[] | select(.nutrientNumber=="269") | .value)
    }) | sort_by(.sugars_per_100g)'
```

## API Quirks

- **`dataType` in POST body MUST be an array of strings**, never a CSV. `"dataType": "Branded"` (string) silently returns all types; only `"dataType": ["Branded"]` actually filters.
- **`foodNutrients` in search results uses `value` + `nutrientNumber`**, not `amount` + `nutrient.number`. Wiring up the detail-endpoint shape instead silently returns nothing.
- **Total sugars = `nutrientNumber == "269"`.** **Added sugars = `"539"`.** They are different metrics — the user almost always cares about 539 (added sugar) for health purposes, but the API is more likely to have 269 populated. Prefer 539 when present, fall back to 269 with disclosure.
- Values in search results are **per 100 g**; for honest per-serving comparisons, either scale by `servingSize/100` or re-fetch each candidate via `/food/{fdcId}` to read `labelNutrients.sugars.value` (per serving, matches the box).
- Empty-query returns HTTP 200 with the full 468K-food database — a destructive dump. Always validate the user's snack keyword is non-empty.
- Watch for sugar-alcohol-sweetened products (erythritol, allulose, maltitol) — these DO have total sugar listed near zero but may still have "sugars" declared at 0 g + "sugar alcohols" disclosed in the ingredient list. Cross-check the `ingredients` string when the sugar count is suspiciously low.

## Common Mistakes

(to be populated during the refinement loop)
