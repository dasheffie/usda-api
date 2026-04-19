---
name: usda-fdc-nutrient-dense-substitute
description: Use when a user is excluded from a major food group (dairy allergy, vegan, gluten-free, nightshade-free) and asks which whole foods naturally cover the nutrient they are now missing — searches FDC Foundation foods ranked by density of the target nutrient. Also handles branded-product screening against clinical constraints (PCOS, hypertension, high cholesterol, prediabetes, CKD) via `GET /food/{id}` + `labelNutrients`, with conservative fallbacks when fields are missing.
---

# USDA FDC — Nutrient-Dense Whole-Food Substitutes

## When to Use

The user can no longer eat a food group they relied on for a key nutrient, and wants natural alternatives. Examples: "I'm dairy-allergic, how do I get enough calcium from whole foods?", "Vegan and need iron — best plant sources?", "Low-potassium diet — what greens can I still eat?". The answer is a ranked list of **Foundation** (whole-food) items ordered by per-100 g density of the target nutrient, ideally excluding the off-limits food group.

**Branded-product clinical screening:** when the user asks if a *specific branded product* is safe/optimal for a condition (PCOS, hypertension, high cholesterol, prediabetes, CKD), use `GET /food/{id}` and read `labelNutrients` (per-serving, not per-100g). Return a verdict plus **explicit confidence tier** (HIGH if all critical nutrients present; MEDIUM if one is missing; LOW if a condition-critical nutrient like phosphorus for CKD is absent). See Clinical Screening Table below.

## API Surface

