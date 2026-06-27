---
name: writing-great-skills
description: "Reference for editing opencode skills in this repo. Covers: the no-op test, leading words (pretrained tokens), description front-loading, bucket conventions (engineering vs productivity vs misc), model-invoked vs user-invoked, and the shared GLOSSARY. Use this skill before creating, editing, or reviewing any SKILL.md in this repo."
disable-model-invocation: true
---

# Writing Great Skills

This is a **reference** for editing skills in this repo, not a
procedural workflow. Before creating or editing any `SKILL.md`, run
each section below against your draft.

---

## Voice Rules (from `skills/README.md`)

These apply to every skill in this repo. Each is a no-op test — if your
skill fails one, rewrite until it passes.

| Rule | No-op test | Pass condition |
|------|-----------|----------------|
| **Mental model first** | Does the skill lead with a checklist? | The first section after the title is philosophy, not steps. |
| **Leading words** (pretrained tokens) | Does the skill use sentences that only restate the obvious? | Every sentence uses one of: tight, red, relentless, tracer, seam, depth, loop, signal. If you can replace a sentence with "do good work", it's a no-op. |
| **No no-ops** | Can you delete a sentence and nothing changes? | Every sentence changes agent behaviour vs default. Cut any sentence that says what was already assumed. |
| **Front-loaded description** | Can the agent tell whether to invoke this skill from the first 5 words of the description? | First 5 words are the invocation trigger — not context or praise. |
| **Single source of truth** | Does the same fact appear in two places? | Every fact lives in one file; all other references link to it. |
| **Disable model invocation on user-invoked skills** | Is this a user-invoked wrapper without `disable-model-invocation: true`? | Add `disable-model-invocation: true` to the frontmatter. |

---

## Bucket Conventions

| Bucket | When to put a skill here | Model-invoked? | Example |
|--------|--------------------------|----------------|---------|
| `engineering/` | Code work: debugging, testing, design, validation | Usually yes — model detects when to fire | `dblcheck`, `tdd`, `feedback-loop`, `codebase-design` |
| `productivity/` | Non-code workflows: planning, interviewing, handoff | Usually user-invoked | `grilling`, `handoff`, `adopt-skills`, `grill-me` |
| `misc/` | Rarely used, experimental, or meta-skills about editing skills | User-invoked | This one |

Rules:
- A model-invoked skill belongs in `engineering/` unless it's clearly
  non-code (e.g. `grilling` is productivity even though agents invoke
  it).
- A user-invoked wrapper belongs in `productivity/` alongside the
  skill it wraps.
- New buckets require updating `skills/README.md` and the
  `bootstrap.sh` install path.

---

## Description Trade-offs

The description field in frontmatter determines when the agent invokes
the skill (model-invoked) or whether the user sees it in listings
(user-invoked).

### Model-invoked description

Must be a single sentence that leads with the strongest invocation
trigger. Example from `feedback-loop`:

> Build a tight, deterministic, red-capable feedback loop before forming hypotheses. Phase 1 of disciplined debugging: if you don't have a loop that goes red on THIS bug, no amount of hypothesising will save you.

This works because:
1. First words are action-oriented ("Build a tight...")
2. Contains leading words (tight, deterministic, red-capable)
3. Tells the agent *when* to invoke (Phase 1, before forming hypotheses)
4. Tells the agent *why* it matters (no loop = no amount of hypothesising saves you)

### User-invoked description

Must tell the user what they're getting, in their language. Example
from `handoff`:

> Compact the current conversation into a handoff document for another agent to pick up. Redacts secrets.

No invocation scenario — the user decides when to run it.

### Common description issues

| Issue | Example | Fix |
|-------|---------|-----|
| Context before trigger | "A skill for..." → delete this prefix | Lead with the verb |
| Passive voice | "Is used when..." → "Use when..." | Active voice |
| Vague trigger | "Helps with code quality" → no agent fires | "Mental model for validating agent work before reporting done" |
| No exclusion | Implicitly fires on everything | Add "Do NOT invoke for..." or narrow the description |
| Jargon from the wrong domain | "Use when refactoring ViewControllers" (in a general skill) | Use domain-agnostic leading words |

---

## GLOSSARY

Terms shared across skills in this repo. Keep this list in sync when
adding a new leading word or concept.

| Term | Meaning | Used by |
|------|---------|---------|
| **Tight loop** | A detect-terminate loop that runs in seconds, is deterministic (same input → same verdict), and goes red on *this specific bug* before you fix it. | `feedback-loop` |
| **Red-capable** | A check that can *fail* on the current bug. Not a smoke test — a test that asserts the exact symptom the user reported. | `feedback-loop`, `dblcheck` |
| **Tracer bullet** | The first vertical slice through the system: one test → one implementation → repeat. Proves the path works end-to-end before adding more behaviour. | `tdd` |
| **Deep module** | A module with a small interface (few functions, few parameters) and deep implementation (lots of logic behind that interface). Opposite: shallow module with a big interface and trivial implementation. | `codebase-design`, `tdd` |
| **Seam** | A point in the code where you can change behaviour without modifying the source in that place. The primary seam is the public interface; dependency injection and test doubles create seams at module boundaries. | `codebase-design`, `tdd` |
| **Deterministic** | Same input → same output (exit code, stdout, side effects). No time dependence, randomness, or unstated env. | `dblcheck`, `feedback-loop` |
| **No-op test** | For any sentence in a skill description: if deleting it does not change agent behaviour, it's a no-op. Delete it. | This skill |

---

## When to use each description format

| Format | When | Example |
|--------|------|---------|
| One-liner + context | Most skills | "Build a tight feedback loop before forming hypotheses." |
| Problem → solution | The default behaviour is wrong and the skill overrides it | "Agents default to confident prose. This skill enforces Facts over claims." |
| Invocation list | The user must decide when to invoke | "Use when: you want to open issues, triage a queue, write a PRD, or QA a plan." |
| Exclusion list | The agent invokes on too many tasks | "Do NOT invoke for trivial one-liners or pure-opinion responses." |

---

## Reference files

- `skills/README.md` — bucket index, voice rules, single source of
  truth for conventions
- Existing skills under `engineering/` and `productivity/` — style
  examples; read the most recently written one first
- `bootstrap.sh` — install path for skills into `~/.codex/skills/`
- Matt Pocock's `writing-great-skills` — source material for the
  leading-words and no-op-test concepts used here
