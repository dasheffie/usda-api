# usda-fdc-low-sugar-snack — 100-question corpus

## Splits
- train_ids (80): `[0, 2, 3, 4, 5, 6, 7, 8, 11, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 25, 26, 27, 28, 29, 31, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 50, 52, 53, 54, 55, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 78, 79, 80, 82, 83, 84, 85, 86, 87, 89, 91, 92, 93, 95, 96, 97, 98, 99]`
- test_ids (20): `[1, 9, 10, 12, 20, 24, 30, 32, 40, 48, 49, 51, 56, 60, 76, 77, 81, 88, 90, 94]`
- seed: `2696116852`  mode: `hackathon`  threshold: `1.0`

## Ability-tag coverage

| Tag | Count |
|---|---|
| `current_favorite_comparison` | 70 |
| `category_keyword_search` | 53 |
| `branded_only_constraint` | 37 |
| `added_sugar_vs_total_sugar_disambiguation` | 26 |
| `kid_friendly_or_household_swap` | 16 |
| `ranked_low_sugar_alternatives` | 13 |
| `sugar_alcohol_disclosure` | 10 |

## EASY (40 questions, ids 0–39)

- ** 0.** Chips Ahoy! has too much sugar — what's a lower-sugar cookie I can buy?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- ** 1.** **[TEST]** I love Oreo cookies but I'm trying to cut back on sugar. Can you find me a lower-sugar packaged cookie alternative?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- ** 2.** What's a store-bought granola bar with less sugar than a Nature Valley Crunchy bar?  
  _tags: `current_favorite_comparison`, `branded_only_constraint`_
- ** 3.** I eat Yoplait strawberry yogurt every morning. Is there a lower-sugar yogurt I could switch to?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- ** 4.** Ben & Jerry's Cherry Garcia has way too much sugar. What's a lower-sugar ice cream I can buy at the store?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- ** 5.** I'm trying to swap my Kellogg's Raisin Bran for something with less sugar. What branded cereal should I try?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- ** 6.** Snickers bars have a lot of sugar. What's a lower-sugar candy bar I can find in stores?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- ** 7.** I snack on Pepperidge Farm Milano cookies daily. Can you find a lower-sugar packaged cookie?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- ** 8.** What branded protein bar has less sugar than a Clif Bar?  
  _tags: `category_keyword_search`, `current_favorite_comparison`, `branded_only_constraint`_
- ** 9.** **[TEST]** I enjoy Reese's Peanut Butter Cups but want something with less sugar. What candy should I try?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **10.** **[TEST]** Chobani vanilla yogurt is my go-to snack. Are there lower-sugar yogurt options I can buy?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **11.** Keebler Fudge Stripes cookies taste great but I know they're high in sugar. What's a lower-sugar cookie I can buy?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **12.** **[TEST]** I eat Hershey's milk chocolate bars as a treat. What branded chocolate with less sugar can I substitute?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **13.** My morning cereal is Special K with berries — can you find a lower-sugar branded cereal for me?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **14.** I grab a Twix bar most afternoons. What's a packaged candy bar with less sugar I could swap it for?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **15.** Nutter Butter cookies are my weakness. What's a lower-sugar peanut butter cookie I can buy?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **16.** I snack on Oikos Triple Zero yogurt — is there anything with even less sugar that's sold in stores?  
  _tags: `category_keyword_search`, `current_favorite_comparison`, `branded_only_constraint`_
- **17.** What branded ice cream has less sugar than Haagen-Dazs vanilla?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **18.** I want to switch from General Mills Honey Nut Cheerios to a lower-sugar cereal. What do you recommend?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **19.** Kashi GoLean bars are my current snack. Can you suggest a lower-sugar granola or nutrition bar I can buy?  
  _tags: `category_keyword_search`, `current_favorite_comparison`, `branded_only_constraint`_
