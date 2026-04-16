# Example: Large batch with label creation and duplicate handling

**User says:** "/jeff:issues all --create"

**Context:** `.jeff/STORY_MAP.md`, `.jeff/OPPORTUNITIES.md`, and `.jeff/HYPOTHESES.md` are all populated. The user wants everything created at once. Repo is `scidept/meal-planner`. Some issues with matching titles already exist from a prior run two weeks ago. The repo doesn't yet have the `opportunity` or `experiment` labels.

**Claude's turn 1:** Parse all three artifacts, count the batch.

> "Full inventory:
> - **MVP** (walking skeleton): 6 issues.
> - **Release 1**: 9 issues.
> - **Opportunity** (untested solutions): 6 issues.
> - **Experiment** (untested hypotheses): 4 issues.
>
> **Total: 25 issues.**
>
> That's a big batch. Three warnings before I proceed:"

**Claude's turn 2:** Warn and ask.

> 1. **25 issues will flood your GitHub** — even with labels, the team will see 25 new issues at once. Consider splitting: MVP first (6), then Release 1 (9), then opportunity/experiment exploration (10). Each batch gives the team a chance to react.
> 2. **Two labels don't exist on the repo yet**: `opportunity` and `experiment`. I'll need to create them before applying.
> 3. **I'll dupe-check each title against open issues** before creating. If a match exists from a prior run, I'll ask what to do.
>
> (AskUserQuestion)
> - "Proceed with all 25"
> - "Just MVP (6) — I'll do the rest later"
> - "MVP + Release 1 (15) — skip opportunity/experiment for now"
> - "Abort"

**User:** "MVP + Release 1. Skip opportunity/experiment."

**Claude's turn 3:** Create missing labels first (none needed for mvp/release-1 since they already exist, but verify).

```bash
gh label list | grep -E '^(jeff|mvp|release-1)'
# → all three exist, good
```

**Claude's turn 4:** For each of the 15 issues, dupe-check then create.

```bash
# Issue 1: "User can sign up with email and password"
gh issue list --search "sign up with email in:title" --state open --limit 3 --json number,title
# → [] empty, no dupes
gh issue create --title "User can sign up with email and password" --body "..." --label "jeff" --label "mvp"
# → https://github.com/scidept/meal-planner/issues/25

# Issue 2: "User can answer one dietary question during onboarding"
gh issue list --search "dietary question onboarding in:title" --state open --limit 3 --json number,title
# → [{"number":18, "title":"User can answer one dietary question during onboarding"}]
# → DUPE DETECTED — stop and ask
```

**Claude's turn 5:** Handle the dupe.

> "Found a potential duplicate for issue 2:
> - **Existing**: #18 'User can answer one dietary question during onboarding' (open)
> - **New draft**: same title
>
> Options:"
> (AskUserQuestion)
> - "Skip — already have this one"
> - "Create anyway — my new draft has updated acceptance criteria"
> - "Close #18 and create new — acceptance criteria changed significantly"
> - "Open #18 in browser so I can compare manually"

**User:** "Skip — the existing one is fine."

**Claude continues the batch**, dupe-checking each, creating where new, skipping where existing. Two more dupes found; one is skipped, one is "create anyway" because criteria changed.

**Claude's turn 6:** Final report.

> "Batch result:
> - **Created**: 13 issues (#25 through #37).
> - **Skipped as duplicates**: 2 (#18, #20 — already existed, unchanged).
> - **Created despite existing match**: 1 (new #38 supersedes #21 — noted in #38's Notes).
> - **Failed**: 0.
>
> Opportunity and experiment issues not touched — come back for those later with `/jeff:issues opportunities` or `/jeff:issues hypotheses`.
>
> Writing the batch record now."

**Claude writes `.jeff/issues/batch-2026-04-16.md`:**

```markdown
# Batch created 2026-04-16

Source: STORY_MAP.md (MVP + Release 1 stories).

## Created
| # | Title | URL | Source | Labels |
|---|-------|-----|--------|--------|
| 25 | User can sign up with email and password | https://.../25 | STORY_MAP.md > Sign in | jeff, mvp |
| 26 | ... | ... | ... | ... |
...

## Skipped as duplicates
- Issue "User can answer one dietary question during onboarding" already exists as #18 (unchanged).
- Issue "User can heart a recipe to save it" already exists as #20 (unchanged).

## Superseded
- New #38 supersedes open #21 (acceptance criteria changed — #21 should be closed once #38 is triaged).
```

**Claude's turn 7:** Final nudge.

> "Done. One manual step: you may want to close #21 once the team agrees #38 supersedes it. I left a note in #38's Notes field pointing to #21."

**What to notice:** Three things scale matters for. (1) Batch size was pushed back on — 25 was flagged as too many, and the user split it voluntarily to 15. (2) Duplicate detection is *per issue*, not once upfront — titles can match old issues nobody remembered. (3) The batch record distinguishes `Created` / `Skipped` / `Superseded`, which gives the team an audit trail rather than a flat success list.
