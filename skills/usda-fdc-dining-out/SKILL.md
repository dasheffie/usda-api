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
- **Request body (preferred — NO brandOwner):** `{"query": "<concrete menu keyword>", "dataType": ["Branded"], "pageSize": 50}` — then post-filter in code by matching the brand token against each result's `brandOwner` / `brandName` / `description`. See API Quirks for canonical tokens and why `brandOwner` is unreliable for chains.
- **Key fields read (from search results):** `description`, `brandOwner`, `foodCategory`, `foodNutrients[]` (flat shape with `value`/`nutrientNumber`), `servingSize`, `labelNutrients` (if pulling detail)
- Optional follow-up: `GET /food/{fdcId}?format=full` on top 2-3 candidates for `labelNutrients` per-serving values

## Per-Serving Conversion (MANDATORY before reporting any numeric answer)

Search-result `foodNutrients[].value` is per 100 g. Every user question about calories / protein / sodium / carbs is per-SERVING. Before reporting a number:

1. Read `servingSize` and `servingSizeUnit` from the search hit (or fetch `GET /food/{fdcId}?format=full` and read `labelNutrients.{calories,protein,sodium,carbohydrates}.value` directly — these are already per-serving).
2. If using search-result nutrients: `per_serving = value_per_100g * (servingSize / 100)` when `servingSizeUnit` is `g` / `ml`. If `servingSize` is missing or in a non-gram unit, fetch the detail endpoint instead — do not report per-100g as if it were per-serving.
3. Report the per-serving number explicitly (e.g. `250 kcal / 248 g serving`), never `N per 100g`. A value expressed as `per 100g` is an incomplete answer and fails every diet-threshold question (under 500 cal, under 700 mg sodium, under 100 cal, >=25 g protein).

## User-Constraint Filtering (MANDATORY before ranking)

The user's question names BOTH a brand AND a food category (sandwich, salad, wrap, burrito bowl, protein box, donut, side, dessert, drink). After brand-filtering, apply a category filter before ranking — never return a chili for a sandwich question, a bread for a salad question, a sauce for a side question, or a frappuccino for a sandwich/protein-box question. Minimum category tokens to require in `description` (case-insensitive):

- sandwich: `sandwich`, `burger`, `whopper`, `big mac`, `mcchicken`, `croissanwich`, `biscuit` (breakfast sandwich), `sub`, `hoagie`, `melt` — EXCLUDE `chili`, `bread` (loaf), `sauce`, `drink`, `coffee`, `frappuccino`, `seasoning`
- salad: `salad`, `cobb`, `market salad`, `caesar` — EXCLUDE `bread`, `sandwich`, `chili`, `wrap` (unless user said wrap)
- wrap: `wrap`, `tortilla wrap`, `snack wrap`
- side: `fries`, `tots`, `coleslaw`, `mac and cheese`, `biscuit` (side), `apple slices`, `hash brown` — EXCLUDE `sauce`, `dressing`, `seasoning`
- protein box: must contain `protein box` or `protein bistro box` (Starbucks) — EXCLUDE `frappuccino`, `coffee`, `latte`, `refresher`
- donut / donuts: `donut`, `doughnut`, `munchkin`, `kreme`, `glazed` — EXCLUDE `creamer`, `coffee`, `k-cup`
- bowl: `bowl`, `burrito bowl`, `famous bowl` — EXCLUDE `cereal bowl`, `soup bowl`
- drink/beverage: `coffee`, `latte`, `frappuccino`, `refresher`, `soda`, `shake`, `smoothie`, `tea`

If the post-brand, post-category filter yields 0 items, retry with alternate brand keywords from the cheat-sheet BEFORE giving up (see retry rule below).

## Minimal Happy Path

```bash
# Find McDonald's hamburger options — search WITHOUT brandOwner, post-filter by brand token
curl -s -X POST "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=${USDA_FDC_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"query":"hamburger","dataType":["Branded"],"pageSize":50,"sortBy":"publishedDate","sortOrder":"desc"}' \
  | jq '[.foods[] | select((.brandOwner // "" | ascii_downcase | contains("mcdonald")) or (.brandName // "" | ascii_downcase | contains("mcdonald")) or (.description // "" | ascii_downcase | contains("mcdonald"))) | {fdcId, description, brandOwner, brandName, category: .foodCategory}]'
```

## API Quirks

