---
name: jeff:opportunity
description: Create or update an Opportunity Solution Tree using Teresa Torres' continuous discovery methodology. Use when the user asks to "build an OST", "explore opportunities", "map outcomes to solutions", or mentions opportunities/experiments/desired outcomes. Writes to .jeff/OPPORTUNITIES.md.
allowed-tools:
  - AskUserQuestion
  - Read
  - Write
  - Edit
---

## Objective

Help the user create or update an Opportunity Solution Tree (OST) following Teresa Torres' continuous discovery methodology. The OST keeps the team focused on **outcomes over outputs**: business outcome → customer opportunities → multiple solutions → experiments that test the riskiest assumptions.

## Process

### 1. Check project state

Use the Read tool to open `.jeff/OPPORTUNITIES.md`. If the file doesn't exist, check whether `.jeff/` exists at all.

- If `.jeff/` is missing entirely, tell the user to run `/jeff:init` first and stop.
- If `.jeff/` exists but `OPPORTUNITIES.md` is missing, offer to recreate it from the template.

### 2. Anchor on the desired outcome

Ask explicitly:

- "What measurable business or user outcome are we trying to move?"
- "Is it within our team's control to influence?"
- "How will we know it's moved — what's the metric and the direction?"

Push back on output-shaped answers ("Ship the mobile app") — those go *below* the outcome as solutions, not at the top. A good outcome is measurable and user/business facing: "Increase weekly active users by 20%", "Reduce time-to-first-value from 8 min to under 2 min".

### 3. Discover opportunities (customer needs, NOT solutions)

For each opportunity, walk the user through:

1. **Statement** — "What is the user *struggling* to do, or *wanting* to do?" Phrase as a need, not a feature. ("Users struggle to find relevant content", not "Add a recommendation engine".)
2. **Evidence** — "What research supports this? Interview quote, usage data, observation?" An opportunity without evidence is a guess; mark it as such.
3. **Impact** — "If we solved this perfectly, how much would it move the desired outcome?" (High / Medium / Low.)

If the user is jumping to solutions, redirect: "Hold on — what's the underlying need this solution serves?"

### 4. Generate multiple solutions per opportunity

For every opportunity, generate **at least three** candidate solutions before evaluating any of them. This is the anti-solution-fixation rule.

For each solution ask:

- "What must be true for this to work?" (assumptions)
- "What's the riskiest of those assumptions — the one most likely to be wrong?"
- "What's the cheapest way to test just that assumption?" (experiment)

### 5. Design experiments

For each solution's riskiest assumption, define an experiment. Match the method to the risk level:

- **Concierge**: manually deliver the service end-to-end. Cheapest way to learn.
- **Wizard of Oz**: fake automation, real human delivery behind it.
- **Fake door**: measure interest before building.
- **Prototype**: low-fidelity clickable test.
- **A/B test**: production comparison (heaviest — only once cheaper tests point one way).

### 6. Review an existing OST

When updating rather than creating:

1. Is the outcome still measurable and within our control? If not, rewrite it.
2. Does every opportunity trace back to evidence? Flag the ones that don't.
3. Does every opportunity have ≥ 3 solutions? If not, brainstorm more.
4. Does every chosen solution have an experiment testing its riskiest assumption?

### 7. Write the updates

Update `.jeff/OPPORTUNITIES.md` in place. Preserve the template's hierarchy (Desired Outcome → Opportunity → Solutions → Assumptions/Experiment). Remove HTML comment placeholders as you fill sections in.

## Examples

**User says:** "We need to figure out what to build next to improve retention."

Actions:
1. Confirm outcome: "Retention on what timescale — D1, W1, M1?" Write it as a measurable target.
2. Ask what research exists; extract opportunities from it. If nothing exists, name the gap and suggest interviews.
3. For the top opportunity, generate at least three candidate solutions.
4. Pick the riskiest assumption across those solutions and design one cheap experiment.
5. Write the results to `.jeff/OPPORTUNITIES.md`.

Result: An OST with a measurable outcome, one evidence-backed opportunity, three solutions, and one experiment ready to run.

---

**User says:** "I want to add a recommendation engine."

Actions:
1. Stop and redirect: "That's a solution. What user need is it serving?" Walk the user up to the opportunity layer.
2. Once the opportunity is clear ("Users struggle to find relevant content"), ask for evidence.
3. Ensure at least two other candidate solutions exist alongside "recommendation engine" before committing to it.
4. Pick an experiment — probably a Wizard of Oz curated list — to test whether curation actually improves discovery before building ML.

Result: The proposed solution is placed in the OST under the right opportunity, alongside alternatives, with an experiment.

## Troubleshooting

- **`.jeff/` missing.** Send the user to `/jeff:init` first.
- **`.jeff/OPPORTUNITIES.md` missing but `.jeff/` exists.** Offer to recreate it from the template.
- **Outcome is output-shaped** ("Launch the new dashboard"). Redirect: "What does launching it *achieve* for users or the business?" Push until the outcome is measurable.
- **Opportunity has no evidence.** Don't silently pretend it's validated. Mark it `Evidence: _none yet — assumption_` and add "run interviews" as a research task.
- **User fixates on one solution.** Refuse to move on until at least three alternatives exist, even if two are "obviously worse". Solution fixation is the failure mode this framework is designed to prevent.
- **Experiment is too heavy** (e.g. "A/B test it for four weeks in production"). Ask what the *cheapest* thing is that would change your mind about the assumption. Usually it's a concierge or fake-door test.

## Methodology reference

Opportunity Solution Trees (Teresa Torres, *Continuous Discovery Habits*, Product Talk LLC 2021):

- Start with a clear, measurable **desired outcome** the team can influence.
- Discover **opportunities** through continuous research (never a one-time interview round).
- Generate **multiple solutions** per opportunity to resist premature commitment.
- Design **small experiments** to test the riskiest assumption cheapest.
- The tree is a working document — expect it to change weekly.
