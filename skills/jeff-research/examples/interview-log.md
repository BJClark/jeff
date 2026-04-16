# Example: Logging a single interview

**User says:** "I just finished an interview with a beta user, let me log it."

**Context:** `.jeff/research/USER_INTERVIEWS.md` exists with 2 prior interviews. This will be the 3rd.

**Claude's turn 1:** Read the file, establish the next participant ID, and start with the Participant field.

> "Next participant is P3. Who are they? Role, background, how you recruited them, and what they use today."

**User:** "Home cook, plans meals for family of 4. Recruited from the beta list. Currently uses a paper notebook and Pinterest."

**Claude's turn 2:** Record Participant, ask for Key Quotes.

> "Got it. **Key quotes** — give me 2–3 things they said, verbatim, that captured the problem or surprised you. Actual words, not summaries."

**User:** "She said 'I always end up cooking the same three things because the list is overwhelming.' And 'I spend my Sunday evenings trying to remember what we ate last week.'"

**Claude's turn 3:** Record the quotes in quotation marks. Ask for Observations.

> "Good — in the notes now. **Observations**: what did you *see her do*, separate from what she said?"

**User:** "She opened the app, scrolled through 40 recipes in under a minute, then closed it without saving anything. And she said the app was 'fine' but hesitated before every tap in the onboarding."

**Claude's turn 4:**

> "Those are gold — behaviour that contradicts reported preference. **Pain points** — what did she explicitly name as frustrations?"

**User:** "No way to filter by cook time. Shopping list doesn't de-duplicate ingredients. Had to re-enter diet prefs on web after setting on mobile."

**Claude's turn 5:**

> "**Goals / desires** — what's she trying to accomplish?"

**User:** "Cook something new each week without spending an hour planning. Feel organised by Sunday night."

**Claude's turn 6:**

> "**Follow-up questions** — what do you wish you'd asked?"

**User:** "Whether she uses a shopping app today, and what she means by 'overwhelming' — too many options or the wrong options."

**Claude appends to `.jeff/research/USER_INTERVIEWS.md`:**

```markdown
## P3 — 2026-04-16
**Role**: Home cook, family of 4. Beta list recruit. Currently uses paper notebook + Pinterest.

### Key Quotes
- "I always end up cooking the same three things because the list is overwhelming."
- "I spend my Sunday evenings trying to remember what we ate last week."

### Observations
- Scrolled through 40 recipes in <1 minute, closed app without saving.
- Said the app was "fine" but hesitated before every tap in onboarding.

### Pain Points
- No filter by cook time.
- Shopping list doesn't de-duplicate ingredients.
- Re-entered diet preferences on web after mobile setup (sync gap).

### Goals
- Cook something new each week without an hour of planning.
- Feel organised by Sunday night.

### Follow-up Questions
- Does she use a shopping app today? Which?
- Probe meaning of "overwhelming" — too many options or wrong ones?
```

**Claude's turn 7:** Ask whether this should update insights now.

> "Interview logged as P3. One pattern stands out — the 'said fine, hesitated' behaviour contradicts her stated satisfaction. If P1 or P2 showed similar hesitation, we might have an emerging pattern. Want to check `INSIGHTS.md` now, or wait for more interviews?"

**What to notice:** Claude walked the six fields in sequence, one at a time, and kept quotes verbatim even when the user's phrasing was clean. It also caught the "said fine / hesitated" contradiction and offered synthesis as a follow-up — but didn't run synthesis from a single interview. That's the N≥2 rule doing its job.
