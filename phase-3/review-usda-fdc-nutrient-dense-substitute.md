# usda-fdc-nutrient-dense-substitute — 100-question corpus

## Splits
- train_ids (80): `[0, 1, 2, 4, 5, 6, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 46, 47, 49, 50, 51, 52, 54, 56, 57, 58, 59, 60, 62, 63, 64, 65, 67, 68, 69, 70, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 94, 96, 97, 99]`
- test_ids (20): `[3, 7, 10, 11, 21, 28, 30, 39, 44, 45, 48, 53, 55, 61, 66, 72, 84, 93, 95, 98]`
- seed: `1363885055`  mode: `hackathon`  threshold: `1.0`

## Ability-tag coverage

| Tag | Count |
|---|---|
| `foundation_whole_food_rank` | 66 |
| `allergy_driven_exclusion` | 41 |
| `iron_vegan_source` | 32 |
| `calcium_nondairy_source` | 25 |
| `fiber_gluten_free` | 20 |
| `potassium_or_low_potassium_ckd` | 11 |
| `b12_vegan_disclosure` | 10 |

## EASY (40 questions, ids 0–39)

- ** 0.** I'm dairy-free. Which plant foods have the most calcium per 100 g?  
  _tags: `calcium_nondairy_source`, `allergy_driven_exclusion`_
- ** 1.** I have a dairy allergy. What are the top whole-food sources of calcium I can eat?  
  _tags: `calcium_nondairy_source`, `allergy_driven_exclusion`_
- ** 2.** I'm vegan. What whole foods are highest in iron per 100 g?  
  _tags: `iron_vegan_source`_
- ** 3.** **[TEST]** I avoid all animal products. Which plant-based foods provide the most iron?  
  _tags: `iron_vegan_source`_
- ** 4.** I'm gluten-free and need more fiber. Which whole foods are high in fiber without gluten?  
  _tags: `fiber_gluten_free`_
- ** 5.** I can't eat wheat, rye, or barley. What gluten-free whole foods give me the most fiber?  
  _tags: `fiber_gluten_free`_
- ** 6.** I have a peanut allergy. What other whole foods are highest in protein per 100 g?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- ** 7.** **[TEST]** I'm allergic to peanuts. Which seeds or legumes give the most protein as a replacement?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- ** 8.** I'm vegetarian and want more magnesium. Which plant foods rank highest in magnesium?  
  _tags: `foundation_whole_food_rank`_
- ** 9.** I eat no meat or fish. What whole foods have the most magnesium per 100 g?  
  _tags: `foundation_whole_food_rank`_
- **10.** **[TEST]** I have a tree-nut allergy. What whole foods are highest in zinc?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **11.** **[TEST]** I'm allergic to tree nuts like almonds and cashews. Which other foods can I eat for zinc?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **12.** I'm dairy-free. Which non-dairy whole foods give me the most potassium?  
  _tags: `calcium_nondairy_source`, `allergy_driven_exclusion`_
- **13.** I have a shellfish allergy. Which whole foods are richest in omega-3 fatty acids?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **14.** I'm allergic to shrimp and crab. Which non-shellfish foods have the most omega-3s?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **15.** I'm vegan. What whole foods provide the most protein per 100 g, and should I be worried about B-12 if I'm only eating whole plant foods?  
  _tags: `iron_vegan_source`, `foundation_whole_food_rank`, `b12_vegan_disclosure`_
- **16.** I don't eat eggs or dairy. Which plant foods have the most folate?  
  _tags: `foundation_whole_food_rank`_
- **17.** I'm soy-allergic. Which whole foods are highest in protein besides soy products?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **18.** I avoid soy. What are the top non-soy plant protein sources per 100 g?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **19.** I have an egg allergy. Which whole foods are high in choline as a substitute?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **20.** I'm nightshade-free. Which vegetables outside the nightshade family are richest in potassium?  
  _tags: `foundation_whole_food_rank`_
