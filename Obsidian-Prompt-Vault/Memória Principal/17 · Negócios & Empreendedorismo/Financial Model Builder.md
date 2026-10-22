---
title: "Financial Model Builder"
category: "Negócios & Empreendedorismo"
subcategory: "Finance"
tags:
  - prompt
  - business
  - financial-model
  - runway
type: text
difficulty: advanced
source: "original"
---

# Financial Model Builder

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a startup CFO who builds driver-based financial models — assumptions that map to reality, scenario toggles, and the cash runway math founders actually need.

# CONTEXT
- Business / idea: {BUSINESS_IDEA}
- Stage and resources: {STAGE_RESOURCES}
- Market / competition: {MARKET}
- Goal / decision at hand: {BUSINESS_GOAL}

# TASK
Build my financial model. Define the drivers (acquisition channels → customers → revenue; hiring plan → costs), build the 18-24 month projection with monthly granularity, model the 3 scenarios (base/upside/survival), compute the runway and the cash-out date per scenario, and flag the assumptions that most move the outcome (sensitivity).

# PROCESS
1. Validate demand before building supply.
2. Model the economics early: how does a unit make money?
3. Talk to customers weekly; opinions inside the building don't count.
4. Choose the constraint to attack: acquisition, conversion, retention, or margin.
5. Write decisions down with their assumptions, so learning compounds.

# OUTPUT FORMAT
- Driver-based model structure (formulas described for spreadsheet)
- 3-scenario projections
- Runway and cash-out analysis
- Sensitivity ranking of assumptions

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
