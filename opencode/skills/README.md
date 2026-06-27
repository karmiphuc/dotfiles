# opencode Skills

This directory contains **generic, portable** mental models and scripts for validating agent work.

## Layout

```
skills/
  engineering/          # Mental models for code work
    dblcheck/           # Facts / Inferences / Biases + deterministic checks
    tdd/                # Vertical-slices red-green-refactor
    feedback-loop/      # Build a red-capable deterministic loop before hypothesising
    codebase-design/    # Deep modules: small interface, deep implementation
  productivity/         # Mental models for non-code workflows
    grilling/           # One-question-at-a-time interview loop
    grill-me/           # User-invoked wrapper for grilling
    grill-with-docs/    # Grilling + ADR/glossary output
    handoff/            # Compact session into portable handoff doc
    adopt-skills/       # Per-repo bootstrap (issue tracker + domain vocab + enabled skills)
  misc/                 # Rarely used / experimental
    writing-great-skills/ # Reference for editing skills in this repo
```

## Why separate "skills/" in dotfiles

- Skills are **project-agnostic**. Putting them in a project repo means reinventing them per project. Putting them in dotfiles means they follow you across machines and projects.
- `bootstrap.sh` mirrors `dotfiles/opencode/skills/` into `~/.codex/skills/` so Codex CLI picks them up alongside the bundled ones.
- Each project **adopts** a skill by running its bootstrap, which sets up the project's checks dir + log dir + project constants.

## Adding a skill to a project

Read the skill's `references/adopt-this-skill.md` (if present) or its `SKILL.md` for the bootstrap steps. Most skills are **mental models** — they apply by default once the skill is loaded in the agent.

## Voice rules (apply to every skill)

- **Mental model first** — every skill leads with a mental model, not a checklist
- **Leading words** — use pretrained tokens (tight, red, relentless, tracer, seam, depth) rather than restatements
- **No no-ops** — every sentence must change behaviour versus default; run the no-op test on each sentence
- **Front-load the description** — the first words of the description are the invocation triggers
- **Single source of truth** — one authoritative place per meaning; changing behaviour is a one-place edit
- **Disable model invocation on user-invoked skills** — `disable-model-invocation: true` on wrapper skills