- **21.** **[TEST]** I avoid nightshades like tomatoes and peppers. What whole foods can replace them for vitamin C?  
  _tags: `foundation_whole_food_rank`_
- **22.** I'm on a low-FODMAP diet. Which whole foods are high in fiber without triggering symptoms?  
  _tags: `fiber_gluten_free`, `foundation_whole_food_rank`_
- **23.** I'm dairy-free and want more vitamin D. Which non-dairy whole foods are highest in vitamin D?  
  _tags: `calcium_nondairy_source`, `allergy_driven_exclusion`_
- **24.** I'm gluten-free. What whole-grain alternatives provide the most iron per 100 g?  
  _tags: `fiber_gluten_free`, `iron_vegan_source`_
- **25.** I have a wheat allergy. Which gluten-free grains have the highest iron content?  
  _tags: `allergy_driven_exclusion`, `fiber_gluten_free`_
- **26.** I'm vegan. Which leafy greens rank highest in calcium per 100 g?  
  _tags: `calcium_nondairy_source`, `iron_vegan_source`_
- **27.** I avoid dairy products. What seeds and legumes are richest in calcium?  
  _tags: `calcium_nondairy_source`, `allergy_driven_exclusion`_
- **28.** **[TEST]** I'm vegetarian and need zinc. Which plant foods are highest in zinc per 100 g?  
  _tags: `foundation_whole_food_rank`_
- **29.** I have a peanut allergy and need healthy fats. What other whole foods are highest in monounsaturated fat?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **30.** **[TEST]** I'm low-FODMAP. Which low-FODMAP vegetables provide the most potassium?  
  _tags: `potassium_or_low_potassium_ckd`, `foundation_whole_food_rank`_
- **31.** I'm dairy-free. Which plant foods provide the most phosphorus per 100 g?  
  _tags: `calcium_nondairy_source`, `allergy_driven_exclusion`_
- **32.** I have a tree-nut allergy. Which seeds are richest in magnesium as a nut substitute?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **33.** I'm vegan. Which whole foods are highest in folate per 100 g, and can any of them also provide B-12?  
  _tags: `iron_vegan_source`, `foundation_whole_food_rank`, `b12_vegan_disclosure`_
- **34.** I'm gluten-free. What non-gluten whole grains or seeds are highest in protein?  
  _tags: `fiber_gluten_free`, `foundation_whole_food_rank`_
- **35.** I have a shellfish allergy. Which non-shellfish whole foods are richest in zinc?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **36.** I'm vegan. Which whole foods per 100 g contain the most omega-3 fatty acids?  
  _tags: `iron_vegan_source`, `foundation_whole_food_rank`_
- **37.** I avoid all dairy. What are the top 5 non-dairy calcium sources among whole foods?  
  _tags: `calcium_nondairy_source`, `allergy_driven_exclusion`_
- **38.** I'm nightshade-free. Which whole foods outside nightshades are highest in vitamin A?  
  _tags: `foundation_whole_food_rank`_
- **39.** **[TEST]** I have a soy allergy. Which whole foods can replace edamame as a protein source?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_

## MODERATE (40 questions, ids 40–79)

- **40.** I'm vegan and iron-deficient. What are the top 5 plant iron sources ranked by mg per 100 g?  
  _tags: `iron_vegan_source`, `foundation_whole_food_rank`_
- **41.** I have a peanut allergy and need omega-3s. What fish or seeds rank highest in omega-3 per 100 g?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **42.** I'm gluten-free and also vegan. Which whole foods provide both high fiber and high protein?  
  _tags: `fiber_gluten_free`, `iron_vegan_source`, `foundation_whole_food_rank`_
- **43.** I'm dairy-allergic and also avoid soy. What whole foods give me the most calcium?  
  _tags: `calcium_nondairy_source`, `allergy_driven_exclusion`_
