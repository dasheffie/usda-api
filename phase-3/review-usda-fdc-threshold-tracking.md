# usda-fdc-threshold-tracking — 100-question corpus

## Splits
- train_ids (80): `[0, 2, 3, 4, 5, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 39, 40, 41, 42, 43, 44, 45, 46, 47, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 67, 68, 69, 70, 71, 72, 73, 74, 76, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 92, 95, 96, 97, 99]`
- test_ids (20): `[1, 9, 10, 13, 19, 27, 37, 38, 48, 49, 63, 64, 65, 66, 75, 77, 85, 93, 94, 98]`
- seed: `430362674`  mode: `hackathon`  threshold: `1.0`

## Ability-tag coverage

| Tag | Count |
|---|---|
| `pass_verdict_with_remaining` | 49 |
| `tight_overage_warning` | 35 |
| `added_sugar_remaining_budget` | 33 |
| `sodium_remaining_budget` | 31 |
| `saturated_fat_remaining_budget` | 25 |
| `calories_remaining_budget` | 21 |
| `clear_overage_swap_suggestion` | 21 |
| `labelnutrients_preferred` | 10 |

## EASY (40 questions, ids 0–39)

- ** 0.** I've had 15 g of added sugar today. Can I have a Yoplait Original Strawberry yogurt?  
  _tags: `added_sugar_remaining_budget`, `pass_verdict_with_remaining`_
- ** 1.** **[TEST]** I've consumed 800 mg of sodium so far today. Is a can of Campbell's Chicken Noodle Soup okay?  
  _tags: `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- ** 2.** I've eaten 8 g of saturated fat today. Can I have a Chobani Whole Milk Plain yogurt?  
  _tags: `saturated_fat_remaining_budget`, `pass_verdict_with_remaining`_
- ** 3.** I've had 1,200 calories today and my daily target is 2,000. Can I have a KIND Dark Chocolate Nuts & Sea Salt bar?  
  _tags: `calories_remaining_budget`, `pass_verdict_with_remaining`_
- ** 4.** I've had 10 g of added sugar today. Can I have a Chobani Strawberry Greek yogurt?  
  _tags: `added_sugar_remaining_budget`, `pass_verdict_with_remaining`_
- ** 5.** I've consumed 600 mg of sodium today. Is it okay to have a serving of Lay's Classic potato chips?  
  _tags: `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- ** 6.** I've eaten 5 g of saturated fat today. Can I have a Clif Bar Chocolate Chip?  
  _tags: `saturated_fat_remaining_budget`, `pass_verdict_with_remaining`_
- ** 7.** I've had 1,400 calories today and my goal is 1,800. Can I eat a Halo Top Vanilla Bean ice cream pint?  
  _tags: `calories_remaining_budget`, `clear_overage_swap_suggestion`_
- ** 8.** I've had 5 g of added sugar today. Can I have a Siggi's Plain 0% yogurt?  
  _tags: `added_sugar_remaining_budget`, `pass_verdict_with_remaining`_
- ** 9.** **[TEST]** I've had 1,000 mg of sodium today. Can I have a serving of Ritz Crackers?  
  _tags: `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- **10.** **[TEST]** I've eaten 3 g of saturated fat today. Can I have an RXBar Chocolate Sea Salt?  
  _tags: `saturated_fat_remaining_budget`, `pass_verdict_with_remaining`_
- **11.** I've had 1,600 calories today and my target is 2,200. Can I have a Chipotle chicken burrito bowl?  
  _tags: `calories_remaining_budget`, `pass_verdict_with_remaining`_
- **12.** I've had 20 g of added sugar today. Can I have a Nature Valley Oats 'n Honey granola bar?  
  _tags: `added_sugar_remaining_budget`, `pass_verdict_with_remaining`_
- **13.** **[TEST]** I've consumed 400 mg of sodium today. Is a serving of Wheat Thins okay?  
  _tags: `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- **14.** I've eaten 10 g of saturated fat today. Can I have a Fage Total 0% Greek yogurt?  
  _tags: `saturated_fat_remaining_budget`, `pass_verdict_with_remaining`_
- **15.** I've had 1,800 calories today and my goal is 2,500. Can I have a Starbucks Caramel Frappuccino (grande)?  
  _tags: `calories_remaining_budget`, `pass_verdict_with_remaining`_
