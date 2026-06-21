# Chapter Workflow

## Planning Prompt Shape

Before drafting, produce a chapter contract:

```text
Based on AGENTS.md, canon, outline, recent summaries, and state ledger, prepare the contract for chapter N.
Do not draft prose yet.
List required events, forbidden events, character state changes, reveals, preserved secrets, foreshadowing, hook_out, and continuity risks.
```

## Drafting Rules

- Draft from the accepted contract.
- Keep canon invention local unless the user approved a change.
- Prefer character-specific motivation over plot convenience.
- Preserve who knows what. Do not let characters act on information they do not have.
- Preserve emotional residue from previous chapters.
- End with a hook that follows from the chapter, not a random shock.

## Review Checklist

Use this structure for `reviews/chNNN_continuity.md`:

```markdown
# Chapter N Continuity Review

## Contract Checklist
- [ ] must_happen item
- [ ] must_not_happen item not violated

## Canon Conflicts
- None / list conflicts with file references.

## Character Consistency
- Character:
  - Voice:
  - Motivation:
  - State transition:

## Continuity
- Timeline:
- Location:
- Objects:
- Secrets and knowledge:

## Hook
- Type:
- Strength:
- Risk:

## Revision Recommendation
none | light | medium | rewrite
```

## Memory Update

After accepted drafting/revision, update:

- `memory/chapter_summaries.yaml`: concise facts of the chapter.
- `memory/state_ledger.yaml`: current durable state.
- `memory/change_requests.yaml`: proposed changes needing user approval.
