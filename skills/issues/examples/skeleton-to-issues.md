# Example: Walking skeleton → MVP GitHub issues

**User says:** "Create GitHub issues from the walking skeleton."

**Context:** `.jeff/STORY_MAP.md` has the 6-column backbone and walking skeleton for a meal-planner app. `.jeff/OPPORTUNITIES.md` and `.jeff/HYPOTHESES.md` exist and have some relevant content. No issues have been generated before — `.jeff/issues/` doesn't exist yet.

**Claude's turn 1:** Parse, confirm target.

> "Read `STORY_MAP.md`. Six walking-skeleton stories (one per activity):
>
> 1. Email + password signup
> 2. One dietary question (skippable)
> 3. Scrollable list of 20 seeded recipes
> 4. Heart button to save
> 5. Flat 'This Week' list
> 6. Combined ingredient dump
>
> Pulling Opportunity context from O1 (applies to #2) and O3 (applies to #3). None of these map to an active hypothesis.
>
> GitHub target: `scidept/meal-planner` (from `gh repo view`). Continuing in `--dry-run` mode. Drafting 6 issues."

**Claude's turn 2:** Show each draft. Issue 1 shown in full; the other 5 would follow the same structure.

```
Issue 1 of 6
Title: User can sign up with email and password
Source: STORY_MAP.md > Sign in > Email + password signup
Labels: jeff, mvp
---
## Summary
A new user arriving via share link can create an account with their email address and a password, and is taken into the onboarding flow. This is the entry point for the MVP.

## Context
- **Source:** STORY_MAP.md > Sign in > Email + password signup
- **Priority:** MVP
- **Why this matters:** The walking-skeleton flow depends on users being able to reach onboarding. Without signup, no other skeleton behaviour is reachable.

## Acceptance Criteria
- [ ] The signup form shows fields for email and password and a 'Create account' button.
- [ ] When the user submits with a valid email and an 8+ character password, an account is created and they're signed in.
- [ ] If either field is empty on submit, the system shows an inline error next to the empty field and does not create an account.
- [ ] If the email is already registered, the system shows "Account exists — sign in instead" with a link to sign-in.
- [ ] On success, the user is routed to the first onboarding screen.

## Notes
- Social login is explicitly out of scope (Future).
- No email verification in MVP (Release 1 concern).
```

*(Issues 2–6 follow in the same format; omitted here for brevity.)*

**Claude's turn 3:** Ask for confirmation.

> "Six drafts shown. Labels applied: `jeff` + `mvp` on all.
>
> Proceed to create? Or adjust any first?"

**User:** "Create them."

**Claude's turn 4:** Verify gh auth, dupe-check, create.

```bash
gh auth status                                    # ✓ authenticated
gh label list | grep -E '^(jeff|mvp)$'            # both labels exist
gh issue list --search "sign up in:title" --state open --limit 5
#   → no matches
gh issue create --title "User can sign up with email and password" --body "..." --label "jeff" --label "mvp"
#   → https://github.com/scidept/meal-planner/issues/13
gh issue create --title "User can answer one dietary question during onboarding" --body "..." --label "jeff" --label "mvp"
#   → https://github.com/scidept/meal-planner/issues/14
# ... (4 more)
```

**Claude's turn 5:** Report and write the batch record.

> "Created 6 issues in `scidept/meal-planner`:
>
> - #13 — User can sign up with email and password
> - #14 — User can answer one dietary question during onboarding
> - #15 — User can browse 20 seeded recipes
> - #16 — User can save a recipe to This Week
> - #17 — User can view saved recipes as a flat list
> - #18 — User can generate a combined shopping list
>
> Wrote the batch record to `.jeff/issues/batch-2026-04-16.md` — commit that with your changes."

**Claude writes `.jeff/issues/batch-2026-04-16.md`:**

```markdown
# Batch created 2026-04-16

Source: STORY_MAP.md (walking skeleton).

| # | Title | URL |
|---|-------|-----|
| 13 | User can sign up with email and password | https://github.com/scidept/meal-planner/issues/13 |
| 14 | User can answer one dietary question during onboarding | https://github.com/scidept/meal-planner/issues/14 |
| 15 | User can browse 20 seeded recipes | https://github.com/scidept/meal-planner/issues/15 |
| 16 | User can save a recipe to This Week | https://github.com/scidept/meal-planner/issues/16 |
| 17 | User can view saved recipes as a flat list | https://github.com/scidept/meal-planner/issues/17 |
| 18 | User can generate a combined shopping list | https://github.com/scidept/meal-planner/issues/18 |

Labels applied: jeff, mvp (all).
```

**What to notice:** Three correct defaults. (1) `--dry-run` first, even though the user asked to "create" — the drafts were shown before creation for a final gate. (2) Before creating, Claude verified `gh auth`, ensured labels existed, and ran duplicate-title searches. (3) After creation, a dated record was written to `.jeff/issues/` so the team has a permanent log of what came from which batch.
