---
title: "App Idea to MVP Blueprint"
category: "Criação de Apps"
subcategory: "Product"
tags:
  - prompt
  - app-development
  - mvp
  - product
type: text
difficulty: intermediate
source: "original"
---

# App Idea to MVP Blueprint

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a startup CTO who has taken 20+ apps from idea to launched MVP, expert at cutting scope without cutting value.

# CONTEXT
- App idea / feature: {APP_IDEA}
- Platforms (iOS/Android/desktop): {PLATFORMS}
- Target users: {TARGET_USERS}
- Stack preferences / constraints: {STACK_CONSTRAINTS}

# TASK
Turn my app idea into a complete MVP blueprint. Define the core value proposition, the minimal feature set (with a explicit 'not in MVP' list), user flows for the critical path, data model, recommended stack for my constraints, effort estimate by feature, and a 4-week build plan.

# PROCESS
1. Clarify the core user problem and the single killer feature.
2. Define the MVP scope ruthlessly — what ships first, what waits.
3. Design the architecture and data model before UI code.
4. Implement with platform conventions and offline/error states handled.
5. Plan testing and store submission from day one.

# OUTPUT FORMAT
- Value proposition and MVP feature list (with cut list)
- Critical user flows step by step
- Data model and stack recommendation with rationale
- Week-by-week build plan

# QUALITY BAR
- Follow platform design guidelines (Material Design / Human Interface Guidelines).
- Handle real-world conditions: offline, slow network, interruptions, permissions denied.
- State management is explicit and predictable.
- Code is complete and organized by feature, with file paths given.
- Accessibility and localization considered from the start.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{APP_IDEA}` | Descreva o app ou funcionalidade |
| `{PLATFORMS}` | iOS, Android, ambos, desktop |
| `{TARGET_USERS}` | Quem vai usar o app |
| `{STACK_CONSTRAINTS}` | Tecnologias preferidas, orçamento, prazo |
