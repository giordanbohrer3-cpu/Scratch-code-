---
title: "Self-Critique Loop"
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

# Self-Critique Loop

> [!info] Como usar
> Make the AI review and improve its own answer. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Complete the task below in three passes. PASS 1 — produce your best answer. PASS 2 — critique it ruthlessly as a hostile expert reviewer: factual errors, logical gaps, missing cases, weak evidence, unclear writing. List every flaw found. PASS 3 — produce the improved final version fixing every flaw from pass 2. Show all three passes.

The task: {TASK}
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{TASK}` | A tarefa a executar com auto-revisão |
