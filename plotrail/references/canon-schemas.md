# Canon Schemas

Use these schemas as flexible templates. Keep entries compact enough to fit into chapter-specific context.

## Character

```yaml
- id: char_example
  name: ""
  aliases: []
  role: ""
  first_appearance: null
  status: active
  core_desire: ""
  core_fear: ""
  wound: ""
  public_mask: ""
  private_self: ""
  competence: []
  flaws: []
  speech_style:
    rhythm: ""
    diction: ""
    tells: []
    taboo_words_or_behaviors: []
  relationships: []
  knows: []
  does_not_know: []
  secrets: []
  never_do: []
  arc:
    start: ""
    midpoint: ""
    end: ""
  current_state:
    chapter: 0
    emotional_state: ""
    physical_state: ""
    goal: ""
```

## Chapter Contract

```yaml
- chapter: 1
  title_working: ""
  pov: ""
  time: ""
  location: ""
  purpose: ""
  must_happen: []
  must_not_happen: []
  character_state_in: {}
  character_state_out: {}
  reveals: []
  secrets_preserved: []
  foreshadowing: []
  hook_out: ""
  continuity_risks: []
  status: proposed
```

## Plot Thread

```yaml
- id: thread_example
  name: ""
  type: main | branch | romance | mystery | power | revenge | family | career | other
  promise_to_reader: ""
  introduced_in: null
  expected_payoff: null
  status: planned
  beats:
    - chapter: null
      event: ""
      effect: ""
  constraints:
    must_not_reveal_before: null
    must_payoff_by: null
```

## State Ledger

Track only facts needed to prevent contradictions.

```yaml
characters: {}
relationships: {}
plot_threads: {}
foreshadowing: {}
objects: {}
locations: {}
secrets:
  known_by_character: {}
  known_by_reader: []
timeline:
  current_chapter: 0
  current_phase: ""
```
