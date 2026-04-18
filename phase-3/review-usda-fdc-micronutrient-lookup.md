# usda-fdc-micronutrient-lookup — 100-question corpus

## Splits
- train_ids (80): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 20, 21, 22, 23, 24, 25, 26, 29, 31, 33, 34, 35, 36, 37, 38, 39, 41, 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 67, 69, 70, 72, 73, 74, 76, 77, 78, 79, 80, 81, 83, 84, 85, 87, 88, 90, 91, 92, 93, 94, 96, 97, 98, 99]`
- test_ids (20): `[13, 14, 18, 19, 27, 28, 30, 32, 40, 42, 51, 60, 66, 68, 71, 75, 82, 86, 89, 95]`
- seed: `1759494165`  mode: `hackathon`  threshold: `1.0`

## Ability-tag coverage

| Tag | Count |
|---|---|
| `specific_micronutrient_extraction` | 48 |
| `labelnutrients_vs_foodnutrients` | 40 |
| `rda_comparison` | 37 |
| `unit_disclosure` | 31 |
| `product_not_in_fdc_or_missing_nutrient` | 14 |
| `doctor_deficiency_context` | 13 |
| `serving_size_conversion` | 10 |

## EASY (40 questions, ids 0–39)

- ** 0.** How much iron is in 1 cup of cooked lentils?  
  _tags: `specific_micronutrient_extraction`_
- ** 1.** What is the calcium content of plain whole-milk yogurt?  
  _tags: `specific_micronutrient_extraction`_
- ** 2.** How much vitamin B-12 is in 3 oz of beef liver?  
  _tags: `specific_micronutrient_extraction`, `unit_disclosure`, `serving_size_conversion`_
- ** 3.** How many milligrams of magnesium are in a 1 oz serving of almonds?  
  _tags: `specific_micronutrient_extraction`, `serving_size_conversion`_
- ** 4.** What is the zinc content of 3 oz of cooked oysters?  
  _tags: `specific_micronutrient_extraction`, `serving_size_conversion`_
- ** 5.** How much vitamin D is in one large egg?  
  _tags: `specific_micronutrient_extraction`, `unit_disclosure`_
- ** 6.** How many micrograms of folate are in 1 cup of raw spinach?  
  _tags: `specific_micronutrient_extraction`, `unit_disclosure`_
- ** 7.** What is the potassium content of one medium banana?  
  _tags: `specific_micronutrient_extraction`_
- ** 8.** How much vitamin C is in one medium orange?  
  _tags: `specific_micronutrient_extraction`_
- ** 9.** How many micrograms of vitamin A (RAE) are in 1 cup of cooked kale?  
  _tags: `specific_micronutrient_extraction`, `serving_size_conversion`_
- **10.** Does a 3 oz serving of canned sardines provide a significant amount of calcium?  
  _tags: `specific_micronutrient_extraction`, `rda_comparison`_
- **11.** How much iron is in a 3 oz serving of cooked beef liver?  
  _tags: `specific_micronutrient_extraction`_
- **12.** What is the magnesium content in 1 oz of cashews?  
  _tags: `specific_micronutrient_extraction`_
- **13.** **[TEST]** How much zinc does a 3 oz serving of cooked ground beef contain?  
  _tags: `specific_micronutrient_extraction`_
- **14.** **[TEST]** What is the potassium content of 1 cup of cooked black beans?  
  _tags: `specific_micronutrient_extraction`_
- **15.** How much vitamin C is in 1 cup of raw broccoli?  
  _tags: `specific_micronutrient_extraction`_
- **16.** How many micrograms of vitamin B-12 does 1 cup of whole milk contain?  
  _tags: `specific_micronutrient_extraction`, `unit_disclosure`_
- **17.** What is the folate content in 1 cup of cooked chickpeas?  
  _tags: `specific_micronutrient_extraction`_
- **18.** **[TEST]** How much vitamin A (RAE) is in 1 medium raw carrot?  
  _tags: `specific_micronutrient_extraction`_
- **19.** **[TEST]** How much calcium is in 1 cup of skim milk?  
  _tags: `specific_micronutrient_extraction`_
- **20.** What is the iron content in 1 oz of pumpkin seeds?  
  _tags: `specific_micronutrient_extraction`_
- **21.** How much potassium is in 1 medium baked potato with skin?  
  _tags: `specific_micronutrient_extraction`_
- **22.** How much vitamin D is in 3 oz of canned salmon?  
  _tags: `specific_micronutrient_extraction`, `unit_disclosure`_
- **23.** How many milligrams of magnesium are in 1 cup of cooked quinoa?  
  _tags: `specific_micronutrient_extraction`, `serving_size_conversion`_
- **24.** How much vitamin C does one medium kiwifruit provide?  
  _tags: `specific_micronutrient_extraction`_
- **25.** How much zinc is in a 3 oz serving of cooked shrimp?  
  _tags: `specific_micronutrient_extraction`_
- **26.** What is the folate content of 1 cup of raw romaine lettuce?  
  _tags: `specific_micronutrient_extraction`_
- **27.** **[TEST]** How much vitamin A (RAE) is in 1 cup of cooked sweet potato?  
  _tags: `specific_micronutrient_extraction`_
- **28.** **[TEST]** How much calcium is in 1 cup of cooked bok choy?  
  _tags: `specific_micronutrient_extraction`_
- **29.** What is the iron content of half a cup of firm tofu?  
  _tags: `specific_micronutrient_extraction`_
- **30.** **[TEST]** How many milligrams of magnesium does 2 tablespoons of chia seeds provide?  
  _tags: `specific_micronutrient_extraction`_
- **31.** How much vitamin D is in 3 oz of cooked rainbow trout?  
  _tags: `specific_micronutrient_extraction`, `unit_disclosure`_
- **32.** **[TEST]** How much potassium is in one cup of plain low-fat yogurt?  
  _tags: `specific_micronutrient_extraction`_
- **33.** What is the vitamin C content in half a cup of red bell pepper, raw?  
  _tags: `specific_micronutrient_extraction`_
- **34.** How many micrograms of vitamin B-12 does a 3 oz serving of cooked clams contain?  
  _tags: `specific_micronutrient_extraction`, `unit_disclosure`_
- **35.** How much folate is in 1 cup of cooked edamame?  
  _tags: `specific_micronutrient_extraction`_
- **36.** What is the zinc content of 1 oz of hemp seeds?  
  _tags: `specific_micronutrient_extraction`_
- **37.** How much calcium is in 1 oz of parmesan cheese?  
  _tags: `specific_micronutrient_extraction`_
- **38.** How many milligrams of potassium are in 1 cup of cooked lentils?  
  _tags: `specific_micronutrient_extraction`_
- **39.** What is the vitamin A (RAE) content in 1 tablespoon of beef liver pâté?  
  _tags: `specific_micronutrient_extraction`_

## MODERATE (40 questions, ids 40–79)

- **40.** **[TEST]** Is a 1-cup serving of cooked spinach a good source of iron relative to the adult RDA?  
  _tags: `rda_comparison`, `serving_size_conversion`_
- **41.** Does a single serving of Kellogg's Special K Original cereal cover a meaningful portion of my daily folate RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **42.** **[TEST]** My doctor told me I have low vitamin D. How much vitamin D does a single serving of Dannon plain Greek yogurt provide, and does it help?  
  _tags: `doctor_deficiency_context`, `rda_comparison`, `unit_disclosure`_
- **43.** I was recently diagnosed with iron-deficiency anemia. Does a per-serving amount of Cream of Wheat original hot cereal meaningfully contribute to my daily iron needs?  
  _tags: `doctor_deficiency_context`, `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **44.** How much calcium does one serving of Chobani plain nonfat Greek yogurt provide compared to the adult RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **45.** How much magnesium is in a 1 oz serving of dry-roasted peanuts, given that FDC stores the value per 100g?  
  _tags: `specific_micronutrient_extraction`, `serving_size_conversion`_
