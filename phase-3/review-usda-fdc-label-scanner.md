# usda-fdc-label-scanner — 100-question corpus

## Splits
- train_ids (80): `[2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33, 34, 36, 38, 39, 40, 42, 43, 44, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 69, 71, 72, 74, 75, 76, 78, 79, 80, 81, 82, 85, 86, 87, 89, 90, 91, 92, 93, 94, 95, 96, 97, 99]`
- test_ids (20): `[0, 1, 9, 10, 24, 32, 35, 37, 41, 45, 49, 62, 68, 70, 73, 77, 83, 84, 88, 98]`
- seed: `3913540746`  mode: `hackathon`  threshold: `1.0`

## Ability-tag coverage

| Tag | Count |
|---|---|
| `plain_language_verdict` | 69 |
| `prediabetes_risk_assessment` | 31 |
| `confidence_disclosure` | 30 |
| `high_cholesterol_risk_assessment` | 28 |
| `hypertension_risk_assessment` | 22 |
| `pcos_risk_assessment` | 20 |
| `alternative_ranking` | 13 |

## EASY (40 questions, ids 0–39)

- ** 0.** **[TEST]** Are Oreos OK for my prediabetes?  
  _tags: `prediabetes_risk_assessment`, `plain_language_verdict`_
- ** 1.** **[TEST]** Is Campbell's Chicken Noodle Soup safe to eat with my hypertension?  
  _tags: `hypertension_risk_assessment`, `plain_language_verdict`_
- ** 2.** Can I eat Cheerios if I have high cholesterol?  
  _tags: `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- ** 3.** Is Yoplait Original Strawberry yogurt okay for PCOS?  
  _tags: `pcos_risk_assessment`, `plain_language_verdict`_
- ** 4.** Should I avoid Progresso Tomato Basil soup because of my CKD?  
  _tags: `plain_language_verdict`_
- ** 5.** Can I snack on KIND Dark Chocolate Nuts & Sea Salt bars with prediabetes?  
  _tags: `prediabetes_risk_assessment`, `plain_language_verdict`_
- ** 6.** Is Gatorade Fruit Punch safe for someone with prediabetes?  
  _tags: `prediabetes_risk_assessment`, `plain_language_verdict`_
- ** 7.** Can I eat Triscuit Original crackers with high cholesterol?  
  _tags: `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- ** 8.** Is Raisin Bran cereal a good breakfast for prediabetes?  
  _tags: `prediabetes_risk_assessment`, `plain_language_verdict`_
- ** 9.** **[TEST]** Is Siggi's Plain Whole Milk Yogurt safe if I have PCOS?  
  _tags: `pcos_risk_assessment`, `plain_language_verdict`_
- **10.** **[TEST]** Are Goldfish crackers okay for my hypertension?  
  _tags: `hypertension_risk_assessment`, `plain_language_verdict`_
- **11.** Can I have Ben & Jerry's Chocolate Chip Cookie Dough ice cream with prediabetes?  
  _tags: `prediabetes_risk_assessment`, `plain_language_verdict`_
- **12.** Is Halo Top Vanilla Bean ice cream a safer option for my prediabetes?  
  _tags: `prediabetes_risk_assessment`, `plain_language_verdict`_
- **13.** Should I eat Kashi Go Crunch cereal if I have high cholesterol?  
  _tags: `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- **14.** Can someone with CKD eat Wheat Thins?  
  _tags: `plain_language_verdict`_
- **15.** Is Special K Red Berries cereal okay for prediabetes?  
  _tags: `prediabetes_risk_assessment`, `plain_language_verdict`_
- **16.** Is Fage Total 0% Plain Greek Yogurt good for someone with PCOS?  
  _tags: `pcos_risk_assessment`, `plain_language_verdict`_
- **17.** Are Nature Valley Oats 'n Honey granola bars safe for high cholesterol?  
  _tags: `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- **18.** Is Progresso Minestrone soup too salty for my hypertension?  
  _tags: `hypertension_risk_assessment`, `plain_language_verdict`_
- **19.** Can I eat Eggo Buttermilk Waffles with prediabetes?  
  _tags: `prediabetes_risk_assessment`, `plain_language_verdict`_
