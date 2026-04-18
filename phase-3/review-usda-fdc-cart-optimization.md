# usda-fdc-cart-optimization — 100-question corpus

## Splits
- train_ids (80): `[0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 29, 30, 31, 33, 34, 36, 38, 39, 40, 41, 42, 43, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 71, 73, 74, 77, 78, 79, 80, 82, 83, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]`
- test_ids (20): `[8, 9, 16, 22, 28, 32, 35, 37, 44, 45, 51, 68, 70, 72, 75, 76, 81, 84, 85, 99]`
- seed: `2865742214`  mode: `hackathon`  threshold: `1.0`

## Ability-tag coverage

| Tag | Count |
|---|---|
| `meal_sodium_aggregate` | 56 |
| `offender_detection` | 56 |
| `same_category_swap_suggestion` | 38 |
| `cart_added_sugar_aggregate` | 25 |
| `meal_vs_daily_threshold` | 10 |
| `saturated_fat_meal_threshold` | 10 |
| `multi_nutrient_aggregate` | 10 |
| `confidence_when_mixed_basis` | 10 |

## EASY (40 questions, ids 0–39)

- ** 0.** Does this lunch fit my low-sodium diet? I'm having Campbell's Chicken Noodle Soup, Oscar Mayer Deli Fresh Oven Roasted Turkey, and Lay's Classic Potato Chips.  
  _tags: `meal_sodium_aggregate`_
- ** 1.** I'm making a quick dinner with Progresso Tomato Basil Soup and Pepperidge Farm Goldfish crackers. How much sodium is that combined?  
  _tags: `meal_sodium_aggregate`_
- ** 2.** My kid's snack is a Yoplait Strawberry yogurt and a Kellogg's Frosted Flakes single-serve cup. How much added sugar is that?  
  _tags: `cart_added_sugar_aggregate`_
- ** 3.** I'm grabbing Amy's Lentil Soup and a slice of Dave's Killer Bread for lunch. Does the sodium stay under 700 mg for this meal?  
  _tags: `meal_sodium_aggregate`_
- ** 4.** Pre-workout I eat a Clif Bar and a Gatorade. How much added sugar am I consuming before my workout?  
  _tags: `cart_added_sugar_aggregate`_
- ** 5.** Road trip snacks: Cheetos Crunchy and a can of Pringles Original. How much sodium is that together, and is it over 500 mg?  
  _tags: `meal_sodium_aggregate`_
- ** 6.** I'm eating a Boar's Head Low Sodium Ham sandwich on Arnold 100% Whole Wheat bread. What's the total sodium and does it fit a single-meal allowance of 700 mg?  
  _tags: `meal_sodium_aggregate`, `meal_vs_daily_threshold`_
- ** 7.** My breakfast is Quaker Instant Oatmeal Maple & Brown Sugar and a Dannon Fruit on the Bottom Strawberry yogurt. How much added sugar am I starting my day with?  
  _tags: `cart_added_sugar_aggregate`_
- ** 8.** **[TEST]** Lunch: Heinz Tomato Ketchup on a Hillshire Farm Lit'l Smokies sausage wrap. Is the saturated fat in these two items under a single-meal threshold of 5 g?  
  _tags: `saturated_fat_meal_threshold`_
- ** 9.** **[TEST]** I'm snacking on Ruffles Original chips and French's Classic Yellow Mustard on a hot dog. What's the combined sodium?  
  _tags: `meal_sodium_aggregate`_
- **10.** Kid's lunchbox: Oscar Mayer Bologna, Kraft American Cheese Singles, and Ritz Crackers. How much sodium does this lunch add up to?  
  _tags: `meal_sodium_aggregate`, `offender_detection`_
- **11.** I'm making a quick pasta dinner using Campbell's Tomato Soup as sauce and Barilla Penne. How much sodium is in this meal?  
  _tags: `meal_sodium_aggregate`_
- **12.** Afternoon snack: Nutella spread on two Pepperidge Farm Milano cookies. What's the combined added sugar?  
  _tags: `cart_added_sugar_aggregate`_
- **13.** I have a Slim Jim Original and a bag of Doritos Nacho Cheese. Is this snack over 800 mg of sodium?  
  _tags: `meal_sodium_aggregate`_
- **14.** Does my Mediterranean snack of Sabra Classic Hummus and Late July Sea Salt tortilla chips fit under 600 mg sodium?  
  _tags: `meal_sodium_aggregate`_
- **15.** I'm having Hellmann's Real Mayonnaise and Applegate Naturals Turkey Breast on a sandwich. What's the saturated fat total for these two items?  
  _tags: `saturated_fat_meal_threshold`_
- **16.** **[TEST]** Morning snack: Kind Dark Chocolate Nuts & Sea Salt bar and a Chobani Vanilla Greek yogurt. How much added sugar is this?  
  _tags: `cart_added_sugar_aggregate`_
