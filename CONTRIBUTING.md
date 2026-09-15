# Contributing

Contributions should improve a demonstrated failure without turning every preference into a universal prohibition.

## Rule requirements

Every new rule must include:

- A stable identifier.
- A narrow description.
- At least one positive fixture.
- At least one counterexample.
- A severity and confidence policy.
- A suppression or configuration path for deterministic rules.
- A review date when the signal may age.

Style-only signals must not fail a delivery gate on their own. Prefer revising an existing rule to adding an overlapping rule.

## Language

Repository code, comments, documentation, configuration keys, and test messages must be written in English. Fixtures may contain other languages when a rule is explicitly testing multilingual content.

## Authorship

Preserve the project attribution: **Created and curated by Hazim Batwa, Software Engineering Expert.** Contributors retain credit through Git history and release notes.
