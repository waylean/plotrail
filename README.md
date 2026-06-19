<p align="center">
  <img src="assets/plotrail-wordmark.svg" alt="PlotRail wordmark" width="820">
</p>

<p align="center">
  <a href="README.zh-CN.md">中文</a> · <a href="README.md">English</a>
</p>

<p align="center">
  <a href="#install-in-30-seconds">Install</a> ·
  <a href="#watch-the-demo">Demo</a> ·
  <a href="#first-prompt-to-run">First prompt</a> ·
  <a href="#case-study">Case study</a>
</p>

# PlotRail

PlotRail is a canon-aware AI fiction skill that helps Codex, Claude Code, and other file-based agents write long-form stories without losing the plot.

It turns a novel from one fragile chat into a durable project with approved canon, chapter contracts, continuity reviews, memory ledgers, and author editing preferences.

```text
One prompt should not carry an entire book.
PlotRail gives the agent rails: canon first, contract before prose, review after every draft.
```

## Watch the Demo

<p align="center">
  <a href="assets/plotrail-promo.mp4">
    <img src="assets/plotrail-promo-preview.gif" alt="PlotRail demo video preview" width="360">
  </a>
</p>

<p align="center">
  <a href="assets/plotrail-promo.mp4"><strong>Watch the full 42-second MP4 demo</strong></a>
</p>

## Why Writers Star This

AI can write fluent scenes. Long fiction breaks when the model:

- changes character motivation halfway through a volume
- reveals secrets before the reader or cast should know them
- forgets unpaid plot threads and foreshadowing
- lets the protagonist win because the outline needs them to win
- ignores how the author revised earlier chapters

PlotRail solves this by making the agent work like a disciplined writing-room assistant. It writes files, asks for approval before canon changes, and reviews drafts against the story state instead of trusting chat memory.

## What You Get

| Capability | What PlotRail Creates |
| --- | --- |
| Story bible | `canon/world.md`, `characters.yaml`, `relationships.yaml`, `timeline.yaml` |
| Chapter planning | `outline/chapters.yaml` contracts before prose |
| Drafting lane | `drafts/chNNN.md` with canon-bound creative freedom |
| Continuity review | `reviews/chNNN_continuity.md` after each chapter |
| Long memory | `memory/chapter_summaries.yaml`, `state_ledger.yaml`, `change_requests.yaml` |
| Author preference loop | `memory/author_editing_profile.md` learned from revisions |

## Install In 30 Seconds

Current installable skill folder: `novel-writer`.

```bash
git clone https://github.com/waylean/plotrail.git
mkdir -p ~/.codex/skills
cp -R plotrail/novel-writer ~/.codex/skills/novel-writer
```

Restart Codex if it does not detect the skill.

For Claude Code, copy the same folder to:

```text
~/.claude/skills/novel-writer
```

More options: see [INSTALL.md](INSTALL.md).

## First Prompt To Run

Open or create a novel folder, then say:

```text
Use the novel-writer skill.

Initialize this folder as a long-form novel project.
Do not write prose yet.

First help me turn my theme, core idea, target readers, taboo content,
style references, and ending direction into 3 story proposals.
Keep proposals outside canon until I approve one.
```

Then provide:

```text
Theme:
Core idea:
Genre:
Target readers:
Main character:
Antagonist:
Comparable works:
Things I dislike:
Ending direction:
Platform / length target:
```

## Workflow

```mermaid
flowchart LR
  A["Idea"] --> B["Proposals"]
  B --> C["Approved canon"]
  C --> D["Chapter contract"]
  D --> E["Draft"]
  E --> F["Continuity review"]
  F --> G["Author revision"]
  G --> H["Memory and editing profile"]
  H --> D
```

1. The author gives the theme, audience, constraints, and ending preference.
2. The agent creates proposals, not canon.
3. The author approves a direction.
4. The agent writes approved material into `canon/` and `outline/`.
5. Every chapter starts with a contract.
6. Prose is drafted only after the contract is accepted or explicitly requested.
7. A continuity review checks canon, character state, secrets, timeline, and hook strength.
8. Author revisions become reusable editing preferences.

## Case Study

The [`examples/假如我成为了反派/`](examples/%E5%81%87%E5%A6%82%E6%88%91%E6%88%90%E4%B8%BA%E4%BA%86%E5%8F%8D%E6%B4%BE/) folder shows PlotRail on a working Chinese web-novel project.

The first 11 chapters demonstrate how the workflow improves:

- protagonist agency through procedure, constraint, fallback, and cost
- antagonist competence
- rule placement and reveal timing
- chapter-end hooks
- moral consequence after taking over the villain's body
- continuity across a serial arc

The key author preference extracted from the revisions:

```text
Do not let the protagonist win because the plot needs him to win.
Show the procedure, constraint, test, fallback, and cost.
```

Open the proof files:

- [sample chapter contract](examples/%E5%81%87%E5%A6%82%E6%88%91%E6%88%90%E4%B8%BA%E4%BA%86%E5%8F%8D%E6%B4%BE/sample-chapter-contract.md)
- [sample continuity review](examples/%E5%81%87%E5%A6%82%E6%88%91%E6%88%90%E4%B8%BA%E4%BA%86%E5%8F%8D%E6%B4%BE/sample-continuity-review.md)
- [author editing profile](examples/%E5%81%87%E5%A6%82%E6%88%91%E6%88%90%E4%B8%BA%E4%BA%86%E5%8F%8D%E6%B4%BE/author-editing-profile.md)

## Model Compatibility

PlotRail works best with agents that can read and write local files:

- Codex with a strong reasoning/coding model
- Claude Code with Skills support
- any agent that supports `SKILL.md`, local project files, and multi-step workflows

If your tool does not support automatic skill loading, open `novel-writer/SKILL.md`, copy the core rules into your system prompt or project instructions, and use `novel-writer/references/` as project knowledge.

## Repository Map

```text
novel-writer/
  SKILL.md
  references/
    canon-schemas.md
    chapter-workflow.md
    human-edit-loop.md
  scripts/
    init_novel_project.py
examples/
  假如我成为了反派/
assets/
  plotrail-wordmark.svg
  plotrail-promo-preview.gif
  plotrail-promo.mp4
```

## Rename Notice

PlotRail was formerly published as `novel-writer`. The repository name changed to make the purpose clearer: keeping AI-assisted long-form fiction on a durable plot rail. The installable skill folder and invocation name remain `novel-writer` for compatibility.

## License

MIT License.
