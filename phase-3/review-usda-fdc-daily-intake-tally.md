# usda-fdc-daily-intake-tally — 100-question corpus

## Splits
- train_ids (80): `[0, 1, 3, 5, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 27, 28, 29, 30, 31, 32, 34, 36, 37, 38, 39, 40, 41, 44, 45, 46, 47, 48, 49, 50, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 64, 65, 67, 68, 69, 70, 71, 73, 75, 76, 77, 78, 79, 80, 81, 82, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99]`
- test_ids (20): `[2, 4, 10, 14, 23, 25, 33, 35, 42, 43, 51, 54, 61, 66, 72, 74, 83, 84, 85, 90]`
- seed: `2330528219`  mode: `hackathon`  threshold: `1.0`

## Ability-tag coverage

| Tag | Count |
|---|---|
| `over_or_under_limit_verdict` | 92 |
| `top_contributor_callout` | 49 |
| `sodium_daily_tally` | 31 |
| `added_sugar_daily_tally` | 27 |
| `saturated_fat_daily_tally` | 24 |
| `potassium_or_calories_tally` | 19 |
| `missing_data_disclosure` | 11 |
| `mixed_branded_and_whole_foods_tally` | 10 |

## EASY (40 questions, ids 0–39)

- ** 0.** I had a bowl of Quaker oatmeal with skim milk for breakfast and a Subway 6-inch turkey sandwich for lunch. Did I stay under 2,000 mg of sodium today?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`_
- ** 1.** I ate Campbell's chicken noodle soup for lunch and a grilled chicken breast with steamed broccoli for dinner. My sodium limit is 1,500 mg — did I go over?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`, `mixed_branded_and_whole_foods_tally`_
- ** 2.** **[TEST]** Breakfast was a Chobani strawberry yogurt and a banana. Lunch was a peanut butter and jelly sandwich on white bread. Did I stay under 25 g of added sugar?  
  _tags: `added_sugar_daily_tally`, `over_or_under_limit_verdict`_
- ** 3.** I had two scrambled eggs with cheddar cheese for breakfast and a McDonald's Quarter Pounder for dinner. Is my saturated fat under 20 g?  
  _tags: `saturated_fat_daily_tally`, `over_or_under_limit_verdict`_
- ** 4.** **[TEST]** My meals today were a bag of Lay's classic chips, a can of Campbell's tomato soup, and baked salmon with rice for dinner. Did I keep sodium below 2,300 mg?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`, `mixed_branded_and_whole_foods_tally`_
- ** 5.** I had a bowl of Frosted Flakes with whole milk for breakfast and a Coca-Cola with lunch. I'm prediabetic and trying to stay under 36 g added sugar — did I make it?  
  _tags: `added_sugar_daily_tally`, `over_or_under_limit_verdict`_
- ** 6.** I have CKD and my potassium limit is 2,000 mg. I ate a baked potato with butter, a banana, and a cup of plain Greek yogurt today. Did I go over?  
  _tags: `potassium_or_calories_tally`, `over_or_under_limit_verdict`_
- ** 7.** Breakfast was two slices of bacon and a fried egg. Dinner was a Chipotle chicken bowl with sour cream and cheese. My sat fat limit is 15 g — did I stay under?  
  _tags: `saturated_fat_daily_tally`, `over_or_under_limit_verdict`_
- ** 8.** I had a Subway 6-inch tuna sub for lunch and a frozen Lean Cuisine chicken alfredo for dinner. Did my sodium stay under 2,000 mg?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`_
- ** 9.** Today I had a Starbucks caramel latte for breakfast and a Snickers bar as an afternoon snack. My added sugar limit is 25 g — am I over?  
  _tags: `added_sugar_daily_tally`, `over_or_under_limit_verdict`_
- **10.** **[TEST]** I'm counting calories and trying to stay under 1,800 kcal. I ate a bowl of oatmeal with blueberries for breakfast, a turkey wrap for lunch, and grilled tilapia with asparagus for dinner. Did I stay under?  
  _tags: `potassium_or_calories_tally`, `over_or_under_limit_verdict`_
