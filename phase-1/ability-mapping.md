# Phase 1 — Ability → Endpoint Mapping

Source of user abilities: `docs/api_skill_builder_plan2.md` (14 proposed abilities).
Source of endpoints: `phase-0/endpoint-catalog.md`.

## Merge table

| # | Ability (user-proposed) | Endpoints | Fields read | Parse strategy | Merged into skill | Merge reason |
|---|---|---|---|---|---|---|
| 1 | Dining Out / Fast Food | `POST /foods/search` (brand+keyword, dataType=Branded) → `GET /food/{id}` | `description, brandOwner, foodNutrients[208,307,269,204], labelNutrients.calories` | rank candidates by calorie-density given brand constraint | `usda-fdc-dining-out` | unique: brand-filter + rank parse |
| 2 | Low-Sugar Snack Discovery | `POST /foods/search` (dataType=Branded) → `GET /food/{id}` | `foodNutrients[269 total sugars, 539 added sugar], labelNutrients.sugars` | sort candidates asc by sugar within a snack category | `usda-fdc-low-sugar-snack` | unique: sort-by-sugar on Branded |
| 3 | Homemade Recipe Breakdown | `GET /foods/search` (SR Legacy / Foundation) per ingredient → `POST /foods` batch | full `foodNutrients[203,204,205,208,269,291,301,303,307,539,418,...]` nested | map each raw ingredient → fdcId → scale by portion → sum across ingredients | `usda-fdc-recipe-breakdown` | unique: multi-ingredient aggregation from SR Legacy |
| 4 | Vegan/Vegetarian Compliance | `GET /food/{id}` | `ingredients` (string) | substring-scan against vegan-blocker keyword list (gelatin, casein, whey, carmine, lard, rennet, etc.) | `usda-fdc-ingredient-compliance` | **merged with #9** — identical endpoint, identical field, identical parse (substring scan); only the keyword list differs per question |
| 5 | Micronutrient Deficiency Target | `GET /food/{id}?nutrients=303,418,301,...` | specific entries in `foodNutrients` (iron 303, B12 418, calcium 301, etc.) | extract single nutrient value → compare against per-serving RDA | `usda-fdc-micronutrient-lookup` | unique: single-micronutrient extraction + RDA comparison |
| 6 | Macronutrient Profile Alignment | `GET /food/{id}` | `foodNutrients[203 protein, 204 fat, 205 carbs, 291 fiber, 539 added sugar]` | compute net carbs (205 − 291) + check macro ratio fits Keto/Paleo/high-protein | `usda-fdc-macro-alignment` | unique: macro-ratio parse (different fields + different math than #5) |
| 7 | Cumulative Daily Intake | `POST /foods` batch | `foodNutrients[307]` or any single tracked nutrient across the batch | sum per-item contributions → compare to daily limit | `usda-fdc-daily-intake-tally` | unique endpoint (POST /foods batch) + sum-and-threshold parse |
| 8 | Nutrient-Dense Allergy Substitution | `POST /foods/search` (dataType=Foundation) | search hits + their `foodNutrients[<target nutrient>]` | rank whole foods by density of a target nutrient given an allergy exclusion | `usda-fdc-nutrient-dense-substitute` | unique: Foundation-only rank-by-nutrient-density search |
| 9 | Hidden Allergen Detection | `GET /food/{id}` | `ingredients` (string) | substring-scan against top-9-allergen keyword list (peanut, soy, tree nut, gluten, dairy, egg, etc.) | `usda-fdc-ingredient-compliance` | **merged with #4** — byte-identical endpoint + field + parse strategy |
| 10 | Smart Label Scanner (health-condition risk) | `GET /food/{id}` | `labelNutrients.{sugars,addedSugar,fiber,sodium,saturatedFat,carbohydrates}` + `foodNutrients` per-100g + `servingSize` | cross-reference metrics against clinical thresholds (prediabetes / hypertension / PCOS) → plain-language verdict + confidence + ranked alternatives | `usda-fdc-label-scanner` | unique: clinical-threshold rule set + confidence scoring parse |
| 11 | Best Option Side-by-Side Comparison | `GET /food/{id}` on each candidate in parallel (OR `POST /foods` with 2-3 ids) | `foodNutrients[208,203,269,606 saturated fat], labelNutrients` | pairwise compare key metrics → pick winner explaining the dominant nutritional lever for user's goal | `usda-fdc-product-comparison` | unique: pairwise-compare + "dominant lever" parse |
| 12 | Cart Optimization (meal threshold alignment) | `POST /foods` batch → follow-up `POST /foods/search` for swaps | `foodNutrients[307,269,606]` aggregates + search for lower-impact swaps | sum cart → detect threshold exceedances per nutrient → suggest 1:1 swap per offending item | `usda-fdc-cart-optimization` | unique: 2-endpoint flow (batch aggregate + search-for-swap) |
| 13 | Threshold Tracking (remaining budget) | `GET /food/{id}` | single candidate food's `foodNutrients[<tracked nutrient>]` + `servingSize` | current_total + candidate_contribution vs daily_target → pass/fail with margin + same-category alternatives if fail | `usda-fdc-threshold-tracking` | unique: running-total projection parse on a single candidate |
| 14 | Healthy Swap Engine | `GET /food/{id}` (original) → `POST /foods/search` (alternatives in Branded) | original's `ingredients` + `foodNutrients` + `labelNutrients`; candidates' same fields | fetch original → search same-category Branded → rank alternatives by cleaner ingredient list + better macros | `usda-fdc-healthy-swap` | unique: 2-endpoint flow (fetch + search-alternatives) with ingredient-vs-ingredient ranking |

## Merge summary

- **14 user-proposed abilities → 13 distinct skills.**
- Single merge: **#4 (Vegan check) + #9 (Hidden allergen detection) → `usda-fdc-ingredient-compliance`**. Both read only `ingredients` from `GET /food/{fdcId}` and both do a case-insensitive substring scan against a keyword list. The only per-question difference is *which* keyword list (vegan blockers vs top-9 allergens), which is a runtime input to the skill, not a per-skill logic difference. This is the canonical worked example from `phase-1-ability-mapping.md` § "Worked Example: USDA".
- Every other ability has either a unique endpoint set, a unique field subset, or a unique parse strategy. Per iron law #1 (strict merge), similarity alone does not justify merging.

## Why we did NOT merge #5 + #6

Both call `GET /food/{id}` but read non-overlapping nutrient subsets (micronutrients 301/303/418 vs macronutrients 203/204/205/291/539) and apply different math (RDA threshold vs macro-ratio check). A rewrite optimizing one skill would not transfer to the other, so merging them recreates the confounding problem this protocol exists to prevent.

## Why we did NOT merge #7 + #12

Both use `POST /foods` batch but #12 adds a second endpoint (`POST /foods/search` for swap suggestions) and a substantially different parse (per-item offender detection + 1:1 swap recommendation). Different endpoint set → different skill.

## Why we did NOT merge #11 + #14

Both compare products, but #11 is a 2-candidate pairwise compare (inputs supplied by the user), while #14 is an original-vs-search-discovered-alternatives rank. #14 adds `POST /foods/search` to the endpoint set. Different endpoints → different skills.

## Skill slugs (for Phase 2 scaffolding)

1. `usda-fdc-dining-out`
2. `usda-fdc-low-sugar-snack`
3. `usda-fdc-recipe-breakdown`
4. `usda-fdc-ingredient-compliance`  *(absorbs vegan-check + allergen-scan)*
5. `usda-fdc-micronutrient-lookup`
6. `usda-fdc-macro-alignment`
7. `usda-fdc-daily-intake-tally`
8. `usda-fdc-nutrient-dense-substitute`
9. `usda-fdc-label-scanner`
10. `usda-fdc-product-comparison`
11. `usda-fdc-cart-optimization`
12. `usda-fdc-threshold-tracking`
13. `usda-fdc-healthy-swap`