- **20.** **[TEST]** I love Fage 0% vanilla yogurt but it feels a bit sweet. What branded yogurt has less sugar?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **21.** What lower-sugar cookie can I buy to replace Nabisco Honey Maid graham crackers?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **22.** I'm currently eating RXBARs — what branded protein bar has less sugar?  
  _tags: `category_keyword_search`, `current_favorite_comparison`, `branded_only_constraint`_
- **23.** Halo Top chocolate ice cream is good but I want the lowest-sugar ice cream available in stores.  
  _tags: `category_keyword_search`, `ranked_low_sugar_alternatives`_
- **24.** **[TEST]** I eat KIND bars daily. Find me a branded bar with less sugar.  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **25.** What's a lower-sugar packaged cracker I can swap for Nabisco Ritz?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **26.** I want to cut my sugar intake by switching from Breyers natural vanilla ice cream to something lower-sugar. What brands should I look at?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **27.** My go-to snack bar is a Lenny & Larry's Complete Cookie. What branded bar or cookie has less sugar?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **28.** Can you find a branded granola bar with less sugar than a Quaker Chewy chocolate chip bar?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **29.** I eat Atkins bars as snacks. Is there a lower-sugar branded bar I should switch to?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **30.** **[TEST]** What's a store-bought yogurt with less sugar than Siggi's plain whole milk yogurt?  
  _tags: `category_keyword_search`, `current_favorite_comparison`, `branded_only_constraint`_
- **31.** I love Built Bar protein bars. What branded snack bar has even less sugar?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **32.** **[TEST]** Talenti gelato has a lot of sugar. What's a lower-sugar frozen dessert I can buy at the grocery store?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **33.** What branded cereal has less sugar than Kellogg's Frosted Flakes?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **34.** I currently snack on Quest protein bars. Can you find a lower-sugar branded bar alternative?  
  _tags: `category_keyword_search`, `current_favorite_comparison`, `branded_only_constraint`_
- **35.** What packaged cookie has less sugar than Pepperidge Farm Chessmen butter cookies?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **36.** I eat Keebler Club crackers as a snack. What branded cracker has less sugar?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **37.** My current ice cream is Breyers Reese's. What's a lower-sugar ice cream brand I could buy instead?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **38.** What branded granola bar has less sugar than a Nature Valley Sweet & Salty Nut bar?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_
- **39.** I eat Kashi Heart to Heart cereal. What lower-sugar branded cereal can I switch to?  
  _tags: `category_keyword_search`, `current_favorite_comparison`_

## MODERATE (40 questions, ids 40–79)

- **40.** **[TEST]** I need a yogurt with under 5g of added sugar per serving for my kid's school lunch box — what branded yogurts should I look at?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `kid_friendly_or_household_swap`, `branded_only_constraint`_
- **41.** My daughter is lactose intolerant and I want to find a lower-sugar lactose-free yogurt alternative to Chobani. What are my options?  
  _tags: `category_keyword_search`, `kid_friendly_or_household_swap`, `branded_only_constraint`_
- **42.** I need a gluten-free granola bar with less sugar than a Quaker Chewy bar for my celiac kid's snack. What branded bars can you find?  
  _tags: `category_keyword_search`, `kid_friendly_or_household_swap`, `branded_only_constraint`_
- **43.** I want 2 or 3 ranked lower-sugar cookie options to replace Oreos — which branded cookies have the least sugar per serving?  
  _tags: `ranked_low_sugar_alternatives`, `category_keyword_search`_
- **44.** Can you give me three ranked low-sugar ice cream brands to replace Ben & Jerry's, sorted by sugar per serving?  
  _tags: `ranked_low_sugar_alternatives`, `category_keyword_search`_
- **45.** I want a cereal with no more than 6g of added sugar per serving. My current brand is General Mills Cinnamon Toast Crunch. What branded cereals qualify?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `current_favorite_comparison`, `branded_only_constraint`_
- **46.** My whole family eats Kellogg's Froot Loops. What lower-sugar branded cereal would work for both kids and adults?  
  _tags: `kid_friendly_or_household_swap`, `category_keyword_search`_
- **47.** I'm looking for a gluten-free, low-sugar cracker to replace Ritz. What branded options exist?  
  _tags: `category_keyword_search`, `branded_only_constraint`_
