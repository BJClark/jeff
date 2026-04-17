# jeff:issues — Troubleshooting

## `.jeff/` missing

Send user to `/jeff:init`.

## Artifacts still template placeholders

"Your story map / OST / hypotheses have no real content yet. Run `/jeff:map`, `/jeff:opportunity`, or `/jeff:hypothesis` first." Don't generate issues from placeholders — they'll be noise in GitHub.

## `gh` CLI not installed

Tell the user: "The `gh` command wasn't found. Install from https://cli.github.com/ and run `gh auth login`." Don't try to install it from inside the skill.

## `gh` not authenticated

Tell the user: "Run `! gh auth login` to authenticate (the `!` prefix runs it in this session so prompts work), then try again."

## `gh issue create` fails with "not a repository"

The user needs to be in a git repo with a GitHub remote, or pass `--repo owner/name`. Ask: "Which repo should these go to?" and use `--repo` on every create.

## Label doesn't exist on the repo

`gh issue create` fails. Create the label first:

```bash
gh label create jeff --color 5319E7
```

Or omit the label and add it manually later.

## Duplicate detection flagged a close match

Don't silently proceed. Show the user the existing issue and the new draft side by side. Offer three options: create-anyway, skip, open-existing.

## Batch of 20+ issues

Warn the user: "Creating 20+ issues in one batch is noisy for your team. Suggest starting with MVP (~N issues) first, then Release 1 after the team has picked up the first batch." Offer to filter by priority.

## Some issues succeed, some fail

Don't abort. Continue the batch. At the end, report both: "Created 8 issues successfully; 2 failed." Show the URLs of successes and the error for each failure.

## `.jeff/issues/` directory doesn't exist

Create it on first `--create`:

```bash
mkdir -p .jeff/issues
```

Then write the batch record file.

## Issue body exceeds GitHub's size limit

GitHub issues have a ~65,536 char body limit — rarely hit, but possible if an opportunity is quoted with lots of research context. If exceeded, trim Notes first, then Acceptance Criteria counts. Keep Summary and Context intact.

## User wants to create into a different repo

Accept `--repo owner/name` or ask. Pass it on every `gh issue create` call in the batch.
