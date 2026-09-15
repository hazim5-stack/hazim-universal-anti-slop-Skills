#!/usr/bin/env python3
"""Behavior tests for the deterministic scanner created for Hazim Batwa."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from hazim_antislop import load_rules, scan_text


class ScannerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rules = load_rules(ROOT / "registry" / "rules.json")

    def test_detects_unfinished_code(self) -> None:
        findings = scan_text("def send():\n    # TODO: connect the provider\n    raise NotImplementedError\n", "sample.py", self.rules, "code")
        ids = {finding.rule for finding in findings}
        self.assertIn("code.placeholder.todo", ids)
        self.assertIn("code.fake.not-implemented", ids)

    def test_detects_formulaic_copy(self) -> None:
        findings = scan_text("In today's fast-paced world, unlock the power of better workflows.", "draft.md", self.rules, "copy")
        ids = {finding.rule for finding in findings}
        self.assertIn("copy.generic.opener", ids)
        self.assertIn("copy.marketing.unlock", ids)

    def test_does_not_label_authorship(self) -> None:
        registry = json.loads((ROOT / "registry" / "rules.json").read_text(encoding="utf-8"))
        messages = " ".join(rule["message"].lower() for rule in registry["rules"])
        self.assertNotIn("written by ai", messages)
        self.assertNotIn("ai-generated", messages)

    def test_clean_text_passes(self) -> None:
        findings = scan_text("The retry limit is three because the provider rejects a fourth request within sixty seconds.", "clean.md", self.rules, "copy")
        self.assertEqual([], findings)


if __name__ == "__main__":
    unittest.main()
