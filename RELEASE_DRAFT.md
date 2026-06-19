# Release Draft: PlotRail v0.2.1

## Title

PlotRail v0.2.1 - Canon-aware AI fiction skill

## Summary

This release packages PlotRail as a clearer skill-first project page for long-form AI fiction writing. It keeps the installable skill folder name as `novel-writer` while presenting the public project as PlotRail.

## Highlights

- Reworked the English and Chinese README files into a product-page structure.
- Added `INSTALL.md` with Codex, Claude Code, macOS/Linux, and Windows install paths.
- Added a first-run smoke test for the project initializer.
- Fixed `init_novel_project.py` so it writes files with stable LF newlines across supported Python versions.
- Preserved the existing case study for `假如我成为了反派`.

## Install

```bash
git clone https://github.com/waylean/plotrail.git
mkdir -p ~/.codex/skills
cp -R plotrail/novel-writer ~/.codex/skills/novel-writer
```

## First Prompt

```text
Use the novel-writer skill.

Initialize this folder as a long-form novel project.
Do not write prose yet.
First help me turn my theme, core idea, target readers, taboo content,
style references, and ending direction into 3 story proposals.
Keep proposals outside canon until I approve one.
```

## Validation

Run:

```bash
python3 novel-writer/scripts/init_novel_project.py /tmp/plotrail-demo
```
