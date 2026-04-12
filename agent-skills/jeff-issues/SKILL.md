---
name: jeff-issues
description: Generate GitHub issues from the jeff story map, Opportunity Solution Tree, or hypotheses. Supports dry-run preview or direct creation via gh CLI. Use when the user asks to "create GitHub issues" or "turn the map into tickets".
allowed-tools: AskUserQuestion Bash Read Write Edit
metadata:
  author: Will Clark
  version: "0.1.0"
  source-repo: https://github.com/BJClark/jeff
---

## Objective

Convert product discovery artifacts into actionable GitHub issues that are independently deliverable, include acceptance criteria, and link back to the motivating opportunity or hypothesis.

## Process

### 1. Read artifacts

Use the Read tool to open `.jeff/STORY_MAP.md`, `.jeff/OPPORTUNITIES.md`, and `.jeff/HYPOTHESES.md`. If `.jeff/` doesn't exist, tell the user to run `jeff-init` first. Ignore individual missing files.

### 2. Extract items

- **STORY_MAP.md**: Walking skeleton stories (MVP priority), Release 1 stories. Skip placeholders.
- **OPPORTUNITIES.md**: Real solutions (not `[Solution A]` placeholders).
- **HYPOTHESES.md**: Untested hypotheses become experiment issues.

### 3. Draft issue bodies

Each issue includes: Summary, Context (source + priority + why it matters), Acceptance Criteria, Notes.

Labels: `jeff` on all, plus `mvp`, `opportunity`, or `experiment` as appropriate.

### 4. Dry-run or create

Default to dry-run (show drafts). If the user confirms, verify `gh auth status` then create via `gh issue create`.

Report each created issue URL. If any fail, continue with remaining issues.

### 5. Record

Write summary to `.jeff/issues/` for reference.

## Examples

**User says:** "Create GitHub issues from the walking skeleton."

Actions: Read STORY_MAP.md. Draft one issue per skeleton story. Present dry-run. On confirmation, create via gh CLI.

## Troubleshooting

- **`gh` not installed.** "Install from https://cli.github.com/"
- **`gh` not authenticated.** "Run `gh auth login` first."
- **Artifacts empty.** "Run jeff-map or jeff-opportunity first."
- **Duplicate issues.** Check with `gh issue list --search` before creating.
