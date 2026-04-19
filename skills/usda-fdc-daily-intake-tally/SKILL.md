---
name: usda-fdc-daily-intake-tally
description: Use when a user tracking a strict nutrient limit (sodium for hypertension, added sugar for diabetes, saturated fat for cardiac risk) asks whether their day's meals stayed under the limit — batch-fetches all meal fdcIds, sums the tracked nutrient, compares to the user's daily ceiling.
---

# USDA FDC — Cumulative Daily Intake Tally

## When to Use

The user names a specific nutrient they monitor (sodium, added sugar, saturated fat, potassium) and lists the meals/foods they ate today. The skill batch-fetches every meal's FDC record, sums the tracked nutrient across the day, compares to the user's daily ceiling, reports over/under with the top contributors.

## API Surface

- **Primary endpoint:** `POST /foods` batch with `{"fdcIds": [...], "format": "full"}`
- Preceding `GET /foods/search` per distinct meal name is REQUIRED (not optional) for any meal you don't already have an fdcId for. Consolidate: search each distinct food once, pick the top relevant fdcId from each, then do ONE `POST /foods` batch for all meals at once. **Branded items (Oreos, Doritos, Coke, Lay's, Snickers, Pop-Tart, Ritz, Chobani, Lean Cuisine, Campbell's, Vitamin Water, Ben & Jerry's, Starbucks drinks) MUST be searched** — they almost always have a Branded record with `labelNutrients`.
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read:** `foodNutrients[]` entries for the tracked nutrient number, `servingSize`, `servingSizeUnit`, `labelNutrients` (Branded only)

## MANDATORY EXECUTION LOOP (do not skip)

Before writing any answer, walk EVERY meal the user listed:

1. **Enumerate** the user's meals into an explicit list. Count them. The final per-item line count MUST equal this count (each meal is either tallied OR has an `excluded:` line — never silently dropped).
2. **For each meal, decide a path**: (a) search FDC and pick a fdcId, (b) decompose composite into 2–4 FDC components and search each, or (c) mark `excluded: <reason>` ONLY after at least 2 search variants returned nothing. There is NO fourth path — "skip silently" or "search failed → 0" is a bug.
3. **Search every distinct food** with `GET /foods/search?query=<term>&pageSize=25`. **"Search failed" is almost never true** — FDC has 300k+ foods and returns something for nearly every English word. If your first query returns zero hits, RETRY with: (i) just the head noun (`oatmeal`, not `Quaker maple and brown sugar oatmeal`; `milk`, not `2% milk`; `bagel`, not `Thomas' cinnamon raisin bagel`; `donut`, not `Dunkin' glazed donut`); (ii) drop apostrophes/punctuation (`Lays classic chips`, `Chick fil A spicy chicken sandwich`); (iii) for branded items also try `dataType=Branded` filter. Reporting `search failed` for staples like eggs, milk, bacon, butter, broccoli, apple, banana, steak, bread, rice, beans, salmon, chicken, yogurt, cheese, ice cream, soda, juice, cereal is ALWAYS a bug — those resolve trivially. Pick the top relevant hit even if not a perfect brand match (a generic `MILK, WHOLE` works for "whole milk"); state the proxy in the basis line.
4. **Batch all chosen fdcIds** into ONE `POST /foods` call (split at 20). If you reach this step with `fdcIds: []` because every search "failed", STOP — go back to step 3 and retry with shorter queries before emitting an answer.
5. **Emit a per-item line for every meal in the original list**, then total, then Top (Top is required even when total is 0 or every item failed — name the meal you would have flagged or write `Top: none (no items resolved — retry searches)`).

If the user said "top two" / "which two" / "biggest two", emit TWO Top lines.

## Minimal Happy Path

```bash
# Sum sodium across 3 meals (oatmeal, turkey sandwich, canned soup)
curl -s -X POST "https://api.nal.usda.gov/fdc/v1/foods?api_key=${USDA_FDC_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"fdcIds":[171287,1954907,2346393],"format":"full"}' \
  | jq '[.[] | {fdcId, desc: .description, sodium_mg_per_100g: (.foodNutrients[] | select(.nutrient.number=="307") | .amount)}]'
```

## Tracked nutrients + typical daily ceilings

| Nutrient | Number | Typical daily ceiling |
|---|---|---|
| Sodium | `"307"` | 2,300 mg (FDA) / 1,500 mg (AHA) |
| Added sugar | `"539"` | 25 g (WHO) / 36 g (AHA male) |
| Saturated fat | `"606"` | < 13 g on a 2,000 kcal diet (< 6 % cals) |
| Potassium | `"306"` | ≤ 2,000 mg (CKD) / 3,400 mg AI (general) |
| Dietary cholesterol | `"601"` | < 300 mg (many guidelines) |
| Energy (calories) | `"208"` (kcal) | user-stated kcal limit (e.g., 1,600 / 2,000 / 2,500) |

