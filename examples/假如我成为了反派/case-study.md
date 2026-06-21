# Case Study: 假如我成为了反派

This case study describes how the PlotRail skill supports a long-form Chinese web-novel project.

The project was originally organized with durable files:

```text
AGENTS.md
canon/
outline/
drafts/
reviews/
research/
memory/
```

The novel's current title is `假如我成为了反派`. The early arc follows Ning Zhao, a cautious technical protagonist whose erased orphanage leads him into a contaminated story-world. In the first major arc, he enters a Cold War island scenario as a low-level repairman and must take over the antagonist's body without letting the organization realize the villain has changed.

## Why The Skill Matters

A long novel has more state than a chat window should hold:

- which facts are canon
- who knows each secret
- what each character wants and fears
- which plot threads are introduced but unpaid
- what a chapter must accomplish
- what a chapter must not reveal yet
- how the author's editing preferences evolve

The skill solves this by turning the novel into a project with explicit memory.

## Working Flow Used In This Project

1. Create the premise, cast, world rules, and volume outline as proposals.
2. Approve the direction before writing it into `canon/`.
3. Create `outline/chapters.yaml` as chapter contracts.
4. Draft chapters into `drafts/`.
5. Review each chapter into `reviews/`.
6. Update `memory/chapter_summaries.yaml` and `memory/state_ledger.yaml`.
7. Let the author revise the chapters.
8. Analyze the author's revisions and turn them into an author editing profile.

## What The First 11 Chapters Demonstrate

The first 11 chapters show the difference between "AI completed the outline" and "the chapter now feels serial-ready."

The revised chapters emphasize:

- concrete investigation before exposition
- visible constraints before protagonist success
- rules explained only when they affect a decision
- chapter endings that create precise next-chapter pressure
- protagonist agency through risk modeling
- antagonist competence
- moral cost after taking over the villain's body

## Example: Chapter Contract To Draft

The contract for chapter 8 requires a controlled communication vulnerability, outside-agent pressure, and an order to bring Ning Zhao into the core area. A weak draft might simply make the villain summon him. The revised direction makes the protagonist manufacture a crisis that only he can solve, while the villain's order still feels consistent with the villain's control needs.

That is the key value of the workflow: chapter contracts do not remove creativity. They give creativity a target.

## Example: Human Editing Feedback

A recurring author preference emerged from chapters 1-11:

```text
Do not let the protagonist win because the plot needs him to win.
Show the procedure, constraint, test, fallback, and cost.
```

The skill turns that preference into a reusable drafting requirement:

```text
Every major choice must have:
1. a concrete reason
2. a visible risk
3. a procedural action
4. a cost or unresolved consequence
```

Future chapters can now be drafted closer to the author's taste, reducing manual revision.

## Included Example Text

The `chapters/` folder includes the first 11 chapters of the example novel. These chapters are included so users can judge the prose quality directly instead of only reading a workflow description.
