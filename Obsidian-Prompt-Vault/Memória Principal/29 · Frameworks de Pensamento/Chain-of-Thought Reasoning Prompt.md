---
title: "Chain-of-Thought Reasoning Prompt"
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

# Chain-of-Thought Reasoning Prompt

> [!info] Como usar
> Force step-by-step reasoning before answers on hard problems. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Think through this problem step by step before giving your final answer. First, restate the problem in your own words. Second, list what is known and unknown. Third, work through the reasoning explicitly, showing each logical step and checking it before building on it. Fourth, consider what could make your reasoning wrong — test at least one alternative path. Only then give your final answer, marked clearly as ## Answer, with a confidence level and the key assumption it depends on.

The problem: {PROBLEM}
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{PROBLEM}` | O problema difícil a resolver |
