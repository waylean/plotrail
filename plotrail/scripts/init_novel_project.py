#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Initialize a durable Codex novel-writing project."""

from __future__ import annotations

import argparse
from pathlib import Path


FILES = {
    "AGENTS.md": """# Novel Writing Rules

## Highest Priority
- `canon/` is the approved story source of truth.
- `outline/chapters.yaml` is the chapter contract source of truth.
- Do not silently change core setting, character motivation, relationships, timeline, power rules, secrets, or plot outcomes.
- If a change is useful but conflicts with approved canon, write it to `memory/change_requests.yaml` and wait for approval.

## Workflow
- Before drafting a chapter, read relevant canon, the chapter contract, the last 3-5 chapter summaries, and the state ledger.
- Produce a chapter contract first unless the user explicitly asks for prose.
- Save chapter prose to `drafts/chNNN.md`.
- After drafting, write `reviews/chNNN_continuity.md`.
- After accepted review/revision, update `memory/chapter_summaries.yaml` and `memory/state_ledger.yaml`.

## Quality Rules
- Character choices must come from desire, fear, wound, interest, constraint, or misunderstanding.
- Chapter hooks must arise from the chapter's real conflict.
- Trends and memes should be translated into emotion, conflict, or social texture, not pasted in raw.
""",
    "README.md": """# Novel Project

This is a long-form novel project managed with the PlotRail (`plotrail`) Codex Skill.

Start by opening this folder in Codex and saying:

```text
Use $plotrail.
Read AGENTS.md and inspect canon/, outline/, and memory/.
I want to develop this novel from theme and core ideas.
First generate proposals; do not write canon or chapter prose yet.
```
""",
    "START_HERE.md": """# Start Here

Paste this into a new Codex project session:

```text
Use $plotrail.

Read AGENTS.md and inspect canon/, outline/, and memory/.
I want to create or continue this novel.

Rules:
1. Generate proposals first; do not directly overwrite canon.
2. Help me develop premise, core conflict, main cast, antagonists, world rules, and book structure.
3. After I approve, write approved material into canon/ and outline/.
4. Do not write chapter 1 unless I explicitly ask.
```
""",
    "canon/world.md": "# World\n\n## Genre\n\n## Tone\n\n## Reader Promise\n\n## Rules\n\n## Do Not Change Without Approval\n",
    "canon/characters.yaml": "characters: []\n",
    "canon/relationships.yaml": "relationships: []\n",
    "canon/timeline.yaml": "timeline:\n  phases: []\n  fixed_events: []\n",
    "canon/plot_threads.yaml": "plot_threads: []\nforeshadowing: []\n",
    "canon/glossary.yaml": "terms: []\nlocations: []\nobjects: []\norganizations: []\n",
    "outline/book_outline.md": "# Book Outline\n\n## One-Line Promise\n\n## Core Conflict\n\n## Main Plot\n\n## Branches\n\n## Ending Direction\n",
    "outline/arcs.yaml": "arcs: []\n",
    "outline/chapters.yaml": "chapters: []\n",
    "outline/proposals.md": "# Proposals\n\nUnapproved ideas go here first.\n",
    "memory/chapter_summaries.yaml": "chapter_summaries: []\n",
    "memory/state_ledger.yaml": "characters: {}\nrelationships: {}\nplot_threads: {}\nforeshadowing: {}\nobjects: {}\nlocations: {}\nsecrets:\n  known_by_character: {}\n  known_by_reader: []\ntimeline:\n  current_chapter: 0\n  current_phase: \"\"\n",
    "memory/change_requests.yaml": "change_requests: []\n",
    "memory/author_editing_profile.md": "# Author Editing Profile\n\n## Keep\n\n## Avoid\n\n## Drafting Requirements\n",
    "research/hook_bank.md": "# Hook Bank\n\n## Information Gap\n\n## Costly Choice\n\n## Identity Reframe\n\n## Emotional Contradiction\n",
    "research/trend_pool.md": "# Trend Pool\n\nRecord trends, memes, platform tropes, and their underlying emotional needs.\n",
    "reviews/.gitkeep": "",
    "drafts/.gitkeep": "",
}


DIRS = ["canon", "outline", "drafts", "reviews", "research", "memory"]


def write_if_missing(path: Path, content: str, force: bool) -> str:
    if path.exists() and not force:
        return "kept"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as file:
        file.write(content)
    return "written"


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a Codex novel project.")
    parser.add_argument("project_dir", help="Path to the novel project folder.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing template files.")
    args = parser.parse_args()

    root = Path(args.project_dir).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    for dirname in DIRS:
        (root / dirname).mkdir(parents=True, exist_ok=True)

    results = {}
    for rel, content in FILES.items():
        results[rel] = write_if_missing(root / rel, content, args.force)

    print(f"Initialized novel project: {root}")
    for rel, status in sorted(results.items()):
        print(f"{status:7} {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
