# usda-fdc-ingredient-compliance — 100-question corpus

## Splits
- train_ids (80): `[0, 1, 4, 5, 6, 7, 8, 9, 11, 13, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 35, 36, 37, 38, 39, 40, 42, 43, 44, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 59, 60, 61, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 97, 99]`
- test_ids (20): `[2, 3, 10, 12, 14, 19, 30, 34, 41, 45, 47, 58, 62, 66, 75, 77, 81, 95, 96, 98]`
- seed: `1487939197`  mode: `hackathon`  threshold: `1.0`

## Ability-tag coverage

| Tag | Count |
|---|---|
| `allergen_top9_scan` | 59 |
| `vegan_hard_blocker_scan` | 41 |
| `vegetarian_scan` | 19 |
| `hidden_sub_ingredient_parens` | 10 |
| `product_not_in_fdc` | 10 |
| `not_branded_disclosure` | 10 |

## EASY (40 questions, ids 0–39)

- ** 0.** Is Skippy Creamy Peanut Butter vegan?  
  _tags: `vegan_hard_blocker_scan`_
- ** 1.** Does Oreo Original Sandwich Cookies contain dairy?  
  _tags: `allergen_top9_scan`_
- ** 2.** **[TEST]** Is Quaker Old Fashioned Oats gluten-free?  
  _tags: `allergen_top9_scan`_
- ** 3.** **[TEST]** Can a vegan eat Annie's Homegrown Cheddar Bunnies?  
  _tags: `vegan_hard_blocker_scan`_
- ** 4.** Is Chobani Plain Nonfat Greek Yogurt vegetarian?  
  _tags: `vegetarian_scan`_
- ** 5.** Does Kind Dark Chocolate Nuts & Sea Salt bar have peanuts in it?  
  _tags: `allergen_top9_scan`_
- ** 6.** Is Impossible Burger vegan?  
  _tags: `vegan_hard_blocker_scan`_
- ** 7.** Does Beyond Burger contain soy?  
  _tags: `allergen_top9_scan`_
- ** 8.** Is Gardein Classic Meatless Meatballs vegetarian?  
  _tags: `vegetarian_scan`_
- ** 9.** Can someone with an egg allergy eat RXBar Chocolate Sea Salt?  
  _tags: `allergen_top9_scan`_
- **10.** **[TEST]** Is CLIF Bar Chocolate Chip Energy Bar vegan?  
  _tags: `vegan_hard_blocker_scan`_
- **11.** Does Snickers Original contain peanuts?  
  _tags: `allergen_top9_scan`_
- **12.** **[TEST]** Is Reese's Peanut Butter Cups safe for someone with a milk allergy?  
  _tags: `allergen_top9_scan`_
- **13.** Can a vegan eat Whole Foods 365 Organic Animal Crackers?  
  _tags: `vegan_hard_blocker_scan`_
- **14.** **[TEST]** Does Trader Joe's Speculoos Cookie Butter contain wheat?  
  _tags: `allergen_top9_scan`_
- **15.** Is Perfect Bar Dark Chocolate Chip Peanut Butter vegan?  
  _tags: `vegan_hard_blocker_scan`_
- **16.** Does Kirkland Signature Mixed Nuts contain tree nuts?  
  _tags: `allergen_top9_scan`_
- **17.** Is Silk Original Soymilk vegan?  
  _tags: `vegan_hard_blocker_scan`_
- **18.** Does Daiya Cheddar Style Shreds contain dairy?  
  _tags: `allergen_top9_scan`, `vegan_hard_blocker_scan`_
- **19.** **[TEST]** Is Tofutti Sour Supreme dairy-free?  
  _tags: `allergen_top9_scan`_
- **20.** Can a vegetarian eat Jell-O Original Strawberry Gelatin?  
  _tags: `vegetarian_scan`_
- **21.** Does Nature Valley Oats 'N Honey Crunchy Granola Bar contain honey?  
  _tags: `vegan_hard_blocker_scan`_
- **22.** Is Lay's Classic Potato Chips vegan?  
  _tags: `vegan_hard_blocker_scan`_
- **23.** Does Pepperidge Farm Goldfish Cheddar crackers contain milk?  
  _tags: `allergen_top9_scan`_
- **24.** Is Bob's Red Mill Gluten Free Rolled Oats safe for a wheat allergy?  
  _tags: `allergen_top9_scan`_
- **25.** Can a vegan eat Starburst Original Fruit Chews?  
  _tags: `vegan_hard_blocker_scan`_
- **26.** Does Kraft Original Macaroni & Cheese contain dairy?  
  _tags: `allergen_top9_scan`_
- **27.** Is Amy's Kitchen Roasted Vegetable Pizza vegetarian?  
  _tags: `vegetarian_scan`_
