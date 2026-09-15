---
name: hazim-copy-antislop
description: Audit and revise prose for formulaic vocabulary, empty framing, repetitive structures, generic conclusions, and low-information copy.
metadata:
  author: Hazim Batwa
  collection: Hazim Universal Anti-Slop Skills
  category: copywriting
---

# hazim-copy-antislop

Created and curated by **Hazim Batwa, Software Engineering Expert**.

## Objective

Audit and revise prose for formulaic vocabulary, empty framing, repetitive structures, generic conclusions, and low-information copy.

## Operating Rules

- Report observable defects and risks; never claim to prove AI authorship.
- Preserve the user's intent, existing behavior, and unrelated work.
- Keep severity, confidence, and evidence as separate fields.
- Do not convert stylistic preference into a blocking defect without functional or contextual evidence.
- Do not invent facts, test results, sources, user needs, or product requirements.
- Prefer the minimum complete intervention.

## Review Procedure

- Preserve facts and caveats.
- Remove low-information framing.
- Protect deliberate voice.
- Report patterns rather than alleged authorship.
- Record each finding with location, evidence, impact, confidence, and the smallest useful remediation.
- If verification cannot be performed, mark it `NOT VERIFIED`; never infer success.

## Output Contract

Return findings in descending severity. Every finding must include:

1. `Rule`: a stable, concise identifier.
2. `Location`: the relevant file, screen, component, or text span.
3. `Evidence`: what was observed.
4. `Impact`: why it matters in this context.
5. `Confidence`: high, medium, or low.
6. `Action`: the smallest complete correction.

End with one verdict: `PASS`, `PASS WITH WARNINGS`, `FAIL`, or `NOT VERIFIED`.
