---
name: usda-fdc-recipe-breakdown
description: Use when a user types a homemade recipe (ingredient list with quantities) and wants an exact macronutrient + micronutrient breakdown — resolves each ingredient to an SR Legacy / Foundation fdcId, batch-fetches the details, scales by user portion, and sums across ingredients.
---

# USDA FDC — Exact Homemade Recipe Breakdown

## When to Use

The user describes a meal they made from scratch with specific ingredients and quantities (e.g. "1 cup spinach + 1 banana + 1 cup whole milk", "4 oz chicken breast + 1 tbsp olive oil + 1 cup brown rice") and wants the exact nutritional profile. The skill maps each raw ingredient to its best FDC whole-food record, scales by the user's portion, and sums.

## API Surface

Two-endpoint flow:

1. **`GET /foods/search`** per ingredient to resolve name → fdcId. Prefer `dataType=["Foundation"]` or `["SR Legacy"]` for whole foods; avoid Branded unless the user specified a brand.
2. **`POST /foods`** to batch-fetch full nutrient detail for all resolved fdcIds in one call (cap: 20 items).

- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Request body (batch):** `{"fdcIds": [171706, 173944, ...], "format": "full"}`
- **Key fields read:** `foodNutrients[]` nested full-format entries. **Canonical USDA nutrient numbers** (these are the ONLY correct codes — do not guess; `298` is NOT sodium):
  - `"208"` Energy (kcal), `"203"` Protein, `"204"` Total fat, `"205"` Carbs, `"291"` Fiber, `"269"` Sugars, `"539"` Added sugar, `"606"` Sat fat
  - Minerals: `"307"` Sodium (Na), `"306"` Potassium (K), `"303"` Iron (Fe), `"301"` Calcium (Ca), `"305"` Phosphorus
  - Vitamins: `"401"` Vitamin C, `"418"` Vitamin B-12, `"324"` Vitamin D, `"323"` Vitamin E
  - If a sodium/potassium total comes back as exactly 0 mg for a recipe that obviously contains salty or potassium-rich items, you used the wrong number — re-pull with `307`/`306`.

## Minimal Happy Path

```bash
# Resolve "spinach, raw" to fdcId
curl -s "https://api.nal.usda.gov/fdc/v1/foods/search?query=spinach+raw&dataType=SR+Legacy&pageSize=3&api_key=${USDA_FDC_API_KEY}"

# Batch-fetch full details for 3 ingredients (spinach, banana, whole milk)
curl -s -X POST "https://api.nal.usda.gov/fdc/v1/foods?api_key=${USDA_FDC_API_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"fdcIds":[168462,173944,171265],"format":"full"}' \
  | jq '.[0] | {fdcId, description, energy: (.foodNutrients[] | select(.nutrient.number=="208") | .amount)}'
```

## API Quirks