- **17.** My quick lunch is Progresso Light Chicken Noodle Soup and a pack of Nabisco Premium Saltine Crackers. Does the sodium stay under 1,000 mg?  
  _tags: `meal_sodium_aggregate`_
- **18.** Road-trip duo: a Jack Link's Original Beef Jerky bag and a Welch's Fruit Snacks pouch. What's the combined sodium?  
  _tags: `meal_sodium_aggregate`_
- **19.** I'm eating a Stonyfield Organic Strawberry Smoothie and a Kashi GoLean cereal bar. How much added sugar is in this snack?  
  _tags: `cart_added_sugar_aggregate`_
- **20.** Does a Pacific Foods Organic Tomato Soup with a Triscuit Original crackers pairing exceed 700 mg sodium per meal?  
  _tags: `meal_sodium_aggregate`_
- **21.** Pre-gym: a Premier Protein Chocolate Shake and a Nature Valley Oats & Honey granola bar. What's the added sugar total?  
  _tags: `cart_added_sugar_aggregate`_
- **22.** **[TEST]** I'm assembling a kid's lunchbox with Lunchables Turkey & Cheddar Cracker Stackers and a Capri Sun Fruit Punch. How much sodium is that combined?  
  _tags: `meal_sodium_aggregate`_
- **23.** Simple dinner: a bowl of Amy's Organic Minestrone Soup and some Keebler Club Crackers. Does the sodium total stay under 1,000 mg?  
  _tags: `meal_sodium_aggregate`_
- **24.** I'm snacking on Siete Grain Free Tortilla Chips and Frontera Mild Salsa. What's the sodium across these two items?  
  _tags: `meal_sodium_aggregate`_
- **25.** Breakfast: Kellogg's Special K Red Berries cereal with Horizon Organic Whole Milk. How much added sugar is in this bowl?  
  _tags: `cart_added_sugar_aggregate`_
- **26.** Snack box: Babybel Original Mini Cheese and Triscuit Rosemary & Olive Oil crackers. How much saturated fat is in this combination?  
  _tags: `saturated_fat_meal_threshold`_
- **27.** I'm putting together a simple dip tray with Hidden Valley Original Ranch Dressing and Lay's Baked Potato Chips. What's the sodium combined?  
  _tags: `meal_sodium_aggregate`_
- **28.** **[TEST]** Does a Muscle Milk Pro Series Chocolate Shake plus a RXBar Chocolate Sea Salt stay under 25 g added sugar?  
  _tags: `cart_added_sugar_aggregate`_
- **29.** Snack time: Oreo Original cookies and a Yoplait Original Strawberry yogurt cup. How much added sugar do these two have combined?  
  _tags: `cart_added_sugar_aggregate`_
- **30.** I'm packing a thermos of Campbell's Tomato Soup and a bag of Pepperidge Farm Goldfish cheddar crackers. Is the sodium under 1,200 mg?  
  _tags: `meal_sodium_aggregate`_
- **31.** Quick breakfast: Jimmy Dean Original Pork Sausage and Pillsbury Grands Biscuits. How much saturated fat is in this meal?  
  _tags: `saturated_fat_meal_threshold`_
- **32.** **[TEST]** My snack is a bag of Cheetos Puffs and a can of Coca-Cola Classic. How much sodium is in the Cheetos and how much added sugar is in the Coke â€” report both totals.  
  _tags: `multi_nutrient_aggregate`_
- **33.** I'm eating Boar's Head Ovengold Roasted Turkey Breast on Arnold Whole Grain White bread. What's the combined sodium for this simple sandwich?  
  _tags: `meal_sodium_aggregate`_
- **34.** Late July Sea Salt chips plus Wholly Guacamole Classic â€” does this snack stay under 300 mg sodium?  
  _tags: `meal_sodium_aggregate`_
- **35.** **[TEST]** I'm pairing a can of Progresso Vegetable Classics Hearty Black Bean with a Thomas' Original English Muffin. What's the combined sodium?  
  _tags: `meal_sodium_aggregate`_
- **36.** Post-workout: Fairlife Core Power Elite Chocolate Protein Shake and a Larabar Apple Pie bar. How much added sugar is in this recovery snack?  
  _tags: `cart_added_sugar_aggregate`_
- **37.** **[TEST]** I'm bringing a Thermos of Pacific Foods Organic Chicken Broth and a pack of Ritz Original Crackers on a day hike. What's the sodium total?  
  _tags: `meal_sodium_aggregate`_
- **38.** Kid's dessert: Jell-O Strawberry Gelatin and a Capri Sun Fruit Punch. How much added sugar is in this after-school treat?  
  _tags: `cart_added_sugar_aggregate`_