- **48.** **[TEST]** What branded protein bar has less than 5g of total sugar and is also nut-free for my kid's school snack?  
  _tags: `kid_friendly_or_household_swap`, `added_sugar_vs_total_sugar_disambiguation`, `branded_only_constraint`_
- **49.** **[TEST]** I need 3 ranked low-sugar branded granola bars to replace my KIND Dark Chocolate Nuts & Sea Salt bar — which ones have the least sugar?  
  _tags: `ranked_low_sugar_alternatives`, `current_favorite_comparison`_
- **50.** My kids love Yoplait Go-Gurt. Can I find a lower-sugar tube yogurt that's also kid-friendly?  
  _tags: `kid_friendly_or_household_swap`, `current_favorite_comparison`_
- **51.** **[TEST]** I want to switch from Talenti Caramel Cookie Crunch gelato to something with under 15g total sugar per serving. What branded frozen desserts qualify?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `current_favorite_comparison`, `branded_only_constraint`_
- **52.** I'm diabetic and need a branded candy alternative to Reese's with less than 5g of added sugar. What are my options?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `category_keyword_search`, `branded_only_constraint`_
- **53.** Give me 3 ranked lower-sugar branded yogurt options to replace my daily Oikos strawberry yogurt.  
  _tags: `ranked_low_sugar_alternatives`, `current_favorite_comparison`_
- **54.** I need a lower-sugar, dairy-free frozen dessert to replace Haagen-Dazs. What branded options can you find?  
  _tags: `category_keyword_search`, `branded_only_constraint`_
- **55.** My son wants a snack bar for after school. I want it to have less sugar than a Clif Bar and be packaged (not homemade). What do you recommend?  
  _tags: `kid_friendly_or_household_swap`, `current_favorite_comparison`, `branded_only_constraint`_
- **56.** **[TEST]** When you say 'lower sugar' for cereal, do you mean total sugar or added sugar? I'm looking at switching from Raisin Bran.  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `current_favorite_comparison`_
- **57.** I want to stock my pantry with lower-sugar crackers for the whole family. What 3 branded options have the least sugar?  
  _tags: `ranked_low_sugar_alternatives`, `kid_friendly_or_household_swap`_
- **58.** I currently buy Chips Ahoy! Chewy for my kids. What lower-sugar branded cookie would still be kid-friendly?  
  _tags: `kid_friendly_or_household_swap`, `current_favorite_comparison`_
- **59.** I want a gluten-free branded cookie with less sugar than Oreos. What are my options?  
  _tags: `category_keyword_search`, `branded_only_constraint`_
- **60.** **[TEST]** What branded ice cream has less added sugar — not just total sugar — compared to Breyers natural vanilla?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `current_favorite_comparison`_
- **61.** I need 2-3 ranked branded protein bars with less sugar than an RXBar. My budget is mainstream grocery stores.  
  _tags: `ranked_low_sugar_alternatives`, `current_favorite_comparison`, `branded_only_constraint`_
- **62.** My toddler loves Cheerios. What lower-sugar branded cereal could I introduce as he gets older?  
  _tags: `kid_friendly_or_household_swap`, `current_favorite_comparison`_
- **63.** Is there a branded candy bar with less sugar than Snickers and also less than 200 calories? Show me ranked options.  
  _tags: `ranked_low_sugar_alternatives`, `current_favorite_comparison`_
- **64.** I want to replace Kellogg's Special K Protein bars with something that has less added sugar. What branded bars can you find?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `current_favorite_comparison`, `branded_only_constraint`_
- **65.** My family goes through a lot of granola bars. What 3 branded options have the lowest sugar and would also appeal to kids?  
  _tags: `ranked_low_sugar_alternatives`, `kid_friendly_or_household_swap`_
- **66.** I currently eat Siggi's skyr yogurt. What branded yogurt has even less total sugar per serving?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `current_favorite_comparison`_
- **67.** What branded granola bars are gluten-free and have less sugar than a Kind Oats & Honey bar?  
  _tags: `category_keyword_search`, `current_favorite_comparison`, `branded_only_constraint`_
