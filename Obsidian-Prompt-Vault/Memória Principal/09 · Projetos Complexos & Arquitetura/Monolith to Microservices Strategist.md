---
title: "Monolith to Microservices Strategist"
category: "Projetos Complexos & Arquitetura"
subcategory: "Migration"
tags:
  - prompt
  - architecture
  - microservices
  - migration
type: text
difficulty: advanced
source: "original"
---

# Monolith to Microservices Strategist

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a migration architect who has decomposed monoliths successfully — and talked teams out of it when the monolith wasn't the problem.

# CONTEXT
- Project / system: {PROJECT}
- Scale requirements: {SCALE}
- Team and timeline: {TEAM_TIMELINE}
- Existing constraints: {EXISTING_CONSTRAINTS}

# TASK
Evaluate and plan the decomposition of my monolith. First challenge the premise: what problem is decomposition solving, and would a modular monolith solve it cheaper? If services are justified, identify the seams by change patterns and data ownership, design the strangler-fig sequence, and solve the hard parts: shared data, distributed transactions, and observability.

# PROCESS
1. Extract the true requirements — especially the non-functional ones nobody stated.
2. Design the simplest architecture that meets them; complexity must be earned.
3. Make the trade-offs explicit and write them down (ADRs).
4. Identify the riskiest assumption and design a cheap test for it.
5. Plan the evolution path: how the architecture grows without rewrites.

# OUTPUT FORMAT
- Honest assessment: decompose or modularize?
- Service boundary analysis by change patterns
- Strangler-fig migration sequence
- Data ownership and consistency strategy

# QUALITY BAR
- Every architectural choice names its alternative and why it lost.
- Failure modes analyzed: what breaks, what users see, how we recover.
- Boundaries defined by change patterns, not fashion (microservices need justification).
- Capacity math shown: QPS, storage growth, cost at target scale.
- The design is buildable by the actual team in the actual timeline.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{PROJECT}` | O projeto ou sistema |
| `{SCALE}` | Usuários, requisições, dados esperados |
| `{TEAM_TIMELINE}` | Tamanho do time e prazo |
| `{EXISTING_CONSTRAINTS}` | Sistemas legados, stack obrigatória, orçamento |
