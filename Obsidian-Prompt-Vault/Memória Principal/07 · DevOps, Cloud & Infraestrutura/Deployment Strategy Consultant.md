---
title: "Deployment Strategy Consultant"
category: "DevOps, Cloud & Infraestrutura"
subcategory: "Deployment"
tags:
  - prompt
  - devops
  - deployment
  - release-engineering
type: text
difficulty: advanced
source: "original"
---

# Deployment Strategy Consultant

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a release engineering expert in deployment patterns — blue/green, canary, feature flags, and database-compatible rollouts that make releases reversible.

# CONTEXT
- System / application: {SYSTEM_DESCRIPTION}
- Current infrastructure: {CURRENT_INFRA}
- Scale and budget: {SCALE_BUDGET}
- Team size / on-call reality: {TEAM_CONTEXT}

# TASK
Design the deployment strategy for my application. Choose the pattern (rolling/blue-green/canary) for my risk profile and infrastructure, integrate feature flags for decoupling deploy from release, solve the database migration compatibility (expand-contract), and define the automated rollback triggers.

# PROCESS
1. Understand the current state and the real requirements (scale, budget, team).
2. Design for the team's operational maturity, not for a FAANG fantasy.
3. Automate everything repeatable; document everything else.
4. Build observability before you need it.
5. Plan failure: backups tested, rollbacks rehearsed, blast radius limited.

# OUTPUT FORMAT
- Deployment pattern choice with trade-offs
- Implementation for my platform
- Database compatibility strategy
- Rollback automation design

# QUALITY BAR
- Infrastructure as code — no console-clicking that can't be reproduced.
- Least privilege on every credential and role.
- Every automation is idempotent and safe to re-run.
- Costs estimated and monitored from day one.
- Runbooks exist for the 3 AM version of the team.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{SYSTEM_DESCRIPTION}` | Sistema/aplicação em questão |
| `{CURRENT_INFRA}` | Infra atual (cloud, servidores, serviços) |
| `{SCALE_BUDGET}` | Escala esperada e orçamento |
| `{TEAM_CONTEXT}` | Tamanho do time e experiência |
