---
title: "Pre-Mortem Analysis"
category: "Frameworks de Pensamento"
subcategory: "Reasoning"
tags:
  - prompt
  - frameworks
  - thinking
  - reasoning
type: text
difficulty: beginner
source: "original"
---

# Pre-Mortem Analysis

> [!info] Como usar
> Find the failure before it happens. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Run a pre-mortem on my plan. It is one year from now and the plan has failed completely. Working backwards: generate the 8 most plausible causes of death (be specific to MY plan, not generic risks), rank them by probability × damage, identify the early warning sign for each (what we'd see 3 months before it kills us), and design the mitigation or tripwire for the top 4. Be ruthless — optimism is what pre-mortems exist to correct.

My plan: {PLAN}
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{PLAN}` | O plano a testar |
