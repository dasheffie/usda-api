---
name: usda-fdc-macro-alignment
description: Use when a user asks whether a specific food fits a macro-based diet (Keto, Paleo, high-protein, low-carb, low-fat) — fetches FDC detail, extracts protein/fat/total carbs/fiber/added-sugar and computes net carbs + macro ratio against the named diet's rule.
---

# USDA FDC — Macronutrient Profile Alignment

## When to Use

The user names a specific diet (Keto / Paleo / high-protein / low-fat / low-carb / DASH) and asks whether a specific food or meal item "fits" that diet's macro rules. Carnivore and Mediterranean are out of scope (no defined rule); decline and suggest the closest supported diet. Examples: "Does a medium Hass avocado fit my Keto macros?", "Is quinoa too carb-heavy for Paleo?", "Can I hit 40 g protein with this chicken breast?".

## API Surface

- **Endpoint:** `GET /food/{fdcId}?format=full` (or with `nutrients=203,204,205,208,269,291,539` to trim payload — include `269` total sugars as Paleo fallback when `539` is absent, and omit the filter entirely when retrying a response with missing nutrients)
- **Base URL:** `https://api.nal.usda.gov/fdc/v1`
- **Auth:** `?api_key=${USDA_FDC_API_KEY}`
- **Key fields read:** `foodNutrients` entries for nutrient numbers `"203"` (protein), `"204"` (total fat), `"205"` (total carbohydrate), `"269"` (total sugars, Paleo fallback), `"291"` (dietary fiber), `"539"` (added sugars), `"208"` (energy kcal), `servingSize`, `servingSizeUnit`, `foodPortions[].gramWeight` (for natural-language portions like "medium apple", "1 cup"), `labelNutrients` (Branded per-serving), `dataType`, `foodCategory`, `description`, `ingredients`

## Macro math

| Metric | Formula |
|---|---|
| Net carbs (g) | `total_carbs (205) − fiber (291)` |
| Energy from protein | `4 × protein_g` |
| Energy from carbs (net) | `4 × net_carbs_g` |
| Energy from fat | `9 × fat_g` |
| Keto rule | `net_carbs_g ≤ 10 per serving` AND `fat_energy % ≥ 70 %` (if total macro energy = 0, e.g. monk fruit / erythritol / plain water, skip the fat % test and answer "Keto-neutral: zero-calorie, no macros to evaluate") |
| Paleo rule (heuristic) | no added sugars (539 == 0), no grains, no legumes. Match against `description` AND `foodCategory` AND a hardcoded grain/legume name list (oat/oats/oatmeal, wheat, rice (including wild rice), corn, barley, rye, quinoa, bean/beans, lentil, pea, peanut, soy/soybean/soya/edamame/tofu/tempeh, chickpea, amaranth, millet, sorghum, spelt, farro, teff, buckwheat. Hardcoded added-sugar fails list (Paleo decidable-by-name when 539 unavailable): honey, maple syrup, agave, cane sugar, brown sugar, molasses, corn syrup, high-fructose corn syrup, dextrose, sucrose, date syrup, coconut sugar). Do NOT rely on the API response containing the word "grain" — it usually won't. |
| High-protein rule | `protein_g ≥ 20 per serving` OR `protein_energy % ≥ 25 %` |
| Low-fat rule | `fat_energy % ≤ 30 %` per serving (USDA/AHA convention) OR `fat_g ≤ 3 per 100 g` for solid foods |
| Low-carb rule | `net_carbs_g ≤ 20 per serving` (strict) OR `≤ 50 per serving` (moderate); state which threshold you applied |
| DASH rule (heuristic) | `sodium_mg ≤ 480 per serving` AND `saturated_fat_g ≤ 2 per serving` AND `added_sugar_g ≤ 5 per serving`; fetch nutrients `307` (sodium) and `606` (saturated fat) in addition to the standard set. Disclose that DASH is sodium-driven, not macro-driven. |

## Minimal Happy Path

```bash
# All macros for Hass avocado (SR Legacy fdcId 171706)
curl -s "https://api.nal.usda.gov/fdc/v1/food/171706?format=full&nutrients=203,204,205,291,539,208&api_key=${USDA_FDC_API_KEY}" \
  | jq '.foodNutrients[] | {num: .nutrient.number, amount: .amount, unit: .nutrient.unitName}'
```

## Search & Resolution

- **Search-then-detail can 404.** Some `fdcId`s returned by `/foods/search` (often older Survey/FNDDS or relinked entries) return 404 on `GET /food/{fdcId}`. On 404, fall back to the next search hit; don't stop. Prefer `dataType=Foundation,SR Legacy,Branded` in the search query to reduce 404s.
- **Query relaxation.** If exact phrase returns no usable hit, drop modifiers in this order: brand → preparation (canned/raw/cooked) → packing medium (in water / in oil) → keep only the head noun. Example: `tuna canned water` → `tuna canned` → `tuna`.
- **Unicode / diacritics.** Strip diacritics before searching (`Lärabar` → `Larabar`); FDC search is ASCII-tolerant but not always Unicode-tolerant. If still empty, try the parent category (e.g. `fruit nut bar`).

## Rate Limits & Offline Fallback

