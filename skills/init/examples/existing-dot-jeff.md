# Example: Detecting and handling an existing `.jeff/`

**User says:** "Init jeff here."

**Context:** `.jeff/` already exists. `.jeff/STORY_MAP.md` has real content (a populated backbone, not just template placeholders).

**Claude's turn 1:** Detect the existing scaffold and check whether it contains real work.

> "`.jeff/` already exists here, and `STORY_MAP.md` has real content (backbone is populated). Reinitializing will **not** overwrite your work, but I want to confirm intent before touching anything."

**Claude asks via AskUserQuestion:**
- "Reinitialize `.jeff/`?"
  - Options: "No, leave it alone" / "Yes, but preserve my edits" / "Yes, wipe and start over (I'll delete `.jeff/` myself first)"

**User's answer:** "Yes, but preserve my edits."

**Claude's turn 2:** For each template file, read the existing version. If it matches the template (only contains HTML comments and scaffold structure), rewrite from template. If it contains real content, skip.

> "Checked all 8 files:
> - `STORY_MAP.md` — has content, keeping.
> - `OPPORTUNITIES.md` — has content, keeping.
> - `HYPOTHESES.md` — template only, refreshed.
> - `TASKS.md` — template only, refreshed.
> - `config.yaml` — refreshed (project_name and created preserved).
> - `research/*` — all template only, refreshed.
>
> Reinit complete. Your discovery work is intact."

**What to notice:** The destructive-action confirmation pattern — the skill asks before touching *any* file that might contain user work, and makes "wipe and start over" the user's responsibility (they delete `.jeff/` by hand). That way the skill cannot lose work even if asked wrong.
