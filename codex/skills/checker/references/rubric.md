# Checker Rubric

Score from evidence only. Unknown or unverified work receives no credit for the affected criterion.

## Weights

| Category | Weight | Award points for |
|---|---:|---|
| Correctness | 30 | Implements the intended behavior; handles important edge cases; no contradicted claims. |
| Goal fit | 15 | Addresses all requested deliverables and constraints without off-scope churn. |
| Evidence quality | 15 | Uses primary sources, cites file/line/command/rule evidence, separates fact from inference. |
| Validation | 15 | Runs or verifies relevant tests/checks; explains coverage and gaps. |
| Maintainability | 10 | Fits existing conventions, avoids needless abstraction, keeps changes scoped. |
| Safety | 10 | Protects user work, avoids destructive actions, checks security/regression risk. |
| Communication | 5 | Clear verdict, actionable findings, confidence calibrated to evidence. |

Total: 100.

## Verdict Gates

- `GO`: 90-100, no P0/P1 findings, relevant validation exists, and remaining risks are minor.
- `HOLD`: 70-89, or any missing verification that matters, or unresolved P2 findings.
- `ABORT`: below 70, any P0/P1 blocker, contradicted core claim, unsafe action, or clear goal mismatch.

Caps override the raw score:

- Any P0 or destructive/security blocker caps score at 49.
- Any P1 correctness blocker caps score at 69.
- Any unresolved P2 finding caps score at 89.
- Any unverified assumption that affects correctness, safety, or goal fit caps score at 89.
- High-risk change with no relevant validation caps score at 79.
- No relevant validation for the central claim caps score at 89.
- Missing primary evidence for the central claim caps score at 84.

## Calibration Rules

- Do not give validation points for tests that were merely suggested.
- Do not give evidence points for unsourced summaries from another agent unless the command, output, or artifact is available.
- Do not penalize unrelated pre-existing issues except when they block the requested work or were made worse.
- Prefer `HOLD` over `GO` when the only support is plausibility.
- Prefer concise findings over exhaustive style notes. Minor style issues should not dominate the score.

## Bias Audit

State the review lens and one likely bias:

- **Anchoring**: trusting the first explanation or prior session memory too much.
- **Style preference**: treating personal taste as correctness.
- **Tool optimism**: assuming a command passed without seeing exit status/output.
- **Scope drift**: reviewing adjacent work more harshly than the requested deliverable.
- **Confirmation**: only searching for evidence that supports the claimed result.

## Evidence Strength

- Strong: source line, diff hunk, exact test command with exit code, build output, official docs, log line.
- Medium: direct code inspection without execution, project convention match, reproducible grep.
- Weak: memory, paraphrase, unstated assumption, generated summary without source.