- **46.** Does a per-serving of General Mills Cheerios (Original) cereal cover my daily folate requirement?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **47.** How much vitamin B-12 is in one serving of Ensure Original Nutrition Shake, in micrograms, and how does that compare to the adult RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`, `unit_disclosure`_
- **48.** Is a single serving of Post Grape-Nuts cereal a good source of iron for adult women?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **49.** How much zinc does a per-serving of Nature Valley Protein Crunchy Bar provide relative to the adult RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **50.** My doctor found I have low vitamin D levels. How much does a per-serving of Silk Unsweetened Almond Milk provide, in IU and micrograms?  
  _tags: `doctor_deficiency_context`, `unit_disclosure`, `labelnutrients_vs_foodnutrients`_
- **51.** **[TEST]** Does a standard 3 oz serving of canned tuna in water cover a significant portion of the adult potassium RDA?  
  _tags: `rda_comparison`, `serving_size_conversion`_
- **52.** How much folate does a serving of Tropicana Pure Premium Orange Juice with DHA provide, and does it meet the adult RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **53.** I am at risk for osteoporosis. Does one serving of Kraft Singles American cheese slices meet a significant fraction of my daily calcium needs?  
  _tags: `doctor_deficiency_context`, `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **54.** How much iron is in a per-serving of Amy's Organic Lentil Vegetable Soup?  
  _tags: `specific_micronutrient_extraction`, `labelnutrients_vs_foodnutrients`_
