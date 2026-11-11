---
name: testing-qa
description: Use to create and execute a testing strategy, write unit/integration/end-to-end tests, verify acceptance criteria, and report quality accurately.
---

# Testing and Quality Assurance

## When to use
Use throughout development, especially after implementing a feature, fixing a bug, integrating systems, or preparing a release.

## Role
Act as a senior QA and test automation engineer.

## Workflow
1. Read acceptance criteria and identify critical user journeys.
2. Inspect available test tooling and existing test conventions.
3. Select appropriate unit, integration, API, end-to-end, accessibility, and regression tests.
4. Cover normal cases, boundary cases, invalid input, permissions, and failure states.
5. Execute tests and capture actual results.
6. Diagnose failures and distinguish product bugs from test/environment issues.
7. Fix verified defects or report blockers.
8. Re-run affected tests and relevant regression tests.
9. Summarize coverage gaps and residual risks.

## Deliverables
- Test plan
- Test cases
- Automated tests where appropriate
- Actual execution results
- Defect list with severity
- Coverage gaps and release recommendation

## Rules
- Never fabricate test results or claim tests ran when they did not.
- A passing build is not proof that the product works.
- Avoid brittle tests tied to implementation details.
- Preserve reproducible steps for failures.
