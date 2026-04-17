# jeff:map — Anti-Patterns & Edge Cases

Each section names a failure mode, how to detect it, and what to redirect to.

## Solution-shaped stories

**Detection.** Story starts with a verb that belongs to the team ("Build", "Add", "Implement") or names a component ("the dashboard", "the recommendation engine", "the admin panel").

**Why it's bad.** A solution-shaped story locks in implementation before the user need is understood. It can't be compared to alternative solutions because it *is* the solution.

**Redirect.** Ask: "What is the user trying to do when they encounter this?" Write the activity. Capture the proposed solution as a candidate under that activity, not the activity itself.

## Output-shaped activities

**Detection.** An activity names a team deliverable ("Launch the mobile app", "Migrate to v2 API") instead of a user action.

**Why it's bad.** Activities are supposed to be user behaviour. Team outputs don't belong on the backbone — they belong in a roadmap or delivery plan.

**Redirect.** "What does launching the app *let the user do* that they can't do today?" Write that.

## Skeleton that's actually a rib

**Detection.** The proposed skeleton story, if removed, still leaves the end-to-end flow working. Or the story includes words like "with recommendations", "with filtering", "with analytics".

**Why it's bad.** The skeleton's whole job is to be the minimum that keeps the flow alive. If it has adjectives, it's already optional.

**Redirect.** Strip every adjective. Re-ask: "What's the thinnest version of this that keeps the user able to reach the next activity?"

## Skeleton that skips an activity

**Detection.** A backbone column has no skeleton cell.

**Why it's bad.** If users can't traverse that activity, they can't reach the activities downstream. The flow is broken.

**Redirect.** Either add a skeleton story or remove the backbone column. An activity with no skeleton is not an activity — it's an aspiration.

## Feature-fixation under an activity

**Detection.** The user proposes one rib and stops. Everything else under that column is empty.

**Why it's bad.** A single rib without alternatives is a commitment, not a candidate. Teams that map this way skip the comparison step and pick the first idea by default.

**Redirect.** "What are two other ways a user could solve this, even if they're worse?" Write them alongside. The decision comes later; first the map needs alternatives.

## Too many activities in the backbone (15+)

**Detection.** The backbone has more than 8 cells.

**Why it's bad.** A long backbone is either too granular (stories masquerading as activities) or too broad (multiple products on one map).

**Redirect.** Ask the user to group adjacent cells. Frame: "Which two of these would a user describe as the same phase?" Collapse until 3–8 remain.

## Too few activities in the backbone (1–2)

**Detection.** The backbone has only one or two cells.

**Why it's bad.** Under-specified. The user journey has structure — either you haven't elicited it or the mapped scope is too narrow.

**Redirect.** Ask the user to narrate a single user's day-in-the-life using the product. Every distinct phase becomes a column.

## Ambiguous priority semantics

**Detection.** Existing map uses labels the user introduced ("P0", "Must", "Critical") without a legend.

**Why it's bad.** Teams have different definitions. Silently normalising to Release 1 / Future will distort intent.

**Redirect.** Ask: "What does P0 mean for you — shipping in the next release, or shipping in the next sprint?" Then map to the template's Release 1 / Future columns explicitly.

## Narrative order broken

**Detection.** Activities are arranged by team, component, or alphabetical — not by the order a user performs them.

**Why it's bad.** The map loses its "reads like a sentence" property. Planning against it becomes harder because cross-column dependencies stop being obvious.

**Redirect.** Ask the user to re-tell the journey as a story. Reorder columns to match the narrative. Make a note if some activities are non-sequential (parallel or optional).