- **20.** Is Vitaminwater Zero ok for someone with hypertension?  
  _tags: `hypertension_risk_assessment`, `plain_language_verdict`_
- **21.** Is a Clif Bar safe to eat if I have PCOS?  
  _tags: `pcos_risk_assessment`, `plain_language_verdict`_
- **22.** Can I eat Nature's Own Honey Wheat bread with high cholesterol?  
  _tags: `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- **23.** Are Lay's Classic Potato Chips okay if I have hypertension?  
  _tags: `hypertension_risk_assessment`, `plain_language_verdict`_
- **24.** **[TEST]** Is Quest Protein Bar (Chocolate Chip Cookie Dough) OK for prediabetes?  
  _tags: `prediabetes_risk_assessment`, `plain_language_verdict`_
- **25.** Should someone with CKD eat Campbell's Tomato Soup?  
  _tags: `plain_language_verdict`_
- **26.** Is Chobani Plain Non-Fat Greek Yogurt good for PCOS?  
  _tags: `pcos_risk_assessment`, `plain_language_verdict`_
- **27.** Are Quaker Oats Instant Oatmeal (Original) packets safe for high cholesterol?  
  _tags: `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- **28.** Can I drink Tropicana Pure Premium Orange Juice with prediabetes?  
  _tags: `prediabetes_risk_assessment`, `plain_language_verdict`_
- **29.** Is Stacy's Simply Naked Pita Chips okay for hypertension?  
  _tags: `hypertension_risk_assessment`, `plain_language_verdict`_
- **30.** Is Chobani Flip Strawberry Cheesecake yogurt safe for high cholesterol?  
  _tags: `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- **31.** Can someone with CKD eat Pringles Original chips?  
  _tags: `plain_language_verdict`_
- **32.** **[TEST]** Is Kellogg's Frosted Flakes cereal too sugary for prediabetes?  
  _tags: `prediabetes_risk_assessment`, `plain_language_verdict`_
- **33.** Are KIND Oats & Honey Clusters granola bars ok for PCOS?  
  _tags: `pcos_risk_assessment`, `plain_language_verdict`_
- **34.** Is Amy's Low Sodium Lentil Soup safe if I have hypertension?  
  _tags: `hypertension_risk_assessment`, `plain_language_verdict`_
- **35.** **[TEST]** Can I eat Pepperidge Farm Whole Grain White Bread with high cholesterol?  
  _tags: `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- **36.** Is Dannon Light & Fit Greek Vanilla Yogurt okay for prediabetes?  
  _tags: `prediabetes_risk_assessment`, `plain_language_verdict`_
- **37.** **[TEST]** Can someone with CKD eat Progresso Lentil Soup?  
  _tags: `plain_language_verdict`_
- **38.** Is RXBar Chocolate Sea Salt okay for high cholesterol?  
  _tags: `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- **39.** Are Pop-Tarts Frosted Strawberry too sugary for PCOS?  
  _tags: `pcos_risk_assessment`, `plain_language_verdict`_

## MODERATE (40 questions, ids 40–79)

- **40.** I have both PCOS and high cholesterol — can I eat Chobani Flip Strawberry Cheesecake yogurt?  
  _tags: `pcos_risk_assessment`, `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- **41.** **[TEST]** I have prediabetes and hypertension. Is Campbell's Healthy Request Chicken Noodle Soup safe to eat?  
  _tags: `prediabetes_risk_assessment`, `hypertension_risk_assessment`, `plain_language_verdict`_
- **42.** Which is better for my prediabetes — Nature Valley Oats 'n Honey or KIND Dark Chocolate Nuts & Sea Salt bar?  
  _tags: `prediabetes_risk_assessment`, `alternative_ranking`, `plain_language_verdict`_
- **43.** I have high cholesterol and hypertension. Can I eat Triscuit Original crackers?  
  _tags: `high_cholesterol_risk_assessment`, `hypertension_risk_assessment`, `plain_language_verdict`_
- **44.** Can I eat Ben & Jerry's Halo Top Vanilla Bean ice cream instead of regular Ben & Jerry's if I have prediabetes? Rank the alternatives.  
  _tags: `prediabetes_risk_assessment`, `alternative_ranking`, `plain_language_verdict`_
