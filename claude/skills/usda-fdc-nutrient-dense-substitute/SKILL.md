---
name: usda-fdc-nutrient-dense-substitute
description: Use when a user is excluded from a major food group (dairy allergy, vegan, gluten-free, nightshade-free) and asks which whole foods naturally cover the nutrient they are now missing — searches FDC Foundation foods ranked by density of the target nutrient.
---

# USDA FDC — Nutrient-Dense Whole-Food Substitutes

## When to Use

The user can no longer eat a food group they relied on for a key nutrient, and wants natural alternatives. Examples: "I'm dairy-allergic, how do I get enough calcium from whole foods?", "Vegan and need iron — best plant sources?", "Low-potassium diet — what greens can I still eat?". The answer is a ranked list of **Foundation** (whole-food) items ordered by per-100 g density of the target nutrient, ideally excluding the off-limits food group.

## API Surface

- **Primary endpoint:** `POST /foods/search` with `dataType: ["Foundation"]` (Foundation = FDC's curated whole-food dataset; nutrient values are per 100 g and consistently populated)
- **Fallback:** `SR Legacy` (older FDA whole-food database) if Foundation returns too few hits
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Request body:** `{"query": "<category keyword>", "dataType": ["Foundation"], "pageSize": 50}`
- **Key fields read:** `description`, `foodCategory`, `foodNutrients[]` flat (look for the target `nutrientNumber`), optional `GET /food/{id}` for more precise values

## Minimal Happy Path

```bash
# Find Foundation foods rich in calcium (301), sort desc
curl -s -X POST "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=${USDA_FDC_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"query":"greens","dataType":["Foundation","SR Legacy"],"pageSize":50}' \
  | jq '.foods | map({
      fdcId, description,
      calcium_mg_per_100g: (.foodNutrients[] | select(.nutrientNumber=="301") | .value)
    }) | map(select(.calcium_mg_per_100g != null)) | sort_by(-.calcium_mg_per_100g) | .[0:10]'
```

## API Quirks

- **`"SR Legacy"` has a space** — spell it exactly `"SR Legacy"`, never `"SRLegacy"` or `"SR_Legacy"` (returns 0 results silently).
- Foundation is the **smaller, more accurate** dataset (~1,000 foods) — prefer it for density rankings. SR Legacy (~8,000 items) is broader but some entries are deprecated. When Foundation returns < 5 hits, fall back to `["Foundation", "SR Legacy"]` combined.
- **`foodNutrients` in search results is FLAT** with `value` + `nutrientNumber`. Nutrient numbers are strings.
- Foundation foods return values per 100 g — this is exactly what you want for density rank, no serving-size conversion needed.
- When the user names an exclusion (e.g. "I'm dairy-allergic"), the skill should filter out the off-limits category *after* the search (e.g. drop `foodCategory == "Dairy and Egg Products"`). The API has no exclusion filter.
- Key nutrient numbers: calcium `"301"`, iron `"303"`, potassium `"306"`, magnesium `"304"`, zinc `"309"`, B-12 `"418"` (note: B-12 is essentially absent from plants — for a vegan asking about B-12, the skill should disclose "fortified foods or supplementation is required; no unfortified plant source is meaningful").
- Returning 5-10 ranked hits with brief "one-line why" descriptions is more actionable than a raw nutrient-density dump.

## Common Mistakes

(to be populated during the refinement loop)
