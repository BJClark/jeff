---
name: jeff-bdd
description: Generate BDD-style tasks with Gherkin acceptance criteria from jeff story map and opportunities. Use when the user asks to "create tasks", "write acceptance criteria", or mentions Gherkin/Given-When-Then/BDD. Reads .jeff/STORY_MAP.md and .jeff/OPPORTUNITIES.md; writes .jeff/TASKS.md.
allowed-tools: AskUserQuestion Read Write Edit
metadata:
  author: Will Clark
  version: "0.1.0"
  source-repo: https://github.com/BJClark/jeff
---

## Objective

Transform product discovery artifacts into structured, behaviour-focused implementation tasks with testable acceptance criteria.

## Process

### 1. Check project state and read artifacts

Use the Read tool to open `.jeff/STORY_MAP.md`. If the file doesn't exist, check whether `.jeff/` exists at all — if missing, tell the user to run `jeff-init` first and stop.

Also read `.jeff/OPPORTUNITIES.md` and `.jeff/TASKS.md` if they exist — ignore missing files.

### 2. Parse the story map

Read naturally. Identify backbone activities, walking skeleton stories, Release 1, and Future stories. Skip placeholder cells.

### 3. Generate tasks

For each real story, create a task with:

- **Title** — behaviour-focused ("User can save a draft recipe", not "Add save endpoint").
- **Source** — traceability to story map location.
- **Priority** — MVP (skeleton), Release 1, or Future.
- **Acceptance criteria** — "The system should [behaviour]" or Given/When/Then format. No implementation details.

### 4. Handle incremental updates

Preserve existing tasks and statuses. Increment IDs. Flag overlaps.

### 5. Write to `.jeff/TASKS.md`

Maintain the overview table and detailed task sections.

## Examples

**User says:** "Turn this story map into actionable tasks."

Actions: Read artifacts. Generate tasks per story. Present summary. Write to TASKS.md.

## Troubleshooting

- **Empty story map.** "Run jeff-map to populate it first."
- **Tech-shaped tasks.** Rewrite as user behaviour.
- **Too many acceptance criteria (8+).** Suggest splitting the task.
