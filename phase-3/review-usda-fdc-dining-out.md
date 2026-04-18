# usda-fdc-dining-out — 100-question corpus

## Splits
- train_ids (80): `[0, 1, 2, 3, 5, 6, 8, 9, 10, 12, 13, 15, 16, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 46, 47, 48, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69, 71, 73, 74, 76, 77, 78, 80, 81, 82, 84, 86, 87, 88, 90, 92, 93, 94, 95, 96, 97, 98, 99]`
- test_ids (20): `[4, 7, 11, 14, 21, 24, 32, 39, 45, 49, 52, 61, 70, 72, 75, 79, 83, 85, 89, 91]`
- seed: `1266166717`  mode: `hackathon`  threshold: `1.0`

## Ability-tag coverage

| Tag | Count |
|---|---|
| `brand_keyword_match` | 90 |
| `calorie_ranked_pick` | 47 |
| `protein_ranked_pick` | 28 |
| `macro_constraint_at_menu` | 27 |
| `sodium_ranked_pick` | 25 |
| `brand_name_resolution` | 10 |
| `menu_item_not_in_fdc` | 10 |

## EASY (40 questions, ids 0–39)

- ** 0.** What is the lowest-calorie burger at McDonald's?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- ** 1.** Which Panera sandwich has the least sodium?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- ** 2.** What is the highest-protein chicken item at Chick-fil-A?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`_
- ** 3.** What is the lowest-calorie drink at Starbucks?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- ** 4.** **[TEST]** Which Subway sandwich has the least sodium?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- ** 5.** What is the highest-protein bowl at Chipotle?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`_
- ** 6.** What is the lowest-calorie taco at Taco Bell?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- ** 7.** **[TEST]** Which salad at Wendy's has the fewest calories?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- ** 8.** What is the lowest-sodium breakfast item at Dunkin?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- ** 9.** Which KFC side dish has the fewest calories?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- **10.** What is the highest-protein sandwich at Burger King?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`_
- **11.** **[TEST]** Which Popeyes item has the least sodium?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- **12.** What is the lowest-calorie pizza slice at Domino's?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- **13.** Which Pizza Hut pizza has the fewest calories per slice?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- **14.** **[TEST]** What is the highest-protein breakfast item at McDonald's?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`_
- **15.** Which Starbucks food item has the least sodium?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- **16.** What is the lowest-calorie chicken sandwich at Chick-fil-A?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- **17.** Which Chipotle bowl has the least sodium?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- **18.** What is the lowest-calorie breakfast sandwich at Panera?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- **19.** Which Taco Bell item has the most protein?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`_
- **20.** What is the lowest-calorie salad at Wendys?  
  _tags: `brand_name_resolution`, `calorie_ranked_pick`_
- **21.** **[TEST]** Which Subway footlong has the least sodium?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- **22.** What is the lowest-fat burger at BK?  
  _tags: `brand_name_resolution`, `calorie_ranked_pick`_
- **23.** Which KFC chicken piece has the least sodium?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- **24.** **[TEST]** What is the highest-protein item at Popeyes?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`_
- **25.** Which Domino's pasta has the fewest calories?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- **26.** What is the lowest-calorie donut at Dunkin' Donuts?  
  _tags: `brand_name_resolution`, `calorie_ranked_pick`_
- **27.** Which McDonald's breakfast sandwich has the least sodium?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- **28.** What is the highest-protein salad at Panera?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`_
- **29.** Which Chick-fil-A side dish has the fewest calories?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- **30.** What is the lowest-calorie item on the T-Bell breakfast menu?  
  _tags: `brand_name_resolution`, `calorie_ranked_pick`_
- **31.** Which Starbucks sandwich has the most protein?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`_
- **32.** **[TEST]** What is the lowest-sodium side at Wendy's?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- **33.** Which Chipotle salad has the fewest calories?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- **34.** What is the lowest-calorie dessert at DQ?  
  _tags: `brand_name_resolution`, `calorie_ranked_pick`_
- **35.** Which Subway 6-inch has the most protein?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`_
- **36.** What is the least-sodium pizza at Pizza Hut?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- **37.** Which Burger King breakfast item has the fewest calories? (I always just say BK)  
  _tags: `brand_name_resolution`, `calorie_ranked_pick`_
