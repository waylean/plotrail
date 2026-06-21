# PlotRail Handoff

Use this reference when the next step is planning or drafting with the PlotRail (`plotrail`) skill.

## Purpose

Produce a compact bridge from existing manuscript evidence to the writing workflow. The handoff should help PlotRail prepare the next chapter contract without re-reading every chapter, audit note, or raw manuscript file. Use `shared-context.md` as the source of truth for artifact ownership and anti-redundancy rules.

## Handoff Rule

Only include what the next writing step needs:

- current story state
- involved character states
- active threads and promises
- canon candidates with evidence and approval status
- continuity risks before the next chapter
- style requirements
- next chapter contract seeds

Exclude:

- full chapter prose
- full diagnosis reports
- low-priority line edits
- long explanation of how the intake was performed
- duplicated schemas already owned by PlotRail

## Continuation Brief Template

```markdown
# Continuation Brief For PlotRail

## Brief Metadata
- brief_version:
- created_from: saved_file | chat_only
- source_scope:
- evidence_index:
- do_not_reload_unless:

## Reader Instructions For PlotRail
- Use this brief to prepare a chapter contract, not to update approved canon.
- Treat candidate facts as constraints to confirm or repair.
- Do not draft prose until P0 conflicts are resolved or made part of the contract.

## Manuscript Scope Read
- Files/chapters:
- Reliability:
- Missing context:

## Current Story State
- Current chapter:
- POV:
- Time/location:
- Active conflict:
- Unresolved promises:

## Character State
- Character:
  - wants:
  - fears:
  - knows:
  - does_not_know:
  - emotional residue:
  - relationship changes:

## Canon Candidates
- fact:
  evidence:
  evidence_status: text-confirmed | project-confirmed | inferred | uncertain | proposed
  approval_status: approved | candidate | needs_author | rejected
  recommended destination:

## Continuity Risks Before Next Chapter
- risk:
  evidence:
  fix:

## Style Requirements
- keep:
- avoid:
- chapter drafting requirements:

## Recommended Next Chapter Contract Seeds
- must_happen:
- must_not_happen:
- reveals:
- secrets_preserved:
- hook_out:
```

## Candidate Destinations

Use these destinations, but do not directly overwrite approved files without user approval:

```text
memory/chapter_summary_candidates.yaml
memory/state_ledger_candidates.yaml
memory/author_editing_profile.md
memory/change_requests.yaml
outline/continuation_brief_chNNN.md
```

When the user approves candidates, PlotRail can convert them into approved `canon/`, `outline/`, and `memory/` updates using its own rules.

## Handoff Completion

End with one of:

- "Ready for PlotRail to prepare chapter N contract."
- "Not ready for drafting; approve or resolve these candidates first."
- "Need more manuscript context before continuation."
- "Ready for PlotRail to prepare a repair-first chapter contract, but not ready for prose drafting."
