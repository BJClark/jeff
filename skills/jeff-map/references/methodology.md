# User Story Mapping — Methodology

Based on Jeff Patton, *User Story Mapping* (O'Reilly, 2014). Patton's core move is to organise work around **what the user does**, not what the team builds. A flat backlog loses the narrative; a map preserves it.

## The three layers

### Backbone — user activities
The horizontal top row of the map. Each cell is a big activity the user performs, written verb-first and in narrative order left to right. A good backbone has 3–8 cells. It reads like a sentence: "Arrive → Discover → Choose → Transact → Follow up."

Rules of thumb:
- Activities, not features. "Discover recipes" is an activity; "Search bar" is a feature hiding under it.
- Narrative order. The backbone reads chronologically from the user's point of view, not by team or module.
- Stable. The backbone should stay relatively constant across releases; only the ribs below shift.

### Walking skeleton — minimum testable flow
One row beneath the backbone. Each cell is the single thinnest story that keeps the end-to-end flow alive for that activity. The skeleton is the smallest thing a real user can actually walk through from start to finish.

Crucially, the skeleton is **minimum testable**, not **minimum viable**. Viable implies it's good enough to ship; testable only implies it's good enough to observe a user using it. That distinction lets teams learn sooner.

### Ribs — Release 1 and Future
Everything else, organised under each backbone column. The Release 1 row is what you actually ship. The Future row is what you would build next (or never). Ribs are where feature-level stories live.

## How slicing works

- **Horizontal slicing = releases.** A release is a horizontal line across the map: the walking skeleton is Release 0; Release 1 is the next line down across every column.
- **Vertical slicing = features.** One column, top to bottom, is all the work on a single activity. Useful for ownership, dangerous for planning — you can't ship a column without the others.

Shipping is always a horizontal cut. Planning by column leads to systems that do one thing perfectly and the others not at all.

## Patton's test

> "If you're not talking about users and what they do, you're not story mapping."

Feature discussions have their place, but the map is not it. Keep the conversation at the activity level until the backbone and skeleton are solid; only then drop into ribs.

## Why backbone comes first

Teams that start with ribs end up with a bag of features they can't prioritise because there's no spine to prioritise against. The backbone gives every future story a home and a comparison ("does this help Discover or Transact?"). Without it, every feature looks equally important.

## Why skeleton comes before ribs

The walking skeleton forces the team to agree on what "end-to-end" means. Until that line exists, every rib looks optional; once it exists, everything else is explicitly a bet about which activity to strengthen first.
