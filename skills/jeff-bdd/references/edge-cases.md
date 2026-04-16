# jeff-bdd — Anti-Patterns & Edge Cases

## Tech-shaped task titles

**Detection.** Title is an imperative verb aimed at code: "Build", "Implement", "Add endpoint", "Refactor".

**Why it's bad.** The task is describing what *we* do, not what the user accomplishes. QA can't verify "Build X" — they can only verify "User can X."

**Redirect.** Rewrite as user behaviour. Keep the implementation hint in Notes if it's useful context.

## Bloated acceptance criteria list

**Detection.** ≥8 criteria on a single task.

**Why it's bad.** Either the task is too broad (two tasks masquerading as one) or criteria are over-granular (hair-splitting a single behaviour into multiple bullets).

**Redirect.** Look for a natural split: happy path vs. error cases, or different user states. Propose two tasks. Alternatively, consolidate pairs of bullets that describe the same behaviour into one "A and B" criterion.

## Criteria include framework names

**Detection.** Bullets mention React, Django, specific libraries, API shapes, or database tables.

**Why it's bad.** Acceptance criteria are the contract for what "done" means to the user — not how it's built. Framework choices change; criteria shouldn't.

**Redirect.** Rewrite at the behaviour level. Move framework notes to Notes if relevant.

## Untestable criteria

**Detection.** Fuzzy verbs: "feel fast", "be intuitive", "delight", "seamless".

**Why it's bad.** No test, automated or manual, can pass or fail against these. They're aspirations, not criteria.

**Redirect.** Pick a measurable threshold or remove. "Feels fast" → "Renders within 200ms on a median device." "Intuitive" → "First-time users complete the task without asking for help in moderated testing."

## Happy-path-only criteria

**Detection.** Every bullet describes the success case. No empty state, no error state, no edge case.

**Why it's bad.** QA will test the happy path and call it done, but production users hit error states daily. Missing error criteria is how things ship "working" and then break.

**Redirect.** For every happy-path criterion, ask: "What if the precondition fails?" Add empty-state and error-state criteria.

## Partial regeneration without preserving statuses

**Detection.** User asks to regenerate tasks; skill wipes existing `In Progress` or `Done` statuses.

**Why it's bad.** Engineering loses track of current work. Regeneration silently discards progress.

**Redirect.** Always preserve statuses on existing tasks. Only add new tasks for new stories. If the user wants a full wipe, confirm explicitly.

## Duplicate tasks from re-running on an updated map

**Detection.** Story text changed slightly in `STORY_MAP.md`; skill creates T12 even though T4 already covers the same behaviour.

**Why it's bad.** Two tasks for one behaviour is a maintenance problem. One gets picked up, one rots.

**Redirect.** Before creating a new task, search existing tasks for overlap (similar title, same Source path). If found, propose updating the existing task rather than creating a new one.

## Priority drift from story map

**Detection.** Story is in walking skeleton (MVP), but the task gets Release 1 priority, or vice versa.

**Why it's bad.** Acceptance criteria tasks are derived — if priorities diverge from the source map, the two files disagree about what's MVP.

**Redirect.** Priority always follows the source. If the user thinks the priority is wrong, update the story map first, then regenerate.

## Notes bloated into criteria territory

**Detection.** Notes contain behaviour specifications; criteria contain Notes-shaped prose.

**Why it's bad.** Swapping contents defeats the template. Engineers scan criteria for what to verify and Notes for why.

**Redirect.** Anything testable goes in Criteria. Anything contextual, strategic, or about "why this exists" goes in Notes.

## Acceptance criteria referencing other tasks by ID

**Detection.** "This should work like T5 does" as a criterion.

**Why it's bad.** If T5's behaviour changes, this criterion becomes wrong without being updated. Cross-task references belong in dependencies (Notes), not criteria.

**Redirect.** State the behaviour explicitly in the criterion. Reference T5 in Notes as "depends on T5 being complete" if relevant.