- **16.** I've had 12 g of added sugar today. Can I have a pack of Oreos (3-cookie serving)?  
  _tags: `added_sugar_remaining_budget`, `clear_overage_swap_suggestion`_
- **17.** I've consumed 900 mg of sodium today. Can I have a serving of Doritos Nacho Cheese?  
  _tags: `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- **18.** I've eaten 6 g of saturated fat today. Can I have a Chobani Flip Almond Coco Loco?  
  _tags: `saturated_fat_remaining_budget`, `pass_verdict_with_remaining`_
- **19.** **[TEST]** I've had 1,000 calories today and my daily budget is 1,500. Can I have a Chipotle steak bowl?  
  _tags: `calories_remaining_budget`, `pass_verdict_with_remaining`_
- **20.** I've had 8 g of added sugar today. Can I have a Starbucks Vanilla Latte (tall)?  
  _tags: `added_sugar_remaining_budget`, `pass_verdict_with_remaining`_
- **21.** I've consumed 1,100 mg of sodium today. Can I have a serving of Goldfish crackers (cheddar)?  
  _tags: `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- **22.** I've eaten 4 g of saturated fat today. Can I have a Nature Valley Crunchy Peanut Butter granola bar?  
  _tags: `saturated_fat_remaining_budget`, `pass_verdict_with_remaining`_
- **23.** I've had 1,300 calories today and my goal is 1,800. Can I eat a Pop-Tart (one pastry)?  
  _tags: `calories_remaining_budget`, `pass_verdict_with_remaining`_
- **24.** I've had 6 g of added sugar today. Can I have a Siggi's Strawberry 2% yogurt?  
  _tags: `added_sugar_remaining_budget`, `pass_verdict_with_remaining`_
- **25.** I've consumed 500 mg of sodium today. Can I have a serving of Cheetos Crunchy?  
  _tags: `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- **26.** I've eaten 7 g of saturated fat today. Can I have a Ben & Jerry's Cherry Garcia ice cream (single serving)?  
  _tags: `saturated_fat_remaining_budget`, `clear_overage_swap_suggestion`_
- **27.** **[TEST]** I've had 1,500 calories today and my daily goal is 2,000. Can I have a KIND Caramel Almond & Sea Salt bar?  
  _tags: `calories_remaining_budget`, `pass_verdict_with_remaining`_
- **28.** I've had 18 g of added sugar today. Can I have a Yoplait Original Blueberry yogurt?  
  _tags: `added_sugar_remaining_budget`, `tight_overage_warning`_
- **29.** I've consumed 1,500 mg of sodium today. Can I have a can of Campbell's Tomato Soup?  
  _tags: `sodium_remaining_budget`, `clear_overage_swap_suggestion`_
- **30.** I've eaten 9 g of saturated fat today. Can I have a Clif Bar Peanut Butter Banana?  
  _tags: `saturated_fat_remaining_budget`, `pass_verdict_with_remaining`_
- **31.** I've had 1,700 calories today and my target is 2,000. Can I have a Starbucks Iced Brown Sugar Oat Milk Shaken Espresso?  
  _tags: `calories_remaining_budget`, `pass_verdict_with_remaining`_
- **32.** I've had 5 g of added sugar today. Can I have an RXBar Blueberry?  
  _tags: `added_sugar_remaining_budget`, `pass_verdict_with_remaining`, `labelnutrients_preferred`_
- **33.** I've consumed 700 mg of sodium today. Is a serving of Ritz Toasted Chips okay?  
  _tags: `sodium_remaining_budget`, `pass_verdict_with_remaining`, `labelnutrients_preferred`_
- **34.** I've eaten 2 g of saturated fat today. Can I have a Fage Total 2% Greek yogurt?  
  _tags: `saturated_fat_remaining_budget`, `pass_verdict_with_remaining`_
- **35.** I've had 900 calories today and my goal is 1,600. Can I have a Chipotle veggie burrito bowl?  
  _tags: `calories_remaining_budget`, `pass_verdict_with_remaining`_
- **36.** I've had 14 g of added sugar today. Can I have a Chobani Peach on the Bottom yogurt?  
  _tags: `added_sugar_remaining_budget`, `pass_verdict_with_remaining`_
- **37.** **[TEST]** I've consumed 1,200 mg of sodium today. Can I have a serving of Lay's Baked Original chips?  
  _tags: `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- **38.** **[TEST]** I've eaten 11 g of saturated fat today. Can I have a Nature Valley Peanut Butter Granola Bar?  
  _tags: `saturated_fat_remaining_budget`, `pass_verdict_with_remaining`_
