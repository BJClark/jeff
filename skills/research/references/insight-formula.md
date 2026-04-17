# The Insight Formula

**Insight = Pattern + Evidence + Implication.**

Missing any of the three means it's not yet an insight:

- Pattern without evidence is a hunch.
- Pattern with evidence but no implication is trivia.
- Implication with no evidence is advocacy.

## Pattern

Something seen in ≥2 interviews or data points. A thing that shows up once is an observation, not a pattern. It lives in `## Emerging Patterns` until more evidence arrives.

Good patterns:
- "Users who completed the preference wizard retained 2× (seen in analytics + corroborated by 4 interviews)."
- "Home cooks treat shopping list de-duplication as 'obviously necessary' even when they haven't asked for it."

Anti-pattern:
- "P3 said X." → That's an observation. Unless P5 and P7 also said X, don't promote it to a pattern.

## Evidence

Specific citations. Interview IDs (P1, P2, …), data points, dates, analytics dashboards. Push for at least two sources per insight.

Good:
> Evidence: P3, P5, P7 quotes (recipe-list overwhelm); analytics: 60% of sessions end without a save.

Anti-pattern:
> Evidence: multiple users mentioned this.

"Multiple" isn't citations. Name them.

## Implication

What should the team *do differently* because of this? This is where insights earn their keep. If the team's behaviour doesn't change based on the insight, it's not an insight — it's a fact.

Good implications:
- "De-prioritise algorithmic recommendations; invest in curation instead. Specifically, update Opportunity O3 evidence and mark Solution A (rec engine) lower priority."
- "Add shopping-list consolidation to Release 1 instead of Future — users treat it as table stakes."

Anti-pattern:
- "Users are overwhelmed by too many recipes." → Observation, not an implication. What do we *do*?

## Emerging patterns

Single-source observations that might become insights with more data. These live in their own section so they don't disappear but also don't get treated as validated.

When an emerging pattern hits its second corroborating data point, promote it to `## Key Insights`. Not before.

## Anti-insights

Some categories masquerade as insights but aren't:

- **Truisms** — "users want the app to be fast." True; not actionable.
- **Single-user preferences** — "P4 wishes the colour was blue." Unless it repeats, it's noise.
- **Implementation-shaped implications** — "We should use GraphQL" is a tech decision, not a user insight.

## How insights feed the OST

Insights are the primary raw material for `OPPORTUNITIES.md`:

- A strong insight often becomes an opportunity's evidence row.
- An insight that contradicts an opportunity's evidence should force a review of that opportunity.
- An insight without an associated opportunity usually means the OST is out of date.

The link goes both ways — insights shape opportunities, and the OST's gaps tell you what research to commission next.
