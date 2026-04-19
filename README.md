# USDA FoodData Central Skills for Claude

A constellation of **13 ready-to-use [Claude Code](https://claude.com/claude-code) skills** that wrap the [USDA FoodData Central (FDC) API](https://fdc.nal.usda.gov/api-guide). Drop them into any Claude-powered agent and it instantly gains detailed knowledge of the US government's nutrition database — over 400,000 foods with full macronutrient, micronutrient, ingredient, and label data.

Each skill was **trained and validated** against 100 held-out questions per ability using the [api-skill-builder](https://github.com/anthropics/skills) meta-protocol. You're not getting un-tested prompt text — you're getting prompts whose refinement trajectories, Phase 6 graduation tests, and Phase 8a paired diagnostics are all published in this repo.

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

Every skill was iterated for **3 rounds** of greedy rewrites (Hackathon Mode), then graduated against a held-out test set. See the aggregate improvement chart at `claude/aggregate-trajectories.png`, and per-skill trajectories at `claude/skills/<skill>/references/trajectory.png`.

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

**Legend:** `mean-issues` is the average number of grading issues the Opus counter found across 20 unseen test questions. Lower is better. `SHIPPED_CLEAN` ≤ 1.0 upper CI. `SHIPPED_PLATEAU` means improvements stopped but test score is within acceptable range. `NOT_SHIPPED` passed the test marginally — the skill still works, but extra caution is warranted.

## Setup

### Prerequisites

- [Claude Code](https://claude.com/claude-code) installed — or any agent that loads skills from a directory
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

### Step 4 — Install the skills into Claude Code

Copy the skills into your Claude Code user skills directory:

```bash
# macOS / Linux
cp -r claude/skills/usda-fdc-* ~/.claude/skills/

# Windows (PowerShell)
Copy-Item -Recurse claude\skills\usda-fdc-* $env:USERPROFILE\.claude\skills\
```

Or, if you want them scoped to just one project:

```bash
mkdir -p .claude/skills
cp -r claude/skills/usda-fdc-* .claude/skills/
```

That's it. Next time you start a Claude Code session, the `/skills` list will include all 13 `usda-fdc-*` skills, and Claude will auto-discover them when the conversation touches nutrition questions.

### Step 5 — Try it

```text
> I'm trying to hit 150g of protein today. Here's what I've eaten so far:
> 3 eggs, 1 cup oatmeal, 1 scoop whey. How much more do I need and
> suggest 3 high-protein branded snacks under 200 calories each.
```

Claude should invoke `usda-fdc-daily-intake-tally` to compute the running protein total, then `usda-fdc-low-sugar-snack` or `usda-fdc-macro-alignment` to surface the snack options — all backed by real FDC data.

## Repo layout

```
claude/
├── aggregate-trajectories.png          # One chart showing improvement across all 13 skills
└── skills/
    └── usda-fdc-<ability>/
        ├── SKILL.md                    # The prompt Claude loads (the actual skill)
        └── references/
            └── trajectory.png          # Per-skill refinement chart
```

Only `SKILL.md` and `references/` are tracked in git; each skill's `eval/`, `runs/`, and per-round artifacts stay local to the training machine (see `.gitignore`).

## How the skills were built

The training pipeline is the open-source [api-skill-builder](https://github.com/anthropics/skills) meta-skill (v3.0), which enforces:

1. **One ability = one skill** — endpoints and parse strategies are kept byte-identical within a skill
2. **100 stratified test questions per skill** (40 easy / 40 moderate / 20 edge), frozen before training starts
3. **Three-role subagent split** — Haiku answers user questions, Opus counts issues, Opus proposes edits; roles never collapse so no model scores its own work
4. **Hackathon Mode greedy acceptance** — every non-empty edit list is applied, then a single held-out test at Phase 6 confirms the skill still works on unseen questions
5. **Paired Wilcoxon diagnostic (Phase 8a)** comparing round 1 baseline vs. final SKILL.md on 20 shared questions, to verify the trajectory actually converged instead of drifting

This repo contains only the finished SKILL.md files and the trajectory charts — the training artifacts, API briefings, and helper scripts stay local.

## Contributing / customizing

The easiest way to extend:

- **Change the answer style:** edit `SKILL.md` directly. The skill is just a markdown prompt; no code to rebuild.
- **Add a new ability:** fork, add `claude/skills/your-new-skill/SKILL.md` following the existing shape (YAML frontmatter + When to Use + API Surface + Minimal Happy Path + Common Mistakes).
- **Retrain with new questions:** install [api-skill-builder](https://github.com/anthropics/skills) and rerun Phase 3 onward in a worktree.

Pull requests welcome.

## License

MIT — see [LICENSE](LICENSE). Use, fork, remix, commercialize — the only requirement is keeping the copyright notice.

## Credits

- [USDA FoodData Central](https://fdc.nal.usda.gov/) for the data
- [Claude Code](https://claude.com/claude-code) / [Anthropic](https://anthropic.com) for the skill-loading runtime and the `api-skill-builder` meta-skill
- Trained and packaged by [David Sheffield](https://github.com/dasheffie)
