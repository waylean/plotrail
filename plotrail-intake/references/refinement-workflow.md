# Refinement Workflow

Use this reference when the user asks to correct, 校正, polish, 润色, make better, edit, revise, improve, or rewrite existing prose.

## Edit Levels

- `diagnosis`: identify issues only.
- `light`: clarify sentences, tighten paragraphs, sharpen motivations, improve transitions, reduce generic exposition, and strengthen hooks without changing plot events.
- `structural`: adjust scene order, add/remove beats, reshape conflict, or change chapter ending while preserving approved story direction.
- `rewrite`: rewrite substantially only when explicitly requested.

If the user does not specify an edit level, default to `light`.

For casual requests like "帮我校正这一章", "改得更好看", "去AI味", or "polish this chapter", do not ask which level they mean. Use `light`, read `anti-ai-prose.md`, produce a revised text or section patch, and put canon or continuity risks in `Author Checks`.

## Minimum Pre-Edit State

Before changing prose, extract a compact state from the chapter and nearby project context when available:

- scope read
- POV, time, and location
- event sequence to preserve
- knowledge state and secrets
- continuity constraints from `AGENTS.md`, relevant `canon/`, recent `memory/`, and chapter contracts if present
- voice and style constraints
- AI-flavored phrases, over-explained emotions, and generic polished passages to remove
- approval-sensitive changes

If project context is unavailable, say that the edit is based only on the provided prose and avoid making whole-book claims.

## Before Editing

State:

- source material read
- assumed edit level
- what will be preserved
- what requires approval

Do not ask many questions. Ask only if the edit would change core plot, character motivation, relationship direction, taboo content, ending direction, or canon.

## Preserve

- the author's intended event sequence unless structural or rewrite authority is granted
- character identity and relationship direction
- distinctive voice and rhythm
- established facts and knowledge state
- genre promise and target reader expectation

## Improve

- causality and motivation visibility
- scene pressure and stakes
- rule placement near decisions
- paragraph flow and readability
- dialogue specificity
- concrete sensory or procedural detail
- chapter ending hook
- anti-AI prose: fewer summary sentences, fewer symmetrical paragraphs, more action/evidence/subtext

## Output Formats

For short prose, provide revised text directly:

```markdown
## Edit Authority Used
light

## Revised Text
...

## What Changed
- ...

## What Was Preserved
- ...

## Author Checks
- ...
```

For long chapters, prefer an edit plan or section-by-section patch:

```markdown
## Revision Plan
| Section | Problem | Fix | Edit Level |
| --- | --- | --- | --- |

## Sample Rewrite
...
```

If the user asked to correct the whole chapter, an edit plan alone is not complete. Provide one of:

- a full revised chapter when it fits the context window
- a section-by-section patch queue with the first substantial section revised
- a clear note that the full correction is not complete yet and the next section is queued

## Do Not

- turn every voice into generic polished AI prose
- add surprise twists unsupported by the manuscript
- remove ambiguity that is functioning as suspense
- explain every subtextual emotion
- improve prose while breaking continuity
- imitate a named living author's distinctive style instead of using transferable craft principles
