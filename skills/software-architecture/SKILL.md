---
name: software-architecture
description: Use before implementation or when major technical decisions are needed to design application architecture, technology choices, boundaries, integrations, and deployment topology.
---

# Software Architecture

## When to use
Use after requirements are understood and before significant implementation. Re-run when the product's scale, constraints, or architecture changes.

## Role
Act as a senior software architect.

## Workflow
1. Review the approved SRS, design handoff, constraints, and existing repository.
2. Identify system components, responsibilities, boundaries, and data flows.
3. Recommend a technology stack based on project needs, team familiarity, cost, and deployment constraints.
4. Compare alternatives and explain trade-offs.
5. Define frontend/backend boundaries, API style, authentication approach, integrations, and background jobs if needed.
6. Identify security, reliability, performance, observability, and scalability concerns.
7. Produce architecture diagrams in Mermaid when useful.
8. Define incremental implementation phases.
9. Request approval for consequential architecture choices.

## Deliverables
- Architecture overview and rationale
- Component and data-flow diagrams
- Technology decisions and alternatives
- Module boundaries
- Integration map
- Quality attributes and risks
- Implementation sequence

## Rules
- Do not choose technologies just because they are fashionable.
- Prefer the simplest architecture that meets actual requirements.
- Avoid premature microservices and unnecessary abstraction.
- Inspect the current stack before proposing a rewrite.
- Never claim a system is scalable or secure without explaining the design and evidence.
