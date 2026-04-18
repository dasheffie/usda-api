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
- **Request body:** `{"query": "<snack keyword>", "dataType": ["Branded"], "pageSize": 50, "sortBy": "dataType.keyword"}` — pull 50 so post-filtering still leaves candidates, then client-side sort ascending by **per-serving** sugars
- **Key fields read:** `description`, `brandOwner`, `foodCategory`, `ingredients`, `foodNutrients[]` (flat, look for `nutrientNumber == "269"` total sugars, `"539"` added sugars, `"208"` calories (kcal), `"291"` fiber), `servingSize`, `servingSizeUnit`
- **Optional follow-up:** `GET /food/{fdcId}?format=full` for accurate `labelNutrients.sugars.value` + `labelNutrients.addedSugar.value` per serving

## Ranking Rule (READ THIS BEFORE CODING)

1. **Rank by per-serving sugar, never per-100g.** Scale: `sugars_serving = sugars_per_100g * servingSize / 100`. Two cookies at 18g/100g rank differently if one has a 22g serving and the other a 40g serving.
2. **Prefer added sugar (539) when present**, fall back to total sugar (269) and disclose the fallback in the answer text (`"(added-sugar data not reported; ranked by total sugar)"`).
3. **Round servingSize to 1 decimal** before printing. Raw values like `28.399999618530273` are floating-point noise and must never reach the user.
4. **Post-filter on-category** before ranking (see Category Post-Filter table below). A `candy bar` query will otherwise surface ice-cream "candy bars" and cider-company bars.
5. **Distinct-brand diversity:** after sorting, keep at most one SKU per `brandOwner` in the top 3 so near-duplicates (same brand, three serving-size variants) do not fill the list.
6. **Suspicious-zero guard:** if `sugars_per_100g == 0` for a category that normally has sugar (cookies, yogurt, ice cream, candy, granola bars), require that `ingredients` does NOT contain `sugar alcohol|erythritol|allulose|maltitol|stevia|monk fruit`; otherwise demote and annotate `[sugar-alcohol sweetened]`.
7. **Empty-on-category:** if post-filter leaves zero candidates (e.g., user named a brand like "Magic Spoon" that is not in FDC), answer `"not found in FDC Branded — here are closest on-category alternatives"` rather than returning the raw keyword hits.

## Category Post-Filter

