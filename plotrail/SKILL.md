---
name: plotrail
description: Long-form AI novel writing workflow for Codex. Use when creating, planning, drafting, reviewing, revising, or continuing a novel with durable canon files, character bibles, plot threads, chapter contracts, continuity checks, trend research, and memory/state ledgers so chapters stay aligned with approved story logic.
---

# PlotRail

Use this skill to run a novel as a durable project, not as one long chat. Treat project files as the source of truth and the conversation as the workbench.

## Core Rule

Preserve approved canon. Do not silently change core setting, character motivation, timeline, relationship state, revealed secrets, power rules, or plot-thread outcomes. If a useful idea conflicts with approved files, write a change request and wait for approval before drafting it into canon or prose.

## Project Layout

Expected layout:

```text
AGENTS.md
README.md
START_HERE.md
canon/
  world.md
  characters.yaml
  relationships.yaml
  timeline.yaml
  plot_threads.yaml
  glossary.yaml
outline/
  book_outline.md
  arcs.yaml
  chapters.yaml
  proposals.md
drafts/
reviews/
research/
  hook_bank.md
  trend_pool.md
memory/
  chapter_summaries.yaml
  state_ledger.yaml
  change_requests.yaml
```

If a project is missing this layout, run `scripts/init_novel_project.py <project-dir>` or create the files manually from the schemas.

## Workflow

1. **Initialize**
   - Ask for or infer title, genre, target readers, style references, taboo content, ending preference, core ideas, and publishing platform.
   - Create the project layout if missing.
   - Put unapproved ideas in `outline/proposals.md` or `memory/change_requests.yaml`; do not overwrite canon without approval.

2. **Develop canon**
   - Convert approved ideas into `canon/` and `outline/`.
   - Keep `canon/characters.yaml` operational: desire, fear, wound, mask, private self, speech style, never-do rules, arc, current state.
   - Keep `outline/chapters.yaml` as chapter contracts, not prose.

3. **Plan before drafting**
   - Read `AGENTS.md`, relevant canon files, `outline/chapters.yaml`, recent `memory/chapter_summaries.yaml`, and `memory/state_ledger.yaml`.
   - Produce a chapter contract with `must_happen`, `must_not_happen`, `character_state_in`, `character_state_out`, `reveals`, `secrets_preserved`, `foreshadowing`, `hook_out`, and `continuity_risks`.
   - Stop after the contract if the user wants approval-first writing.

4. **Draft**
   - Draft only after the contract is accepted or clearly requested.
   - Save prose to `drafts/chNNN.md` or the project's existing chapter extension.
   - Use creativity in texture, scene choice, dialogue, pacing, and emotional emphasis. Do not use creativity to bypass canon.

5. **Review**
   - Write `reviews/chNNN_continuity.md` with contract checklist, canon conflicts, character consistency, timeline/location/object continuity, knowledge-state checks, hook strength, and revision recommendation.
   - Read `references/human-edit-loop.md` when the user asks to compare AI draft quality, infer editing preferences, or improve the workflow from revised chapters.

6. **Update memory**
   - Update `memory/chapter_summaries.yaml` and `memory/state_ledger.yaml` only with durable facts established by accepted prose.
   - Add proposed canon changes to `memory/change_requests.yaml` instead of applying them silently.

7. **Revise**
   - Make narrow revisions against review findings.
   - Re-run the continuity review after meaningful changes.

## Research And Hooks

Use web search or available connectors when the user asks for current trends, memes, platform tropes, or comparable works. Trends change quickly, so browse before making current claims.

Save research to `research/`. Convert trends into emotional needs, conflict patterns, character pressure, chapter hooks, or platform-facing titles. Avoid dumping raw memes into prose unless the setting and voice support it.

Hook categories:

- information gap
- unresolved promise
- costly choice
- emotional contradiction
- identity reframe
- delayed reveal
- status reversal
- relationship rupture
- object or clue recurrence

## Context Strategy

Never load the whole novel by default. For each task, load only:

- `AGENTS.md`
- directly relevant canon files
- the chapter contract being worked on
- the last 3-5 chapter summaries
- state entries for involved characters, plot threads, objects, secrets, locations, and relationships

For whole-book questions, inspect indexes and summaries first, then drill into specific files.

## File Discipline

- Use YAML for structured state and Markdown for prose/planning.
- Keep IDs stable: `char_`, `evt_`, `thread_`, `foreshadow_`, `loc_`, `obj_`.
- Do not rename established IDs unless the user asks.
- Preserve user-written text unless explicitly editing it.
- Before major edits, explain which files will change.

## References

- Read `references/canon-schemas.md` when creating or repairing canon files.
- Read `references/chapter-workflow.md` when planning, drafting, reviewing, or revising chapters.
- Read `references/human-edit-loop.md` when learning from revised chapters or building a repeatable author-editing profile.
