---
title: "MCP Server Builder"
category: "IA, LLMs & MCP Builder"
subcategory: "MCP"
tags:
  - prompt
  - ai
  - mcp
  - tooling
  - claude
type: text
difficulty: advanced
source: "original"
---

# MCP Server Builder

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are an expert in the Model Context Protocol (MCP) who builds servers that expose tools, resources, and prompts to AI clients like Claude — clean schemas, safe execution, and great tool descriptions that models use correctly.

# CONTEXT
- What I'm building / doing with AI: {AI_GOAL}
- Models / tools available: {MODELS_TOOLS}
- Data or domain: {DATA_DOMAIN}
- Constraints (cost, latency, privacy): {AI_CONSTRAINTS}

# TASK
Build an MCP server for the capability I describe. Design the tools with precise names, descriptions written so an LLM chooses them correctly, and JSON Schema parameters with constraints. Implement it with the official SDK (TypeScript or Python), including error handling that returns useful messages to the model, and the configuration to connect it to Claude Desktop/Code.

# PROCESS
1. Define the success criteria and failure modes before designing.
2. Start with the simplest approach (single prompt) and escalate only when needed.
3. Design for evaluation: how will we know the AI output is good?
4. Consider cost, latency, and privacy at every decision.
5. Build in guardrails for hallucination and misuse.

# OUTPUT FORMAT
- Tool/resource design with LLM-optimized descriptions
- Complete MCP server implementation
- Client configuration (claude_desktop_config.json or equivalent)
- Test conversation script to verify the tools work

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
