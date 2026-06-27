---
name: dblcheck
description: "Mental model for validating agent work before reporting done. Enforces three rules: (1) every claim must be either a Fact (file/line/command/test output) or an explicit Inference (marked and reasoned); (2) write deterministic checks (tests, scripts) and run them — never trust a verbal claim that a check 'would pass'; (3) list and counter your own biases (overconfidence, anchoring on prior failures, pattern-matching from training data). Trigger by saying '/dblcheck' or before declaring any non-trivial task done."
---

# Double-check (dblcheck)

A mental model, not a checklist. Three rules that change how you think
before reporting work as done.

> **If you remember nothing else**: every claim must be a Fact with
> evidence, or an Inference marked as such. If you can't tell which it
> is, you don't know enough to report done.

---

## Rule 1 — Facts, not claims

Every sentence in your report must be either:

| Kind | What it looks like | How to mark it |
|---|---|---|
| **Fact** | A specific thing you observed: a file path, a line number, a command's exit code, a test result, a screenshot, an API response. | Cite the source inline: `file:line`, `cmd: output`, `test: passed in 1.2s`. |
| **Inference** | A conclusion drawn from facts, plus the reasoning. Includes "I think", "probably", "should", "likely". | Lead with `[Inference]` and give the reasoning chain in one line. |
| **Unknown** | You don't have evidence either way. | Say `not verified` and stop. Do not hedge with confident-sounding language. |

### Why this matters

Agents default to **confident prose**. They produce sentences that
*read* like facts but were never observed. The reader can't tell
which is which. The user makes a decision based on a sentence that
might be a hallucination wearing a colon between two pieces of
evidence.

### Pattern to use in reports

```
**Goal**: User asked to verify X.
**What I observed** (Facts):
  - ran `pytest tests/test_x.py::test_y` -> 3 passed, 0 failed (42ms)
  - file src/x.py:117 imports `module.Z` (verified by `grep -n "^import" src/x.py`)
  - exit code 0 on `make build`

**What I concluded** (Inferences):
  - [Inference] X is fixed because the failing test now passes and the
    import resolves; confidence: medium (no integration test covers
    the downstream consumer).
  - [Inference] Safe to deploy; however the regression-test gap is real.

**What I did not verify**:
  - downstream consumers of module.Z (no test coverage)
  - production load behavior under concurrent calls
```

Notice: facts are first, inferences are tagged, gaps are named. The
reader can audit each claim by following the citation.

---

## Rule 2 — Deterministic checks, not assurances

"Trust me, it works" is not evidence. An assurance that "the test
would pass" is weaker than running the test.

### What "deterministic" means

- Same input -> same output (no time, no randomness, no unstated env).
- Exit code 0 = pass, non-zero = fail. No "warnings are okay" without
  the user opting in.
- Output captured to a file or log. A test that prints "PASS" to
  stdout and returns 0 is fine; a test that "succeeded" because the
  agent saw no error in the surrounding code is not.

### The cycle you must run

1. **Hypothesize**: what would I observe if this change were correct?
   What would I observe if it were broken? Make both concrete.
2. **Write a check** that distinguishes the two. Prefer:
   - An existing test extended (cheapest).
   - A new test in the project's test framework.
   - A small script under `.opencode/checks/` that returns exit 0/1.
   - Last resort: a `grep | wc -l` or a file-existence probe. Document
     why no real test was possible.
3. **Run the check**. Capture exit code and stdout/stderr.
4. **Read the output yourself**. Do not summarize from memory. If the
   output is 200 lines long, read all 200.
5. **Update the hypothesis** if reality disagrees. Do not retrofit the
   claim to fit the output.

### Where checks live (project-agnostic)

- `<repo>/tests/` — primary test suite (language-appropriate framework)
- `<repo>/.opencode/checks/` — ad-hoc checks for things the project's
  test suite doesn't cover (linter quirks, naming conventions,
  encoding artifacts, workflow YAML schema, etc.)
- `<repo>/.opencode/logs/YYYY-MM-DD.md` — record the check + result
  per task (see references/daily-log-template.md)

