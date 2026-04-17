# Example: Scaffolding a fresh project

**User says:** "Set up jeff for this project."

**Context:** Current directory is `~/Developer/meal-planner`. No `.jeff/` exists.

**Claude's turn 1:** Confirm nothing to clobber, derive the name.

> "No existing `.jeff/` — scaffolding fresh. I'll use `meal-planner` as the project name (from the directory). Proceeding."

**Claude runs:**
```bash
mkdir -p .jeff/research .jeff/issues
```

**Then writes each template**, substituting `{project_name}` → `meal-planner` and `{created}` → today's date (e.g. `2026-04-16`).

**Claude's turn 2:** Confirm.

> "Initialized **meal-planner**. Created 8 template files:
>
> - `.jeff/config.yaml`
> - `.jeff/STORY_MAP.md`
> - `.jeff/OPPORTUNITIES.md`
> - `.jeff/HYPOTHESES.md`
> - `.jeff/TASKS.md`
> - `.jeff/research/USER_INTERVIEWS.md`
> - `.jeff/research/INSIGHTS.md`
> - `.jeff/research/VALIDATION_RESULTS.md`
>
> Next: try `/jeff:map` to start mapping the user journey, or `/jeff:help` for the full command list."

**What to notice:** No AskUserQuestion was needed because there was nothing to confirm. Scaffolding is only interactive when something's at risk (existing `.jeff/`, weird directory). Silent on the happy path.