- **44.** **[TEST]** I'm vegan and also gluten-free. Which seeds or legumes are richest in zinc?  
  _tags: `iron_vegan_source`, `fiber_gluten_free`, `foundation_whole_food_rank`_
- **45.** **[TEST]** I have both a shellfish and a tree-nut allergy. Which whole foods can give me the most omega-3 per 100 g?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **46.** I'm nightshade-free and dairy-free. Which whole foods are highest in calcium and vitamin C combined?  
  _tags: `calcium_nondairy_source`, `allergy_driven_exclusion`_
- **47.** I'm vegan and pregnant. What whole foods rank highest in both iron and folate per 100 g?  
  _tags: `iron_vegan_source`, `foundation_whole_food_rank`_
- **48.** **[TEST]** I avoid gluten and dairy. Which whole foods give me both calcium and fiber?  
  _tags: `calcium_nondairy_source`, `fiber_gluten_free`_
- **49.** I'm low-FODMAP and need to boost potassium. Which low-FODMAP whole foods are richest in potassium?  
  _tags: `potassium_or_low_potassium_ckd`, `foundation_whole_food_rank`_
- **50.** I'm on a low-potassium diet for CKD. Which whole foods are low in potassium but still provide good protein?  
  _tags: `potassium_or_low_potassium_ckd`, `foundation_whole_food_rank`_
- **51.** I have CKD and my doctor said to limit potassium. What whole-food protein sources are lowest in potassium?  
  _tags: `potassium_or_low_potassium_ckd`, `foundation_whole_food_rank`_
- **52.** I'm soy-allergic and vegan. Which non-soy plant foods are highest in protein per 100 g?  
  _tags: `allergy_driven_exclusion`, `iron_vegan_source`, `foundation_whole_food_rank`_
- **53.** **[TEST]** I have a wheat allergy and need more fiber. Which gluten-free whole grains rank highest in fiber?  
  _tags: `allergy_driven_exclusion`, `fiber_gluten_free`_
- **54.** I'm vegan and need both vitamin D and B-12. Which non-animal whole foods are highest in vitamin D, and what should I know about B-12 in plant foods?  
  _tags: `b12_vegan_disclosure`, `foundation_whole_food_rank`, `iron_vegan_source`_
- **55.** **[TEST]** I'm dairy-free and also nut-allergic. What are the highest calcium whole foods excluding both categories?  
  _tags: `calcium_nondairy_source`, `allergy_driven_exclusion`_
- **56.** I'm vegan and want to boost B-12. What whole foods actually contain B-12?  
  _tags: `b12_vegan_disclosure`, `iron_vegan_source`_
- **57.** I'm gluten-free and need more magnesium. Which gluten-free whole foods are highest in magnesium?  
  _tags: `fiber_gluten_free`, `foundation_whole_food_rank`_
- **58.** I have a peanut allergy and tree-nut allergy. Which seeds are highest in protein and healthy fats?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **59.** I'm nightshade-free and low-FODMAP. Which whole foods in both categories are richest in fiber?  
  _tags: `fiber_gluten_free`, `foundation_whole_food_rank`_
- **60.** I'm vegetarian, dairy-free, and need calcium. Which legumes or seeds are highest in calcium?  
  _tags: `calcium_nondairy_source`, `foundation_whole_food_rank`_
- **61.** **[TEST]** I avoid nightshades and also gluten. Which non-nightshade, gluten-free whole foods are highest in iron?  
  _tags: `iron_vegan_source`, `fiber_gluten_free`, `foundation_whole_food_rank`_
- **62.** I'm egg-allergic and also vegetarian. Which plant foods are highest in vitamin D?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **63.** I have a shellfish allergy and need zinc. Which non-shellfish whole foods rank highest in zinc?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **64.** I'm low-FODMAP and also gluten-free. Which foods in both categories supply the most fiber?  
  _tags: `fiber_gluten_free`, `potassium_or_low_potassium_ckd`, `foundation_whole_food_rank`_
