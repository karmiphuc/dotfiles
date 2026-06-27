# opencode Skills

This directory contains **generic, portable** mental models and small
scripts for validating agent work.

## Layout

```
opencode/
  README.md                            # This file
  skills/
    engineering/                       # Mental models for code work
      dblcheck/                        # Facts / Inferences / Biases + deterministic checks
        references/
          adopt-this-skill.md           # Bootstrap steps for a new project
      tdd/                             # Vertical-slices red-green-refactor
      feedback-loop/                   # Red-capable deterministic loop before hypothesising
      codebase-design/                 # Deep modules vocabulary
    productivity/                      # Mental models for non-code workflows
      grilling/                        # One-question-at-a-time interview loop
      grill-me/                        # User-invoked wrapper for grilling
      handoff/                         # Compact session into portable handoff doc
      adopt-skills/                    # Per-repo bootstrap (issue tracker + domain vocab + enabled skills)
        references/
          issue-tracker-github.md
          issue-tracker-gitlab.md
          issue-tracker-local.md
          domain.md
          enabled-skills.md
      grill-with-docs/                 # Grilling + ADR/glossary output
    misc/                              # Rarely used / experimental
      writing-great-skills/            # Reference for editing skills in this repo
  templates/                           # Seed files for ad-hoc use outside dotfiles
```

## Why separate "opencode/" in dotfiles

- Skills are **project-agnostic**. Putting them in a project repo
  means reinventing them per project. Putting them in dotfiles means
  they follow you across machines and projects.
- `bootstrap.sh` mirrors `dotfiles/opencode/skills/` into
  `~/.codex/skills/` so Codex CLI picks them up alongside the bundled
  ones.
- Each project **adopts** a skill via `adopt-skills`, which sets up
  `.opencode/issue-tracker.md`, `.opencode/domain.md`, and
  `.opencode/enabled-skills.md` in the project.

## Adding a skill to a project

Run the `adopt-skills` skill (user-invoked). It asks three questions
one at a time: issue tracker, domain docs layout, and which skills to
enable.

## Voice rules

See `skills/README.md` for the voice rules that apply to every skill
in this repo.
