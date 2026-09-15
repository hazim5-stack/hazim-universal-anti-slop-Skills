#!/usr/bin/env python3
"""Deterministic anti-slop scanner created for Hazim Batwa.

The scanner reports inspectable signals and defects. It never attempts to
identify whether a human or a model authored the input.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RULES = ROOT / "registry" / "rules.json"


@dataclass(frozen=True)
class Finding:
    rule: str
    severity: str
    path: str
    line: int
    column: int
    message: str
    evidence: str


def load_rules(path: Path) -> list[dict[str, str]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload["rules"]


def line_column(text: str, offset: int) -> tuple[int, int]:
    line = text.count("\n", 0, offset) + 1
    previous = text.rfind("\n", 0, offset)
    column = offset + 1 if previous < 0 else offset - previous
    return line, column


def scan_text(text: str, display_path: str, rules: Iterable[dict[str, str]], domain: str) -> list[Finding]:
    findings: list[Finding] = []
    for rule in rules:
        if domain != "all" and rule["domain"] != domain:
            continue
        expression = re.compile(rule["pattern"], re.IGNORECASE | re.MULTILINE)
        for match in expression.finditer(text):
            line, column = line_column(text, match.start())
            evidence = match.group(0).replace("\n", " ")[:120]
            findings.append(Finding(rule["id"], rule["severity"], display_path, line, column, rule["message"], evidence))
    return findings


def iter_files(paths: list[str]) -> Iterable[Path]:
    ignored = {".git", "node_modules", "dist", "build", ".venv", "venv"}
    for raw in paths:
        path = Path(raw)
        if path.is_file():
            yield path
            continue
        if path.is_dir():
            for candidate in path.rglob("*"):
                if candidate.is_file() and not any(part in ignored for part in candidate.parts):
                    yield candidate


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan code or prose for deterministic anti-slop findings.")
    parser.add_argument("paths", nargs="+", help="Files or directories to scan")
    parser.add_argument("--domain", choices=("all", "code", "copy"), default="all")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES)
    parser.add_argument("--fail-on", choices=("none", "error", "warning", "signal"), default="error")
    args = parser.parse_args()

    rules = load_rules(args.rules)
    findings: list[Finding] = []
    for path in iter_files(args.paths):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        findings.extend(scan_text(text, str(path), rules, args.domain))

    if args.format == "json":
        print(json.dumps({"findings": [asdict(item) for item in findings]}, indent=2))
    else:
        for item in findings:
            print(f"{item.path}:{item.line}:{item.column}: {item.severity} {item.rule}: {item.message} [{item.evidence}]")
        print(f"Hazim Anti-Slop: {len(findings)} finding(s)")

    if args.fail_on == "none":
        return 0
    ranks = {"signal": 1, "warning": 2, "error": 3}
    threshold = ranks[args.fail_on]
    return 1 if any(ranks[item.severity] >= threshold for item in findings) else 0


if __name__ == "__main__":
    sys.exit(main())
