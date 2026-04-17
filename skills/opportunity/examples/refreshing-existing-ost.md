# Example: Reviewing and refreshing a stale OST

**User says:** "Look over our OPPORTUNITIES.md — it's a few months old and I'm not sure it still reflects where we are."

**Context:** `.jeff/OPPORTUNITIES.md` has one outcome, four opportunities, eleven solutions, and six experiments — most recorded six weeks ago. `.jeff/research/INSIGHTS.md` has grown since.

**Claude's turn 1:** Read both files and apply the review checklist.

> "Reviewed both. Four findings:
>
> 1. **Outcome drift.** Outcome is 'Increase W1 retention to 30%.' Actual W1 retention is now 27%. Outcome is still valid but close to done — you may want to retire this tree and start a new one soon.
>
> 2. **O2 has no evidence.** 'Users want mobile notifications' was recorded six weeks ago with `Evidence: none`. Still `none` today. Either interview this out or drop it — it's been sitting as an assumption for a month and a half.
>
> 3. **O3 has only one solution.** 'Users struggle during checkout' has exactly one candidate ('Add Apple Pay'). That's solution fixation — we need two more candidates before the experiment matters.
>
> 4. **Experiment on S4 ran and was never recorded.** Your `VALIDATION_RESULTS.md` has results from the Apple Pay fake door test on 2026-02-14, but `OPPORTUNITIES.md` still shows it as 'pending'. The loop isn't closed."

**Claude's turn 2:** Ask the user to prioritise.

> "Four things to address. Which first?"
> (AskUserQuestion options: "Close the S4 loop with real results", "Generate the missing O3 solutions", "Decide on O2 — interview or drop", "All of the above in order")

**User:** "All of the above in order."

**Claude's turn 3:** Work through them.

> "Starting with S4. Your `VALIDATION_RESULTS.md` says Apple Pay fake door saw 12% click-through — above the 8% threshold you set. Marking S4's experiment **validated** and its solution **greenlit for real build**. Updating OPPORTUNITIES.md now."

**Claude edits:**
```diff
 ### Solution S4: Add Apple Pay
-- Experiment: Fake door button on checkout page. Status: pending.
+- Experiment: Fake door button on checkout page.
+- Result (2026-02-14): 12% CTR, above 8% threshold. **Validated.**
+- Decision: Greenlit for real build.
```

> "Next — O3 solutions. Beyond Apple Pay, what are two other candidates for 'users struggle during checkout'?"

**User:** "Guest checkout. And storing card-on-file from the free trial."

**Claude:** Records both; assumes riskiest assumptions ('guests convert as well as account-holders', 'users who trial will consent to card storage'); proposes fake-door tests for each.

> "O2 last. 'Users want mobile notifications' — six weeks with no evidence. Want me to (a) add 'interview 5 users about notification preferences' to research priorities and keep O2 in the tree as an assumption, or (b) drop O2 for now until evidence appears?"

**User:** "(a). I'll schedule the interviews."

**Claude:** Keeps O2, adds the research task to `INSIGHTS.md` with an action flag.

**What to notice:** Review mode isn't just reading — it's closing feedback loops. The skill caught a stale experiment result (the loop wasn't being closed manually), flagged a solution-fixated opportunity, and demanded a decision on an assumption-based opportunity rather than letting it rot. The OST is supposed to be alive; this is what "alive" looks like.
