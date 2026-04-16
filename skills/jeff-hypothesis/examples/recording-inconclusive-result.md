# Example: Recording an inconclusive experiment result

**User says:** "H3's experiment just finished. We saw a 4% lift in signup conversion, not the 15% we predicted."

**Context:** `.jeff/HYPOTHESES.md` has H3 as `Untested` with threshold `+15%, p < 0.05`. The user ran an A/B test for two weeks.

**Claude's turn 1:** Read H3 and check the threshold.

> "H3's threshold was +15% with p < 0.05. You saw +4%. Two questions:
>
> 1. Was the +4% statistically significant at the power you had?
> 2. Is +4% inside or outside noise for that metric historically?"

**User:** "It hit p = 0.03, so statistically significant. But historically this metric wobbles ±3% week-to-week, so 4% is barely outside noise."

**Claude's turn 2:** Classify as Inconclusive (not Invalidated).

> "Sounds like **Inconclusive** — directionally positive and statistically significant, but below your decision threshold and barely above historical noise. Marking H3 Inconclusive, not Invalidated — the hypothesis isn't dead, but it's not proven either."

**Claude's turn 3:** Ask about the decision.

> "Three options from here. Which fits?"
> (AskUserQuestion)
> - "Rerun with more power / longer duration — maybe the true effect is 8% and we were underpowered."
> - "Abandon — 4% isn't worth shipping; move on to the next hypothesis."
> - "Ship it anyway — even a small lift is worth it for a permanent change."

**User:** "Abandon. 4% isn't worth the complexity of maintaining dynamic logos."

**Claude's turn 4:** Record the decision and the learning.

> "Abandoning H3. Capturing the learning: **'Logo-only social proof is not a meaningful conversion lever for this audience.'** Moving H3 to `## Invalidated` with this learning attached — so future-you won't re-run the same experiment in six months."

**Claude edits `.jeff/HYPOTHESES.md`:**

```diff
-## Active Hypotheses
-
-## H3 — Customer logos on pricing page increase signup conversion
-- Status: Untested
+## Validated / Invalidated / Inconclusive
+
+## H3 — Customer logos on pricing page increase signup conversion  [Inconclusive → Abandoned]
+- Status: Inconclusive (directional +4%, p=0.03, but below +15% threshold and barely above ±3% weekly noise)
+- Decision: Abandoned. The lift isn't worth the maintenance cost of dynamic logos.
+- Learning: Logo-only social proof is not a meaningful conversion lever for this audience. Consider testing testimonial quotes or usage-number social proof before revisiting logos.
```

**What to notice:** Two important moves. First, Claude distinguished **Inconclusive** from **Invalidated** — the hypothesis wasn't disproven, just unconvincing. Second, Claude captured a **learning** beyond the specific result ("logo-only social proof doesn't move this metric") that will inform future hypotheses. The Invalidated section is the team's memory — losing detail there costs the next experiment cycle.
