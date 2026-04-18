---
name: usda-fdc-ingredient-compliance
description: Use when a user asks whether a specific branded packaged food is vegan, vegetarian, or contains a hidden allergen (soy, peanut, tree nut, gluten, dairy, egg, sesame, shellfish, fish) — scans the FDC ingredients string for animal derivatives or allergen keywords.
---

# USDA FDC — Ingredient Compliance Scan

## When to Use

The user asks a yes/no question about whether a specific branded packaged product meets a dietary or allergy constraint that can be answered by scanning its printed ingredient list. Covers vegan / vegetarian checks AND top-9 allergen detection. Examples: "Is this protein bar vegan?", "Does this candy contain gelatin?", "Is this bread soy-free?".

## API Surface

- **Endpoint:** `GET /food/{fdcId}` (optionally preceded by `GET /foods/search` to resolve a brand/product name to an fdcId)
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}` query parameter on every call
- **Key fields read:** `dataType`, `description`, `brandOwner`, `ingredients` (string; Branded only)
- **Parse strategy:** case-insensitive substring scan of the `ingredients` string against a per-question keyword list
- **Resolve strategy:** search with the user's literal product name ONLY. Do NOT append the user's dietary constraint (e.g. `vegetarian`, `vegan`, `gluten-free`) to the query — it pollutes the match and returns generic lookalike records.

## Product Resolution (do this before the scan)

The `/foods/search` endpoint is a fuzzy matcher and WILL cheerfully return a wrong-category product when the exact product is absent. Before scanning, verify the chosen hit actually matches the user's product:

1. Tokenize the user's product name (brand + EVERY flavor/variety/type word). Every user-supplied token is REQUIRED. Reject any hit whose `description` + `brandOwner` drops a user token OR adds a differentiating flavor/variety/category token the user did not say. Verify BEFORE calling `/food/{fdcId}` — if no hit passes, say the product is not in FDC rather than scan a lookalike.
   - `Chobani Plain Nonfat Greek Yogurt` → reject `PLAIN NONFAT YOGURT` (missing `Greek`; `brandOwner` not Chobani).
   - `Silk Original Soymilk` → reject `Silk Chocolate Soymilk` (added `Chocolate`, dropped `Original` — different variety).
   - `Rao's Marinara Sauce` → reject `RAO'S, LEMON COOKING SAUCE` (missing `Marinara`, added `Lemon`).
   - `Lightlife Smart Dogs` → reject `LIGHTLIFE, ORGANIC THREE GRAINS TEMPEH` (missing `Smart Dogs` — different category).
   - `RXBar Chocolate Sea Salt` → reject `CHOCOLATE SEA SALT ALMONDS` (almonds ≠ protein bar; `brandOwner` not RXBar).
   - `Kind Dark Chocolate Almond bar` → reject `KIND, BARS, DARK CHOCOLATE CHILI ALMOND` (added `Chili` — different flavor).
   - `Ocean's Halo No Shell Noodle Soup` → reject `OCEAN'S HALO, NOODLE SOUP` (missing `No Shell`) AND `THE SEAWEED CHIP` (category mismatch).
   - `Trader Joe's Peanut Butter Cups` → reject `CRUNCHY UNSALTED ORGANIC PEANUT BUTTER` (missing `CUPS`).
   - `Nutella Hazelnut Spread` → reject `COOKIES FILLED WITH NUTELLA HAZELNUT SPREAD` (extra `COOKIES` — different product).
   - `Chobani Plain Nonfat Greek Yogurt` → reject `PLAIN GREEK NONFAT YOGURT` with `brandOwner: Bi-Lo` (brandOwner is not Chobani — store-brand lookalike).
   - `Gardein Classic Meatless Meatballs` → reject `GARDEIN HOME STYLE MEATLESS MEATLOAF` (meatloaf ≠ meatballs — different product even with matching brand).
   - `Perfect Bar Dark Chocolate Chip Peanut Butter` → reject `SEATTLE CHOCOLATES DARK CHOCOLATE TRUFFLE` (wrong brandOwner AND truffle ≠ bar — category mismatch).
