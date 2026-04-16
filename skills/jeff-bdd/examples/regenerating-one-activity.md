# Example: Regenerating tasks for one changed activity

**User says:** "Just regenerate tasks for 'Plan the week' — we changed the story map."

**Context:** `.jeff/STORY_MAP.md` was edited: 'Plan the week' column now has a different walking-skeleton story ("Drag recipes to day slots" instead of the old "Flat 'This Week' list") and one new Release 1 story ("Copy last week's plan"). `.jeff/TASKS.md` has 9 existing tasks across all activities, including two under 'Plan the week' (T4, T5) with statuses `In Progress` and `Pending` respectively.

**Claude's turn 1:** Read both files, identify what's affected.

> "Located the 'Plan the week' column. Two existing tasks trace to it:
>
> - **T4** — 'User can see saved recipes in a flat This Week list' (**In Progress**, source: old skeleton).
> - **T5** — 'User can remove a recipe from This Week' (**Pending**).
>
> The new skeleton story ('Drag recipes to day slots') is a bigger behaviour than T4. Two options:"
>
> (AskUserQuestion)
> - "Replace T4 (keep as In Progress, update criteria to match new story)"
> - "Create new T10 for the new story, mark T4 as superseded"
> - "Keep T4 as-is (already in flight, don't disturb), add T10 alongside"

**User:** "Option 3 — T4 is already being built, we'll ship it and add day-slot dragging after."

**Claude's turn 2:** Create the new tasks, leave T4 alone, mark the story map overlap in Notes.

> "Keeping T4 unchanged. Creating two new tasks:"

```markdown
### T10: User can drag saved recipes onto day slots for the week
**Source:** STORY_MAP.md > Plan the week > Drag recipes to day slots
**Priority:** MVP (supersedes skeleton; T4 still ships as Release 1 behaviour)

**Description:**
Once a user has saved recipes this week, they can drag each recipe card onto a specific day of the week (Mon–Sun). Each day can hold multiple recipes.

**Acceptance Criteria:**
- [ ] The 'This Week' view shows seven day slots labelled Mon–Sun plus an unassigned saved-recipes pool.
- [ ] When the user drags a recipe from the pool onto a day slot, the recipe is assigned to that day.
- [ ] A recipe can be dragged between days; it appears only in its most recent destination.
- [ ] If the user drags a recipe off all slots (back into the pool), the day assignment is cleared.
- [ ] Day assignments persist across app restarts.
- [ ] The shopping-list generator combines ingredients across all assigned days, regardless of day.

**Notes:**
- Supersedes the flat-list behaviour from T4. T4 will still ship (engineering is mid-way); T10 arrives after.
- Depends on T4 (recipes must be saveable before they can be planned).
- Linked to Emerging Pattern EP2 in INSIGHTS.md ("users who plan by day retain better") — prioritise after T4.

### T11: User can copy last week's plan into this week
**Source:** STORY_MAP.md > Plan the week > Copy last week's plan
**Priority:** Release 1

**Description:**
On the 'This Week' screen, the user can tap 'Copy last week' to duplicate their previous week's day-slot assignments into the current week. The copy respects which recipes are still available in their saved list.

**Acceptance Criteria:**
- [ ] A 'Copy last week' button appears on the 'This Week' view if the user had day assignments last week.
- [ ] When tapped, the system copies each day's assignments from the previous week into the current week.
- [ ] Recipes removed from the saved list since last week are omitted from the copy; the system shows a toast: "3 recipes not available — replace or remove."
- [ ] If the user already has current-week assignments, the system asks to confirm replacement before copying.

**Notes:**
- Depends on T10 (day slots must exist).
- Traces to P4 interview ("I basically re-plan the same thing every week").
```

**Claude's turn 3:** Update the overview table and confirm.

> "Added T10 and T11, updated the overview table. T4 is unchanged (still `In Progress`). No criteria were modified on tasks outside 'Plan the week'.
>
> Note: T4 has a Notes entry about being superseded by T10 — engineering can read that and know the evolution path."

**What to notice:** The user's preference to keep T4 in flight shaped the outcome — the skill didn't force a "correct" regeneration over a practical one. Also, T10's Notes explicitly document that it supersedes T4. Without that note, future readers would see two tasks for similar behaviour and wonder which is authoritative.
