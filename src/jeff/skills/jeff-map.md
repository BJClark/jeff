---
name: jeff:map
description: Create or update a user story map using Jeff Patton's backbone / walking skeleton / ribs methodology. Use when the user asks to "map the product", "plan an MVP", "slice a release", "work on the backbone/skeleton/ribs", or mentions user story mapping. Writes to .jeff/STORY_MAP.md.
argument-hint: "[focus: backbone|skeleton|ribs]"
allowed-tools:
  - AskUserQuestion
  - Read
  - Write
  - Edit
---

## Objective

Help the user create or update a User Story Map following Jeff Patton's methodology. The story map organises work around the user's journey (what the user DOES) before feature lists (what we BUILD).

## Arguments

Optional focus area: `$ARGUMENTS`

- `backbone` — concentrate on the high-level user activities
- `skeleton` — concentrate on the minimum end-to-end slice (walking skeleton)
- `ribs` — concentrate on additional stories under each backbone item
- (none) — work on whichever layer the map needs most

## Process

### 1. Check project state

Use the Read tool to open `.jeff/STORY_MAP.md`. If the file doesn't exist, check whether `.jeff/` exists at all.

- If `.jeff/` is missing entirely, tell the user to run `/jeff:init` first and stop.
- If `.jeff/` exists but `STORY_MAP.md` is missing, offer to recreate it from the template before proceeding (see Troubleshooting).

### 2. Decide which layer to work on

- **New or nearly empty map** → start with the backbone.
- **Backbone present, no walking skeleton** → define the walking skeleton.
- **Both present** → flesh out ribs (Release 1 and Future).
- **Explicit `$ARGUMENTS`** → go straight to that layer.

### 3. Facilitate by layer

#### Backbone (user activities)

Ask the user, in order:

1. "Who is the primary user / persona for this journey?"
2. "What triggers them to start this journey?"
3. "What does 'done' look like from their perspective?"
4. "Walk me through the 3–8 big activities they perform, start to finish, in narrative order."

Write activities left to right, one per column. Keep them verb-first and user-centric ("Discover recipes", not "Search API").

#### Walking skeleton (MVP slice)

For **each** backbone column, ask:

- "What is the ONE story we need here so the user can get end-to-end?"
- "If we removed this story, does the end-to-end flow still work?" (If yes → it belongs in ribs, not skeleton.)
- "Is this testable with real users in its simplest form?"

The walking skeleton is **minimum testable**, not minimum viable. It should be the thinnest possible line through every backbone activity.

#### Ribs (Release 1 and Future)

Under each backbone column, for each story the user suggests:

- "What user problem does this solve that the skeleton doesn't?"
- "Which users feel this pain — all of them, or a segment?"
- "Would we ship without it? If yes → Future. If no → Release 1."

Challenge solution-shaped stories ("Add a recommendation engine") — push back to the underlying user need and capture the *activity*, letting implementation flex.

### 4. Review an existing map

When updating rather than creating:

1. Walk the backbone left-to-right and ask "what's missing between these?"
2. Check every skeleton cell is populated — gaps block end-to-end flow.
3. Ask "which Release 1 stories would you actually cut if the deadline slipped by a week?" — move those to Future.
4. Look for solution-fixated stories ("Build the admin dashboard") and rewrite as activities.

### 5. Write the updates

Edit `.jeff/STORY_MAP.md` using the markdown table structure the template established. Preserve existing content the user didn't change. Keep cells short — one line each — and use the HTML comments in the template as placeholders, removing them once a row is filled.

## Examples

**User says:** "Let's start mapping out the onboarding flow for this product."

Actions:
1. Check `.jeff/STORY_MAP.md` exists.
2. Facilitate backbone: walk the user through the 3–8 top-level activities a new user performs from signup to first value.
3. Define the walking skeleton — the single thinnest story per activity.
4. Write the results to `.jeff/STORY_MAP.md`.

Result: `.jeff/STORY_MAP.md` populated with a backbone + walking skeleton for onboarding.

---

**User says:** "/jeff:map ribs — I want to flesh out Release 1 under each activity."

Actions:
1. Read the existing map; note which backbone columns already have ribs and which don't.
2. For each activity, ask for the 2–4 stories that would make Release 1 stronger, prompting with "what does the user still struggle with after the skeleton?"
3. Challenge each one with "would you ship without it?" and sort into Release 1 vs Future.
4. Update the `### Release 1` and `### Future` tables in place.

Result: Release 1 and Future rows filled in under the existing backbone.

## Troubleshooting

- **`.jeff/` missing.** Tell the user: "Run `/jeff:init` to scaffold the project, then come back." Do not create `.jeff/` from this skill.
- **`.jeff/STORY_MAP.md` missing but `.jeff/` exists.** The init skill didn't finish, or the file was deleted. Offer to recreate it from the template before proceeding.
- **User is describing features, not user activities.** Redirect: "Before we talk about the feature, what is the user *trying to do* when they need this?" Keep the backbone at the user-activity level.
- **Backbone has 15+ activities.** Too granular — those are probably stories, not activities. Ask the user to group them into 3–8 higher-level phases.
- **Walking skeleton is missing in some columns.** The user may be protecting those as "not in scope." Ask explicitly: "If this column has no skeleton story, how does the end-to-end flow work?" Either add a story or remove the column.
- **Existing map has ambiguous priority labels.** Ask the user what each label means for them before editing — don't silently normalise.

## Methodology reference

User Story Mapping (Jeff Patton, *User Story Mapping*, O'Reilly 2014):

- **Backbone**: Narrative-ordered user activities (left to right).
- **Walking skeleton**: Minimum *testable* end-to-end flow — one story per backbone activity.
- **Ribs**: Everything else, prioritised into Release 1 / Future.
- Slice horizontally for releases, not vertically by feature.
- "If you're not talking about users and what they do, you're not story mapping."
