# Skill Router

Use this as the quick index. Each skill contains its detailed workflow.

| Need | Primary skill(s) | Add when useful |
|---|---|---|
| New app / requirements | `product-discovery` | `market-research`, `product-lens`, `product-capability`, `competitive-platform-analysis` |
| UX flows / design brief | `ui-ux-design` | `ui-ux-pro-max`, `design-system`, `frontend-design-direction` |
| UI implementation / visual QA | `ui-ux-pro-max` | `impeccable` plugin, `frontend-a11y`, `frontend-patterns` |
| Architecture | `software-architecture` | `blueprint`, `architecture-decision-records`, `council` |
| Database / API | `database-api-design` | `api-design`, `postgres-patterns`, `backend-patterns` |
| React frontend | `frontend-development` | `react-patterns`, `frontend-patterns`, `coding-standards` |
| Backend | `backend-development` | `backend-patterns`, `python-patterns` |
| LLM / RAG / agents | `ai-engineering` | `security-review` |
| Debugging | `integration-debugging` | Superpowers `systematic-debugging` |
| Unit / integration tests | `testing-qa` | Superpowers `test-driven-development`, `tdd-workflow` |
| Browser / end-to-end tests | `testing-qa` | `e2e-testing` |
| Review / refactor | `code-review-refactoring` | `ponytail-review`, `verification-loop` |
| Security / release readiness | `security-review` | `production-audit` |
| Git / branches | `git-workflow` | Superpowers `using-git-worktrees` |
| Deployment | `deployment-release` | `deployment-patterns`, `docker-patterns` |
| Documentation | `documentation-handoff` | `architecture-decision-records` |
| Multi-role review | `dev-team` | `council` for adversarial trade-offs |
| Learn while building | VibeWise `/vibe-wise:learn` | Use only when explicitly requested |
| Find more capabilities | `find-skills` | Verify source, permissions, and compatibility before installing |

## Avoiding overlap
- `product-discovery` is the workflow owner; `product-lens` and `product-capability` are specialist lenses, not mandatory duplicate discovery passes.
- `ui-ux-design` defines user flows/design requirements; UI UX Pro Max is the detailed design intelligence and implementation reference; Impeccable is for critique and polish.
- Superpowers owns the default brainstorming → plan → TDD/debugging → verification method. The Vibe Coding Team `tdd-workflow` is optional if Superpowers is installed.
- Use one primary code-review pass, then add security/production audits only when relevant.
- Ponytail optimizes for simplicity; it must not weaken correctness, security, accessibility, or test coverage.
- Do not run multiple team/council/blueprint skills for a small task.

## Universal task gates
- **Before repository edits:** inspect instructions, Git status/branch/diff, scripts, dependencies, architecture, and relevant tests. Preserve user changes.
- **Before substantial new builds:** discovery → requirements/acceptance criteria → UX direction → architecture/ADR → phased plan → approval.
- **During implementation:** small vertical slices; select skills minimally; use TDD for behavior changes and systematic debugging for defects.
- **Before completion:** execute relevant tests/lint/typecheck/build; inspect actual results and final diff; update docs; report not-run checks and limitations honestly.
- **Before consequential actions:** request explicit approval for destructive operations, production data/schema changes, production deployment, significant costs, public release, or major scope/architecture changes.
- **Agent use:** parallelize independent research/review tasks only; do not concurrently edit the same files; verify agent findings.
