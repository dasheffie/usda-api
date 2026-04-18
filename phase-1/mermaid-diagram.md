# USDA FoodData Central — Ability ↔ Endpoint Graph

```mermaid
graph LR
  subgraph endpoints
    E1[GET /foods/search]
    E2[POST /foods/search]
    E3[GET /food/fdcId]
    E4[POST /foods batch]
  end

  subgraph abilities
    A1(dining-out)
    A2(low-sugar-snack)
    A3(recipe-breakdown)
    A4(vegan-check)
    A5(micronutrient-lookup)
    A6(macro-alignment)
    A7(daily-intake-tally)
    A8(nutrient-dense-substitute)
    A9(allergen-scan)
    A10(label-scanner)
    A11(product-comparison)
    A12(cart-optimization)
    A13(threshold-tracking)
    A14(healthy-swap)
  end

  A1 -->|brandOwner + keyword| E2
  A1 -->|labelNutrients + calories| E3
  A2 -->|dataType=Branded| E2
  A2 -->|labelNutrients.sugars| E3
  A3 -->|SR Legacy lookup| E1
  A3 -->|foodNutrients full| E4
  A4 -->|ingredients substring| E3
  A5 -->|nutrients filter 303/418/301| E3
  A6 -->|foodNutrients 203/204/205/291/539| E3
  A7 -->|batch + nutrient sum| E4
  A8 -->|dataType=Foundation sort-by-nutrient| E2
  A9 -->|ingredients substring| E3
  A10 -->|full profile + labelNutrients| E3
  A11 -->|parallel fetch 2-3 items| E3
  A12 -->|batch + aggregate + swap search| E4
  A12 -->|find-swap follow-up| E2
  A13 -->|single nutrient contribution| E3
  A14 -->|fetch target| E3
  A14 -->|search Branded alternatives| E2
```

## Merge-visualization note

`A4 (vegan-check)` and `A9 (allergen-scan)` both have **exactly one outbound edge → E3** and both read only the `ingredients` field with the same substring-scan parse. Per iron law #1 they MERGE into `usda-fdc-ingredient-compliance`.

All other ability pairs either hit a different endpoint set OR read different response fields OR apply a different parse strategy, so they remain separate per the strict merge rule.
