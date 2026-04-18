---
name: usda-fdc-threshold-tracking
description: Use when a user names their current intake of a constrained nutrient and a candidate next food, and asks whether the candidate keeps them under their daily target — fetches the candidate's contribution, projects the running total, returns pass/fail with tight-margin warnings and same-category alternatives on fail.
---

# USDA FDC — Running-Total Threshold Projection

## When to Use

The user has a daily nutrient budget (e.g. 25 g added sugar), reports their current day's intake (e.g. "I've had 15 g already"), and names a candidate food to possibly eat next. The skill fetches the candidate's nutrient contribution, projects `current + candidate` vs the daily target, returns pass/fail with margin. If over, suggests same-category alternatives.

## API Surface

- **Primary endpoint:** `GET /food/{fdcId}?format=full` on the candidate (single fetch)
- Preceded by `GET /foods/search` if the candidate is named but fdcId is unknown
- Optional follow-up: `POST /foods/search` for same-category alternatives when the projection fails
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read:** `labelNutrients.<tracked>.value`, fallback to `foodNutrients` per-100g × `servingSize/100`, `description`, `brandedFoodCategory`

## Minimal Happy Path

```bash
# User: "15g added sugar so far, can I have Yoplait Original Strawberry Yogurt?"
curl -s "https://api.nal.usda.gov/fdc/v1/food/2587575?format=full&api_key=${USDA_FDC_API_KEY}" \
  | jq '{desc: .description, serving: .servingSize, addedSugar_g: .labelNutrients.addedSugar.value}'
# Project: 15 + 12 = 27 g, target 25 g, overage = 2 g → tight overage warning
```

## Tracked-nutrient + typical target cheat-sheet

| Nutrient | Field (labelNutrients) | Typical daily target |
|---|---|---|
| Added sugar | `addedSugar.value` | 25 g WHO / 36 g AHA M |
| Sodium | `sodium.value` | 2,300 mg FDA / 1,500 mg AHA |
| Saturated fat | `saturatedFat.value` | < 13 g on 2,000 kcal |
| Total carbs | `carbohydrates.value` | varies (keto ≤ 50 g/day) |
| Calories | `calories.value` | user-supplied |

## Pass/fail verdict structure

The skill's output must always include:

1. **Arithmetic:** `current + candidate = projected`
2. **Verdict:** `PASS` / `TIGHT_OVER` / `CLEAR_OVER` based on margin
3. **Guidance:**
   - PASS → approve with remaining-budget note
   - TIGHT_OVER (≤ 10 % over) → "acceptable once but not a daily habit"
   - CLEAR_OVER (> 10 % over) → name 2 cleaner same-category swaps (e.g. Chobani Zero Sugar Strawberry instead of Yoplait Original)
4. **Confidence:** `labelNutrients` present → 90-95 %; fallback to `foodNutrients × servingSize/100` → 70-80 %; missing data → disclose

## API Quirks

- **Prefer `labelNutrients` per-serving over `foodNutrients × servingSize/100`** — the user's mental model is "this serving", and labelNutrients matches the printed box.
- `labelNutrients` sub-objects are `{value: number}` — `.labelNutrients.addedSugar.value`. Guard against missing keys (older Branded entries don't have `addedSugar`). If missing, fall back to `foodNutrients` nutrient number `"539"` and disclose.
- **Nutrient numbers are strings.** Added sugar = `"539"`, total sugar = `"269"` — they are DIFFERENT metrics. The user almost always cares about added sugar (539) when tracking blood-sugar impact.
- **404 on nonexistent fdcId returns an empty body** (no JSON). Check `status == 404` before parsing.
- Serving-size conversions are only safe when `servingSizeUnit == "g"` or `"ml"`. For household units (e.g. `"TBSP"`) without a gram weight, disclose the approximation.
- Same-category swap search: use `brandedFoodCategory` as the search keyword with a "low sugar" or "zero sugar" prefix — e.g. category "Yogurts & Cultured Dairy" + offender's added-sugar value → search `"zero sugar yogurt"`.
- Always quote both the user's **current** intake and the candidate's **projected** total so they can verify the math.

## Common Mistakes

(to be populated during the refinement loop)
