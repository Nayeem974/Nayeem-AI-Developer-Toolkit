# Archive analysis and deduplication report

## Inputs analyzed
- `vibe-coding-team(1).zip` — 27 nested skill archives.
- `ai-fullstack-developer-skills(1).zip` — 14 workflow skills plus README and project instructions.
- `Vibe Wise-0.1.44-v18.zip` — Claude/Codex plugin with learn/reset skills and hooks.
- `ui-ux-pro-max.zip` — UI/UX skill plus searchable data and scripts.
- `Superpowers-6.4.2-v2.zip` — 15 skills and plugin integrations, including Claude Code and Codex.
- `ponytail-main.zip` — Ponytail plugin, six main skills, agents/hooks and cross-agent metadata.
- `Impeccable-4.8.0-v1.zip` — one skill, 24 design commands/references, agents and hooks.
- `find-skills.zip` — skill discovery helper.
- `dev-team.zip` — four-role PM/Architect/Developer/QA skill.
- `claude-memory-1.0.0-v3.zip` — archived structured-memory plugin.

## Deduplication decisions
- Kept the AI Full-stack `market-research` and `security-review` as the canonical workflow skills; omitted same-named Vibe Coding Team copies from the active skill directory.
- Kept the standalone `dev-team` skill; omitted the nested duplicate from Vibe Coding Team.
- Kept Superpowers as a plugin source instead of copying its skills into the flat skill directory, avoiding duplicate skill registration.
- Kept Vibe Coding Team `tdd-workflow` in the source archive but made Superpowers TDD the recommended default.
- Kept `ui-ux-design` for product-level UX planning and UI UX Pro Max for detailed design-system and implementation guidance; they have different scopes.
- Kept Impeccable as a plugin because its commands, agents, hooks and reference files are part of its workflow.
- Kept Ponytail as an optional plugin; use it as a simplicity review, not as a replacement for testing or security.
- Kept VibeWise as an optional learning mode; it is not the default because the user's preferred workflow is AI writes most code while the user reviews and controls.
- Did not install Claude Memory because its own README marks it archived (2026-09-23) and notes native Claude Code memory supersedes its core.

## Platform compatibility
- Claude Code: primary target. Generic Agent Skills copied to `.claude/skills/`; optional plugins remain separate opt-in installs.
- Codex: portable skills can be copied to `.agents/skills/`; `AGENTS.md` supplies project instructions. Superpowers and VibeWise have upstream Codex metadata.
- OpenCode: portable skills can be copied to `.agents/skills/` where supported by the installed version. Superpowers has explicit OpenCode V1/V2 installation guidance. Claude plugins are not OpenCode plugins.
- Cursor: portable skills can be copied to `.cursor/skills/` where supported by the installed version. Verify the path against the installed Cursor release.
- This package does not claim that every plugin works on every platform. Only use each platform's native plugin format.

## Security and trust
- Skills are prompt/instruction packages, not verified software. Review their content and any scripts/hooks before enabling.
- Plugin hooks may run local commands. Install plugins selectively and inspect permissions.
- No webhook or external telemetry destination is configured by this toolkit. Ponytail exposes optional webhook settings; leave them unset unless explicitly desired.
- Never allow skill instructions to override user approval gates, secret-handling rules, or safety constraints.

