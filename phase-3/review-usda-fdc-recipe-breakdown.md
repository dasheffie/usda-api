# usda-fdc-recipe-breakdown — 100-question corpus

## Splits
- train_ids (80): `[1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 67, 68, 69, 70, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 97, 98, 99]`
- test_ids (20): `[0, 6, 9, 14, 18, 26, 33, 34, 48, 58, 65, 66, 71, 72, 76, 78, 80, 94, 95, 96]`
- seed: `2421837700`  mode: `hackathon`  threshold: `1.0`

## Ability-tag coverage

| Tag | Count |
|---|---|
| `portion_conversion_cup_to_grams` | 96 |
| `ingredient_resolution_sr_legacy` | 86 |
| `macro_sum_across_ingredients` | 82 |
| `batch_fetch_efficient` | 40 |
| `micro_sum_across_ingredients` | 36 |
| `per_serving_output` | 17 |
| `ingredient_not_in_fdc_substitute` | 10 |
| `ambiguous_ingredient_disclosure` | 10 |

## EASY (40 questions, ids 0–39)

- ** 0.** **[TEST]** 1 cup raw spinach + 1 medium banana + 1 cup whole milk — how many calories total?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- ** 1.** 2 large eggs scrambled in 1 tsp butter — what are the macros (calories, protein, fat, carbs)?  
  _tags: `ingredient_resolution_sr_legacy`, `macro_sum_across_ingredients`_
- ** 2.** 1 cup rolled oats + 1 cup water — calories and protein?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- ** 3.** 1 medium apple + 2 tbsp peanut butter — calories?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- ** 4.** 1 slice whole wheat bread + 1 oz cheddar cheese — how many grams of protein?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- ** 5.** Half a cup of plain Greek yogurt + 1 tbsp honey — calories and carbs?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- ** 6.** **[TEST]** 1 medium orange + 1 cup skim milk — total calories?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- ** 7.** 2 tbsp olive oil + 3 oz grilled chicken breast — fat and protein?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- ** 8.** 1 cup cooked brown rice + 1 tbsp soy sauce — sodium total?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`_
- ** 9.** **[TEST]** 1/2 cup black beans + 1/4 cup salsa — iron content?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`_
- **10.** 1 cup almond milk + 1 medium banana + 1 tbsp almond butter — calories?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **11.** 2 slices whole wheat toast + 1/4 avocado — calories and fat?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **12.** 1 cup broccoli florets + 1 tsp olive oil — calories?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **13.** 3 oz canned tuna + 1 tbsp mayo — protein and fat?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **14.** **[TEST]** 1 cup strawberries + 1 cup plain yogurt — calcium?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`_
- **15.** 2 tbsp butter + 1 cup all-purpose flour — calories?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **16.** 1 large egg + 1/4 cup shredded mozzarella — protein?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **17.** 1 medium sweet potato + 1 tsp brown sugar — carbs and calories?  
  _tags: `ingredient_resolution_sr_legacy`, `macro_sum_across_ingredients`_
- **18.** **[TEST]** 1 cup lentils + 2 cups water (cooked) — fiber and protein?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`_
- **19.** 2 tbsp cream cheese + 1 plain bagel — total calories?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **20.** 1 cup orange juice + 1 tbsp chia seeds — calories and fiber?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`_
- **21.** 4 oz salmon fillet + 1 tsp lemon juice — protein and fat?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **22.** 1 cup cottage cheese + 1/2 cup blueberries — protein?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **23.** 1 medium carrot + 2 tbsp hummus — calories?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **24.** 1 cup raw oats + 1 tbsp maple syrup + 1 cup 2% milk — total calories?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **25.** 2 oz cheddar + 6 whole grain crackers — fat and calories?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **26.** **[TEST]** 1 tbsp flaxseed + 1 cup unsweetened almond milk — fiber?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`_
- **27.** 3 oz ground beef (80% lean) + 1 oz American cheese — fat and protein?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **28.** 1 medium banana + 1 tbsp peanut butter — potassium?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`_
- **29.** 1/2 cup frozen edamame + 1 tsp sesame oil — protein and fat?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **30.** 1 cup whole milk + 2 tbsp cocoa powder + 1 tsp sugar — calories?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **31.** 4 oz boneless chicken thigh + 1 tbsp olive oil — calories and fat?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **32.** 1/2 cup cooked quinoa + 1/4 cup cucumber slices — carbs?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **33.** **[TEST]** 2 tbsp sunflower seeds + 1 medium apple — calories?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **34.** **[TEST]** 1 cup beef broth + 2 oz lean ground beef — sodium?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`_
- **35.** 1 tsp cinnamon + 1 cup oatmeal + 1 tbsp brown sugar — total carbs?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **36.** 2 large eggs + 1/4 cup bell pepper — calories and vitamin C?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`_
- **37.** 1 cup raspberry + 1 tbsp sugar — carbs?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **38.** 3 oz shrimp + 1 tsp garlic powder — protein?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **39.** 1/2 cup canned chickpeas + 1 tbsp tahini — iron? Note: if tahini isn't in FDC as a prepared product, use the best available substitute and disclose it.  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`, `ingredient_not_in_fdc_substitute`_

