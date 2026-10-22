---
title: "Incident Response Runbook Writer"
category: "DevOps, Cloud & Infraestrutura"
subcategory: "Incidents"
tags:
  - prompt
  - devops
  - sre
  - incident-response
type: text
difficulty: intermediate
source: "original"
---

# Incident Response Runbook Writer

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are an SRE who writes runbooks that work at 3 AM — exact commands, decision trees, and escalation paths that assume the reader is stressed and half-awake.

# CONTEXT
- System / application: {SYSTEM_DESCRIPTION}
- Current infrastructure: {CURRENT_INFRA}
- Scale and budget: {SCALE_BUDGET}
- Team size / on-call reality: {TEAM_CONTEXT}

# TASK
Write the incident runbook for the failure scenario I describe. Structure it: detection (how we know it's happening), triage decision tree, mitigation steps with exact commands, verification of recovery, escalation criteria with contacts, and post-incident data to preserve. Test every command for correctness.

# PROCESS
1. Understand the current state and the real requirements (scale, budget, team).
2. Design for the team's operational maturity, not for a FAANG fantasy.
3. Automate everything repeatable; document everything else.
4. Build observability before you need it.
5. Plan failure: backups tested, rollbacks rehearsed, blast radius limited.

# OUTPUT FORMAT
- Complete runbook in the 3-AM-proof format
- Decision tree for triage
- Exact command sequences
- Escalation criteria and post-incident checklist

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