- **11.** My breakfast was two slices of whole-wheat toast with avocado, and dinner was a bowl of Progresso minestrone soup. Sodium limit is 1,500 mg — how did I do?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`_
- **12.** I drank a bottle of Gatorade after my morning run and had a Yoplait strawberry yogurt as a snack. Did my added sugar intake exceed 25 g?  
  _tags: `added_sugar_daily_tally`, `over_or_under_limit_verdict`_
- **13.** Lunch was a Wendy's Dave's Single burger and a small frosty. My cardiologist said keep saturated fat under 13 g. Did I go over just from those two items?  
  _tags: `saturated_fat_daily_tally`, `over_or_under_limit_verdict`_
- **14.** **[TEST]** I only ate once today — a big bowl of Pho with beef broth from a restaurant. My sodium limit is 2,300 mg. How close to the limit am I likely to be?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`_
- **15.** Breakfast was a cup of Honey Nut Cheerios with 2% milk. Lunch was a ham and cheese sandwich on white bread. Did I stay under 36 g of added sugar?  
  _tags: `added_sugar_daily_tally`, `over_or_under_limit_verdict`_
- **16.** I'm managing CKD stage 3 and my potassium limit is 2,500 mg. Today I had scrambled eggs, white rice with grilled chicken, and an apple. Did I stay under the limit?  
  _tags: `potassium_or_calories_tally`, `over_or_under_limit_verdict`_
- **17.** I had a cup of whole milk with breakfast cereal and a slice of pepperoni pizza for lunch. Is my saturated fat under 15 g?  
  _tags: `saturated_fat_daily_tally`, `over_or_under_limit_verdict`_
- **18.** For dinner I had a Stouffer's mac and cheese frozen entrée and a side salad with ranch dressing. My sodium limit is 2,000 mg — did dinner alone put me over?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`_
- **19.** I had a glass of orange juice and a Thomas' English muffin with strawberry jam for breakfast. Limit is 25 g added sugar. How am I doing?  
  _tags: `added_sugar_daily_tally`, `over_or_under_limit_verdict`_
- **20.** Lunch was a can of StarKist canned tuna in water mixed with mayo on crackers. Dinner was baked chicken thighs and steamed broccoli. Did I stay under 1,800 mg sodium?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`, `mixed_branded_and_whole_foods_tally`_
- **21.** I skipped breakfast. Lunch was a Chipotle chicken bowl with no soda, and I had a Chobani plain yogurt with honey as dessert. Added sugar limit is 25 g — am I good?  
  _tags: `added_sugar_daily_tally`, `over_or_under_limit_verdict`_
- **22.** Breakfast was Greek yogurt with granola. Lunch was a grilled cheese sandwich made with American cheese and butter. Limit is 13 g saturated fat. Did I go over?  
  _tags: `saturated_fat_daily_tally`, `over_or_under_limit_verdict`_
- **23.** **[TEST]** I'm trying to stay under 1,600 kcal today. I had a protein shake for breakfast, a Caesar salad with grilled chicken for lunch, and nothing else yet. Am I still on track?  
  _tags: `potassium_or_calories_tally`, `over_or_under_limit_verdict`_
- **24.** My only two meals today were a Panera Bread broccoli cheddar soup in a bread bowl for lunch and a bowl of brown rice with soy sauce and vegetables for dinner. Sodium limit is 2,000 mg — where did I land?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`_
- **25.** **[TEST]** I practice intermittent fasting and only eat one meal a day. Today it was a large Chipotle steak burrito with salsa and a Coke. Added sugar limit is 36 g — am I over?  
  _tags: `added_sugar_daily_tally`, `over_or_under_limit_verdict`_
- **26.** Dinner was a 6-oz ribeye steak with a pat of butter and mashed potatoes made with heavy cream. My sat fat limit is 20 g — how does dinner alone look?  
  _tags: `saturated_fat_daily_tally`, `over_or_under_limit_verdict`_
- **27.** I had a bowl of Ramen noodles (Maruchan chicken flavor) for lunch and a handful of Goldfish crackers as a snack. Sodium limit is 1,500 mg — did I blow past it?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`_
- **28.** Breakfast was a Nutri-Grain blueberry bar and a 12 oz can of Minute Maid orange juice. My added sugar limit is 25 g — am I already over by breakfast?  
  _tags: `added_sugar_daily_tally`, `over_or_under_limit_verdict`_
- **29.** I have CKD and can't exceed 3,000 mg potassium. Today I had oatmeal with raisins for breakfast, a baked sweet potato for lunch, and black beans and rice for dinner. Did I stay under?  
  _tags: `potassium_or_calories_tally`, `over_or_under_limit_verdict`_
- **30.** I had a bagel with full-fat cream cheese for breakfast and a Caesar salad with parmesan and croutons for lunch. Sat fat limit is 15 g — how am I doing?  
  _tags: `saturated_fat_daily_tally`, `over_or_under_limit_verdict`_
- **31.** Breakfast was two eggs and turkey bacon. Lunch was Amy's lentil soup. Dinner was a grilled pork chop with steamed green beans. My sodium limit is 2,300 mg — did I stay under?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`_
- **32.** I drank a 20 oz bottle of Sprite with lunch and had a Dannon Activia vanilla yogurt as a snack. Added sugar limit is 30 g — am I over?  
  _tags: `added_sugar_daily_tally`, `over_or_under_limit_verdict`_
