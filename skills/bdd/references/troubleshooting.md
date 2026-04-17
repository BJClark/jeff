# jeff:bdd — Troubleshooting

## `.jeff/` missing

Send user to `/jeff:init`.

## Story map is empty (only placeholders)

Tell the user: "The story map has no real stories yet. Run `/jeff:map` to populate the backbone, walking skeleton, or ribs first."

## Tech-shaped task titles

Story is phrased as engineering work ("Build REST API for X"). Rewrite as user behaviour ("User can retrieve X") and push implementation detail to Notes. The `/jeff:map` skill is supposed to catch this upstream — if it didn't, this skill cleans up.

## Too many acceptance criteria (8+)

The task is probably too big. Suggest splitting into two tasks — often one for happy path and one for edge cases, or one per sub-behaviour. Offer specific split suggestions, don't just say "this is too big."

## Acceptance criteria have implementation details

Remove mentions of specific frameworks, database schemas, API shapes, class names. Those belong in engineering design, not acceptance tests. Rewrite as what the user observes or what the system does.

## Criteria use fuzzy language

"Fast", "intuitive", "delightful", "user-friendly" — not testable. Ask for a specific threshold (ms, click count, completion rate) or drop the criterion.

## Task duplicates an existing one

If a new story overlaps an existing task, don't create a duplicate. Add a note to the existing task: "Updated from STORY_MAP.md on [date] — [what changed]." Or propose merging the two stories in the map.

## Priority mismatch

A walking-skeleton story wants Release 1 priority, or vice versa. Don't silently override — ask: "Story is in the walking skeleton, so I've marked it MVP. Confirm or change?"

## User wants to regenerate but preserve statuses

Default behaviour: preserve statuses on existing tasks; only add new tasks for new stories. If the user wants a full regeneration, confirm explicitly before overwriting — the `In Progress` tasks are engineering's current work.

## Story map uses non-standard labels

If the map has priority labels the skill doesn't recognise (P0/P1/P2 instead of MVP/R1/Future), ask: "Your story map uses P0/P1/P2. Map them as P0=MVP, P1=Release 1, P2=Future, or something else?"
