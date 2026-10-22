---
title: "Eisenhower Priority Triage"
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

# Eisenhower Priority Triage

> [!info] Como usar
> Sort your overwhelming list into action. Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
Triage my task list with the Eisenhower matrix, but do it rigorously: for each task I list, interrogate the real urgency (deadline-true or anxiety-fake?) and real importance (consequence-linked or just loud?). Sort into: Do now (urgent+important), Schedule (important, not urgent — these get calendar slots, not 'later'), Delegate/Automate (urgent, not important — with the specific delegation/automation suggestion), Delete (neither — with permission to let each go). End with today's top 3 and the calendar blocks for the Schedule quadrant.

My list: {TASK_LIST}
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{TASK_LIST}` | Sua lista de tarefas |