- **429 OVER_RATE_LIMIT:** FDC returns 429 when the hourly/daily key quota is exhausted. Do NOT loop exponential-backoff past ~60s — account-level quotas don't clear within a run. **Detect 429 on the FIRST search call and switch to offline mode for the entire run** — do not repeat searches for subsequent foods; each failed call wastes latency and confirms nothing. On sustained 429, switch to offline reasoning: (a) if the food is on the hardcoded grain/legume/soy OR added-sugar list, Paleo answer is decidable by name alone — return it with "flagged by name; API unreachable (429)"; (b) for Keto/low-carb/low-fat/high-protein on commodity whole foods (butter, egg, celery, walnuts, apple, salmon, brown rice, quinoa, black beans, edamame, wild rice, ricotta, hemp seeds, almonds, avocado, olive oil, kale, skim milk, mozzarella, Greek yogurt plain, macadamia nuts, cashews, flaxseed, honey, whey protein unflavored), cite typical USDA per-100g / per-serving values from training knowledge and disclose "API rate-limited; values from cached reference"; (c) for Branded items (Oikos, Quest, Atkins, Larabar, Halo Top, Oatly), decline the numeric verdict but still apply decidable-by-name rules (e.g., Oatly contains oats → fails Paleo even without label) and disclose "Branded label data requires live API; rate-limited — retry later."
- **Request budget:** 1 search + 1 detail per food. For multi-food questions, run all searches first, then only fetch detail for confirmed fdcIds to stay under quota.

## API Quirks

- **Nutrient numbers are STRINGS.** Match `.nutrient.number === "205"`, not `=== 205`.
- **Basis differs by dataType.** Foundation / SR Legacy foodNutrients are per 100 g. Branded stores foodNutrients per 100 g AND `labelNutrients` per serving. Mixing the two silently produces wrong ratios. **For Branded items, prefer `labelNutrients` (already per-serving and matches the on-pack panel) over computing from foodNutrients** — especially when the user asks about a low-fat / low-sugar variant or a specific brand. To scale to a whole container, multiply per-serving by `servingsPerContainer` (or by `packageWeight / servingSize`).
- **Convert to per-serving** before evaluating diet rules: `per_serving = per_100g × servingSize / 100` (only when `servingSizeUnit == "g"` or `"ml"`). For natural-language portions like "a medium apple" or "1 cup", look up the gram weight in `foodPortions[]` (`gramWeight` field) and scale `per_100g × gramWeight / 100`. Never report per-100g numbers as a serving — a "medium apple" is ~182 g, not 100 g, so 75 g carbs/100g becomes ~14 g per apple, not 75.
- **Branded low-carb bar caveat (Quest, Atkins, etc.):** USDA nutrient 291 does not include isolated fibers (inulin, chicory root) or sugar alcohols/glycerin. The label-claimed "net carbs" subtracts those; the API-derived net carb will therefore exceed the label claim by 5–15 g typically. Always report BOTH: `API net carbs = 205 − 291 = X g` AND `label claim = Y g` (read from `labelNutrients` if present, or scan `ingredients` for inulin/chicory/glycerin/erythritol/maltitol and note the gap). Do NOT silently use either number.
- **Net carbs = max(0, 205 − 291).** Clamp at zero — high-fiber foods like flaxseed can produce a negative result that is meaningless. USDA does not publish "net carbs"; compute from 205 − 291. Low-carb bars (Quest, Atkins) DO print label "net carbs" or "net impact carbs" that additionally subtract sugar alcohols / glycerin / specialty fibers (inulin, chicory root). USDA nutrient 291 may not include these isolated fibers, so the API-derived net carb can exceed the label claim — report both: "API net carbs = X g; label claim = Y g (subtracts glycerin/inulin not in nutrient 291)". If 291 is missing, first re-fetch with `format=full` (no nutrient filter) since the trimmed response can omit zero/null nutrients; only then assume fiber=0 and disclose. A present-but-low fiber value (e.g. 2.1 g) is NOT zero — report the actual number.
- **Added sugar (539):** a present non-zero 539 (e.g. 12 g) IMMEDIATELY fails Paleo — no further checks needed. Absence ≠ zero; 539 is a newer FDA field and may be missing even on Branded foods. If 539 is missing, disclose "added sugar data not available" and fall back to (a) `ingredients` string scan for sugar/syrup/honey/dextrose/maltodextrose/cane/agave/glycerin, and (b) total sugars (nutrient `269`) as an upper bound — state which fallback you used.
- Paleo rules are heuristic and contested. The skill should disclose the rule set it applied (e.g. "Paleo excludes grains and legumes; I used that rule").

## Common Mistakes

- Reporting per-100g numbers as a serving for whole-food portions (apple, banana, egg) — always resolve `foodPortions[].gramWeight` first.
- Trusting the search's first hit and giving up on 404 — retry with the next hit or relax the query.
- Treating absent fiber (291) or added sugar (539) as zero without disclosing — and never call a present-but-low fiber value (e.g. 2.1 g) "zero".
- Using foodNutrients (per 100 g) for a Branded item when `labelNutrients` (per serving) is present.
- Searching with diacritics (Lärabar) — strip to ASCII first.
- Flagging Paleo grain/legume status by hoping the API response says "grain" — use the hardcoded name list in the Macro-math table.
