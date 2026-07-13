---
title: "Persona Panel Discussion"
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

# Persona Panel Discussion

> [!info] Como usar
> Get multiple expert perspectives debating your question. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Convene a panel of 4 experts with genuinely different perspectives on my question: {EXPERT_1}, {EXPERT_2}, {EXPERT_3}, and {EXPERT_4}. Each gives their opening position (2-3 sentences, in character, with their distinctive reasoning style). Then run 2 rounds of debate where they challenge each other's weakest points specifically. Close with: where they converge (probably true), where they diverge (genuinely uncertain), and the synthesis recommendation.

My question: {QUESTION}
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{QUESTION}` | Sua pergunta |
| `{EXPERT_1}` | Especialista 1 |
| `{EXPERT_2}` | Especialista 2 |
| `{EXPERT_3}` | Especialista 3 |
| `{EXPERT_4}` | Especialista 4 |
