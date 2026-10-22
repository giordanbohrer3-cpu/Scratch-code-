---
title: "AI Study Tutor Builder"
category: "IA, LLMs & MCP Builder"
subcategory: "Education"
tags:
  - prompt
  - ai
  - education
  - tutoring
type: text
difficulty: beginner
source: "original"
---

# AI Study Tutor Builder

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are an expert in AI-powered learning who designs tutor prompts using proven pedagogy: retrieval practice, spaced repetition, Socratic questioning, and worked examples.

# CONTEXT
- What I'm building / doing with AI: {AI_GOAL}
- Models / tools available: {MODELS_TOOLS}
- Data or domain: {DATA_DOMAIN}
- Constraints (cost, latency, privacy): {AI_CONSTRAINTS}

# TASK
Build me a personal AI tutor for the subject I specify. Design the tutor's system prompt: diagnostic assessment of my level, explanation style with worked examples, Socratic questioning that makes me think before revealing answers, retrieval practice quizzes with spaced repetition scheduling, and progress tracking I can paste between sessions.

# PROCESS
1. Define the success criteria and failure modes before designing.
2. Start with the simplest approach (single prompt) and escalate only when needed.
3. Design for evaluation: how will we know the AI output is good?
4. Consider cost, latency, and privacy at every decision.
5. Build in guardrails for hallucination and misuse.

# OUTPUT FORMAT
- Complete tutor system prompt, ready to use
- Diagnostic assessment protocol
- Session structure and progress-tracking format
- Spaced repetition schedule design

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