- **55.** How much vitamin C does a 100g vs a standard per-serving portion of raw strawberries provide?  
  _tags: `specific_micronutrient_extraction`, `serving_size_conversion`_
- **56.** My doctor said I have a B12 deficiency. How much B-12 is in one serving of Activia probiotic yogurt, in micrograms?  
  _tags: `doctor_deficiency_context`, `unit_disclosure`, `labelnutrients_vs_foodnutrients`_
- **57.** How much magnesium is in a per-serving of Quaker Old Fashioned Oats, and what percentage of the adult RDA does that represent?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **58.** Does a single serving of Kashi GOLEAN Crunch cereal provide a meaningful contribution to the daily zinc RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **59.** How does the per-serving potassium in Bolthouse Farms carrot juice compare to the adult adequate intake?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **60.** **[TEST]** I'm worried about iron-deficiency anemia. Does a serving of Kind Dark Chocolate Nuts & Sea Salt bar meaningfully contribute to my daily iron needs?  
  _tags: `doctor_deficiency_context`, `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **61.** What is the per-serving vitamin A (RAE) content in Libby's 100% Pure Pumpkin canned, and does it meet the adult RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **62.** How much calcium is in a per-serving of Oikos Triple Zero Greek Nonfat Yogurt, and what fraction of the adult RDA is that?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **63.** How much vitamin D is in one serving of Stonyfield Organic Whole Milk yogurt, and does it meet the adult RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`, `unit_disclosure`_
- **64.** How much folate does a per-serving of Pepperidge Farm Whole Grain 15 Grain Bread provide against the adult RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **65.** My doctor diagnosed me with low vitamin D. Does a serving of Horizon Organic Whole Milk provide enough vitamin D to matter?  
  _tags: `doctor_deficiency_context`, `rda_comparison`, `unit_disclosure`_
- **66.** **[TEST]** How much potassium per serving does Campbell's Tomato Soup provide, and how does that compare to the daily adequate intake?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **67.** I have been told I am B12 deficient. How much vitamin B-12 does a serving of Clif Bar provide, and is the unit micrograms?  
  _tags: `doctor_deficiency_context`, `unit_disclosure`, `labelnutrients_vs_foodnutrients`_
