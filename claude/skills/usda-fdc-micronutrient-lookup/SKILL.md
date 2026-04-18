---
name: usda-fdc-micronutrient-lookup
description: Use when a user asks how much of a specific micronutrient (iron, Vitamin B12, calcium, magnesium, zinc, vitamin D, folate, potassium, etc.) is in a particular food — fetches the FDC detail record and extracts the per-serving value for the requested nutrient, comparing to the adult RDA.
---

# USDA FDC — Micronutrient Lookup

## When to Use

The user has a doctor-diagnosed deficiency or wants to verify a supplement-worthy nutrient amount in a specific food. Examples: "Is this pasta a good source of iron?", "How much Vitamin B12 does this yogurt have?", "Does this cereal cover my daily calcium?". The question names **one** micronutrient — if the user asks for the full macro breakdown instead, route to `usda-fdc-macro-alignment` or `usda-fdc-recipe-breakdown`.

## API Surface

- **Endpoint:** `GET /food/{fdcId}?format=full&nutrients=<comma-separated nutrient numbers>` (the `nutrients` filter trims payload; optional but cheaper)
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read:** `foodNutrients[].nutrient.number`, `foodNutrients[].amount`, `foodNutrients[].nutrient.unitName`, `servingSize`, `servingSizeUnit`, `labelNutrients` (Branded only)

## Key nutrient numbers (USDA canonical)

| Nutrient | Number |
|---|---|
| Iron (Fe) | `"303"` |
| Calcium (Ca) | `"301"` |
| Vitamin B-12 | `"418"` |
| Vitamin D (D2 + D3) | `"324"` |
| Magnesium | `"304"` |
| Zinc | `"309"` |
| Potassium | `"306"` |
| Folate (total) | `"417"` |
| Vitamin C | `"401"` |
| Vitamin A (RAE) | `"320"` |

## Minimal Happy Path

```bash
# Get ONLY iron (303) + calcium (301) for fdcId 1750340, full format
curl -s "https://api.nal.usda.gov/fdc/v1/food/1750340?format=full&nutrients=303,301&api_key=${USDA_FDC_API_KEY}" \
  | jq '.foodNutrients[] | {num: .nutrient.number, name: .nutrient.name, amount: .amount, unit: .nutrient.unitName}'
```

## API Quirks

- **Nutrient numbers are STRINGS, not integers.** `foodNutrients[].nutrient.number === "303"`, never `=== 303`.
- **Basis differs by dataType.** Foundation / SR Legacy / Survey foodNutrients are **per 100 g**. Branded foodNutrients are also stored per 100 g (LCCS-derived), but **`labelNutrients` is per serving** as printed on the nutrition-facts panel.
- To convert per-100 g → per-serving, multiply by `servingSize / 100`. Check `servingSizeUnit` — only safe to do this math when it is `"g"` or `"ml"` (density ≈ 1 g/ml for most liquids).
- **`foodNutrients` shape differs between `?format=full` and `?format=abridged`.** Full: nested `{nutrient: {number, name, unitName}, amount, ...}`. Abridged: flat `{number, name, amount, unitName}`. When you pick a format, parse consistently.
- Category-header entries (e.g. `{"nutrient": {"number": "951", "name": "Proximates"}, ...}`) have no `amount` field. Filter them out.
- RDA reference (adult, IOM 2023 baseline): iron 18 mg (women) / 8 mg (men), calcium 1000 mg, B-12 2.4 µg, vitamin D 15 µg, magnesium 400 mg, zinc 11 mg, potassium 3400 mg, folate 400 µg DFE, vitamin C 90 mg, vitamin A 900 µg RAE.

## Common Mistakes

(to be populated during the refinement loop)
