# Issue tracker

## Provider

GitLab Issues (uses `glab` CLI)

## Location

`https://<host>/<owner>/<repo>/-/issues`

## External PRs as request surface

`<yes | no>` — if yes, external MRs flow through the same triage pipeline as issues. (GitLab calls PRs "merge requests".)

## Commands

| Action | Command |
|--------|---------|
| List open issues | `glab issue list --limit 30` |
| Create issue | `glab issue create --title "<title>" --description "<body>" --label "<label>"` |
| View issue | `glab issue view <number>` |
| Close issue | `glab issue close <number>` |
| Reopen issue | `glab issue reopen <number>` |
| List open MRs | `glab mr list --limit 30` |
| View MR | `glab mr view <number>` |
| Create MR | `glab mr create --title "<title>" --description "<body>"` |
