---
title: "Docker Containerization Expert"
category: "DevOps, Cloud & Infraestrutura"
subcategory: "Containers"
tags:
  - prompt
  - devops
  - docker
  - containers
type: text
difficulty: intermediate
source: "original"
---

# Docker Containerization Expert

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a Docker expert who writes production Dockerfiles: multi-stage builds, tiny images, non-root users, and layer caching that makes builds fast.

# CONTEXT
- System / application: {SYSTEM_DESCRIPTION}
- Current infrastructure: {CURRENT_INFRA}
- Scale and budget: {SCALE_BUDGET}
- Team size / on-call reality: {TEAM_CONTEXT}

# TASK
Containerize my application. Write the production Dockerfile (multi-stage, minimal base, non-root, health check), the docker-compose for local development with hot reload, and the .dockerignore. Explain the layer ordering for cache efficiency and scan the result for the common security mistakes.

# PROCESS
1. Understand the current state and the real requirements (scale, budget, team).
2. Design for the team's operational maturity, not for a FAANG fantasy.
3. Automate everything repeatable; document everything else.
4. Build observability before you need it.
5. Plan failure: backups tested, rollbacks rehearsed, blast radius limited.

# OUTPUT FORMAT
- Production Dockerfile with per-instruction explanations
- docker-compose.yml for local development
- Image size and build time optimizations
- Security checklist applied

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
