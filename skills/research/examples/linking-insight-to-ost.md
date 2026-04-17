# Example: An insight that contradicts the OST

**User says:** "I want to log an insight from the last few interviews — but I think it's going to mess up our OST."

**Context:** `.jeff/research/INSIGHTS.md` has 3 existing insights. `.jeff/OPPORTUNITIES.md` has Opportunity O2 ("Users want mobile notifications") with Solution A ("Push notifications for new recipes") scheduled for an A/B test via hypothesis H4.

**Claude's turn 1:** Capture the insight normally first.

> "Walk me through the pattern before worrying about the OST — we can figure out the downstream effect after."

**User:** "P4, P6, and P7 all said — unprompted — that they don't want notifications from cooking apps. P4: 'If I wanted more notifications I'd be on Instagram.' P6 turned off all notifications after one day. P7 uninstalled a different recipe app because of notifications."

**Claude's turn 2:** Draft the insight.

> "**Pattern**: Target users actively reject push notifications from cooking apps.
>
> **Evidence**:
> - P4 quote: 'If I wanted more notifications I'd be on Instagram.'
> - P6 observation: disabled all notifications within 24 hours of install.
> - P7: uninstalled a competing product specifically because of notifications.
>
> **Implication**: Opportunity O2 ('Users want mobile notifications') is likely wrong. We should pause H4's notification A/B test and consider invalidating O2 before testing further.
>
> That's an insight. But it directly contradicts O2 and H4 — want me to surface the conflict?"

**User:** "Yes please."

**Claude's turn 3:** Write the insight, then propose updates to OPPORTUNITIES.md and HYPOTHESES.md (don't silently edit).

> "Writing I4 to `INSIGHTS.md` now. Proposing two downstream changes:
>
> **In `OPPORTUNITIES.md`:**
> - Add I4 to O2's Evidence row with status `Contradicting`.
> - Flag O2 for review — consider moving to an `## Invalidated Opportunities` section or reframing it. The data says users don't want what O2 assumes they want.
>
> **In `HYPOTHESES.md`:**
> - Flag H4 (push notifications A/B test) for deprioritisation or cancellation. If we run it and get low opt-in, we've confirmed the insight at higher cost than the interviews just showed us.
>
> Want me to make these edits, or do you want to discuss first?"

**User:** "Make them."

**Claude appends I4 to `INSIGHTS.md`:**

```markdown
### I4 — Users reject push notifications from cooking apps
- **Pattern**: Target segment actively dislikes notifications from cooking apps; unprompted rejection across 3 interviews.
- **Evidence**:
  - P4: "If I wanted more notifications I'd be on Instagram."
  - P6: disabled all notifications within 24h of install.
  - P7: uninstalled a competitor specifically because of notifications.
- **Implication**: O2 ("Users want mobile notifications") contradicted. Pause H4 (notification A/B test). Reconsider whether O2 belongs in the tree or needs reframing (e.g., "Users want weekly meal reminders in a specific context").
- **Scope**: Home cooks (3 sources). Not yet tested with professionals.
```

**Claude edits `OPPORTUNITIES.md`:**

```diff
 ## Opportunity O2: Users want mobile notifications
 - Evidence: none yet — assumption.
+- Contradicting evidence: INSIGHTS.md I4 — 3 users unprompted said they reject notifications.
+- **Status: Under review** — consider invalidating or reframing.
```

**Claude edits `HYPOTHESES.md`:**

```diff
 ## H4 — Push notifications for new recipes increase return visits
-- Status: Untested (A/B test scheduled)
+- Status: **Deprioritised** — contradicting evidence in INSIGHTS.md I4. Running the A/B test likely confirms the insight at higher cost. Revisit only if we can reframe the hypothesis (e.g., weekly reminder vs. per-recipe notification).
```

**What to notice:** Three cross-file edits, all surfaced to the user before making them. The research skill doesn't silently rewrite the OST — it proposes, then acts on confirmation. This is the correct pattern whenever an artifact's validity depends on evidence in another file: make the dependency visible, then edit both sides together. Silent cross-file edits are how discovery artifacts drift apart.