- **65.** I'm dairy-allergic and also egg-allergic. Which whole foods are richest in vitamin D?  
  _tags: `allergy_driven_exclusion`, `calcium_nondairy_source`_
- **66.** **[TEST]** I'm vegan and have low ferritin. Rank the top non-heme iron sources I can eat per 100 g.  
  _tags: `iron_vegan_source`, `foundation_whole_food_rank`_
- **67.** I have CKD and need to stay low in both potassium and phosphorus. Which whole foods fit both constraints?  
  _tags: `potassium_or_low_potassium_ckd`, `foundation_whole_food_rank`_
- **68.** I'm soy-allergic and gluten-free. Which legumes excluding soy are highest in protein?  
  _tags: `allergy_driven_exclusion`, `fiber_gluten_free`, `foundation_whole_food_rank`_
- **69.** I'm dairy-free and also low-FODMAP. Which low-FODMAP whole foods have the most calcium?  
  _tags: `calcium_nondairy_source`, `potassium_or_low_potassium_ckd`_
- **70.** I'm vegetarian, iron-deficient, and also gluten-free. Rank the best iron-rich, gluten-free foods.  
  _tags: `iron_vegan_source`, `fiber_gluten_free`, `foundation_whole_food_rank`_
- **71.** I have a peanut allergy and need selenium. Which whole foods excluding peanuts are highest in selenium?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **72.** **[TEST]** I'm vegan and gluten-free. Which grains or pseudograins give the most protein per 100 g?  
  _tags: `iron_vegan_source`, `fiber_gluten_free`, `foundation_whole_food_rank`_
- **73.** I'm low-FODMAP and vegan. Which low-FODMAP plant foods are highest in calcium?  
  _tags: `calcium_nondairy_source`, `iron_vegan_source`_
- **74.** I'm nightshade-free and vegan. Which vegetables outside nightshades are richest in iron?  
  _tags: `iron_vegan_source`, `foundation_whole_food_rank`_
- **75.** I have an egg allergy and need more choline. Which egg-free whole foods rank highest in choline?  
  _tags: `allergy_driven_exclusion`, `foundation_whole_food_rank`_
- **76.** I'm dairy-free and also vegan. What are the best plant sources of both calcium and magnesium?  
  _tags: `calcium_nondairy_source`, `iron_vegan_source`_
- **77.** I have a wheat allergy and low iron. Which gluten-free legumes or seeds are highest in iron?  
  _tags: `allergy_driven_exclusion`, `iron_vegan_source`, `fiber_gluten_free`_
- **78.** I'm vegan and need more potassium. Which plant foods rank highest in potassium per 100 g?  
  _tags: `iron_vegan_source`, `potassium_or_low_potassium_ckd`_
- **79.** I'm soy-allergic and dairy-allergic. Which seeds or legumes excluding soy give the most calcium?  
  _tags: `calcium_nondairy_source`, `allergy_driven_exclusion`_

## EDGE (20 questions, ids 80–99)

- **80.** I'm vegan. Are there any unfortified plant foods with meaningful B-12, or do I need supplements?  
  _tags: `b12_vegan_disclosure`, `iron_vegan_source`_
- **81.** I'm vegan and eat a lot of nori and tempeh. Can those replace a B-12 supplement?  
  _tags: `b12_vegan_disclosure`, `iron_vegan_source`_
- **82.** I rely on spinach for calcium since I'm dairy-free. Is spinach actually a good calcium source given its oxalate content?  
  _tags: `calcium_nondairy_source`, `allergy_driven_exclusion`_
- **83.** The FDC shows spinach is very high in calcium. But I've heard it's mostly unavailable due to oxalates — what should I eat instead?  
  _tags: `calcium_nondairy_source`, `foundation_whole_food_rank`_
- **84.** **[TEST]** I'm vegan. Can I get enough B-12 from chlorella or spirulina?  
  _tags: `b12_vegan_disclosure`, `iron_vegan_source`_
