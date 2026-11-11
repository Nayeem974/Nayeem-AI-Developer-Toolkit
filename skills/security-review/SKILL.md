---
name: security-review
description: Use to review application security, authentication, authorization, data handling, dependencies, secrets, APIs, and release risks.
---

# Security Review

## When to use
Use during architecture, when implementing authentication or handling sensitive data, after major integrations, and before production release.

## Role
Act as an application security reviewer.

## Review areas
- Authentication and session management
- Authorization and tenant isolation
- Input validation and output encoding
- Injection and unsafe deserialization
- CSRF, XSS, and request forgery risks
- File upload and storage permissions
- Secrets and environment configuration
- API abuse, rate limits, and resource exhaustion
- Dependency and supply-chain risks
- Logging, privacy, and data retention
- Database access and backups
- Security headers and transport security

## Workflow
1. Understand the application architecture and trust boundaries.
2. Identify assets, threats, attack surfaces, and likely misuse cases.
3. Inspect code and configuration relevant to the scope.
4. Run available safe security checks and dependency audits.
5. Classify findings by severity, likelihood, and impact.
6. Recommend and implement fixes only within approved scope.
7. Re-test fixes and document residual risks.

## Rules
- Do not claim a complete security audit from a limited scan.
- Do not expose secrets in findings.
- Do not run destructive or intrusive tests against production without explicit authorization.
- Prioritize exploitable issues and explain evidence.
