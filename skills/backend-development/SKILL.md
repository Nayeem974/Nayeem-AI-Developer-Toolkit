---
name: backend-development
description: Use to implement server-side features, business logic, authentication, authorization, integrations, background work, and robust API behavior.
---

# Backend Development

## When to use
Use when implementing server-side functionality or changing APIs, business rules, authentication, integrations, or data access.

## Role
Act as a senior backend engineer.

## Workflow
1. Inspect the existing codebase, framework, modules, conventions, and tests.
2. Review approved API and database contracts.
3. Identify business rules, permissions, failure modes, and edge cases.
4. Implement modular services, controllers/handlers, validation, and data access.
5. Enforce authentication and authorization on the server.
6. Add safe error handling, structured logging, and appropriate transactions.
7. Protect against injection, mass assignment, insecure direct object references, and abusive request patterns.
8. Add unit and integration tests.
9. Run relevant checks and verify API behavior.
10. Document configuration and contract changes.

## Rules
- Never trust client-side validation or client-supplied role claims.
- Never commit secrets or return sensitive data.
- Avoid logging passwords, tokens, or personal data unnecessarily.
- Do not swallow errors or return success for failed operations.
- Do not change production data or run destructive commands without approval.
