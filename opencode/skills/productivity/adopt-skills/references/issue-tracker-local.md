# Issue tracker

## Provider

Local markdown (issues live as `.opencode/issues/<NNN>-<slug>.md`)

## Location

`.opencode/issues/`

## External PRs as request surface

`<yes | no>` — if yes, external PRs (monitored manually) flow through the same triage queue.

## Conventions

| Aspect | Convention |
|--------|------------|
| File name | `<NNN>-<slug>.md` where `NNN` is a zero-padded counter and `slug` is a kebab-case label |
| Frontmatter | `title`, `status` (open / in-progress / closed), `created`, `labels` |
| Body | Problem description, acceptance criteria, notes |
| Closing | Rename the file extension to `.closed.md` or set `status: closed` |
