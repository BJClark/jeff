# Example: Synthesising insights across multiple interviews

**User says:** "I've done five interviews now. Help me pull out the insights."

**Context:** `.jeff/research/USER_INTERVIEWS.md` has P1–P5. `.jeff/research/INSIGHTS.md` is empty (template only).

**Claude's turn 1:** Read both files, scan for repeated patterns.

> "Scanning P1–P5. Three potential patterns:
>
> 1. **Recipe-list overwhelm.** P3 and P5 used the word 'overwhelming'; P1 scrolled past 40 recipes and didn't save. 3 sources.
>
> 2. **Shopping list de-duplication expected as default.** P2, P3, P4 all mentioned it as a pain point unprompted. 3 sources.
>
> 3. **Onboarding hesitation despite stated satisfaction.** Observed in P3 and P5. 2 sources — borderline.
>
> Want me to turn each into an insight, and which one first?"

**User:** "Let's do all three, starting with the overwhelm one."

**Claude's turn 2:** Draft the first insight using the formula.

> "**Pattern**: Users experience the main recipe list as overwhelming rather than abundant.
>
> **Evidence**:
> - P3 quote: 'I always end up cooking the same three things because the list is overwhelming.'
> - P5 quote: 'Too much choice — I'd rather just be told what to make.'
> - P1 observation: scrolled past 40 recipes without saving any.
>
> **Implication**: Curated weekly lists or algorithmic matching may outperform the current scrollable list. This reinforces Opportunity O3 ('users struggle to find recipes they'll cook') and suggests Solution B (curated weekly lists) deserves a faster test than Solution C (better filters).
>
> That's an insight. Confirm or adjust?"

**User:** "Confirm. But flag that the three users are all home cooks — maybe professionals would say different."

**Claude's turn 3:** Add scope limitation to the insight before writing.

> "Good catch — I'll add a scope note: 'Pattern observed in home-cook segment only; professional cooks not yet interviewed.'"

**Claude's turn 4:** Draft the second insight.

> "**Pattern**: Users treat shopping-list de-duplication as table stakes, not a feature to earn.
>
> **Evidence**:
> - P2 pain point: 'Shopping list double-counts ingredients.'
> - P3 pain point: 'Shopping list doesn't de-duplicate.'
> - P4 pain point: 'Ended up buying 3 lbs of tomatoes because the list didn't combine.'
>
> **Implication**: De-duplication belongs in walking skeleton or Release 1, not Future. Update `STORY_MAP.md` to pull de-duplication up from Future if it's currently there.
>
> Confirm?"

**User:** "Confirm."

**Claude's turn 5:** Third pattern — borderline.

> "**Pattern**: Onboarding hesitation despite stated satisfaction.
>
> Only 2 sources (P3 + P5). That's borderline for an insight — I'd put it under `## Emerging Patterns` for now, with 'corroborate in next 2 interviews' as a next step. Do you agree, or want to promote it anyway?"

**User:** "Agree, emerging pattern."

**Claude appends to `.jeff/research/INSIGHTS.md`:**

```markdown
## Key Insights

### I1 — Recipe-list overwhelm (home-cook segment)
- **Pattern**: Users experience the main recipe list as overwhelming rather than abundant.
- **Evidence**:
  - P3: "I always end up cooking the same three things because the list is overwhelming."
  - P5: "Too much choice — I'd rather just be told what to make."
  - P1 observation: scrolled past 40 recipes without saving.
- **Implication**: Curation / matching likely outperforms current list. Reinforces Opportunity O3. Accelerate Solution B (curated weekly lists).
- **Scope**: Home-cook segment only; professionals not yet interviewed.

### I2 — Shopping-list de-duplication is table stakes
- **Pattern**: Users expect de-duplication as a default, not a premium feature.
- **Evidence**: P2, P3, P4 pain points (unprompted).
- **Implication**: Pull de-duplication into walking skeleton or Release 1. Update STORY_MAP.md.

## Emerging Patterns

### EP1 — Onboarding hesitation despite stated satisfaction
- **Observed**: P3 and P5 — users describe the app as "fine" but hesitate 5–8 seconds before each onboarding tap.
- **Status**: Emerging (2 sources). Corroborate in next 2 interviews before promoting.
```

**Claude's turn 6:** Offer to link to the OST.

> "Two updates to propose:
> 1. **I1** reinforces O3 in `OPPORTUNITIES.md` — I can add this as an Evidence row on O3. Want me to?
> 2. **I2** suggests pulling shopping-list de-duplication from Future into Release 1 in `STORY_MAP.md`. That's a `/jeff:map` decision — want me to flag it there?"

**What to notice:** Three moves that matter. First, pattern threshold — 3 sources passed; 2 sources went to Emerging Patterns, not Key Insights. Second, scope note on I1 ("home-cook segment only") keeps the insight from over-generalising. Third, Claude *proposed* the OST and story map updates rather than silently making them — cross-file edits need visible approval.