- **39.** Midday meal: two slices of Oscar Mayer Classic Bologna and a serving of Kraft Mac & Cheese. Does the sodium fit within a 700 mg single-meal allowance?  
  _tags: `meal_sodium_aggregate`, `meal_vs_daily_threshold`_

## MODERATE (40 questions, ids 40–79)

- **40.** Here's my week's grocery cart: Campbell's Chunky Beef Stew, Progresso Clam Chowder, Hormel Chili with Beans, Oscar Mayer Center Cut Bacon, Heinz Ketchup, and Lay's Classic Chips. How much sodium am I bringing home total? Who's the worst offender and what lower-sodium swap do you recommend in the same category?  
  _tags: `meal_sodium_aggregate`, `meal_vs_daily_threshold`, `offender_detection`_
- **41.** I'm meal-prepping a week of lunches: Amy's Tomato Soup, Applegate Naturals Genoa Salami, Boar's Head American Cheese, Hellmann's Mayonnaise, Pepperidge Farm Soft White Bread, and Dave's Killer Bread 21 Whole Grains. Aggregate sodium, name the top offender, and suggest a same-category swap.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **42.** My kid's weekly lunchbox cart: Lunchables Turkey & Cheddar, Oscar Mayer Bologna, Welch's Fruit Snacks, Capri Sun Fruit Punch, Jif Creamy Peanut Butter, and Smucker's Strawberry Jam. How much added sugar is in this cart? What single item drives it most, and what should I swap?  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **43.** Pre-workout stack for the week: Gatorade Thirst Quencher Fruit Punch, Clif Bar Chocolate Chip, PowerBar Performance Energy Vanilla, Quest Protein Bar Chocolate Chip Cookie Dough, Nature Valley Sweet & Salty Almond granola bar, and Premier Protein Caramel Shake. What's my total added sugar? Flag the top offender and suggest a swap.  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **44.** **[TEST]** Road-trip snack haul: Doritos Nacho Cheese, Cheetos Crunchy, Pringles Original, Jack Link's Beef Jerky, Slim Jim Original, and Snyder's of Hanover Honey Mustard Pretzel Pieces. What's the total sodium across these six items? Who's the biggest sodium bomb, and what's a lower-sodium alternative in the same snack category?  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **45.** **[TEST]** Mediterranean meal prep cart: Sabra Classic Hummus, Athenos Traditional Feta Cheese, Kalamata Naturals Pitted Olives, Pacific Foods Organic Chicken Broth, Amy's Indian Palak Paneer, and Siete Grain Free Tortilla Chips. Aggregate sodium, rank contributors, and suggest swaps for the top two offenders.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **46.** I'm shopping for breakfasts for the week: Kellogg's Frosted Flakes, Quaker Instant Oatmeal Maple & Brown Sugar, Yoplait Original Strawberry, Dannon Fruit on the Bottom Blueberry, Pop-Tarts Frosted Strawberry, and Stonyfield Organic Whole Milk Vanilla Yogurt. How much added sugar am I stocking up on? Name the worst item and suggest a swap.  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **47.** Dinner for two â€” Mediterranean-style: Rao's Homemade Marinara Sauce, Barilla Linguine, Applegate Naturals Chicken & Apple Sausage, Progresso Italian-Style Bread Crumbs, Kraft Parmesan Cheese, and Hidden Valley Italian Dressing. What's the total sodium and which item should I swap to bring the meal under 1,400 mg combined?  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **48.** Full grocery cart for one person's week: Heinz Tomato Ketchup, French's Classic Yellow Mustard, Hellmann's Real Mayonnaise, Hidden Valley Original Ranch Dressing, Kraft Original BBQ Sauce, and Sweet Baby Ray's Original BBQ Sauce. How much sodium is in my condiment aisle alone? Flag top offender and suggest a lower-sodium substitute.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **49.** My Saturday meal plan includes Campbell's Tomato Soup, Pepperidge Farm Goldfish Cheddar Crackers, Oscar Mayer Deli Fresh Honey Ham, Kraft American Cheese Singles, Ritz Crackers, and Jell-O Chocolate Pudding Cup. Aggregate added sugar, identify the biggest contributor, and suggest a swap for it.  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **50.** Post-workout recovery meal: Jimmy Dean Turkey Sausage Breakfast Sandwich, Chobani Vanilla Greek Yogurt, Kashi GoLean Original Cereal, Horizon Organic Reduced Fat Milk, Nature Valley Protein Dark Chocolate & Peanut Butter bar, and a Stonyfield Organic Strawberry Smoothie. What's total added sugar? Name the worst offender and provide a same-category swap suggestion.  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **51.** **[TEST]** I'm preparing a holiday appetizer spread: Boar's Head Pepperoni, Hormel Pepperoni, Sargento Ultra Thin Sharp Cheddar, Kraft Mozzarella String Cheese, Pepperidge Farm Milano Cookies, and Triscuit Original Crackers. How much saturated fat is in this spread? Rank items and recommend a swap for the top offender.  
  _tags: `saturated_fat_meal_threshold`, `offender_detection`, `same_category_swap_suggestion`_