- **68.** I want to swap out Hershey's chocolate chips (used in cookies) for a lower-sugar branded alternative. What branded baking chocolate chips should I buy?  
  _tags: `category_keyword_search`, `current_favorite_comparison`, `branded_only_constraint`_
- **69.** My daughter's sports team needs a packaged snack with under 8g added sugar per serving. What branded granola bars or crackers fit the bill?  
  _tags: `kid_friendly_or_household_swap`, `added_sugar_vs_total_sugar_disambiguation`, `branded_only_constraint`_
- **70.** I eat ice cream every night and want to cut back on added sugar specifically. What branded ice cream has the least added sugar?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `ranked_low_sugar_alternatives`_
- **71.** What's the difference between total sugar and added sugar in yogurt, and which should I focus on when comparing Chobani vs Fage?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `current_favorite_comparison`_
- **72.** I need a lower-sugar snack bar for long hikes that has less sugar than a Clif Builder's bar. It needs to be purchasable at outdoor retailers. What branded options exist?  
  _tags: `current_favorite_comparison`, `branded_only_constraint`_
- **73.** My kids want something sweet for dessert that isn't ice cream. What branded cookies or bars have less sugar than Oreo Thins?  
  _tags: `kid_friendly_or_household_swap`, `current_favorite_comparison`_
- **74.** Can you give me 3 ranked lower-sugar branded cereals that are also high in fiber, to replace my Kellogg's Raisin Bran?  
  _tags: `ranked_low_sugar_alternatives`, `current_favorite_comparison`_
- **75.** I want a store-bought protein bar with under 4g added sugar. I currently eat Lenny & Larry's cookies. What do you suggest?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `current_favorite_comparison`, `branded_only_constraint`_
- **76.** **[TEST]** My wife and I both snack on Pepperidge Farm Goldfish crackers. What lower-sugar branded cracker can we switch to as a household?  
  _tags: `kid_friendly_or_household_swap`, `current_favorite_comparison`_
- **77.** **[TEST]** I need a kid-friendly branded yogurt tube or pouch with under 10g total sugar. My current choice is Gogurt. What alternatives exist?  
  _tags: `kid_friendly_or_household_swap`, `added_sugar_vs_total_sugar_disambiguation`, `current_favorite_comparison`_
- **78.** What 2-3 branded candy options have the least added sugar and would still satisfy a chocolate craving?  
  _tags: `ranked_low_sugar_alternatives`, `added_sugar_vs_total_sugar_disambiguation`_
- **79.** I'm trying to find a dairy-free, low-sugar branded yogurt alternative to Chobani for my lactose-intolerant teenager.  
  _tags: `kid_friendly_or_household_swap`, `category_keyword_search`, `branded_only_constraint`_

## EDGE (20 questions, ids 80–99)

- **80.** I found a 'zero sugar' Quest Hero bar. Does it actually have zero sugar, or does it use sugar alcohols like erythritol? Will the skill disclose that?  
  _tags: `sugar_alcohol_disclosure`, `current_favorite_comparison`, `branded_only_constraint`_
- **81.** **[TEST]** This Lily's chocolate bar says 'no added sugar' on the label but the ingredients list erythritol and stevia. Is it really zero sugar? What will the nutrition label say?  
  _tags: `sugar_alcohol_disclosure`, `added_sugar_vs_total_sugar_disambiguation`_
- **82.** I want a 'sugar-free' gum. The pack says 0g sugar but lists xylitol. How should that be interpreted when ranking low-sugar snacks?  
  _tags: `sugar_alcohol_disclosure`, `added_sugar_vs_total_sugar_disambiguation`_
- **83.** The Atkins Endulge bar says 'only 1g sugar' but uses maltitol and glycerin. Does the skill flag sugar alcohols when suggesting this as a low-sugar alternative?  
  _tags: `sugar_alcohol_disclosure`, `current_favorite_comparison`_
