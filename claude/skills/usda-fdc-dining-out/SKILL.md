---
name: usda-fdc-dining-out
description: Use when a user is at (or about to eat at) a specific fast-food chain or restaurant brand and asks which menu item best fits a diet goal (lowest-calorie, lowest-sodium, most protein, Keto-compatible) — searches FDC Branded foods for that brand and ranks options.
---

# USDA FDC — Dining Out / Fast Food Navigator

## When to Use

The user names a fast-food chain or restaurant brand (McDonald's, Wendy's, Chipotle, Starbucks, Panera, Subway, Chick-fil-A, Taco Bell, etc.) and asks for the most reasonable diet-compliant choice. Examples: "I'm at a rest stop with only a McDonald's — what's the lowest-calorie option?", "Wendy's — anything under 500 calories with 30 g protein?", "What's the least-sodium thing on the Panera menu?".

## API Surface

- **Endpoint:** `POST /foods/search` (preferred because it supports `brandOwner` + `tradeChannel` body fields) or `GET /foods/search` with query param form
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Request body:** `{"query": "<food keyword>", "dataType": ["Branded"], "brandOwner": "<exact string>", "pageSize": 25}`
- **Key fields read (from search results):** `description`, `brandOwner`, `foodCategory`, `foodNutrients[]` (flat shape with `value`/`nutrientNumber`), `servingSize`, `labelNutrients` (if pulling detail)
- Optional follow-up: `GET /food/{fdcId}?format=full` on top 2-3 candidates for `labelNutrients` per-serving values

## Minimal Happy Path

```bash
# Find McDonald's hamburger options, ranked by calories ascending
curl -s -X POST "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=${USDA_FDC_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"query":"hamburger","dataType":["Branded"],"brandOwner":"McDonald'"'"'s","pageSize":10,"sortBy":"publishedDate","sortOrder":"desc"}' \
  | jq '.foods[] | {fdcId, description, brandOwner, category: .foodCategory}'
```

## API Quirks

- **`brandOwner` requires an EXACT stored string match** including apostrophes, spacing, and capitalization. "McDonald's" works; "McDonalds" returns 0 hits. When unsure, omit `brandOwner` and filter results by substring on the `brandOwner` field in each result.
- Restaurant chains are not always categorized under their human name — Chipotle may appear as "Chipotle Mexican Grill" and Starbucks items as "Starbucks Corporation". Try a few variants if the first returns 0.
- **`foodNutrients` in search results is FLAT with `value` (not `amount`).** Shape: `{nutrientId, nutrientName, nutrientNumber: "208", unitName: "kcal", value: 250.0, ...}`. Do not destructure `.nutrient.number` — that's the detail-endpoint shape.
- Menu items appear as Branded foods; their foodNutrients on search results are per 100 g. For per-serving calorie comparisons, the skill should either (a) fetch each candidate's full detail and read `labelNutrients.calories.value`, or (b) multiply search-result nutrient values by `servingSize / 100`.
- Many fast-food items are catalogued with category=Restaurant (not all brands). If `foodCategory` is unexpected, still trust the `brandOwner` field.
- Restaurant menus change frequently. `publishedDate` or `modifiedDate` on the search result indicates currency — prefer recent entries when duplicates exist.

## Common Mistakes

(to be populated during the refinement loop)
