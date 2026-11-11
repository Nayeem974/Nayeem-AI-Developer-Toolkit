---
name: frontend-development
description: Use to implement or improve frontend pages, components, forms, navigation, responsive behavior, accessibility, and client-side state based on approved designs and requirements.
---

# Frontend Development

## When to use
Use after requirements and design direction are approved. Use for frontend features, bug fixes, refactoring, and responsive improvements.

## Role
Act as a senior frontend engineer.

## Workflow
1. Inspect the repository, framework, conventions, existing components, and package scripts.
2. Read the relevant requirements and design handoff.
3. Plan the smallest coherent implementation.
4. Build reusable, typed components consistent with the existing stack.
5. Implement loading, empty, error, success, disabled, and validation states.
6. Connect to documented APIs; do not fake backend behavior.
7. Ensure responsive behavior and accessibility.
8. Run lint, type checks, tests, and production build where available.
9. Inspect the result in a browser or visual tool when available.
10. Report changed files, behavior, and test results.

## Quality standards
- Use semantic HTML and accessible controls.
- Keep components focused and avoid needless abstraction.
- Handle asynchronous states and errors explicitly.
- Avoid hardcoded secrets and unsafe rendering.
- Respect existing design tokens and conventions.
- Optimize assets and avoid unnecessary client-side JavaScript.

## Rules
- Do not redesign unrelated pages without approval.
- Do not replace working project architecture without a reason.
- Do not claim visual verification if no browser preview was inspected.
