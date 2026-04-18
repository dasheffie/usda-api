# usda-fdc-macro-alignment — 100-question corpus

## Splits
- train_ids (80): `[0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 19, 21, 23, 24, 25, 26, 27, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 70, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 86, 87, 89, 90, 91, 93, 95, 96, 97, 98, 99]`
- test_ids (20): `[5, 11, 13, 17, 20, 22, 28, 29, 52, 53, 62, 69, 71, 72, 73, 77, 85, 88, 92, 94]`
- seed: `970980990`  mode: `hackathon`  threshold: `1.0`

## Ability-tag coverage

| Tag | Count |
|---|---|
| `net_carb_computation` | 41 |
| `keto_verdict` | 38 |
| `macro_ratio_presentation` | 27 |
| `low_fat_or_low_carb_general` | 24 |
| `high_protein_verdict` | 22 |
| `paleo_verdict` | 22 |
| `per_serving_conversion` | 20 |

## EASY (40 questions, ids 0–39)

- ** 0.** Does a medium avocado fit the Keto diet?  
  _tags: `keto_verdict`, `net_carb_computation`_
- ** 1.** Is chicken breast a good food for a high-protein diet?  
  _tags: `high_protein_verdict`_
- ** 2.** Can I eat salmon on a Keto diet?  
  _tags: `keto_verdict`_
- ** 3.** Does white rice fit a low-carb diet?  
  _tags: `low_fat_or_low_carb_general`, `net_carb_computation`_
- ** 4.** Is olive oil allowed on a Paleo diet?  
  _tags: `paleo_verdict`_
- ** 5.** **[TEST]** Does spinach fit a Keto diet?  
  _tags: `keto_verdict`, `net_carb_computation`_
- ** 6.** Is beef allowed on a carnivore diet?  
  _tags: `keto_verdict`_
- ** 7.** Does broccoli fit a low-carb diet?  
  _tags: `low_fat_or_low_carb_general`, `net_carb_computation`_
- ** 8.** Can I eat almonds on a Keto diet?  
  _tags: `keto_verdict`, `net_carb_computation`_
- ** 9.** Is oatmeal allowed on a Paleo diet?  
  _tags: `paleo_verdict`_
- **10.** Does eggs fit a high-protein diet at one serving (2 large eggs)?  
  _tags: `high_protein_verdict`_
- **11.** **[TEST]** Is coconut oil suitable for a Keto diet based on its fat content?  
  _tags: `keto_verdict`, `macro_ratio_presentation`_
- **12.** Does kale fit a low-fat diet?  
  _tags: `low_fat_or_low_carb_general`, `macro_ratio_presentation`_
- **13.** **[TEST]** Is lentils allowed on a low-carb diet?  
  _tags: `low_fat_or_low_carb_general`, `net_carb_computation`_
- **14.** Can I eat quinoa on a high-protein diet?  
  _tags: `high_protein_verdict`_
- **15.** Does cheddar cheese fit the Keto diet?  
  _tags: `keto_verdict`, `macro_ratio_presentation`_
- **16.** Is turkey breast suitable for a high-protein diet?  
  _tags: `high_protein_verdict`_
- **17.** **[TEST]** Does peanut butter fit a Paleo diet?  
  _tags: `paleo_verdict`_
- **18.** Is brown rice allowed on a low-carb diet?  
  _tags: `low_fat_or_low_carb_general`, `net_carb_computation`_
- **19.** Can I eat whole eggs on a carnivore diet?  
  _tags: `keto_verdict`_
- **20.** **[TEST]** Does almond butter fit a Keto diet?  
  _tags: `keto_verdict`, `net_carb_computation`_
- **21.** Is tuna (canned in water) good for a high-protein diet?  
  _tags: `high_protein_verdict`_
- **22.** **[TEST]** Does sweet potato fit a Paleo diet?  
  _tags: `paleo_verdict`_
- **23.** Is cottage cheese suitable for a low-fat diet?  
  _tags: `low_fat_or_low_carb_general`, `macro_ratio_presentation`_
- **24.** Can I eat full-fat Greek yogurt on a Keto diet?  
  _tags: `keto_verdict`, `net_carb_computation`_
- **25.** Is pork rinds allowed on a carnivore diet?  
  _tags: `keto_verdict`_
- **26.** Does sunflower seeds fit a Paleo diet?  
  _tags: `paleo_verdict`_
- **27.** Is mozzarella cheese suitable for a low-fat diet?  
  _tags: `low_fat_or_low_carb_general`, `macro_ratio_presentation`_
- **28.** **[TEST]** Does bacon fit a carnivore diet?  
  _tags: `keto_verdict`_
- **29.** **[TEST]** Is edamame allowed on a Paleo diet?  
  _tags: `paleo_verdict`_
