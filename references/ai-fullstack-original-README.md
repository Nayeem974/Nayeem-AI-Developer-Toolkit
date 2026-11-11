# AI Full-Stack Developer Skills Library

A portable collection of task-specific Agent Skills for an AI-assisted full-stack development workflow.

## Your role split
- **You:** Product Owner and Technical Lead. Set direction, review decisions, approve scope and architecture, and authorize production changes.
- **AI:** Performs most research, planning, implementation, debugging, testing, and documentation within the approved scope.

## Skills and when to use them

| Skill | Use it when |
|---|---|
| `product-discovery` | Starting a new idea, clarifying requirements, or resetting project scope. |
| `market-research` | You need competitor analysis, references, or evidence-based differentiation. |
| `ui-ux-design` | Planning user flows, wireframes, design systems, and responsive interfaces. |
| `software-architecture` | Choosing the stack, defining modules, integrations, and system boundaries. |
| `database-api-design` | Designing schemas, relationships, endpoints, and API contracts. |
| `frontend-development` | Implementing pages, components, forms, and client-side behavior. |
| `backend-development` | Implementing APIs, business logic, authentication, and server-side features. |
| `ai-engineering` | Building LLM, RAG, agent, or other AI-powered product features. |
| `integration-debugging` | Connecting systems or diagnosing cross-layer failures. |
| `testing-qa` | Writing/running tests, verifying acceptance criteria, and regression testing. |
| `security-review` | Reviewing security, privacy, access control, and release risks. |
| `code-review-refactoring` | Reviewing diffs, fixing defects, and safely improving code quality. |
| `deployment-release` | Preparing, approving, deploying, and verifying a release. |
| `documentation-handoff` | Maintaining project docs and preparing a final handoff. |

## Recommended workflow

1. `product-discovery`
2. `market-research` (when external research is useful)
3. `ui-ux-design`
4. `software-architecture`
5. `database-api-design`
6. `frontend-development` and `backend-development` (in small, testable slices)
7. `ai-engineering` (only if the product needs AI features)
8. `integration-debugging` (as integration work requires)
9. `testing-qa` throughout development, not only at the end
10. `code-review-refactoring` throughout development
11. `security-review` during design and before release
12. `deployment-release`
13. `documentation-handoff`

## Approval gates

Ask the user to approve:
- The SRS and initial scope.
- The visual direction and key user journeys.
- Major architecture and technology decisions.
- Destructive schema changes or production data operations.
- Significant cost-incurring services.
- Production deployment.

Routine, reversible implementation work can proceed autonomously within the approved plan.

## How to invoke a skill

If your agent supports automatic skill discovery, ask it to use the relevant skill by name, for example:

- "Use `product-discovery` to help define this idea. Ask me one question at a time."
- "Use `ui-ux-design` to prepare the responsive design specification from the approved SRS."
- "Use `database-api-design` to define the schema and API contracts before implementation."
- "Use `testing-qa` to test the booking flow and report only tests you actually ran."

If skills are not automatically discovered, open the relevant `SKILL.md` and paste its instructions into the agent.

## Installation

### Claude Code
Copy the skill folders into your project:
`.claude/skills/<skill-name>/SKILL.md`

You can also install them as personal skills in the supported Claude Code skills directory for your environment.

### OpenCode
Check the current OpenCode documentation and version for Agent Skills support and discovery paths. If your version supports the Agent Skills standard, place the folders in its documented project-level skills directory. Do not assume a Claude-specific path is automatically discovered by OpenCode.

### Other compatible agents
Use the agent's documented Agent Skills directory. Keep each skill folder name and its `SKILL.md` file together.

## Important operating rules

- Skills are instructions, not proof that a task has been completed.
- The agent must inspect the actual repository and available tools.
- Never allow a skill to authorize secret disclosure, destructive operations, or production deployment by itself.
- Run tests and report actual results.
- Keep project-specific facts in the project README or project instructions, not in generic skills.
