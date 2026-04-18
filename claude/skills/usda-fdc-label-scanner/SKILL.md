---
name: usda-fdc-label-scanner
description: Use when a user with a chronic condition (prediabetes, hypertension, PCOS, CKD, high cholesterol) asks whether a specific packaged food is a safe choice — fetches FDC detail, cross-references added-sugar/fiber/net-carbs/sodium/saturated-fat against the condition's clinical thresholds, returns plain-language verdict + confidence + ranked alternatives.
---

# USDA FDC — Smart Label Scanner (Health-Condition Risk)

## When to Use

The user discloses a chronic condition and asks a go/no-go question about a packaged product. Examples: "I'm prediabetic — are Nature Valley Oats 'n Honey bars a good snack?", "I have hypertension, is this canned soup OK?", "PCOS-friendly: Chobani flip yogurts yes or no?". The user wants a plain-language verdict, not just nutrient numbers.

## API Surface

- **Endpoint:** `GET /food/{fdcId}?format=full` (optionally preceded by `GET /foods/search` to resolve product name)
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read:** `labelNutrients.{sugars, addedSugar, fiber, sodium, saturatedFat, carbohydrates, calories, protein}`, `foodNutrients` per-100g backstop, `servingSize`, `servingSizeUnit`, `householdServingFullText`, `ingredients`

## Condition rule sets (per serving)

| Condition | Watch-out thresholds |
|---|---|
| Prediabetes / type-2 risk | added sugar > 6 g → red; fiber < 3 g AND net carbs > 20 g → red; ratio (net_carbs / fiber) > 10 → amber |
| Hypertension (DASH-aligned) | sodium > 400 mg/serving → red; > 230 mg/serving = "moderate" if daily limit is 1,500 mg |
| PCOS / insulin-resistance | added sugar > 8 g → red; saturated fat > 5 g → amber; trans fat > 0 → red |
| High cholesterol | saturated fat > 5 g → red; trans fat > 0 → red; dietary fiber ≥ 5 g → green signal |
| CKD stage 3+ | sodium > 200 mg → red; potassium > 300 mg → amber; phosphorus > 150 mg → amber |

## Minimal Happy Path

```bash
# Fetch full Branded detail and extract per-serving label nutrients
curl -s "https://api.nal.usda.gov/fdc/v1/food/1955793?format=full&api_key=${USDA_FDC_API_KEY}" \
  | jq '{serving: .servingSize, unit: .servingSizeUnit, label: .labelNutrients}'
```

## API Quirks

- **`labelNutrients` is Branded-only AND per serving.** `foodNutrients` is per 100 g on Foundation/SR Legacy/Survey and ALSO stored per 100 g on Branded. If the user's question is about a Branded packaged food, prefer `labelNutrients` — it matches the printed nutrition-facts panel the user is actually reading.
- `labelNutrients` sub-objects are shaped `{value: number}` — e.g. `labelNutrients.sugars.value`. Account for missing keys (e.g. `addedSugar` may not be present on older entries).
- `labelNutrients.calories` vs `foodNutrients[208]` may differ slightly due to rounding — prefer the labelNutrients value for display, foodNutrients for calculation.
- **Net carbs** for the prediabetes rule = `labelNutrients.carbohydrates.value − labelNutrients.fiber.value`. If fiber is missing, say so explicitly.
- 404 on a nonexistent fdcId returns an **empty body** (not JSON). Check `status == 404` before parsing.
- Every verdict the skill returns should include a **confidence score (0–100 %)** and a **list of 2-3 ranked better alternatives** (hand-curated per condition — this skill does NOT dispatch a search; the alternatives are supplied as part of the skill's rule set).

## Common Mistakes

(to be populated during the refinement loop)
