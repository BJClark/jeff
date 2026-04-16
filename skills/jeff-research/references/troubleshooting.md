# jeff-research — Troubleshooting

## `.jeff/research/` missing

Send the user to `/jeff:init`. Don't scaffold from here.

## User paraphrased a "quote"

Ask: "Did they actually say that, or is that your interpretation?" Paraphrases go in `Observations` with a note like "user conveyed that X"; verbatim quotes go in `Key Quotes` in quotation marks. Mixing these two contaminates synthesis later.

## PII in notes

If the user gives you real names, emails, or identifying info, ask before writing: "Should I anonymise this as P1/P2, or do you need the real identity preserved?" Default to anonymising. Never silently write real contact info to a plaintext file that might be committed to git.

## Single-source "insight"

If the user proposes an insight based on one interview, don't promote it. Write it under `## Emerging Patterns` with a note that more evidence is needed. Single-source insights are how teams mistake one loud user for a market.

## Insight with no implication

Push back: "What would the team do differently because of this?" If the answer is "nothing specific," it's not an insight — it's an observation. Park it under `## Emerging Patterns` until an implication surfaces.

## Insight contradicts the OST

Surface it to the user. Don't silently edit `OPPORTUNITIES.md`. Example: "This insight contradicts O3's assumption that users want curated recommendations. Should we revisit the opportunity, or is there a way to reconcile?"

## Interview entry is too short

If the user hurries through the six fields and ends up with one line each, ask specifically about observations and quotes — those are the fields that decay fastest without detail and matter most in synthesis.

## Interviews are being merged into one entry

Each interview is its own section. If the user says "P4 and P5 said basically the same thing," log them separately and note the overlap in both — don't merge. Later pattern-matching depends on being able to see per-user behaviour.

## User asks for a synthesis across too little data

If there are 2 interviews and the user wants to extract insights, explain that insights generally need ≥3 data points to be stable. Offer to capture what patterns *might* be emerging under `## Emerging Patterns` and suggest running more interviews before synthesising.
