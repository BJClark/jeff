# Validation Methods — Matching method to hypothesis

Pick the lightest method that credibly tests the specific assumption. Match method to risk level.

## Concierge
Manually deliver the thing, end-to-end, to a small number of users. Works when the hypothesis is about whether users *want* or *use* a behaviour at all.

- **Fits**: Low / Medium risk hypotheses about new workflows.
- **Cost**: Hours to days of human labour per user.
- **Example**: Before building an automated meal planner, hand-curate plans for 5 users and see whether they cook from them.

## Wizard of Oz
Real UI, fake automation. Users believe they're interacting with a product; humans are responding behind the scenes.

- **Fits**: Medium risk hypotheses about product-like interactions you can't afford to build yet.
- **Cost**: Lightweight UI + sustained human effort to maintain the fiction.
- **Example**: A "smart" reply suggestion feature where the suggestions are being written by a human operator.

## Fake door
Show a CTA for a feature that doesn't exist. Measure clicks. On click, tell the user honestly.

- **Fits**: Low / Medium risk hypotheses about desirability — do users *want* this.
- **Cost**: One page change, hours of work.
- **Example**: Add an "Export to Notion" button and count how many users click before anything exists behind it.
- **Caveat**: Overuse erodes trust. Don't fake every door.

## Prototype
Clickable mockup (Figma, HTML, pen-and-paper) tested with users in moderated sessions.

- **Fits**: Low / Medium risk hypotheses about usability, comprehension, workflow.
- **Cost**: 1–3 days to build + interview time with 3–7 users.
- **Example**: A Figma prototype of a redesigned checkout flow, tested with 5 users.
- **Caveat**: Qualitative only. Can't substitute for traffic-based tests.

## A/B test
Two production variants, real traffic, statistical comparison.

- **Fits**: High risk hypotheses where cheaper tests have already pointed one way and you need confidence at scale.
- **Cost**: Weeks of traffic + engineering to maintain both variants + analysis.
- **Example**: After a Wizard of Oz test showed promise, A/B test the real automated feature against the old flow for 10% of traffic.
- **Caveat**: Heavy. Needs traffic for statistical power. Save for when the answer can't come any cheaper.

## Risk-to-method table

| Risk | Best-fit method                             | Method to avoid                          |
|------|----------------------------------------------|------------------------------------------|
| L    | Fake door, prototype                         | A/B test (overkill; takes weeks for a low-stakes answer) |
| M    | Wizard of Oz, concierge, prototype           | A/B test unless the cheap methods failed |
| H    | A/B test (after a cheaper method dies-try)   | Prototype only (too qualitative for high-stakes) |

## Decision heuristic

1. Write the one specific assumption you're testing.
2. Ask: **"What result would make me say no?"** If you can't answer, the hypothesis isn't falsifiable — fix that before picking a method.
3. Ask: **"Which of the five methods could produce that 'no' result credibly?"** Usually more than one.
4. Pick the cheapest. If you keep defaulting to A/B, you're probably not naming the assumption precisely enough.
