---
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up. Redacts secrets. References artifacts by path/URL instead of duplicating. If arguments passed, treat them as a description of what the next session will focus on.
disable-model-invocation: true
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS — not the current workspace.

Include a "suggested skills" section in the document, which suggests skills that the agent should invoke.

Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information: API keys, passwords, personally identifiable information, secrets.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.

## Structure

```markdown
# Handoff - YYYY-MM-DD HH:MM

## Session summary
<one paragraph>

## Work completed
- <bullet list of files touched, changes made>

## Open questions / unresolved
- <what was not resolved, why>

## Suggested skills for next agent
- <skill name> — <why it applies>

## Artifacts to reference
- <path or URL> — <what it contains>

## Redacted
- <secrets redacted: API keys, tokens, PII>
```

Save to `%TEMP%/handoff-<session-id>.md` (Windows) or `/tmp/handoff-<session-id>.md` (Unix).