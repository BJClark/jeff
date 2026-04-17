# Opportunity Solution Trees — Methodology

Based on Teresa Torres, *Continuous Discovery Habits* (Product Talk, 2021). The OST is a tool for keeping a team anchored on **outcomes over outputs** — the tree structure forces every proposed build to trace up to a user need and a business result.

## The four layers

### Desired outcome (trunk)
A measurable, team-influenceable business or user result. "Increase weekly active users by 20%" works; "Ship the mobile app" doesn't. The outcome is the only reason the tree exists — everything below is in service of moving this number.

Outcome hygiene:
- **Measurable.** There's a number and a direction.
- **Team-controllable.** The team can plausibly move it (not stock price, not macroeconomic indicators).
- **User- or business-facing.** Not an internal engineering metric (code coverage, deploy frequency).

### Opportunities (major branches)
Customer needs discovered through research. Each is phrased as a user struggle or desire: "Users struggle to find recipes they'll actually cook." Opportunities are **never solutions** — no feature names, no components, no "add X."

Each opportunity gets:
- An **evidence** list (quotes, usage data, observations from interviews).
- An **impact estimate** (H/M/L) of how much solving it would move the outcome.

### Solutions (sub-branches)
Candidate ways to address an opportunity. The rule: **at least three solutions per opportunity, generated before any are evaluated**. This is the single most important move in Torres' method — it defeats solution fixation.

A single solution isn't a choice; it's a commitment. Three solutions (even if two are obviously worse) force the team to reason about trade-offs.

### Experiments (leaves)
The cheapest possible test of a solution's riskiest assumption. The goal is not to prove the solution works — it's to disprove a specific assumption cheaply. If the assumption survives, you've learned something; if it doesn't, you've saved the cost of building the wrong thing.

## The tree is alive

Torres' framing: the OST is a working document, not a static plan. Expect it to change weekly as research lands and experiments resolve. A tree that hasn't changed in a month is probably being ignored, not validated.

## Why outcomes over outputs

Output-driven teams ship features. Outcome-driven teams move metrics. The tree makes the difference concrete: every proposed output has to trace up to an opportunity and an outcome, or it doesn't belong in the tree.

## Why ≥3 solutions per opportunity

When a team generates only one solution per need, they commit to it by default. Torres' data: teams that force themselves to generate three solutions find that the "obvious" first solution is the chosen one less than half the time. The comparison forces criteria to surface.

## Why "cheapest experiment" beats "best experiment"

A/B tests feel rigorous but take weeks of traffic and engineering. Concierge and Wizard of Oz tests feel scrappy but resolve the underlying assumption in days. Match rigour to risk: high-stakes assumptions deserve heavier methods; low-stakes ones deserve the fastest answer that's credible enough to act on.

## Relation to other jeff artifacts

- `STORY_MAP.md` — the backbone/activities inform which opportunities even make sense to discover.
- `HYPOTHESES.md` — an experiment in the OST usually gets formalised as a hypothesis once it's scheduled.
- `research/INSIGHTS.md` — synthesised patterns become evidence rows on opportunities.
