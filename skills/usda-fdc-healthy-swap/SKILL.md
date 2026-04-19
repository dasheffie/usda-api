---
name: usda-fdc-healthy-swap
description: Use when a user loves a specific branded product but wants a 1:1 healthier replacement that preserves the eating experience — fetches the original's profile, then searches Branded foods in the same category for cleaner-ingredient or better-macro alternatives and ranks them.
---

# USDA FDC — Healthy Swap Engine (1:1 Branded Replacement)

## When to Use

The user names a specific commercial product they enjoy (Doritos, Oreos, Cheez-Its, Haagen-Dazs, Coca-Cola, etc.) and asks for a healthier replacement that still scratches the same itch. Examples: "I love Doritos but want something cleaner — what should I switch to?", "Healthier version of Oreos?", "Alternative to seed-oil potato chips?". The output is 2-3 ranked 1:1 swaps with an explicit "here's what improves" summary.

## API Surface

Three-step flow (do NOT skip step 1):

1. **`POST /foods/search`** with the brand+product name **only if** you don't already have an `fdcId` — take the top Branded hit's `fdcId`. If the user gave an `fdcId`, skip this.
2. **`GET /food/{fdcId}`** on the original — read `brandedFoodCategory`, `ingredients`, `labelNutrients`, `brandOwner`. This step is mandatory; the second search keyword is derived from this response, never from the user's brand string.
3. **`POST /foods/search`** with `dataType: ["Branded"]` + a category keyword derived from the original's `brandedFoodCategory` (see API Quirks). Request `pageSize: 50` so post-filters have enough candidates. The keyword MUST be a SINGLE noun phrase — never contain a comma, slash, semicolon, or `&`. If your derived keyword contains any of those separators, you have a list; pick ONE noun phrase and discard the rest before calling search.

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
- **Same-category search keyword** comes from the original's `brandedFoodCategory` string, lower-cased, stripped of brand/place tokens (`milano`, `pepperidge`, `goldfish`, etc.) and stripped of `&`/`and`/`,`/`/`. Pick ONE noun phrase, not a list — and when the category is an umbrella (`Candy`, `Carbonated Beverages`, `Cookies & Biscuits`, `Cereal`, `Chips, Pretzels & Snacks`, `Snack, Energy & Granola Bars`, `Sandwiches/Filled Rolls/Wraps`), derive the subtype from the `description` field of the original (e.g. `Dr Pepper` → `pepper soda` or `cola`, `Mountain Dew` → `citrus soda`, `Virgil's Root Beer` → `root beer`, `Reese's` → `peanut butter cups`, `Skittles` → `fruit candy`, `M&M's` → `chocolate candy`, `Doritos` → `tortilla chips`, `Beanfields` → `bean chips`, `Biena` → `chickpea snacks`, `Ritz` → `crackers`, `Wheat Thins` → `crackers`, `Triscuit` → `crackers`, `Chips Ahoy` → `chocolate chip cookies`, `Nature Valley` → `granola bars`, `Clif Bar` → `energy bars`, `Snickers Marathon` → `protein bars`, `Oreo O's` → `chocolate cereal`, `Hot Pocket` → `frozen sandwich`, `Hellmann's` → `mayonnaise`). Examples:
  - `"Tortilla & Corn Chips"` → `"tortilla chips"` (NOT `"tortilla corn chips snacks"`)
  - `"Cookies & Biscuits"` for Milano → `"cookies"` (NOT `"milano cookie"` — `milano` is a place name and returns salami)
  - `"Carbonated Beverages"` for Pepsi → `"cola"` (use the product subtype, not the category umbrella)
  - `"Ice Cream & Frozen Desserts"` for Magnum → `"ice cream bars"` (keep the form factor noun)
  - `"Candy"` for Reese's → `"peanut butter cups"` (never ship `candy` alone — it returns unbranded `CANDY` rows)
  - `"Cereal"` for Oreo O's → `"chocolate cereal"` (never ship `cereal` alone — same unbranded-row problem)
  - `"Sandwiches/Filled Rolls/Wraps"` for Hot Pocket → `"frozen sandwich"` (strip the slashes; add `frozen` to exclude cold wraps)
- **`foodCategory` is almost always null on Branded foods.** Use `brandedFoodCategory` only; do not branch on `foodCategory`. If `brandedFoodCategory` is also missing, fall back to a noun extracted from `description` (e.g. `"Pepsi Cola"` → `"cola"`).
- **Never put filter words in the query.** `"without seed oils"`, `"no palm oil"`, `"less sugar"`, `"high fiber"` will return literal seed-oil bottles, palm-oil jars, sweeteners, and fiber powders. Filtering and ranking happen in post-processing on `ingredients` and `foodNutrients`, never in the search query.
- **Post-filter candidates BEFORE ranking** in this order:
  1. Drop any candidate whose `brandedFoodCategory` does not match the original's `brandedFoodCategory` (case-insensitive substring either way). This is the same-category guarantee — without it, kombucha returns gefilte fish, ice cream returns yogurt, protein bars return raw beef. If this filter drops 0 of 50 candidates, something is wrong — you almost certainly put a list-keyword in the query and the search never returned same-category hits; fix the keyword and re-search rather than passing through.
  2. Drop any candidate with empty/missing `ingredients` (a 0-ingredient count is a parse failure, not a virtue).
  3. Drop any candidate whose `description` is an unbranded generic noun (case-insensitive exact or near-exact match to the category umbrella: `CANDY`, `SODA`, `CEREAL`, `BISCOTTI`, `SNACK CRACKERS`, `CHEESE`, `COOKIE`, etc.) — these rows are category-label placeholders, not products, and violate the branded 1:1 contract even when `brandOwner` is populated.
  4. Drop any candidate with no `brandOwner`.
  5. Drop the original `brandOwner` (unless the user asks for same-brand swaps).
  After filtering, if fewer than 3 candidates remain, re-run the search with a DIFFERENT keyword (broader OR a sibling subtype from step 3 above — e.g. `crackers` → `whole grain crackers`, `cookies` → `sandwich cookies`) rather than relaxing these filters. Re-search up to 2 times before returning `No alternatives found`.
- **Rank by composite score** on the post-filtered set: lower added sugar (nutrient 539, fall back to total sugars 269), higher protein (203), higher fiber (291), absence of seed-oil ingredients, fewer total ingredients (count commas + 1). Disclose the ranking rule in the answer **and cite the actual numeric deltas** (`"5g sugar vs 18g"`, `"4g fiber vs 1g"`) — never just `"cleaner profile"` or `"fewer ingredients"` alone. If the user asked about a specific axis (sugar, fiber, seed oils), put that axis first in every candidate's justification.
- `labelNutrients` is per-serving — when comparing originals to candidates, use labelNutrients for both so the basis matches.
- **Portion-control warning:** the skill should always add "portion control still matters" — a cleaner product eaten in excess can still be worse than a small serving of the original.

## Common Mistakes

- **Skipping GET on the original** and going straight to a category search loses the `brandedFoodCategory` anchor — the second search becomes ad-hoc and returns off-category junk.
- **Putting negative filters in the query** (`"without seed oils"`, `"no palm oil"`, `"less sugar"`) returns the literal opposite — bottles of those very ingredients. Filters live in post-processing only.
- **Treating `foodCategory` as a usable field** on Branded foods — it is null in practice. Use `brandedFoodCategory`, then `description` as fallback.
- **Reporting unbranded generic descriptions** (`SNACK CRACKERS`, `SODA`, `BISCUIT`, `CANDY`, `CEREAL`, `BISCOTTI`, `CHEESE`) as swaps — these violate the branded 1:1 contract even when a `brandOwner` is populated; drop them in the post-filter (step 3) and re-search if fewer than 3 candidates survive.
- **Citing only ingredient count** when the user asked about sugar, fiber, or seed oils — always quote the numeric delta on the user's axis.
