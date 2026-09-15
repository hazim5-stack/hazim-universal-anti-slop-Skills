#!/usr/bin/env python3
"""Validate repository invariants for Hazim Universal Anti-Slop Skills."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NAME_PATTERN = re.compile(r"^[a-z0-9-]{1,64}$")


def main() -> int:
    errors: list[str] = []
    registry = json.loads((ROOT / "registry" / "skills.json").read_text(encoding="utf-8"))
    registered = {}
    for category, data in registry["categories"].items():
        for name, description in data["skills"].items():
            registered[name] = category
            if not NAME_PATTERN.fullmatch(name):
                errors.append(f"Invalid skill name: {name}")
            if len(description) < 40:
                errors.append(f"Description is not discriminating: {name}")

    discovered = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
    if discovered != set(registered):
        errors.append(f"Registry mismatch: missing={sorted(set(registered) - discovered)}, extra={sorted(discovered - set(registered))}")

    for name, category in registered.items():
        skill_path = ROOT / "skills" / name / "SKILL.md"
        content = skill_path.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            errors.append(f"Missing frontmatter: {name}")
        if f"name: {name}" not in content:
            errors.append(f"Incorrect frontmatter name: {name}")
        if f"category: {category}" not in content:
            errors.append(f"Incorrect category: {name}")
        if "Hazim Batwa" not in content:
            errors.append(f"Missing authorship: {name}")
        if re.search(r"\[TODO\]|<TODO>|REPLACE_ME|Example resource content", content):
            errors.append(f"Unfinished marker in skill: {name}")

    for preset_path in (ROOT / "presets").glob("*.json"):
        preset = json.loads(preset_path.read_text(encoding="utf-8"))
        unknown = set(preset["skills"]) - set(registered)
        if unknown:
            errors.append(f"Unknown skills in {preset_path.name}: {sorted(unknown)}")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"Validated {len(registered)} skills and {len(list((ROOT / 'presets').glob('*.json')))} presets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
