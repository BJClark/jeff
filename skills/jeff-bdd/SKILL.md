---
name: jeff-bdd
description: Generate behaviour-focused tasks with Gherkin-style acceptance criteria from the story map and opportunities. Use when the user wants to bridge discovery and engineering — turning user stories into testable tasks with Given/When/Then or 'the system should' criteria. Triggers on 'create tasks', 'generate tests', 'write acceptance criteria', 'turn the story map into tasks', 'Gherkin', 'Given-When-Then', 'BDD tasks'. Reads .jeff/STORY_MAP.md and .jeff/OPPORTUNITIES.md; writes .jeff/TASKS.md.
allowed-tools:
  - AskUserQuestion
  - Read
  - Write
  - Edit
---

## When to use
- User says "turn the story map into tasks" / "write acceptance criteria" / "create BDD tasks".
- User needs engineering-ready tasks derived from discovery artifacts.
- User is regenerating tasks after a story-map change.

## Inputs
- Required: `.jeff/STORY_MAP.md` (scaffolded by `/jeff:init`, populated by `/jeff:map`).
- Optional context: `.jeff/OPPORTUNITIES.md` — enriches Notes with business context.
- Optional existing: `.jeff/TASKS.md` — preserved and extended, not overwritten.

## Workflow

1. **Check project state.** Read `.jeff/STORY_MAP.md`. If `.jeff/` is missing, send the user to `/jeff:init`. If the story map is still template placeholders, tell the user to run `/jeff:map` first.

2. **Parse the story map.** Natural-language read, no regex. Extract:
   - **Backbone activities** (column headers).
   - **Walking skeleton** stories (row under skeleton heading) → MVP priority.
   - **Release 1** stories → Release 1 priority.
   - **Future** stories → Future priority.
   - Skip placeholder cells (`<!-- ... -->`, `_`, or empty).

3. **Load optional opportunity context.** If `.jeff/OPPORTUNITIES.md` exists, read it to enrich task Notes with source opportunity / assumption. Skip silently if absent.

4. **Generate one task per real story.** Each task has:
   - **Title** — behaviour-focused, not tech-focused. "User can save a draft recipe" ✓. "Add save endpoint to recipes controller" ✗.
   - **Source** — `STORY_MAP.md > Activity > Story`.
   - **Priority** — MVP / Release 1 / Future.
   - **Description** — what the user accomplishes, one or two sentences.
   - **Acceptance criteria** — behaviour-level, independently pass/fail, no implementation details. Use "the system should" or Gherkin `Given / When / Then`.
   - **Notes** — business context from opportunities, dependencies, open questions.

   Full template in `references/task-template.md`. Criteria quality rules in `references/acceptance-criteria.md`.

5. **Handle incremental updates.** If `.jeff/TASKS.md` already has tasks:
   - Preserve existing tasks and statuses.
   - Increment IDs from the highest existing (`T7` exists → new tasks start `T8`).
   - If a new story overlaps an existing task, note the overlap instead of duplicating.

6. **Update the overview table** at the top of `.jeff/TASKS.md`. New tasks default to `Pending`.

7. **Present before writing.** Summarise: "Generated N new tasks — M MVP, K Release 1, J Future." Ask whether to adjust priorities or criteria. Only write after confirmation.

## Output
- Writes/extends `.jeff/TASKS.md`. Preserves prior entries. Task IDs are monotonic.

## More
- Acceptance criteria quality rules and anti-patterns: `references/acceptance-criteria.md`
- Task template structure: `references/task-template.md`
- Common failures and fixes: `references/troubleshooting.md`
- Edge cases: `references/edge-cases.md`
- Worked examples: `examples/full-map-to-tasks.md`, `examples/regenerating-one-activity.md`, `examples/enriching-from-opportunity.md`
