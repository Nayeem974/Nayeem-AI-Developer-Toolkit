---
name: database-api-design
description: Use when designing or changing database schemas, data relationships, API contracts, validation rules, or persistence behavior.
---

# Database and API Design

## When to use
Use before implementing persistence or API features, and whenever schema or endpoint contracts change.

## Role
Act as a database architect and API designer.

## Workflow
1. Derive entities and operations from approved requirements and user flows.
2. Define entities, attributes, types, primary keys, foreign keys, uniqueness, nullability, and constraints.
3. Model relationships and cardinality.
4. Consider indexes, query patterns, pagination, filtering, and data volume.
5. Define API routes, methods, request/response schemas, status codes, validation, and error format.
6. Specify authentication and authorization requirements per operation.
7. Plan migrations, seed data, and rollback considerations.
8. Check for privacy, retention, and sensitive-data concerns.
9. Review contracts with frontend and backend before implementation.

## Deliverables
- ER diagram
- Schema definitions
- Migration plan
- API contract or OpenAPI specification when appropriate
- Validation rules
- Authorization matrix
- Example requests and responses

## Rules
- Do not expose internal database errors or sensitive fields through APIs.
- Validate input at trust boundaries.
- Use transactions where multi-step data consistency requires them.
- Avoid destructive migrations without explicit approval and backups.
- Keep API contracts consistent and document breaking changes.
