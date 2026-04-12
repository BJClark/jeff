---
name: jeff:issues
description: Generate GitHub issues from the jeff story map, Opportunity Solution Tree, or hypotheses. Use when the user asks to "create GitHub issues", "turn the map into tickets", "file issues for the walking skeleton", or wants to push discovery artifacts into GitHub. Supports dry-run preview or direct creation via gh CLI.
argument-hint: "[source: map|opportunities|hypotheses|all] [--dry-run|--create]"
allowed-tools:
  - AskUserQuestion
  - Bash
  - Read
  - Write
  - Edit
---

## Objective

Convert product discovery artifacts into actionable **GitHub issues** that are independently deliverable, include acceptance criteria, and link back to the opportunity or hypothesis that motivates them.

## Arguments

`$ARGUMENTS` can include:

- **Source filter**: `map`, `opportunities`, `hypotheses`, or `all` (default: `all`).
- **Mode**: `--dry-run` (show drafts without creating) or `--create` (create via `gh` CLI). Default: dry-run.

## Process

### 1. Check project state

Use the Read tool to open `.jeff/STORY_MAP.md`. If the file doesn't exist, check whether `.jeff/` exists at all.

- If `.jeff/` is missing entirely, tell the user to run `/jeff:init` first and stop.

Also read `.jeff/OPPORTUNITIES.md` and `.jeff/HYPOTHESES.md` if they exist — ignore missing files.

### 2. Parse the artifacts by reading them

Read each markdown file naturally (no regex parsing needed). Extract:

**From STORY_MAP.md:**
- The backbone activities (column headers).
- Walking skeleton stories — one per backbone column. These become MVP-priority issues.
- Release 1 stories — become Release 1-priority issues.
- Skip placeholder cells (starting with `_` or empty), template comments, and separator rows.

**From OPPORTUNITIES.md:**
- Each solution under an opportunity that isn't a placeholder (`[Solution A]`-style).
- Include the opportunity name, assumptions, and experiment as issue context.

**From HYPOTHESES.md:**
- Each hypothesis marked as `Untested` — generate an experiment/validation issue.
- Skip already-validated/invalidated hypotheses.

### 3. Draft issue bodies

For each extracted item, draft a GitHub issue using this format:

```markdown
## Summary
[What needs to be built and why — one or two sentences]

## Context
- **Source:** [STORY_MAP.md > Activity > Story | OPPORTUNITIES.md > Opportunity > Solution | HYPOTHESES.md > H#]
- **Priority:** [MVP | Release 1 | Experiment]
- **Why this matters:** [User impact / business outcome connection]

## Acceptance Criteria
- [ ] [Specific, testable criterion]
- [ ] [Another criterion]

## Notes
[Technical considerations, dependencies, open questions]
```

### 4. Suggest labels

Apply labels based on source and priority:

- All issues: `jeff` label.
- Walking skeleton stories: add `mvp`.
- Opportunities: add `opportunity`.
- Hypotheses: add `experiment`.

### 5. Present the dry-run

Show each issue draft to the user with a summary header:

```
Issue 1 of N: [Title]
Source: [reference]
Labels: [list]
---
[body]
```

Ask: "Should I create these, or would you like to adjust any first?"

### 6. Create issues (if --create or user confirms)

Before creating, verify that `gh` is authenticated:

```bash
gh auth status
```

If not authenticated, tell the user:

> "The `gh` CLI isn't authenticated. Run `! gh auth login` to log in, then try again."

Do NOT proceed with creation if `gh` is not authenticated.

For each issue, create via:

```bash
gh issue create --title "TITLE" --body "BODY" --label "LABEL1" --label "LABEL2"
```

Report each created issue's URL. If any fail, report the failure and continue with the remaining issues (don't abort the entire batch).

### 7. Write a record

After creation, write the generated issue list to `.jeff/issues/` for reference:

```bash
mkdir -p .jeff/issues
```

Write a summary file listing what was created, with issue URLs.

## Examples

**User says:** "Create GitHub issues from the walking skeleton."

Actions:
1. Read `.jeff/STORY_MAP.md`. Extract walking skeleton stories.
2. Draft one issue per story, priority MVP, with acceptance criteria.
3. Present in dry-run format.
4. If the user says "looks good, create them" — verify `gh auth status`, then create and report URLs.

Result: GitHub issues created for each walking skeleton story with `jeff` and `mvp` labels.

---

**User says:** "/jeff:issues opportunities --dry-run"

Actions:
1. Read `.jeff/OPPORTUNITIES.md`. Extract each real solution.
2. Draft one issue per solution, including the opportunity context, assumptions, and experiment plan.
3. Present all drafts without creating anything.
4. Ask if the user wants to adjust or proceed to creation.

Result: Issue drafts shown in chat; nothing created in GitHub.

## Troubleshooting

- **`.jeff/` missing.** Send the user to `/jeff:init` first.
- **Artifacts are empty.** "Your story map / OST / hypotheses are still template placeholders. Run `/jeff:map` or `/jeff:opportunity` first."
- **`gh` CLI not installed.** "The `gh` command wasn't found. Install it from https://cli.github.com/ and run `gh auth login`."
- **`gh` not authenticated.** "Run `! gh auth login` to authenticate, then try again."
- **`gh issue create` fails with "not a repository".** The user needs to be in a Git repo with a GitHub remote, or specify `--repo owner/name`.
- **Duplicate issues.** Before creating, check if issues with similar titles already exist: `gh issue list --search "TITLE" --state open`. Warn the user if potential duplicates are found.
- **User wants all issues at once.** Warn that creating many issues (>10) in a batch can be noisy. Suggest starting with MVP issues only and adding Release 1 later.
