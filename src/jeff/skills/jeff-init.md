---
name: jeff:init
description: Initialize a new project with the .jeff/ directory and artifact templates. Use when the user says "start a new project", "initialize jeff", "set up product discovery", or when another jeff skill reports that .jeff/ is missing.
argument-hint: "[project-name]"
allowed-tools:
  - AskUserQuestion
  - Bash
  - Read
  - Write
---

## Objective

Scaffold a `.jeff/` directory in the current project with all the artifact templates needed for product discovery. This is the entry point for all other jeff skills.

## Arguments

Optional project name: `$ARGUMENTS`

If not provided, use the current directory name.

## Process

### 1. Check if already initialized

Try to read `.jeff/config.yaml` using the Read tool. If it exists, the project is already initialized.

If `.jeff/` already exists, use AskUserQuestion to ask:

> "`.jeff/` already exists in this project. Do you want to reinitialize? This will overwrite existing templates but preserve any content you've added."

If the user says no, stop.

### 2. Determine project name

Use `$ARGUMENTS` if provided. Otherwise, derive from the current directory name.

### 3. Create directory structure

```bash
mkdir -p .jeff/research .jeff/issues
```

### 4. Write template files

Write each file below, substituting `{project_name}` with the project name and `{created}` with today's date (YYYY-MM-DD format).

**`.jeff/config.yaml`:**

```yaml
# jeff project configuration
project_name: "{project_name}"
created: "{created}"

# GitHub integration settings
github:
  # Labels to apply to generated issues
  labels:
    - "jeff"
  # Prefix for issue titles
  title_prefix: ""
```

**`.jeff/STORY_MAP.md`:**

Use the template from `src/jeff/skills/templates/STORY_MAP.md` — it contains a backbone/walking skeleton/ribs structure with HTML comment guidance.

**`.jeff/OPPORTUNITIES.md`:**

Use the template from `src/jeff/skills/templates/OPPORTUNITIES.md` — desired outcome → opportunities → solutions → experiments.

**`.jeff/HYPOTHESES.md`:**

Use the template from `src/jeff/skills/templates/HYPOTHESES.md` — active/validated/invalidated sections with the hypothesis formula.

**`.jeff/TASKS.md`:**

Use the template from `src/jeff/skills/templates/TASKS.md` — overview table + task detail sections.

**`.jeff/research/USER_INTERVIEWS.md`:**

Use the template from `src/jeff/skills/templates/USER_INTERVIEWS.md` — interview template with consistent field structure.

**`.jeff/research/INSIGHTS.md`:**

Use the template from `src/jeff/skills/templates/INSIGHTS.md` — key insights + emerging patterns.

**`.jeff/research/VALIDATION_RESULTS.md`:**

Use the template from `src/jeff/skills/templates/VALIDATION_RESULTS.md` — experiment outcome tracker.

In every template, replace `{project_name}` with the project name and `{created}` with today's date.

### 5. Confirm success

After writing all files, list the created structure:

```bash
find .jeff -type f | sort
```

Then tell the user:

> "Initialized jeff project: **{project_name}**
>
> Next steps:
> - `/jeff:map` — start mapping the user journey
> - `/jeff:opportunity` — build your Opportunity Solution Tree
> - `/jeff:hypothesis` — track risky assumptions
>
> Or run `/jeff:help` for the full command reference."

## Examples

**User says:** "Set up jeff for this project."

Actions:
1. Check `.jeff/` doesn't exist.
2. Get the project name from the current directory.
3. Create `.jeff/` with all 8 template files.
4. Confirm and show next steps.

Result: `.jeff/` directory created with all templates, ready for `/jeff:map`.

---

**User says:** "/jeff:init My New Product"

Actions:
1. Check `.jeff/` doesn't exist.
2. Use "My New Product" as the project name.
3. Create `.jeff/` with all templates, substituting the name throughout.
4. Confirm.

Result: `.jeff/` directory created with "My New Product" as the project name in all files.

## Troubleshooting

- **`.jeff/` already exists.** Ask before overwriting. If the user wants to start fresh, remove the old directory first, then reinitialize.
- **Permission denied.** The user doesn't have write access to the current directory. They need to fix permissions or change to a writable directory.
- **Not in a project directory.** This works in any directory, but warn if they're in `/`, home, or another unusual location — they probably meant to `cd` somewhere first.
