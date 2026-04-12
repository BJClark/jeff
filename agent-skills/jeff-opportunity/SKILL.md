---
name: jeff-opportunity
description: Create or update an Opportunity Solution Tree using Teresa Torres' continuous discovery methodology. Use when the user asks to "build an OST", "explore opportunities", "map outcomes to solutions", or mentions opportunities/experiments/desired outcomes. Writes to .jeff/OPPORTUNITIES.md.
allowed-tools: AskUserQuestion Read Write Edit
metadata:
  author: Will Clark
  version: "0.1.0"
  source-repo: https://github.com/BJClark/jeff
---

## Objective

Help the user create or update an Opportunity Solution Tree (OST) following Teresa Torres' continuous discovery methodology. The OST keeps the team focused on outcomes over outputs: business outcome, customer opportunities, multiple solutions, experiments.

## Process

### 1. Check project state

Use the Read tool to open `.jeff/OPPORTUNITIES.md`. If the file doesn't exist, check whether `.jeff/` exists at all.

- If `.jeff/` is missing entirely, tell the user to run `jeff-init` first and stop.
- If `.jeff/` exists but `OPPORTUNITIES.md` is missing, offer to recreate it from the template.

### 2. Anchor on the desired outcome

Ask: "What measurable business or user outcome are we trying to move?" Push back on output-shaped answers ("Ship the mobile app") — those are solutions. A good outcome is measurable: "Increase weekly active users by 20%".

### 3. Discover opportunities

For each opportunity: statement (user need, not feature), evidence (research backing), impact (High/Medium/Low). Redirect solution-shaped opportunities: "What's the underlying need?"

### 4. Generate multiple solutions per opportunity

At least three candidates per opportunity before evaluating any. For each: assumptions, riskiest assumption, cheapest experiment to test it.

### 5. Design experiments

Match method to risk: Concierge, Wizard of Oz, Fake door, Prototype, A/B test (from lightest to heaviest).

### 6. Write the updates

Update `.jeff/OPPORTUNITIES.md` in place, preserving hierarchy.

## Examples

**User says:** "We need to figure out what to build next to improve retention."

Actions: Confirm outcome as measurable target. Extract opportunities from research. Generate three solutions for top opportunity. Design one experiment. Write to `.jeff/OPPORTUNITIES.md`.

## Troubleshooting

- **Outcome is output-shaped.** Redirect: "What does launching it achieve for users?"
- **Opportunity has no evidence.** Mark as assumption and suggest interviews.
- **User fixates on one solution.** Require at least three alternatives.
- **Experiment too heavy.** Ask for the cheapest thing that would change their mind.

## Methodology reference

Opportunity Solution Trees (Teresa Torres, *Continuous Discovery Habits*, 2021): measurable outcome, evidence-backed opportunities, multiple solutions, small experiments testing riskiest assumptions.