- **52.** My full week of soup lunches: Campbell's Chunky Classic Chicken Noodle, Progresso Rich & Hearty Chicken Pot Pie Style, Amy's Organic Cream of Tomato, Pacific Foods Organic Roasted Red Pepper Tomato, Campbell's Well Yes! Sipping Soup Tomato Basil, and Healthy Choice Garden Vegetable Soup. Aggregate sodium, flag the two worst soups, and suggest lower-sodium alternatives.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **53.** Grocery run for deli-style lunches: Boar's Head Low Sodium Turkey Breast, Applegate Naturals Roast Beef, Oscar Mayer Deli Fresh Rotisserie Chicken, Sara Lee Honey Roasted Turkey, Hillshire Farm Ultra Thin Sliced Honey Ham, and Kraft Swiss Singles Cheese. What's the total sodium? Who contributes most per serving and what's a same-category swap?  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **54.** I'm building a week's worth of kid's breakfast cereals: Kellogg's Froot Loops, Post Honey Bunches of Oats, General Mills Cinnamon Toast Crunch, Quaker Cap'n Crunch, General Mills Lucky Charms, and Kellogg's Apple Jacks. Total added sugar per serving across all six? Worst offender and swap?  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **55.** A Mediterranean mezze meal: Sabra Roasted Garlic Hummus, Late July Multigrain Sea Salt chips, Wholly Guacamole Spicy, Cedar's Foods Tzatziki, Athenos Traditional Feta Crumbles, and Pacific Foods Organic Free Range Chicken Broth. How much sodium is in this spread? Rank items and suggest a swap for the top contributor.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **56.** I'm checking my full grocery cart for saturated fat: Jimmy Dean Original Pork Sausage Roll, Hillshire Farm Smoked Sausage, Johnsonville Original Bratwurst, Tyson Regular Pork Sausage Links, Ball Park Beef Franks, and Oscar Mayer Cheese Dogs. Total saturated fat for these six products, top offender, and a same-category lower-sat-fat swap?  
  _tags: `saturated_fat_meal_threshold`, `offender_detection`, `same_category_swap_suggestion`_
- **57.** Pre-game snack table: Tostitos Original Restaurant Style Tortilla Chips, Tostitos Chunky Salsa Medium, Lay's Classic Potato Chips, Ruffles Original, French Onion Dip by Dean's, and Hidden Valley Original Ranch Dip. Aggregate sodium, identify the biggest single contributor, and suggest a lower-sodium swap for it.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **58.** My school-week snack drawer: Kellogg's Rice Krispies Treats, Welch's Fruit Snacks Mixed Fruit, General Mills Fruit Roll-Ups Strawberry, Betty Crocker Fruit by the Foot, Nature Valley Sweet & Salty Cashew bar, and Quaker Chewy Chocolate Chip Granola Bar. How much added sugar is in this snack drawer? Which item tops the chart and what should I replace it with?  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **59.** Taco night cart: Old El Paso Taco Seasoning Mix, Old El Paso Refried Beans, Pace Chunky Salsa Medium, Kraft Shredded Mexican Four Cheese Blend, Mission Flour Tortillas, and Hormel Ground Beef with Taco Seasoning. What's the total sodium? Who's the top offender and what's a lower-sodium substitute in the same category?  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **60.** Week's worth of yogurt parfait ingredients: Yoplait Original Strawberry, Dannon Light & Fit Vanilla, Chobani Strawberry On The Bottom, Stonyfield Organic Blueberry, Activia Strawberry Probiotic Yogurt, and Fage Total 0% Strawberry. Total added sugar across the six? Worst offender and a lower-sugar swap in the same category?  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **61.** I'm stocking up on condiments and sauces for pasta week: Rao's Homemade Marinara, Prego Traditional Italian Sauce, Barilla Tomato & Basil Pasta Sauce, Ragu Old World Style Traditional, Newman's Own Marinara, and Hunt's Pasta Sauce Traditional. Aggregate sodium per serving across all six, flag the top contributor, and suggest a swap.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **62.** Camping trip food haul: Hormel SPAM Classic, Mountain House Chicken & Rice (branded), Knorr Chicken Flavor Rice Sides, Campbell's Bean with Bacon Soup, Maruchan Instant Lunch Chicken Ramen, and Idahoan Buttery Homestyle Mashed Potatoes. What's the total sodium? Rank each item and provide a same-category swap for the worst.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **63.** I'm tracking added sugar for my weekly grocery run: Tropicana Orange Juice Original, Ocean Spray Cranberry Cocktail, Minute Maid Lemonade, Welch's Grape Juice Cocktail, Capri Sun Pacific Cooler, and V8 Splash Berry Blend. Total added sugar? Rank the worst offender and suggest a same-category lower-sugar swap.  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **64.** My lunch meal kit for the week: Amy's Organic Roasted Vegetable Pizza, Amy's Veggie Burger, Dr. Praeger's California Veggie Burger, Morningstar Farms Classic Burger, Hilary's World's Best Veggie Burger, and Field Roast Herb & Greens FieldRoast. Aggregate sodium, identify the highest contributor, and suggest a same-category swap.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **65.** Does my meal-prep Sunday plan for a week of dinners â€” Rao's Arrabiata Sauce, Barilla Penne Rigate, Applegate Naturals Uncured Pepperoni, Kraft Parmesan Shaker, Heinz Tomato Ketchup, Stubb's Original Bar-B-Q Sauce â€” exceed 2,300 mg sodium in aggregate? Which item is the top offender and what's a low-sodium alternative in the same category?  
  _tags: `meal_sodium_aggregate`, `meal_vs_daily_threshold`, `offender_detection`_