- **30.** Can I eat butter on a Keto diet based on its fat percentage?  
  _tags: `keto_verdict`, `macro_ratio_presentation`_
- **31.** Does whey protein powder fit a high-protein diet per serving?  
  _tags: `high_protein_verdict`_
- **32.** Is black beans allowed on a Paleo diet?  
  _tags: `paleo_verdict`_
- **33.** Does celery fit a low-carb diet?  
  _tags: `low_fat_or_low_carb_general`, `net_carb_computation`_
- **34.** Can I eat shrimp on a carnivore diet?  
  _tags: `keto_verdict`_
- **35.** Does whole milk fit a low-fat diet?  
  _tags: `low_fat_or_low_carb_general`, `macro_ratio_presentation`_
- **36.** Is walnuts suitable for a Keto diet?  
  _tags: `keto_verdict`, `net_carb_computation`_
- **37.** Does corn fit a Paleo diet?  
  _tags: `paleo_verdict`_
- **38.** Is skim milk suitable for a low-fat diet?  
  _tags: `low_fat_or_low_carb_general`, `macro_ratio_presentation`_
- **39.** Can I eat sardines on a high-protein diet?  
  _tags: `high_protein_verdict`_

## MODERATE (40 questions, ids 40–79)

- **40.** Can I eat quinoa on a Paleo diet, given it is a seed and not a true grain?  
  _tags: `paleo_verdict`, `net_carb_computation`_
- **41.** Are chickpeas high-protein enough for bodybuilder macros requiring at least 20g protein per serving?  
  _tags: `high_protein_verdict`, `per_serving_conversion`_
- **42.** What is the full macro breakdown (protein/fat/carb %) for a Quest Bar, and does it fit a Keto diet?  
  _tags: `keto_verdict`, `macro_ratio_presentation`, `per_serving_conversion`_
- **43.** Does an Atkins bar meet low-carb diet criteria when accounting for net carbs from fiber?  
  _tags: `low_fat_or_low_carb_general`, `net_carb_computation`, `per_serving_conversion`_
- **44.** Can I have both almonds and avocado in a Keto snack without exceeding 10g net carbs?  
  _tags: `keto_verdict`, `net_carb_computation`_
- **45.** Is a Halo Top ice cream pint (entire container) low enough in net carbs for a low-carb diet?  
  _tags: `low_fat_or_low_carb_general`, `net_carb_computation`, `per_serving_conversion`_
- **46.** What are the macro percentages for Oatly oat milk, and is it suitable for a low-fat diet?  
  _tags: `low_fat_or_low_carb_general`, `macro_ratio_presentation`, `per_serving_conversion`_
- **47.** Does a serving of lentils provide enough protein for a high-protein diet, and what are the net carbs?  
  _tags: `high_protein_verdict`, `net_carb_computation`_
- **48.** Can I eat peanuts on a Paleo diet, and are they low-carb enough for a low-carb constraint?  
  _tags: `paleo_verdict`, `low_fat_or_low_carb_general`_
- **49.** What is the macro breakdown of 100g of wild-caught Atlantic salmon, and does it fit high-protein criteria?  
  _tags: `high_protein_verdict`, `macro_ratio_presentation`_
- **50.** Does a typical serving of Oikos Triple Zero Greek yogurt fit Keto based on net carbs and fat ratio?  
  _tags: `keto_verdict`, `net_carb_computation`, `per_serving_conversion`_
- **51.** Can I include soybeans on a Paleo diet if they are fermented (like tempeh)?  
  _tags: `paleo_verdict`_
- **52.** **[TEST]** What percentage of calories in olive oil come from fat, and does olive oil fit a Keto macro ratio?  
  _tags: `keto_verdict`, `macro_ratio_presentation`_
- **53.** **[TEST]** Is a serving of kidney beans too carb-heavy for a low-carb diet after subtracting fiber?  
  _tags: `low_fat_or_low_carb_general`, `net_carb_computation`_
- **54.** Does 150g of boiled chicken breast meet the 25% protein energy threshold for a high-protein diet?  
  _tags: `high_protein_verdict`, `macro_ratio_presentation`, `per_serving_conversion`_
- **55.** Can hemp seeds satisfy both a Paleo and high-protein constraint simultaneously?  
  _tags: `paleo_verdict`, `high_protein_verdict`_
- **56.** What is the net carb count for a medium banana, and does it disqualify it from a Keto diet?  
  _tags: `keto_verdict`, `net_carb_computation`_
- **57.** Does a serving of Quest Protein Chips satisfy the high-protein criterion of 20g per serving?  
  _tags: `high_protein_verdict`, `per_serving_conversion`_
