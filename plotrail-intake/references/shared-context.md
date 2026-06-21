# Shared Context Protocol

Use this reference when `plotrail-intake` and `novel-writer` are both relevant in one task.

## Goal

Minimize redundant context while preserving story safety. The two skills should share compact artifacts, not each other's full instructions or long reports.

## Division Of Labor

`plotrail-intake` owns:

- reading existing prose
- diagnosis and refinement
- extracting manuscript facts as candidates
- style snapshots and author editing profiles
- continuity audits from existing chapters
- continuation briefs

`novel-writer` owns:

- project initialization
- approved canon and outline maintenance
- chapter contracts
- new chapter drafting
- post-draft continuity review
- durable memory updates after accepted prose

## Shared Artifacts

Prefer these over repeated prose summaries. Ownership:

| Artifact | Intake may write | novel-writer may write | Include in handoff when |
| --- | --- | --- | --- |
| `memory/chapter_summaries.yaml` | read only unless explicitly approved | approved summaries after approved prose | approved recent facts affect next chapter |
| `memory/chapter_summary_candidates.yaml` | yes | read as candidates | manuscript chapter facts need confirmation |
| `memory/state_ledger.yaml` | read only unless explicitly approved | approved durable state | current state is already approved |
| `memory/state_ledger_candidates.yaml` | yes | read as candidates | manuscript facts need confirmation |
| `memory/author_editing_profile.md` | yes, with evidence limits | read during contracts/drafting | style affects next chapter |
| `memory/change_requests.yaml` | yes | yes after approval workflow | canon changes or conflicts exist |
| `outline/continuation_brief_chNNN.md` | yes | read | moving from intake to drafting |
| `reviews/manuscript_continuity_audit.md` | yes | read only when a listed risk affects contract | audit contains relevant P0/P1 risks |

## Minimal Context Packet

When handing work from `plotrail-intake` to `novel-writer`, include only:

1. the continuation brief
2. relevant character state entries
3. relevant plot thread or secret entries
4. style requirements that affect the next chapter
5. unresolved risks that must shape the chapter contract

Do not include:

- all raw chapters
- all review notes
- complete audit tables when only one risk matters
- full style analysis when a short drafting requirement is enough
- duplicated canon schemas from `novel-writer`

## Chat-Only Briefs

If the user asks not to write files, a chat-only continuation brief is a valid temporary shared artifact. It must include:

- `brief_version`
- `created_from: chat_only`
- `source_scope`
- `evidence_index`
- `do_not_reload_unless`

Save it later only if the user asks or the session needs durable handoff.

## Same-Turn Cooperation

If both skills are invoked in a single user request:

1. Run `plotrail-intake` first for existing prose.
2. Produce or refresh a compact continuation brief.
3. Switch to `novel-writer` only after the brief is ready.
4. Let `novel-writer` read the brief and its own relevant canon/memory files.
5. Avoid re-reading the same source chapters unless the chapter contract depends on exact wording.

## Confidence Control

Mark every transferred fact with two axes:

Evidence status:

- `text-confirmed`: present in the manuscript being ingested.
- `project-confirmed`: present in accepted project files.
- `inferred`: useful but not explicit.
- `uncertain`: do not draft from it as fact.
- `proposed`: editorial recommendation only.

Approval status:

- `approved`: safe to use as established context.
- `candidate`: use as a contract constraint, not canon.
- `needs_author`: ask or design a confirmation beat.
- `rejected`: do not use.

`novel-writer` may draft from `project-confirmed + approved` facts and approved canon. It should treat `text-confirmed + candidate`, inferred, uncertain, or proposed items as constraints to confirm, repair, or preserve as risks.

## P0 Conflict Gate

If intake finds a P0 conflict with approved canon, a never-do rule, or core world logic:

- do not update approved canon or durable memory
- do not proceed to prose drafting
- either ask the author to approve a retcon or hand `novel-writer` a repair-first chapter contract brief
- make the first contract purpose "repair or explain the conflict" before new plot advancement