2. If no hit in the first page matches, you MUST actually retry (not abandon): (a) bump `pageSize` to 25-50, (b) try alternate phrasings — drop adjectives, swap synonyms (`Mixed Nuts`→`Nut Mix`, `Birthday Cake Bar`→`Birthday Cake Protein Bar`, `Chocolate Sandwich Cookies`→`Joe-Joe's Cookies`), add or drop the `brandOwner`, (c) try `brandOwner=<brand>` as a separate query param (e.g. `brandOwner=Clean Simple Eats`, `brandOwner=Trader Joe's`, `brandOwner=Enjoy Life Foods`, `brandOwner=Amy's Kitchen`, `brandOwner=SunButter`, `brandOwner=Justin's`). Only after at least TWO distinct retry queries returned nothing usable may you tell the user the product is not in FDC. A single off-category hit (e.g. Strawberry Spread returned for a Mixed Nuts query) is NOT grounds to give up — retry first. HARD BRAND RULE: if the user named a brand (Kirkland, Daiya, Lärabar, Quest, Clean Simple Eats, Perfect Bar, RXBar, Justin's, SunButter, Enjoy Life, Amy's Kitchen, Trader Joe's, Silk, Gardein, Cascadian Farm, etc.), the matched `brandOwner` MUST plausibly be that brand or a known parent/subsidiary (e.g. Danone for Silk, Pinnacle Foods for Gardein, General Mills for Cascadian Farm/Annie's). A hit whose `brandOwner` is a completely unrelated company (Patron Saint Records for Lärabar, Oberlin Canteen for Daiya, D's Naturals for Quest, Flowers Foods for Clean Simple Eats, Seattle Chocolate for Perfect Bar, Wonder Natural Foods for a `banana` query, Publix/Harris-Teeter/Bi-Lo/Kroger/Wegmans for ANY named brand, Hi-Tech Accessories for Trader Joe's, Jo-Lee Food Products for Enjoy Life, Peanut Butter Americano for Justin's, Conagra for Amy's Kitchen) is an AUTO-REJECT — do not scan it, retry or declare not-in-FDC. `Store-brand lookalike at a grocery-chain brandOwner` is itself a distinct auto-reject category.
3. Only after a verified match proceed to `GET /food/{fdcId}`. When citing the call in your answer, paste the ACTUAL numeric fdcId you used (e.g. `GET /food/1851232`) — never `GET /food/?` or a placeholder. If you cannot produce the id, you did not actually resolve the product and must redo step 1.
4. SELF-CHECK before answering — MANDATORY BRAND-OWNER GATE: before you call `/food/{fdcId}`, write out one line: `user brand: <X>; matched brandOwner: <Y>; same company? <yes/no>`. If `no` (or the matched brandOwner is a grocery chain/store brand like Publix, Harris-Teeter, Kroger, Bi-Lo, Wegmans, Safeway; a clearly unrelated entity like Hi-Tech Accessories, Jo-Lee Food Products, Flowers Foods for Clean Simple Eats, Peanut Butter Americano for Justin's, Conagra for Amy's Kitchen; or a private-label co-packer), the hit is an AUTO-REJECT — do NOT scan, retry with a different query or declare not-in-FDC. Also reject if the matched description adds a flavor/variety word the user did not say (Chocolate for Original, Meatloaf for Meatballs, Oats-and-Honey for Honey-Almond, Vanilla-Creme for Sandwich) or drops one the user did say. Treat `close enough same brand different product` as auto-reject too — matching brand does NOT save a meatloaf-for-meatballs mismatch.

## Minimal Happy Path

```bash
# 1. Resolve product name to fdcId
curl -s "https://api.nal.usda.gov/fdc/v1/foods/search?query=SweetTreats+Marshmallows&dataType=Branded&pageSize=3&api_key=${USDA_FDC_API_KEY}"

# 2. Fetch the full ingredient list for the chosen fdcId
curl -s "https://api.nal.usda.gov/fdc/v1/food/1955793?api_key=${USDA_FDC_API_KEY}" | jq '.ingredients'
```

## API Quirks

