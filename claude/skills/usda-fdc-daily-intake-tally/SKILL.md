---
name: usda-fdc-daily-intake-tally
description: Use when a user tracking a strict nutrient limit (sodium for hypertension, added sugar for diabetes, saturated fat for cardiac risk) asks whether their day's meals stayed under the limit — batch-fetches all meal fdcIds, sums the tracked nutrient, compares to the user's daily ceiling.
---

# USDA FDC — Cumulative Daily Intake Tally

## When to Use

The user names a specific nutrient they monitor (sodium, added sugar, saturated fat, potassium) and lists the meals/foods they ate today. The skill batch-fetches every meal's FDC record, sums the tracked nutrient across the day, compares to the user's daily ceiling, reports over/under with the top contributors.

## API Surface

- **Primary endpoint:** `POST /foods` batch with `{"fdcIds": [...], "format": "full"}`
- Optional preceding `GET /foods/search` if a meal is named but fdcId is unknown
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read:** `foodNutrients[]` entries for the tracked nutrient number, `servingSize`, `servingSizeUnit`, `labelNutrients` (Branded only)

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

## API Quirks

- **`POST /foods` returns a BARE ARRAY**, not `{foods: [...]}`. Parse as `response[0], response[1], ...`.
- **Batch cap = 20 fdcIds.** If the user listed 25 meals, split into 2 calls.
- **Empty `fdcIds: []` returns `{}` (empty object)** with HTTP 200, not an empty array and not an error — validate before calling.
- **`foodNutrients` in full format is nested** (`nutrient.number`, `amount`). Nutrient numbers are strings.
- **Values are per 100 g** on Foundation / SR Legacy / Survey AND on Branded (Branded LCCS-derived). For accurate daily tallies, scale by `servingSize / 100` when `servingSizeUnit == "g"` or `"ml"`.
- **For Branded items, `labelNutrients` is PER SERVING** and often more accurate than `foodNutrients × servingSize / 100` because it matches the printed box. Prefer labelNutrients when available.
- Always report: **(a) total**, **(b) comparison to limit** (e.g. "2,350 mg vs 2,000 mg = 350 mg over"), **(c) top 1-2 contributors** (which single meal drove the most of the total). Users need the top contributor to know what to swap tomorrow.
- Nutrient may be absent from a record — report "sodium data not available for meal X" rather than silently treating missing as 0.

## Common Mistakes

(to be populated during the refinement loop)
