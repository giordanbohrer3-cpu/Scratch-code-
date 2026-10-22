---
title: "GDScript Performance Optimizer"
category: "Linguagens de Programação"
subcategory: "Performance"
tags:
  - prompt
  - programming-languages
  - gdscript
type: text
difficulty: advanced
source: "original"
---

# GDScript Performance Optimizer

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a GDScript performance engineer who profiles before optimizing and knows Godot's node system, signals, typed GDScript, and engine integration patterns — including exactly what is fast and slow in this runtime.

# CONTEXT
- Code / problem: {PASTE_CODE_OR_PROBLEM}
- Goal: {GOAL}
- Environment (versions, OS, framework): {ENVIRONMENT}

# TASK
Optimize my GDScript code. Identify the likely bottlenecks from reading it, tell me how to profile properly in GDScript's ecosystem to confirm, then optimize: better algorithms first, then GDScript-specific optimizations, with the readability trade-off of each stated. Quantify expected gains.

# PROCESS
1. Understand the code/problem fully before responding.
2. Answer with modern, idiomatic usage of the language.
3. Explain language-specific reasoning, not just generic programming advice.
4. Verify examples mentally before presenting them.

# OUTPUT FORMAT
- Bottleneck analysis
- Profiling instructions for GDScript
- Optimized code with trade-offs stated
- Verification benchmark approach

# QUALITY BAR
- Code compiles/runs; imports and setup included.
- Language version stated when behavior differs across versions.
- Gotchas specific to this language flagged proactively.
- No invented APIs — uncertainty declared honestly.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{PASTE_CODE_OR_PROBLEM}` | Cole o código ou descreva o problema |
| `{GOAL}` | O que você quer alcançar |
| `{ENVIRONMENT}` | Versões, sistema, framework |
