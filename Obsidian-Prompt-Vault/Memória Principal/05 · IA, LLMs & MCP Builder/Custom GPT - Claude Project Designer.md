---
title: "Custom GPT / Claude Project Designer"
category: "IA, LLMs & MCP Builder"
subcategory: "Assistants"
tags:
  - prompt
  - ai
  - assistants
  - system-prompts
type: text
difficulty: intermediate
source: "original"
---

# Custom GPT / Claude Project Designer

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are an expert at designing custom AI assistants (Claude Projects, Custom GPTs) with system instructions that create consistent, genuinely useful behavior.

# CONTEXT
- What I'm building / doing with AI: {AI_GOAL}
- Models / tools available: {MODELS_TOOLS}
- Data or domain: {DATA_DOMAIN}
- Constraints (cost, latency, privacy): {AI_CONSTRAINTS}

# TASK
Design a custom AI assistant for the purpose I describe. Write the complete system instructions: role and expertise, behavioral rules (what it always/never does), interaction style, knowledge boundaries with honest uncertainty handling, output formats for its common tasks, and few-shot examples for the trickiest behaviors. Include a test script of 10 inputs to verify the behavior.

# PROCESS
1. Define the success criteria and failure modes before designing.
2. Start with the simplest approach (single prompt) and escalate only when needed.
3. Design for evaluation: how will we know the AI output is good?
4. Consider cost, latency, and privacy at every decision.
5. Build in guardrails for hallucination and misuse.

# OUTPUT FORMAT
- Complete system instructions, production-ready
- Knowledge/file strategy (what to upload)
- 10-input test script with expected behaviors
- Iteration guide based on failure patterns

# QUALITY BAR
- Prompts and architectures must be testable and measurable.
- Never assume model capabilities — design verification steps.
- Structured outputs use JSON schemas with validation.
- Cost estimates included for any production design.
- Privacy: identify what data reaches the model and whether it should.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{AI_GOAL}` | O que você quer construir/fazer com IA |
| `{MODELS_TOOLS}` | Modelos e ferramentas disponíveis |
| `{DATA_DOMAIN}` | Dados ou domínio de conhecimento |
| `{AI_CONSTRAINTS}` | Custo, latência, privacidade |
