# jeff:opportunity — Anti-Patterns & Edge Cases

## Output-shaped outcome

**Detection.** Outcome names a deliverable, not a result: "Launch the mobile app", "Complete the migration", "Ship v2".

**Why it's bad.** Deliverables have no direction. You can "launch" a mobile app that moves no metric; the tree then points at activity, not value.

**Redirect.** "What does launching it *let users do differently* — and what number moves as a result?"

## Solution-disguised-as-opportunity

**Detection.** Opportunity reads like "Add X" or "Build Y" or names a component.

**Why it's bad.** Solutions can't be compared to alternative solutions — they're already committed.

**Redirect.** Walk up to the underlying need. "What is the user *trying to do* when they'd encounter this feature?" That answer is the opportunity.

## Evidence-free opportunity

**Detection.** The user proposes an opportunity and can't cite an interview, observation, or data point.

**Why it's bad.** You're making up user needs. The opportunity might be real, but right now it's a guess.

**Redirect.** Don't refuse to record it — mark it `Evidence: none yet — assumption` and add it as a research priority. Record the guess, but record it honestly.

## Solution fixation (one candidate per opportunity)

**Detection.** The user proposes one solution and wants to move on to experiments.

**Why it's bad.** A single candidate is a commitment, not a choice. The OST's value comes from comparison.

**Redirect.** "What are two other ways to solve this, even if they're worse?" Refuse to design an experiment until three solutions exist.

## Evaluating solutions before all candidates are on the table

**Detection.** User writes three solutions, then immediately crosses out two.

**Why it's bad.** Premature evaluation narrows the tree without evidence. The "obviously worse" solution often surfaces criteria you hadn't articulated.

**Redirect.** "Keep all three for now. What assumption would we test to know which is best?"

## Experiment tests the wrong thing

**Detection.** The experiment tests whether users *use* the solution, but the riskiest assumption is whether they *want* it.

**Why it's bad.** A usability test can't answer a desirability question.

**Redirect.** "Write the assumption as one sentence. Does this experiment disprove that sentence if it fails?" If not, redesign.

## A/B test by default

**Detection.** Every experiment in the tree is an A/B test.

**Why it's bad.** A/B tests are the heaviest method — weeks of traffic, engineering to run both variants. Used by default, they slow discovery to a crawl.

**Redirect.** For each A/B test, ask: "What's the cheapest method that could disprove this assumption?" Most of the time it's concierge or fake door.

## Tree hasn't changed in weeks

**Detection.** Git blame on `OPPORTUNITIES.md` shows no edits in >30 days.

**Why it's bad.** The OST is supposed to be a living artifact. A static tree is being ignored, not validated.

**Redirect.** In review mode, prompt: "What have we learned since we last touched this?" Update or deprecate opportunities based on recent research.

## Outcome owned by someone else

**Detection.** The outcome is "increase revenue" but the team has no influence on pricing, marketing, or sales.

**Why it's bad.** The team can't move the metric — the tree will produce frustration, not progress.

**Redirect.** Find a downstream outcome the team *can* move. "What metric upstream of revenue is within our control?"