- **85.** I'm looking for high-iron plant foods but I've heard non-heme iron absorption is low. Which plants give me the best practical iron intake even accounting for absorption?  
  _tags: `iron_vegan_source`, `foundation_whole_food_rank`_
- **86.** Avocado is high in nutrients but also very calorie-dense. Is it a good nutrient-dense substitute or does the calorie load make it unsuitable for someone watching weight?  
  _tags: `foundation_whole_food_rank`_
- **87.** I need to increase calcium but also count calories. Chia seeds and almonds are high in calcium — how do they compare in calcium-per-calorie vs. collard greens?  
  _tags: `calcium_nondairy_source`, `foundation_whole_food_rank`_
- **88.** I want to rank seaweed by calcium and iron content using FDC, but seaweed varieties like wakame, hijiki, and nori may not all be cataloged. How should I handle the data gaps?  
  _tags: `calcium_nondairy_source`, `foundation_whole_food_rank`_
- **89.** I'm vegan and keep seeing different FDC values for kale calcium depending on whether I search Foundation or SR Legacy data. Which dataset should I trust for nutrient ranking?  
  _tags: `calcium_nondairy_source`, `foundation_whole_food_rank`, `b12_vegan_disclosure`_
- **90.** I'm vegan and reading that hemp seeds and flaxseeds have omega-3, but is it ALA or DHA/EPA? Does that matter for my health goals?  
  _tags: `iron_vegan_source`, `foundation_whole_food_rank`_
- **91.** I have CKD and my potassium needs to stay under 2,000 mg/day. I also need to avoid phosphorus additives. Which whole foods fit both constraints and still provide adequate protein?  
  _tags: `potassium_or_low_potassium_ckd`, `foundation_whole_food_rank`_
- **92.** I'm vegan and learned that phytic acid in legumes blocks zinc absorption. Rank the plant zinc sources that are also low in phytic acid or can be prepared to reduce it.  
  _tags: `iron_vegan_source`, `foundation_whole_food_rank`_
- **93.** **[TEST]** I eat Brazil nuts for selenium daily. Am I at risk of selenium toxicity, and how do they compare to other selenium sources in FDC data?  
  _tags: `foundation_whole_food_rank`, `allergy_driven_exclusion`_
- **94.** I'm nightshade-free and vegan. I want the top non-nightshade, plant-only sources of iron and B-12 combined — but is that even achievable without fortified foods?  
  _tags: `b12_vegan_disclosure`, `iron_vegan_source`, `foundation_whole_food_rank`_
- **95.** **[TEST]** FDC Foundation data may not list every variety of collard greens or bok choy. If my preferred variety isn't in Foundation, should I fall back to SR Legacy, and how might values differ?  
  _tags: `calcium_nondairy_source`, `foundation_whole_food_rank`_
- **96.** I have CKD, am dairy-free, and need calcium without high potassium. Which low-potassium, dairy-free foods also provide meaningful calcium per 100 g?  
  _tags: `potassium_or_low_potassium_ckd`, `calcium_nondairy_source`, `allergy_driven_exclusion`_
- **97.** I'm vegan and low-FODMAP. I've heard most legumes are high-FODMAP. What low-FODMAP plant foods still give me adequate protein and iron without compromising gut tolerance?  
  _tags: `iron_vegan_source`, `potassium_or_low_potassium_ckd`, `fiber_gluten_free`_
- **98.** **[TEST]** I want to use FDC to find the best vegan B-12 sources, but I've read that the B-12 analogs in algae are not bioavailable. How should the skill handle this and what should it recommend?  
  _tags: `b12_vegan_disclosure`, `foundation_whole_food_rank`_
- **99.** I have both a shellfish allergy and a soy allergy. I'm also gluten-free and vegan. Which whole foods give me the best omega-3, iron, and zinc without triggering any of my restrictions?  
  _tags: `allergy_driven_exclusion`, `iron_vegan_source`, `fiber_gluten_free`_
