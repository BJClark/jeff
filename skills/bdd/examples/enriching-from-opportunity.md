# Example: Enriching task Notes with opportunity context

**User says:** "Generate tasks for the 'Discover recipes' activity and pull in anything relevant from OPPORTUNITIES.md."

**Context:** `.jeff/STORY_MAP.md` has 'Discover recipes' with three Release 1 stories: **Title search**, **Dietary filter (respects saved preference)**, **Recipe sharing**. `.jeff/OPPORTUNITIES.md` has **O3** ("Users struggle to find recipes they'll cook") with three candidate solutions and a Wizard of Oz experiment run result showing curation outperformed the algorithmic alternative. `.jeff/TASKS.md` is empty.

**Claude's turn 1:** Read both files, identify which stories map to O3.

> "Three stories under 'Discover recipes'. All three are relevant to Opportunity O3 — they're the first Release 1 implementations of the 'curation beats filtering' insight. I'll note that on each task. Drafting now."

**Claude's turn 2:** Draft the three tasks with opportunity-enriched Notes.

```markdown
### T1: User can search recipes by title
**Source:** STORY_MAP.md > Discover recipes > Title search
**Priority:** Release 1

**Description:**
The user can type into a search field on the main recipe list and see results filtered by title match. Matching is case-insensitive and supports partial matches.

**Acceptance Criteria:**
- [ ] The main recipe list includes a search field at the top.
- [ ] When the user types 2+ characters, the list filters in real time (within 200ms per keystroke) to recipes whose title contains the typed string, case-insensitive.
- [ ] If no recipes match, the system shows "No recipes found — try a shorter search" with a link to clear the search.
- [ ] Clearing the search field restores the full list.
- [ ] Search state is not preserved across app restarts (per UX decision; each session starts fresh).

**Notes:**
- Traces to **Opportunity O3** ("Users struggle to find recipes they'll cook").
- Context from OPPORTUNITIES.md: The Wizard of Oz experiment on O3 showed human curation (Solution B) outperformed algorithmic matching (Solution A) for the home-cook segment. Search (this task) and dietary filter (T2) are the Release 1 bets — they support the *current* discovery flow. If adoption is low, curation becomes the Release 2 focus. Track search usage vs. discovery-via-scroll as a leading indicator.

### T2: User can filter recipes by their saved dietary preference
**Source:** STORY_MAP.md > Discover recipes > Dietary filter (respects saved preference)
**Priority:** Release 1

**Description:**
When the user has set a dietary preference during onboarding, the main recipe list defaults to filtering out recipes that don't match. They can toggle the filter off to see all recipes.

**Acceptance Criteria:**
- [ ] If the user has a saved dietary preference (not 'None'), the main list defaults to showing only matching recipes.
- [ ] A "Showing: Vegetarian recipes" chip (or equivalent label) is visible above the list indicating the active filter.
- [ ] When the user taps the chip, the filter clears and the full list displays, with a "Showing: All recipes" state.
- [ ] The filter state is independent of search — both can be applied simultaneously.
- [ ] If the user has no saved dietary preference (or 'None'), no filter is applied by default.

**Notes:**
- Traces to **Opportunity O1** ("Users drop off the preference wizard") AND **Opportunity O3**.
- The preference wizard exists *so that* this filter can be respected — without T2, O1's entire value proposition is unclear. This task closes the loop on asking for dietary prefs in onboarding (T2 in MVP).
- Depends on MVP task for preference capture during onboarding.

### T3: User can share a recipe to iMessage
**Source:** STORY_MAP.md > Discover recipes > Recipe sharing
**Priority:** Release 1

**Description:**
From any recipe card, the user can tap a share button and send a link to the recipe via iMessage (or any sharing target the OS supports). The shared link opens the recipe in the app if the recipient has it installed, or on the web if not.

**Acceptance Criteria:**
- [ ] Each recipe detail view includes a share button.
- [ ] Tapping share opens the system share sheet with a link and optional title preformatted.
- [ ] The shared link, when tapped by a recipient with the app installed, opens the app to that recipe.
- [ ] When tapped by a recipient without the app, the link opens the recipe on the web with a 'Get the app' prompt.
- [ ] Shared links do not expire and remain valid for at least 90 days.

**Notes:**
- Traces to **Opportunity O5** ("Users acquire via friend-to-friend share") — validated via P7 insight (retention 5× for users who shared).
- Also closes the acquisition loop that started the persona journey in STORY_MAP.md (the primary user "arrived via iMessage share from a friend").
- Consider instrumenting share-link click-through in Mixpanel to track the viral coefficient. Not a criterion but engineering should be aware.
```

**Claude's turn 3:** Summarise.

> "Three tasks, all Release 1, all linked to opportunities. T1 and T2 both trace to O3 (the 'struggle to find' opportunity); T2 also closes the loop on O1 (preference wizard); T3 traces to O5 (viral acquisition, validated by the 5× retention insight for sharers).
>
> Write to TASKS.md?"

**User:** "Yes."

**What to notice:** Enrichment from opportunities does three things well here. (1) It tells engineering *why* each task exists — not just what to build. (2) It flags cross-task dependencies that might not be obvious from the story map alone (T2 closes the loop on the MVP preference-capture task). (3) It surfaces measurement hints ("track search vs scroll", "instrument share-link CTR") that belong in Notes, not criteria. The result: tasks an engineer can pick up and prioritise with context, not just checkboxes.
