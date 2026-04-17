---
name: issues
description: Generate GitHub issues from the story map, OST, or hypotheses via the gh CLI. Supports --dry-run preview or --create.
argument-hint: "[map|opportunities|hypotheses|all] [--dry-run|--create]"
allowed-tools:
  - Skill
---

Invoke the `jeff:issues` skill. Pass `$ARGUMENTS` as the source filter and mode.

Workflow, issue template, gh CLI setup, and examples live under `skills/issues/`.