- **33.** **[TEST]** My OMAD meal today was a Domino's cheese pizza — three slices. My sat fat limit is 20 g — did one meal put me over?  
  _tags: `saturated_fat_daily_tally`, `over_or_under_limit_verdict`_
- **34.** Lunch was a cup of Campbell's chicken noodle soup and a bag of Lay's classic chips. Dinner was a homemade turkey burger on a whole-wheat bun. Sodium limit 2,000 mg — how did I do?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`_
- **35.** **[TEST]** Breakfast was a bowl of Special K red berries cereal with skim milk. Snack was a small bag of M&Ms. My added sugar limit is 25 g — am I over?  
  _tags: `added_sugar_daily_tally`, `over_or_under_limit_verdict`_
- **36.** I'm counting calories and aim for under 2,000 kcal. Today I had a breakfast burrito, a chicken Caesar wrap for lunch, and a bowl of pasta with marinara sauce for dinner. Did I stay under?  
  _tags: `potassium_or_calories_tally`, `over_or_under_limit_verdict`_
- **37.** My only meal today was a Chipotle steak bowl with queso blanco and sour cream. Sat fat limit is 18 g — did I go over?  
  _tags: `saturated_fat_daily_tally`, `over_or_under_limit_verdict`_
- **38.** I had eggs and whole-wheat toast for breakfast, a deli turkey sandwich from Publix for lunch, and baked tilapia with a side salad for dinner. Sodium limit is 1,800 mg — did I stay under?  
  _tags: `sodium_daily_tally`, `over_or_under_limit_verdict`_
- **39.** I had a bowl of Quaker oatmeal with maple syrup for breakfast and a Clif Bar during my afternoon workout. My added sugar limit is 36 g — did I stay under?  
  _tags: `added_sugar_daily_tally`, `over_or_under_limit_verdict`_

## MODERATE (40 questions, ids 40–79)

- **40.** Full day: breakfast was two eggs and two strips of turkey bacon; lunch was a Subway 6-inch chicken teriyaki sub; afternoon snack was a bag of Lay's classic chips; dinner was Campbell's chicken noodle soup with crackers. My sodium limit is 2,000 mg — did I go over, and which meal was the worst offender?  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **41.** Today I had: Frosted Flakes with whole milk for breakfast, a Snapple peach tea with lunch, a Chobani strawberry yogurt as an afternoon snack, and a Coca-Cola with dinner. Added sugar limit is 36 g — am I over, and which item contributed the most?  
  _tags: `added_sugar_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **42.** **[TEST]** Breakfast: a bacon egg and cheese biscuit from McDonald's. Lunch: a Chipotle chicken burrito with cheese and sour cream. Snack: a handful of cheddar Goldfish crackers. Dinner: baked salmon with steamed vegetables. Sat fat limit is 20 g — did I go over, and what were the two biggest contributors?  
  _tags: `saturated_fat_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **43.** **[TEST]** My day: scrambled eggs and toast for breakfast; a can of Progresso chicken noodle soup for lunch; string cheese and Triscuit crackers for a snack; a Healthy Choice frozen chicken pasta bowl for dinner; a handful of pretzels before bed. Sodium limit is 1,800 mg — how far over am I, and what hit hardest?  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **44.** Breakfast: Honey Nut Cheerios with 2% milk plus a glass of orange juice. Morning snack: a Nutri-Grain strawberry bar. Lunch: a turkey wrap with veggies. Afternoon snack: a bag of Skittles. Dinner: grilled chicken with a side salad. Added sugar limit 25 g — am I over, and which item topped the list?  
  _tags: `added_sugar_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **45.** I'm tracking calories (limit 1,800 kcal). I had a McDonald's Egg McMuffin for breakfast, a Chick-fil-A grilled chicken sandwich for lunch, a banana and peanut butter for a snack, and a bowl of spaghetti with meat sauce for dinner. Did I go over, and which meal had the most calories?  
  _tags: `potassium_or_calories_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **46.** Full day of eating: Greek yogurt with granola for breakfast, a grilled cheese sandwich and tomato soup for lunch, a Starbucks caramel macchiato as an afternoon treat, and a pan-fried pork chop with mashed potatoes made with butter and cream for dinner. My sat fat limit is 15 g — over or under, and which two meals did the most damage?  
  _tags: `saturated_fat_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **47.** I'm a snacker and eat across the day: Ritz crackers with peanut butter, a hot dog on a bun, a slice of deli pepperoni pizza, a cup of instant miso soup, and canned black olives. Sodium limit 2,300 mg — did I make it, and which two snacks contributed the most sodium?  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **48.** Today's meals: a Dannon Activia vanilla yogurt for breakfast, a Subway sandwich for lunch, a Starbucks Frappuccino in the afternoon, a Nature Valley oats and honey granola bar as a snack, and pasta with marinara sauce for dinner. Added sugar limit is 30 g — over or under, and which item was top contributor?  
  _tags: `added_sugar_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **49.** CKD patient, potassium limit 2,500 mg. Today: oatmeal with dried apricots for breakfast, a banana and almond butter snack, grilled salmon with a baked sweet potato for lunch, and chicken stir-fry with broccoli and mushrooms for dinner. Did I go over, and which meals contributed the most potassium?  
  _tags: `potassium_or_calories_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **50.** Full-day log: two strips of bacon and two eggs fried in butter for breakfast; a cheeseburger from Burger King for lunch; Lay's chips as a snack; baked chicken breast with salad for dinner; a scoop of Ben & Jerry's ice cream at night. Sat fat limit is 18 g — did I go over, and what were the top 2 sources?  
  _tags: `saturated_fat_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **51.** **[TEST]** Intermittent fasting — I eat in a 6-hour window. Today I had: a large bowl of Pho with beef and noodles, a side order of spring rolls, a Diet Coke, and a Chobani yogurt for dessert. Sodium limit is 2,000 mg — how did I do, and what was the biggest sodium hit?  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **52.** Grazing day: a Kellogg's Pop-Tart in the morning, string cheese and grapes as a mid-morning snack, a Panera Bread frontega chicken sandwich for lunch, a Dunkin' glazed donut in the afternoon, and homemade chili for dinner. Added sugar limit is 25 g — did I go over, and which item was the worst?  
  _tags: `added_sugar_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **53.** Meals today: a Quaker oatmeal packet with brown sugar and cinnamon, a ham and Swiss cheese sandwich on sourdough, a cup of tomato basil soup, a pickle spear, and a grilled chicken dinner. Sodium limit is 1,500 mg — did I exceed it, and which item pushed me over?  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **54.** **[TEST]** Calorie budget is 2,200 kcal. I ate: two pancakes with syrup and butter, a grilled chicken wrap from Panera, a bag of Doritos cool ranch, a grande Starbucks latte, and slow-cooker beef stew for dinner. Did I go over, and which meal packed the most calories?  
  _tags: `potassium_or_calories_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **55.** I had: a full-fat Starbucks caramel latte for breakfast, a Wendy's Baconator for lunch, cheddar and crackers as an afternoon snack, and a dinner of shrimp pasta with heavy cream alfredo sauce. Sat fat limit is 20 g — way over or just over, and what were the two biggest contributors?  
  _tags: `saturated_fat_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **56.** My meals: Quaker maple and brown sugar oatmeal for breakfast, an apple with almond butter as a snack, a turkey sandwich for lunch, a 12 oz can of Pepsi with dinner, and a Yoplait original strawberry yogurt for dessert. Added sugar limit is 30 g — did I make it, and which item spiked my total the most?  
  _tags: `added_sugar_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **57.** Today I had: two strips of turkey bacon and an egg for breakfast; a can of Amy's lentil vegetable soup for lunch; string cheese and Triscuits for a snack; a Lean Cuisine frozen herb chicken for dinner; and a cup of miso soup before bed. Sodium limit is 2,000 mg — did I go over, and which meal was the biggest contributor?  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **58.** CKD stage 4, potassium limit 2,000 mg. I had: scrambled eggs with white toast, a cup of white rice with grilled chicken breast, an apple, and pasta with tomato sauce for dinner. Did I stay under my limit, and which meal contributed the most potassium?  
  _tags: `potassium_or_calories_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **59.** My eating today: a cheddar omelette for breakfast, two slices of pepperoni pizza from Pizza Hut for lunch, a 3 Musketeers bar for a snack, and a baked chicken thigh with brown rice for dinner. Sat fat limit is 13 g — over or under, and which two foods had the most?  
  _tags: `saturated_fat_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **60.** Today's full log: a glass of apple juice and a Nutri-Grain blueberry bar for breakfast; a chicken Caesar salad for lunch; a Starbucks Caramel Frappuccino in the afternoon; grilled salmon with steamed vegetables for dinner; and a small brownie for dessert. Added sugar limit is 36 g — am I over, and what was the top contributor?  
  _tags: `added_sugar_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **61.** **[TEST]** Meals: a packet of instant oatmeal for breakfast; Chipotle chicken burrito bowl with salsa for lunch; a bag of SunChips for a snack; a homemade chicken and vegetable stir-fry with soy sauce for dinner; and a cup of low-sodium V8 juice in the evening. Sodium limit is 2,300 mg — did I stay under, and which item had the most sodium?  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **62.** Tracking calories (limit 1,600 kcal). I had a Dannon Light & Fit yogurt for breakfast, a Chipotle chicken bowl (no rice, extra veggies) for lunch, a handful of cashews as a snack, and a bowl of vegetable soup with whole-wheat bread for dinner. Did I stay under my calorie budget, and what contributed the most?  
  _tags: `potassium_or_calories_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **63.** Full day: a Starbucks egg bites for breakfast; a Chick-fil-A spicy chicken sandwich with waffle fries for lunch; a string cheese stick as a snack; and a T-bone steak with butter and baked potato with sour cream for dinner. Sat fat limit is 18 g — am I over, and what were my top two sources?  
  _tags: `saturated_fat_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **64.** I am diabetic and track added sugar (limit 25 g). Today: a Kellogg's Raisin Bran bowl for breakfast, an orange as a morning snack, a PB&J on white bread for lunch, a 12 oz can of 7UP with dinner, and Jell-O sugar-free pudding for dessert. Over or under, and what was my top contributor?  
  _tags: `added_sugar_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **65.** OMAD: one large meal eaten at 2 PM — a Chipotle steak burrito with salsa, cheese, sour cream, and guacamole, plus a medium Coke and a bag of Doritos. Sodium limit 2,000 mg — all in one sitting, am I over, and what contributed most?  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **66.** **[TEST]** Meals: Greek yogurt parfait for breakfast; a BLT sandwich on white bread for lunch; a Starbucks Pumpkin Spice Latte as an afternoon snack; and a Kraft mac and cheese bowl for dinner. My sat fat limit is 15 g — did I go over, and which two meals were the worst?  
  _tags: `saturated_fat_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **67.** CKD patient tracking potassium (limit 3,400 mg). My day: oatmeal with a tablespoon of peanut butter, a grilled chicken breast with white rice and green beans, a pear as a snack, and beef tacos with lettuce, cheese, and salsa for dinner. Did I stay under 3,400 mg, and which meals drove the most potassium?  
  _tags: `potassium_or_calories_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **68.** Meals today: a bowl of Frosted Mini-Wheats with skim milk for breakfast; peanut butter crackers and a 100-calorie pack of Oreos as snacks; a Chick-fil-A grilled nuggets wrap for lunch; and pasta with marinara sauce for dinner. Added sugar limit is 30 g — did I stay under, and what was the biggest hit?  
  _tags: `added_sugar_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **69.** I graze all day: Wasa crispbread with hummus, a cup of Campbell's tomato soup, a deli ham and Swiss wrap, carrot sticks with ranch dip, and grilled salmon for dinner. Sodium limit is 1,500 mg — did I go over, and which two items dominated my sodium intake?  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **70.** Full-day log for sat fat (limit 20 g): a cream cheese bagel for breakfast; a Cobb salad with blue cheese dressing for lunch; a bag of Doritos as a snack; and a ribeye steak dinner with butter-sautéed mushrooms and a side of creamed spinach. Top 2 contributors?  
  _tags: `saturated_fat_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **71.** Calorie goal is 2,000 kcal. Meals: two large eggs and two pancakes with butter and syrup for breakfast; a Chipotle chicken bowl (rice, beans, chicken, salsa) for lunch; a protein bar as a snack; and grilled cod with roasted potatoes for dinner. Did I stay under, and which meal was the calorie heavyweight?  
  _tags: `potassium_or_calories_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **72.** **[TEST]** Day log: peanut butter on whole-wheat toast for breakfast; a bowl of ramen from a restaurant with pork broth for lunch; an afternoon Clif Bar snack; a frozen Healthy Choice Power Bowl for dinner; and string cheese for evening. Sodium limit 2,000 mg — result and top contributor?  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **73.** I'm prediabetic, limit 25 g added sugar. Today: a Thomas' cinnamon raisin bagel with regular cream cheese for breakfast; a 16 oz Vitamin Water for a mid-morning snack; a grilled chicken salad for lunch; an afternoon Yoplait original strawberry yogurt; and steak with roasted carrots for dinner. Over or under, and what contributed most?  
  _tags: `added_sugar_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **74.** **[TEST]** Sat fat limit is 13 g. My meals: a Starbucks iced coffee with 2% milk for breakfast; a grilled cheese on sourdough for lunch; Lay's potato chips as a snack; baked salmon with asparagus for dinner; and a small bowl of ice cream for dessert. Did I go over, and what were the top 2 contributors?  
  _tags: `saturated_fat_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **75.** CKD, potassium limit 2,500 mg. Meals: two scrambled eggs on white toast, a cup of white rice with grilled chicken, a bowl of canned peaches, and beef and potato soup for dinner. Did I stay under, and which meal had the highest potassium?  
  _tags: `potassium_or_calories_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **76.** Meals: a Dunkin' glazed donut and large iced coffee with sugar for breakfast; a plain chicken sandwich for lunch; a Kind Dark Chocolate Nuts & Sea Salt bar for a snack; and homemade pasta primavera for dinner. Added sugar limit is 30 g — over or under, and what was the biggest single contributor?  
  _tags: `added_sugar_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **77.** Full-day sodium log (limit 1,800 mg): a bowl of instant grits with cheese for breakfast; a Panera Bread turkey and avocado BLT for lunch; a handful of pretzels for a snack; and a homemade chicken enchilada with canned green chili sauce for dinner. How did I do, and what hit hardest?  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **78.** My cardiologist gave me a 15 g sat fat limit. Today: a Chick-fil-A chicken biscuit for breakfast; a KFC original recipe chicken breast with mashed potatoes and gravy for lunch; an afternoon Chobani flip almond coco loco yogurt; and baked trout with steamed green beans for dinner. Am I over, and what drove the total?  
  _tags: `saturated_fat_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **79.** Tracking calories (limit 1,800 kcal): Greek yogurt with honey and walnuts for breakfast; a Chipotle veggie burrito bowl for lunch; a banana as a snack; spaghetti bolognese for dinner; and a glass of whole milk at night. Did I go over, and which meal was the calorie peak?  
  _tags: `potassium_or_calories_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_

