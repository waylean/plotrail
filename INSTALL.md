# Install PlotRail

PlotRail's public repository name is `plotrail`. The installable skill folder is still `novel-writer`.

## Codex On macOS Or Linux

```bash
git clone https://github.com/waylean/plotrail.git
mkdir -p ~/.codex/skills
cp -R plotrail/novel-writer ~/.codex/skills/novel-writer
```

Restart Codex if the skill does not appear.

## Claude Code On macOS Or Linux

```bash
git clone https://github.com/waylean/plotrail.git
mkdir -p ~/.claude/skills
cp -R plotrail/novel-writer ~/.claude/skills/novel-writer
```

Restart Claude Code if needed.

## Windows PowerShell For Codex

```powershell
git clone https://github.com/waylean/plotrail.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\plotrail\novel-writer" "$env:USERPROFILE\.codex\skills\novel-writer"
```

## Smoke Test

Create a blank project:

```bash
python3 ~/.codex/skills/novel-writer/scripts/init_novel_project.py /tmp/plotrail-demo
```

Then open `/tmp/plotrail-demo` in your agent and run the first prompt from the README.

## Manual Mode

If your agent does not support automatic skill loading:

1. Open `novel-writer/SKILL.md`.
2. Copy the core rules into your system prompt or project instructions.
3. Keep `novel-writer/references/` available as project knowledge.
4. Use `novel-writer/scripts/init_novel_project.py` to create the durable folder layout.