- **68.** **[TEST]** Does a per-serving of Silk Soy Milk Original count toward my daily calcium RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **69.** How much vitamin C is in a per-serving of Tropicana Pure Premium Original Orange Juice, and does it meet the adult RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **70.** How much iron does a serving of Kellogg's Raisin Bran provide, and does it cover the adult RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **71.** **[TEST]** I am at risk for osteoporosis. Does one serving of Kirkland Signature (Costco) Almond Milk fortified provide a meaningful fraction of my daily calcium needs?  
  _tags: `doctor_deficiency_context`, `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **72.** How much magnesium is in a per-serving of Bob's Red Mill Organic Rolled Oats?  
  _tags: `specific_micronutrient_extraction`, `labelnutrients_vs_foodnutrients`_
- **73.** What percentage of the adult potassium AI does a serving of V8 Original Vegetable Juice cover?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **74.** How much zinc is in a per-serving of Optimum Nutrition Gold Standard 100% Whey Protein powder?  
  _tags: `specific_micronutrient_extraction`, `labelnutrients_vs_foodnutrients`_
- **75.** **[TEST]** Does a serving of Quaker Instant Oatmeal (original flavor) meet the adult folate RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **76.** How much vitamin A (RAE) does a per-serving of Bolthouse Farms 100% Carrot Juice provide, and does it exceed the adult RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`_
- **77.** I was recently told I have low vitamin D. Does a per-serving of Nature Made Vitamin D3 Gummy supplement meet the adult RDA, and what is the unit (IU or mcg)?  
  _tags: `doctor_deficiency_context`, `rda_comparison`, `unit_disclosure`_
- **78.** How much vitamin B-12 per serving does Abbott Pediasure Grow & Gain provide, and what is the unit?  
  _tags: `specific_micronutrient_extraction`, `unit_disclosure`, `labelnutrients_vs_foodnutrients`_
- **79.** Does a serving of Kirkland Signature (Costco) Salmon (canned) contribute meaningfully to the adult vitamin D RDA?  
  _tags: `rda_comparison`, `labelnutrients_vs_foodnutrients`, `unit_disclosure`_

## EDGE (20 questions, ids 80–99)

- **80.** How much vitamin B-12 is in 1 cup of raw tempeh? Note that tempeh is an unfortified fermented soy product.  
  _tags: `specific_micronutrient_extraction`, `unit_disclosure`, `product_not_in_fdc_or_missing_nutrient`_
- **81.** How much vitamin B-12 is in 1 cup of cooked white rice? Rice is an unfortified plant food — what should the skill report?  
  _tags: `unit_disclosure`, `product_not_in_fdc_or_missing_nutrient`_
- **82.** **[TEST]** What is the iron content of 'Ancient Grain Power Bowl' sold at a local food truck — this product is not in any national database.  
  _tags: `product_not_in_fdc_or_missing_nutrient`_
- **83.** A package of 'NutriBlend Superfood Bars' claims '100% of your daily iron in every bar' — can you verify this using FDC?  
  _tags: `product_not_in_fdc_or_missing_nutrient`, `rda_comparison`_
- **84.** How much vitamin B-12 is in 1 cup of cooked lentils, an unfortified plant food? Disclose the unit and explain expected near-zero value.  
  _tags: `unit_disclosure`, `product_not_in_fdc_or_missing_nutrient`_
- **85.** Centrum Silver Adults 50+ claims to provide both iron and vitamin B-12. The label lists both nutrients — does the FDC record reflect actual label values for both, and are the units disclosed correctly?  
  _tags: `labelnutrients_vs_foodnutrients`, `unit_disclosure`, `rda_comparison`_
- **86.** **[TEST]** How much vitamin D is stored in the FDC record for a brand of UV-treated portobello mushrooms that claims 'fortified with vitamin D by UV light'? Does FDC capture this, and what unit is used?  
  _tags: `product_not_in_fdc_or_missing_nutrient`, `unit_disclosure`_