- **66.** I'm putting together a week of protein bars for a gym diet: Clif Bar Crunchy Peanut Butter, KIND Dark Chocolate Nuts & Sea Salt, Larabar Peanut Butter Chocolate Chip, RXBar Maple Sea Salt, RXBAR Chocolate Sea Salt, and Quest Bar Double Chocolate Chunk. What's the total added sugar across all six? Which bar has the most and is there a similar bar with less sugar?  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **67.** Is my Saturday morning brunch cart â€” Jimmy Dean Fully Cooked Turkey Sausage Crumbles, Hillshire Farm Smoked Sausage, Pillsbury Grands Flaky Layers Biscuits, Kraft American Cheese Singles, Heinz Tomato Ketchup, and Tropicana Orange Juice â€” over 2,300 mg sodium in total? Flag the biggest contributor and suggest a swap.  
  _tags: `meal_sodium_aggregate`, `meal_vs_daily_threshold`, `offender_detection`_
- **68.** **[TEST]** I have a full pasta dinner cart: Prego Three Cheese Marinara Sauce, Barilla Spaghetti, Kraft Shredded Italian Five Cheese, Hillshire Farm Italian Style Smoked Sausage, Progresso Italian Style Bread Crumbs, and Newman's Own Caesar Dressing for the salad. How much saturated fat is in this dinner total? Name the top contributor and suggest a lower-saturated-fat alternative in the same category.  
  _tags: `saturated_fat_meal_threshold`, `offender_detection`, `same_category_swap_suggestion`_
- **69.** Track both sodium AND added sugar in my road-trip cart: Lay's Classic Chips, Doritos Nacho Cheese, Welch's Fruit Snacks, Gatorade Cool Blue, Snyder's of Hanover Sourdough Nuggets, and a Starbucks Frappuccino Mocha bottled drink. Aggregate both nutrients, flag the worst offender for each, and suggest a same-category swap for each offender.  
  _tags: `multi_nutrient_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **70.** **[TEST]** My kid's birthday party snack cart: Capri Sun Fruit Punch, Kool-Aid Jammers Cherry, Welch's Mixed Fruit Fruit Snacks, General Mills Fruit Roll-Ups, Jell-O Strawberry Gelatin, and Hershey's Chocolate Syrup. Total added sugar? Worst single offender and a lower-sugar swap in the same food category?  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **71.** My weekly grocery cart includes Progresso Minestrone Soup, Amy's Organic Lentil Vegetable Soup, Pacific Foods Organic French Onion Soup, Campbell's Homestyle Chicken Noodle Soup, Healthy Choice Garden Minestrone, and Campbell's Condensed Chicken with Rice. Aggregate sodium, rank all six soups, call out the top two offenders, and suggest lower-sodium swaps for each.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **72.** **[TEST]** Does my Mediterranean dinner â€” Sabra Classic Hummus, Athenos Feta Crumbles, Kalamata Naturals Pitted Olives, Cedar's Foods Baba Ghanoush, Amy's Greek Spanakopita, and Stacy's Simply Naked Pita Chips â€” push past a single-meal sodium allowance of 700 mg? Who's the worst offender and what should I swap?  
  _tags: `meal_sodium_aggregate`, `meal_vs_daily_threshold`, `offender_detection`_
- **73.** Weekly grocery cart, checking for added sugar: Tropicana Fruit Punch, Smucker's Strawberry Preserves, Jif Creamy Peanut Butter, Kraft Original BBQ Sauce, Sweet Baby Ray's Original BBQ Sauce, and Hidden Valley Original Ranch Dressing. Total added sugar? Top offender and a same-category lower-sugar swap?  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **74.** I'm tracking sodium and saturated fat together for my week of breakfasts: Jimmy Dean Original Pork Sausage, Oscar Mayer Center Cut Bacon, Hillshire Farm Smoked Sausage, Pillsbury Grands Biscuits, Kraft American Cheese Singles, and Thomas' Original English Muffins. Report totals for both nutrients, and flag the worst offender for each with a suggested swap.  
  _tags: `multi_nutrient_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **75.** **[TEST]** Quick build-your-own taco cart for dinner: Old El Paso Taco Shells, Pace Mild Chunky Salsa, Kraft Mexican Four Cheese, Old El Paso Refried Beans, Lawry's Taco Seasoning, and Hormel Canned Chicken. Does this meal stay under 2,000 mg combined sodium, and what item drives it most? Suggest a swap for the worst offender.  
  _tags: `meal_sodium_aggregate`, `meal_vs_daily_threshold`, `offender_detection`_
