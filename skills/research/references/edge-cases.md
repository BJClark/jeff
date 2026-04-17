# jeff:research — Anti-Patterns & Edge Cases

## Paraphrase masquerading as a quote

**Detection.** The "quote" is in the third person or uses phrasing the user wouldn't naturally use. "P3 felt that the interface was confusing" isn't a quote; it's a summary.

**Why it's bad.** Paraphrases carry the interviewer's interpretation. When you re-read three months later, you can't tell what the user actually said.

**Redirect.** Ask: "Do you have their verbatim words? If not, this belongs in Observations, not Key Quotes."

## Interpretation buried in Observations

**Detection.** Observations section contains sentences like "clearly the user didn't understand" or "this confirms our hypothesis."

**Why it's bad.** Observations should be behavioural facts, not interpretations. Mixing them contaminates analysis.

**Redirect.** Split: "What did they *do*?" goes in Observations. "What do you think it means?" goes in a separate Follow-up or Analysis field if needed — not in Observations.

## Identifying info left in notes

**Detection.** Notes include real names, employer names, email addresses, or phone numbers.

**Why it's bad.** Research notes often get committed to git. PII in git is hard to fully remove (`git filter-branch` doesn't scale). Better to never write it.

**Redirect.** Anonymise before writing. P1, P2, etc. If role/company matter, abstract them: "PM at a 200-person SaaS company" not "PM at Acme Corp."

## Single-user insight promoted too early

**Detection.** Insight cites exactly one interview.

**Why it's bad.** N=1 is a story, not a pattern. Treating it as validated leads to building for an outlier.

**Redirect.** Move to `## Emerging Patterns`. Add "needs corroboration from 2 more interviews" as a next step.

## Insight with no implication

**Detection.** Insight ends at "users are frustrated by X" with no "so we should…"

**Why it's bad.** An insight whose behaviour-change implication is unclear won't shape any decisions. It rots.

**Redirect.** "Given this pattern, what does the team do differently next sprint?" If nothing, it's not yet actionable — park until it is.

## Confirmation-biased synthesis

**Detection.** The user goes into synthesis already knowing what they want the insights to say. Evidence selection is cherry-picked.

**Why it's bad.** Synthesis becomes post-hoc justification instead of genuine pattern discovery.

**Redirect.** Before synthesis, ask: "What would *disconfirm* the patterns you think you're seeing? Scan for those first." If they emerge, record them — they're often more useful than the confirming ones.

## Running synthesis before enough data

**Detection.** Attempting to synthesise insights from 1–2 interviews.

**Why it's bad.** Patterns aren't yet patterns. Everything looks like a universal truth because there's no variance visible.

**Redirect.** "Let's capture these as emerging patterns for now. Plan 3–5 more interviews, then re-synthesise."

## Insight contradicts the OST but is filed silently

**Detection.** A new insight invalidates an assumption under `OPPORTUNITIES.md` or `HYPOTHESES.md`, but the research skill records it without flagging.

**Why it's bad.** Two files disagree and nobody's watching. The outdated artifact keeps being cited as if valid.

**Redirect.** Surface the contradiction explicitly: "This insight contradicts O2's assumption. Update the OST now, or note the contradiction for review?"

## Interview merged with previous

**Detection.** User wants to append a new interview to a previous entry rather than create a new section.

**Why it's bad.** Per-participant data gets lost. You can't later ask "which patterns held for the 3 home cooks vs. the 2 chefs?"

**Redirect.** Always a new dated section per interview, even if the participant is the same (they're unlikely to be; if truly a follow-up with the same person, note it and still keep chronological sections).