## EDGE (20 questions, ids 80–99)

- **80.** I had a Quaker oatmeal cup for breakfast, a homemade shakshuka for lunch, and a can of Campbell's low-sodium tomato soup for dinner. My sodium limit is 1,500 mg. Note: I can't find an FDC entry for homemade shakshuka — can you still tally what's available and flag what's missing?  
  _tags: `sodium_daily_tally`, `missing_data_disclosure`, `over_or_under_limit_verdict`_
- **81.** I had: a Chobani strawberry yogurt, a homemade tres leches cake slice, a 12 oz Dr Pepper, and a Subway cookie. My added sugar limit is 25 g. The tres leches cake was made from scratch — if FDC doesn't have a match, tell me what you included and what you had to skip.  
  _tags: `added_sugar_daily_tally`, `missing_data_disclosure`, `over_or_under_limit_verdict`_
- **82.** My meals were: two strips of bacon with eggs, a grilled cheese sandwich, a grandmother's homemade beef stroganoff, and a scoop of Breyers vanilla ice cream. Sat fat limit is 18 g. Since the stroganoff is a family recipe with no FDC entry, show me what you can calculate and note what's excluded.  
  _tags: `saturated_fat_daily_tally`, `missing_data_disclosure`, `over_or_under_limit_verdict`_