- **28.** Does Lärabar Apple Pie contain gluten?  
  _tags: `allergen_top9_scan`_
- **29.** Is Talenti Gelato Alphonso Mango vegan?  
  _tags: `vegan_hard_blocker_scan`_
- **30.** **[TEST]** Does Triscuit Original Whole Grain Crackers contain wheat?  
  _tags: `allergen_top9_scan`_
- **31.** Can someone with a sesame allergy eat Sabra Classic Hummus?  
  _tags: `allergen_top9_scan`_
- **32.** Is Lightlife Smart Dogs vegetarian?  
  _tags: `vegetarian_scan`_
- **33.** Does Rao's Marinara Sauce contain dairy?  
  _tags: `allergen_top9_scan`_
- **34.** **[TEST]** Is So Delicious Coconut Milk Vanilla Bean ice cream vegan?  
  _tags: `vegan_hard_blocker_scan`_
- **35.** Does Kellogg's Frosted Flakes contain gluten?  
  _tags: `allergen_top9_scan`_
- **36.** Can a vegan eat Nabisco Ritz Original Crackers?  
  _tags: `vegan_hard_blocker_scan`_
- **37.** Is Cascadian Farm Organic Honey Almond Granola vegan?  
  _tags: `vegan_hard_blocker_scan`_
- **38.** Does Justin's Classic Almond Butter contain peanuts?  
  _tags: `allergen_top9_scan`_
- **39.** Is Kite Hill Plain Almond Milk Yogurt vegetarian?  
  _tags: `vegetarian_scan`_

## MODERATE (40 questions, ids 40–79)

- **40.** I'm vegan and have a soy allergy — can I eat Lightlife Smart Dogs veggie sausage?  
  _tags: `vegan_hard_blocker_scan`, `allergen_top9_scan`_
- **41.** **[TEST]** I follow a vegetarian diet and I'm allergic to tree nuts. Is Kind Maple Glazed Pecan & Sea Salt bar safe for me?  
  _tags: `vegetarian_scan`, `allergen_top9_scan`_
- **42.** Can a vegan with a peanut allergy eat Trader Joe's Peanut Butter Cups? I want to make sure there's no milk buried in the chocolate shell ingredients.  
  _tags: `vegan_hard_blocker_scan`, `allergen_top9_scan`, `hidden_sub_ingredient_parens`_
- **43.** I need to avoid both gluten and dairy. Is Amy's Kitchen Gluten Free Mac & Cheese safe for me?  
  _tags: `allergen_top9_scan`_
- **44.** I keep a vegan diet but I'm also allergic to sesame seeds. Is Trader Joe's Tahini safe to eat?  
  _tags: `vegan_hard_blocker_scan`, `allergen_top9_scan`_
- **45.** **[TEST]** My child has both a milk allergy and an egg allergy. Can they eat Enjoy Life Soft Baked Snickerdoodle Cookies?  
  _tags: `allergen_top9_scan`_
- **46.** Is CLIF Kid ZBar Chocolate Brownie safe for a child who has both a peanut allergy and a tree nut allergy?  
  _tags: `allergen_top9_scan`_
- **47.** **[TEST]** I'm vegan and also have a wheat allergy. Can I eat Banza Chickpea Pasta?  
  _tags: `vegan_hard_blocker_scan`, `allergen_top9_scan`_
- **48.** Does Gardein Beefless Ground contain gelatin or any other animal-derived ingredient?  
  _tags: `vegan_hard_blocker_scan`_
- **49.** Can a vegan eat Kellogg's Pop-Tarts Strawberry Frosted? I heard there might be gelatin in them.  
  _tags: `vegan_hard_blocker_scan`, `vegetarian_scan`_
- **50.** I'm lactose intolerant and vegan. Is Silk Oat Yeah Plain Oatmilk safe for me?  
  _tags: `vegan_hard_blocker_scan`, `allergen_top9_scan`_
- **51.** I keep kosher pareve and have a fish allergy. Is Annie's Organic BBQ Sauce compliant on both counts?  
  _tags: `allergen_top9_scan`, `vegetarian_scan`_
- **52.** My daughter is vegetarian and allergic to eggs. Can she eat Pillsbury Grands! Flaky Biscuits?  
  _tags: `vegetarian_scan`, `allergen_top9_scan`_
- **53.** Can someone who is vegan and allergic to shellfish eat Ocean's Halo No Shell Noodle Soup? I'm not sure if this niche product is even in your database.  
  _tags: `vegan_hard_blocker_scan`, `allergen_top9_scan`, `product_not_in_fdc`_
- **54.** I'm on a plant-based diet and I need to avoid peanuts too. Is SunButter Natural Sunflower Seed Butter a safe option?  
  _tags: `vegan_hard_blocker_scan`, `allergen_top9_scan`_
