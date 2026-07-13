---
title: "Socratic Deep Dive"
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

# Socratic Deep Dive

> [!info] Como usar
> Interrogate a belief you hold until it's earned or abandoned. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Interrogate my belief Socratically. I state it; you probe with one question at a time: What do I mean precisely by the key terms? What evidence would change my mind (and have I looked for it)? Where did this belief come from — reasoning or inheritance? What does the smartest person who disagrees see that I might not? Keep each question focused on my previous answer. After 6-8 rounds, summarize: the belief as refined, the load-bearing assumptions exposed, and whether it survived on evidence or on my attachment.

My belief: {BELIEF}
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{BELIEF}` | A crença a examinar |
