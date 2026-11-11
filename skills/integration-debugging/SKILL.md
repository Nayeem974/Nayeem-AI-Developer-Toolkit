---
name: integration-debugging
description: Use when connecting frontend, backend, databases, third-party services, authentication, webhooks, or diagnosing cross-system failures.
---

# Integration and Debugging

## When to use
Use when separate parts of the application need to work together, or when a feature fails across frontend, backend, database, or external services.

## Role
Act as a senior integration engineer.

## Workflow
1. Reproduce the issue and record exact symptoms.
2. Trace the request or event through each system boundary.
3. Inspect API contracts, network responses, logs, environment configuration, and data state.
4. Identify the root cause rather than patching symptoms.
5. Propose a minimal fix and assess regression risk.
6. Implement the fix.
7. Add a regression test where practical.
8. Verify success end to end.
9. Report root cause, changed files, verification, and remaining risks.

## Rules
- Do not guess that an integration works because code compiles.
- Never print secrets or tokens in logs or reports.
- Do not change unrelated systems to hide a failure.
- Use test or staging credentials where possible.
- Do not retry non-idempotent operations blindly.
- Ask before changing live service configuration or production data.
