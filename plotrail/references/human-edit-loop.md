# Human Edit Loop

Use this reference when the user has revised AI-generated chapters and wants Codex to learn the author's editing pattern.

## Compare With Integrity

First look for exact originals:

- Git history.
- `drafts_original/`, `backup/`, `old/`, or similarly named files.
- Editor autosaves or exported versions.
- Review notes that quote old lines.

If exact originals are unavailable, say so. Use triangulation instead:

- compare revised chapters to approved chapter contracts
- compare revised chapters to continuity reviews
- compare revised chapters to later unedited/batch-generated chapters
- compare title, hook, scene density, explanation density, and motivation clarity

Do not claim a line-by-line diff unless an actual original exists.

## Infer The Author's Editing Profile

Look for changes in these categories:

- **Causal clarity**: fewer convenient events; more visible reasons and constraints.
- **Character agency**: protagonist chooses from risk models, not from plot pressure.
- **Rule placement**: rules arrive just before they matter; avoid long system exposition.
- **Hook quality**: chapter endings create a specific next question.
- **Voice control**: shorter paragraphs, cleaner tension, less generic explanation.
- **Knowledge state**: who knows what remains precise.
- **Moral texture**: decisions have cost and do not flatten the protagonist into pure coolness.
- **Genre promise**: every chapter pays the platform promise in some visible way.

## Feed The Profile Back Into Drafting

After analysis, update a project file such as `memory/author_editing_profile.md`:

```markdown
# Author Editing Profile

## Keep
- Concrete sensory details before abstract explanation.
- Hooks that create a precise unresolved question.
- Protagonist as cautious risk-modeler.

## Avoid
- Long rule dumps.
- Easy success without procedural obstacles.
- Villains who fail because they become stupid.

## Drafting Requirements
- Every chapter must include a visible constraint.
- Every major choice must have a reason, cost, and fallback.
- Chapter ending must be a stronger hook than the contract's default hook.
```

Use this profile during future chapter contracts and drafts.