- **58.** Can I eat a moderate serving of dark chocolate (70% cacao) on a Keto diet?  
  _tags: `keto_verdict`, `net_carb_computation`_
- **59.** What macro breakdown does a serving of Fairlife whole milk have, and is it low-fat?  
  _tags: `low_fat_or_low_carb_general`, `macro_ratio_presentation`, `per_serving_conversion`_
- **60.** Does a 100g serving of tofu provide enough protein for high-protein bodybuilder needs, and does it fit Paleo?  
  _tags: `high_protein_verdict`, `paleo_verdict`_
- **61.** Can I eat pumpkin seeds on a Keto diet — what are the net carbs and fat ratio per serving?  
  _tags: `keto_verdict`, `net_carb_computation`, `macro_ratio_presentation`_
- **62.** **[TEST]** Is a large baked potato suitable for either a low-carb or a low-fat diet?  
  _tags: `low_fat_or_low_carb_general`, `net_carb_computation`, `macro_ratio_presentation`_
- **63.** Does a single serving of hummus (made from chickpeas) fit a Paleo diet?  
  _tags: `paleo_verdict`_
- **64.** What are the P/F/C percentages for full-fat ricotta cheese, and does it fit a Keto diet?  
  _tags: `keto_verdict`, `macro_ratio_presentation`_
- **65.** Can I include wild rice in a high-protein diet, and what is the net carb count per serving?  
  _tags: `high_protein_verdict`, `net_carb_computation`_
- **66.** Is a Clif Bar appropriate for a low-carb diet, and does it meet a high-protein threshold?  
  _tags: `low_fat_or_low_carb_general`, `high_protein_verdict`, `per_serving_conversion`_
- **67.** Does a serving of macadamia nuts fit Keto based on net carbs and fat-to-calorie ratio?  
  _tags: `keto_verdict`, `net_carb_computation`, `macro_ratio_presentation`_
- **68.** Can I use flaxseed meal on a Paleo diet, and how does its fiber affect net carbs on Keto?  
  _tags: `paleo_verdict`, `net_carb_computation`, `keto_verdict`_
- **69.** **[TEST]** Does a 30g serving of parmesan cheese fit high-protein criteria and a Keto fat ratio?  
  _tags: `high_protein_verdict`, `keto_verdict`, `macro_ratio_presentation`_
- **70.** Is a serving of soy milk suitable for a low-fat diet, and does its protein make it high-protein?  
  _tags: `low_fat_or_low_carb_general`, `high_protein_verdict`, `per_serving_conversion`_
- **71.** **[TEST]** Can chickpea pasta fit a Paleo diet, and what is its net carb count versus regular pasta?  
  _tags: `paleo_verdict`, `net_carb_computation`_
- **72.** **[TEST]** Does a serving of Siggi's Icelandic yogurt (0% fat) meet high-protein and low-fat simultaneously?  
  _tags: `high_protein_verdict`, `low_fat_or_low_carb_general`, `per_serving_conversion`_
- **73.** **[TEST]** What is the macro ratio for ground beef (80/20), and does it align with Keto's fat-energy threshold?  
  _tags: `keto_verdict`, `macro_ratio_presentation`_
- **74.** Is a serving of cashews too carb-heavy for Keto, and how does it compare to macadamia nuts?  
  _tags: `keto_verdict`, `net_carb_computation`_
- **75.** Can I have a low-fat diet and still eat a Lärabar (dates and nuts), given its macro composition?  
  _tags: `low_fat_or_low_carb_general`, `macro_ratio_presentation`, `per_serving_conversion`_
- **76.** Does a serving of edamame (shelled) provide enough protein for a high-protein diet, and does it fit Paleo?  
  _tags: `high_protein_verdict`, `paleo_verdict`_
- **77.** **[TEST]** What is the net carb count for cooked oats per 100g, and how does this scale to a 250g bowl?  
  _tags: `net_carb_computation`, `per_serving_conversion`_
- **78.** Can someone on a low-carb diet eat a medium apple, given the fiber content?  
  _tags: `low_fat_or_low_carb_general`, `net_carb_computation`_
- **79.** Does a 40g serving of natural almond butter from a branded 100g jar meet Keto fat and net-carb rules?  
  _tags: `keto_verdict`, `net_carb_computation`, `per_serving_conversion`_

## EDGE (20 questions, ids 80–99)

- **80.** Is honey Paleo-compliant? The Paleo community is split — the USDA data shows added sugars; does the skill flag it as non-Paleo?  
  _tags: `paleo_verdict`_
- **81.** Can full-fat Greek yogurt fit a carnivore diet if dairy is allowed, and does its lactose push it over Keto's net-carb limit?  
  _tags: `keto_verdict`, `net_carb_computation`_
