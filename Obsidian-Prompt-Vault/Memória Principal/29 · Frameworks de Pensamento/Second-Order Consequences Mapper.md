---
title: "Second-Order Consequences Mapper"
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

# Second-Order Consequences Mapper

> [!info] Como usar
> See past the immediate effects of a decision. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Map the consequence cascade of my decision. First-order: the immediate effects (obvious, usually what people decide on). Second-order: what each first-order effect causes next — especially the incentives it changes (who now behaves differently?). Third-order: the equilibrium after everyone adapts. For each order, mark effects as positive/negative/uncertain for me. Conclude: does the decision still look good at order three? What early indicator would reveal the cascade going wrong?

The decision: {DECISION}
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{DECISION}` | A decisão a analisar |
