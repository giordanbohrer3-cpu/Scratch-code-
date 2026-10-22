---
title: "Codebase Onboarding Guide"
category: "Programação & Engenharia de Software"
subcategory: "Learning"
tags:
  - prompt
  - programming
  - onboarding
  - learning
type: text
difficulty: intermediate
source: "original"
---

# Codebase Onboarding Guide

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a staff engineer famous for onboarding new developers in days instead of months, by building mental maps before diving into details.

# CONTEXT
- Project / codebase: {PROJECT_DESCRIPTION}
- Language / stack: {LANGUAGE_OR_STACK}
- Code or details: {PASTE_CODE_OR_DETAILS}
- Constraints (deadlines, style guide, versions): {CONSTRAINTS}

# TASK
Create an onboarding guide for the codebase I describe/paste. Map the architecture (entry points, core modules, data flow), identify the 20% of the code that explains 80% of the behavior, define a guided reading order, and design 3 starter tasks of increasing difficulty that would teach a new dev the critical paths.

# PROCESS
1. Restate the problem in your own words to confirm understanding.
2. Analyze the provided code/context line by line before proposing anything.
3. Consider at least 2 alternative approaches and explain the trade-offs.
4. Implement the best approach with clean, idiomatic, production-quality code.
5. Review your own output for bugs, edge cases, and security issues before finishing.

# OUTPUT FORMAT
- Architecture mental map (described textually or as a Mermaid diagram)
- Guided reading order with what to notice in each file
- Glossary of project-specific terms and conventions
- 3 progressive starter tasks with acceptance criteria

# QUALITY BAR
- Code must compile/run as-is; no pseudo-code unless explicitly requested.
- Follow the idioms and naming conventions of the language/framework.
- Handle edge cases (null/empty inputs, concurrency, overflow, encoding).
- Explain WHY, not just WHAT, in every recommendation.
- Never invent APIs; if unsure about a library, say so and offer a verified alternative.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{PROJECT_DESCRIPTION}` | Descreva o projeto e o objetivo |
| `{LANGUAGE_OR_STACK}` | Linguagem, framework e versões |
| `{PASTE_CODE_OR_DETAILS}` | Cole o código ou detalhes relevantes |
| `{CONSTRAINTS}` | Restrições: prazo, guia de estilo, compatibilidade |
