# Example: Full story-map-to-tasks generation

**User says:** "Let's turn the story map into tasks."

**Context:** `.jeff/STORY_MAP.md` has a populated backbone, walking skeleton, and Release 1 ribs (see `skills/map/examples/` for the underlying content). `.jeff/OPPORTUNITIES.md` exists with opportunities O1–O3. `.jeff/TASKS.md` is template-only.

**Claude's turn 1:** Read everything, summarise what will be generated.

> "Read your story map, opportunities, and empty tasks file. Planning to generate:
>
> - **6 walking-skeleton tasks (MVP)** — one per backbone column.
> - **3 Release 1 tasks** — title search, dietary filter, recipe sharing under 'Discover recipes'.
> - **0 Future tasks** — you said hold those until MVP lands.
>
> Opportunity enrichment: **O1** links to one MVP task (preference onboarding), **O3** links to three Release 1 tasks.
>
> Want me to draft them?"

**User:** "Yes."

**Claude's turn 2:** Draft tasks (first two shown here; full list would continue through T9).

```markdown
### T1: New user can sign up with email and password
**Source:** STORY_MAP.md > Sign in > Email + password signup
**Priority:** MVP

**Description:**
A new user arriving via share link can create an account with their email address and a password, and is taken into the onboarding flow.

**Acceptance Criteria:**
- [ ] The signup form shows fields for email and password and a 'Create account' button.
- [ ] When the user submits with a valid email and a password of 8+ characters, an account is created and they're signed in.
- [ ] If either field is empty on submit, the system shows an inline error next to the empty field and does not create an account.
- [ ] If the email is already registered, the system shows "Account exists — sign in instead" with a link to the sign-in flow.
- [ ] On successful signup, the user is routed to the first onboarding screen.

**Notes:**
- Walking skeleton story — keep it minimal. Social login is Future.
- No email verification in MVP (Release 1 concern).

### T2: New user can answer one dietary-preference question
**Source:** STORY_MAP.md > Set preferences > One dietary question (skippable)
**Priority:** MVP

**Description:**
During onboarding, the user is asked a single dietary-restriction question. They can answer or skip. The answer (if any) is persisted to their profile and feeds recipe filtering.

**Acceptance Criteria:**
- [ ] After signup, the user sees a screen with one question ("Do you follow a specific diet?") and four options (None, Vegetarian, Vegan, Gluten-free).
- [ ] When the user selects an option and taps 'Continue', the selection is saved to their profile.
- [ ] When the user taps 'Skip', no preference is saved and they proceed to the next screen.
- [ ] The saved preference is readable from the profile API in subsequent sessions.

**Notes:**
- Linked to Opportunity O1 ("Users drop off the preference wizard"), Solution A (shorten to minimal).
- MVP deliberately excludes the full 5-step wizard. If this validates, expand in Release 1.
- Depends on T1 (signup must complete first).
```

**(Tasks T3–T9 continue similarly.)**

**Claude's turn 3:** Present summary.

> "Drafted 9 tasks — 6 MVP, 3 Release 1. Four of them link to opportunities. Want to adjust any priorities or criteria before I write to `TASKS.md`?"

**User:** "T5 acceptance criteria — the heart button task. 'Persists across app restarts' should be split from the save criteria."

**Claude's turn 4:** Split the criterion and ask about anything else.

> "Updated T5 — persistence is now its own criterion ('The saved recipe is retained after quitting and reopening the app'). Anything else?"

**User:** "No, write them."

**Claude writes to `.jeff/TASKS.md`** — full overview table at top, nine task sections, all `Pending`.

**What to notice:** Three moves. First, Claude previewed the generation (counts per priority, opportunity linkages) before drafting — gave the user a chance to reshape scope cheaply. Second, draft tasks were presented *before* writing, so adjustments happened against drafts, not committed content. Third, the user's adjustment request ("split the persistence criterion") was taken at face value and applied precisely — no re-opening the broader task structure.
