# jeff:opportunity — Troubleshooting

## `.jeff/` is missing

Send the user to `/jeff:init`. Don't scaffold from here.

## `.jeff/OPPORTUNITIES.md` is missing but `.jeff/` exists

Offer to recreate it from the template (`skills/init/templates/OPPORTUNITIES.md`). Don't proceed against a missing file.

## Outcome is output-shaped

Example: "Launch the new dashboard." Redirect: "What does launching it *achieve* for users or the business?" Push until the outcome is measurable. An outcome you can't measure is a goal, not an outcome.

## Opportunity has no evidence

Don't silently mark it as validated. Record it with `Evidence: none yet — assumption` and add "run interviews" as a research task. An unsupported opportunity is a hypothesis about customer needs, not a discovered one.

## User fixates on one solution

Refuse to move on until ≥3 alternatives exist, even if two are obviously worse. Solution fixation is the failure mode this framework is designed to prevent — the tree is not doing its job unless alternatives exist.

## Experiment is too heavy

"A/B test it for four weeks in production" is almost always too heavy for a new opportunity. Ask: "What's the *cheapest* thing that would change your mind about the riskiest assumption?" Usually concierge or fake door.

## Opportunity and solution are phrased the same way

If the opportunity is "Add recommendations" and the solution is "Recommendation engine", the opportunity is actually a solution in disguise. Rewrite the opportunity up one level: "Users struggle to find content they'll like."

## Metric requires instrumentation that doesn't exist

Note the instrumentation as a prerequisite task. Don't schedule the experiment until you can actually measure the thing you're claiming to measure.

## Opportunity moves no needle on the outcome

If the user says "impact: low" and the outcome is already modest, consider removing the opportunity — the tree is noisy, not exhaustive. Only opportunities that could plausibly move the outcome deserve tree space.