- **39.** I've had 1,100 calories today and my daily target is 1,800. Can I have a Pop-Tart Frosted Brown Sugar Cinnamon (one pastry)?  
  _tags: `calories_remaining_budget`, `pass_verdict_with_remaining`, `labelnutrients_preferred`_

## MODERATE (40 questions, ids 40–79)

- **40.** I've had 22 g of added sugar today and my daily limit is 25 g. Can I have a Yoplait Original Strawberry yogurt?  
  _tags: `added_sugar_remaining_budget`, `tight_overage_warning`_
- **41.** I've consumed 2,050 mg of sodium today and my target is 2,300. Can I have a serving of Doritos Nacho Cheese?  
  _tags: `sodium_remaining_budget`, `tight_overage_warning`_
- **42.** I've eaten 18 g of saturated fat today and my limit is 20 g. Can I have a Ben & Jerry's Chocolate Chip Cookie Dough?  
  _tags: `saturated_fat_remaining_budget`, `clear_overage_swap_suggestion`_
- **43.** I have 400 calories left for the day and my dinner goal is to stay under that. Can I have a Chipotle chicken burrito bowl?  
  _tags: `calories_remaining_budget`, `clear_overage_swap_suggestion`_
- **44.** I've had 18 g of added sugar AND 1,800 mg of sodium today. My limits are 25 g sugar and 2,300 mg sodium. Can I have a Starbucks Caramel Macchiato (grande)?  
  _tags: `added_sugar_remaining_budget`, `sodium_remaining_budget`, `tight_overage_warning`_
- **45.** I've had 20 g of added sugar today and my limit is 25 g. Can I have a Chobani Strawberry Banana yogurt?  
  _tags: `added_sugar_remaining_budget`, `tight_overage_warning`_
- **46.** I've consumed 2,100 mg of sodium today and my limit is 2,300 mg. Is it okay to have a can of Campbell's Chicken Noodle Soup?  
  _tags: `sodium_remaining_budget`, `clear_overage_swap_suggestion`_
- **47.** I've eaten 17 g of saturated fat today and my daily target is 20 g. Can I have a serving of Goldfish Cheddar crackers?  
  _tags: `saturated_fat_remaining_budget`, `tight_overage_warning`_
- **48.** **[TEST]** I have 350 calories left for dinner and my daily goal is 1,800. Can I have a Starbucks Iced Pumpkin Spice Latte (grande)?  
  _tags: `calories_remaining_budget`, `tight_overage_warning`_
