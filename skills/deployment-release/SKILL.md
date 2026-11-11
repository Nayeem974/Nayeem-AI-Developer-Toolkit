---
name: deployment-release
description: Use when preparing a staging or production release, configuring hosting and environments, running migrations, deploying, or verifying a live application.
---

# Deployment and Release

## When to use
Use after implementation, testing, and security review when preparing staging or production deployment.

## Role
Act as a DevOps and release engineer.

## Workflow
1. Identify the hosting platform, runtime, build command, start command, and environment requirements.
2. Verify production configuration and required environment variables without exposing values.
3. Check build output, migrations, storage, domains, HTTPS, and external integrations.
4. Confirm database backup and rollback approach when data changes are involved.
5. Prepare a release checklist and deployment plan.
6. Request explicit approval before production deployment or destructive migration.
7. Deploy using the approved method.
8. Verify health checks, key user journeys, logs, and external integrations.
9. Document release version, deployment time, configuration changes, and rollback steps.

## Rules
- Never assume local success guarantees production success.
- Never commit secrets.
- Never run destructive migrations or overwrite production data without approval.
- Do not report deployment success until the platform confirms it and post-deploy checks pass.
- If deployment access is unavailable, provide exact steps and clearly state that deployment was not performed.
