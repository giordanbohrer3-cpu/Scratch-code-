---
title: "Five Whys Root Cause"
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

# Five Whys Root Cause

> [!info] Como usar
> Drill from symptom to root cause. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Run a Five Whys analysis on my problem. Start from the symptom I give you, and ask 'why did that happen?' — but do it properly: at each level, verify the answer is a cause (not a parallel symptom or a blame), consider whether multiple causes branch (follow each significant branch), and stop when we reach something we can actually fix (a process, a design, a missing safeguard — roots are rarely 'human error'). Conclude with the root cause(s), the fix for each, and the systemic change that prevents the class of problem.

The symptom: {SYMPTOM}
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{SYMPTOM}` | O sintoma/problema observado |
