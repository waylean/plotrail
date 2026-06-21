---
name: plotrail-intake
description: "PlotRail companion workflow for existing fiction manuscripts. Use when diagnosing pasted chapters or long prose, correcting or lightly revising an existing chapter, ingesting existing novel drafts before continuation, refining chapters without losing author intent, learning author style from prose or revised drafts, extracting canon and continuity state from manuscripts, preparing compact handoff briefs for novel-writer, or auditing long-form fiction for character, timeline, knowledge-state, plot-thread, hook, pacing, voice, and style consistency. Do not use for new project initialization, new chapter planning, drafting from approved canon, or approved canon/memory updates unless existing prose must be read first; use novel-writer for those writing-pipeline tasks."
---

# PlotRail Intake

Use this skill for existing prose. Treat the manuscript as evidence, not approved canon, until the user approves extracted facts or the project already marks them as accepted.

PlotRail Intake is the editor and intake layer for PlotRail. It helps an agent read existing chapters, diagnose problems, refine text conservatively, extract reusable story state, learn author style, audit continuity, and prepare compact handoff briefs for `novel-writer`.

## Core Rule

Preserve author intent and remove AI-flavored prose by default. Do not silently rewrite plot outcomes, core character motivation, relationship direction, timeline, genre promise, voice, or approved canon. Do not imitate a living author's distinctive style; use named authors only as high-level craft anchors such as pacing, scene pressure, dialogue economy, information release, concrete texture, or hook design. Separate:

- text-confirmed manuscript facts
- inferred but uncertain facts
- approval status for transferred facts
- editorial diagnosis
- proposed edits
- final revised prose

If an edit changes canon, relationship direction, ending direction, power rules, or the author's likely intent, stop and ask for approval.

## Mode Selection

Choose the smallest mode that answers the user:

1. **Cold-start pasted prose** - The user pasted one chapter, excerpt, or long handwritten passage. Read `references/intake-protocol.md`.
2. **Chapter diagnosis** - The user asks what is weak or how to improve a chapter. Read `references/diagnosis-rubric.md`.
3. **Chapter correction or refinement** - The user asks to correct, 校正, polish, 润色, make better, edit, revise, or rewrite existing prose. First run the minimum pass from `references/intake-protocol.md`, then read `references/refinement-workflow.md`.
4. **Manuscript intake** - The user provides multiple chapters or a folder before continuation. Read `references/intake-protocol.md`.
5. **Style learning** - The user asks to learn voice, compare original/revised drafts, or build an editing profile. Read `references/style-learning.md`.
6. **Long-form audit** - The user asks for consistency across chapters. Read `references/continuity-audit.md`.
7. **Handoff to PlotRail writing** - The next step is planning or drafting with `novel-writer`. Read `references/novel-writer-handoff.md` and `references/shared-context.md`.

Boundary rules:

- If the user wants a new project, approved canon, a chapter contract, or new prose from an accepted contract, switch to `novel-writer`.
- If the user wants to read existing prose before writing, run `plotrail-intake` first and hand off a compact brief.
- If the user says "校正", "润色", "改得更好看", "去AI味", "polish", or "copyedit" without asking for diagnosis first, default to `light` refinement, apply `references/anti-ai-prose.md`, and deliver a revised text or section patch, not only a report.

## Default Workflow

1. Identify the input shape: pasted text, local files, messy manuscript folder, or existing PlotRail project.
2. Preserve the original text. For files, do not overwrite source prose unless the user explicitly asks.
3. Build an evidence map from the minimum needed material.
4. Diagnose before rewriting unless the user clearly requested direct revision, correction, or polishing.
5. Make a concise edit plan with priority and edit authority.
6. Revise only within the requested authority.
7. When project files exist, write reusable outputs to `reviews/`, `memory/`, or `outline/` as candidates first.
8. For continuation, produce a compact handoff brief instead of passing every diagnosis note to `novel-writer`.

## Cold-Start Behavior

Do not require a PlotRail project, canon files, or a world bible. If the user only pasted text, answer in chat unless they ask to save files.

For a quick diagnosis, use:

```markdown
## What This Passage Is Doing
## Strongest Existing Material
## Main Problems
## Revision Priorities
## Suggested Next Pass
```

For continuation pre-read, use:

```markdown
## What This Passage Establishes
## Character/World/Timeline Facts
## Open Threads
## Voice And Style Snapshot
## Continuation Risks
## Next Scene Or Handoff Recommendation
```

## Edit Authority

Default to conservative editing:

- `diagnosis`: identify issues only; do not rewrite.
- `light`: improve clarity, pacing, motivation visibility, paragraph flow, and hook sharpness without changing plot events.
- `structural`: change scene order, conflict shape, or chapter ending while preserving approved story direction.
- `rewrite`: rewrite substantially only when explicitly requested.

State the edit authority used before major revisions.

## File Discipline

When working in a PlotRail-style project, write:

```text
reviews/chNNN_diagnosis.md
reviews/chNNN_refinement_notes.md
reviews/manuscript_continuity_audit.md
memory/author_editing_profile.md
memory/chapter_summary_candidates.yaml
memory/state_ledger_candidates.yaml
memory/change_requests.yaml
outline/continuation_brief_chNNN.md
```

Do not directly overwrite these without explicit approval:

```text
canon/characters.yaml
canon/relationships.yaml
canon/timeline.yaml
outline/chapters.yaml
drafts/chNNN.md
source manuscript files
```

Use candidate files for extracted state until the user approves it. If the project already has accepted canon and memory, compare against it and record conflicts rather than silently changing it.

## Shared Context With novel-writer

Do not duplicate `novel-writer` reference material inside this skill. Read `references/shared-context.md` for artifact ownership, chat-only handoff rules, P0 conflict gates, and the minimal context packet.

## Trust Rules

Use clear evidence labels:

```text
Evidence status:
Approval status:
Editorial diagnosis:
Needs author approval:
```

Avoid:

- claiming to have read chapters or files that were not inspected
- treating inference as canon
- rewriting when the user asked only for diagnosis
- making generic writing advice without text-specific evidence
- changing relationship outcome, core wound, power rules, or ending direction without approval
- flattening the author's prose into generic AI style
- mimicking a named living author's exact style, catchphrases, sentence fingerprint, or signature scene pattern

## References

- Read `references/intake-protocol.md` for pasted prose, messy manuscript folders, existing drafts, or continuation pre-read.
- Read `references/diagnosis-rubric.md` for chapter or manuscript diagnosis.
- Read `references/refinement-workflow.md` for polishing, structural edits, or rewrites.
- Read `references/anti-ai-prose.md` for every correction, polish, light revision, style calibration, or request to remove AI flavor.
- Read `references/style-learning.md` for author voice, style snapshots, original/revised comparisons, or editing profiles.
- Read `references/continuity-audit.md` for multi-chapter consistency review.
- Read `references/novel-writer-handoff.md` when preparing files for PlotRail / `novel-writer`.
- Read `references/shared-context.md` when both PlotRail skills are used and context size matters.
