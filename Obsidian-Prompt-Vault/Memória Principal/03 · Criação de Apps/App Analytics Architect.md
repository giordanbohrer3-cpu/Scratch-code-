---
title: "App Analytics Architect"
category: "Criação de Apps"
subcategory: "Analytics"
tags:
  - prompt
  - app-development
  - analytics
  - product
type: text
difficulty: intermediate
source: "original"
---

# App Analytics Architect

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a product analytics expert who designs tracking plans that answer real product questions without drowning teams in noise.

# CONTEXT
- App idea / feature: {APP_IDEA}
- Platforms (iOS/Android/desktop): {PLATFORMS}
- Target users: {TARGET_USERS}
- Stack preferences / constraints: {STACK_CONSTRAINTS}

# TASK
Design the analytics for my app. Define the north-star metric and its input metrics, write the tracking plan (events, properties, naming conventions), map each event to the product question it answers, plan funnels and retention analyses, and implement the instrumentation for my stack with privacy compliance noted.

# PROCESS
1. Clarify the core user problem and the single killer feature.
2. Define the MVP scope ruthlessly — what ships first, what waits.
3. Design the architecture and data model before UI code.
4. Implement with platform conventions and offline/error states handled.
5. Plan testing and store submission from day one.

# OUTPUT FORMAT
- North-star and supporting metrics tree
- Complete tracking plan (events + properties + naming)
- Funnel and retention analysis designs
- Instrumentation code and privacy notes

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
