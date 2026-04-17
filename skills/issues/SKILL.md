---
name: issues
description: Generate GitHub issues from the story map, Opportunity Solution Tree, or hypotheses via the gh CLI. Use when the user wants to push discovery artifacts into GitHub — MVP stories, opportunity solutions, or pending experiments — as draftable or directly-created issues. Triggers on 'create GitHub issues', 'turn the map into tickets', 'file issues for the walking skeleton', 'gh issue create', 'push to GitHub'. Supports --dry-run preview and --create.
argument-hint: "[source: map|opportunities|hypotheses|all] [--dry-run|--create]"
allowed-tools:
  - AskUserQuestion
  - Bash
  - Read
  - Write
  - Edit
---

## When to use
- User says "create GitHub issues" / "turn the map into tickets" / "file issues for the walking skeleton".
- User has discovery artifacts and is ready to hand work to engineering via GitHub.
- User wants to preview issue drafts before creating anything.

## Inputs
- Required: `.jeff/STORY_MAP.md` (scaffolded by `/jeff:init`, populated by `/jeff:map`).
- Optional: `.jeff/OPPORTUNITIES.md`, `.jeff/HYPOTHESES.md` — used if present, skipped silently if not.
- Optional `$ARGUMENTS`:
  - Source filter: `map`, `opportunities`, `hypotheses`, `all` (default: `all`).
  - Mode: `--dry-run` (default) or `--create`.

## Workflow

1. **Check project state.** Read `.jeff/STORY_MAP.md`. If `.jeff/` is missing, send the user to `/jeff:init`. Also read `OPPORTUNITIES.md` and `HYPOTHESES.md` if they exist — silent skip if absent.

2. **Parse the artifacts.** Natural-language read. Extract:
   - **STORY_MAP.md**: walking-skeleton stories (MVP priority), Release 1 stories (Release 1 priority). Skip placeholders.
   - **OPPORTUNITIES.md**: each real solution under an opportunity. Include opportunity name, assumptions, experiment as context.
   - **HYPOTHESES.md**: each hypothesis marked `Untested`. Generate an experiment/validation issue. Skip validated/invalidated.

3. **Draft issue bodies.** One issue per extracted item, following the template in `references/issue-template.md`. Each issue has Summary, Context (source + priority + why), Acceptance Criteria, Notes.

4. **Apply labels.**
   - All issues: `jeff`.
   - Walking-skeleton stories: add `mvp`.
   - Opportunity solutions: add `opportunity`.
   - Hypothesis experiments: add `experiment`.

5. **Present the dry-run.** Show each issue draft with a header block showing title, source, and labels. Ask: "Create these, or adjust first?"

6. **Create (if `--create` or user confirms after dry-run).**
   - First verify `gh` is authenticated: `gh auth status`. If not, stop with instructions to run `gh auth login`.
   - Before creating each issue, check for duplicates: `gh issue list --search "TITLE" --state open`. Warn if close matches exist.
   - Create with `gh issue create --title "..." --body "..." --label "jeff" --label "..."`.
   - Report each URL. If one fails, continue the batch; report failures at the end.
   - If creating >10 issues, warn the user and suggest splitting (MVP first, Release 1 later).

7. **Write a record.** After creation, write a summary file under `.jeff/issues/` listing what was created with URLs. That's the artifact record — commit it so the team knows which issues were auto-generated.

## Output
- `--dry-run` (default): prints issue drafts to chat, nothing touches GitHub.
- `--create`: creates issues via `gh`, then writes `.jeff/issues/batch-YYYY-MM-DD.md` with the list of created URLs.

## More
- Issue template: `references/issue-template.md`
- gh CLI setup and duplicate detection: `references/gh-cli-setup.md`
- Common failures and fixes: `references/troubleshooting.md`
- Edge cases: `references/edge-cases.md`
- Worked examples: `examples/skeleton-to-issues.md`, `examples/opportunities-dry-run.md`, `examples/batch-create-with-labels.md`
