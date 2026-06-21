# Publishing Checklist

## Recommended Positioning

Publish as a **skill-first** project:

```text
plotrail/
  README.md
  README.en.md
  PUBLISHING_CHECKLIST.md
  CHANGELOG.md
  LICENSE
  plotrail/
  examples/
```

Add a harness later if you want automated tests, sample project generation, chapter-review benchmarks, or model comparisons.

## README Should Include

- One-sentence project promise.
- What problem it solves.
- Installation instructions.
- First-use prompt.
- Example workflow.
- Case study summary.
- License.
- Model compatibility.
- Simple installation instructions.
- What example chapter text is included.
- First-screen CTA links: install, case study, example chapters.
- First-screen demo media: GIF preview linked to the full MP4.
- macOS/Linux and Windows install paths.
- Smoke-test command for `scripts/init_novel_project.py`.
- Explanation that the author approves canon changes.
- Invocation-name note for the `plotrail` skill folder, placed after the value proposition.

## Skill Folder Should Include

- `SKILL.md`: concise core workflow and trigger description.
- `references/`: schemas, chapter workflow, human edit loop.
- `scripts/init_novel_project.py`: deterministic project setup.
- `agents/openai.yaml`: UI metadata when supported.

## License

Current license: MIT, copyright holder `waylean`.

## Before Publishing

- Keep `README.md` as Chinese default and `README.en.md` as the optional English entry.
- Confirm that publishing the first 11 example chapters is intended.
- Run the skill validator if available.
- Test `scripts/init_novel_project.py` in a blank folder.
- Confirm `INSTALL.md` works for Codex and Claude Code.
- Create a GitHub release using `RELEASE_DRAFT.md`.
- Add repo topics: `ai-writing`, `ai-agent`, `codex-skill`, `novel-writing`, `writing-tools`, `long-form-fiction`, `ai-skill`.
- Pin the repository on the GitHub profile.
- Confirm the promo GIF and MP4 render from `assets/` after the README is published.
- Do not publish low-quality poster drafts or local experiment assets.
