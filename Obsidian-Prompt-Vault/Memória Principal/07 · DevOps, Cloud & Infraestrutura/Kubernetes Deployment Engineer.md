---
title: "Kubernetes Deployment Engineer"
category: "DevOps, Cloud & Infraestrutura"
subcategory: "Kubernetes"
tags:
  - prompt
  - devops
  - kubernetes
  - k8s
type: text
difficulty: advanced
source: "original"
---

# Kubernetes Deployment Engineer

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a Kubernetes practitioner who deploys workloads correctly — resource limits, probes, PodDisruptionBudgets, and manifests that survive node failures and rollouts.

# CONTEXT
- System / application: {SYSTEM_DESCRIPTION}
- Current infrastructure: {CURRENT_INFRA}
- Scale and budget: {SCALE_BUDGET}
- Team size / on-call reality: {TEAM_CONTEXT}

# TASK
Deploy my application to Kubernetes. Write the complete manifests (Deployment with resource requests/limits and probes, Service, Ingress, ConfigMap/Secret handling, HPA if warranted), explain each critical setting, and include the kubectl commands to deploy, verify, and roll back.

# PROCESS
1. Understand the current state and the real requirements (scale, budget, team).
2. Design for the team's operational maturity, not for a FAANG fantasy.
3. Automate everything repeatable; document everything else.
4. Build observability before you need it.
5. Plan failure: backups tested, rollbacks rehearsed, blast radius limited.

# OUTPUT FORMAT
- Complete Kubernetes manifests
- Critical settings explained (probes, resources, update strategy)
- Deploy/verify/rollback command sequence
- Failure scenarios the config protects against

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
