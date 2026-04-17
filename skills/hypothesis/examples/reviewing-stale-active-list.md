# Example: Pruning a stale active hypothesis list

**User says:** "Review the active hypotheses — I think some of them are old."

**Context:** `.jeff/HYPOTHESES.md` has seven entries in `## Active Hypotheses`. Five were created >60 days ago. No experiments currently in progress.

**Claude's turn 1:** Read the file and apply the review checklist to each active entry.

> "Seven active hypotheses. Running the checklist — falsifiable? metric real? method proportionate? stale? Here's the triage:
>
> - **H1** (62 days old): falsifiable ✓, metric exists ✓, A/B method for Medium risk ✓, but no experiment scheduled. **Stale.** Either schedule or deprecate.
> - **H2** (58 days old): **not falsifiable** — threshold is 'users will prefer it'. Needs rewriting before it can be scheduled.
> - **H4** (45 days old): risk H, method = prototype. **Method too light.** Prototype can't answer the pricing question.
> - **H5** (38 days old): duplicate of validated H2 from Q4 last year — same hypothesis, no new evidence. Propose abandonment.
> - **H6** (12 days old): falsifiable ✓, metric real ✓, method ✓. **Healthy.**
> - **H7** (8 days old): healthy. Experiment scheduled for next week.
> - **H3** (5 days old): healthy.
>
> Four need action. Want me to go through them one at a time?"

**User:** "Yes."

**Claude's turn 2:** Work H1 first.

> "**H1** (62 days old, stale). Options:"
> (AskUserQuestion)
> - "Schedule the experiment this sprint"
> - "Deprecate — mark as abandoned with note"
> - "Rewrite hypothesis, I don't remember why it's here"

**User:** "Deprecate. We already learned this was resolved by a different feature we shipped."

**Claude:** Moves H1 to a new `## Abandoned` section with a one-line note ("Resolved incidentally by feature X shipped 2026-03-12"). That way future-you knows the hypothesis didn't die in ignorance — it was overtaken by events.

**Claude's turn 3:** Work H2.

> "**H2** not falsifiable — threshold was 'users will prefer it'. Can you give me a specific metric and number? If not, we park H2 until you can."

**User:** "Let's park it. I don't have a metric for this yet."

**Claude:** Adds `[Parked — awaiting falsifiable threshold]` to H2, doesn't delete.

**Claude's turn 4:** Work H4 (method too light).

> "**H4** — risk High, method prototype. Pricing questions need behavioural signal, not qualitative. Suggested escalation:
>
> (AskUserQuestion)
> - 'Fake-door test with pretend checkout'
> - 'A/B test with real billing once we're ready'
> - 'Concierge — offer the price manually to 10 users'"

**User:** "Fake door for now. We'll A/B once we validate interest."

**Claude:** Updates H4's method. Notes the two-phase plan.

**Claude's turn 5:** Work H5 (duplicate).

> "**H5** duplicates validated H2 from Q4 — same hypothesis, same metric, no new evidence. Unless something's changed (new audience, new product state), re-running will get the same result. Abandon?"

**User:** "Yeah, abandon. I forgot we already tested this."

**Claude:** Moves H5 to `## Abandoned` citing the prior validated H2.

**Claude summarises:**

> "Active list was 7; now 4 healthy, 1 parked (H2), 2 abandoned (H1, H5). H4 method escalated from prototype to fake door."

**What to notice:** Review mode is an audit — every hypothesis has to justify its continued existence. Non-falsifiable entries get parked (not deleted) with a note about what's missing; duplicates get abandoned (not re-run); stale entries get a decision forced. The `## Abandoned` section is new — teams should add it when review reveals hypotheses that died of irrelevance, not invalidation.