- **Primary endpoint:** `POST /foods/search` with `dataType: ["Foundation"]` (Foundation = FDC's curated whole-food dataset; nutrient values are per 100 g and consistently populated)
- **Fallback:** `SR Legacy` (older FDA whole-food database) if Foundation returns too few hits
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Request body:** `{"query": "<category keyword>", "dataType": ["Foundation"], "pageSize": 50}`
- **Key fields read:** `description`, `foodCategory`, `foodNutrients[]` flat (look for the target `nutrientNumber`), optional `GET /food/{id}` for more precise values
- **Branded foods (`dataType: "Branded"`):** `GET /food/{id}` returns `labelNutrients` keyed by common names (`calories, protein, carbohydrates, sugars, addedSugar, fat, saturatedFat, transFat, cholesterol, sodium, fiber, calcium, iron, potassium, phosphorus`). Values are **per `servingSize`** (also returned, in `servingSizeUnit`), NOT per 100g. Always read `servingSize` + `householdServingFullText` and state the basis in your answer. Any field may be absent — treat missing as unknown, not zero.

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
- **Known Foundation gaps — go straight to SR Legacy for:** tempeh, nori, most named seaweeds (wakame/kelp/dulse), fortified plant milks, nutritional yeast. Foundation seaweed entries use opaque commercial names (e.g., `Canadian Cultivated EMI-TSUNOMATA`) — map them to common names (wakame/kombu/nori) in your answer rather than echoing the raw description.
- **Dry vs. cooked distortion:** dry legumes and dehydrated seaweeds report per-100 g values at ~0–10% moisture, so absolute numbers look 2–3× higher than per-serving reality. When ranking potassium, protein, iron in legumes/seaweeds, note that cooked values are ~⅓ of dry, and prefer cooked entries (`description` contains `cooked`, `boiled`) when the question implies a meal context.
- **`foodNutrients` in search results is FLAT** with `value` + `nutrientNumber`. Nutrient numbers are strings.
- Foundation foods return values per 100 g — this is exactly what you want for density rank, no serving-size conversion needed.
- When the user names an exclusion, filter **after** the search — the API has no exclusion parameter. Match on both `foodCategory` AND a description substring (category labels miss items where the allergen is an ingredient, and description-only misses plain-category items). Reference table:

  | Exclusion | Drop `foodCategory` contains | Drop `description` regex (case-insensitive) |
  |---|---|---|
  | Dairy allergy | `Dairy and Egg Products` | `milk\|cheese\|yogurt\|whey\|casein\|butter\|cream` |
  | Egg allergy | `Dairy and Egg Products` | `\begg\b\|albumen` |
  | Gluten-free | `Cereal Grains and Pasta`, `Baked Products` | `wheat\|rye\|barley\|spelt\|kamut\|triticale\|farro\|semolina\|bulgur` |
  | Soy-free | — | `\bsoy\|tofu\|tempeh\|edamame\|miso\|natto` |
  | Nightshade-free | — | `tomato\|potato\|eggplant\|pepper\|paprika\|goji` (allow sweet potato) |
  | Vegan | `Dairy and Egg Products`, `Beef`, `Pork`, `Poultry`, `Finfish\|Shellfish`, `Lamb\|Veal\|Game`, `Sausages and Luncheon Meats` | — |
  | Shellfish | `Finfish and Shellfish Products` | `shrimp\|crab\|lobster\|clam\|oyster\|mussel\|scallop` |
- **Nutrient number reference** (strings; pass exactly). Using the wrong number silently returns 0 — double-check here before searching:

  | Nutrient | # | Nutrient | # |
  |---|---|---|---|
  | Protein | `203` | Total fiber | `291` |
  | Calcium | `301` | Iron | `303` |
  | Magnesium | `304` | Phosphorus | `305` |
  | Potassium | `306` | Zinc | `309` |
  | Vitamin C | `401` | Folate, total | `417` |
  | Vitamin B-12 | `418` | Choline, total | `421` |
  | Vitamin D (D2+D3) | `328` | ALA (plant ω-3, 18:3 n-3) | `851` |
  | EPA (fish ω-3, 20:5 n-3) | `629` | DHA (fish ω-3, 22:6 n-3) | `621` |

  - **Vitamin D:** always use `328` (D2+D3 combined, mcg). `324` is IU, `325`/`326` are D2/D3 split and often null. Don't use them unless the user asks for IU.
  - **Omega-3:** for plant/vegan contexts use `851` (ALA). `629`/`621` (EPA/DHA) are fish-only and return 0 for plants — if the user is vegan, skip them and state that EPA/DHA require algae-oil supplementation.
  - **B-12:** essentially absent from plants. For vegans, state up front that fortified foods or supplementation is required; do not rank unfortified plant sources as a meaningful answer. Tempeh/seaweed trace amounts (~0.1 mcg) do NOT meet the 2.4 mcg/day RDA.
  - **Choline (`421`) is sparsely populated** in Foundation — most vegetables and grains return null, not zero. Expect only nuts, seeds, and a few legumes to have values; note the gap when answering.
- Returning 5-10 ranked hits with brief "one-line why" descriptions is more actionable than a raw nutrient-density dump.
- **Clinical screening thresholds** (per serving, apply against `labelNutrients`; cite tier + missing-field caveats):

  | Condition | Red flags (per serving) | Critical fields | If missing |
  |---|---|---|---|
  | Hypertension | sodium > 480 mg; realistic 2-3× consumption pushes daily load toward 2,300 mg cap (1,500 mg strict) | sodium | LOW conf. **Every clinical verdict (including CAUTION/partial) MUST cite a confidence tier (HIGH/MEDIUM/LOW) in the answer** — a verdict without an explicit tier is incomplete. |
  | High cholesterol | saturated fat > 5 g; added sugar > 10 g (drives triglycerides); trans fat > 0 | saturatedFat, addedSugar, transFat | MEDIUM conf |
  | PCOS / Prediabetes | added sugar > 6 g; carb:protein > 3:1; low fiber (< 3 g) | addedSugar, sugars, carbs, protein, fiber | if `addedSugar` missing, **conservatively assume all `sugars` are added** AND drop confidence to MEDIUM AND name the missing field in the answer. In head-to-head rankings, if both products have null `addedSugar`, do NOT declare a winner on sugar — rank on a non-null secondary axis (fiber, protein, sat fat) and flag the unresolved sugar tie. |
  | CKD stage 3+ | sodium > 400 mg; potassium > 250 mg; phosphorus > 150 mg | sodium, potassium, phosphorus | **phosphorus missing ⇒ LOW confidence, even for a NOT-RECOMMENDED verdict. A K-or-Na flag alone does not upgrade confidence to HIGH while P is unknown — a P breach could still be present and the verdict's completeness is unverified.** |
- **Marketing-vs-label discrepancy:** a branded `description` claim ("Naturals", "Lightly Salted", "Heart Healthy") is not regulated nutrition data. If labelNutrients contradicts the claim (e.g., 5 g saturated fat in "Naturals" popcorn), lead with the numeric value and note the discrepancy.
- **Data-quality sanity check:** if a labelNutrients value looks implausible for the food (e.g., 5 g protein in a meat pot pie, or sodium that matches the full container weight rather than `servingSize`), flag it and lower confidence — do not silently pass the number through.
- **Multi-nutrient queries** (e.g., CKD = low K + low P; "protein AND iron"): read all target `nutrientNumber`s in one pass, drop rows where any required nutrient is null, then rank by the primary (or by a normalized composite). For "low X AND low Y" constraints, sort ascending on the sum or filter by explicit thresholds — don't rank by a single nutrient and hope the other falls in line.
- **Out-of-scope clinical classifications:** FDC has no flags for low-FODMAP, glycemic index, oxalate load, or histamine. When the user asks for these, answer the FDC-computable part (nutrient density + allergen exclusion) and explicitly flag the clinical axis as requiring external verification — do not silently treat every legume as low-FODMAP or every leafy green as low-oxalate.
- **Bioavailability caveat:** per-100 g values measure content, not absorbed dose. Plant calcium (oxalate-bound in spinach), non-heme iron, and plant choline absorb at 20–50% of animal-source rates — mention this when ranking plant substitutes for a nutrient the user previously got from animal foods.

## Common Mistakes

- Using nutrient `694` for choline — `694` is trans-dienoic fatty acids. Choline total is `421`.
- Using EPA (`629`) or DHA (`621`) for a vegan omega-3 question — these are fish-only and return 0. Use ALA (`851`) for plants.
- Assuming `foodCategory` alone excludes an allergen — a "Baked Products" entry may contain dairy without being in "Dairy and Egg Products". Combine category + description regex.
- Ranking dry legumes/seaweeds per 100 g without noting the dry-weight distortion.
- Searching with overly broad queries (`"vegetables grains legumes nuts seeds meats fish"`) — prefer targeted queries (`"seeds nuts"`, `"legumes"`) then merge results; broad queries waste the 50-hit pageSize and still miss niche items like tempeh/nori that need SR Legacy.
- **Branded search disambiguation:** for branded-product lookups (e.g., `"Chobani Zero Sugar"`), add `dataType: ["Branded"]` and include the product form in the query (`"Chobani Zero Sugar yogurt"`) — bare brand queries return unrelated SKUs. If the top hit's `description`/`brandOwner` doesn't match, filter results by `foodCategory` (e.g., `Yogurt`) before picking the `fdcId`. **Never search a bare generic query like `"granola bar"` or `"yogurt"` for a branded-product question** — the returned `fdcId` will be arbitrary and not the user's intended SKU. If the user has not named a brand, ask for one before calling `GET /food/{id}`.
- **Head-to-head comparisons:** when ranking two branded products, verify the two `fdcId`s are DIFFERENT before presenting a winner. If both search paths collapse to the same `fdcId`, re-query the missing product with a more specific brand+form+flavor query (e.g., `"Ben & Jerry's Vanilla Ice Cream pint"`) or state that the second product could not be resolved — do not compare a record to itself.
- **Answering with missing critical data:** never fabricate a verdict from absent fields. If a condition-critical nutrient (phosphorus for CKD, addedSugar for prediabetes/PCOS) is missing, state LOW/MEDIUM confidence, name the missing field, and recommend the conservative action (assume worst-case, or request a full panel).
- **Null-safe formatting (load-bearing for user-facing answers):** before printing any `labelNutrients` value, null-check it. Render missing values as the literal token `missing` (e.g., `phosphorus: missing`, `addedSugar: missing`), never `None`, `Noneg`, `Nonemg`, or `null`. Emitting `Noneg`/`Nonemg` is a correctness bug — the user cannot distinguish a bad unit from a missing field.
- **Round label-style floats:** `labelNutrients` values arrive as floats and often render as `2.99g`/`4.08g`/`4.01g` (a rendering artifact, not label precision). Round to 1 decimal for display AND for threshold comparisons (e.g., compare `round(fiber, 1) < 3`, not the raw float) — otherwise `fiber=2.99` flags as `<3g` when the label says 3 g. For sodium/potassium/phosphorus round to the nearest whole mg.
