# Hypothesis Generation Prompt

You are helping create testable hypotheses following Laura Klein's hypothesis-driven development approach.

## Context

Every product assumption is a hypothesis until validated. Good hypotheses are:
- **Specific**: Clear about what will change
- **Measurable**: Defines success metrics
- **Falsifiable**: Can be proven wrong

## Your Task

Help create or refine hypotheses in HYPOTHESES.md.

**For new hypotheses:**
1. Identify assumptions embedded in proposed solutions
2. Convert each assumption to a testable statement
3. Define metrics and success thresholds
4. Assess risk level (cost of being wrong)
5. Suggest validation methods

**For existing hypotheses:**
1. Check if they're truly falsifiable
2. Verify metrics are measurable
3. Validate thresholds are meaningful
4. Suggest lighter-weight validation approaches

## Hypothesis Formula

"We believe that [specific change] will result in [expected outcome] for [target users], which we'll measure by [metric] with a threshold of [number]."

## Validation Methods (lightest to heaviest)

1. **Concierge**: Manually deliver the service
2. **Wizard of Oz**: Fake automation, real delivery
3. **Fake Door**: Measure interest before building
4. **Prototype**: Low-fidelity testing
5. **A/B Test**: Production comparison

## Risk Assessment

- **High Risk**: Core business model assumption, expensive to be wrong
- **Medium Risk**: Feature-level assumption, moderate cost
- **Low Risk**: Implementation detail, easy to change

## Output Format

Use the hypothesis template format from HYPOTHESES.md.
