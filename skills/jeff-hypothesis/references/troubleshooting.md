# jeff-hypothesis — Troubleshooting

## `.jeff/` missing

Send the user to `/jeff:init`. Don't scaffold from here.

## Hypothesis isn't falsifiable

If the user can't describe a result that would *disprove* it, it's a wish, not a hypothesis. Refuse to record it until they can. Ask: "What number, if we saw it, would make you say 'we were wrong'?"

## No metric defined

Ask whether the metric exists today or needs instrumentation. If instrumentation is needed, note it as a prerequisite task — don't schedule the experiment until it can actually be measured. A hypothesis without live instrumentation is a plan, not a test.

## Threshold too vague

"We'll see if it helps" isn't a threshold. Push for a number, even a rough one. The threshold can be wrong and you'll learn anyway; the absence of a threshold turns the experiment into confirmation bias.

## Validation method too heavy

User proposes A/B test for a Low risk hypothesis. Suggest a fake door or prototype instead. A/B tests take weeks of traffic — save them for hypotheses that can't be answered cheaper.

## Validation method too light

User proposes a prototype for a "we'll charge 3× the current price" hypothesis. Prototypes can't answer pricing questions at scale. Ask: "Can this method produce the 'no' result credibly?" If not, escalate method.

## User wants to delete an invalidated hypothesis

Refuse. Move it to `## Invalidated` with the learning captured. Future-you needs to know what was tried. Deleting invalidated hypotheses is the fastest way to reinvent the same failures next quarter.

## Results inconclusive

If the result is directionally positive but below threshold, record as `Inconclusive`, not `Invalidated`. Then decide: rerun with more power, or abandon. Pretending inconclusive = invalidated hides the ambiguity.

## Experiment ran but was never recorded

Check `.jeff/research/VALIDATION_RESULTS.md`. If there's a matching experiment result sitting there un-linked, it's an unclosed loop — ask the user whether to import it.

## Hypothesis duplicates an existing one

Before creating a new H#, grep existing IDs for similar statements. If the duplicate is `Invalidated`, ask whether the user has new evidence that would change the outcome — if not, don't rerun; if yes, create a new hypothesis citing the previous result.