- **49.** **[TEST]** I've had 15 g of added sugar AND 1,000 mg of sodium today. Can I have a serving of Nature Valley Oats 'n Honey granola bars? My limits are 30 g sugar and 1,500 mg sodium.  
  _tags: `added_sugar_remaining_budget`, `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- **50.** I've had 24 g of added sugar today and my limit is 25 g. Can I have a KIND Dark Chocolate Cherry Cashew bar?  
  _tags: `added_sugar_remaining_budget`, `tight_overage_warning`, `labelnutrients_preferred`_
- **51.** I've consumed 2,200 mg of sodium today and my target is 2,300 mg. Can I have a serving of Cheetos Crunchy?  
  _tags: `sodium_remaining_budget`, `clear_overage_swap_suggestion`_
- **52.** I've eaten 16 g of saturated fat today and my limit is 20 g. Can I have a Chobani Whole Milk Plain yogurt?  
  _tags: `saturated_fat_remaining_budget`, `tight_overage_warning`_
- **53.** I have 500 calories left today and my daily goal is 2,000. It's dinnertime — can I have a Chipotle steak burrito with sour cream and guacamole?  
  _tags: `calories_remaining_budget`, `clear_overage_swap_suggestion`_
- **54.** I've had 16 g of added sugar AND 12 g of saturated fat today. My limits are 25 g sugar and 15 g saturated fat. Can I have Ben & Jerry's Phish Food ice cream?  
  _tags: `added_sugar_remaining_budget`, `saturated_fat_remaining_budget`, `clear_overage_swap_suggestion`_
- **55.** I've had 27 g of added sugar today and my limit is 30 g. Can I have a Yoplait Whips Strawberry Mist?  
  _tags: `added_sugar_remaining_budget`, `tight_overage_warning`, `labelnutrients_preferred`_
- **56.** I've consumed 1,900 mg of sodium today and my target is 2,000 mg. Can I have a serving of Wheat Thins Original?  
  _tags: `sodium_remaining_budget`, `tight_overage_warning`_
- **57.** I've eaten 14 g of saturated fat today and my limit is 15 g. Can I have a Clif Bar White Chocolate Macadamia Nut?  
  _tags: `saturated_fat_remaining_budget`, `tight_overage_warning`_
- **58.** I have 600 calories left for dinner and my daily target is 1,800. Can I have a Starbucks Double Smoked Bacon, Cheddar & Egg Sandwich?  
  _tags: `calories_remaining_budget`, `pass_verdict_with_remaining`_
- **59.** I've had 10 g of added sugar AND 1,400 mg of sodium today. My limits are 25 g sugar and 1,500 mg sodium. Can I have a serving of Ritz Crackers?  
  _tags: `added_sugar_remaining_budget`, `sodium_remaining_budget`, `tight_overage_warning`_
- **60.** I've had 30 g of added sugar today and my limit is 36 g. Can I have a Starbucks White Chocolate Mocha (grande)?  
  _tags: `added_sugar_remaining_budget`, `clear_overage_swap_suggestion`_
- **61.** I've consumed 1,300 mg of sodium today and my target is 1,500 mg. Can I have a serving of Lay's Classic potato chips?  
  _tags: `sodium_remaining_budget`, `tight_overage_warning`_
- **62.** I've eaten 12 g of saturated fat today and my limit is 13 g. Can I have a Fage Total 5% Greek yogurt?  
  _tags: `saturated_fat_remaining_budget`, `tight_overage_warning`_
- **63.** **[TEST]** I have 250 calories left today and my daily target is 1,600. Can I have a Pop-Tart Frosted Strawberry (one pastry)?  
  _tags: `calories_remaining_budget`, `tight_overage_warning`_
- **64.** **[TEST]** I've had 12 g of added sugar AND 1,900 mg of sodium today. My limits are 25 g sugar and 2,300 mg sodium. Can I have a bowl of Campbell's Tomato Soup with Ritz crackers?  
  _tags: `added_sugar_remaining_budget`, `sodium_remaining_budget`, `tight_overage_warning`_
- **65.** **[TEST]** I've had 26 g of added sugar today and my limit is 30 g. Can I have a Halo Top Birthday Cake ice cream (one serving)?  
  _tags: `added_sugar_remaining_budget`, `pass_verdict_with_remaining`_
- **66.** **[TEST]** I've consumed 1,800 mg of sodium today and my limit is 2,000 mg. Can I have a serving of Doritos Cool Ranch?  
  _tags: `sodium_remaining_budget`, `clear_overage_swap_suggestion`_
- **67.** I've eaten 11 g of saturated fat today and my limit is 13 g. Can I have a Siggi's Strawberry Whole Milk yogurt?  
  _tags: `saturated_fat_remaining_budget`, `pass_verdict_with_remaining`_
- **68.** I have 700 calories left for dinner and my daily goal is 2,000. Can I have Chipotle barbacoa bowl with beans and cheese?  
  _tags: `calories_remaining_budget`, `pass_verdict_with_remaining`_
- **69.** I've had 8 g of added sugar AND 1,600 mg of sodium today. My limits are 25 g sugar and 2,300 mg sodium. Can I have a Starbucks Pike Place brewed coffee with 2 pumps of vanilla syrup?  
  _tags: `added_sugar_remaining_budget`, `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- **70.** I've had 32 g of added sugar today and my limit is 36 g. Can I have an Oreo Double Stuf (3-cookie serving)?  
  _tags: `added_sugar_remaining_budget`, `tight_overage_warning`_
