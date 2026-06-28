# Codex Profile

Portable Codex defaults for dotfiles. This profile intentionally stores only durable, non-secret configuration.

## Install

Copy or symlink these files into the local Codex/OpenCode locations:

```powershell
Copy-Item -Force .\codex\AGENTS.md $env:USERPROFILE\.codex\AGENTS.md
Copy-Item -Force .\codex\config.toml $env:USERPROFILE\.codex\config.toml
Copy-Item -Recurse -Force .\codex\skills\checker $env:USERPROFILE\.codex\skills\checker
Copy-Item -Force .\opencode\agents\checker.md $env:USERPROFILE\.opencode\agents\checker.md
```

Review `config.toml` before overwriting an existing machine config. Keep machine-specific runtime paths, auth, state databases, logs, histories, and project trust entries local.

## Excluded From Dotfiles

- `auth.json`
- `history.jsonl`
- `session_index.jsonl`
- `*.sqlite`, `*.sqlite-shm`, `*.sqlite-wal`
- local runtime paths under `AppData`, `.cache`, `.tmp`, or marketplace cache folders
- per-machine `notify`, `mcp_servers`, and project trust entries
