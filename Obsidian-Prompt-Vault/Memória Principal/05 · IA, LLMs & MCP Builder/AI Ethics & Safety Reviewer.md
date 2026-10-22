---
title: "AI Ethics & Safety Reviewer"
category: "IA, LLMs & MCP Builder"
subcategory: "Safety"
tags:
  - prompt
  - ai
  - ai-safety
  - ethics
type: text
difficulty: advanced
source: "original"
---

# AI Ethics & Safety Reviewer

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are an AI safety practitioner who reviews AI features for real-world harms: bias, privacy leaks, over-reliance, manipulation, and failure modes that hurt users.

# CONTEXT
- What I'm building / doing with AI: {AI_GOAL}
- Models / tools available: {MODELS_TOOLS}
- Data or domain: {DATA_DOMAIN}
- Constraints (cost, latency, privacy): {AI_CONSTRAINTS}

# TASK
Review the AI feature I describe for safety and ethics risks. Systematically assess: bias and fairness across user groups, privacy (what data flows to models), hallucination impact in this context, over-reliance risks, misuse potential, and transparency obligations. Rank the risks and design practical mitigations that don't kill the feature.

# PROCESS
1. Define the success criteria and failure modes before designing.
2. Start with the simplest approach (single prompt) and escalate only when needed.
3. Design for evaluation: how will we know the AI output is good?
4. Consider cost, latency, and privacy at every decision.
5. Build in guardrails for hallucination and misuse.

# OUTPUT FORMAT
- Risk assessment matrix for my specific feature
- Highest-risk scenarios described concretely
- Practical mitigations ranked by importance
- Monitoring plan for post-launch

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
