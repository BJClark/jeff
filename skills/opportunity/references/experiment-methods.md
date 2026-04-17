# Experiment Methods — When to use which

Match method to risk. Pick the *cheapest* method that credibly tests the specific assumption, not the most impressive one.

## Concierge
**What.** Deliver the service manually, end-to-end, to a small number of users. No product, no automation — just you doing it by hand.

**When.** The riskiest assumption is "will users want this at all?" or "will they do the behaviour we're imagining?" Works best pre-build.

**Cost.** Your time × number of users. Often 1–2 weeks of founder/PM effort.

**Example.** Before building an AI meal planner, manually plan meals for five users each week and see if they cook from the plan.

**Avoid when.** The assumption is about scale, pricing, or discovery — concierge can't test those.

## Wizard of Oz
**What.** Fake the automation. The UI looks real; humans are doing the work behind the scenes.

**When.** The assumption is "will users interact with a product that does this?" — you want product-like behaviour but can't afford to build the real thing yet.

**Cost.** Lightweight frontend (often a Notion page, Figma prototype, or simple form) + ongoing human labour.

**Example.** A chatbot UI where responses are composed by a human on the other end.

**Avoid when.** You can't sustain the fakery for the test duration — 20 daily users is fine; 2000 isn't.

## Fake door
**What.** Show a CTA for a feature that doesn't exist, measure clicks. On click, honestly tell the user it's coming.

**When.** The assumption is "will users actually want this?" and you need to measure intent, not deliver value.

**Cost.** One marketing-page change. Hours, not days.

**Example.** Add a "Share to iMessage" button. If >5% of users click it, build it.

**Avoid when.** Disappointing users matters (paid customers, regulated contexts). Use sparingly — trust erodes if every door is fake.

## Prototype
**What.** A clickable mockup — Figma, pen-and-paper, HTML — tested with users 1:1 or in moderated sessions.

**When.** The assumption is about usability, comprehension, or workflow ("will users understand this flow?").

**Cost.** 1–3 days for the prototype, plus interview time.

**Example.** A Figma prototype of the onboarding flow, tested with five users to see where they get stuck.

**Avoid when.** You need quantitative signal (prototypes give qualitative signal from small N).

## A/B test
**What.** Two production variants, real traffic, statistical comparison.

**When.** The assumption is "does this change move a metric at scale?" — and cheaper tests have already pointed one way.

**Cost.** Weeks of traffic + engineering to instrument both variants + analysis overhead.

**Example.** After Wizard of Oz showed promise, A/B test the real automated version against the old flow with 10% of traffic for 2 weeks.

**Avoid when.** You have low traffic (underpowered), the change is small, or the assumption can be tested cheaper. A/B tests are the heaviest method for a reason — they're the last resort, not the default.

## Decision heuristic

1. **Write down the one specific assumption you're testing.** ("Users will share recipes with friends.")
2. **List which methods could disprove it.** (Fake door: yes. Prototype: no. Concierge: maybe.)
3. **Pick the cheapest of those.**

If you find yourself picking A/B by default, you're probably not naming the assumption precisely enough.