- **`brandOwner` is unreliable for restaurant chains — DO NOT rely on it as the primary filter.** The transcript shows `brandOwner="McDonald's"`, `"Subway"`, `"Chipotle"`, `"Taco Bell"`, `"Starbucks"`, `"Domino's"`, `"KFC"`, `"Dunkin"`, `"DQ"`, `"Arby's"`, `"Popeyes"`, `"Whataburger"`, `"Burger King"`, `"Chick-fil-A"` all returning 0 items or 0 on-brand items. Many chain items are stored under `brandName` or embedded in `description` rather than `brandOwner`.
- **Required strategy:** issue the search WITHOUT `brandOwner`, then post-filter results in code by matching the brand token (case-insensitive) against EACH result's `brandOwner`, `brandName`, AND `description` fields. Only treat an item as on-brand when one of those three contains the brand token.
- **Canonical brand tokens to match** (substring, case-insensitive, try all variants before giving up): McDonald → `mcdonald` / `mccafe`; Subway → `subway`; Chipotle → `chipotle` (the brand item's `brandOwner`/`brandName` MUST contain `chipotle mexican grill` or `chipotle` as the brand — reject items where `chipotle` only appears in description as a flavor/ingredient, e.g. Marie Callender's Cheesy Chipotle Bowl); Starbucks → `starbucks`; Taco Bell → `taco bell` (prefer items where brandOwner/brandName is Taco Bell itself — retail Cravings Kits / frozen boxes from grocery aisles are NOT restaurant menu items; exclude if description contains `kit`, `box`, `frozen meal`); Burger King → `burger king` OR `bk cafe` (exclude `king's chef`); Wendy → `wendy`; Chick-fil-A → `chick-fil-a` OR `chick fil a` (exclude `hip chick`); KFC → `kfc` OR `kentucky fried`; Popeyes → `popeyes`; Arby → `arby`; Domino → `domino` (exclude `domino sugar`); Dunkin → `dunkin` (exclude coffee-creamer retail products like `ESL 32oz Extra Extra` — those are not donut/menu items); DQ / Dairy Queen → `dairy queen` OR `dq`; Panera → `panera`; Whataburger → `whataburger`; Five Guys → `five guys`.
- **Brand-match must be on `brandOwner` or `brandName`, NOT on `description` alone** for ambiguous tokens (`chipotle`, `dq`, `bk`, `domino`). Description-only matches admit off-brand grocery products that happen to mention the word.
- **Reject retail/grocery SKUs when the user asked about the restaurant menu.** Description tokens that signal retail (not in-store menu): `oz box`, `oz bag`, `frozen meal`, `cravings kit`, `ESL`, `creamer`, `k-cup`, `ground coffee`, `bottle`, `multipack`. Filter these out before ranking.
- If post-filter yields 0 on-brand items for a given query keyword, RETRY with AT LEAST 3 alternate keywords drawn from the brand-specific cheat-sheet below before reporting "not in FDC". This is NOT optional — the transcript shows repeated give-ups after one empty search (Chipotle bowl, Burger King sandwich, Popeyes chicken sandwich, Subway wrap, Dunkin donut, Domino's wings, McDonald's mccafe, Popeyes blackened sandwich, Subway sub). The retry procedure: (a) try the cheat-sheet keyword most specific to the user's category; (b) if 0, try the next 2 cheat-sheet keywords for the same brand; (c) only after 3+ distinct brand-native keywords all return 0 on-brand hits may you report "FDC has limited coverage for `<brand>`". Never search with generic placeholders like `item`, `meal`, `food`, `thing`, `breakfast`, `dessert`, `kids meal`, `sandwich` alone — always translate the user's diet constraint into a concrete branded menu noun.
- **Brand-specific keyword cheat-sheet** (try these in order, stop at first brand-matched hit):
  - McDonald's: `big mac`, `quarter pounder`, `mcchicken`, `mcnugget`, `egg mcmuffin`, `mccafe`, `mcflurry`, `apple pie`, `filet-o-fish`, `french fries`
  - Burger King: `whopper`, `croissanwich`, `chicken fries`, `impossible whopper`
  - Wendy's: `dave's single`, `baconator`, `frosty`, `spicy chicken`, `chili`
  - KFC: `original recipe`, `extra crispy`, `popcorn chicken`, `famous bowl`, `pot pie`, `biscuit`, `coleslaw`
  - Chick-fil-A: `chick-fil-a sandwich`, `grilled nuggets`, `waffle fries`, `cobb salad`, `market salad`, `spicy deluxe`
  - Taco Bell: `crunchwrap`, `chalupa`, `quesadilla`, `mexican pizza`, `crunchy taco`, `bean burrito` (use brandOwner filter, reject grocery `cravings kit`)
  - Starbucks: `frappuccino`, `refresher`, `cold brew`, `protein box`, `egg bites`, `cake pop`, `pike place`
  - Dunkin: `munchkin`, `glazed donut`, `boston kreme`, `breakfast sandwich`, `macchiato` (reject retail creamers)
  - Domino's: `hand tossed`, `pan pizza`, `cheesy bread`, `parmesan bites`, `wings`
  - Chipotle: `burrito bowl`, `barbacoa`, `carnitas`, `sofritas`, `guacamole` (require Chipotle Mexican Grill in brandOwner/brandName)
  - Panera: `you pick two`, `mac and cheese`, `broccoli cheddar`, `bacon turkey bravo`
  - Arby's: `roast beef`, `beef n cheddar`, `curly fries`
  - Popeyes: `spicy chicken sandwich`, `cajun fries`, `red beans`
  - Whataburger: `whataburger`, `honey butter chicken biscuit`, `patty melt`, `taquito`
  - Five Guys: `little hamburger`, `bacon cheeseburger`, `cajun fries`
- If ALL 3+ branded keywords still yield 0 on-brand hits, THEN and only then report honestly: "FDC has limited coverage for `<brand>` — try the chain's published nutrition page." Do not fall back to retail SKUs from other brands.
- **`foodNutrients` in search results is FLAT with `value` (not `amount`).** Shape: `{nutrientId, nutrientName, nutrientNumber: "208", unitName: "kcal", value: 250.0, ...}`. Do not destructure `.nutrient.number` — that's the detail-endpoint shape.
- Menu items appear as Branded foods; their foodNutrients on search results are per 100 g. For per-serving calorie comparisons, the skill should either (a) fetch each candidate's full detail and read `labelNutrients.calories.value`, or (b) multiply search-result nutrient values by `servingSize / 100`.
- Many fast-food items are catalogued with category=Restaurant (not all brands). If `foodCategory` is unexpected, still trust the `brandOwner` field.
- Restaurant menus change frequently. `publishedDate` or `modifiedDate` on the search result indicates currency — prefer recent entries when duplicates exist.

## Common Mistakes

- **Sending `brandOwner` in the body and trusting a non-empty response.** A response can have 11-25 items yet zero on-brand items (Chick-fil-A → HIP CHICK FARMS; Burger King → King's Chef Diner; Dunkin' Donuts → Golden Donut Inc.). ALWAYS post-filter and verify at least one item matches the brand token before ranking.
- **Using a generic query keyword like `item`, `meal`, `food`, `thing`, `breakfast`, `dessert`.** These either dilute the results with other brands or return nothing on-brand. Translate the user's constraint into a concrete menu noun (burger, salad, wrap, burrito, biscuit, latte, frappuccino, nuggets, fries, taco, sub).
- **Giving up after one keyword+brand attempt returns 0.** Retry with at least 3 brand-native menu nouns from the cheat-sheet above before concluding the chain is absent from FDC.
- **Ignoring the brand-matched subset and reporting "not found".** If even 1 item passes the brand filter, use it — do not discard a 2- or 4-item matched subset and report empty (Q56 transcript: 'latte' returned 4 on-brand Starbucks matches but answer was 'not found').
- **Accepting a description-only brand match as on-brand.** `chipotle` in a Marie Callender's frozen-meal description is a flavor descriptor, not a Chipotle Mexican Grill menu item. Require the brand token to land in `brandOwner` or `brandName` for ambiguous brands. This also applies to Starbucks: Q3 returned a `VANILLA LIGHT CHILLED COFFEE DRINK` whose description did not contain `starbucks` — verify `starbucks` appears in `brandOwner` or `brandName` before treating a chilled coffee drink as a Starbucks menu item, otherwise it's a retail-aisle Frappuccino bottled SKU from a different bottler.
- **Returning a retail SKU when the user asked about the in-store menu.** Cravings Kits, frozen bowls, coffee creamers, K-cups, bottled drinks, `15 oz Can` canned chili, `Taco Seasoning Mix` packets are grocery products — exclude via the retail-SKU filter (extend retail tokens to include `can`, `canned`, `seasoning mix`, `packet`, `pouch`, `jar`) and prefer actual menu items. Q20 (Wendy's Canned Chili 15 oz Can) and Q95 (Taco Seasoning Mix) both leaked through — the retail filter must run BEFORE ranking, not after.
- **Reporting a nutrient value as `N per 100g`.** Never ship this to the user. Convert to per-serving first (see Per-Serving Conversion section) or fetch `labelNutrients` from the detail endpoint. A frappuccino at `63.2 per 100g protein` (Q31) or iced coffee at `5.0 per 100g calories` (Q82) is both implausible and useless for a diet-threshold comparison.
- **Ignoring the second half of a compound user constraint.** Q82 asked for a `filling` low-cal drink (implying protein or fiber minimum) and the skill returned plain iced coffee with 0 protein. When the user's question has two constraints (e.g. under 500 cal AND 30 g protein, under 700 mg sodium AND lunch-sized), BOTH must be satisfied by the returned item; rank only items that pass both filters.
