---
name: grilling
description: Interview the user relentlessly about a plan or design. One question at a time. Wait for the answer before continuing. Asking multiple questions at once is bewildering. If a question can be answered by exploring the codebase, explore the codebase instead.
---

# Grilling

Interview the user relentlessly about a plan or design until every branch of the decision tree is resolved. For each question, provide your recommended answer.

- Ask **one question at a time**. Wait for the answer before continuing.
- If a question can be answered by exploring the codebase, explore the codebase instead.
- Stop when the plan has no unresolved branches.

## The loop

```
1. Identify the next unresolved decision point in the plan.
2. Formulate one question that resolves it.
3. Provide your recommended answer with reasoning.
3. Ask the question. Wait for the user's answer.
4. Update the plan with the decision.
5. Repeat until no unresolved decisions remain.
```

## What counts as a branch

- Interface shape (what the caller sees, invariants, error modes)
- Data flow (who owns what, mutation vs return, ownership transfer)
- Error handling (who handles, what information propagates, recovery)
- Ordering constraints (before/after, happens-before, idempotency)
- Seams (where behaviour varies, adapter surface, feature flags)
- Trade-offs (performance vs correctness, build vs buy, depth vs breadth)
- External dependencies (who we call, what contracts they provide)

## What grilling is NOT

- A checklist you run through in batch
- Asking multiple questions at once
- Asking questions the codebase already answers
- Filling in a template without resolving branches

## When to use

- Before writing a PRD, spec, or design doc
- When the user says "grill me" or "/grill-me"
- Before any non-trivial implementation
- When you detect unresolved ambiguity in a plan