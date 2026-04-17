# Example: Building an OST for retention

**User says:** "We need to figure out what to build next to improve retention."

**Context:** `.jeff/OPPORTUNITIES.md` exists but is empty. `.jeff/research/INSIGHTS.md` has five synthesised insights from recent interviews.

**Claude's turn 1:** Anchor the outcome.

> "Retention on what timescale — D1, W1, M1? And what's the current baseline vs. the target?"

**User:** "W1. We're at 18% today. Goal is 30%."

**Claude's turn 2:** Confirm it's measurable and owned by the team.

> "Good — **Increase W1 retention from 18% to 30%** is our outcome. Is that fully in your team's control, or does it depend on marketing / sales?"

**User:** "Mostly us — the onboarding and first-week experience is ours."

**Claude's turn 3:** Pull evidence from existing insights before brainstorming.

> "Your `INSIGHTS.md` has five patterns. Three look relevant to W1 retention:
> - **I2**: users who complete the preference wizard retain 2× (12 interviews).
> - **I4**: users who save ≥3 recipes in week 1 retain 3× (usage data).
> - **I5**: users who share with a friend retain 5× (usage data, small N).
>
> Let's turn those into opportunities. First: **users struggle to complete the preference wizard** — your own data says the ones who do retain much better. Sound right?"

**User:** "Yes — the wizard has a 40% drop-off at step 3."

**Claude's turn 4:** Record the opportunity with evidence.

```markdown
## Opportunity O1: Users drop off the preference wizard before finishing
- **Evidence:** I2 (12 interviews), wizard analytics shows 40% drop at step 3.
- **Impact:** H — 2× retention for completers.
```

> "Now three candidate solutions for O1. We won't evaluate any until we have all three."

**User:** "One: shorten the wizard from 5 steps to 2. Two: make every step skippable. Three: replace the wizard with inline prompts inside the app."

**Claude's turn 5:** Record all three, then find the riskiest assumption on the most promising one.

> "All three recorded. On **Solution A (shorten to 2 steps)**, what must be true for this to work? Probably: 'the 3 dropped steps aren't actually necessary for good recommendations.' That's the riskiest — if it's wrong, recommendations get worse and retention drops *further*.
>
> Cheapest test: offline analysis of existing users who skipped steps vs. completed — do skippers get worse recommendations? If yes, Solution A is ruled out before we build anything."

**Claude writes to `.jeff/OPPORTUNITIES.md`:**

```markdown
## Desired Outcome
Increase W1 retention from 18% to 30%.

## Opportunity O1: Users drop off the preference wizard
- **Evidence:** INSIGHTS.md I2 (12 interviews); analytics (40% drop at step 3).
- **Impact:** H (2× retention for completers)

### Solution A: Shorten wizard to 2 steps
- **Assumption:** Steps 3–5 aren't necessary for good recommendations.
- **Experiment:** Offline analysis of existing users — compare recommendation quality for completers vs. drop-offs. 1 day.

### Solution B: Make every step skippable
- **Assumption:** Users who currently drop off would skip instead of abandoning.
- **Experiment:** Add skip buttons, measure completion rate for 1 week.

### Solution C: Replace wizard with inline prompts
- **Assumption:** Users will answer preference questions later in context.
- **Experiment:** Wizard of Oz — manually insert prompts into the app for 10 users, measure engagement.
```

**What to notice:** Claude drew evidence from existing `INSIGHTS.md` rather than brainstorming blind, forced three solutions before evaluating any, and picked a 1-day offline analysis as the first experiment — because the riskiest assumption (step necessity) could be tested against historical data without any new build. That's the OST working: cheap test, sharp assumption, alternatives preserved.