- **`POST /foods` returns a BARE ARRAY** `[FoodItem, ...]`, not a `{foods: [...]}` envelope. Do not destructure `.foods`.
- **Batch cap = 20 fdcIds.** If the recipe has more than 20 ingredients, chunk.
- **`foodNutrients` in full format is NESTED:** `{nutrient: {number: "208", name: "Energy"}, amount: 42.5}`. Search result nutrient shape is FLAT (`{nutrientNumber, value}`) — don't mix them.
- **Values are per 100 g.** To scale by the user's portion: `portion_value = amount_per_100g × user_grams / 100`. Write the division out per ingredient (grams, per-100g value, portion_value) before summing — skipping the /100 is the single most common scaling bug and produces totals ~100× too high on one ingredient, which the sanity-check band below will flag.
- **Dry vs cooked must match the fdcId.** If you fetched `Rice, white, long-grain, cooked` but the user gave dry-cup grams (158 g/cup), or fetched `Oats, raw` but the user ate cooked oatmeal, your grams and your per-100g values disagree by a 2-3× factor. Rule: match the fdcId's state to the user's stated state. Dry oats 1 cup = 80 g; cooked oatmeal 1 cup ≈ 234 g. Dry rice 1 cup = 158 g; cooked rice 1 cup ≈ 158 g (coincidentally close, but different per-100g values). For dry lentils 1 cup ≈ 192 g; cooked lentils 1 cup ≈ 198 g. Pick ONE side consistently.
- **Unit conversion table** (from common recipe units):
  - 1 cup raw spinach ≈ 30 g (loose-packed)
  - 1 medium banana ≈ 118 g
  - 1 cup whole milk ≈ 244 g
  - 1 tbsp olive oil ≈ 13.5 g
  - 1 large egg ≈ 50 g
  - 4 oz chicken breast = 113 g
  - 1 medium carrot ≈ 61 g; 1 medium bagel ≈ 85 g; 1 medium bell pepper ≈ 150 g (1/4 cup chopped ≈ 37 g)
  - 1 cup raspberries ≈ 123 g; 1 cup blueberries ≈ 148 g; 1 tbsp sugar ≈ 12.5 g; 1 tsp baking powder ≈ 5 g
  - 1/2 cup canned chickpeas ≈ 134.5 g; 1 tbsp tahini ≈ 15 g; 2 tbsp hummus ≈ 30 g; 1 tbsp almond/peanut butter ≈ 16 g
  - 1 cup all-purpose flour ≈ 120 g; 1 cup granulated sugar ≈ 200 g; 1 cup uncooked rice ≈ 158 g; 1 cup uncooked oats ≈ 80 g
  - 1 cup chicken broth ≈ 240 g; 1 cup cooked pasta ≈ 140 g; 2 oz dry pasta ≈ 57 g
  - 1 medium onion ≈ 110 g; 1 garlic clove ≈ 3 g; 1 tbsp olive/vegetable oil ≈ 13.5 g
  - 1 scoop whey protein ≈ 30 g; 1 tbsp cocoa powder ≈ 5 g (2 tbsp ≈ 10-12 g); 1 cup frozen strawberries ≈ 144 g; 1 cup sliced/diced zucchini ≈ 124 g; 1/4 cup crumbled goat cheese ≈ 30 g; 1 cup baby spinach ≈ 30 g (loose)
  - 1 tbsp active dry yeast ≈ 8.5 g; 1 tsp table salt ≈ 6 g; 1 tsp baking soda ≈ 4.6 g; ice cubes / plain water → 0 g contribution (note inline, don't fetch)
  - Canned chickpeas: `Chickpeas, canned, drained solids` scales as DRAINED weight only; 1/2 cup drained ≈ 82 g (NOT 134.5 g, which is drained+liquid). Use 82 g per 1/2 cup unless the user says "with liquid".
  - Disclose the conversion in the answer so the user can correct you.
  - If a unit is not in this table, state your assumed grams explicitly in the answer (e.g. "assuming 1 medium X ≈ Ng") so the user can correct it.
- `"SR Legacy"` spelling has a space — `"SRLegacy"` returns 0 results.
- Some ingredients (e.g. "garlic clove") have many FDC matches — pick the most-generic SR Legacy / Foundation entry. If unsure, ask the user whether they meant "raw" vs "cooked". Always echo the chosen `fdcId` + `description` per ingredient in the final answer so the user can spot a wrong pick.
- **Reject off-category matches before batch-fetching.** `foods/search` ranks by text relevance, not semantic fit — the top hit is often a processed/babyfood/blended/vegetarian-analog variant of the requested food. Read the `description` of each top hit and REJECT it when any of these apply:
  - User said plain X, hit says `Babyfood, ...` (e.g. orange juice → Babyfood, juice, orange). Re-search with `pageSize=10` and pick the non-babyfood entry.
  - User said X, hit says `Vegetarian ...` or `... substitute` when X is an animal product (salmon → Vegetarian fillets). Re-search; never ship a vegetarian analog as the animal food.
  - User said X oil, hit is a blended oil (olive oil → `Oil, corn, peanut, and olive`). Pick the pure single-source oil.
  - User said raw/fresh X, hit is `dehydrated`, `powder`, `dried`, `canned with ...`, `breaded`, `with vegetables`, or `lowfat/reduced-fat` when the user did not ask for that variant (banana → `Bananas, dehydrated, or banana powder`; chicken breast → `Chicken breast tenders, breaded, uncooked`; cottage cheese → `Cheese, cottage, with vegetables`; Greek yogurt plain → `Yogurt, Greek, plain, lowfat`). Scaling a dehydrated product's per-100g nutrients to fresh-weight grams inflates totals ~3-5×.
  - If no acceptable match appears in the top 10 SR Legacy / Foundation hits, say so in the answer rather than forcing a bad pick.
- Category-header entries in `foodNutrients` have no `amount` — filter them out before summing.
- Sum ACROSS ingredients: total_protein = Σ(ingredient_protein_per_100g × ingredient_grams / 100).
- **Sanity-check the total before returning.** Rough per-ingredient kcal/100g: veg 20-50, fruit 50-90, lean protein 120-200, cheese 250-400, oils 800-900, nuts/nut-butter 550-650, dry grains/flour 350-380, cooked grains 100-160, milk/plant-milk 40-70, coconut milk (canned) ~230, butter ~720, eggs ~145, sugar ~390. Compute rough_kcal = Σ(kcal/100g × grams/100) from this table BEFORE answering; if your computed recipe kcal is outside [0.6×, 1.5×] of rough_kcal, you have a scaling bug (forgot /100, used dry-weight per-100g on cooked grams or vice-versa, dropped an ingredient, or divided by servings twice). The same check applies to macro mass: total fat cannot exceed Σ(ingredient fat-mass upper bounds) — e.g. 0.7 g fat across a batch containing 1/2 cup butter (≈90 g fat) is physically impossible. Re-derive before returning.
- **Baking water-loss:** USDA values are for the raw ingredient as fetched. When computing per-slice/per-portion for baked goods, divide total by slice count — do NOT try to "subtract water"; instead disclose: "per-slice macros assume no water loss; actual baked weight ≈ 0.85× dough weight."

## Common Mistakes

- **Do not drop ingredients.** Before calling `POST /foods`, list every ingredient from the user's recipe and verify each appears in your fdcId set. If an ingredient (e.g. milk, oat milk, onion) cannot be resolved, name it explicitly in the answer instead of silently omitting — totals must reflect every line of the recipe.
- **Do not silently substitute.** If you searched for ingredient A but the resolved fdcId is for ingredient B (e.g. user said "onion", you fetched "potato"), this is a bug — re-search or ask the user. Never relabel a different food as the requested one. When a requested ingredient genuinely is not in FDC (black garlic, dashi, tahini as prepared, labneh), choosing a substitute is allowed BUT requires (a) naming the substitute fdcId+description in the answer body and (b) a matching entry in friction_notes — see substitute-disclosure rule below.
- **Skip nutritionally-inert ingredients.** Plain water (and similar zero-macro items) contributes 0 to every nutrient — do NOT spend a search/fetch slot on them; just note "water: 0 kcal" inline.
- **Substitute-disclosure is MANDATORY, not optional.** Any time an ingredient is not found as a direct FDC entry and you use a different fdcId (regular garlic for black garlic, sesame seeds or sesame paste for tahini, kombu+bonito or chicken broth for dashi, plain yogurt for labneh, etc.), you MUST (a) name both the requested ingredient and the fdcId/description you used, and (b) add a line to `friction_notes`. Empty `friction_notes` with a substitute in the ingredient list is a bug. This applies especially when the user explicitly asks "disclose if substituted" — honor that verbatim in the answer body, not just friction_notes. Spice blends / pastes (za'atar, garam masala, ras el hanout, harissa, gochujang, sambal, dashi, etc.) additionally require ASKING before substituting; if you proceed without confirmation, prefer a no-op (0 g, disclosed) over a wrong-flavor swap (harissa ≠ sweet red pepper; gochujang ≠ generic chili sauce — it is fermented, sweet, salty).
- **Honor user disambiguation requests.** If the user explicitly asks which FDC entry to use (e.g. "sesame seeds vs sesame butter for tahini"), name the chosen `fdcId` and `description` in the answer and justify the pick — don't bury it.
