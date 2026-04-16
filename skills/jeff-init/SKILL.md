---
name: jeff-init
description: Scaffold a new project with the .jeff/ directory and artifact templates. Use when the user is starting a new project with jeff, or when another skill reports .jeff/ is missing. Triggers on 'start a new project', 'initialise jeff', 'set up product discovery', '.jeff/ is missing', '/jeff:init'. Creates .jeff/ with 8 artifact templates.
argument-hint: "[project-name]"
allowed-tools:
  - AskUserQuestion
  - Bash
  - Read
  - Write
---

## When to use
- User says "start a new project" / "initialise jeff" / "set up product discovery".
- Another jeff skill errors with "`.jeff/` missing" and refers the user back here.
- User explicitly invokes `/jeff:init`.

## Inputs
- None required in the filesystem — this skill is the scaffolder.
- Optional `$ARGUMENTS`: project name. If absent, derive from the current directory name.

## Workflow

1. **Check if already initialized.** Try `Read .jeff/config.yaml`. If it exists, ask the user whether to reinitialize. If they say no, stop. If yes, preserve existing artifacts and only rewrite template files the user hasn't modified.

2. **Determine the project name.** Use `$ARGUMENTS` when provided. Otherwise use the current directory name (ask the user to confirm if it looks machine-generated like `tmp.abc123`).

3. **Create the directory structure.**
   ```bash
   mkdir -p .jeff/research .jeff/issues
   ```

4. **Write the 8 template files.** Copy from this skill's `templates/` folder, substituting `{project_name}` and `{created}` (today's date, YYYY-MM-DD) in each:
   - `.jeff/config.yaml`
   - `.jeff/STORY_MAP.md`
   - `.jeff/OPPORTUNITIES.md`
   - `.jeff/HYPOTHESES.md`
   - `.jeff/TASKS.md`
   - `.jeff/research/USER_INTERVIEWS.md`
   - `.jeff/research/INSIGHTS.md`
   - `.jeff/research/VALIDATION_RESULTS.md`

5. **Confirm success.** List the created files and point the user at the next commands: `/jeff:map`, `/jeff:opportunity`, `/jeff:hypothesis`, `/jeff:help`.

## Output
- Writes `.jeff/` and its 8 template files in the current directory. Never touches files outside `.jeff/`.

## More
- Common failures and fixes: `references/troubleshooting.md`
- Edge cases (reinit, weird directories): `references/edge-cases.md`
- Templates (source of truth): `templates/`
- Worked examples: `examples/fresh-project.md`, `examples/existing-dot-jeff.md`, `examples/named-project.md`