- **76.** **[TEST]** I'm checking the saturated fat in my weekly charcuterie board haul: Boar's Head Pepperoni, Applegate Naturals Genoa Salami, Sargento Ultra Thin Sharp Cheddar, Brie Le Chatelain Brie Cheese, Hormel Pepperoni, and Kraft Pepper Jack Slices. Total saturated fat? Rank all six and suggest a same-category swap for the top offender.  
  _tags: `saturated_fat_meal_threshold`, `offender_detection`, `same_category_swap_suggestion`_
- **77.** Does this full lunch meal kit â€” Progresso Lentil Soup, Oscar Mayer Deli Fresh Oven Roasted Turkey, Sara Lee Honey Wheat Bread, Hellmann's Light Mayonnaise, Kraft Swiss Singles, and a dill pickle by Vlasic â€” exceed the daily sodium limit of 2,300 mg when totaled? Who's the worst offender and what lower-sodium swap exists in that product category?  
  _tags: `meal_sodium_aggregate`, `meal_vs_daily_threshold`, `offender_detection`_
- **78.** Check both sodium and added sugar for this summer BBQ cart: Kraft Original BBQ Sauce, Sweet Baby Ray's Honey BBQ Sauce, Heinz 57 Steak Sauce, French's Classic Yellow Mustard, Hellmann's Real Mayonnaise, and Hunt's Ketchup. Aggregate both nutrients per cart, flag the top offender for each, and recommend same-category swaps.  
  _tags: `multi_nutrient_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **79.** My full week of packaged snacks for the office: Lay's Classic, Cheetos Flamin' Hot Crunchy, Ruffles Cheddar & Sour Cream, Doritos Cool Ranch, Late July Sea Salt chips, and Siete Fuego chips. What's the total sodium across all six bags per serving? Call out the worst offender and suggest a same-category lower-sodium alternative.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_

## EDGE (20 questions, ids 80–99)

- **80.** My cart has a mix of branded and non-branded items: Campbell's Tomato Soup (branded), fresh Roma tomatoes (Foundation/SR Legacy), Progresso Chicken Broth (branded), and fresh celery (Foundation). Aggregate sodium for everything you can; disclose any items where the basis differs from labelNutrients. Who is the worst branded offender for sodium?  
  _tags: `confidence_when_mixed_basis`, `meal_sodium_aggregate`, `offender_detection`_
- **81.** **[TEST]** I'm doing a bulk grocery haul â€” 22 items total: Campbell's Chunky Beef Stew, Progresso Chicken Noodle, Amy's Lentil Soup, Pacific Foods Roasted Red Pepper Tomato, Healthy Choice Minestrone, Hormel Chili with Beans, SPAM Classic, Boar's Head Honey Ham, Oscar Mayer Bologna, Hillshire Farm Smoked Sausage, Lay's Classic, Doritos Nacho Cheese, Cheetos Crunchy, Ruffles Original, Pringles Original, Heinz Ketchup, French's Mustard, Hellmann's Mayo, Hidden Valley Ranch, Sweet Baby Ray's BBQ Sauce, Smucker's Strawberry Jam, and Kraft Mac & Cheese. Aggregate sodium across all 22 items. Note: you may need to batch into two API calls to stay under the 20-item cap.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `confidence_when_mixed_basis`_
- **82.** My cart is all under the daily sodium limit individually. Cart: Applegate Naturals Roast Turkey (low sodium), Amy's Light in Sodium Lentil Soup, Pacific Foods Organic Low Sodium Chicken Broth, Late July Sea Salt chips, and Dave's Killer Bread 21 Whole Grains. Does the aggregated sodium still stay under 700 mg per meal when you add them all together? Also, does the combined saturated fat stay under a single-meal allowance of 5 g? Are there any offenders at all for either nutrient?  
  _tags: `saturated_fat_meal_threshold`, `multi_nutrient_aggregate`, `offender_detection`_
- **83.** Cart: Progresso Chunky New England Clam Chowder (branded), fresh Yukon Gold potatoes (Foundation), Horizon Organic Heavy Whipping Cream (branded), and fresh clams (Foundation). I know fresh items won't have labelNutrients â€” report on the branded items' sodium with full confidence disclosure, and note what can't be estimated from the API.  
  _tags: `confidence_when_mixed_basis`, `meal_sodium_aggregate`_
- **84.** **[TEST]** I have 21 items in my cart but only have 20 FDC IDs ready. How should the skill handle chunking the POST /foods batch call? Please aggregate both sodium and saturated fat across the cart: Campbell's six soup varieties (Tomato, Chicken Noodle, Cream of Mushroom, Tomato Bisque, Clam Chowder, Minestrone), four Progresso soups, three Amy's soups, four Hormel Chili varieties, and two Healthy Choice soups. Flag the top offender for each nutrient.  
  _tags: `meal_sodium_aggregate`, `multi_nutrient_aggregate`, `offender_detection`_
- **85.** **[TEST]** My cart is: Boar's Head Pepperoni (branded, has labelNutrients), fresh mozzarella ball from a deli (no FDC branded entry, likely Foundation), Rao's Homemade Marinara (branded), and fresh basil leaves (Foundation). Some items will lack labelNutrients. Report sodium for everything with confidence flags where you fall back to per-100g estimates.  
  _tags: `confidence_when_mixed_basis`, `meal_sodium_aggregate`_
- **86.** None of the five items in my pre-workout cart exceed 5 g added sugar individually: RXBar Blueberry, Larabar Apple Pie, Kind Almond & Coconut bar, 365 Whole Foods Organic Granola Bar Oat & Honey, and Bare Baked Crunchy Apple Chips. Even with all five under the limit, does the aggregate reach 25 g? Confirm whether there are any offenders or if the cart is fully compliant.  
  _tags: `cart_added_sugar_aggregate`, `offender_detection`_
- **87.** My cart mixes branded and Foundation data: Amy's Organic Tomato Soup (branded), fresh Roma tomatoes (Foundation), Horizon Organic Whole Milk (branded), wild-caught canned sardines in water by a very small brand (possibly missing labelNutrients), and Progresso Italian Herb Bread Crumbs (branded). Aggregate sodium and added sugar simultaneously, disclosing confidence level per item.  
  _tags: `confidence_when_mixed_basis`, `multi_nutrient_aggregate`_
- **88.** I have a 20-item exact-cap grocery cart â€” all soups: Campbell's Tomato, Campbell's Chicken Noodle, Campbell's Cream of Mushroom, Campbell's Bean with Bacon, Campbell's French Onion, Progresso Minestrone, Progresso Clam Chowder, Progresso Lentil, Progresso Chicken Noodle, Amy's Organic Lentil, Amy's Organic Tomato Basil, Amy's Organic Minestrone, Pacific Foods Organic Tomato, Pacific Foods Organic Chicken, Pacific Foods Organic French Onion, Healthy Choice Chicken Noodle, Healthy Choice Minestrone, Hormel Home Style Chicken Noodle, Wolfgang Puck Organic Tortilla, and Imagine Organic Creamy Tomato. Aggregate sodium across all 20 in one batch call. Rank the top three and suggest swaps.  
  _tags: `meal_sodium_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **89.** All six items in my grocery cart are well within the daily saturated fat limit individually. Cart: Applegate Naturals Turkey Breast, Boar's Head Low Sodium Chicken Breast, Amy's Organic Lentil Soup, Dave's Killer Bread Powerseed, Pacific Foods Low Sodium Chicken Broth, and Stonyfield Organic Plain Greek Yogurt. Aggregate saturated fat â€” does the total stay under 13 g for the day? Confirm no offenders.  
  _tags: `saturated_fat_meal_threshold`, `offender_detection`_
