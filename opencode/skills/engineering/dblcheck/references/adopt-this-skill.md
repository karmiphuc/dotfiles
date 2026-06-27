# Adopt dblcheck

One-time setup for using dblcheck in a project.

## Steps

### 1. Create `.opencode/` directories

```
mkdir -p .opencode/checks .opencode/logs
```

### 2. Set project constants

Edit the constant table in the dblcheck `SKILL.md` (or create
`.opencode/project-constants.md` with overrides). Minimum entries:

| Topic | Value |
|-------|-------|
| Test runner | `<npm test, make test, cargo test, etc.>` |
| Build check | `<tsc --noEmit, go build, cargo check, etc.>` |
| Lint | `<eslint, ruff, cargo clippy, etc.>` |
| Type check | `<tsc --noEmit, mypy, go vet, etc.>` |

### 3. First check

Write a trivial check under `.opencode/checks/` and run it:

```
echo 'echo "all good"' > .opencode/checks/smoke.sh
chmod +x .opencode/checks/smoke.sh
.opencode/checks/smoke.sh
```

Log the result to `.opencode/logs/YYYY-MM-DD.md`.

Done. dblcheck is now active for this project.
