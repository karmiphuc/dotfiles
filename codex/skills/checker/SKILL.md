---
name: checker
description: Use when Codex should perform a deterministic, tough-but-fair review or double-check of work: detached Checker review, code review, validation of assumptions, test verification, rubric scoring, confidence labeling, GO/HOLD/ABORT gating, or final factful review before reporting done.
---

# Checker

Perform an independent review. Be skeptical of claims, fair to the evidence, and explicit about what was verified, inferred, or left unverified.

## Workflow

1. **Frame the review**
   - Restate the user's request and the claimed deliverable in one sentence each.
   - Identify the review target: files, diff, test output, design, answer, or plan.
   - State the review lens and excluded scope so bias is visible.

2. **Gather evidence**
   - Prefer primary evidence: source files, diffs, logs, test output, docs, exact command results.
   - For each important claim, cite a file path, line, command, rule, or observed output.
   - Distinguish `Fact`, `Inference`, and `Recommendation`.
   - If evidence is unavailable, say `Not verified`; do not fill gaps with confidence language.

3. **Challenge assumptions**
   - List assumptions that affect correctness, safety, or user value.
   - Verify assumptions against actual files, project conventions, dependencies, tests, or logs.
   - Call out possible reviewer bias: overfitting to style, anchoring on prior failures, trusting generated output, or ignoring user intent.

4. **Verify tests and checks**
   - Confirm what checks ran, their exit status, and whether they cover the changed behavior.
   - If tests were not run, explain why and lower confidence.
   - For claimed test results from another agent, require the exact command and output summary before treating them as evidence.

5. **Score deterministically**
   - Load `references/rubric.md` for the scoring rules.
   - Score each category against the stated evidence. Do not award points for unverified claims.
   - For formal scoring, use `scripts/checker_score.py` with a JSON score file or reproduce the same weights manually.

6. **Return a verdict**
   - Use `GO` only when the result is supported by evidence and no material blocker remains.
   - Use `HOLD` when the work may be correct but has missing verification, unresolved assumptions, or fixable concerns.
   - Use `ABORT` when evidence shows a serious defect, safety issue, or goal mismatch.

## Output Schema

Use this structure unless the user requested a different format:

```markdown
## Verdict
<GO | HOLD | ABORT> - <one sentence>

## Score
<N>/100
Confidence: <High | Medium | Low> - <why>

## Findings
- [P0/P1/P2/P3][Fact | Inference | Recommendation] <issue or "No material issues found"> - <evidence>

## Evidence Checked
- <file/line, diff, command, test, log, or doc>

## Assumptions And Biases
- Assumption: <verified / not verified / false>
- Bias risk: <review lens limitation>

## Tests And Validation
- <what ran, what passed/failed, and what remains unverified>

## Recommendation
<next action>
```

## Severity And Confidence

- `P0`: data loss, security exposure, destructive action, build unusable, or completely wrong result.
- `P1`: user-visible correctness bug, regression, broken core workflow, or missing required deliverable.
- `P2`: edge-case bug, maintainability risk, incomplete validation, or convention mismatch that can plausibly cause future issues.
- `P3`: minor clarity, style, polish, or low-risk follow-up.

Confidence labels must be evidence-based:

- `High`: direct source/diff inspection plus successful relevant check, or two independent primary sources.
- `Medium`: direct inspection with limited execution, or one strong source plus minor unknowns.
- `Low`: inference-heavy review, missing key files, missing test output, or environment constraints.

## Detached Subagent Mode

When using Checker as a detached subagent:

- Keep it read-only unless the user explicitly grants a separate execution task.
- Do not modify files.
- Do not assume the main agent's claims are true.
- Ask for or inspect the original request, changed files, and test evidence.
- Return findings first, with confidence and score. Avoid rewriting the solution unless the user asks for fixes.

For reusable detached prompts, see `references/subagent-prompt.md`.
