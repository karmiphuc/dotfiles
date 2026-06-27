---
name: adopt-skills
description: Configure this repo for the opencode skills — set up its issue tracker, domain vocabulary, and which skills are enabled. Run once before first use of the other skills.
disable-model-invocation: true
---

# Adopt Skills

Scaffold the per-repo configuration that the other skills assume:

- **Issue tracker** — where issues live (GitHub by default; local markdown is also supported)
- **Domain docs** — where `CONTEXT.md` and ADRs live, and the consumer rules for reading them
- **Enabled skills** — which skills are active for this repo

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Process

### 1. Explore

Look at the current repo to understand its starting state. Read whatever exists; don't assume:

- `git remote -v` and `.git/config` — is this a GitHub repo? Which one?
- `AGENTS.md` and `CLAUDE.md` at the repo root — does either exist? Is there already an `## Agent skills` section in either?
- `CONTEXT.md` and `CONTEXT-MAP.md` at the repo root
- `docs/adr/` and any `src/*/docs/adr/` directories
- `docs/agents/` — does this skill's prior output already exist?
- `.opencode/` — does this skill's prior output already exist?

### 2. Present findings and ask

Summarise what's present and what's missing. Then walk the user through the three decisions **one at a time** — present a section, get the user's answer, then move to the next. Don't dump all three at once.

Assume the user does not know what these terms mean. Each section starts with a short explainer (what it is, why these skills need it, what changes if they pick differently). Then show the choices and the default.

**Section A — Issue tracker.**

> Explainer: The "issue tracker" is where issues live for this repo. Skills like `to-issues`, `triage`, `to-prd`, and `qa` read from and write to it — they need to know whether to call `gh issue create`, write a markdown file under `.opencode/issues/`, or follow some other workflow you describe. Pick the place you actually track work for this repo.

Default posture: these skills were designed for GitHub. If a `git remote` points at GitHub, propose that. If a `git remote` points at GitLab (`gitlab.com` or a self-hosted host), propose GitLab. Otherwise (or if the user prefers), offer:

- **GitHub** — issues live in the repo's GitHub Issues (uses the `gh` CLI)
- **GitLab** — issues live in the repo's GitLab Issues (uses the [`glab`](https://gitlab.com/gitlab-org/cli) CLI)
- **Local markdown** — issues live as files under `.opencode/issues/` in this repo (good for solo projects or repos without a remote)
- **Other** (Jira, Linear, etc.) — ask the user to describe the workflow in one paragraph; the skill will record it as freeform prose

If — and only if — the user picked **GitHub** or **GitLab**, ask one follow-up:

> Explainer: Open-source repos often receive feature requests as pull requests, not just issues — a PR is an issue with attached code. If you turn this on, triage pulls *external* PRs into the same queue and runs them through the same labels and states as issues (collaborators' in-flight PRs are left alone). Leave it off if PRs aren't a request surface for you.

- **PRs as a request surface** — yes / no (default: no). Record the answer in `.opencode/issue-tracker.md`.

**Section B — Domain docs.**

> Explainer: Some skills (`feedback-loop`, `tdd`, `codebase-design`) read a `CONTEXT.md` file to learn the project's domain language, and `docs/adr/` for past architectural decisions. They need to know whether the repo has one global context or multiple (e.g. a monorepo with separate frontend/backend contexts) so they look in the right place.

Confirm the layout:

- **Single-context** — one `CONTEXT.md` + `docs/adr/` at the repo root. Most repos are this.
- **Multi-context** — `CONTEXT-MAP.md` at the root pointing to per-context `CONTEXT.md` files (typically a monorepo).

### 3. Enabled skills

Confirm which skills are enabled for this repo. Default: all skills in `engineering/` and `productivity/` buckets. Let the user disable any they don't want.

### 4. Confirm and edit

Show the user a draft of:

- The `## Agent skills` block to add to whichever of `CLAUDE.md` / `AGENTS.md` is being edited (see step 5 for selection rules)
- The contents of `.opencode/issue-tracker.md`, `.opencode/domain.md`, `.opencode/enabled-skills.md`

Let them edit before writing.

### 5. Write

**Pick the file to edit:**

- If `CLAUDE.md` exists, edit it.
- Else if `AGENTS.md` exists, edit it.
- If neither exists, ask the user which one to create — don't pick for them.

Never create `AGENTS.md` when `CLAUDE.md` already exists (or vice versa) — always edit the one that's already there.

If an `## Agent skills` block already exists in the chosen file, update its contents in-place rather than appending a duplicate. Don't overwrite user edits to the surrounding sections.

The block:

```markdown
## Agent skills

### Issue tracker

[one-line summary of where issues are tracked, plus whether external PRs are a triage surface]. See `.opencode/issue-tracker.md`.

### Domain docs

[one-line summary of layout — "single-context" or "multi-context"]. See `.opencode/domain.md`.

### Enabled skills

[list of enabled skills]. See `.opencode/enabled-skills.md`.
```

Then write the three docs files using the seed templates in this skill folder as a starting point:

- `issue-tracker-github.md` — GitHub issue tracker
- `issue-tracker-gitlab.md` — GitLab issue tracker
- `issue-tracker-local.md` — local-markdown issue tracker
- `domain.md` — domain doc consumer rules + layout
- `enabled-skills.md` — list of enabled skills + their project constants

For "other" issue trackers, write `.opencode/issue-tracker.md` from scratch using the user's description.

### 5. Done

Tell the user the setup is complete and which skills will now read from these files. Mention they can edit `.opencode/*.md` directly later — re-running this skill is only necessary if they want to switch issue trackers or restart from scratch.