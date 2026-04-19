# USDA FoodData Central Skills

A constellation of **13 ready-to-use skills** that wrap the [USDA FoodData Central (FDC) API](https://fdc.nal.usda.gov/api-guide). Drop them into any agent runtime that loads skills from a directory and the agent instantly gains detailed knowledge of the US government's nutrition database — over 400,000 foods with full macronutrient, micronutrient, ingredient, and label data.

Each skill was **trained and validated** against 100 held-out questions per ability. You're not getting un-tested prompt text — you're getting prompts whose refinement trajectories, held-out graduation tests, and paired diagnostics are all published in this repo.

## What superpowers does this give your agent?

With these skills enabled, your agent can answer questions like:

| Skill | Sample user question |
|---|---|
| **usda-fdc-dining-out** | *"I'm at Chipotle — what's the lowest-sodium bowl under 700 calories?"* |
| **usda-fdc-low-sugar-snack** | *"Show me 5 branded snacks with less than 5g added sugar per serving."* |
| **usda-fdc-recipe-breakdown** | *"I'm making spaghetti with 1 lb ground beef, 2 cups marinara, 1 lb pasta — what's the per-serving protein?"* |
| **usda-fdc-ingredient-compliance** | *"Is this specific brand of protein bar vegan? Any hidden soy or egg?"* |
| **usda-fdc-micronutrient-lookup** | *"I'm low on B-12 — which 5 foods have the most per serving?"* |
| **usda-fdc-macro-alignment** | *"Does a Greek yogurt and banana hit my 40g protein / 50g carbs breakfast target?"* |
| **usda-fdc-daily-intake-tally** | *"Log a cheeseburger, fries, and Coke — total calories, sodium, added sugar for the day?"* |
| **usda-fdc-nutrient-dense-substitute** | *"Dairy-free substitute for Greek yogurt with similar protein per serving?"* |
| **usda-fdc-healthy-swap** | *"Healthier 1:1 swap for regular potato chips?"* |
| **usda-fdc-label-scanner** | *"I have hypertension — scan this cereal box for sodium red flags."* |
| **usda-fdc-product-comparison** | *"Kind bar vs RxBar vs Clif bar — which wins on protein-per-calorie?"* |
| **usda-fdc-cart-optimization** | *"Given this grocery list totaling $47, swap 2 items to keep me under 2000mg sodium."* |
| **usda-fdc-threshold-tracking** | *"Alert me if my daily added-sugar will cross 30g based on my log so far."* |

All 13 skills hit the real FDC API (no mocked data) and cite the FDC ID + dataType in their answers so you can always verify.

## Refinement evidence

Every skill was iterated for **3 rounds** of greedy rewrites, then graduated against a held-out test set. See the aggregate improvement chart at [`aggregate-trajectories.png`](aggregate-trajectories.png), and per-skill trajectories at [`skills/<skill>/references/trajectory.png`](skills/).

Results by skill:

| Skill | Verdict | Test mean-issues | CI |
|---|---|---|---|
| usda-fdc-threshold-tracking | SHIPPED_CLEAN | 0.60 | [0.35, 0.85] |
| usda-fdc-micronutrient-lookup | SHIPPED_CLEAN | 0.70 | [0.45, 0.95] |
| usda-fdc-label-scanner | SHIPPED_CLEAN | 1.00 | [1.00, 1.00] |
| usda-fdc-product-comparison | SHIPPED_PLATEAU | 0.95 | [0.75, 1.15] |
| usda-fdc-macro-alignment | SHIPPED_PLATEAU | 1.05 | [1.00, 1.15] |
| usda-fdc-nutrient-dense-substitute | SHIPPED_PLATEAU | 1.40 | [1.15, 1.65] |
| usda-fdc-cart-optimization | SHIPPED_PLATEAU | 1.40 | [1.20, 1.65] |
| usda-fdc-recipe-breakdown | SHIPPED_PLATEAU | 1.50 | [1.10, 1.95] |
| usda-fdc-low-sugar-snack | SHIPPED_PLATEAU | 1.55 | [1.30, 1.80] |
| usda-fdc-healthy-swap | SHIPPED_PLATEAU | 2.15 | [1.85, 2.40] |
| usda-fdc-ingredient-compliance | NOT_SHIPPED | 1.10 | [0.80, 1.40] |
| usda-fdc-dining-out | NOT_SHIPPED | 1.10 | [1.00, 1.25] |
| usda-fdc-daily-intake-tally | NOT_SHIPPED | 1.65 | [1.45, 1.85] |

**Legend:** `mean-issues` is the average number of grading issues an independent counter found across 20 unseen test questions. Lower is better. `SHIPPED_CLEAN` ≤ 1.0 upper CI. `SHIPPED_PLATEAU` means improvements stopped but test score is within acceptable range. `NOT_SHIPPED` passed the test marginally — the skill still works, but extra caution is warranted.

## Setup

### Prerequisites

- An agent runtime that loads skills from a directory (one `SKILL.md` per skill with optional `references/` for supporting files)
- A free USDA FoodData Central API key (instructions below)
- ~1 minute to set up

### Step 1 — Get a free USDA FoodData Central API key

1. Go to <https://fdc.nal.usda.gov/api-key-signup>
2. Enter your name and email — no credit card, no approval wait
3. You'll receive a key immediately that looks like `aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890abcd`

**Rate limit:** 1,000 requests per hour per IP per key. One user question usually costs 1–3 API calls, so a single key comfortably handles an active conversation.

### Step 2 — Clone this repo

```bash
git clone https://github.com/dasheffie/usda-api.git
cd usda-api
```

### Step 3 — Set the API key

Pick one of:

**Option A (recommended) — environment variable:**

```bash
# macOS / Linux / Git Bash
export USDA_FDC_API_KEY=your_real_key_here

# Windows PowerShell
$env:USDA_FDC_API_KEY = "your_real_key_here"
```

**Option B — `.env` file next to the repo root:**

```bash
echo "USDA_FDC_API_KEY=your_real_key_here" > .env
# .env is gitignored so your key won't be committed
```

Every skill's SKILL.md embeds `${USDA_FDC_API_KEY}` in its curl examples, so whichever method you pick, the skills will see the key.

### Step 4 — Install the skills into your agent

Copy the skill directories into wherever your agent loads skills from. For example:

```bash
# if your agent reads skills from a user-scoped directory
cp -r skills/usda-fdc-* /path/to/your/agent/skills/

# or scope them to a single project
mkdir -p .your-agent/skills
cp -r skills/usda-fdc-* .your-agent/skills/
```

Check your agent's documentation for the exact target directory. Each skill is self-contained — one `SKILL.md` with YAML frontmatter plus an optional `references/` folder.

### Step 5 — Try it

```text
> I'm trying to hit 150g of protein today. Here's what I've eaten so far:
> 3 eggs, 1 cup oatmeal, 1 scoop whey. How much more do I need and
> suggest 3 high-protein branded snacks under 200 calories each.
```

Your agent should invoke `usda-fdc-daily-intake-tally` to compute the running protein total, then `usda-fdc-low-sugar-snack` or `usda-fdc-macro-alignment` to surface snack options — all backed by real FDC data.

## Repo layout

```
.
├── aggregate-trajectories.png          # One chart showing improvement across all 13 skills
├── skills/
│   └── usda-fdc-<ability>/
│       ├── SKILL.md                    # The prompt the agent loads (the actual skill)
│       └── references/
│           └── trajectory.png          # Per-skill refinement chart
├── LICENSE
└── README.md
```

Only `SKILL.md` and `references/` are tracked in git; training artifacts (per-round dispatches, trajectory JSONL, test results) stay local to the training machine (see `.gitignore`).

## How the skills were built

The training pipeline enforces:

1. **One ability = one skill** — endpoints and parse strategies are kept byte-identical within a skill
2. **100 stratified test questions per skill** (40 easy / 40 moderate / 20 edge), frozen before training starts
3. **Three-role grading split** — one model answers user questions, a second counts issues, a third proposes edits; roles never collapse so no model scores its own work
4. **Greedy acceptance** — every non-empty edit list is applied, then a single held-out test confirms the skill still works on unseen questions
5. **Paired diagnostic** comparing round 1 baseline vs. final SKILL.md on 20 shared questions, verifying the trajectory converged instead of drifting

This repo contains only the finished SKILL.md files and the trajectory charts — the training artifacts, API briefings, and helper scripts stay local.

## Contributing / customizing

The easiest ways to extend:

- **Change the answer style:** edit `SKILL.md` directly. The skill is just a markdown prompt; no code to rebuild.
- **Add a new ability:** fork, add `skills/your-new-skill/SKILL.md` following the existing shape (YAML frontmatter + When to Use + API Surface + Minimal Happy Path + Common Mistakes).
- **Retrain with new questions:** rerun your training pipeline of choice against the `skills/*/SKILL.md` starting point.

Pull requests welcome.

## License

MIT — see [LICENSE](LICENSE). Use, fork, remix, commercialize — the only requirement is keeping the copyright notice.

## Credits

- [USDA FoodData Central](https://fdc.nal.usda.gov/) for the data
- Trained and packaged by [David Sheffield](https://github.com/dasheffie)