- **83.** **[TEST]** Today's meals mix branded and whole foods: a Lean Cuisine frozen meal (branded, label nutrients per serving), a 6 oz raw chicken breast cooked plain (whole food, FDC per 100g), a can of Amy's tomato bisque (branded), and 1 cup of cooked brown rice (whole food). Sodium limit 2,000 mg — can you handle both nutrient bases and tell me the top contributor?  
  _tags: `sodium_daily_tally`, `mixed_branded_and_whole_foods_tally`, `top_contributor_callout`_
- **84.** **[TEST]** My day included: a Yoplait original strawberry yogurt (branded), a fresh mango (whole food), a Starbucks bottled Frappuccino mocha (branded), and a homemade smoothie with 1 cup of strawberries and 1 banana (whole foods). Added sugar limit 25 g — tally both branded and whole-food items and flag the biggest contributor.  
  _tags: `added_sugar_daily_tally`, `mixed_branded_and_whole_foods_tally`, `top_contributor_callout`_
- **85.** **[TEST]** I need a batch of 22 foods checked for sodium in a single day — I'm a competitive eater doing a food challenge. Meals included: Ramen noodles (Maruchan), dill pickles, canned tuna, deli turkey breast, American cheese, Spam, soy sauce packet, pretzels, saltine crackers, cottage cheese, jarred salsa, hot sauce, chicken broth, frozen shrimp, canned black beans, ham slice, Velveeta, cream of mushroom soup, ketchup, Worcestershire sauce, olive tapenade, and one raw chicken breast. Sodium limit 2,300 mg. Note this is over 20 items — batch accordingly.  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **86.** Tracking potassium for CKD (limit 2,500 mg). My meals mix branded and whole foods: a bowl of Quaker oats (branded) with half a banana (whole food), a Lean Cuisine salmon meal (branded), a raw avocado half (whole food), and a can of Del Monte green beans (branded). Correctly scale the whole foods and parse the branded label nutrients.  
  _tags: `potassium_or_calories_tally`, `mixed_branded_and_whole_foods_tally`, `over_or_under_limit_verdict`_