- **87.** A new private-label grocery store brand 'Fresh Market Omega Blend' granola bar claims high folate. Can the skill verify this via FDC, or is the product missing from the database?  
  _tags: `product_not_in_fdc_or_missing_nutrient`, `rda_comparison`_
- **88.** How much vitamin B-12 is in 1 tablespoon of nutritional yeast that is NOT fortified? Disclose unit and explain why the value may be zero or missing.  
  _tags: `unit_disclosure`, `product_not_in_fdc_or_missing_nutrient`_
- **89.** **[TEST]** A FDC entry for a generic 'Green Powder Supplement' lists vitamin D as '0 IU' but the label claims 400 IU. Which value should the skill use, and how should the discrepancy be reported?  
  _tags: `labelnutrients_vs_foodnutrients`, `unit_disclosure`, `product_not_in_fdc_or_missing_nutrient`_
- **90.** My doctor says I have B12 deficiency. I eat only raw vegetables. How much B-12 is in 1 cup of raw kale, and what should I understand about plant foods and B-12?  
  _tags: `doctor_deficiency_context`, `unit_disclosure`, `product_not_in_fdc_or_missing_nutrient`_
- **91.** How much iron is in a 2 oz serving of a 'house-made vegan chorizo' product from a local restaurant, not available in FDC?  
  _tags: `product_not_in_fdc_or_missing_nutrient`_
- **92.** How much vitamin D is listed in the FDC record for raw shiitake mushrooms (not UV-treated)? Is the nutrient populated, and what is the unit?  
  _tags: `specific_micronutrient_extraction`, `unit_disclosure`, `product_not_in_fdc_or_missing_nutrient`_
- **93.** A box of Kellogg's Special K Red Berries lists both folate (DFE) and folic acid on the label. Which nutrient number does the skill use, and what unit should be reported?  
  _tags: `labelnutrients_vs_foodnutrients`, `unit_disclosure`_
- **94.** My doctor found I have iron-deficiency anemia. I want to check the iron in 'TrailMix Supreme' from a small regional brand — the product appears in FDC but the iron nutrient field is blank. How should the skill handle this?  
  _tags: `doctor_deficiency_context`, `product_not_in_fdc_or_missing_nutrient`_
- **95.** **[TEST]** How much calcium is in 1 cup of fortified oat milk versus what FDC stores (per 100g)? Show the conversion and disclose whether a labelNutrients field is present.  
  _tags: `serving_size_conversion`, `labelnutrients_vs_foodnutrients`, `unit_disclosure`_
- **96.** Vitamin D in FDC can be expressed as nutrient 324 (IU) or nutrient 1110 (mcg). If a branded food only has nutrient 1110, how should the skill report the value, and what conversion to IU should be shown?  
  _tags: `unit_disclosure`, `labelnutrients_vs_foodnutrients`_
- **97.** A nutrition blogger claims their homemade spirulina smoothie provides over 500% of the daily B-12 RDA. How much B-12 is actually in 1 tablespoon of dried spirulina according to FDC, and is the claim plausible?  
  _tags: `rda_comparison`, `unit_disclosure`, `product_not_in_fdc_or_missing_nutrient`_
- **98.** A store-brand 'Multivitamin Complete' supplement in FDC has both foodNutrients and labelNutrients populated for calcium, but with different values. Which should the skill prefer, and why?  
  _tags: `labelnutrients_vs_foodnutrients`, `rda_comparison`_
- **99.** My doctor diagnosed me with both iron-deficiency anemia and vitamin D insufficiency. I want to evaluate two nutrients at once for a serving of Kellogg's All-Bran Original cereal. How should the skill handle a dual-nutrient query, and what units should be reported for each?  
  _tags: `doctor_deficiency_context`, `unit_disclosure`, `labelnutrients_vs_foodnutrients`_
