---
name: usda-fdc-macro-alignment
description: Use when a user asks whether a specific food fits a macro-based diet (Keto, Paleo, high-protein, low-carb, low-fat) — fetches FDC detail, extracts protein/fat/total carbs/fiber/added-sugar and computes net carbs + macro ratio against the named diet's rule.
---

# USDA FDC — Macronutrient Profile Alignment

## When to Use

The user names a specific diet (Keto / Paleo / high-protein / low-fat / carnivore / Mediterranean / DASH) and asks whether a specific food or meal item "fits" that diet's macro rules. Examples: "Does a medium Hass avocado fit my Keto macros?", "Is quinoa too carb-heavy for Paleo?", "Can I hit 40 g protein with this chicken breast?".

## API Surface

- **Endpoint:** `GET /food/{fdcId}?format=full` (or with `nutrients=203,204,205,291,539` to trim payload)
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read:** `foodNutrients` entries for nutrient numbers `"203"` (protein), `"204"` (total fat), `"205"` (total carbohydrate), `"291"` (dietary fiber), `"539"` (added sugars), `"208"` (energy kcal), `servingSize`, `servingSizeUnit`, `labelNutrients` (Branded per-serving)

## Macro math

| Metric | Formula |
|---|---|
| Net carbs (g) | `total_carbs (205) − fiber (291)` |
| Energy from protein | `4 × protein_g` |
| Energy from carbs (net) | `4 × net_carbs_g` |
| Energy from fat | `9 × fat_g` |
| Keto rule | `net_carbs_g ≤ 10 per serving` AND `fat_energy % ≥ 70 %` |
| Paleo rule (heuristic) | no added sugars (539 == 0), no grains (check `description` for "wheat", "rice", "corn"), no legumes |
| High-protein rule | `protein_g ≥ 20 per serving` OR `protein_energy % ≥ 25 %` |

## Minimal Happy Path

```bash
# All macros for Hass avocado (SR Legacy fdcId 171706)
curl -s "https://api.nal.usda.gov/fdc/v1/food/171706?format=full&nutrients=203,204,205,291,539,208&api_key=${USDA_FDC_API_KEY}" \
  | jq '.foodNutrients[] | {num: .nutrient.number, amount: .amount, unit: .nutrient.unitName}'
```

## API Quirks

- **Nutrient numbers are STRINGS.** Match `.nutrient.number === "205"`, not `=== 205`.
- **Basis differs by dataType.** Foundation / SR Legacy foodNutrients are per 100 g. Branded stores foodNutrients per 100 g AND `labelNutrients` per serving. Mixing the two silently produces wrong ratios.
- **Convert to per-serving** before evaluating diet rules: `per_serving = per_100g × servingSize / 100` (only when `servingSizeUnit == "g"` or `"ml"`).
- **Net carbs = 205 − 291.** US nutrition labels never print "net carbs" — it has to be computed. If fiber is missing from the response, assume 0 and disclose the assumption in the answer.
- **Added sugar (539)** is NOT always present even on Branded foods — it is a newer FDA-mandated field. Absence ≠ zero; disclose "added sugar data not available" if 539 is missing.
- Paleo rules are heuristic and contested. The skill should disclose the rule set it applied (e.g. "Paleo excludes grains and legumes; I used that rule").

## Common Mistakes

(to be populated during the refinement loop)