- **82.** A Quest Bar lists chicory root fiber (inulin) separately. Can net carbs be computed accurately when some fiber may not be captured under nutrient 291?  
  _tags: `net_carb_computation`, `per_serving_conversion`_
- **83.** Erythritol has 0 kcal and is a sugar alcohol; does the USDA API return fiber or sugar data that allows an accurate Keto net-carb calculation for a product containing it?  
  _tags: `keto_verdict`, `net_carb_computation`_
- **84.** Does the Mediterranean diet rule flag extra-virgin olive oil positively, even though it is nearly 100% fat with no fiber?  
  _tags: `macro_ratio_presentation`_
- **85.** **[TEST]** Wild blueberries are high in antioxidants and fiber but also contain sugars. How does the DASH directional rule evaluate them, and can net carbs be reliably computed if fiber data is missing for a freeze-dried variant?  
  _tags: `net_carb_computation`_
- **86.** Beef liver is carnivore-compliant but contains glycogen (carbohydrate). Does it still fit Keto after subtracting its minimal fiber (nutrient 291 may be 0 or absent)?  
  _tags: `keto_verdict`, `net_carb_computation`_
- **87.** A branded 'keto-friendly' granola bar lists 2g net carbs on the label, but USDA data shows 18g total carbs and 8g fiber. What net carb value should the skill compute, and does it pass the Keto ≤10g threshold?  
  _tags: `keto_verdict`, `net_carb_computation`, `per_serving_conversion`_
- **88.** **[TEST]** Coconut aminos are used as a Paleo soy sauce substitute; but USDA data may list added sugars. Does the skill pass or fail it for Paleo based on the added-sugar nutrient (539)?  
  _tags: `paleo_verdict`_
- **89.** For an Atkins Endulge chocolate bar, the label uses 'net impact carbs' subtracting glycerin. USDA nutrient 291 only captures dietary fiber — what net carbs does the skill compute, and does it match the label claim?  
  _tags: `net_carb_computation`, `per_serving_conversion`, `keto_verdict`_
- **90.** Nutritional yeast has no USDA fiber entry (nutrient 291 absent). Can the skill still compute net carbs, or does it return an indeterminate result for a Keto check?  
  _tags: `net_carb_computation`, `keto_verdict`_
- **91.** Does the DASH diet directional rule give a positive verdict for canned low-sodium black beans, even though legumes are Paleo-banned?  
  _tags: `paleo_verdict`, `macro_ratio_presentation`_
- **92.** **[TEST]** Grass-fed butter is 80% fat; can it be used as a Mediterranean diet food given the diet favors unsaturated fats but the USDA API does not include saturated-fat breakdown in the requested nutrient set?  
  _tags: `macro_ratio_presentation`_
- **93.** A flavored whey protein powder has 25g protein but 12g added sugar per serving. Does it pass a high-protein check while failing Paleo due to added sugars?  
  _tags: `high_protein_verdict`, `paleo_verdict`_
- **94.** **[TEST]** Jackfruit (canned, in brine) is often used as a meat substitute. USDA data may list minimal protein (<2g/serving). Does it fail a high-protein check, and does its fiber allow a low-carb diet pass?  
  _tags: `high_protein_verdict`, `net_carb_computation`, `low_fat_or_low_carb_general`_
- **95.** MCT oil is 100% fat and 0g carbs; it trivially passes Keto by fat ratio and net carbs — but can the skill detect if the serving size in the USDA record is per 100g (requiring per_serving_conversion to the labeled 14g serving)?  
  _tags: `keto_verdict`, `per_serving_conversion`, `macro_ratio_presentation`_
- **96.** Date syrup is marketed as a 'natural' sweetener used in Paleo recipes. USDA data shows high added sugars (nutrient 539). Does the skill correctly flag it as non-Paleo?  
  _tags: `paleo_verdict`_
- **97.** A USDA entry for a breakfast cereal shows 0g fiber (nutrient 291 is present but zero). Net carbs = total carbs. Does a low-carb diet check produce a clear fail, and how does this compare to a missing-fiber scenario?  
  _tags: `net_carb_computation`, `low_fat_or_low_carb_general`_
- **98.** Sheep's milk cheese (like Manchego) has high fat and minimal carbs but also comes in a 100g USDA reference. If I eat a 28g serving, what are the scaled P/F/C values, and does it pass Keto?  
  _tags: `keto_verdict`, `per_serving_conversion`, `macro_ratio_presentation`_
- **99.** Monk fruit sweetener has no calories and no macros recorded in USDA. If the skill retrieves a food with 0 kcal and all nutrient values absent or zero, how should it handle a Keto macro-ratio check that would divide by zero?  
  _tags: `keto_verdict`, `net_carb_computation`, `macro_ratio_presentation`_