- **90.** The top sodium offender in my cart is a very niche branded product â€” Trader Joe's Miso Ginger Broth â€” which has no obvious direct competitor in the branded search results for 'low sodium miso broth'. How should the skill handle a swap search that returns no viable lower-sodium alternatives? What fallback should it communicate?  
  _tags: `same_category_swap_suggestion`, `offender_detection`_
- **91.** My cart is a mix of branded and Foundation items: Oscar Mayer Deli Fresh Turkey (branded), raw spinach (Foundation), Kraft Parmesan Shaker (branded), fresh garlic (Foundation), and canned chickpeas by a generic store brand that may lack labelNutrients. Check sodium across the cart, disclose which estimates are derived from per-100g rather than labelNutrients, and name the worst branded offender.  
  _tags: `confidence_when_mixed_basis`, `meal_sodium_aggregate`, `offender_detection`_
- **92.** I'm asking about two nutrients simultaneously. Cart (8 items): Hormel Chili with Beans, Oscar Mayer Beef Bologna, Lay's Classic Chips, Heinz Ketchup, Wonder Classic White Bread, Kraft American Singles, Welch's Grape Juice Cocktail, and Dannon Strawberry Yogurt. Aggregate both sodium AND added sugar. For each nutrient identify the top offender and suggest a same-category swap.  
  _tags: `multi_nutrient_aggregate`, `offender_detection`, `same_category_swap_suggestion`_
