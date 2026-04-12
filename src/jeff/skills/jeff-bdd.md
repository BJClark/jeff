---
name: jeff:bdd
description: Generate BDD-style tasks with Gherkin acceptance criteria from jeff story map and opportunities. Use when the user asks to "create tasks", "generate tests", "write acceptance criteria", "turn the story map into tasks", or mentions Gherkin / Given-When-Then / BDD. Reads .jeff/STORY_MAP.md and .jeff/OPPORTUNITIES.md; writes .jeff/TASKS.md.
allowed-tools:
  - AskUserQuestion
  - Read
  - Write
  - Edit
---

## Objective

Transform product discovery artifacts into structured, **behaviour-focused** implementation tasks that bridge product thinking and engineering execution. Each task has clear acceptance criteria written as testable "should" statements or Gherkin Given/When/Then.

## Process

### 1. Check project state

Use the Read tool to open `.jeff/STORY_MAP.md`. If the file doesn't exist, check whether `.jeff/` exists at all.

- If `.jeff/` is missing entirely, tell the user to run `/jeff:init` first and stop.

Also read `.jeff/OPPORTUNITIES.md` and `.jeff/TASKS.md` if they exist — ignore missing files (TASKS.md might not exist yet; OPPORTUNITIES.md is optional context).

### 2. Understand the story map structure

Read `.jeff/STORY_MAP.md` naturally — it's a markdown file with tables. Identify:

- **Backbone activities** — the column headers in the first table.
- **Walking skeleton stories** — the row under the skeleton heading.
- **Release 1 stories** — rows under `### Release 1`.
- **Future stories** — rows under `### Future`.

Skip placeholder cells (those starting with `_` or empty) — they're unfilled template slots.

### 3. Generate tasks

For **each real story** in the story map (walking skeleton first, then Release 1), create a task. Each task must have:

- **Title** — behaviour-focused, not tech-focused. "User can save a draft recipe" not "Add save endpoint to recipes controller".
- **Source** — where in the story map it came from (e.g. `STORY_MAP.md > Discover > Browse categories`).
- **Priority** — `MVP` for walking skeleton stories, `Release 1` for release 1 stories, `Future` for future stories.
- **Description** — what needs to be accomplished from the user's perspective. One to two sentences.
- **Acceptance criteria** — written as testable assertions:
  - "The system should [behaviour]" statements.
  - Or Gherkin: `Given [context], When [action], Then [result]`.
  - Each criterion is independently pass/fail.
  - Each adds actual user or business value (no "the code should be clean" criteria).
  - No implementation details ("the React component should…" is wrong; "the user should see…" is right).

If `.jeff/OPPORTUNITIES.md` exists, enrich tasks with business context from the matching opportunity/solution.

### 4. Task template

Use this structure for each task in `.jeff/TASKS.md`:

```markdown
### T[N]: [Task Title]
**Source:** STORY_MAP.md > [Activity] > [Story Title]
**Priority:** MVP / Release 1 / Future

**Description:**
[What needs to be accomplished from the user's perspective]

**Acceptance Criteria:**
- [ ] The system should [behaviour 1]
- [ ] The system should [behaviour 2]
- [ ] When [condition], then [expected behaviour]
- [ ] Given [context], when [action], then [result]

**Notes:**
[Business context from opportunities, related tasks, dependencies]
```

### 5. Update the overview table

At the top of `.jeff/TASKS.md`, maintain the summary table:

```markdown
| ID | Task | Priority | Source | Status |
|----|------|----------|--------|--------|
| T1 | … | MVP | … | Pending |
```

Set all new tasks to `Pending`.

### 6. Handle incremental updates

If `.jeff/TASKS.md` already has tasks:

- Preserve all existing tasks and their statuses unchanged.
- Increment the task ID counter from the highest existing ID.
- If a new story overlaps an existing task, note the conflict instead of duplicating.

### 7. Present results to the user

After generating, summarise: "Generated N new tasks — M MVP, K Release 1, J Future." Then ask if they want to adjust any priorities or acceptance criteria before writing.

## Examples

**User says:** "Let's turn this story map into actionable tasks."

Actions:
1. Read `.jeff/STORY_MAP.md` and `.jeff/OPPORTUNITIES.md`.
2. For each walking skeleton story, draft a task with behavioural acceptance criteria.
3. For each Release 1 story, do the same.
4. Present the task list as a summary, then ask for adjustments.
5. Write the full list to `.jeff/TASKS.md`.

Result: `.jeff/TASKS.md` populated with prioritised tasks, each with acceptance criteria.

---

**User says:** "Just regenerate tasks for Activity 2 — we changed the story map."

Actions:
1. Read the existing TASKS.md. Identify which tasks trace to Activity 2.
2. Read the updated STORY_MAP.md.
3. Generate new tasks for the changed stories; note overlaps with existing tasks.
4. Present deltas ("removed T3, added T8 and T9") and ask for confirmation.
5. Write the updates.

Result: Activity 2 tasks refreshed without disturbing the rest of the task list.

## Troubleshooting

- **`.jeff/` missing.** Send the user to `/jeff:init` first.
- **Story map is empty** (only placeholders). "The story map has no real stories yet. Run `/jeff:map` to populate it first."
- **Tech-shaped tasks.** If the user's stories are solution-shaped ("Build REST API for X"), rewrite the task title as the user behaviour ("User can retrieve X") and push the implementation detail into Notes.
- **Too many acceptance criteria.** If a task has 8+ criteria, it's probably too big. Suggest splitting into two tasks.
- **Acceptance criteria have implementation details.** Remove mentions of specific frameworks, database schemas, or API shapes. Those belong in engineering design, not acceptance tests.
