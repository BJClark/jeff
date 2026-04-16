---
name: jeff-map
description: Create or update a user story map using Jeff Patton's backbone / walking skeleton / ribs methodology. Use when the user wants to map a product journey, plan an MVP slice, prioritise releases, or discuss user activities before features. Triggers on 'map the product', 'plan an MVP', 'slice a release', 'walking skeleton', 'user story mapping', 'backbone / skeleton / ribs'. Writes to .jeff/STORY_MAP.md.
argument-hint: "[focus: backbone|skeleton|ribs]"
allowed-tools:
  - AskUserQuestion
  - Read
  - Write
  - Edit
---

## When to use
- User says "let's map the product" / "map the onboarding flow" / "plan the MVP".
- User mentions backbone, walking skeleton, or ribs.
- User wants to slice work into Release 1 vs Future priorities.
- User is stuck describing features and needs to be pulled up to user activities.

## Inputs
- Required: `.jeff/STORY_MAP.md` (scaffolded by `/jeff:init`).
- Optional `$ARGUMENTS`: `backbone`, `skeleton`, or `ribs` — focus the session on one layer.

## Workflow

1. **Check project state.** Read `.jeff/STORY_MAP.md`. If `.jeff/` is missing, tell the user to run `/jeff:init` first and stop. If the file is missing but `.jeff/` exists, offer to recreate it from the template.

2. **Decide which layer to work on.**
   - Empty map → start with the backbone.
   - Backbone present, no skeleton → define the walking skeleton.
   - Both present → flesh out ribs (Release 1 and Future).
   - `$ARGUMENTS` overrides — go straight to that layer.

3. **Facilitate the chosen layer.** Ask one question at a time; do not dump the template.
   - **Backbone** (user activities): primary user, trigger, "done" condition, then 3–8 verb-first activities in narrative order. Keep them user-centric ("Discover recipes", not "Search API").
   - **Walking skeleton** (MVP slice): for each backbone column, the ONE story that keeps the end-to-end flow alive. If removing it leaves the flow intact, it belongs in ribs, not skeleton. Minimum *testable*, not minimum viable.
   - **Ribs** (Release 1 / Future): under each activity, add stories that solve real user pain the skeleton doesn't. Gate with "would you ship without it?" — Yes → Future, No → Release 1.

4. **Challenge solution-shaped stories.** If the user proposes a feature ("Add a recommendation engine"), push back to the underlying user activity ("Discover content they'll like"). Record the activity; let implementation flex later.

5. **Review mode.** When updating an existing map: walk the backbone left-to-right and ask what's missing between steps; confirm every skeleton cell is populated; ask "which Release 1 stories would you cut if the deadline slipped by a week?" and move those to Future.

6. **Write the updates.** Edit `.jeff/STORY_MAP.md` in place. Preserve the template's table structure and existing content the user didn't change. Remove HTML comment placeholders as you fill rows. One line per cell.

## Output
- Writes/edits `.jeff/STORY_MAP.md`. Preserves prior content. Never silently deletes a row.

## More
- Methodology and theory: `references/methodology.md`
- Common failures and fixes: `references/troubleshooting.md`
- Anti-patterns and redirects: `references/edge-cases.md`
- Worked examples: `examples/backbone-facilitation.md`, `examples/skeleton-slicing.md`, `examples/ribs-pruning.md`
