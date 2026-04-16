# gh CLI Setup — Auth, Repo Detection, Duplicate Search

The `gh` CLI is the primary dependency for `--create`. If it's missing or misconfigured, stop before creating anything.

## Installation

```bash
brew install gh    # macOS
# or follow https://cli.github.com/ for other OSes
```

## Authentication

Before any creation step, verify auth:

```bash
gh auth status
```

If the output says "You are not logged in", tell the user to run:

> `! gh auth login`

The `!` prefix runs the command directly in this session so its interactive prompts work. Do not try to `gh auth login` from inside the skill — it's interactive and will block.

## Repo detection

`gh issue create` needs a GitHub remote on the current repo. Check with:

```bash
gh repo view --json nameWithOwner
```

If this fails with "not a repository", the user either:
- Isn't in a git repo → tell them to `cd` to one.
- Is in a repo with no GitHub remote → ask: "Which repo should these issues go to?" Then pass `--repo owner/name` on every create command.

## Duplicate detection

Before creating each issue:

```bash
gh issue list --search "TITLE_HERE in:title" --state open --limit 5 --json number,title
```

Parse the result. If any open issue has a title matching substantively (same verb + same noun), warn the user:

> "Found a potentially duplicate issue: #42 'User can save recipes'. Your new issue: 'User can save a recipe from the main list'. Create anyway, skip, or open the existing one?"

Offer three AskUserQuestion options: create-anyway, skip-this-one, open-existing-in-browser.

## Creating the issue

```bash
gh issue create \
  --title "TITLE" \
  --body "BODY" \
  --label "jeff" \
  --label "mvp"
```

Capture the URL from the output. If creation fails (network, permissions, invalid label), report the failure and continue with the rest of the batch — don't abort the whole run.

## Creating labels if they don't exist

`gh issue create` fails if a label doesn't exist on the repo. To create missing labels in advance:

```bash
gh label create jeff --color 5319E7 --description "Generated from jeff discovery artifacts"
gh label create mvp --color E11D48 --description "Walking skeleton (MVP scope)"
gh label create release-1 --color 2563EB --description "Release 1 scope"
gh label create opportunity --color 7C3AED --description "Opportunity Solution Tree candidate"
gh label create experiment --color F59E0B --description "Hypothesis experiment"
```

Idempotent-ish: if the label exists, `gh label create` fails with a message that can be safely ignored. Check `gh label list` before attempting to create, to keep output clean.

## Rate limiting

GitHub rate-limits authenticated users at 5000 requests/hour. For batches under 50 issues this is irrelevant. For larger batches, pause 1s between creates to be polite.

## Dry-run mode

When `--dry-run` is set (default), do not call `gh` at all except `gh auth status` for a sanity check. Generate all bodies and print them; do not create.

## Creating into a specific repo

If the user is in a different directory (not the target repo), pass `--repo`:

```bash
gh issue create --repo owner/name --title "..." --body "..."
```

Ask the user for `owner/name` if they didn't supply it.
