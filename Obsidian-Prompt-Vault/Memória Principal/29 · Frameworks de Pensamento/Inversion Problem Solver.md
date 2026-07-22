---
title: "Inversion Problem Solver"
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

# Inversion Problem Solver

> [!info] Como usar
> Solve by asking how to guarantee failure. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Solve my problem by inversion. Instead of 'how do I achieve {GOAL}', first answer: 'how would I GUARANTEE failure at this?' Generate the 10 most effective ways to fail, ranked by how commonly people actually do them. Then invert each into its avoidance rule. Finally, audit my current plan/behavior against the list: which failure modes am I already committing? The output is the anti-checklist plus my violations.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{GOAL}` | Seu objetivo |