- **55.** Does Whole Foods 365 Organic Chocolate Sandwich Cookies contain dairy or eggs — I'm fully vegan?  
  _tags: `vegan_hard_blocker_scan`_
- **56.** I have celiac disease and a dairy allergy. Is Enjoy Life Semi-Sweet Chocolate Mini Chips safe for me? I want to know if any sub-ingredients contain hidden milk derivatives.  
  _tags: `allergen_top9_scan`, `hidden_sub_ingredient_parens`_
- **57.** Can a strict vegan eat Haribo Goldbären (Gold Bears) gummy bears? I heard they might use gelatin.  
  _tags: `vegan_hard_blocker_scan`, `vegetarian_scan`_
- **58.** **[TEST]** I'm vegetarian and avoid rennet in cheese. Does Sargento Natural Sharp Cheddar Slices use animal rennet?  
  _tags: `vegetarian_scan`_
- **59.** My son has a soy allergy and a wheat allergy. Can he eat RXBar Kids Banana Chocolate Chip?  
  _tags: `allergen_top9_scan`_
- **60.** Is Kirkland Signature Organic Strawberry Spread vegan — does it use any gelatin for pectin gelling? Can you find this Costco private-label product in the database?  
  _tags: `vegan_hard_blocker_scan`, `product_not_in_fdc`_
- **61.** I'm trying to avoid both soy and gluten. Can I eat Udi's Gluten Free White Sandwich Bread?  
  _tags: `allergen_top9_scan`_
- **62.** **[TEST]** Does Trader Joe's Unexpected Cheddar contain gelatin or any meat-derived ingredients — I'm vegetarian?  
  _tags: `vegetarian_scan`_
- **63.** I follow a vegan diet and have a tree nut allergy. Is Nuttzo Power Fuel Seven Nut & Seed Butter safe?  
  _tags: `vegan_hard_blocker_scan`, `allergen_top9_scan`_
- **64.** Can a vegan eat Jelly Belly Jelly Beans? I need to know if they use shellac or confectioner's glaze listed inside any coating sub-ingredient.  
  _tags: `vegan_hard_blocker_scan`, `hidden_sub_ingredient_parens`_
- **65.** I'm allergic to fish and shellfish. Is Worcestershire sauce (Lea & Perrins) safe for me?  
  _tags: `allergen_top9_scan`_
- **66.** **[TEST]** Can a vegan with a sesame allergy eat Sabra Roasted Garlic Hummus?  
  _tags: `vegan_hard_blocker_scan`, `allergen_top9_scan`_
- **67.** My partner is vegetarian and also has a peanut allergy. Is Nutella Hazelnut Spread safe for them?  
  _tags: `vegetarian_scan`, `allergen_top9_scan`_
- **68.** Does Annie's Homegrown Mac & Cheese White Cheddar contain gluten and dairy — my friend has both sensitivities?  
  _tags: `allergen_top9_scan`_
- **69.** I'm vegan and allergic to soy. Is Follow Your Heart Vegan Ranch Dressing safe for me? I wasn't able to find it easily online.  
  _tags: `vegan_hard_blocker_scan`, `allergen_top9_scan`, `product_not_in_fdc`_
- **70.** Can a vegetarian eat Campbell's Condensed Tomato Soup? I want to make sure there's no chicken or beef stock. Also, is a plain raw tomato vegetarian — just to confirm I understand the baseline?  
  _tags: `vegetarian_scan`, `not_branded_disclosure`_
- **71.** I keep a strict vegan diet. Does Red Bull Energy Drink use taurine derived from animals? I can't find this product in any database — does it even have an FDC entry?  
  _tags: `vegan_hard_blocker_scan`, `product_not_in_fdc`_
- **72.** I'm allergic to eggs and soy. Can I eat Hellmann's Real Mayonnaise?  
  _tags: `allergen_top9_scan`_
- **73.** Can a vegetarian eat Worcestershire sauce — I've heard it might contain anchovies?  
  _tags: `vegetarian_scan`, `allergen_top9_scan`_
- **74.** I have a milk allergy and a sesame allergy. Is Trader Joe's Everything But the Bagel Sesame Seasoning Blend safe for me?  
  _tags: `allergen_top9_scan`_
- **75.** **[TEST]** I'm a vegan with a soy allergy. Is Miyoko's Creamery Organic Cultured Vegan Butter safe for me? Can you even find this product in your database?  
  _tags: `vegan_hard_blocker_scan`, `allergen_top9_scan`, `product_not_in_fdc`_
- **76.** Does Quest Chocolate Chip Cookie Dough Protein Bar contain milk or eggs?  
  _tags: `allergen_top9_scan`_
- **77.** **[TEST]** I'm vegetarian and avoid isinglass. Is Guinness Draught Stout in cans vegetarian now? And is that product even in the food database?  
  _tags: `vegetarian_scan`, `vegan_hard_blocker_scan`, `product_not_in_fdc`_
