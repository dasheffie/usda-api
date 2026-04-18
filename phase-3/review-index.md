# Phase 3 — Question Corpus Review Index

Protocol: **Hackathon**. Per-skill corpus: 100 questions (40 easy / 40 moderate / 20 edge), split **80 train / 0 val / 20 test**. Train is rotated by the coverage-weighted sampler in Phase 4; val is skipped under Hackathon greedy acceptance; test is touched exactly once at Phase 6 graduation.

Run parameters: `max_rounds=5`, `base_train_batch_size=20`, `decay_rate=1.0`, `graduation_threshold=1.0`.

## Skill overview

| # | Skill | Total | Train | Test | Axes | Review file |
|---|---|---:|---:|---:|---:|---|
| 1 | `usda-fdc-cart-optimization` | 100 | 80 | 20 | 8 | [review-usda-fdc-cart-optimization.md](./review-usda-fdc-cart-optimization.md) |
| 2 | `usda-fdc-daily-intake-tally` | 100 | 80 | 20 | 8 | [review-usda-fdc-daily-intake-tally.md](./review-usda-fdc-daily-intake-tally.md) |
| 3 | `usda-fdc-dining-out` | 100 | 80 | 20 | 7 | [review-usda-fdc-dining-out.md](./review-usda-fdc-dining-out.md) |
| 4 | `usda-fdc-healthy-swap` | 100 | 80 | 20 | 8 | [review-usda-fdc-healthy-swap.md](./review-usda-fdc-healthy-swap.md) |
| 5 | `usda-fdc-ingredient-compliance` | 100 | 80 | 20 | 6 | [review-usda-fdc-ingredient-compliance.md](./review-usda-fdc-ingredient-compliance.md) |
| 6 | `usda-fdc-label-scanner` | 100 | 80 | 20 | 7 | [review-usda-fdc-label-scanner.md](./review-usda-fdc-label-scanner.md) |
| 7 | `usda-fdc-low-sugar-snack` | 100 | 80 | 20 | 7 | [review-usda-fdc-low-sugar-snack.md](./review-usda-fdc-low-sugar-snack.md) |
| 8 | `usda-fdc-macro-alignment` | 100 | 80 | 20 | 7 | [review-usda-fdc-macro-alignment.md](./review-usda-fdc-macro-alignment.md) |
| 9 | `usda-fdc-micronutrient-lookup` | 100 | 80 | 20 | 7 | [review-usda-fdc-micronutrient-lookup.md](./review-usda-fdc-micronutrient-lookup.md) |
| 10 | `usda-fdc-nutrient-dense-substitute` | 100 | 80 | 20 | 7 | [review-usda-fdc-nutrient-dense-substitute.md](./review-usda-fdc-nutrient-dense-substitute.md) |
| 11 | `usda-fdc-product-comparison` | 100 | 80 | 20 | 8 | [review-usda-fdc-product-comparison.md](./review-usda-fdc-product-comparison.md) |
| 12 | `usda-fdc-recipe-breakdown` | 100 | 80 | 20 | 8 | [review-usda-fdc-recipe-breakdown.md](./review-usda-fdc-recipe-breakdown.md) |
| 13 | `usda-fdc-threshold-tracking` | 100 | 80 | 20 | 8 | [review-usda-fdc-threshold-tracking.md](./review-usda-fdc-threshold-tracking.md) |

## How to review

- Open each per-skill markdown to browse all 100 questions grouped by tier.
- Questions flagged **[TEST]** are in the 20-question held-out test set (touched exactly once at graduation).
- If the questions look off-target for an ability, tell the orchestrator which skill + which tier to regenerate, or which ability-axes to adjust.
- If a skill looks correct but you want to remove it from the run (to shrink the Phase 4 budget), say so — we can update `phase-1/selected-skills.json` before launching Phase 4.