- `ingredients` field exists **only on `dataType: "Branded"` foods**. Foundation / SR Legacy / Survey records do NOT carry an ingredients string. If the user asks about a whole food (e.g. "Is raw spinach vegan?") the skill must recognize the food is not packaged and answer from general knowledge rather than force an API call.
- Substring matching must be **case-insensitive** — ingredients are stored uppercase (e.g. `"GELATIN"`, `"SOY LECITHIN"`). Use `lower()` before `in` / regex.
- Substring matching must be **word-boundary aware** for short tokens. `milk` naively substring-matches inside `oatmilk`, `soymilk`, `almondmilk`, `buttermilk` — all plant-based and NOT a dairy hit. `butter` substring-matches inside `peanut butter`, `almond butter`, `cocoa butter`, `shea butter`, `sunflower butter`, `buttermilk` — none of those are dairy butter; chocolate-chip ingredient lists almost always list `COCOA BUTTER` which is plant fat, NOT dairy. `egg` substring-matches inside `eggplant`. Before declaring a hit, verify the keyword is NOT a prefix/suffix of a plant-based compound word. Correct dairy-butter match requires `butter` NOT preceded by `peanut|almond|cocoa|shea|nut|apple|sunflower|seed` and NOT followed by `milk`. Correct dairy-milk match requires `milk` NOT preceded by `oat|soy|almond|coconut|rice|cashew|hemp|pea|butter|nut`. MANDATORY EVIDENCE LINE: when a short-token keyword (`milk`, `butter`, `egg`) matches, paste the SURROUNDING 3-5 words from the ingredient string (e.g. `...SUGAR, COCOA BUTTER, SOY LECITHIN...`) before declaring the hit. If the matched token is part of a plant-based compound (cocoa butter, soymilk, eggplant), disqualify the hit.
- Ingredient strings are run-on text with parentheticals for sub-ingredients (e.g. `"CHOCOLATE COATING (SUGAR, COCOA BUTTER, MILK, ...)")`. Plan for "ingredient of ingredient" matches — `"milk"` must be found inside `"(..., MILK, ...)"`.
- Common vegan blockers to match: `gelatin`, `casein`, `whey`, `lactose`, `carmine`, `cochineal`, `shellac`, `confectioner's glaze`, `lard`, `tallow`, `rennet`, `honey`, `milk`, `butter`, `egg`, `isinglass`, `L-cysteine`.
- Top-9 allergen families: `milk`/`dairy`, `egg`, `fish`, `shellfish`/`crustacean`, `tree nut` (almond, cashew, walnut, pecan, pistachio, hazelnut, Brazil, macadamia), `peanut`, `wheat`/`gluten`, `soy`/`soya`/`soybean`, `sesame`.
- The `allergens` summary field is not universally populated — always cross-check by substring-scanning `ingredients` even when an `allergens` string is returned.

## Answer Shape

- Echo BOTH the user-provided product name AND the matched FDC `description` + `brandOwner` in the answer, so the user can catch a wrong-product match (e.g. `You asked about Trader Joe's Peanut Butter Cups; FDC returned 'CRUNCHY UNSALTED ORGANIC PEANUT BUTTER' — these are different products.`).
- If the user asked `is it in your database` / `do you have it` as a sub-question, answer that FIRST with an explicit `in FDC: yes (fdcId <N>)` or `in FDC: no (retried queries: …)` line BEFORE any scan verdicts.
- Address EVERY constraint the user named, one by one, naming the keyword list scanned for each. Never collapse to `does not appear to contain the specified ingredients` and never issue a single conflated verdict like `appears compliant` for a multi-constraint question — enumerate per-constraint. Required format per constraint: `<constraint>: scanned [<explicit keyword list>] against ingredients — <found|not found> → <verdict>`. Examples: `vegan: scanned [gelatin/casein/whey/lactose/carmine/cochineal/shellac/honey/milk/butter/egg/lard/tallow/rennet/isinglass] — not found → VEGAN`; `vegetarian: scanned [beef/pork/chicken/turkey/fish/anchovy/gelatin/lard/tallow/rennet] — not found → VEGETARIAN`; `peanut: scanned [peanut/groundnut/arachis] — not found → safe`; `tree nut: scanned [almond/cashew/walnut/pecan/pistachio/hazelnut/brazil/macadamia/pine nut/coconut] — not found → safe`; `dairy: scanned [milk/casein/whey/lactose/butter/cheese/cream] — not found → safe`; `lactose: scanned [milk/lactose/whey/cream] — not found → safe`; `egg: scanned [egg/albumen/ovalbumin/lysozyme] — not found → safe`. A verdict without its bracketed keyword list is incomplete. EXTRACTION RULE: before scanning, explicitly list EVERY constraint the user named — vegan, vegetarian, peanut-allergy/peanut-free, dairy-allergy, lactose-intolerant, egg-allergy, gluten-free, soy, sesame, tree-nut, fish, shellfish, `is it in your database`, `is X vegan generally` — and output one bracketed line per constraint. A vegan hit does NOT discharge a separate peanut or egg constraint; answer each one. Compound questions about a partner/family member count as separate constraints too.
- Ground every verdict in the ingredients string actually read. Do NOT speculate about ingredients not found (e.g. `biscuits could contain lard`) and do NOT assert an ingredient is `also present` unless its keyword matched in the scanned string. A product-name hint like `Vegan` in the description is NOT a substitute for scanning the vegan-blocker keyword list.
- When the user asks about a product that IS the allergen (tahini for a sesame allergy, peanut butter for a peanut allergy), state directly that the product is categorically unsafe. Do NOT lead with `SAFE` and then reverse mid-sentence — pick one verdict and hold it.
- General-knowledge ingredient questions (`is honey vegan?`, `is gelatin vegetarian?`, `is casein dairy?`) still use the bracketed format: `<constraint>: <ingredient> is <origin> → <verdict>`, plus one sentence on nuance if relevant (honey ethical divide; gelatin = animal collagen; carmine = cochineal insect). No API call needed, but the format is required.
- Distinguish `vegan` from `vegetarian`. Vegetarian allows dairy and eggs; vegan does not. Answer the exact question asked — do not upgrade a vegetarian question to a vegan verdict or vice versa.
- If the user asks a compound question (e.g. vegan AND sesame-free, a packaged product AND a whole-food comparison, or `is X in FDC AND is X vegan`), split it and answer each part. Even when half the question is blocked (product not in FDC, supplement sourcing not disclosed), you MUST still answer the OTHER halves from general knowledge. EVERY sub-question gets its own output line — no silent drops. Examples: `Red Bull not in FDC` still owes a general-knowledge vegan answer (taurine is now typically synthetic but historically bovine — ask the manufacturer); `Campbell's Tomato Soup + is a raw tomato vegetarian` owes BOTH a scan of the soup AND a one-line `raw tomatoes are trivially vegetarian/vegan`; `is it in your database AND does it contain gelatin AND is it vegetarian` owes THREE lines — explicit in-database yes/no, a gelatin: scanned [gelatin] line, and the vegetarian scan. A general-knowledge-only question like `is honey vegan?` or `is gelatin vegetarian?` still gets the bracketed format: `vegan: honey is an animal product (bee-produced) → NOT VEGAN (ethical divide: strict vegans exclude; some flexibly include)`; `vegetarian: gelatin is animal collagen (bovine/porcine hide/bone) → NOT VEGETARIAN`.

## Non-Packaged / Non-FDC Products

If the user's product is a local-bakery item, restaurant dish, homemade food, raw whole food, or commodity (e.g. `cupcake from a local bakery`, `my grandma's cookies`, `raw spinach`, `plain granulated sugar`, `a banana`, `Sprinkles Red Velvet Cupcake` (bakery chain, not packaged)), it will NOT have a useful FDC entry. Do NOT scan a coincidental branded match. A bare whole-food word (`banana`, `apple`, `carrot`) or a bakery/restaurant name MUST short-circuit the API call entirely — do not `/foods/search` it, answer `a plain banana is trivially vegan (it's a fruit)` from general knowledge. Instead you MUST: (a) explicitly note FDC doesn't cover this class of food, AND (b) still answer the user's actual dietary question from general knowledge — e.g. `plain granulated sugar is usually vegan, but some US cane sugar is filtered through bone char; look for beet sugar or `vegan`/`organic` certification to be sure`; e.g. `typical Honey Wheat Bread contains wheat flour, yeast, honey (not vegan), and often milk or butter — ask the baker for the specific recipe`. Stopping at `out of scope` with no general-knowledge content is NOT an acceptable answer.

## Known Formulation Traps

| Product family | Scan must also check for |
|---|---|
| Pop-Tarts, frosted toaster pastries | `gelatin` (in frosting), milk derivatives — frosted varieties are NOT vegan |
| Marshmallows, gummies, jelly beans | `gelatin`, `confectioner's glaze`/`shellac`, `carmine` |
| Chocolate-coated candies (cups, bars) | `milk`, `milkfat`, `whey`, `casein`, `lactose` inside the `(CHOCOLATE COATING: ...)` parenthetical |
| Bread, bagels, pizza dough | `L-cysteine` (often animal-derived), `mono- and diglycerides` (ambiguous) |
| Red/pink candies, yogurts | `carmine`, `cochineal`, `natural red 4` |
| Wine/juice/beer finings | `isinglass`, `gelatin` |
| Supplements (glucosamine, chondroitin, omega-3, vitamin D3, collagen, glycerin capsules) | FDC ingredient string will NOT disclose raw-material sourcing — glucosamine may be shellfish OR fungal; chondroitin usually bovine/shark; D3 often lanolin (sheep); collagen is animal. For these, state that the scan is INSUFFICIENT and the user must check the manufacturer label or contact the brand. |
| Cane sugar, beet sugar, brown sugar | Cane sugar in US is sometimes bone-char filtered (not vegan). Beet sugar and certified-vegan cane sugar are safe. FDC ingredient string rarely says which. |
| Worcestershire sauce | Traditional Lea & Perrins-style Worcestershire contains `anchovies` and is NOT vegetarian. Vegetarian/vegan variants exist (Annie's, some store brands). If the FDC ingredient string shows no anchovy, cite that explicitly but warn the user that most Worcestershire DOES contain anchovy and they must confirm on the specific bottle. |
| Energy drinks (Red Bull, Monster, Rockstar) | `taurine` and `L-carnitine` were historically animal-derived (bovine bile / meat) but are now typically synthetic in mass-market energy drinks. FDC ingredient string does NOT disclose sourcing. State: currently synthetic by industry standard, but confirm with manufacturer if strict. |
| Chocolate chips, chocolate coatings | `COCOA BUTTER` is plant-derived fat from cacao — it is NOT dairy butter. Do not flag it as a dairy hit. Scan instead for `MILK`, `MILKFAT`, `WHEY`, `CASEIN`, `LACTOSE`, `BUTTERFAT` or `BUTTER` NOT preceded by `cocoa/peanut/almond/shea/nut/sunflower`. |
| `Vegan`/`Plant-Based` labeled products (Follow Your Heart, Beyond, etc.) | Ingredient strings routinely contain plant-based compound words (`SOYMILK`, `OAT MILK`, `ALMOND BUTTER`, `COCONUT MILK`) that will false-positive naive `milk`/`butter` substring scans. If a product is labeled Vegan and your scan returns a dairy hit, re-check with the word-boundary rule AND paste the surrounding ingredient context — most such hits are false positives. |

## Common Mistakes

- Appending the dietary constraint to the search query (`...+vegan`, `...+gluten-free`) — search by product name only.
- Accepting the first `/foods/search` hit without verifying EVERY user token is present in `description`+`brandOwner` AND no differentiating token (flavor/variety/category) was added. Common failure mode: hit matches 3 of 4 user words and looks close enough — it isn't. Recurring regressions observed: Gardein meatloaf-for-meatballs, Silk Chocolate-for-Original, RXBar almonds-for-bar, Cascadian Farm Oats-and-Honey-for-Honey-Almond, Trader Joe's Vanilla-Creme-for-Sandwich, store brands (Publix/Harris-Teeter/Bi-Lo/Conagra/Jo-Lee/Flowers Foods/Hi-Tech Accessories/Peanut Butter Americano) scanned instead of the user's named brand. If the brandOwner-gate line cannot be written honestly, the resolution is NOT complete.
- Taking a `Vegan`/`Organic`/`Natural` label in the product description as proof of compliance without still running the animal-derivative keyword scan on `ingredients`.
- Speculating about ingredients that might be present (`could contain lard`, `gelatin also present`) when the scanned string does not contain that keyword.
- Answering `vegan` when the user asked `vegetarian` (or vice versa).
- Collapsing multi-constraint questions into a single vague `does not appear to contain the specified ingredients` — enumerate each constraint.
- Scanning FDC for bakery/restaurant/homemade items that aren't packaged products.
- Forgetting Pop-Tart-style frosted pastries commonly contain gelatin even though the word `gelatin` is easy to overlook in a long ingredient string.
- Naive substring matching `milk` inside `oatmilk`/`soymilk`/`almondmilk`, `butter` inside `peanut butter`/`cocoa butter`/`almond butter`, or `egg` inside `eggplant` — always require a word boundary or disqualifying-prefix check before declaring the hit.
- Answering only one constraint of a compound question (e.g. user asks vegan AND peanut-allergy, skill answers only vegan). Extract every constraint BEFORE scanning and emit one bracketed line per constraint.
- Scanning a branded coincidence for a bare whole-food word (`banana`, `apple`) or a bakery-chain name — short-circuit these before `/foods/search`.