- **45.** **[TEST]** I have PCOS and prediabetes. Is Clif Bar Chocolate Chip a reasonable snack?  
  _tags: `pcos_risk_assessment`, `prediabetes_risk_assessment`, `plain_language_verdict`_
- **46.** The label on this Quaker Oatmeal packet doesn't list added sugar. Can I still assess it for my prediabetes?  
  _tags: `prediabetes_risk_assessment`, `confidence_disclosure`_
- **47.** I have hypertension and CKD stage 3. Is Amy's Low Sodium Minestrone Soup safe for me?  
  _tags: `hypertension_risk_assessment`, `plain_language_verdict`_
- **48.** My doctor says I have high cholesterol. Which granola bar should I pick: Kind Dark Chocolate Nuts & Sea Salt, Nature Valley Protein Bar, or Kashi Dark Mocha Almond Bar?  
  _tags: `high_cholesterol_risk_assessment`, `alternative_ranking`_
- **49.** **[TEST]** Can I eat Kellogg's Special K Protein cereal if I have both high cholesterol and prediabetes?  
  _tags: `high_cholesterol_risk_assessment`, `prediabetes_risk_assessment`, `plain_language_verdict`_
- **50.** The FDC record for this older Branded Cream of Wheat doesn't include labelNutrients at all. Can you still evaluate it for my hypertension?  
  _tags: `hypertension_risk_assessment`, `confidence_disclosure`_
- **51.** I have PCOS and high cholesterol. Please compare Siggi's 4% Plain Yogurt vs Fage Total 2% and rank them.  
  _tags: `pcos_risk_assessment`, `high_cholesterol_risk_assessment`, `alternative_ranking`_
- **52.** I have hypertension on the DASH diet. Can I eat Wheat Thins Original crackers? And what would be a better swap?  
  _tags: `hypertension_risk_assessment`, `alternative_ranking`_
- **53.** I have both high cholesterol and hypertension. Is Progresso Light Chicken Noodle Soup safe to eat?  
  _tags: `high_cholesterol_risk_assessment`, `hypertension_risk_assessment`, `plain_language_verdict`_
- **54.** I have PCOS. I'm looking at Yoplait Original vs Chobani Zero Sugar yogurt — which is better for me?  
  _tags: `pcos_risk_assessment`, `alternative_ranking`_
- **55.** Can I eat Kashi Heart to Heart Honey Toasted Oat cereal if I have both prediabetes and high cholesterol?  
  _tags: `prediabetes_risk_assessment`, `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- **56.** The FDC entry for this RXBar doesn't list added sugar separately. How confident are you in your prediabetes verdict?  
  _tags: `prediabetes_risk_assessment`, `confidence_disclosure`_
- **57.** I have CKD and hypertension. What's your take on Swanson's Low Sodium Chicken Broth?  
  _tags: `hypertension_risk_assessment`, `plain_language_verdict`_
- **58.** I have high cholesterol. Is Orville Redenbacher's Naturals Simply Salted popcorn okay? Suggest cleaner alternatives if not.  
  _tags: `high_cholesterol_risk_assessment`, `alternative_ranking`_
- **59.** Can I eat Pepperidge Farm Cinnamon Raisin Swirl bread with prediabetes and high cholesterol?  
  _tags: `prediabetes_risk_assessment`, `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- **60.** I have PCOS. This granola bar label is missing added sugar info. Can you still rate it for me?  
  _tags: `pcos_risk_assessment`, `confidence_disclosure`_
- **61.** Is Kellogg's Corn Flakes cereal safe for CKD stage 3?  
  _tags: `plain_language_verdict`, `confidence_disclosure`_
- **62.** **[TEST]** I have hypertension. Rank these three soups for me: Campbell's Healthy Request Tomato, Amy's Low Sodium Tomato, and Pacific Foods Organic Tomato.  
  _tags: `hypertension_risk_assessment`, `alternative_ranking`_
- **63.** Can someone with both PCOS and prediabetes eat a Larabar Peanut Butter Cookie bar?  
  _tags: `pcos_risk_assessment`, `prediabetes_risk_assessment`, `plain_language_verdict`_
- **64.** I'm on the DASH diet for hypertension. Is Snyder's of Hanover Pretzels a safe snack?  
  _tags: `hypertension_risk_assessment`, `plain_language_verdict`_
