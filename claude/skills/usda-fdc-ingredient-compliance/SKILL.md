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
- Ingredient strings are run-on text with parentheticals for sub-ingredients (e.g. `"CHOCOLATE COATING (SUGAR, COCOA BUTTER, MILK, ...)")`. Plan for "ingredient of ingredient" matches — `"milk"` must be found inside `"(..., MILK, ...)"`.
- Common vegan blockers to match: `gelatin`, `casein`, `whey`, `lactose`, `carmine`, `cochineal`, `shellac`, `confectioner's glaze`, `lard`, `tallow`, `rennet`, `honey`, `milk`, `butter`, `egg`, `isinglass`, `L-cysteine`.
- Top-9 allergen families: `milk`/`dairy`, `egg`, `fish`, `shellfish`/`crustacean`, `tree nut` (almond, cashew, walnut, pecan, pistachio, hazelnut, Brazil, macadamia), `peanut`, `wheat`/`gluten`, `soy`/`soya`/`soybean`, `sesame`.
- The `allergens` summary field is not universally populated — always cross-check by substring-scanning `ingredients` even when an `allergens` string is returned.

## Common Mistakes

(to be populated during the refinement loop)
