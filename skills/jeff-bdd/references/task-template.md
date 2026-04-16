# Task Template

The structure for each task in `.jeff/TASKS.md`. Consistent formatting lets engineers scan the file and find what they need without training.

## Overview table (top of file)

Maintained at the top of `TASKS.md`. One row per task.

```markdown
| ID  | Task                                    | Priority  | Source                              | Status   |
|-----|-----------------------------------------|-----------|-------------------------------------|----------|
| T1  | User can save a draft recipe           | MVP       | STORY_MAP.md > Save > Heart button  | Pending  |
| T2  | User can generate a shopping list      | MVP       | STORY_MAP.md > Shopping > Ingredient dump | Pending |
```

Status values: `Pending`, `In Progress`, `Blocked`, `Done`.

## Per-task section

```markdown
### T[N]: [Behaviour-focused title]
**Source:** STORY_MAP.md > [Activity] > [Story title]
**Priority:** MVP | Release 1 | Future

**Description:**
[One or two sentences describing what the user accomplishes.]

**Acceptance Criteria:**
- [ ] The system should [behaviour 1]
- [ ] When [condition], then [behaviour 2]
- [ ] Given [context], when [action], then [result]

**Notes:**
[Business context from OPPORTUNITIES.md, dependencies on other tasks, open questions, links to research.]
```

## Field rules

- **Title** — behaviour-focused, imperative/present tense. "User can save a draft recipe" ✓. "Save-recipe endpoint" ✗.
- **Source** — full path through the story map so engineers can find context. `STORY_MAP.md > Discover > Browse categories`.
- **Priority** — MVP (walking skeleton), Release 1 (first release ribs), Future (post-release ribs). Match what the story map says; don't re-prioritise silently.
- **Description** — user-perspective outcome. Not implementation notes.
- **Acceptance Criteria** — 3–6 items typically. Behaviour-level, independently pass/fail, no implementation detail. See `acceptance-criteria.md` for full rules.
- **Notes** — where business context lives. If the task traces to an opportunity or hypothesis, cite the ID. If it has dependencies on other tasks, list them. If there are open questions, write them here rather than in the criteria.

## Example filled-in task

```markdown
### T3: User can save a recipe from the main list
**Source:** STORY_MAP.md > Save a recipe > Heart button to save
**Priority:** MVP

**Description:**
A user browsing the recipe list can tap a heart icon on any recipe card to save it. Saved recipes appear in their "This Week" list for later planning.

**Acceptance Criteria:**
- [ ] Each recipe card in the main list displays a heart icon.
- [ ] When the user taps the heart on an unsaved recipe, the recipe appears in "This Week" and the heart fills in.
- [ ] When the user taps the heart on an already-saved recipe, the recipe remains in "This Week" and the heart stays filled (no duplicates).
- [ ] If the save action fails (network error), the system shows a toast "Couldn't save — try again" and the heart stays unfilled.
- [ ] The saved recipe persists across app restarts.

**Notes:**
- Traces to Opportunity O1 ("Users struggle to commit to a recipe during discovery"), Solution B.
- Depends on T2 (recipe list rendering).
- Open question: should saves across devices sync in MVP or Release 1? Currently assumed MVP — confirm with team.
```
