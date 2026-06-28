# Global Codex Instructions

## Working Style
- Be direct, pragmatic, and implementation-oriented.
- Prefer inspecting the repository before proposing architecture or edits.
- Make small, focused changes that fit the existing codebase.
- Protect user work: do not revert or overwrite unrelated local changes.
- Explain meaningful tradeoffs, blockers, and verification results concisely.

## Tooling
- Use `rg` / `rg --files` for search when available.
- Use native project tooling for installs, builds, tests, linting, and formatting.
- Before editing, identify the relevant files and current patterns.
- Use `apply_patch` for manual file edits where practical.
- Avoid destructive commands unless explicitly requested.

## Verification
- Run the narrowest useful checks after changes.
- If checks cannot run, state exactly why and what remains unverified.
- For frontend work, verify the rendered UI in the browser when a local target is available.

## Git
- Treat the worktree as shared with the user.
- Check status before large edits or commits.
- Do not amend, rebase, reset, clean, force-push, or delete branches without explicit instruction.

## Preferences
- Default to ASCII in new files unless the project already uses Unicode or the content needs it.
- Keep comments sparse and useful.
- Favor existing project conventions over introducing new abstractions.