- **71.** I've consumed 1,200 mg of sodium today and my limit is 1,500 mg. Can I have a serving of Cheetos Flamin' Hot?  
  _tags: `sodium_remaining_budget`, `tight_overage_warning`_
- **72.** I've eaten 15 g of saturated fat today and my limit is 18 g. Can I have a Chobani Flip S'Mores yogurt?  
  _tags: `saturated_fat_remaining_budget`, `pass_verdict_with_remaining`_
- **73.** I have 450 calories left today and my goal is 2,000. It's 9 PM — can I have Ben & Jerry's Tonight Dough (one serving)?  
  _tags: `calories_remaining_budget`, `tight_overage_warning`_
- **74.** I've had 14 g of added sugar AND 14 g of saturated fat today. My limits are 25 g sugar and 16 g saturated fat. Can I have a Starbucks Java Chip Frappuccino (grande)?  
  _tags: `added_sugar_remaining_budget`, `saturated_fat_remaining_budget`, `clear_overage_swap_suggestion`_
- **75.** **[TEST]** I've had 33 g of added sugar today and my limit is 36 g. Can I have a Yoplait Original Harvest Peach yogurt?  
  _tags: `added_sugar_remaining_budget`, `pass_verdict_with_remaining`_
- **76.** I've consumed 2,150 mg of sodium today and my limit is 2,300 mg. Can I have a serving of Goldfish Cheddar crackers?  
  _tags: `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- **77.** **[TEST]** I've eaten 18 g of saturated fat today and my limit is 20 g. Can I have an RXBar Peanut Butter bar?  
  _tags: `saturated_fat_remaining_budget`, `pass_verdict_with_remaining`_
- **78.** I have 800 calories left for dinner and my daily goal is 2,200. Can I have a Chipotle carnitas burrito with everything on it?  
  _tags: `calories_remaining_budget`, `tight_overage_warning`_
- **79.** I've had 20 g of added sugar AND 2,000 mg of sodium today. My limits are 25 g sugar and 2,300 mg sodium. Can I have a serving of Ritz Bits Peanut Butter?  
  _tags: `added_sugar_remaining_budget`, `sodium_remaining_budget`, `tight_overage_warning`_

## EDGE (20 questions, ids 80–99)

- **80.** I've had 10 g of added sugar today. Can I have a 'Whole Foods 365 Strawberry Organic Yogurt'? I don't think it's in the USDA database.  
  _tags: `added_sugar_remaining_budget`, `pass_verdict_with_remaining`_
- **81.** I've consumed 1,000 mg of sodium today. Can I check if 'Trader Joe's Organic Minestrone Soup' fits in my 2,300 mg limit?  
  _tags: `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- **82.** I've had maybe 15 g of added sugar today — not totally sure. Can I have a Chobani Mango yogurt? My limit is 25 g.  
  _tags: `added_sugar_remaining_budget`, `tight_overage_warning`_
- **83.** I've eaten roughly 10 g of saturated fat today. Can I have a Ben & Jerry's Chunky Monkey ice cream? My limit is 13 g.  
  _tags: `saturated_fat_remaining_budget`, `clear_overage_swap_suggestion`_
- **84.** I've had 24 g of added sugar today and my limit is 25 g. Can I have a Yoplait Light Strawberry yogurt? If I'm barely over, suggest something in the same category.  
  _tags: `added_sugar_remaining_budget`, `tight_overage_warning`, `clear_overage_swap_suggestion`_
- **85.** **[TEST]** I've consumed 2,280 mg of sodium today and my limit is 2,300 mg. Can I have a serving of Campbell's Well Yes! Chicken Noodle Soup? Also, every lower-sodium soup I've tried is also over budget.  
  _tags: `sodium_remaining_budget`, `tight_overage_warning`, `clear_overage_swap_suggestion`_
- **86.** I've eaten 5 g of saturated fat today. Can I have a KIND Breakfast Protein Bar Almond Butter? I'm not sure if it has labelNutrients or just per-100g data.  
  _tags: `saturated_fat_remaining_budget`, `labelnutrients_preferred`_
