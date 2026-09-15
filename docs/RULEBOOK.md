# Universal Anti-Slop Rulebook

## Core decisions

1. Load only the skills relevant to the active task.
2. Do not identify a human or machine author from style signals.
3. Keep severity, confidence, evidence, and remediation separate.
4. A stylistic marker may trigger review but cannot block delivery alone.
5. Preserve user intent, facts, caveats, behavior, and unrelated work.
6. Prefer the minimum complete intervention.
7. Record failed, skipped, and unavailable verification honestly.

## UI and visual design

- Reject nested containers that add no grouping, interaction, or hierarchy.
- Treat gradients, glass, neumorphism, bento layouts, blobs, glows, and rounded cards as techniques requiring a product-specific purpose.
- Reject visualizations that display decorative or fabricated data.
- Require each primary component to define loading, empty, error, disabled, focus, pressed, and success states where relevant.
- Test whether the design could be transferred unchanged to an unrelated product. If it could, identify what product-specific information or interaction is missing.
- Keep identity recognizable beyond the logo and accent color.
- Do not add a fake terminal, dashboard, status indicator, testimonial, or pricing emphasis merely to fill a familiar template.
- Make motion communicate state, hierarchy, causality, continuity, or feedback; otherwise remove it.

## UX and product integrity

- Name the primary user job for every screen.
- Trace a complete path from entry to completion and recovery.
- Do not expose controls that have no connected behavior.
- Do not label cached, simulated, or periodic data as live.
- Do not display metrics without a real source and definition.
- Preserve user input across recoverable failures.
- Ask only for information required at the current stage.
- Make destructive actions explicit, reversible where practical, and appropriately confirmed.

## Copywriting and voice

- Remove generic openings, self-announcing prose, canned reframes, empty conclusions, and unsupported urgency.
- Replace low-information adjectives with concrete behavior or evidence.
- Do not ban a word solely because models use it; evaluate density, context, and alternatives.
- Vary rhythm only when it improves comprehension or preserves authentic voice.
- Do not introduce spelling errors or random fragments to appear human.
- Maintain a protect list for deliberate signatures, dialect, formality, humor, and terminology.
- Compare every rewrite with its source for invented facts, false causality, stronger certainty, and lost caveats.
- Support Arabic as its own writing system and register, not as translated English syntax.

## Code completeness

- Flag TODO, FIXME, HACK, XXX, temporary, placeholder, mock, stub, and `for now` markers according to repository policy.
- Distinguish declared test fixtures from production fake data.
- Reject handlers that return success without completing the operation.
- Reject empty exception handling and fallbacks that hide failure.
- Keep comments that explain rationale, constraints, contracts, hazards, or non-obvious workarounds.
- Remove comments that merely restate syntax.
- Do not create new dependencies, files, layers, or abstractions without a current need.

## Architecture and scope

- A new abstraction needs more than one real consumer or a documented imminent requirement.
- A dependency needs a capability gap, license review, maintenance check, and cost assessment.
- Keep changes within the requested scope.
- Do not mix broad formatting, renaming, or cleanup into a functional change.
- Prefer platform and existing-project capabilities before adding packages.
- Do not introduce services, repositories, factories, event buses, or configuration frameworks as architectural decoration.

## Security and privacy

- Verify authorization separately from authentication.
- Treat client-provided identifiers as lookup inputs, not ownership proof.
- Trace sensitive data from collection through retention, logging, sharing, export, deletion, and backup.
- Keep credentials out of source, client bundles, logs, fixtures, and error messages.
- Review injection, XSS, CSRF, SSRF, redirects, path handling, uploads, and unsafe defaults where relevant.
- Scope findings to observable code or behavior and state uncertainty explicitly.

## Evidence and substance

- Deletion test: remove the span and name the information or behavior lost.
- Inversion test: negate the claim and decide whether the opposite is a plausible position.
- Specificity test: locate names, dates, constraints, measurements, observations, or product-specific examples.
- Attribution test: resolve the cited source and verify that it supports the precise claim.
- Load-bearing test: remove the wrapper, comment, or test and observe what fails.
- Stranger test: identify the fact that only a reader of the source or product context would know.

## Accessibility, mobile, and RTL

- Verify keyboard navigation, visible focus, semantic structure, labels, announcements, contrast, zoom, and reduced motion.
- Test intermediate viewport widths, not only phone and desktop endpoints.
- Account for safe areas, software keyboards, touch targets, overflow, and non-hover input.
- Handle Arabic-English mixing, numerals, punctuation, directional icons, tables, and logical alignment explicitly.
- Mirror meaning, not every coordinate.

## Testing, repositories, and release

- Exercise changed controls individually and record outcomes.
- Reject tests with empty assertions, unconditional success, mock-only behavior, or missing failure cases.
- Verify migrations, rollback, configuration, monitoring, rate limits, backups, and health signals before production claims.
- Compare PR descriptions with the actual diff.
- Use contributor metadata only as a low-confidence operational signal, never proof of low quality.
- Do not say fully tested, production ready, or everything works without recorded evidence.

## Model output

- Profile each model and version separately against a representative human corpus.
- Record corpus language, domain, date, and sampling method.
- Measure words, phrases, n-grams, structures, and repetition without collapsing them into authorship probability.
- Evaluate specificity, substance, accuracy, voice, rhythm, originality, completeness, and safety independently.
- Document throughput and quality tradeoffs for inference-time suppression or fine-tuning.