## MODERATE (40 questions, ids 40–79)

- **40.** Greek salad: 4 cups romaine lettuce, 1/2 cup cucumber slices, 1/4 cup kalamata olives, 3 oz feta cheese, 1/4 cup cherry tomatoes, 2 tbsp olive oil, 1 tbsp red wine vinegar — give me macros and sodium.  
  _tags: `ingredient_resolution_sr_legacy`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `batch_fetch_efficient`_
- **41.** Overnight oats: 1/2 cup rolled oats, 3/4 cup oat milk, 1 tbsp chia seeds, 1/2 cup blueberries, 1 tbsp almond butter, 1 tsp honey — total calories, protein, and fiber for 1 serving.  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `batch_fetch_efficient`_
- **42.** Chicken stir-fry: 5 oz chicken breast, 1 cup broccoli, 1/2 cup snap peas, 2 tbsp soy sauce, 1 tbsp sesame oil, 1 cup cooked white rice — total calories, protein, and sodium.  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `batch_fetch_efficient`_
- **43.** Veggie omelet: 3 large eggs, 1/4 cup diced onion, 1/4 cup diced bell pepper, 1/4 cup mushrooms, 1 oz Swiss cheese, 1 tsp butter — macros breakdown?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_
- **44.** Pasta primavera: 2 oz dry pasta, 1 cup mixed vegetables (zucchini, bell pepper, onion), 2 tbsp olive oil, 2 tbsp parmesan, 2 cloves garlic — calories, carbs, and fat?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_
- **45.** Lentil soup: 1 cup dry green lentils, 2 medium carrots, 2 stalks celery, 1 medium onion, 2 cloves garlic, 1 tbsp olive oil, 4 cups vegetable broth — iron and fiber for the whole pot.  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`, `batch_fetch_efficient`_
- **46.** Turkey wrap: 1 large flour tortilla, 4 oz sliced turkey breast, 2 tbsp mayo, 1 cup romaine, 1/4 cup shredded carrot, 1 oz provolone — macros and sodium?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `batch_fetch_efficient`_
- **47.** Smoothie bowl: 1 cup frozen acai pulp, 1/2 cup frozen mango, 1 medium banana, 1/2 cup coconut milk, toppings: 1 tbsp granola, 1 tbsp coconut flakes — total calories and sugar?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_
- **48.** **[TEST]** Bean burrito filling: 1 cup pinto beans, 1/2 cup cooked brown rice, 1/4 cup salsa, 1/4 cup shredded cheddar, 2 tbsp sour cream — total calories and iron?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `batch_fetch_efficient`_
- **49.** Banana bread batter: 3 medium bananas, 2 cups all-purpose flour, 1/2 cup sugar, 1/4 cup butter, 2 large eggs, 1 tsp baking soda — calories and carbs for the whole loaf?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_
- **50.** Quinoa power bowl: 1 cup cooked quinoa, 3 oz grilled salmon, 1/2 cup edamame, 1/2 cup roasted sweet potato, 2 tbsp tahini dressing — give me macros and calcium.  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `batch_fetch_efficient`_
- **51.** Tuna salad sandwich: 3 oz canned tuna, 2 tbsp mayo, 1 tbsp diced celery, 2 slices whole wheat bread, 2 leaves romaine — protein and sodium?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `batch_fetch_efficient`_
- **52.** Chocolate protein shake: 1 cup whole milk, 1 scoop whey protein powder (30g), 1 medium banana, 2 tbsp cocoa powder, 1 tbsp peanut butter, 5 ice cubes — total calories and protein?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_
- **53.** Minestrone soup: 1/2 cup kidney beans, 1/2 cup elbow pasta, 1 cup diced tomatoes, 1 medium zucchini, 1 medium carrot, 1/2 cup spinach, 3 cups vegetable broth — fiber and sodium?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`, `batch_fetch_efficient`_
- **54.** Chicken Caesar salad: 4 cups romaine, 4 oz grilled chicken breast, 1 oz parmesan, 1/4 cup croutons, 2 tbsp Caesar dressing — total calories and fat?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_
- **55.** Oatmeal raisin cookie dough (makes 24 cookies): 2 cups oats, 1 cup flour, 1/2 cup butter, 1/2 cup brown sugar, 1/2 cup raisins, 2 eggs, 1 tsp vanilla — macros per cookie?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **56.** Beef taco filling (serves 4): 1 lb ground beef, 1 packet taco seasoning (28g), 1/2 cup diced onion, 1/4 cup tomato paste — calories per taco?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `per_serving_output`_
- **57.** Spinach and feta frittata (6 portions): 6 large eggs, 1 cup fresh spinach, 2 oz feta, 1/4 cup milk, 1 tbsp olive oil — calories and protein per slice?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **58.** **[TEST]** Pesto pasta: 3 oz dry spaghetti, 2 tbsp basil pesto, 1 oz pine nuts, 1 oz parmesan, 1 cup cherry tomatoes — calories, fat, and carbs?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_
- **59.** Vegetable curry (serves 3): 2 cups coconut milk, 1 cup diced tomatoes, 1 cup chickpeas, 1 medium potato, 1 cup spinach, 2 tbsp curry powder — macros per serving?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **60.** Mango lassi: 1 cup mango chunks, 1 cup plain yogurt, 1/2 cup whole milk, 2 tbsp sugar, 1/4 tsp cardamom — calories and sugar?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **61.** Shrimp fried rice: 1 cup cooked white rice, 4 oz shrimp, 2 large eggs, 1/2 cup frozen peas, 2 tbsp soy sauce, 1 tbsp vegetable oil, 2 green onions — sodium and protein?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `batch_fetch_efficient`_
- **62.** Avocado toast plate: 2 slices sourdough, 1/2 medium avocado, 2 large eggs (poached), 1 tsp red pepper flakes, 1 tsp everything bagel seasoning — total macros?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_
- **63.** Chicken noodle soup (serves 6): 8 oz chicken breast, 2 cups egg noodles, 3 medium carrots, 3 stalks celery, 1 medium onion, 6 cups chicken broth — sodium per serving?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **64.** Blueberry muffins (makes 12): 2 cups flour, 3/4 cup sugar, 1/2 cup butter, 2 eggs, 3/4 cup milk, 1 cup blueberries, 1 tsp baking powder — calories per muffin?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **65.** **[TEST]** Black bean tacos (makes 4): 1 cup black beans, 4 small corn tortillas, 1/2 cup corn, 1/4 cup red onion, 1/4 cup cilantro, 1 tbsp lime juice — iron and fiber per taco?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **66.** **[TEST]** Hummus bowl: 1/2 cup homemade hummus, 1/4 cup cucumber, 1/4 cup cherry tomatoes, 1/4 cup kalamata olives, 2 tbsp olive oil, 1 whole wheat pita — macros and calcium?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `batch_fetch_efficient`_
- **67.** Steak salad: 5 oz sirloin steak, 3 cups mixed greens, 1/2 cup cherry tomatoes, 1/4 cup red onion, 2 tbsp balsamic vinaigrette, 1 oz blue cheese — total macros?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_
- **68.** Cauliflower fried rice: 2 cups riced cauliflower, 2 large eggs, 1/2 cup frozen peas and carrots, 2 tbsp soy sauce, 1 tbsp sesame oil, 2 oz chicken breast — calories and fat?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_
- **69.** Strawberry banana smoothie: 1 cup frozen strawberries, 1 medium banana, 3/4 cup Greek yogurt, 1/2 cup orange juice, 1 tbsp honey — total calories and vitamin C?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`_
- **70.** Chili (serves 8): 1 lb ground turkey, 2 cups kidney beans, 1 can diced tomatoes (14.5 oz), 1 medium onion, 1 medium green bell pepper, 2 tbsp chili powder, 1 cup beef broth — protein and sodium per serving?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **71.** **[TEST]** Egg salad: 4 large hard-boiled eggs, 3 tbsp mayo, 1 tbsp yellow mustard, 2 stalks celery — fat and calories?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_
- **72.** **[TEST]** Caprese salad: 2 medium tomatoes, 4 oz fresh mozzarella, 1 tbsp fresh basil, 2 tbsp olive oil, 1 tsp balsamic vinegar — total fat and calcium?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`_
- **73.** Granola bars (makes 10): 2 cups oats, 1/3 cup honey, 1/4 cup almond butter, 1/4 cup mini chocolate chips, 1/4 cup dried cranberries, 2 tbsp coconut oil — calories and sugar per bar?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **74.** Beef and broccoli stir-fry: 6 oz flank steak, 2 cups broccoli, 2 tbsp oyster sauce, 1 tbsp soy sauce, 1 tbsp cornstarch, 1 tsp sesame oil — protein and sodium?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `batch_fetch_efficient`_
- **75.** Vegetable frittata (serves 4): 6 eggs, 1/2 cup diced zucchini, 1/2 cup cherry tomatoes, 1/4 cup goat cheese, 1/4 cup baby spinach, 1 tbsp olive oil — calories and fat per serving?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **76.** **[TEST]** Loaded baked potato soup (serves 4): 3 large russet potatoes, 4 strips bacon, 1 cup shredded cheddar, 1/2 cup sour cream, 3 cups chicken broth, 2 green onions — sodium and fat per bowl?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **77.** Poke bowl: 1 cup cooked sushi rice, 4 oz raw ahi tuna, 1/2 avocado, 1/4 cup cucumber, 1 tbsp soy sauce, 1 tsp sesame oil, 1 tbsp sesame seeds — full macro breakdown?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_
- **78.** **[TEST]** Apple cinnamon oatmeal: 1 cup old-fashioned oats, 1 medium apple (diced), 1 tbsp butter, 1 tsp cinnamon, 1 tbsp brown sugar, 1 cup whole milk — calories and fiber?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`_
- **79.** Falafel wrap: 4 homemade falafel patties (~30g each), 1 whole wheat pita, 2 tbsp tzatziki, 1/4 cup shredded lettuce, 2 slices tomato, 1/4 cup red onion — total macros?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `batch_fetch_efficient`_

## EDGE (20 questions, ids 80–99)

- **80.** **[TEST]** Tabbouleh: 1 cup cooked bulgur wheat, 2 tbsp sumac (the spice), 1/4 cup fresh parsley, 2 tbsp fresh mint, 2 tbsp olive oil, 1 medium tomato, 1 tbsp lemon juice — macros? Note sumac may not have a direct FDC entry.  
  _tags: `ingredient_not_in_fdc_substitute`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **81.** 1 cup cooked rice — please clarify: is this using the cooked-rice FDC entry or the raw-rice entry scaled to cooked weight? I want the accurate calorie count.  
  _tags: `ambiguous_ingredient_disclosure`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **82.** 1 cup cooked spinach + 1/2 cup cooked lentils — iron? Use the cooked versions, not raw.  
  _tags: `ambiguous_ingredient_disclosure`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`_
