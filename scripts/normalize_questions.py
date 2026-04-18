"""Normalize questions_raw.json files to the schema freeze_splits.py requires.

Required schema:
  top-level: skill_name, generated_at, questions
  per question: id, tier, text, expected_endpoints, expected_fields, ability_tags
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

# Per-skill defaults when the generator forgot to emit expected_endpoints / expected_fields.
# Keys are skill directory names (which match the frontmatter `name` in each SKILL.md).
SKILL_DEFAULTS: dict[str, dict[str, list[str]]] = {
    "usda-fdc-ingredient-compliance": {
        "expected_endpoints": ["GET /food/{fdcId}"],
        "expected_fields": ["ingredients", "dataType"],
    },
    "usda-fdc-micronutrient-lookup": {
        "expected_endpoints": ["GET /food/{fdcId}"],
        "expected_fields": ["foodNutrients", "servingSize", "labelNutrients"],
    },
    "usda-fdc-macro-alignment": {
        "expected_endpoints": ["GET /food/{fdcId}"],
        "expected_fields": ["foodNutrients", "servingSize", "labelNutrients"],
    },
    "usda-fdc-label-scanner": {
        "expected_endpoints": ["GET /food/{fdcId}"],
        "expected_fields": ["labelNutrients", "foodNutrients", "servingSize", "ingredients"],
    },
    "usda-fdc-dining-out": {
        "expected_endpoints": ["POST /foods/search", "GET /food/{fdcId}"],
        "expected_fields": ["description", "brandOwner", "labelNutrients", "foodNutrients"],
    },
    "usda-fdc-low-sugar-snack": {
        "expected_endpoints": ["POST /foods/search", "GET /food/{fdcId}"],
        "expected_fields": ["description", "labelNutrients", "foodNutrients"],
    },
    "usda-fdc-nutrient-dense-substitute": {
        "expected_endpoints": ["POST /foods/search"],
        "expected_fields": ["description", "foodNutrients", "foodCategory"],
    },
    "usda-fdc-healthy-swap": {
        "expected_endpoints": ["GET /food/{fdcId}", "POST /foods/search"],
        "expected_fields": ["ingredients", "labelNutrients", "brandedFoodCategory"],
    },
    "usda-fdc-recipe-breakdown": {
        "expected_endpoints": ["GET /foods/search", "POST /foods"],
        "expected_fields": ["foodNutrients", "servingSize"],
    },
    "usda-fdc-daily-intake-tally": {
        "expected_endpoints": ["POST /foods"],
        "expected_fields": ["foodNutrients", "labelNutrients", "servingSize"],
    },
    "usda-fdc-cart-optimization": {
        "expected_endpoints": ["POST /foods", "POST /foods/search"],
        "expected_fields": ["labelNutrients", "foodNutrients", "brandedFoodCategory"],
    },
    "usda-fdc-product-comparison": {
        "expected_endpoints": ["POST /foods"],
        "expected_fields": ["labelNutrients", "servingSize", "description"],
    },
    "usda-fdc-threshold-tracking": {
        "expected_endpoints": ["GET /food/{fdcId}"],
        "expected_fields": ["labelNutrients", "foodNutrients", "servingSize"],
    },
}


def normalize(path: Path) -> tuple[int, list[str]]:
    skill_name = path.parent.parent.name  # <skill>/eval/questions_raw.json
    defaults = SKILL_DEFAULTS.get(skill_name)
    if not defaults:
        raise SystemExit(f"no defaults for skill {skill_name}")

    data = json.loads(path.read_text(encoding="utf-8"))

    # Top-level: skill_name + generated_at
    if "skill_name" not in data:
        if "skill" in data:
            data["skill_name"] = data.pop("skill")
        else:
            data["skill_name"] = skill_name
    if "generated_at" not in data:
        data["generated_at"] = data.pop("generated", datetime.now(timezone.utc).isoformat())

    fixes: list[str] = []
    qs = data.get("questions", [])
    if len(qs) != 100:
        raise SystemExit(f"{skill_name}: expected 100 questions, got {len(qs)}")

    for q in qs:
        if "tier" not in q:
            for alt in ("difficulty", "level"):
                if alt in q:
                    q["tier"] = q.pop(alt)
                    break
            else:
                raise SystemExit(f"{skill_name} q{q.get('id')}: no tier/difficulty field")
        if "text" not in q:
            for alt in ("question", "prompt"):
                if alt in q:
                    q["text"] = q.pop(alt)
                    break
            else:
                raise SystemExit(f"{skill_name} q{q.get('id')}: no text/question field")
        if not q.get("expected_endpoints"):
            q["expected_endpoints"] = list(defaults["expected_endpoints"])
            fixes.append(f"q{q['id']}: injected expected_endpoints default")
        if not q.get("expected_fields"):
            q["expected_fields"] = list(defaults["expected_fields"])
        if not q.get("ability_tags"):
            raise SystemExit(f"{skill_name} q{q.get('id')}: missing ability_tags (required)")

        # Drop generator-extra fields that aren't in the canonical schema
        for extra in ("product", "condition", "expected_verdict", "brand", "nutrient",
                      "foods", "target", "goal", "meta", "ingredients"):
            q.pop(extra, None)

    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return len(qs), fixes


def main() -> int:
    root = Path(r"C:/Users/dshef/Repos/usda-api/claude/skills")
    for skill_dir in sorted(root.iterdir()):
        if not skill_dir.is_dir():
            continue
        raw = skill_dir / "eval" / "questions_raw.json"
        if not raw.exists():
            print(f"SKIP {skill_dir.name}: no questions_raw.json")
            continue
        n, fixes = normalize(raw)
        extra = f"  ({len(fixes)} injections)" if fixes else ""
        print(f"OK  {skill_dir.name}: {n} questions{extra}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