### What you write checks for (not exhaustive)

- Did the file I claimed to create actually get written? (`Test-Path`,
  `wc -l`, byte size)
- Did the build succeed? (`exit 0` from `make build`, `tsc --noEmit`)
- Did the changed function still type-check?
- Does the new dependency import resolve?
- For each behavior the user asked for, is there a test that exercises
  it? If not, write one.
- For each commit message claim ("fixes #N"), is `#N` actually fixed?
- For each "I tested it locally" claim, is the test output attached?

### What does NOT count as a check

- "I read the file and it looks right."
- "The change is small so I didn't run tests."
- "I'm confident the API works."
- "The test file already exists."
- "Tests would have caught this if I'd run them."

---

## Rule 3 — Name your biases

You have predictable failure modes. Before reporting done, list them
and counter each one. This is not optional — it's how you catch what
the next two rules miss.

### Common biases to check for

| Bias | What it looks like | Counter |
|---|---|---|
| **Completion bias** | Reporting done because the change looks finished, not because it's verified. | Re-read the original request; cross off each deliverable with a Fact. |
| **Confirmation bias** | Reading test output as "passing" because you expected it to pass. | Run the test under `--tb=long` or with verbose logging. Read the assertion line, not the summary. |
| **Anchoring** | First error you saw dominates your reasoning; you stop looking after one fix. | List all symptoms from the original report; verify each is resolved. |
| **Pattern-matching** | "This looks like the kind of bug that X fixes" without checking. | Cite the actual symptom; require a Fact for each step of the fix. |
| **Trailing-confidence** | Hedging words ("probably", "should") packed into sentences that *read* as facts. | Re-read your report; any hedge belongs in `[Inference]` form, not buried in prose. |
| **Anchoring on prior failures** | "Last time this was a Y problem, so this time it's also Y" — without checking. | Force the hypothesis from the current evidence, not the prior case. |
| **Trusting the agent that came before** | "The previous agent said X, so I accept X." | Re-verify from primary sources; do not inherit inferences as facts. |
| **Reading more than is there** | Inferring structure or behavior from code you haven't run. | If you didn't run it, mark it `[Inference]` and say so explicitly. |

### Anti-patterns that hide biases

- "It works on my machine." — environment-specific and unverified.
- "Tests pass." — without counts and exit codes.
- "Looks good." — pure assertion, zero evidence.
- "Should be fine." — hedge dressed as conclusion.

---

## When to invoke dblcheck

- Before reporting any non-trivial task done.
- Before answering a factual question (verify the answer is a Fact).
- Before pushing a commit (verify the diff and the test results).
- After making a non-trivial change in a long session (catch drift).
- When the user says "are you sure?" — the answer should always cite.

## When NOT to invoke dblcheck

- For trivial one-liners ("read X for me") with zero state changes.
- For conversational responses that are pure opinion or preference.
- When the user explicitly says "skip the check, just do it."

---

## Project-specific constants

If you keep repeating "did I remember to run X?" for the same X,
add it here. Otherwise this section is empty — the rules above are
self-contained.

| Topic | Value |
|---|---|
| Test runner | `<e.g. npm test, make test, pwsh ./scripts/test.ps1>` |
| Build check | `<e.g. tsc --noEmit, go build ./..., cargo check>` |
| Lint | `<e.g. eslint ., ruff check ., pwsh -c "Invoke-ScriptAnalyzer ...">` |
| Type check | `<e.g. tsc --noEmit, mypy src, go vet ./...>` |
| Project-specific anti-patterns | `<things that always bite you in this codebase>` |

---

## Adoption

For the bootstrap (one-time, ~10 minutes) and project-local usage:

- `references/adopt-this-skill.md` — 5-step bootstrap for a new project
- `references/daily-log-template.md` — what to record in `.opencode/logs/`
- `references/check-template.sh` — minimal `.opencode/checks/` example

The mental model itself does not need a per-project override. The
constants table above is the only project-specific knob. If you find
yourself needing more than that, the rule probably isn't general — go
back and rewrite Rule 1/2/3 instead of adding knobs.