# opinions.md

These are defaults, not laws. The repository, user request, and verified runtime
facts win when they conflict.

## Work shape
- Make the smallest useful change.
- Prefer boring code that is easy to inspect.
- Optimize for maintainability before cleverness.
- Keep durable rules short; move task-specific detail out of `AGENTS.md`.
- Do not add configurability until there is a real second use case.

## Design
- Start from existing extension points before inventing new ones.
- Keep ownership clear: one module should have one reason to own a behavior.
- Make data flow explicit where hidden state would make debugging expensive.
- Prefer simple contracts and local invariants over broad defensive layers.
- Name things by what they own or decide, not by implementation trivia.

## Code
- Match local style even when another style is personally preferable.
- Isolate side effects at the boundary.
- Treat error handling as behavior, not plumbing.
- Delete only code made unused by the current change.
- Avoid speculative cleanup in unrelated areas.

## Tests
- Test the behavior users depend on, not incidental implementation details.
- For bugs, prefer a failing or targeted check that would have caught the issue.
- Use narrower checks first; broaden only when the blast radius justifies it.
- If tests are impossible locally, explain the missing dependency or environment.

## Review
- Look for wrong-layer fixes, ownership leaks, silent behavior changes, missing
  migrations, missing tests, and edge cases.
- Findings should be concrete enough that someone can act without re-reading the
  whole codebase.
- Severity comes from user impact and likelihood, not from how interesting the
  issue is.

## Communication
- State what changed and how it was verified.
- Separate facts from inferences.
- Say when evidence is stale, missing, or bounded.
- Avoid performative certainty.
