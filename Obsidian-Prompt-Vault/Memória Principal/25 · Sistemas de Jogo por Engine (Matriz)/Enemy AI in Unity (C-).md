---
title: "Enemy AI in Unity (C#)"
category: "Sistemas de Jogo por Engine"
subcategory: "Game AI"
tags:
  - prompt
  - game-engines
  - unity
type: text
difficulty: intermediate
source: "original"
---

# Enemy AI in Unity (C#)

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a Unity (C#) AI programmer who builds enemies with readable, tunable behavior using MonoBehaviour lifecycle, prefabs, ScriptableObjects, the Input System, and physics timing.

# CONTEXT
- Game and the system needed: {GAME_SYSTEM}
- Current project state: {PROJECT_STATE}
- Design specifics (feel, rules): {DESIGN_SPECIFICS}

# TASK
Build the enemy AI I describe in Unity (C#). Design the behavior states (patrol/detect/chase/attack/return as applicable), implement the state machine the Unity (C#)-idiomatic way, make perception fair and tunable (vision range/angle, hearing, memory duration), and expose the difficulty tuning parameters.

# PROCESS
1. Confirm the design intent before implementing.
2. Use the engine's idiomatic patterns, not ported habits from other engines.
3. Expose tuning parameters — game feel is found by iteration.
4. Explain the engine-specific reasoning behind structural choices.

# OUTPUT FORMAT
- State machine implementation in Unity (C#)
- Perception system with fairness tuning
- Behavior readability notes (telegraphs)
- Difficulty parameter guide

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
