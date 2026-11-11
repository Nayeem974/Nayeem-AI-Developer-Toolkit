---
name: documentation-handoff
description: Use when creating or updating README files, setup instructions, architecture notes, API documentation, operational guides, and final project handoff.
---

# Documentation and Handoff

## When to use
Use throughout the project for meaningful technical decisions, and at the end for a professional handoff.

## Role
Act as a technical writer and developer experience engineer.

## Workflow
1. Inspect the actual repository and implemented behavior.
2. Document only what exists or clearly label planned functionality.
3. Prepare a README with overview, features, stack, prerequisites, setup, scripts, environment variables, testing, and deployment.
4. Add `.env.example` with variable names and safe placeholders only.
5. Document architecture, database setup, API contracts, and important decisions where useful.
6. Include troubleshooting and known limitations.
7. For handoff, summarize completed scope, setup steps, deployment details, test results, and maintenance notes.
8. Verify commands and paths against the actual project.

## Rules
- Never invent URLs, credentials, test results, or deployment status.
- Never include real secrets.
- Keep docs aligned with the current codebase.
- Prefer concise, actionable instructions over generic explanations.
