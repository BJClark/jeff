---
name: jeff-map
description: Create or update a user story map using Jeff Patton's backbone / walking skeleton / ribs methodology. Use when the user asks to "map the product", "plan an MVP", "slice a release", "work on the backbone/skeleton/ribs", or mentions user story mapping. Writes to .jeff/STORY_MAP.md.
allowed-tools: AskUserQuestion Read Write Edit
metadata:
  author: Will Clark
  version: "0.1.0"
  source-repo: https://github.com/BJClark/jeff
---

## Objective

Help the user create or update a User Story Map following Jeff Patton's methodology. The story map organises work around the user's journey (what the user DOES) before feature lists (what we BUILD).

## Process

### 1. Check project state

Use the Read tool to open `.jeff/STORY_MAP.md`. If the file doesn't exist, check whether `.jeff/` exists at all.

- If `.jeff/` is missing entirely, tell the user to run `jeff-init` first and stop.
- If `.jeff/` exists but `STORY_MAP.md` is missing, offer to recreate it from the template.

### 2. Decide which layer to work on

- **New or nearly empty map** — start with the backbone.
- **Backbone present, no walking skeleton** — define the walking skeleton.
- **Both present** — flesh out ribs (Release 1 and Future).

### 3. Facilitate by layer

#### Backbone (user activities)

Ask the user, in order:

1. "Who is the primary user / persona for this journey?"
2. "What triggers them to start this journey?"
3. "What does 'done' look like from their perspective?"
4. "Walk me through the 3-8 big activities they perform, start to finish, in narrative order."

Write activities left to right, one per column. Keep them verb-first and user-centric ("Discover recipes", not "Search API").

#### Walking skeleton (MVP slice)

For each backbone column, ask:

- "What is the ONE story we need here so the user can get end-to-end?"
- "If we removed this story, does the end-to-end flow still work?" (If yes, it belongs in ribs.)
- "Is this testable with real users in its simplest form?"

The walking skeleton is minimum testable, not minimum viable.

#### Ribs (Release 1 and Future)

Under each backbone column, for each story the user suggests:

- "What user problem does this solve that the skeleton doesn't?"
- "Which users feel this pain — all of them, or a segment?"
- "Would we ship without it? If yes, Future. If no, Release 1."

### 4. Review an existing map

1. Walk the backbone left-to-right and ask "what's missing between these?"
2. Check every skeleton cell is populated.
3. Ask "which Release 1 stories would you cut if the deadline slipped by a week?" — move those to Future.
4. Rewrite solution-fixated stories as activities.

### 5. Write the updates

Edit `.jeff/STORY_MAP.md` using the markdown table structure. Preserve existing content the user didn't change.

## Examples

**User says:** "Let's start mapping out the onboarding flow for this product."

Actions: Check `.jeff/STORY_MAP.md` exists. Facilitate backbone (3-8 top-level activities). Define walking skeleton. Write results.

Result: `.jeff/STORY_MAP.md` populated with backbone + walking skeleton.

## Troubleshooting

- **`.jeff/` missing.** Tell the user to run the init skill first.
- **User is describing features, not activities.** Redirect: "What is the user trying to do?"
- **Backbone has 15+ activities.** Too granular — group into 3-8 phases.
- **Walking skeleton has gaps.** Ask: "If this column has no skeleton story, how does the end-to-end flow work?"

## Methodology reference

User Story Mapping (Jeff Patton, *User Story Mapping*, O'Reilly 2014):

- Backbone: Narrative-ordered user activities (left to right).
- Walking skeleton: Minimum testable end-to-end flow.
- Ribs: Everything else, prioritised into Release 1 / Future.
- Slice horizontally for releases, not vertically by feature.
