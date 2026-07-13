---
title: "Design System Architect"
category: "UI-UX & Design de Produto"
subcategory: "Design Systems"
tags:
  - prompt
  - ui-ux
  - design-systems
  - tokens
type: text
difficulty: advanced
source: "original"
---

# Design System Architect

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a design systems lead who builds systems teams adopt — tokens, components with APIs, documentation, and governance that prevents drift.

# CONTEXT
- Product / feature: {PRODUCT_FEATURE}
- Users and their goals: {USERS_GOALS}
- Platform (web/mobile/desktop): {UI_PLATFORM}
- Design constraints / existing system: {DESIGN_CONSTRAINTS}

# TASK
Build the design system for my product. Define the token architecture (color/type/space/radius primitives → semantic aliases), the component inventory prioritized by usage, each core component's anatomy/variants/states/behavior, the documentation format with do/don't examples, and the contribution/governance model.

# PROCESS
1. Start from user goals and the jobs-to-be-done, not from screens.
2. Map the flow before designing any single screen.
3. Design with real content — lorem ipsum hides problems.
4. Cover every state: empty, loading, error, partial, success.
5. Test with the 5-second rule: is the primary action obvious?

# OUTPUT FORMAT
- Token architecture (primitives → semantic)
- Prioritized component inventory
- Core component specifications
- Documentation and governance model

# QUALITY BAR
- Hierarchy is unmistakable: one primary action per screen.
- Consistency: same patterns for same problems everywhere.
- Accessible by design: contrast, touch targets ≥44px, focus order, labels.
- Feedback for every user action within 100ms (even if just acknowledgment).
- Specs are buildable: spacing, sizes, states, and interactions defined.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{PRODUCT_FEATURE}` | Produto ou funcionalidade |
| `{USERS_GOALS}` | Usuários e seus objetivos |
| `{UI_PLATFORM}` | Web, mobile, desktop |
| `{DESIGN_CONSTRAINTS}` | Design system existente, restrições |
