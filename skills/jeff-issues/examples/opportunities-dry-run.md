# Example: Dry-run preview of opportunity solutions

**User says:** "/jeff:issues opportunities --dry-run"

**Context:** `.jeff/OPPORTUNITIES.md` has three opportunities (O1, O2, O3). O1 has three solutions (one validated, two untested). O2 has two solutions (both untested). O3 has three solutions (one validated, two untested). The user wants to see what opportunity-based issues would look like before committing.

**Claude's turn 1:** Parse and filter.

> "Reading `OPPORTUNITIES.md`. Eight total solutions, but filtering:
> - **Validated solutions** — skip (they'll become build work, which comes via `/jeff:bdd` or the story map, not directly as opportunity issues).
> - **Untested solutions** — these become `opportunity` issues for exploration/scoping.
>
> That leaves 6 solutions → 6 draft issues. None of them create anything — this is dry-run."

**Claude's turn 2:** Show drafts. First two:

```
Issue 1 of 6
Title: Explore: Shorten preference wizard to 2 steps (O1 / Solution A)
Source: OPPORTUNITIES.md > O1 > Solution A
Labels: jeff, opportunity
---
## Summary
Reduce the preference wizard from 5 steps to 2 to address the 40% drop-off at step 3. Untested — this is scoping/experiment work, not a committed build.

## Context
- **Source:** OPPORTUNITIES.md > O1 (Users drop off the preference wizard) > Solution A
- **Priority:** Opportunity
- **Why this matters:** W1 retention is 18% → 30% goal; users who complete the wizard retain 2× (INSIGHTS.md I2). If step 3 is the drop-off point, shortening may capture the lost 2× retention bump without behaviour change.

## Acceptance Criteria
- [ ] Decision made on which 3 steps to drop (offline analysis of existing users' recommendation quality with vs. without those steps).
- [ ] Riskiest assumption ("Steps 3–5 aren't necessary for good recommendations") tested against historical data before build.
- [ ] Go/no-go recorded in OPPORTUNITIES.md.

## Notes
- Experiment plan: 1-day offline analysis of existing recommendation quality for completers vs. drop-offs.
- Traces up to outcome "W1 retention 18%→30%".
- If validated → spawn build tasks via `/jeff:bdd`.

Issue 2 of 6
Title: Explore: Make every preference step skippable (O1 / Solution B)
Source: OPPORTUNITIES.md > O1 > Solution B
Labels: jeff, opportunity
---
## Summary
Add skip buttons to all preference wizard steps. Users who currently drop off might continue if given an explicit exit, rather than abandoning.

## Context
- **Source:** OPPORTUNITIES.md > O1 > Solution B
- **Priority:** Opportunity
- **Why this matters:** Untested alternative to Solution A. If skip buttons get users through the wizard at the same rate, we preserve the full question set for users who want it.

## Acceptance Criteria
- [ ] Mock skip-buttons into the wizard (prototype only — no backend changes).
- [ ] Measure completion rate in a user test (5 users) vs. current drop-off.
- [ ] Record result in OPPORTUNITIES.md.

## Notes
- Cheaper than Solution A (no historical analysis required).
- If both A and B look promising, one A/B test can compare them once we reach that stage.
```

*(Issues 3–6 would follow in the same structure — one per untested solution.)*

**Claude's turn 3:** Summarise and ask.

> "Six opportunity-issue drafts. All dry-run; nothing hit GitHub.
>
> These are exploration issues, not build work. They're for the team to track which solutions are being actively investigated vs. sitting dormant.
>
> Want to:"
> (AskUserQuestion)
> - "Create all 6 in GitHub"
> - "Create a subset (name which)"
> - "Adjust the drafts first"
> - "Don't create — I just wanted the preview"

**User:** "Don't create — I just wanted the preview. I'll come back when I've picked which to run."

**Claude's turn 4:**

> "No issues created. Drafts shown above are not persisted anywhere — if you want them saved for later, I can write them to `.jeff/issues/drafts-2026-04-16.md`. Want that?"

**User:** "Yes, save the drafts."

**Claude writes `.jeff/issues/drafts-2026-04-16.md`** with the 6 issue bodies and a header noting they're drafts, not created.

**What to notice:** Dry-run mode did its job — the user got the preview without commitment, and the saved-drafts option gives them something to iterate on before committing anything to GitHub. The skill also correctly filtered out validated solutions (those should become tasks via `/jeff:bdd`, not opportunity-exploration issues). Different artifacts create different issue types, and the filter keeps the distinction clean.
