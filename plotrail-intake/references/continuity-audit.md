# Continuity Audit

Use this reference when the user asks to check many chapters or the whole manuscript for consistency.

## Context Strategy

Do not load the entire book by default. Inspect indexes, filenames, chapter summaries, and existing memory first, then drill into chapters connected to a suspected issue.

Read in this order when available:

1. `AGENTS.md`
2. `memory/chapter_summaries.yaml`
3. `memory/state_ledger.yaml` and candidate ledgers
4. relevant `canon/` files
5. relevant chapters
6. prior `reviews/`

## Audit Dimensions

- character status, goals, wounds, knowledge, and emotional residue
- relationship changes and unresolved tensions
- timeline order, elapsed time, and travel feasibility
- locations and spatial continuity
- objects, clues, records, tools, and injuries
- secrets: who knows, who does not know, and what readers know
- foreshadowing and payoff
- plot-thread promises and unresolved costs
- power, system, magic, technology, or genre rules
- protagonist agency and earned success
- antagonist or organization competence
- hook continuity and reader expectation

## Evidence Table

Use this structure:

```markdown
| Priority | Conflict | Evidence A | Evidence B | Impact | Repair Options |
| --- | --- | --- | --- | --- | --- |
```

Priority:

- `P0`: contradiction breaks plot logic or future drafting.
- `P1`: weakens credibility or payoff.
- `P2`: local cleanup or wording consistency.

## Repair Planning

Prefer the smallest repair that preserves accepted prose:

1. Add a missing setup beat.
2. Clarify knowledge transfer.
3. Adjust timing or location wording.
4. Move a reveal later or earlier.
5. Update candidate memory.
6. Rewrite scene logic only when smaller repairs fail.

## Output Files

When saving:

```text
reviews/manuscript_continuity_audit.md
reviews/chNNN_continuity_diagnosis.md
memory/change_requests.yaml
```

Do not update canon directly from an audit. Record proposed fixes and ask for approval when they change accepted story facts.
