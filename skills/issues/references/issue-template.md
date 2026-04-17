# GitHub Issue Template

Every issue generated from jeff artifacts follows this structure. Consistent shape makes triage scannable and keeps the discovery → engineering trace visible from within GitHub.

## Template

```markdown
## Summary
[One or two sentences on what needs to be built and why.]

## Context
- **Source:** [STORY_MAP.md > Activity > Story | OPPORTUNITIES.md > Opportunity > Solution | HYPOTHESES.md > H#]
- **Priority:** [MVP | Release 1 | Experiment]
- **Why this matters:** [User impact / business-outcome connection.]

## Acceptance Criteria
- [ ] [Specific, testable criterion]
- [ ] [Another criterion]

## Notes
[Technical considerations, dependencies, open questions, research links.]
```

## Field rules

- **Summary** — behaviour-focused. What does the user get? What's the business reason? Not "Build the save endpoint" — "User can save a recipe from the list so they can plan the week."
- **Source** — full path through the discovery artifact so a reader can open the file and see the context. Always include the artifact filename and heading path.
- **Priority** — maps directly from the source:
  - Walking-skeleton story → `MVP`
  - Release 1 story → `Release 1`
  - Opportunity solution → `Opportunity` (not MVP/R1 yet; belongs in the tree, not the release plan until scheduled)
  - Untested hypothesis → `Experiment`
- **Why this matters** — connects to user pain or business outcome. Pull from `OPPORTUNITIES.md` if the source traces back to one; otherwise write a one-line rationale.
- **Acceptance Criteria** — behavioural, 3–6 items, pass/fail. Same rules as `jeff:bdd`.
- **Notes** — links to interviews, research insights, dependencies on other issues, instrumentation needs. GitHub will render `#123`-style issue references; use them for dependencies.

## Title conventions

- **MVP issues**: start the title with the user behaviour. "User can save a recipe to Saved."
- **Opportunity issues**: start with "Explore: " to mark it as discovery work, not build work. "Explore: Curated weekly list solves 'users struggle to find recipes they'll cook'."
- **Experiment issues**: start with "Experiment: " followed by the hypothesis ID. "Experiment: H4 — Push notifications A/B test."

Consistent prefixes make grep-filtering the issue list trivial.

## Labels

Always:
- `jeff` — signals the issue came from a jeff artifact. Filterable in GitHub.

By source:
- `mvp` — walking-skeleton stories.
- `release-1` — Release 1 stories.
- `opportunity` — opportunity solutions.
- `experiment` — hypothesis validation issues.

By scope (optional, user-provided):
- `frontend`, `backend`, `infra`, etc. — if the user wants engineering-scope labels, ask.

## Example filled-in issue

```markdown
## Summary
User can save a recipe from the main list so they can plan the week. Tap the heart icon on any recipe card to add it to the 'This Week' list.

## Context
- **Source:** STORY_MAP.md > Save a recipe > Heart button to save
- **Priority:** MVP
- **Why this matters:** The walking-skeleton flow requires users to be able to commit to a recipe; without this, Plan the week and Generate shopping list have nothing to operate on.

## Acceptance Criteria
- [ ] Each recipe card displays a heart icon.
- [ ] Tapping an unsaved heart adds the recipe to 'This Week' and fills the heart.
- [ ] Tapping an already-saved heart leaves the list unchanged (no duplicates).
- [ ] If the save API fails, the system shows a retry toast; the recipe is not silently lost.
- [ ] The saved recipe persists across app restarts.

## Notes
- Traces to Opportunity O1 ("Users struggle to commit during discovery"), Solution B.
- Linked interview: P3 quote ("I always cook the same three things").
- Depends on the recipe-list rendering issue (#12).
```

Labels on this issue: `jeff`, `mvp`.