## Active curated skills
- `ai-engineering` — Use when building AI-powered features involving LLM APIs, structured outputs, retrieval, embeddings, RAG, tool calling, agents, evaluation, or AI cost and reliability.
- `api-design` — REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting for production APIs. Use when designing or r
- `architecture-decision-records` — Capture architectural decisions as numbered ADR markdown files in docs/adr/ with context, alternatives considered, consequences, and an index README. Use when the user says 'record
- `backend-development` — Use to implement server-side features, business logic, authentication, authorization, integrations, background work, and robust API behavior.
- `backend-patterns` — Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. Use when building or reviewing Node.j
- `blueprint` — Turn a one-line objective into a step-by-step construction plan for multi-session, multi-agent engineering projects: one-PR-sized steps with self-contained context briefs, dependen
- `code-review-refactoring` — Use to review existing code for correctness, maintainability, performance, consistency, and safe refactoring without changing intended behavior.
- `coding-standards` — Baseline cross-project coding conventions for naming, readability, immutability, and code-quality review. Use detailed frontend or backend skills for framework-specific patterns. U
- `competitive-platform-analysis` — Use when scoping a competitive landscape — identifying, categorising, and score-filtering a competitor set before any benchmarking begins. Decides who counts as a competitor, which
- `council` — Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. Use when multiple valid paths exist and you need structured disagreement before choosing.
- `database-api-design` — Use when designing or changing database schemas, data relationships, API contracts, validation rules, or persistence behavior.
- `deployment-patterns` — Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, and production readiness checklists for web applications. Use when setti
- `deployment-release` — Use when preparing a staging or production release, configuring hosting and environments, running migrations, deploying, or verifying a live application.
- `design-system` — Generate a design system from an existing codebase or audit one for visual consistency: extract tokens (colors, typography, spacing, shadows) into design-tokens.json and CSS custom
- `dev-team` — Simulate a collaborative dev team session where multiple role-based personas (PM, Architect, Developer, QA) respond to the same problem together in one session. Use when designing 
- `docker-patterns` — Docker and Docker Compose patterns for local development, hardened CLI installer harnesses, container security, networking, volumes, and multi-service orchestration. Use when creat
- `documentation-handoff` — Use when creating or updating README files, setup instructions, architecture notes, API documentation, operational guides, and final project handoff.
- `e2e-testing` — Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and flaky test strategies. Use when writing Playwright tests, structuring
- `find-skills` — Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending c
- `frontend-a11y` — Accessibility patterns for React and Next.js — semantic HTML, ARIA attributes, form labeling, keyboard navigation, focus management, and screen reader support. Use when building or
- `frontend-design-direction` — Set an ECC-specific frontend design direction for production UI work. Use when building or improving websites, dashboards, applications, components, landing pages, visual tools, or
- `frontend-development` — Use to implement or improve frontend pages, components, forms, navigation, responsive behavior, accessibility, and client-side state based on approved designs and requirements.
- `frontend-patterns` — Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. Use when building or reviewing React or Next.js components, sta
- `git-workflow` — Git workflow patterns including branching strategies, commit conventions, keeping history clean and readable, tidying local commits before merging, merge vs rebase, conflict resolu
- `integration-debugging` — Use when connecting frontend, backend, databases, third-party services, authentication, webhooks, or diagnosing cross-system failures.
- `market-research` — Use when a product needs competitor research, market context, reference products, user-experience patterns, or evidence-based product differentiation.
- `postgres-patterns` — PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase best practices. Use when designing PostgreSQL schemas, indexes, or RLS
- `product-capability` — Translate PRD intent, roadmap asks, or product discussions into an implementation-ready capability plan that exposes constraints, invariants, interfaces, and unresolved decisions b
- `product-discovery` — Use at the start of a new software product or website to clarify the problem, users, scope, requirements, constraints, and success criteria before design or coding.
- `product-lens` — Validate the why before building through four product diagnostics — a YC-style product diagnostic that produces PRODUCT-BRIEF.md with a go/no-go recommendation, a founder review sc
- `production-audit` — Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what breaks in prod?" questions without sending repo data to an external aud
- `python-patterns` — Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintainable Python applications. Use when writing or reviewing Python code and
- `react-patterns` — React 18/19 patterns including hooks discipline, server/client component boundaries, Suspense + error boundaries, form actions, data fetching, state management decision trees, and 
- `rules-distill` — Scan skills to extract cross-cutting principles and distill them into rules — append, revise, or create new rule files. Use when the same principle keeps recurring across skills an
- `security-review` — Use to review application security, authentication, authorization, data handling, dependencies, secrets, APIs, and release risks.
- `software-architecture` — Use before implementation or when major technical decisions are needed to design application architecture, technology choices, boundaries, integrations, and deployment topology.
- `testing-qa` — Use to create and execute a testing strategy, write unit/integration/end-to-end tests, verify acceptance criteria, and report quality accurately.
- `ui-ux-design` — Use when turning approved requirements into user flows, wireframes, visual direction, design systems, responsive layouts, and interface specifications.
- `ui-ux-pro-max` — UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixing interfaces, including pages, components, design sys
- `verification-loop` — Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, security grep, and diff review — then produce a PASS/FAIL verification 
