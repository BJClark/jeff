# jeff-map — Troubleshooting

Quick fixes for the failure modes that actually happen during a mapping session.

## `.jeff/` is missing

Tell the user to run `/jeff:init` first. Do not create `.jeff/` from this skill — that's what `jeff-init` is for, and doing it here would bypass its scaffolding.

## `.jeff/STORY_MAP.md` is missing but `.jeff/` exists

Either `/jeff:init` didn't finish or the file was deleted. Offer to recreate it from the template rather than proceeding against a missing file. The template lives at `skills/jeff-init/templates/STORY_MAP.md`.

## User is describing features, not activities

Redirect once, firmly: "Before we talk about the feature, what is the user *trying to do* when they need this?" Write the activity, not the feature. If the user pushes back, name the move: "I'm parking this as a story under the activity — that way we can compare it to other ways of solving the same need."

## Backbone has 15+ cells

Too granular. Those are probably stories, not activities. Ask the user to group them into 3–8 higher-level phases. A useful prompt: "If a new hire explained this to their manager in two sentences, which words would they use?" — those words are activities.

## Walking skeleton has empty cells

The user may be protecting those columns as "not in scope." Ask directly: "If this column has no skeleton story, how does the end-to-end flow work?" Then either add a story or remove the column from the backbone. A backbone cell with no skeleton story is a lie about the flow.

## Skeleton stories are too heavy

If a skeleton story takes three sprints, it's not a skeleton — it's a rib masquerading as one. Test: "Can we ship this in days, not weeks?" If not, strip it further. The skeleton is allowed to be embarrassing.

## Ambiguous priority labels on an existing map

If the map uses something other than "Release 1 / Future" (e.g., P0/P1/P2, Must/Should/Could), ask the user what each label means to them before editing. Don't silently normalise — you may misinterpret the intent.

## User wants "everything" in Release 1

Apply the cut-test: "Which of these would you actually drop if the deadline slipped a week?" The ones they'd drop move to Future. If they insist nothing would drop, the scope is untenable and someone needs to have that conversation before more planning happens.

## Merge conflict on `STORY_MAP.md`

If the file was edited out-of-band (e.g., another teammate, a previous session), Read it fresh before writing and reconcile row-by-row. Never overwrite wholesale.
