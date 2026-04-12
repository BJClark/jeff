---
name: jeff-init
description: Initialize a new project with the .jeff/ directory and artifact templates. Use when the user says "start a new project", "initialize jeff", or when another skill reports .jeff/ is missing.
allowed-tools: AskUserQuestion Bash Read Write
metadata:
  author: Will Clark
  version: "0.1.0"
  source-repo: https://github.com/BJClark/jeff
---

## Objective

Scaffold a `.jeff/` directory in the current project with all artifact templates needed for product discovery.

## Process

### 1. Check if already initialized

Use the Read tool to try reading `.jeff/config.yaml`. If it exists, the project is already initialized — use AskUserQuestion to confirm before overwriting.

### 2. Determine project name

Use user-provided name, or derive from the current directory name.

### 3. Create directory structure

```bash
mkdir -p .jeff/research .jeff/issues
```

### 4. Write template files

Create each file, substituting `{project_name}` and `{created}` (today's date YYYY-MM-DD):

- `.jeff/config.yaml` — project settings and GitHub integration config.
- `.jeff/STORY_MAP.md` — backbone / walking skeleton / ribs structure.
- `.jeff/OPPORTUNITIES.md` — desired outcome / opportunities / solutions / experiments.
- `.jeff/HYPOTHESES.md` — active / validated / invalidated sections.
- `.jeff/TASKS.md` — overview table + task detail sections.
- `.jeff/research/USER_INTERVIEWS.md` — interview template.
- `.jeff/research/INSIGHTS.md` — key insights + emerging patterns.
- `.jeff/research/VALIDATION_RESULTS.md` — experiment outcome tracker.

### 5. Confirm

List created files and show next steps: jeff-map, jeff-opportunity, jeff-hypothesis.

## Examples

**User says:** "Set up jeff for this project."

Actions: Check `.jeff/` doesn't exist. Get project name. Create directories and 8 template files. Confirm.

## Troubleshooting

- **Already initialized.** Ask before overwriting.
- **Permission denied.** User needs write access to current directory.
