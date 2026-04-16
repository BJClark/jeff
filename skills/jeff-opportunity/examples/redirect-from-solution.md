# Example: Redirecting "Add X" to an opportunity

**User says:** "I want to add a recommendation engine."

**Context:** `.jeff/OPPORTUNITIES.md` has an active outcome and two existing opportunities but no related solution yet.

**Claude's turn 1:** Stop and redirect.

> "Hold on — 'recommendation engine' is a solution. What user need is it serving? Think about what the user is *trying to do* when they'd benefit from recommendations."

**User:** "They open the app, scroll for a while, and don't find anything they'd actually cook, so they give up."

**Claude's turn 2:** Name the opportunity.

> "So the opportunity is something like: **Users struggle to find recipes they'll actually cook**. Is that right?"

**User:** "Yes, that's it."

**Claude's turn 3:** Ask for evidence before recording.

> "What's the evidence? Any interview quotes, or usage data showing drop-off from the recipe list?"

**User:** "P3 said 'I always end up cooking the same thing because the list is overwhelming'. And we have data that shows 60% of sessions end without a save."

**Claude's turn 4:** Record the opportunity, then force multiple solutions before returning to recommendations.

```markdown
## Opportunity O3: Users struggle to find recipes they'll actually cook
- **Evidence:** P3 quote: "I always cook the same thing because the list is overwhelming." Usage data: 60% sessions end without save.
- **Impact:** H (directly blocks the "save a recipe" activity in the story map)
```

> "Good. Before we commit to recommendations, we need at least two other candidate solutions. What else could solve 'users can't find recipes they'll cook'?"

**User:** "Hmm… curated weekly lists? Or better filtering on the existing list?"

**Claude's turn 5:** Record all three, pick the riskiest assumption for recommendations.

> "Three solutions:
> - A: **Recommendation engine** — risky assumption: 'an algorithm can predict what this user will cook better than curation can.'
> - B: **Curated weekly lists** — risky assumption: 'our curation matches the user's taste.'
> - C: **Better filters** — risky assumption: 'users know what they want if given the right filters.'
>
> A is the most expensive to build and the most uncertain. Cheapest test of A's assumption: **Wizard of Oz** — curate a personalised list for 5 users manually for 1 week. If curation beats the current flow, we know content-based matching helps; we haven't learned whether ML is needed yet. If curation doesn't help, A is dead and we focus on C."

**Claude writes to `.jeff/OPPORTUNITIES.md`:**

```markdown
## Opportunity O3: Users struggle to find recipes they'll actually cook
- Evidence: P3 quote; 60% session drop-off data.
- Impact: H

### Solution A: Recommendation engine
- Assumption: Algorithmic matching beats human curation for this user.
- Experiment: Wizard of Oz — manually curate 5 users' weekly lists for 1 week. 5 days.

### Solution B: Curated weekly lists
- Assumption: Human curation matches user taste well enough.
- Experiment: Same as A (this experiment tests both).

### Solution C: Better filters
- Assumption: Users know what they want given filters.
- Experiment: Prototype a filter sidebar; watch 5 users use it.
```

**What to notice:** Two moves. First, Claude refused to record "add a recommendation engine" as an opportunity — it's a solution — and walked the user up to the underlying need. Second, Claude collapsed two experiments into one (the Wizard of Oz test resolves both A's and B's riskiest assumption at the same time), which is the kind of efficiency the method rewards.