- **93.** I want to know if this meal exceeds BOTH the single-meal sodium allowance (700 mg) AND the daily sodium ceiling (2,300 mg). Cart: Campbell's Tomato Soup, Oscar Mayer Bologna, Lay's Classic Chips, Heinz Ketchup, and Wonder Classic White Bread. Does the meal exceed the single-meal threshold? Does it exceed the daily limit? Explain the difference in how these thresholds are applied.  
  _tags: `meal_vs_daily_threshold`, `meal_sodium_aggregate`_
- **94.** Cart: Progresso Tomato Basil Soup (branded â€” labelNutrients available), fresh basil (Foundation â€” no labelNutrients), La Croix Sparkling Water (branded â€” no significant nutrients), and a generic store-brand crouton package where labelNutrients may be absent. Aggregate sodium: which items can you report with high confidence versus estimated confidence, and does the mix affect your ability to detect offenders?  
  _tags: `confidence_when_mixed_basis`, `meal_sodium_aggregate`, `offender_detection`_
- **95.** I want a full multi-nutrient report for my 8-item kid's lunchbox cart: Lunchables Turkey & Cheddar, Capri Sun Fruit Punch, Kellogg's Rice Krispies Treat, Welch's Fruit Snacks, Oscar Mayer Bologna, Kraft American Singles, Ritz Crackers, and a small Dannon Strawberry yogurt. Report sodium AND added sugar totals, rank top offenders for each, and suggest swaps. Disclose any items where labelNutrients was unavailable.  
  _tags: `multi_nutrient_aggregate`, `offender_detection`, `confidence_when_mixed_basis`_
- **96.** The worst offender in my cart is a very specialty item: Cento San Marzano Whole Peeled Tomatoes â€” there are no branded search results for 'low sodium canned whole peeled tomatoes San Marzano style' with a lower sodium value. The swap search returns items in different sub-categories. How should the skill behave when no same-category swap is found, and what alternative guidance can it offer?  
  _tags: `same_category_swap_suggestion`, `offender_detection`_
- **97.** My grocery cart has 25 items requiring two batch calls (chunk at 20). Part 1: Campbell's Tomato Soup, Progresso Minestrone, Amy's Lentil, Pacific Foods Tomato, Healthy Choice Chicken Noodle, Hormel Chili, SPAM Classic, Oscar Mayer Bologna, Boar's Head Turkey, Hillshire Farm Sausage, Lay's Classic, Doritos Nacho Cheese, Cheetos Crunchy, Ruffles Original, Pringles Original, Heinz Ketchup, French's Mustard, Hellmann's Mayo, Hidden Valley Ranch, Sweet Baby Ray's BBQ. Part 2: Kraft Mac & Cheese, Smucker's Strawberry Jam, Welch's Grape Juice, Pop-Tarts Frosted Strawberry, Capri Sun Fruit Punch. Aggregate both sodium AND added sugar across all 25 items (note the chunking required), flag the top 3 offenders for sodium and the top offender for added sugar, and suggest swaps.  
  _tags: `meal_sodium_aggregate`, `multi_nutrient_aggregate`, `confidence_when_mixed_basis`_
- **98.** Some items in my cart have labelNutrients, others only have foodNutrients (per 100 g). Cart: Progresso Clam Chowder (labeled), a generic off-brand canned tuna where only per-100g data is available, Amy's Tomato Soup (labeled), a store-brand whole grain cracker (per-100g only), and Horizon Organic Whole Milk (labeled). Aggregate sodium, clearly flag which items used per-100g estimation and what confidence level that carries, and state whether offender detection is reliable given the mixed basis.  
  _tags: `confidence_when_mixed_basis`, `meal_sodium_aggregate`, `offender_detection`_
- **99.** **[TEST]** My cart is entirely low-sodium branded products: Boar's Head Low Sodium Turkey Breast, Amy's Light in Sodium Tomato Soup, Pacific Foods Low Sodium Chicken Broth, Applegate Naturals Organic Chicken Breast, and Campbell's Healthy Request Chicken Noodle Soup. All items individually are under 200 mg sodium per serving. Does the aggregate total stay under both the single-meal ceiling (700 mg) and the daily limit (2,300 mg)? Confirm whether any offenders exist â€” and if none do, how should the skill communicate a fully compliant cart?  
  _tags: `meal_sodium_aggregate`, `meal_vs_daily_threshold`, `offender_detection`_