- **38.** What is the highest-protein item at KFC?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`_
- **39.** **[TEST]** Which Panera soup has the least sodium?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_

## MODERATE (40 questions, ids 40–79)

- **40.** What at Chipotle has under 700 calories and at least 40g of protein?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`_
- **41.** What Starbucks drink has under 200 calories and at least 10g of protein?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`_
- **42.** What is the best Wendy's option under 500 calories with at least 30g protein?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`, `calorie_ranked_pick`_
- **43.** I'm on a keto diet at Chipotle — what menu items fit with under 10g carbs?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`_
- **44.** What McDonald's breakfast item has under 400 calories and at least 20g protein?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`, `calorie_ranked_pick`_
- **45.** **[TEST]** Which Panera salads have under 600mg sodium and more than 25g protein?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`, `macro_constraint_at_menu`_
- **46.** What is the best low-carb sandwich at Subway under 300 calories?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`, `calorie_ranked_pick`_
- **47.** Which Taco Bell items fit a 1200-calorie daily budget for lunch — under 400 calories with decent protein?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`, `calorie_ranked_pick`_
- **48.** What is the highest-protein meal at Chick-fil-A under 600 calories?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `calorie_ranked_pick`_
- **49.** **[TEST]** Which Dunkin breakfast sandwich has the most protein under 450 calories?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `calorie_ranked_pick`_
- **50.** What Burger King item has under 1000mg sodium and at least 25g protein?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`, `macro_constraint_at_menu`_
- **51.** Which Domino's pizza toppings and crust combination keeps a slice under 250 calories?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`, `macro_constraint_at_menu`_
- **52.** **[TEST]** What KFC meal is under 800mg sodium with the most protein?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`, `protein_ranked_pick`_
- **53.** Which Popeyes chicken sandwich has the fewest calories while still being at least 30g protein?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`, `protein_ranked_pick`_
- **54.** I have hypertension — what at Panera keeps sodium under 700mg for a full lunch?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`, `macro_constraint_at_menu`_
- **55.** What is the best post-workout meal at Chipotle maximizing protein while staying under 800 calories?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `macro_constraint_at_menu`_
- **56.** What are the macros on the Starbucks holiday Gingerbread Latte? It's seasonal — does FDC have it?  
  _tags: `brand_keyword_match`, `menu_item_not_in_fdc`, `macro_constraint_at_menu`_
- **57.** What Subway wrap has the most protein under 600mg sodium?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `sodium_ranked_pick`_
- **58.** Which McDonald's burger is under 500 calories and has more than 25g protein?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`, `calorie_ranked_pick`_
- **59.** What is the best Taco Bell vegetarian option under 500 calories?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`, `macro_constraint_at_menu`_
- **60.** Which Pizza Hut personal pizza has the most protein under 700 calories?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `calorie_ranked_pick`_
- **61.** **[TEST]** What Wendy's item is the best high-protein, low-fat option for someone cutting calories?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `macro_constraint_at_menu`_
- **62.** I'm diabetic — which Chick-fil-A items have under 30g carbs and are not fried?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`_
- **63.** What is the lowest-sodium, highest-protein option at KFC for someone with high blood pressure?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`, `protein_ranked_pick`_
- **64.** Which Dunkin donut has the fewest carbs? Also, do they still have the limited-time apple cider donut and is it in FDC?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`, `menu_item_not_in_fdc`_
- **65.** What is the best Five Guys burger option for someone staying under 700 calories?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- **66.** Which Shake Shack burger has the most protein per calorie?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `calorie_ranked_pick`_
- **67.** What Arby's sandwich has the highest protein under 800mg sodium?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `sodium_ranked_pick`_
- **68.** Domino's just launched a new loaded tot flavor LTO — can FDC find it? Also which existing wing flavor has the least calories?  
  _tags: `brand_keyword_match`, `menu_item_not_in_fdc`, `calorie_ranked_pick`_