- **87.** I've had 1,900 calories today and my goal is 2,000. Can I have a Halo Top Sea Salt Caramel pint? The label says 280 calories for the whole pint but I want to eat only half.  
  _tags: `calories_remaining_budget`, `tight_overage_warning`, `labelnutrients_preferred`_
- **88.** I've had around 20 g of added sugar today — give or take 5 g. My limit is 25 g. Can I have a Nature Valley Sweet & Salty Nut Almond bar?  
  _tags: `added_sugar_remaining_budget`, `tight_overage_warning`_
- **89.** I've consumed 1,400 mg of sodium today and my limit is 1,500 mg. Can I have a serving of Lay's Kettle Cooked Original chips? The FDC entry for this product may only have per-100g data, not labelNutrients.  
  _tags: `sodium_remaining_budget`, `tight_overage_warning`, `labelnutrients_preferred`_
- **90.** I've eaten 12 g of saturated fat today and my limit is 13 g. Can I have a Clif Builder's Protein Bar Chocolate? I need you to suggest an alternative if it doesn't fit, but please check if alternatives also don't exceed my budget.  
  _tags: `saturated_fat_remaining_budget`, `tight_overage_warning`, `clear_overage_swap_suggestion`_
- **91.** I've had 1,750 calories today and my goal is 1,800. Can I have a Starbucks Pumpkin Cream Cold Brew (grande)? Please check both calories and added sugar (I'm also tracking sugar at 25 g/day, I've had 20 g so far).  
  _tags: `calories_remaining_budget`, `added_sugar_remaining_budget`, `tight_overage_warning`_
- **92.** I've consumed about 2,000 mg of sodium today — I'm estimating, could be 100 mg off. My limit is 2,300 mg. Can I have a serving of Doritos Spicy Sweet Chili? This might be a newer variety with limited FDC data.  
  _tags: `sodium_remaining_budget`, `pass_verdict_with_remaining`_
- **93.** **[TEST]** I've eaten 9 g of saturated fat today and my limit is 13 g. Can I have a Ben & Jerry's Non-Dairy Cherry Garcia? The non-dairy version may have different nutrition than the regular version in FDC.  
  _tags: `saturated_fat_remaining_budget`, `labelnutrients_preferred`_
- **94.** **[TEST]** I've had 23 g of added sugar today and my limit is 25 g. Can I have a Chobani Flip Peanut Butter Dream yogurt? If I'm over, please suggest a same-category alternative — but I know most flavored yogurts are also high in added sugar.  
  _tags: `added_sugar_remaining_budget`, `tight_overage_warning`, `clear_overage_swap_suggestion`_
- **95.** I've consumed 1,450 mg of sodium today and my limit is 1,500 mg. Can I have Campbell's Chunky Classic Chicken Noodle Soup? Please suggest alternatives if not, and check that the alternatives aren't also over my budget.  
  _tags: `sodium_remaining_budget`, `tight_overage_warning`, `clear_overage_swap_suggestion`_
- **96.** I've eaten about 17 g of saturated fat today — somewhere between 15 and 19 g. My limit is 20 g. Can I have a Starbucks Egg & Cheddar Protein Box?  
  _tags: `saturated_fat_remaining_budget`, `tight_overage_warning`_
- **97.** I have 300 calories left today and my goal is 1,600. Can I have an RXBar Chocolate Sea Salt? I believe this product only has full nutrition data available as per-100g, not as labelNutrients.  
  _tags: `calories_remaining_budget`, `pass_verdict_with_remaining`, `labelnutrients_preferred`_
- **98.** **[TEST]** I've had 24 g of added sugar AND 2,250 mg of sodium today. My limits are 25 g sugar and 2,300 mg sodium. Can I have a bag of Smartfood White Cheddar Popcorn? I've already eaten all lower-sugar, lower-sodium alternatives I know of.  
  _tags: `added_sugar_remaining_budget`, `sodium_remaining_budget`, `tight_overage_warning`, `clear_overage_swap_suggestion`_
- **99.** I've consumed 1,490 mg of sodium today and my limit is 1,500 mg. I want to have Lay's Flamin' Hot chips — but I'm not sure if this specific variety is in FDC. If it's not, can you suggest a similar snack that is in the database and fits my budget?  
  _tags: `sodium_remaining_budget`, `tight_overage_warning`, `clear_overage_swap_suggestion`_
