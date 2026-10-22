---
title: "Steelman Both Sides"
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

# Steelman Both Sides

> [!info] Como usar
> Understand a debate by strengthening both positions. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Steelman both sides of this question: {QUESTION}. For each side: present the STRONGEST version of the argument (the version its smartest advocates make, not the strawman), the best evidence supporting it, and the values/premises someone holds when this side convinces them. Then: identify the crux — the specific factual or value disagreement the debate actually reduces to — and what evidence would settle it. Do not tell me which side you favor until I ask.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{QUESTION}` | A questão em debate |