- **65.** I have CKD stage 3 and I'm watching my potassium. Is V8 Original Vegetable Juice safe for me?  
  _tags: `confidence_disclosure`, `plain_language_verdict`_
- **66.** I have high cholesterol. Which is better: Cheerios vs Kashi GOLEAN Crunch vs Raisin Bran?  
  _tags: `high_cholesterol_risk_assessment`, `alternative_ranking`_
- **67.** I manage prediabetes and hypertension. Is Trader Joe's Low Sodium Black Bean Soup a good option?  
  _tags: `prediabetes_risk_assessment`, `hypertension_risk_assessment`, `plain_language_verdict`_
- **68.** **[TEST]** I have PCOS. The label on this Clif Builder's Protein Bar doesn't show saturated fat clearly. Can you still assess it?  
  _tags: `pcos_risk_assessment`, `confidence_disclosure`_
- **69.** I have high cholesterol and I want to swap Goldfish for a better cracker. Rank Triscuit, Wasa Crispbread, and Mary's Gone Crackers.  
  _tags: `high_cholesterol_risk_assessment`, `alternative_ranking`_
- **70.** **[TEST]** I have CKD and I'm eating Dole Pineapple Chunks in juice. Is this safe given my phosphorus restrictions?  
  _tags: `confidence_disclosure`, `plain_language_verdict`_
- **71.** I manage both PCOS and prediabetes. Is Kashi GOLEAN Original cereal safe for me?  
  _tags: `pcos_risk_assessment`, `prediabetes_risk_assessment`, `plain_language_verdict`_
- **72.** I have hypertension. Can I eat Sabra Classic Hummus with my DASH diet, and which brand is cleaner?  
  _tags: `hypertension_risk_assessment`, `alternative_ranking`_
- **73.** **[TEST]** I have high cholesterol and my LDL is very high. Is Justin's Classic Almond Butter good for me?  
  _tags: `high_cholesterol_risk_assessment`, `plain_language_verdict`_
- **74.** I have hypertension and CKD. The older FDC record for this Progresso soup doesn't have labelNutrients. Can you still advise?  
  _tags: `hypertension_risk_assessment`, `confidence_disclosure`_
- **75.** I have prediabetes. Rank these three yogurts: Chobani Zero Sugar, Yoplait Light, and Dannon Light & Fit.  
  _tags: `prediabetes_risk_assessment`, `alternative_ranking`_
- **76.** I have PCOS and I want to know if Kirkland Signature Chocolate Almonds are safe. The label is missing added sugar info.  
  _tags: `pcos_risk_assessment`, `confidence_disclosure`_
- **77.** **[TEST]** I have both high cholesterol and hypertension. Should I eat Boar's Head Low Sodium Oven Roasted Turkey?  
  _tags: `high_cholesterol_risk_assessment`, `hypertension_risk_assessment`, `plain_language_verdict`_
- **78.** I manage prediabetes. Can I eat Thomas' Plain Bagels? Suggest better bread alternatives.  
  _tags: `prediabetes_risk_assessment`, `alternative_ranking`_
- **79.** I have CKD stage 3. Is Jif Creamy Peanut Butter safe, given concerns about potassium and phosphorus?  
  _tags: `confidence_disclosure`, `plain_language_verdict`_

## EDGE (20 questions, ids 80–99)

- **80.** The nutrition label on this crackers box says 0g trans fat per serving, but the ingredients list 'partially hydrogenated soybean oil.' Do I need to worry about trans fat with my high cholesterol?  
  _tags: `high_cholesterol_risk_assessment`, `confidence_disclosure`, `plain_language_verdict`_
- **81.** This cookie shows exactly 5g saturated fat per serving. Does it pass or fail for high cholesterol?  
  _tags: `high_cholesterol_risk_assessment`, `confidence_disclosure`_
- **82.** I have PCOS. This older Branded FDC entry for a granola bar is missing added sugar AND saturated fat in labelNutrients. How do you assess it?  
  _tags: `pcos_risk_assessment`, `confidence_disclosure`_
- **83.** **[TEST]** I have CKD stage 3. This FDC record for a canned tomato product doesn't have phosphorus populated. How confident are you in your potassium/phosphorus verdict?  
  _tags: `confidence_disclosure`, `plain_language_verdict`_