- **83.** I have a recipe with 2 tbsp za'atar spice blend — what's the best FDC substitute and what are the macros for that amount?  
  _tags: `ingredient_not_in_fdc_substitute`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **84.** Whole roasted chicken (serves 6): 1 large whole chicken (~3.5 lbs), 2 tbsp olive oil, 1 tbsp rosemary, 1 tsp thyme — protein and fat per serving. The recipe uses the whole bird including skin.  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `per_serving_output`_
- **85.** Fermented black garlic (2 tbsp) + 1 cup white rice — is black garlic in FDC? If not, substitute regular garlic and disclose. Total macros?  
  _tags: `ingredient_not_in_fdc_substitute`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `ambiguous_ingredient_disclosure`_
- **86.** Miso soup: 1 tbsp white miso paste, 2 cups dashi stock, 1/4 cup tofu (soft), 1 tbsp wakame seaweed — sodium. Note: dashi stock may need a substitute if not in FDC.  
  _tags: `ingredient_not_in_fdc_substitute`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`_
- **87.** Smoothie made with 1 cup raw kale vs 1 cup cooked kale — explain which FDC entry you use for each version and what the calorie difference is.  
  _tags: `ambiguous_ingredient_disclosure`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **88.** Bread recipe (makes 12 slices): 3 cups bread flour, 1 tbsp active dry yeast, 1 tsp salt, 1 tbsp olive oil, 1 cup warm water — note that baking reduces water weight; what are the macros per slice?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **89.** 1 large head of romaine lettuce (whole head used) — how do you convert 'one head' to grams? Give me total calories, fiber, and iron.  
  _tags: `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`_
- **90.** Harissa paste (2 tbsp) + 1 cup cooked couscous — harissa is a blend not in FDC. What ingredient do you substitute and what are the macros?  
  _tags: `ingredient_not_in_fdc_substitute`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **91.** My recipe calls for 'a handful of pine nuts' (roughly 1 oz) — resolve the vague unit, find the FDC entry, and report fat and calories.  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **92.** Bone broth (homemade, 2 cups) — this isn't a single FDC ingredient. What's the best substitute (beef broth? chicken broth?) and what's the sodium estimate?  
  _tags: `ingredient_not_in_fdc_substitute`, `portion_conversion_cup_to_grams`, `micro_sum_across_ingredients`, `ambiguous_ingredient_disclosure`_
- **93.** Coconut cream (1/4 cup) vs coconut milk (1/4 cup) — these are different products. I used coconut cream. Make sure to pick the right FDC entry and give me fat and calories.  
  _tags: `ambiguous_ingredient_disclosure`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **94.** **[TEST]** Trail mix recipe (makes 10 servings): 2 cups mixed nuts, 1 cup dried cranberries, 1 cup dark chocolate chips, 1/2 cup pumpkin seeds, 1/4 cup coconut flakes — calories and fat per serving?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **95.** **[TEST]** Protein pancakes (makes 8 small pancakes): 1 cup oat flour, 1 scoop vanilla protein powder (35g), 2 eggs, 1/2 cup cottage cheese, 1 tsp baking powder — protein and calories per pancake?  
  _tags: `ingredient_resolution_sr_legacy`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **96.** **[TEST]** My recipe uses 'amaranth leaves' (2 cups raw) — this is a less common leafy green. What FDC entry do you use or substitute, and what is the iron content?  
  _tags: `ingredient_not_in_fdc_substitute`, `ingredient_resolution_sr_legacy`, `micro_sum_across_ingredients`, `ambiguous_ingredient_disclosure`_
- **97.** Loaded nachos (serves 6): 8 oz tortilla chips, 1.5 cups shredded cheddar, 1 cup black beans, 1/2 cup sour cream, 1/4 cup pickled jalapeños, 1/4 cup salsa — give me calories, fat, and sodium per serving. Note: pickled jalapeños may differ from fresh jalapeños in FDC.  
  _tags: `ambiguous_ingredient_disclosure`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
- **98.** Tahini dressing: 3 tbsp tahini, 1 tbsp lemon juice, 1 tbsp water, 1/2 tsp garlic powder — FDC lists sesame seeds and sesame butter; which entry should be used for tahini? Report fat and calories for the full dressing.  
  _tags: `ingredient_not_in_fdc_substitute`, `ambiguous_ingredient_disclosure`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`_
- **99.** Korean bibimbap (serves 2): 1.5 cups cooked short-grain rice, 2 large eggs, 2 cups bean sprouts, 1 cup spinach (cooked), 2 oz ground beef, 2 tbsp gochujang sauce, 1 tsp sesame oil — macros and iron per serving. Note: gochujang may not be in FDC; choose best substitute and disclose.  
  _tags: `ingredient_not_in_fdc_substitute`, `ambiguous_ingredient_disclosure`, `portion_conversion_cup_to_grams`, `macro_sum_across_ingredients`, `micro_sum_across_ingredients`, `per_serving_output`, `batch_fetch_efficient`_
