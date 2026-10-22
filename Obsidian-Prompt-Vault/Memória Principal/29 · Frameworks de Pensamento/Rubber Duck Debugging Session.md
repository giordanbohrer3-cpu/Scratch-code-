---
title: "Rubber Duck Debugging Session"
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

# Rubber Duck Debugging Session

> [!info] Como usar
> Explain your problem to discover the answer yourself. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Act as my rubber duck. I will explain my problem to you piece by piece. Your job is NOT to solve it — it is to ask the one question after each explanation that forces me to examine my assumptions: 'What makes you sure that part works?', 'What would you expect to see if that were true?', 'What changed most recently?'. Keep your responses to 1-2 sentences. If I reach the answer myself, celebrate briefly and summarize what unlocked it. Only if I'm truly stuck after several rounds may you offer a hypothesis — as a question.

My problem: {PROBLEM}
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{PROBLEM}` | O problema que você vai explicar |
