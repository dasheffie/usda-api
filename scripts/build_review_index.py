"""Write a human-readable markdown summary per skill + one aggregate index.

For each skill produces:
  phase-3/review-<skill>.md — all 100 questions, grouped easy/moderate/edge, with tags.

And one aggregate:
  phase-3/review-index.md — axis coverage table + sample 3 per tier per skill.
"""
from __future__ import annotations
import json
from pathlib import Path
from collections import Counter

ROOT = Path(r"C:/Users/dshef/Repos/usda-api")
SKILLS_DIR = ROOT / "claude" / "skills"
OUT_DIR = ROOT / "phase-3"


def render_skill(skill_dir: Path) -> tuple[str, dict[str, int]]:
    name = skill_dir.name
    q = json.loads((skill_dir / "eval" / "questions.json").read_text(encoding="utf-8"))
    questions = q["questions"]
    tag_counts = Counter()
    for item in questions:
        for t in item.get("ability_tags", []):
            tag_counts[t] += 1

    by_tier = {"easy": [], "moderate": [], "edge": []}
    for item in questions:
        by_tier[item["tier"]].append(item)

    lines = [f"# {name} — 100-question corpus\n"]
    lines.append("## Splits")
    lines.append(f"- train_ids ({len(q['train_ids'])}): `{q['train_ids']}`")
    lines.append(f"- test_ids ({len(q['test_ids'])}): `{q['test_ids']}`")
    lines.append(f"- seed: `{q['split_seed']}`  mode: `{q['mode']}`  threshold: `{q['graduation_threshold']}`")

    lines.append("\n## Ability-tag coverage\n")
    lines.append("| Tag | Count |")
    lines.append("|---|---|")
    for tag, c in tag_counts.most_common():
        lines.append(f"| `{tag}` | {c} |")

    for tier, items in by_tier.items():
        lines.append(f"\n## {tier.upper()} ({len(items)} questions, ids {items[0]['id']}–{items[-1]['id']})\n")
        for q_item in items:
            tags = ", ".join(f"`{t}`" for t in q_item.get("ability_tags", []))
            in_test = " **[TEST]**" if q_item["id"] in q["test_ids"] else ""
            lines.append(f"- **{q_item['id']:>2}.**{in_test} {q_item['text']}  \n  _tags: {tags}_")

    return "\n".join(lines) + "\n", dict(tag_counts)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summary_rows: list[tuple[str, int, int, int, int]] = []
    all_skills = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())

    for skill_dir in all_skills:
        md, tag_counts = render_skill(skill_dir)
        out = OUT_DIR / f"review-{skill_dir.name}.md"
        out.write_text(md, encoding="utf-8")
        q = json.loads((skill_dir / "eval" / "questions.json").read_text(encoding="utf-8"))
        summary_rows.append((
            skill_dir.name,
            len(q["questions"]),
            len(q["train_ids"]),
            len(q["test_ids"]),
            len(tag_counts),
        ))

    # Aggregate index
    lines = ["# Phase 3 — Question Corpus Review Index\n"]
    lines.append("Protocol: **Hackathon**. Per-skill corpus: 100 questions (40 easy / 40 moderate / 20 edge), split **80 train / 0 val / 20 test**. Train is rotated by the coverage-weighted sampler in Phase 4; val is skipped under Hackathon greedy acceptance; test is touched exactly once at Phase 6 graduation.\n")
    lines.append(f"Run parameters: `max_rounds=5`, `base_train_batch_size=20`, `decay_rate=1.0`, `graduation_threshold=1.0`.\n")
    lines.append("## Skill overview\n")
    lines.append("| # | Skill | Total | Train | Test | Axes | Review file |")
    lines.append("|---|---|---:|---:|---:|---:|---|")
    for i, (name, total, train, test, axes) in enumerate(summary_rows, 1):
        lines.append(f"| {i} | `{name}` | {total} | {train} | {test} | {axes} | [review-{name}.md](./review-{name}.md) |")

    lines.append("\n## How to review\n")
    lines.append("- Open each per-skill markdown to browse all 100 questions grouped by tier.")
    lines.append("- Questions flagged **[TEST]** are in the 20-question held-out test set (touched exactly once at graduation).")
    lines.append("- If the questions look off-target for an ability, tell the orchestrator which skill + which tier to regenerate, or which ability-axes to adjust.")
    lines.append("- If a skill looks correct but you want to remove it from the run (to shrink the Phase 4 budget), say so — we can update `phase-1/selected-skills.json` before launching Phase 4.")

    (OUT_DIR / "review-index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(all_skills)} per-skill review files + 1 aggregate index to {OUT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
