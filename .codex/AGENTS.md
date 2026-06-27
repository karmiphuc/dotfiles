# Global Codex Instructions

## Operating Style
- Be direct, pragmatic, and implementation-oriented.
- Inspect the relevant repository context before proposing architecture or edits.
- Prefer small, focused changes that match existing project conventions.
- Do not revert, overwrite, or clean up unrelated user work.
- Surface important assumptions, tradeoffs, blockers, and verification results concisely.

## Context Files
- Read `opinions.md` for non-trivial implementation, design, or review work.
- Read the relevant section of `voices.md` when a specialist lens applies.
- Do not read every voice by default; keep the working context small.

Voice routing:
- `voices.md#architect`: new abstractions, module boundaries, APIs, data models.
- `voices.md#reviewer`: reviews, bug fixes, risky diffs, final self-checks.
- `voices.md#operator`: commands, installs, migrations, deployment, git, cleanup.
- `voices.md#security`: auth, secrets, permissions, network, user data, dependencies.

## Implementation Discipline
- Solve only the requested problem; do not add speculative features, abstractions, configurability, or broad refactors.
- Touch only files and lines needed for the task.
- Match local style even when you would choose a different style.
- Remove only unused code introduced by your own changes.
- Mention unrelated issues when useful, but do not fix them unless asked.
- If multiple interpretations materially affect the solution, ask before editing. Otherwise, state the assumption and proceed.

## Tooling
- Use `rg` / `rg --files` for search when available.
- Use native project tooling for installs, builds, tests, linting, and formatting.
- Identify relevant files and current patterns before editing.
- Use `apply_patch` for manual edits where practical.
- Avoid destructive commands unless explicitly requested.

## Verification
- Define success criteria for non-trivial tasks before implementing.
- Run the narrowest useful checks after changes.
- For bug fixes, prefer reproducing the failure first when practical.
- For frontend changes, verify the rendered UI in a browser when a local target is available.
- If checks cannot run, state exactly why and what remains unverified.
- Before reporting done, review the diff for scope creep, regressions, and stray edits.

## Git
- Treat the worktree as shared.
- Check status before large edits or commits.
- Do not amend, rebase, reset, clean, force-push, delete branches, or discard changes without explicit instruction.

## Defaults
- Prefer simplicity over flexibility.
- Prefer concrete implementation over advice-only responses.
- Default to ASCII in new files unless Unicode is already used or required.
- Keep comments sparse and useful.

## Skills
This section documents the mental models and scripts available in the
dotfiles skills directory. All skills under `~/opencode/skills/` are
mirrored into `~/.codex/skills/` by `bootstrap.sh`.

### Engineering skills (model-invoked unless noted)

| Skill | Type | Invocation | Description |
|-------|------|------------|-------------|
| `dblcheck` | mental model | Auto (non-trivial tasks) | Facts / Inferences / Biases + deterministic checks; trigger via `/dblcheck` |
| `tdd` | mental model | Auto (test-first requests) | Vertical-slices red-green-refactor; one test → one implementation |
| `feedback-loop` | mental model | Auto (debugging) | Build a red-capable deterministic loop before hypothesising |
| `codebase-design` | mental model | Auto (new abstractions) | Deep modules vocabulary (small interface, deep implementation) |

### Productivity skills (user-invoked unless noted)

| Skill | Type | Invocation | Description |
|-------|------|------------|-------------|
| `grilling` | mental model | Auto (planning/design) | One-question-at-a-time interview loop |
| `grill-me` | wrapper | User-invoked | Runs `/grilling`; disable-model-invocation |
| `handoff` | script | User-invoked | Compact session into portable handoff doc; redacts secrets |
| `adopt-skills` | script | User-invoked | Per-repo bootstrap (issue tracker + domain vocab + enabled skills) |
| `grill-with-docs` | wrapper | User-invoked | Grilling + ADR/glossary output |

### Misc skills (user-invoked)

| Skill | Type | Invocation | Description |
|-------|------|------------|-------------|
| `writing-great-skills` | reference | User-invoked | Editing guidelines for skills in this repo |

### Applying skills

- Mental models (model-invoked) fire automatically when the agent
  detects the relevant scenario. No user action needed.
- Wrapper skills and scripts (user-invoked) require the user to name
  them. They have `disable-model-invocation: true` in frontmatter.
- Before reporting work done, always run `/dblcheck` on non-trivial
  tasks.
- For project bootstrap: run `adopt-skills` (sets up
  `.opencode/issue-tracker.md`, `.opencode/domain.md`,
  `.opencode/enabled-skills.md`).

### Daily log location (project-relative)

`.opencode/logs/YYYY-MM-DD.md`