- **69.** What Starbucks protein box has the most protein under 400 calories?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `calorie_ranked_pick`_
- **70.** **[TEST]** Which Panera flatbread pizza has the least sodium?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- **71.** What is the best Popeyes meal for someone on a high-protein diet under 900 calories?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `calorie_ranked_pick`_
- **72.** **[TEST]** Which Jack in the Box item has the highest protein under 600 calories?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `calorie_ranked_pick`_
- **73.** What Taco Bell item fits a keto diet under 10g net carbs?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`_
- **74.** Which Burger King salad or wrap keeps me under 500 calories with at least 20g protein?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`, `calorie_ranked_pick`_
- **75.** **[TEST]** What Subway sandwich has the best protein-to-calorie ratio?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `calorie_ranked_pick`_
- **76.** Which McDonald's McCafé drink has the fewest calories?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- **77.** What Chipotle burrito bowl can I build to stay under 600 calories with at least 35g protein?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`, `protein_ranked_pick`_
- **78.** Which Chick-fil-A sauce has the fewest calories to keep my meal low-calorie?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- **79.** **[TEST]** What is the best high-protein low-sodium lunch at Wendy's for someone watching their heart health?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `sodium_ranked_pick`_

## EDGE (20 questions, ids 80–99)

- **80.** What is the nutrition info for the McRib at McDonald's? I know it's seasonal.  
  _tags: `brand_keyword_match`, `menu_item_not_in_fdc`_
- **81.** I'm at McDs — what's the healthiest thing I can get for under 300 calories?  
  _tags: `brand_name_resolution`, `calorie_ranked_pick`_
- **82.** Does Starbs have anything under 100 calories that's actually filling?  
  _tags: `brand_name_resolution`, `calorie_ranked_pick`, `macro_constraint_at_menu`_
- **83.** **[TEST]** What's the healthiest option at In-N-Out for someone on a low-carb diet?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`_
- **84.** I'm at Whataburger — what has the most protein and is under 700 calories?  
  _tags: `brand_keyword_match`, `protein_ranked_pick`, `calorie_ranked_pick`_
- **85.** **[TEST]** What should I get at Culver's if I'm trying to stay under 600 calories?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`_
- **86.** What are the nutrition facts for Taco Bell's Nacho Fries? They're back for a limited time.  
  _tags: `brand_keyword_match`, `menu_item_not_in_fdc`_
- **87.** I don't really know what I want at Chipotle — just something healthy and filling. What do you recommend?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`_
- **88.** What does a McDonald's Happy Meal with apple slices look like nutritionally for my 6-year-old?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`_
- **89.** **[TEST]** Can I get the calorie info for the Starbucks Pumpkin Spice Latte? It's only available in fall.  
  _tags: `brand_keyword_match`, `menu_item_not_in_fdc`_
- **90.** What is Mickey D's lowest-calorie dessert?  
  _tags: `brand_name_resolution`, `calorie_ranked_pick`_
- **91.** **[TEST]** I'm at BK and I want something under 400 calories — what should I get?  
  _tags: `brand_name_resolution`, `calorie_ranked_pick`_
- **92.** What are the calories in Panera's seasonal autumn squash soup?  
  _tags: `brand_keyword_match`, `menu_item_not_in_fdc`_
- **93.** I want a kids' meal at Chick-fil-A — which one has the least sodium for my toddler?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`_
- **94.** Does Wingstop have any options on FoodData Central? I'm trying to find their nutrition info.  
  _tags: `brand_keyword_match`, `menu_item_not_in_fdc`_
- **95.** I have no idea what I want at Taco Bell — what's something low-calorie and low-sodium that actually tastes good?  
  _tags: `brand_keyword_match`, `calorie_ranked_pick`, `sodium_ranked_pick`_
- **96.** What's the nutrition breakdown for the Popeyes Blackened Chicken Sandwich? I think it might be a regional item.  
  _tags: `brand_keyword_match`, `menu_item_not_in_fdc`_
- **97.** I'm at Subway and I want something filling but I don't know what — just make it under 500 calories with at least 25g protein.  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`, `calorie_ranked_pick`_
- **98.** What's a good kids' meal at McDonald's that keeps fat under 15g and sodium under 600mg?  
  _tags: `brand_keyword_match`, `macro_constraint_at_menu`, `sodium_ranked_pick`_
- **99.** I'm visiting a Whataburger in Texas — does FoodData Central have their full menu? What's lowest-sodium on there?  
  _tags: `brand_keyword_match`, `sodium_ranked_pick`, `menu_item_not_in_fdc`_