- **84.** I'm looking for a low-sugar granola bar — the one I found says 'no added sugar' but has apple juice concentrate as the third ingredient. Is that misleading?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `branded_only_constraint`_
- **85.** A Nature Valley bar claims 'made with natural sweeteners' and '0g added sugar.' The ingredient list shows honey and brown rice syrup. How does this affect the sugar ranking?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `current_favorite_comparison`_
- **86.** I want a Catalina Crunch cereal because it's marketed as low-sugar. Does FoodData Central have this brand? How should the skill handle brands not in the database?  
  _tags: `category_keyword_search`, `branded_only_constraint`_
- **87.** Can you find Magic Spoon cereal in FoodData Central? It's a newer DTC brand with very low sugar claims. What happens if it's not in the USDA database?  
  _tags: `branded_only_constraint`, `category_keyword_search`_
- **88.** **[TEST]** Halo Top says it has fewer calories and less sugar than regular ice cream. But is its sugar count driven by erythritol? How should I interpret the nutrition panel?  
  _tags: `sugar_alcohol_disclosure`, `current_favorite_comparison`, `added_sugar_vs_total_sugar_disambiguation`_
- **89.** I bought a 'sugar-free' Werther's candy. It lists isomalt and acesulfame potassium. Does the FDC label show 0g sugar? Should I still consider it a low-sugar snack?  
  _tags: `sugar_alcohol_disclosure`, `added_sugar_vs_total_sugar_disambiguation`_
- **90.** **[TEST]** A protein bar I found lists 'allulose' in the ingredients but claims 2g sugar on the label. Does allulose count toward added sugar on FDA labels? How does the skill handle this?  
  _tags: `sugar_alcohol_disclosure`, `added_sugar_vs_total_sugar_disambiguation`_
- **91.** I want a 'no added sugar' ice cream. Breyers has a line called 'No Sugar Added' that uses sorbitol. Does sorbitol change how it should be ranked against regular ice cream?  
  _tags: `sugar_alcohol_disclosure`, `current_favorite_comparison`, `branded_only_constraint`_
- **92.** The Enlightened ice cream bar shows 6g sugar on the label, but some of that appears to come from erythritol. Should the skill disclose that sugar alcohol content when recommending it?  
  _tags: `sugar_alcohol_disclosure`, `branded_only_constraint`_
- **93.** A 'low-sugar' granola I found lists coconut sugar as the first sweetener. Isn't coconut sugar still added sugar? How does FDC categorize it?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `branded_only_constraint`_
- **94.** **[TEST]** I found a Kodiak Cakes granola bar 'protein packed' with 8g added sugar. The brand isn't showing up in FoodData Central. How should the skill handle this gap?  
  _tags: `branded_only_constraint`, `current_favorite_comparison`_
- **95.** I want a zero-sugar candy — not just low-sugar. The Atkins peanut butter cups use erythritol and show 0g sugar on the label. How should the skill disclose that?  
  _tags: `sugar_alcohol_disclosure`, `ranked_low_sugar_alternatives`_
- **96.** A KIND Protein bar says '5g sugar' but has soluble corn fiber listed before the sweeteners. Does fiber content affect how FDC ranks the sugar? Should the skill note this?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `current_favorite_comparison`_
- **97.** I'm comparing two Chobani flavors: one says '0% added sugar' using fruit puree and the other uses cane sugar. Are both classified the same way in FDC's labelNutrients?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `branded_only_constraint`_
- **98.** I eat Costco Kirkland Signature protein bars. This private label brand may not be in FoodData Central. How does the skill handle private-label or warehouse brands with incomplete FDC records?  
  _tags: `branded_only_constraint`, `current_favorite_comparison`_
- **99.** A 'no sugar added' dried mango snack I found lists 34g total sugar. It's all intrinsic fruit sugar with no added sugar. Should the skill recommend or avoid it when someone asks for a 'low-sugar snack'?  
  _tags: `added_sugar_vs_total_sugar_disambiguation`, `branded_only_constraint`_