- **78.** My kid is allergic to peanuts and sesame. Can they eat Sunbutter Creamy Sunflower Butter?  
  _tags: `allergen_top9_scan`_
- **79.** I eat vegan and I'm allergic to tree nuts. Is Oatly Original Oat Drink safe for me?  
  _tags: `vegan_hard_blocker_scan`, `allergen_top9_scan`_

## EDGE (20 questions, ids 80–99)

- **80.** Is a plain banana vegan?  
  _tags: `not_branded_disclosure`_
- **81.** **[TEST]** Can someone with a peanut allergy eat a raw carrot?  
  _tags: `not_branded_disclosure`_
- **82.** Is wild Atlantic salmon safe for a shellfish allergy?  
  _tags: `not_branded_disclosure`, `allergen_top9_scan`_
- **83.** Does Trader Joe's Dark Chocolate Peanut Butter Cups contain milk hidden inside the chocolate coating ingredients?  
  _tags: `hidden_sub_ingredient_parens`, `allergen_top9_scan`_
- **84.** I'm allergic to milk. Does the Ghirardelli Intense Dark Twilight Delight 72% bar have dairy buried anywhere in its sub-ingredient list?  
  _tags: `hidden_sub_ingredient_parens`, `allergen_top9_scan`_
- **85.** Is the vegan red velvet cake at my local bakery safe for my egg allergy? The product is called 'Sprinkles Red Velvet Cupcake'.  
  _tags: `product_not_in_fdc`, `allergen_top9_scan`_
- **86.** I'm vegan. Is plain white granulated sugar vegan? I heard some cane sugar is filtered through bone char.  
  _tags: `not_branded_disclosure`, `vegan_hard_blocker_scan`_
- **87.** Is the Whole Foods Market 365 Organic Gummy Bears vegan? I'm worried about gelatin or confectioner's glaze.  
  _tags: `vegan_hard_blocker_scan`, `hidden_sub_ingredient_parens`_
- **88.** Is honey a vegan food? My friend says some vegans eat it and some don't.  
  _tags: `not_branded_disclosure`, `vegan_hard_blocker_scan`_
- **89.** Is the 'Nature's Own Local Honey Wheat Bread' sold at my farmer's market listed in your food database?  
  _tags: `product_not_in_fdc`_
- **90.** My label says the chocolate drizzle on Kind Dark Chocolate Almond bar may contain milk — does the actual ingredient list confirm dairy?  
  _tags: `hidden_sub_ingredient_parens`, `allergen_top9_scan`_
- **91.** Is an organic Fuji apple from the grocery produce section vegan and allergen-free?  
  _tags: `not_branded_disclosure`_
- **92.** I have a shellfish allergy. Is glucosamine in Kirkland Signature Glucosamine & Chondroitin Sulfate tablets derived from shellfish?  
  _tags: `allergen_top9_scan`, `hidden_sub_ingredient_parens`_
- **93.** Can a vegan eat L-cysteine as an ingredient? I know it can come from feathers or human hair, and I want to understand whether it's a vegan blocker in general before I check specific products.  
  _tags: `not_branded_disclosure`, `vegan_hard_blocker_scan`_
- **94.** I'm strict vegetarian and I'm trying to find a protein bar called 'Clean Simple Eats Birthday Cake Bar' — is it in your database and does it contain gelatin?  
  _tags: `product_not_in_fdc`, `vegetarian_scan`_
- **95.** **[TEST]** Does Talenti Gelato Romano's Mango Sorbetto contain any allergens hidden inside a sub-ingredient (like milk inside a stabilizer blend)?  
  _tags: `hidden_sub_ingredient_parens`, `allergen_top9_scan`_
- **96.** **[TEST]** Is boiled lentils vegan and are they safe for someone with a peanut allergy?  
  _tags: `not_branded_disclosure`, `allergen_top9_scan`_
- **97.** Is gelatin vegan or vegetarian on its own? I'm trying to figure out if any product that lists it as an ingredient is automatically off-limits for me.  
  _tags: `not_branded_disclosure`, `vegetarian_scan`, `vegan_hard_blocker_scan`_
- **98.** **[TEST]** I found a private-label protein shake at Costco called 'Kirkland Signature Protein Bar Chocolate Brownie' — is it in the FoodData Central database and does it contain soy or eggs?  
  _tags: `product_not_in_fdc`, `allergen_top9_scan`_
- **99.** I'm a vegan with a sesame allergy. Are there any hidden sub-ingredients in Trader Joe's Joe-Joe's Chocolate Sandwich Cookies that contain sesame or any animal products?  
  _tags: `hidden_sub_ingredient_parens`, `vegan_hard_blocker_scan`, `allergen_top9_scan`_