## API Quirks

- **`POST /foods` returns a BARE ARRAY**, not `{foods: [...]}`. Parse as `response[0], response[1], ...`.
- **Batch cap = 20 fdcIds.** If the user listed 25 meals, split into 2 calls.
- **Empty `fdcIds: []` returns `{}` (empty object)** with HTTP 200, not an empty array and not an error — validate before calling. **An empty `fdcIds` list means you skipped resolving items**: go back to step 1 of the execution loop and search them. Reporting a 0-total with `endpoints_called: []` when the user listed real foods is ALWAYS wrong.
- **`foodNutrients` in full format is nested** (`nutrient.number`, `amount`). Nutrient numbers are strings.
- **Values are per 100 g** on Foundation / SR Legacy / Survey AND on Branded. For daily tallies you MUST scale by the **actual eaten amount**, not the FDC `servingSize`: ask or assume a typical portion in grams, then `amount × grams / 100`. A canned soup at 683 mg sodium per 100 g is ~1,640 mg for a 240 g (1-cup) serving, NOT 683 mg.
- **For Branded items, `labelNutrients` is PER LABEL SERVING** and matches the printed box — prefer it, but still scale by `(eaten_servings)` if the user ate more/less than one label serving (a 20 oz Sprite = ~1.7 label servings). `labelNutrients` keys use lowercased nutrient names (`sodium`, `potassium`, `sugars`, `addedSugars`, `saturatedFat`, `cholesterol`); if the key for your tracked nutrient is missing, fall back to `foodNutrients[]` per-100g × label `servingSize` g — do NOT report 0 just because `labelNutrients.potassium` was absent on a Branded record.
- **Always state the basis per item in the per-item line** (`basis: labelNutrients × 1.7 servings` or `basis: per-100g × 240 g`) so the user can audit the math.
- **MANDATORY answer shape (every response, no shortcuts):**
  1. Per-item line for EVERY meal: `- <meal>: <amount> <unit> (basis: labelNutrients | per-100g × <serving_g>g | excluded: <reason>)`
  2. Total + comparison line: `Total <X> vs <limit> = <Y> over/under`
  3. Top contributor line: `Top: <meal> (<amount>, <pct>%)` — REQUIRED on EVERY response, no exceptions. Include it even when obvious, even when only one item was tallied, even when total is 0, and even when every search failed (in that last case write `Top: none (no items resolved — retry searches with shorter queries)`). If user asked "top two" / "which two" / "biggest two" / "worst offender" / "biggest contributor" / "spiked the most", emit the requested number of `Top:` lines.
  Never collapse items into "Five items" / "Mixed foods" / "Multiple items" — the user must be able to verify and know what to swap.
  **Self-check before sending:** count per-item lines (tallied + excluded) and confirm it equals the count of meals the user listed. If it doesn't, you dropped items — go back and resolve them.
- Nutrient may be absent — report "sodium data not available for meal X" rather than silently treating missing as 0; never fold a missing item into the total without disclosure.

## Common Mistakes

- **Composite / restaurant items have no FDC entry.** Chipotle bowls, Subway sandwiches, Panera bread bowls, grilled cheese, "oatmeal with raisins", "black beans and rice", "pasta primavera", "beef stroganoff", "mac and cheese", "chicken salad", "egg bites", homemade baklava, mole-sauce chicken, Indian korma, Lean Cuisine entrées (alfredo/salmon), Chick-fil-A biscuit, KFC chicken bucket — none resolve cleanly to a single fdcId. **DEFAULT IS DECOMPOSITION**, not exclusion: break the dish into 2–4 FDC-resolvable components (grilled cheese → bread + cheese + butter; Chipotle bowl → rice + black beans + chicken + salsa; oatmeal with raisins → oats + raisins; black beans and rice → black beans + white rice; pasta primavera → pasta + olive oil + mixed vegetables; beef stroganoff → beef + egg noodles + sour cream; mac and cheese → macaroni + cheddar + butter) and search/fetch each. Only exclude after you have searched the components AND they all returned nothing useful. Never exclude a composite without first attempting decomposition — "excluded: composite/homemade recipe" without component searches is ALWAYS a bug.
- **Unknown / under-specified items.** If the user says "a muffin" with no brand/size, ask one clarifying question (brand or grams) before estimating. If you must estimate, state the assumed proxy and grams explicitly ("assumed: generic blueberry muffin, 113 g").
- **Total sugar (269) vs Added sugar (539) — DO NOT CONFLATE.** When tallying added sugar, fruit (orange, strawberries), 100% juice (Tropicana OJ), plain milk/yogurt, and sugar-free products (Jell-O sugar-free, Diet Sprite) contribute **0 g added sugar** even though they have natural/lactose sugar in nutrient 269. If a record lacks 539 but has 269, do NOT substitute 269 — report "added sugar not labeled" or 0 for whole-food fruits/dairy.
