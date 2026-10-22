---
title: "Tree-of-Thoughts Explorer"
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

# Tree-of-Thoughts Explorer

> [!info] Como usar
> Explore multiple solution branches before committing. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Solve this by exploring multiple approaches in parallel before committing. Generate 3 fundamentally different approaches to the problem. For each: sketch how it would work, its strongest advantage, its fatal risk, and a confidence score (1-10). Then pick the most promising branch and develop it fully. If you hit a dead end while developing it, back up and switch branches explicitly, saying why.

The problem: {PROBLEM}
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{PROBLEM}` | O problema a explorar |
