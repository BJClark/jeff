# Example: Slicing the walking skeleton

**User says:** "We have the backbone. Now let's do the walking skeleton for the onboarding flow."

**Context:** `.jeff/STORY_MAP.md` has the six-activity backbone from the previous example: *Sign in → Set preferences → Discover recipes → Save a recipe → Plan the week → Generate shopping list*.

**Claude's turn 1:** Confirm the scope and ask for the first column's skeleton story.

> "Six columns to fill. Let's go one at a time. For **Sign in** — what's the ONE story we need so the user can get past this step? Thinnest possible."

**User's answer:** "Email + password signup, no social login yet."

**Claude's turn 2:** Apply the cut test.

> "If we removed 'email + password signup', would the user still be able to reach Set preferences? No — so it belongs in the skeleton. Noted. Next: **Set preferences.**"

**User's answer:** "A multi-step wizard with dietary restrictions, household size, cuisine preferences, allergies, and cooking skill level."

**Claude's turn 3:** Push back — that's not a skeleton, it's a feature spec.

> "That's more than we need for a walking skeleton. Can the user reach Discover recipes without the full wizard? What's the thinnest version — maybe just one question, or even skippable?"

**User:** "…fair. Okay, just dietary restrictions. One screen. They can skip it."

**Claude's turn 4:** Accept the strip-down and continue.

> "One dietary question, skippable. That keeps the flow alive. **Discover recipes** next — what's the thinnest way a user can see *any* recipe?"

**User's answer:** "A simple scrollable list of 20 seeded recipes. No search, no filtering."

**Claude's turn 5:**
> "Good. **Save a recipe** — thinnest version?"

**User:** "A heart button on the recipe card."

**Claude's turn 6:**
> "**Plan the week**?"

**User:** "Saved recipes just appear in a flat 'This Week' list. No day assignment yet — we can test whether users even want day-by-day planning before we build it."

**Claude's turn 7:**
> "Good instinct — you're leaving room for learning. **Generate shopping list** last. Thinnest?"

**User:** "Combined ingredient list from the 'This Week' recipes. No de-duplication, no quantities merged. Just a dump."

**Claude writes to `.jeff/STORY_MAP.md`:**

```diff
 ## Walking Skeleton
 
-| <!-- Skeleton story 1 --> | <!-- Skeleton story 2 --> | ... |
+| Email + password signup | One dietary question (skippable) | Scrollable list of 20 seeded recipes | Heart button to save | Flat 'This Week' list | Combined ingredient dump |
```

**What to notice:** The user's second answer (the full preference wizard) violated the skeleton contract — Claude pushed back explicitly with "can the user reach Discover without this?" The correct skeleton answer emerged only after stripping. This is the skeleton facilitator's most important move: refuse adjectives.
