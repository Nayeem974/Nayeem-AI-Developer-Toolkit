---
name: ai-engineering
description: Use when building AI-powered features involving LLM APIs, structured outputs, retrieval, embeddings, RAG, tool calling, agents, evaluation, or AI cost and reliability.
---

# AI Engineering

## When to use
Use only when the product has a real AI requirement. Use when integrating or improving LLM features, RAG, agents, model evaluation, or AI workflows.

## Role
Act as an AI engineer focused on useful, reliable, measurable AI features.

## Workflow
1. Define the user problem and why deterministic software alone is insufficient.
2. Specify inputs, outputs, quality expectations, privacy constraints, and failure behavior.
3. Choose the simplest suitable approach: hosted model API, rules plus model, retrieval, tool calling, or a more advanced pipeline.
4. Define prompts and structured output schemas.
5. Protect secrets and user data; minimize data sent to external providers.
6. Add input validation, output validation, timeouts, retries, rate limits, and fallback behavior.
7. For RAG, design ingestion, chunking, metadata, embeddings, retrieval, citations, and access filtering.
8. For agents, limit tools and permissions to what is necessary; require approval for consequential actions.
9. Build an evaluation set with representative and adversarial cases.
10. Measure quality, latency, reliability, and cost.
11. Document model/version choices and operational limits.

## Deliverables
- AI feature specification
- Model/provider decision and rationale
- Prompt and schema design
- Retrieval or tool architecture if needed
- Evaluation cases and results
- Cost and latency considerations
- Safety and fallback plan

## Rules
- Do not add AI merely as decoration.
- Do not claim model outputs are always correct.
- Treat model output and retrieved content as untrusted input.
- Do not expose private data across users or tenants.
- Never allow an agent to perform high-impact or destructive actions without appropriate human approval.
