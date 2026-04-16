# jeff-issues — Anti-Patterns & Edge Cases

## Creating issues from templates (empty artifacts)

**Detection.** Story map or OST is mostly HTML comments and template-scaffold placeholders.

**Why it's bad.** GitHub fills up with `<!-- Activity 1 -->` as issue titles. Nobody benefits.

**Redirect.** Detect placeholder patterns (`<!--`, `_`, empty cells) and skip them silently. If every cell is a placeholder, tell the user to populate the artifact first.

## Silently creating without dry-run

**Detection.** User runs `/jeff:issues --create` without ever seeing the drafts.

**Why it's bad.** Once created, issues are visible to the team, notify watchers, and are hard to retract. Mistakes cost real trust.

**Redirect.** Always preview first unless the user explicitly opts out. On a fresh run, default to `--dry-run`. If the user passes `--create`, still show the titles-and-labels summary and confirm before firing.

## Duplicate title check skipped

**Detection.** Skill proceeds to `gh issue create` without first running `gh issue list --search`.

**Why it's bad.** Users re-running `/jeff:issues` after story-map edits create duplicates of issues they already filed.

**Redirect.** Always dupe-check per issue before creation. Only skip if the user explicitly opts out.

## Creating labels that already exist

**Detection.** Skill runs `gh label create jeff` unconditionally, producing "already exists" errors.

**Why it's bad.** Noisy output; obscures real errors.

**Redirect.** Check `gh label list` first, create only missing labels. Or swallow "already exists" errors silently with rc-check.

## Batch too large

**Detection.** >15 issues in a single batch.

**Why it's bad.** Floods the team, dilutes prioritisation, makes triage painful. Also makes any mistake painful to reverse.

**Redirect.** Warn the user. Offer: "Want to file just MVP (~6) first and come back for Release 1 later?" Let them override if they insist.

## Priority labels not matching artifact priority

**Detection.** Walking-skeleton story gets `release-1` label, or vice versa.

**Why it's bad.** The team filters by label and gets the wrong scope.

**Redirect.** Priority always follows the source. If the user wants different prioritisation, they should change the source artifact first.

## Issue body bloated with research

**Detection.** Body is >10k chars, most of it quoted interview transcripts.

**Why it's bad.** GitHub renders it, but nobody reads it. The signal-to-noise ratio drops; contributors skim and miss the acceptance criteria.

**Redirect.** Link to `INSIGHTS.md` or `USER_INTERVIEWS.md` in Notes instead of inlining full quotes. Keep the body focused: Summary, Context, Acceptance Criteria, short Notes.

## Stale draft batch record

**Detection.** `.jeff/issues/batch-YYYY-MM-DD.md` exists with stale URLs (issues have since been closed, merged, or renamed).

**Why it's bad.** Team members read the file assuming it's current.

**Redirect.** On each new batch, write a new dated file — don't overwrite. Over time the directory shows the creation history. If the user wants a consolidated view, they can generate one manually; don't auto-maintain.

## Running `--create` in the wrong repo

**Detection.** `gh repo view` shows a repo unrelated to the user's project, or `gh` is configured for a personal repo when the work is a work repo.

**Why it's bad.** Issues end up in the wrong place. Hard to move.

**Redirect.** Before creating, print the target: "Creating issues in `owner/name`. Confirm?" If they say wrong, ask for `--repo owner/name`.
