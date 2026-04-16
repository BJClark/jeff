# Example: Pruning ribs with the "would you ship without it?" test

**User says:** "/jeff:map ribs — we have seven stories under Discover recipes and I can't decide what's Release 1."

**Context:** `.jeff/STORY_MAP.md` has a backbone and walking skeleton; the **Discover recipes** column has these proposed ribs:

1. Full-text search across recipe titles
2. Filter by cuisine (Italian, Thai, etc.)
3. Filter by dietary restriction (respects user's saved preference)
4. "Similar to" recommendations on each recipe card
5. Weekly "what's in season" curated list
6. Ingredient-first search ("I have broccoli and pasta")
7. Sharing a recipe to a friend via iMessage

**Claude's turn 1:** Apply the cut test, one story at a time.

> "Seven candidates. Let's go through them. **Full-text search across titles** — if the deadline slipped by a week and you had to cut this, would you ship Release 1 without it?"

**User:** "No. Without search, users are stuck scrolling the seeded list forever. Release 1."

**Claude's turn 2:**
> "**Filter by cuisine** — ship without it?"

**User:** "Probably yes. People will use search for that. Future."

**Claude's turn 3:**
> "**Filter by dietary restriction** — notice this one respects the preference we captured in the skeleton. Ship without it?"

**User:** "No, because the whole point of asking for dietary info was to use it. Release 1."

**Claude's turn 4:**
> "**'Similar to' recommendations on each recipe card** — ship without?"

**User:** "Yes. That's a nice-to-have discovery path, not the primary one. Future. Also — that feels like a recommendation engine hiding inside, which we haven't validated yet."

**Claude's turn 5:** Flag the embedded risk.

> "Good catch — I'll note that one as depending on a hypothesis about whether curation actually improves discovery. Consider pulling it up in `/jeff:hypothesis` before building. Next: **'What's in season' curated list** — ship without?"

**User:** "Yes. Future. It's seasonal so we can always add it in v2."

**Claude's turn 6:**
> "**Ingredient-first search ('I have broccoli and pasta')** — ship without?"

**User:** "Yes, but only because the search story handles 80% of that. Future, but high priority Future."

**Claude's turn 7:**
> "**Sharing a recipe to a friend** — ship without?"

**User:** "…actually no. That's how users came in via the iMessage link in the first place. Release 1."

**Claude summarises and writes:**

> "Release 1 under Discover recipes: full-text title search, dietary filter (respects saved preference), recipe sharing. Future: cuisine filter, 'similar to' recommendations (flagged for hypothesis first), seasonal list, ingredient-first search."

**Claude writes to `.jeff/STORY_MAP.md`:**

```diff
 ### Release 1
 
-| <!-- story --> | <!-- story --> | <!-- story --> | ... |
+| — | — | Title search; dietary filter; recipe sharing | — | — | — |
 
 ### Future
 
-| <!-- story --> | <!-- story --> | ... |
+| — | — | Cuisine filter; recommendations [hypothesis]; seasonal list; ingredient-first search | — | — | — |
```

**What to notice:** Two techniques in play. First, the cut-test ("would you ship without it?") forces a binary decision per rib, avoiding the usual "everything is P1" slide. Second, Claude caught that one rib ('similar to' recommendations) was actually an untested assumption in disguise and deferred it to `/jeff:hypothesis` instead of silently moving it forward. This is how the map hands work off to the OST and HDD skills without overstepping.
