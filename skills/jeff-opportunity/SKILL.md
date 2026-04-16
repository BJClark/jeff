---
name: jeff-opportunity
description: Create or update an Opportunity Solution Tree using Teresa Torres' continuous discovery methodology. Use when the user wants to connect a business outcome to customer opportunities, alternative solutions, and cheap experiments — or needs to resist solution fixation. Triggers on 'build an OST', 'opportunity solution tree', 'explore opportunities', 'map outcomes to solutions', 'desired outcome', 'experiment to run'. Writes to .jeff/OPPORTUNITIES.md.
allowed-tools:
  - AskUserQuestion
  - Read
  - Write
  - Edit
---

## When to use
- User says "build an OST" / "let's map opportunities" / "figure out what to build next".
- User proposes a specific solution before grounding it in a user need — redirect them here.
- User has a measurable outcome and needs to decompose it into opportunities and experiments.

## Inputs
- Required: `.jeff/OPPORTUNITIES.md` (scaffolded by `/jeff:init`).
- Optional context: `.jeff/research/INSIGHTS.md` and `USER_INTERVIEWS.md` — evidence for opportunities.

## Workflow

1. **Check project state.** Read `.jeff/OPPORTUNITIES.md`. If `.jeff/` is missing, tell the user to run `/jeff:init` first and stop. If the file is missing but `.jeff/` exists, offer to recreate from template.

2. **Anchor on the desired outcome.** Ask:
   - "What measurable business or user outcome are we trying to move?"
   - "Is it within our team's control to influence?"
   - "How will we know it moved — what metric and direction?"

   Push back on output-shaped answers ("Ship the mobile app"). A good outcome is user/business facing and measurable: "Reduce time-to-first-value from 8 min to under 2 min."

3. **Discover opportunities** (customer needs, NOT solutions). For each one:
   - **Statement** — "What is the user *struggling* to do, or *wanting* to do?" Phrase as a need, not a feature.
   - **Evidence** — research quote, usage data, observation. Unsupported opportunities get marked `Evidence: none yet — assumption`.
   - **Impact** — if solved perfectly, how much would it move the outcome? (H/M/L)

   If the user jumps to solutions, redirect: "Hold on — what's the underlying need?"

4. **Generate ≥3 solutions per opportunity.** Anti-solution-fixation rule: no evaluating any solution until at least three candidates exist, even obviously-worse ones.

5. **For each solution, name the riskiest assumption** ("what must be true for this to work, that's most likely wrong?") and **design the cheapest experiment** that could disprove it. Method selection lives in `references/experiment-methods.md`.

6. **Review mode.** For an existing tree:
   - Is the outcome still measurable and ours to influence? If not, rewrite.
   - Does every opportunity trace to evidence? Flag the ones that don't.
   - Does every opportunity have ≥3 solutions? If not, brainstorm more.
   - Does every chosen solution have an experiment targeting its riskiest assumption?

7. **Write the updates.** Edit `.jeff/OPPORTUNITIES.md` in place. Preserve the hierarchy (Outcome → Opportunity → Solutions → Assumptions/Experiment). Remove HTML comment placeholders as you fill them.

## Output
- Writes/edits `.jeff/OPPORTUNITIES.md`. Preserves prior content. If an insight from `research/` reinforces an opportunity, append to the Evidence field with a citation.

## More
- Methodology and theory: `references/methodology.md`
- Experiment method comparison: `references/experiment-methods.md`
- Common failures and fixes: `references/troubleshooting.md`
- Anti-patterns and redirects: `references/edge-cases.md`
- Worked examples: `examples/retention-ost.md`, `examples/redirect-from-solution.md`, `examples/refreshing-existing-ost.md`
