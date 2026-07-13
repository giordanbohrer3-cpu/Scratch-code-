---
title: "OODA Rapid Decision Loop"
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

# OODA Rapid Decision Loop

> [!info] Como usar
> Decide fast under changing conditions. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Run me through an OODA loop on my fast-moving situation. OBSERVE: what are the raw facts right now, stripped of my interpretation — and what critical data am I missing? ORIENT: what frames fit these facts (list 2-3), which biases might be distorting my read, and what would each frame predict happens next? DECIDE: the options with speed-vs-reversibility ratings — favoring reversible moves under uncertainty. ACT: the concrete next action, the signal to watch, and when we re-loop.

The situation: {SITUATION}
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{SITUATION}` | A situação em movimento |
