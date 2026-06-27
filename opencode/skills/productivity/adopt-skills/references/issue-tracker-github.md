# Issue tracker

## Provider

GitHub Issues (uses `gh` CLI)

## Location

`https://github.com/<owner>/<repo>/issues`

## External PRs as request surface

`<yes | no>` — if yes, external PRs flow through the same triage pipeline as issues.

## Commands

| Action | Command |
|--------|---------|
| List open issues | `gh issue list --limit 30` |
| Create issue | `gh issue create --title "<title>" --body "<body>" --label "<label>"` |
| View issue | `gh issue view <number>` |
| Close issue | `gh issue close <number>` |
| Reopen issue | `gh issue reopen <number>` |
| List open PRs | `gh pr list --limit 30` |
| View PR | `gh pr view <number>` |
| Create PR | `gh pr create --title "<title>" --body "<body>"` |
