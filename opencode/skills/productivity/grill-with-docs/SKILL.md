---
name: grill-with-docs
description: "Run a relentless interview on a plan or design, then write ADRs and a glossary from the session. Wraps grilling (one-question-at-a-time interview loop) with codebase-design vocabulary (deep modules, seams). User invokes; agent runs the loop and produces docs."
disable-model-invocation: true
---

# Grill with Docs

Run a `/grilling` session to sharpen a plan or design. After the
session, write an **Architecture Decision Record (ADR)** and a
**domain glossary** capturing what emerged.

## Before the session

Tell the user:

> I will ask one question at a time about the design. Answer each
> before I ask the next. When I have enough clarity, I will write
> an ADR and a glossary for this session.

## During the session

Same as `/grilling`: one question at a time. Wait for the answer.
If a question can be answered by exploring the codebase, explore
instead of asking.

Use the `codebase-design` vocabulary (deep vs shallow, seam,
cohesion, coupling, testability) when the design involves module
boundaries.

## After the session

Write two documents:

### ADR

`docs/adr/<NNN>-<title>.md` — template:

```markdown
# <NNN> - <Title>

**Date:** YYYY-MM-DD

## Context

<what problem this ADR addresses, in domain language>

## Decision

<what we decided, in one sentence>

## Rationale

<why this decision, structured reasoning>

## Consequences

<positive — what becomes easier>
<negative — what becomes harder>

## Glossary terms introduced

- <term> — <definition>
```

### Glossary

Append to an existing `GLOSSARY.md` or create one at the project root:

```markdown
# Glossary

| Term | Definition |
|------|------------|
| <term> | <definition> |
```

Only include terms that are **new** in this session or had their
meaning **clarified** by the session. Do not duplicate existing
glossary entries — link to them instead.

## When to use this skill

- Before starting a new feature with significant design unknowns
- When the user says "I have a rough idea but need to think it through"
- After a handoff doc suggests a design session
