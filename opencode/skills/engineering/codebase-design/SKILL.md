---
name: codebase-design
description: "Deep modules vocabulary for designing small-interface, deep-implementation modules. Run BEFORE writing new abstractions or refactoring existing ones. Provides the shared language (deep vs shallow, seam, cohesion, coupling, testability) and the checks to apply on every module boundary."
---

# Codebase Design

A vocabulary for reasoning about module boundaries, not a checklist.
Use the terms below to describe what you see before deciding what to
change.

---

## Foundational term — Deep vs Shallow

A **deep module** has a small interface and deep implementation. Most
of the module's complexity is hidden behind its public API. The user
of the module thinks in the module's domain language, not in the
details of how it works.

A **shallow module** has a large interface relative to its
implementation. Each function does a small, obvious thing — but
because the interface is big, the caller must understand many
functions and their interactions.

| Aspect | Deep | Shallow |
|--------|------|---------|
| Interface size | Few functions, few parameters per function | Many functions, many parameters |
| Implementation size | Lots of logic, error handling, edge cases | Trivial — one or two lines per function |
| Cognitive load on caller | Low — caller stays in domain terms | High — caller must stitch many primitives |
| Change resistance | High — internal changes don't affect callers | Low — interface changes ripple everywhere |

### Example

```typescript
// Shallow — exposes internal decisions as options
function saveUser(name: string, email: string, notify: boolean, retry: number) {}

// Deep — hides decisions behind domain vocabulary
function saveUser(draft: UserDraft): User {}
```

---

## Supporting terms

### Seam

A point where you can change behaviour without editing the source at
that place. The primary seam is the **public interface** of a module.
When you write a test against the public API and swap a real
dependency for a test double, you are exercising a seam.

Check: can every module boundary in the codebase serve as a seam?
If no — if changing a caller requires editing the module — that
module boundary is not a seam. That is a design smell.

### Cohesion

How closely the responsibilities of a module are related. High
cohesion means everything in the module works toward one purpose.
Low cohesion means the module is an arbitrary bucket.

Check: can you name the single purpose of this module in one
sentence? If no, it has low cohesion.

### Coupling

How much a module depends on the internals of another module. Loose
coupling means callers depend only on the public interface. Tight
coupling means callers depend on internal structure, error handling,
or side effects.

Check: does changing the implementation of module A require changing
callers in module B? If yes, coupling is too tight.

### Testability

Whether a module can be tested through its public interface without
special setup. A deep module is easy to test — the interface is
narrow so you exercise real behaviour. A shallow module is hard to
test — you must call many functions to exercise one scenario, or
you must mock internal collaborators.

Check: can you construct the one scenario that exercises the module's
primary behaviour with a single function call? If the test requires
three setup steps that all know about internal structure, the module
is shallow.

---

## The cycle

### 1. Name what you see

Before touching a module, describe it in these terms:

- Is it deep or shallow?
- Where are the seams?
- What is the single purpose (cohesion)?
- What do callers depend on (coupling)?
- Can you test it through the public interface (testability)?

### 2. Apply the deep module pressure

For any module you are creating or refactoring:

- What is the smallest interface that hides the most complexity?
- Which parameters can become domain types instead of primitives?
- Which functions can become private?
- Which external dependencies can the caller not see?

### 3. Verify

After writing:

- [ ] The interface has fewer functions than the implementation
- [ ] Each function name uses domain vocabulary, not implementation
- [ ] The module can be tested through its public interface
- [ ] No caller depends on internal structure
- [ ] The module's purpose fits one sentence

---

## Related skills

- `tdd` — runs codebase-design checks during the planning phase;
  also uses the terms deep module, seam, and testability during
  tracer-bullet cycles
- `dblcheck` — verify that module-design claims are Facts, not
  verbal assurances

---

## References

- John Ousterhout, *A Philosophy of Software Design* — source of the
  deep-vs-shallow term
- Matt Pocock's `codebase-design` — source material for the
  vocabulary and checks used here