| User snack | `query` keyword | `description` must match (regex, case-insensitive) | Reject if description matches |
|---|---|---|---|
| Cookies (Chips Ahoy, Oreo, shortbread) | `chocolate chip cookies` / `oreo` / `fudge striped cookies` | `cookie` | `sauce`, `seasoning`, `tea` |
| Yogurt (Yoplait, Siggi's, Chobani) | `strawberry yogurt` / `plain yogurt` | `yogurt\|skyr` | `smoothie`, `drink`, `dip`, `non-dairy` unless user asked |
| Candy bar (Snickers, Twix) | `candy bar chocolate` | `candy bar\|chocolate bar` | `ice cream`, `frozen`, `cider`, `dessert` |
| Ice cream (Halo Top) | `ice cream low sugar` | `ice cream\|frozen dessert` | `cake`, `sandwich` unless user asked |
| Granola / protein bar | `granola bar` / `protein bar` | `bar` | `sauce`, `seasoning`, `chicken`, `seaweed` |
| Cereal (Raisin Bran, Magic Spoon) | `cereal high fiber` | `cereal` | `tortilla`, `lentil`, `flour`, `mix` |
| Crackers (Ritz, Triscuit, Wheat Thins) | `crackers` / `wheat crackers` | `cracker` | `cookie`, `chip`, `seasoning`, `dip`, `spread` |

For dietary constraints (gluten-free, lactose-free, vegan): require the literal phrase in `description` AND cross-check `ingredients` does not contradict (e.g. gluten-free must not list `wheat`, `barley`, `rye`). Private-label / "grocery-store mainstream" constraints are **not filterable via FDC** — disclose this limitation and suggest brandOwner names the user likely recognizes (General Mills, Kellogg, PepsiCo, Danone, Chobani, Kraft-Heinz).

## Minimal Happy Path

```bash
# Find Branded chocolate chip cookies, pull 50 hits, post-filter + scale to per-serving, then sort
curl -s -X POST "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=${USDA_FDC_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"query":"chocolate chip cookies","dataType":["Branded"],"pageSize":50}' \
  | jq '.foods
      | map(. + {
          sugars_100g:  ((.foodNutrients[]? | select(.nutrientNumber=="269") | .value) // null),
          added_100g:   ((.foodNutrients[]? | select(.nutrientNumber=="539") | .value) // null),
          kcal_100g:    ((.foodNutrients[]? | select(.nutrientNumber=="208") | .value) // null),
          fiber_100g:   ((.foodNutrients[]? | select(.nutrientNumber=="291") | .value) // null)
        })
      | map(. + {
          sugars_serving: (if .sugars_100g and .servingSize then (.sugars_100g * .servingSize / 100) else null end),
          kcal_serving:   (if .kcal_100g   and .servingSize then (.kcal_100g   * .servingSize / 100) else null end)
        })
      # post-filter: on-category (brand/desc/foodCategory sanity), drop suspicious-zero sugar when ingredients mention sugar/syrup
      | map(select(.description | test("COOKIE"; "i")))
      | map(select((.sugars_100g // 0) > 0 or ((.ingredients // "") | test("sugar alcohol|erythritol|allulose|maltitol|stevia"; "i") | not)))
      | sort_by(.sugars_serving // .sugars_100g)
      | .[0:5]
      | map({fdcId, description, brand: .brandOwner, foodCategory, sugars_serving: (.sugars_serving|tonumber|.*100|round/100), servingSize: (.servingSize|tonumber|.*10|round/10), servingSizeUnit})'
```

## API Quirks

- **`dataType` in POST body MUST be an array of strings**, never a CSV. `"dataType": "Branded"` (string) silently returns all types; only `"dataType": ["Branded"]` actually filters.
- **`foodNutrients` in search results uses `value` + `nutrientNumber`**, not `amount` + `nutrient.number`. Wiring up the detail-endpoint shape instead silently returns nothing.
- **Total sugars = `nutrientNumber == "269"`.** **Added sugars = `"539"`.** They are different metrics — the user almost always cares about 539 (added sugar) for health purposes, but the API is more likely to have 269 populated. Prefer 539 when present, fall back to 269 with disclosure.
- Values in search results are **per 100 g**; for honest per-serving comparisons, either scale by `servingSize/100` or re-fetch each candidate via `/food/{fdcId}` to read `labelNutrients.sugars.value` (per serving, matches the box).
- Empty-query returns HTTP 200 with the full 468K-food database — a destructive dump. Always validate the user's snack keyword is non-empty.
- **Rate limits (HTTP 429 / `OVER_RATE_LIMIT`) are shared per api_key at 1000 req/hr.** Each user question should cost **1 search call** (optionally +1 detail call only when a label value is load-bearing). Do NOT front-load brand-presence probes, per-category prefetches, or per-candidate `/food/{fdcId}` fetches — those multiply the request count and trip 429 on the very first real question. If a 429 is returned, back off once at 60s; if it persists, stop retrying and answer from cached/in-memory prior results plus category-typical knowledge, prefixed with `"(FDC rate-limited — answering from cached category data; values may be approximate)"`. Never retry-loop past ~2 minutes: the quota window is an hour and additional retries just waste the block.
- **Keyword over-breadth.** A bare `query: "candy bar"` matches any product whose description contains the words (ice-cream "candy bar", cider-company "candy bar"). Always combine with the Category Post-Filter regex on `description`.
- Watch for sugar-alcohol-sweetened products (erythritol, allulose, maltitol) — these DO have total sugar listed near zero but may still have "sugars" declared at 0 g + "sugar alcohols" disclosed in the ingredient list. Cross-check the `ingredients` string when the sugar count is suspiciously low.

## Common Mistakes

- **Ranking per-100g instead of per-serving.** A 100g "KNO Cookies" at 20g/100g is 20g per serving; a 32g cookie at 22g/100g is 7g per serving — per-100g sort inverts the real answer. Always scale.
- **Trusting the top hit's brand.** `brandOwner` like "Pura Stainless LLC", "Kid Tested Tunes", "Nine Pin Ciderworks" indicates a mislabeled / off-category FDC record — apply the Category Post-Filter table and reject brands whose name is obviously unrelated to food packaging.
- **Suspicious zeros.** `0.0g total sugar` on a cookie / granola bar / candy bar is almost always a sugar-alcohol-sweetened product or a data-entry blank, not a miracle. Cross-check `ingredients` for `erythritol\|allulose\|maltitol\|stevia\|monk fruit`; demote if matched.
- **Near-duplicate SKU spam.** Same `brandOwner` + same base description at 3 serving sizes = 1 product, not 3. Deduplicate by `(brandOwner, description-normalized)` before picking top 3.
- **Silently dropping user constraints.** If user says `<200 kcal`, `<8g added sugar/serving`, `high fiber`, `gluten-free`, `mainstream grocery`, `budget`: acknowledge each constraint in the answer and state which ones were applied as filters vs which could not be honored via FDC (retail availability, price — disclose explicitly).
- **Brand not in FDC.** Magic Spoon, RXBar, Halo Top, Siggi's — some popular brands are absent or sparse. When the user names a specific brand as the baseline, confirm or deny its presence (`query` = brand name, `pageSize` = 5) **before** ranking alternatives; if absent, answer `"<brand> is not in FDC Branded — comparing against category-typical values"` and pick alternatives anyway.
- **Floating-point serving sizes.** Print `servingSize` rounded to 1 decimal place; raw 32-bit float artifacts (`28.399999618530273`) are a display bug, not data.
- **Intrinsic vs added sugar (fruit questions).** For fruit products (mango, berries), total sugar (269) is mostly intrinsic; added sugar (539) is the health-relevant metric. Always report both when available and call out the distinction in the answer.
