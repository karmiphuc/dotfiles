#!/usr/bin/env bash

cd "$(dirname "${BASH_SOURCE[0]}")";

git pull origin master;

# Mirror dotfiles into $HOME (skips repo metadata and license noise).
function doIt() {
	rsync --exclude ".git/" --exclude ".DS_Store" --exclude "bootstrap.sh" \
		--exclude "README.md" --exclude "LICENSE-MIT.txt" -avh --no-perms . ~;
	source ~/.bash_profile;
}

# Install codex-discoverable skills from this repo into ~/.codex/skills/.
# Iterates over bucket subdirectories (engineering/, productivity/, misc/),
# then each skill inside them. This mirrors the bucket layout in the repo
# but flattens them so Codex discovers skills directly under ~/.codex/skills/.
function installCodexSkills() {
	local src_base="$HOME/opencode/skills"
	local dst="$HOME/.codex/skills"
	mkdir -p "$dst"
	for bucket in "$src_base"/*/; do
		[ -d "$bucket" ] || continue
		for skill in "$bucket"*/; do
			[ -d "$skill" ] || continue
			local name
			name="$(basename "$skill")"
			mkdir -p "$dst/$name"
			if compgen -G "$dst/$name/SKILL.md" > /dev/null \
				&& [ -f "$dst/$name/.project-override" ]; then
				echo "  - skipping $name (project-override present)"
				continue
			fi
			cp -n "$skill/SKILL.md" "$dst/$name/SKILL.md" 2>/dev/null || true
			if [ -d "$skill/references" ]; then
				mkdir -p "$dst/$name/references"
				cp -n "$skill/references/"* "$dst/$name/references/" 2>/dev/null || true
			fi
			echo "  + installed skill: $name"
		done
	done
	# Templates: keep in $HOME/opencode/templates/ for ad-hoc copy.
	mkdir -p "$HOME/opencode/templates"
	if [ -d "$HOME/opencode/templates" ]; then
		echo "  + templates ready at ~/opencode/templates/"
	fi
}

if [ "$1" == "--force" -o "$1" == "-f" ]; then
	doIt;
	installCodexSkills;
else
	read -p "This may overwrite existing files in your home directory. Are you sure? (y/n) " -n 1;
	echo "";
	if [[ $REPLY =~ ^[Yy]$ ]]; then
		doIt;
		installCodexSkills;
	fi;
fi;
unset doIt;
unset installCodexSkills;
