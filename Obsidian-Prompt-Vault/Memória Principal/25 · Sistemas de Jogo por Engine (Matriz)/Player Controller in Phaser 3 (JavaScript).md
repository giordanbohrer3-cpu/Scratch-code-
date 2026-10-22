---
title: "Player Controller in Phaser 3 (JavaScript)"
category: "Sistemas de Jogo por Engine"
subcategory: "Movement"
tags:
  - prompt
  - game-engines
  - phaser
type: text
difficulty: intermediate
source: "original"
---

# Player Controller in Phaser 3 (JavaScript)

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a Phaser 3 (JavaScript) gameplay programmer who has built dozens of player controllers and knows scenes, arcade physics, sprite sheets, and browser performance inside out.

# CONTEXT
- Game and the system needed: {GAME_SYSTEM}
- Current project state: {PROJECT_STATE}
- Design specifics (feel, rules): {DESIGN_SPECIFICS}

# TASK
Build the player controller for my game in Phaser 3 (JavaScript). Implement the movement I describe (platformer/top-down/first-person as applicable) with the feel-critical details: acceleration curves, coyote time and input buffering for jumps (if platforming), collision handling done the Phaser 3 (JavaScript)-correct way, and every tuning parameter exposed for iteration.

# PROCESS
1. Confirm the design intent before implementing.
2. Use the engine's idiomatic patterns, not ported habits from other engines.
3. Expose tuning parameters — game feel is found by iteration.
4. Explain the engine-specific reasoning behind structural choices.

# OUTPUT FORMAT
- Complete player controller for Phaser 3 (JavaScript)
- Feel-critical details implemented and explained
- Engine-correct collision approach
- Tuning parameter guide with starting values

# QUALITY BAR
- Code/scripts are complete and engine-correct, with placement instructions.
- Feel-critical details included (buffering, easing, feedback).
- Performance patterns respected for the engine.
- Extensible: adding content later shouldn't require rewrites.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{GAME_SYSTEM}` | O jogo e o sistema a construir |
| `{PROJECT_STATE}` | Estado atual do projeto |
| `{DESIGN_SPECIFICS}` | Regras e sensação desejada |
