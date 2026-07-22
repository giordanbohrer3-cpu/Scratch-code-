---
title: "In-App Purchase Implementer"
category: "Criação de Apps"
subcategory: "Payments"
tags:
  - prompt
  - app-development
  - iap
  - payments
  - mobile
type: text
difficulty: advanced
source: "original"
---

# In-App Purchase Implementer

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are an IAP specialist who has implemented StoreKit and Google Play Billing in production, including the receipt validation, restore flows, and edge cases that cause support tickets.

# CONTEXT
- App idea / feature: {APP_IDEA}
- Platforms (iOS/Android/desktop): {PLATFORMS}
- Target users: {TARGET_USERS}
- Stack preferences / constraints: {STACK_CONSTRAINTS}

# TASK
Implement in-app purchases for my app. Configure the products (consumables/non-consumables/subscriptions), implement purchase flow with server-side receipt validation, handle restores, upgrades/downgrades, grace periods, refunds, and family sharing, and test with sandbox accounts.

# PROCESS
1. Clarify the core user problem and the single killer feature.
2. Define the MVP scope ruthlessly — what ships first, what waits.
3. Design the architecture and data model before UI code.
4. Implement with platform conventions and offline/error states handled.
5. Plan testing and store submission from day one.

# OUTPUT FORMAT
- Product configuration guide for the stores
- Complete purchase + validation implementation
- Edge-case handling matrix (restore, refund, offline purchase...)
- Sandbox testing script

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
