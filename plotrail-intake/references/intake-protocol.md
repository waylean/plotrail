# Intake Protocol

Use this reference when the user provides pasted prose, a chapter file, a messy manuscript folder, or existing chapters that must be understood before editing or continuation.

## Input Shapes

- **Pasted excerpt**: Answer in chat unless the user asks to save files.
- **Single chapter file**: Read the chapter and nearby metadata if present.
- **Multiple chapters**: Build a chapter map first; do not immediately write long per-chapter reviews.
- **Existing PlotRail project**: Inspect `AGENTS.md`, `canon/`, `outline/`, `drafts/`, `reviews/`, and `memory/` only as needed.
- **Messy folder**: Identify chapter order, duplicates, missing numbers, title inconsistencies, and likely source files before analysis.

## Minimum Intake Steps

1. State the scope actually read.
2. Identify chapter/excerpt purpose, POV, active conflict, time/location, and ending hook.
3. Extract only evidence-backed facts.
4. Label uncertain deductions as inferred.
5. Identify open threads, secrets, promises, and unresolved costs.
6. Recommend the next useful pass: diagnosis, refinement, continuity audit, style learning, or handoff.

## Evidence And Approval Labels

Use two separate axes. Never use one label to mean both "seen in text" and "approved canon".

Evidence status:

- `text-confirmed`: directly supported by the current manuscript text.
- `project-confirmed`: directly supported by accepted project files.
- `inferred`: likely, but not explicitly established.
- `uncertain`: possible but needs author confirmation.
- `proposed`: editorial suggestion, not a manuscript fact.

Approval status:

- `approved`: accepted canon or durable memory.
- `candidate`: extracted from manuscript but not yet approved.
- `needs_author`: cannot be used as fact until the author decides.
- `rejected`: contradicted or declined.

Every handoff fact should carry both labels.

## Cold-Start Output

For a single pasted chapter or excerpt:

```markdown
## What This Passage Establishes
- Scope read:
- POV/time/location:
- Main conflict:
- Ending hook:

## Text-Confirmed Facts
- Character:
- World:
- Timeline:
- Relationship:

## Inferred But Not Canon
- ...

## Open Threads
- ...

## Voice And Style Snapshot
- Sentence/paragraph rhythm:
- Dialogue pattern:
- Exposition pattern:
- Hook pattern:

## Recommended Next Pass
- diagnosis | light refinement | structural edit | handoff
```

## Batch Intake Output

For many chapters:

```markdown
## Manuscript Scope Read
## Chapter Map
## Global Story State
## Character And Relationship State
## Open Threads And Promises
## Continuation Risks
## Suggested Processing Queue
```

Prefer one concise row per chapter. Drill into specific chapters only after identifying the highest-risk chapters.

## Chapter Correction Minimum Pass

Before correcting or polishing a chapter, extract this compact state:

- scope read
- POV, time, and location
- event sequence that must be preserved
- current knowledge state and secrets
- relationship direction and emotional residue
- genre promise and chapter purpose
- approval-sensitive changes that require the author

Then proceed to refinement. Do not turn this minimum pass into a long report unless the user asked for diagnosis.

## Candidate Files

When local project files exist, write candidates instead of final canon:

```text
memory/chapter_summary_candidates.yaml
memory/state_ledger_candidates.yaml
memory/change_requests.yaml
outline/continuation_brief_chNNN.md
reviews/manuscript_intake_report.md
```

Do not update `canon/` directly unless the user has approved the extracted facts.