- **84.** **[TEST]** This granola bar label says 0g trans fat, but the ingredients include 'partially hydrogenated cottonseed oil.' Is it safe for PCOS?  
  _tags: `pcos_risk_assessment`, `confidence_disclosure`_
- **85.** I have CKD stage 3 and need to restrict potassium. The FDC record for this Bolthouse Farms Green Goodness juice doesn't list potassium in labelNutrients. Can you still give me a verdict?  
  _tags: `confidence_disclosure`, `plain_language_verdict`_
- **86.** I have prediabetes. This protein bar shows exactly 6g added sugar per serving — right at the threshold. Is it red or green?  
  _tags: `prediabetes_risk_assessment`, `confidence_disclosure`_
- **87.** I have both CKD and high cholesterol. The FDC entry for this Amy's Frozen Burrito is missing phosphorus and potassium. What's your confidence level on this assessment?  
  _tags: `high_cholesterol_risk_assessment`, `confidence_disclosure`_
- **88.** **[TEST]** I have hypertension. This Branded soup's sodium is listed as 230mg per serving exactly — right on the DASH amber threshold. How do you classify it?  
  _tags: `hypertension_risk_assessment`, `plain_language_verdict`_
- **89.** I have prediabetes. The FDC Branded record for this Clif Bar lists net carbs as 44g but fiber as 4g. Doesn't the net carbs/fiber ratio trigger the amber rule?  
  _tags: `prediabetes_risk_assessment`, `confidence_disclosure`_
- **90.** I have PCOS. This bar says 0g trans fat on the nutrition label, but 'partially hydrogenated palm kernel oil' appears late in the ingredient list. What's your verdict?  
  _tags: `pcos_risk_assessment`, `confidence_disclosure`_
- **91.** I have CKD stage 3. The FDC record for this Gatorade G2 shows sodium but phosphorus is missing. How do you handle the phosphorus assessment?  
  _tags: `confidence_disclosure`, `plain_language_verdict`_
- **92.** I have high cholesterol. This snack bar has exactly 5g saturated fat. The FDC record also doesn't list trans fat in labelNutrients but the ingredients contain 'interesterified soybean oil.' How do you rate it?  
  _tags: `high_cholesterol_risk_assessment`, `confidence_disclosure`_
- **93.** I have prediabetes. This older FDC Branded record for a cereal has no labelNutrients at all — only the raw foodNutrients array. Can you fall back to that and give me a verdict?  
  _tags: `prediabetes_risk_assessment`, `confidence_disclosure`_
- **94.** I have high cholesterol and the label says 0g trans fat on this microwave popcorn, but the ingredient list includes 'partially hydrogenated oil.' The FDC entry also lacks addedSugar. How do you assess it?  
  _tags: `high_cholesterol_risk_assessment`, `confidence_disclosure`_
- **95.** I have CKD stage 3. The FDC record for this Bush's Best Baked Beans has sodium and potassium listed, but phosphorus is missing. How confident can you be?  
  _tags: `confidence_disclosure`, `plain_language_verdict`_
- **96.** I have prediabetes. This Branded FDC record for Nature Valley Sweet & Salty Nut bar is missing addedSugar but shows total sugars of 11g. How do you interpret this for the >6g added sugar rule?  
  _tags: `prediabetes_risk_assessment`, `confidence_disclosure`_
- **97.** I have both CKD stage 3 and hypertension. The FDC record for this Amy's Kitchen Vegetable Pot Pie is missing potassium AND phosphorus. Give me a verdict with appropriate confidence disclosure.  
  _tags: `hypertension_risk_assessment`, `confidence_disclosure`_
- **98.** **[TEST]** I have PCOS and high cholesterol. This protein bar says 0g trans fat but lists 'fully hydrogenated oil' AND 'partially hydrogenated oil' — which one should I care about?  
  _tags: `pcos_risk_assessment`, `high_cholesterol_risk_assessment`, `confidence_disclosure`_
- **99.** I have prediabetes. This snack has net carbs of 21g (just over the 20g threshold) and fiber of 2g (under 3g). But the added sugar is only 4g. Does it fail or pass, and with what confidence?  
  _tags: `prediabetes_risk_assessment`, `confidence_disclosure`, `plain_language_verdict`_
