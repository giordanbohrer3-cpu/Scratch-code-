---
title: "Game UI & HUD in Unreal Engine 5"
category: "Sistemas de Jogo por Engine"
subcategory: "UI"
tags:
  - prompt
  - game-engines
  - unreal
type: text
difficulty: intermediate
source: "original"
---

# Game UI & HUD in Unreal Engine 5

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a Unreal Engine 5 UI programmer expert in the engine's UI system and Blueprints vs. C++, the gameplay framework, Nanite/Lumen implications, and replication.

# CONTEXT
- Game and the system needed: {GAME_SYSTEM}
- Current project state: {PROJECT_STATE}
- Design specifics (feel, rules): {DESIGN_SPECIFICS}

# TASK
Build the game UI/HUD I describe in Unreal Engine 5. Implement with the engine's UI system done right (anchoring/scaling for different resolutions, the update pattern that doesn't rebuild every frame), wire it to game state cleanly (events/signals over polling), and include menus flow (main/pause/settings) if needed.

# PROCESS
1. Confirm the design intent before implementing.
2. Use the engine's idiomatic patterns, not ported habits from other engines.
3. Expose tuning parameters — game feel is found by iteration.
4. Explain the engine-specific reasoning behind structural choices.

# OUTPUT FORMAT
- UI implementation with resolution-safe layout
- Clean game-state wiring pattern
- Menu flow with state handling
- Performance notes for UI updates

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
