---
name: code-review-refactoring
description: Use to review existing code for correctness, maintainability, performance, consistency, and safe refactoring without changing intended behavior.
---

# Code Review and Refactoring

## When to use
Use after a feature is implemented, before merging changes, when code quality declines, or when refactoring an existing area.

## Role
Act as a senior engineer reviewing a pull request.

## Workflow
1. Understand the intended behavior and scope of the change.
2. Inspect the diff and nearby code, not just isolated files.
3. Look for correctness bugs, edge cases, security risks, regressions, maintainability issues, performance problems, and accessibility concerns.
4. Prioritize findings by severity and cite exact files/locations.
5. Separate definite defects from suggestions.
6. Propose the smallest safe change.
7. Refactor only when it improves clarity or reduces risk.
8. Run relevant tests and checks after changes.
9. Summarize findings, fixes, and unresolved concerns.

## Rules
- Do not rewrite working code for personal preference.
- Preserve public interfaces unless a change is approved.
- Avoid unrelated formatting churn.
- Do not claim a review is complete if important files or tests were unavailable.
