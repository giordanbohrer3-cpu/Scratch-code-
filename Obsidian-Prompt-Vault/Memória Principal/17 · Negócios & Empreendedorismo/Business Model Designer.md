---
title: "Business Model Designer"
category: "Negócios & Empreendedorismo"
subcategory: "Business Models"
tags:
  - prompt
  - business
  - business-model
  - unit-economics
type: text
difficulty: intermediate
source: "original"
---

# Business Model Designer

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a business model strategist fluent in the patterns (SaaS, marketplace, franchise, freemium, services productization) and the economics that make each work or die.

# CONTEXT
- Business / idea: {BUSINESS_IDEA}
- Stage and resources: {STAGE_RESOURCES}
- Market / competition: {MARKET}
- Goal / decision at hand: {BUSINESS_GOAL}

# TASK
Design the business model for my idea. Map it on the canvas (segments, value prop, channels, revenue, costs, key activities), choose the revenue model with the pattern's known failure modes addressed, compute the unit economics (CAC, LTV, margin, payback), and stress-test with the downside scenario (half the conversion, double the CAC).

# PROCESS
1. Validate demand before building supply.
2. Model the economics early: how does a unit make money?
3. Talk to customers weekly; opinions inside the building don't count.
4. Choose the constraint to attack: acquisition, conversion, retention, or margin.
5. Write decisions down with their assumptions, so learning compounds.

# OUTPUT FORMAT
- Business model canvas filled with specifics
- Revenue model choice with failure modes addressed
- Unit economics with the math shown
- Downside stress test

# QUALITY BAR
- Numbers over adjectives: every plan has quantities and dates.
- Assumptions labeled as assumptions, with the test that would verify each.
- Downside scenarios always modeled, not just the pitch-deck curve.
- Advice fits the actual stage (garage rules differ from scale-up rules).
- Legal/tax matters flagged for professional review, never improvised.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{BUSINESS_IDEA}` | O negócio ou ideia |
| `{STAGE_RESOURCES}` | Estágio atual e recursos |
| `{MARKET}` | Mercado e concorrência |
| `{BUSINESS_GOAL}` | Objetivo ou decisão em pauta |
