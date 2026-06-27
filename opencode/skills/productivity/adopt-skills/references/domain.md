# Domain docs

## Layout

`<single-context | multi-context>`

## Context file

| Aspect | Value |
|--------|-------|
| Path | `<path to CONTEXT.md or CONTEXT-MAP.md>` |
| Format | Markdown |
| Purpose | Domain vocabulary, architecture overview, key assumptions |

### Consumer rules

These skills read the context file before doing work. They do not
modify it.

| Skill | Reads | Why |
|-------|-------|-----|
| `feedback-loop` | `CONTEXT.md` | Use domain language when describing the bug; understand which seams are relevant |
| `tdd` | `CONTEXT.md` | Match test names and interface vocabulary to project domain language |
| `codebase-design` | `CONTEXT.md` + `docs/adr/` | Understand module boundaries and past architectural decisions |

## ADR directory

| Aspect | Value |
|--------|-------|
| Path | `<path to docs/adr/>` |
| Format | `<NNN>-<title>.md` (Markdown, ADR template) |

### Consumer rules

These skills read ADRs before proposing changes. They do not modify
ADRs unless explicitly asked.

| Skill | Reads | Why |
|-------|-------|-----|
| `codebase-design` | All ADRs | Understand past decisions before proposing new ones |
| `tdd` | ADRs in the area being touched | Respect previously agreed design constraints |
| `feedback-loop` | ADRs in the area being debugged | Understand why the code is the way it is |

## Glossary

| Aspect | Value |
|--------|-------|
| Path | `GLOSSARY.md` or `<none>` |
| Format | Markdown table |