- **87.** Meals: a McDonald's Sausage McMuffin with egg, a deli-counter lamb gyro from a local Greek restaurant with no FDC entry, a bag of Kettle Brand sea salt chips, and a homemade lamb and lentil stew. The gyro and lamb stew likely have no direct FDC entry — exclude them with a note, tally what you can, and tell me the top sat fat contributor from what remains.  
  _tags: `saturated_fat_daily_tally`, `missing_data_disclosure`, `top_contributor_callout`_
- **88.** I think I had around 6 different sweet items today but I can't remember exactly what the third one was — I know it was some kind of store-bought muffin. I had: a Starbucks Caramel Frappuccino, a Dannon Activia vanilla yogurt, [unknown muffin], a can of Sprite, and Frosted Flakes with milk. Added sugar limit is 25 g. I know you may not be able to nail the muffin — can you ask me to clarify or estimate based on a standard store-bought blueberry muffin?  
  _tags: `added_sugar_daily_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **89.** I had: Heinz canned tomato soup (branded), a bowl of homemade bone broth (no FDC entry), grilled wild-caught king salmon (whole food), and a bag of Late July sea salt tortilla chips (branded). Sodium limit 1,500 mg. Please use label nutrients for the branded items, per-100g for the wild salmon, and disclose that the bone broth is excluded.  
  _tags: `sodium_daily_tally`, `missing_data_disclosure`, `mixed_branded_and_whole_foods_tally`_
- **90.** **[TEST]** Full day: a Chobani whole-milk plain yogurt (branded), two large whole eggs fried in 1 tbsp of butter (whole food), a Kraft Singles American cheese slice (branded), and a 4 oz beef ground chuck patty (whole food, 80/20). Sat fat limit is 15 g — correctly calculate the branded items per serving and the whole foods per 100g, then give me a pass/fail.  
  _tags: `saturated_fat_daily_tally`, `mixed_branded_and_whole_foods_tally`, `over_or_under_limit_verdict`_
- **91.** CKD patient tracking potassium (limit 2,000 mg). Today I had: a glass of carrot juice (whole food), a can of white kidney beans (branded), a homemade mole sauce chicken (restaurant-style mole, likely no FDC match), and steamed white rice. Disclose the mole chicken as excluded, tally the rest, and tell me if I'm over.  
  _tags: `potassium_or_calories_tally`, `missing_data_disclosure`, `over_or_under_limit_verdict`_
- **92.** I need to tally sodium for 21 items eaten across a party-food day: Lay's classic chips, Tostitos salsa, Velveeta queso dip, deli turkey slices, American cheese, pepperoni, Ritz crackers, canned black olives, dill pickle spears, Pringles original, a hot dog, ketchup, yellow mustard, Campbell's French onion soup, soy sauce packets, garlic bread, frozen mozzarella sticks, ranch dressing, blue cheese dip, a bratwurst, and homemade kimchi (no FDC). Sodium limit 2,300 mg. Batch into groups of ≤20, exclude what's missing, and name the top 2 contributors.  
  _tags: `sodium_daily_tally`, `top_contributor_callout`, `missing_data_disclosure`_
- **93.** My meals included a Kirkland Signature protein bar (Costco brand — might not be in FDC), a 12 oz Coke, a Chobani strawberry yogurt, a bag of Skittles fun-size, and a homemade fruit tart. Added sugar limit 36 g. Disclose any items not found in FDC, tally what you can, and name the top sugar contributor.  
  _tags: `added_sugar_daily_tally`, `missing_data_disclosure`, `top_contributor_callout`_
- **94.** Mixed branded and whole food day for sat fat tracking (limit 20 g): a Ben & Jerry's Half Baked ice cream (branded, label per serving), 3 oz of cheddar cheese (whole food, per 100g), a Land O'Lakes butter tablespoon (branded), and a 6 oz beef New York strip steak (whole food). Scale each properly and name the top sat fat contributor.  
  _tags: `saturated_fat_daily_tally`, `mixed_branded_and_whole_foods_tally`, `top_contributor_callout`_
- **95.** I'm tracking total calories today and need a batch of 23 foods tallied — meal-prep Sunday taste-testing day. Foods: hard-boiled eggs x2, Greek yogurt, banana, oatmeal, almond butter, blueberries, grilled chicken breast, cooked quinoa, cherry tomatoes, cucumber slices, mixed greens, olive oil dressing, canned tuna in water, whole-wheat bread, hummus, carrot sticks, roasted sweet potato, black beans, avocado, brown rice, raw almonds, apple slices, and protein shake. Calorie limit 2,500 kcal. Batch the FDC calls and tell me my total.  
  _tags: `potassium_or_calories_tally`, `top_contributor_callout`, `over_or_under_limit_verdict`_
- **96.** I had oatmeal for breakfast, a hand-rolled sushi platter from a local Japanese restaurant (no FDC match), Lay's classic chips for a snack, and a Progresso Italian-style wedding soup for dinner. Sodium limit 1,800 mg. Please tally the three items you can find, flag the sushi platter as excluded, and tell me if the remaining items alone put me over.  
  _tags: `sodium_daily_tally`, `missing_data_disclosure`, `over_or_under_limit_verdict`_
- **97.** My day: Honey Nut Cheerios (branded) with fresh strawberries (whole food) for breakfast; a Tropicana 100% orange juice 12 oz (branded); a homemade baklava slice (no standard FDC entry); and a plain Chobani yogurt with honey drizzle (branded + whole honey). Added sugar limit 30 g. Handle the dual nutrient bases, exclude the baklava with a note, and tally the rest.  
  _tags: `added_sugar_daily_tally`, `mixed_branded_and_whole_foods_tally`, `missing_data_disclosure`_
- **98.** Sat fat limit is 13 g. Meals: a Starbucks egg white and red pepper egg bites for breakfast, a homemade lamb korma (restaurant-style, no FDC match), a Kind bar for a snack, and a grilled pork tenderloin for dinner. Exclude the lamb korma with a note, tally the three remaining items, and tell me if I'm over or under.  
  _tags: `saturated_fat_daily_tally`, `missing_data_disclosure`, `over_or_under_limit_verdict`_
- **99.** I need a dual tally today: sodium (limit 2,300 mg) AND potassium (limit 2,500 mg for CKD). Meals: scrambled eggs with diced ham, a can of Progresso kidney bean soup, a banana, grilled tilapia with soy sauce marinade, and a small bag of pretzels. Can the skill run both nutrient tallies in a single batch fetch and give me pass/fail on each?  
  _tags: `sodium_daily_tally`, `potassium_or_calories_tally`, `over_or_under_limit_verdict`_
