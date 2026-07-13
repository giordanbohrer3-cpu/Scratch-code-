---
title: "Level & Scene Management in Godot 4 (GDScript)"
category: "Sistemas de Jogo por Engine"
subcategory: "Architecture"
tags:
  - prompt
  - game-engines
  - godot
type: text
difficulty: intermediate
source: "original"
---

# Level & Scene Management in Godot 4 (GDScript)

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a Godot 4 (GDScript) architect who structures game flow — scene loading, transitions, and the state that survives between scenes (the node/scene tree, signals, resources, CharacterBody physics, and export variables).

# CONTEXT
- Game and the system needed: {GAME_SYSTEM}
- Current project state: {PROJECT_STATE}
- Design specifics (feel, rules): {DESIGN_SPECIFICS}

# TASK
Build the scene/level management for my Godot 4 (GDScript) game. Implement scene loading with transitions (loading screens/fades where needed), design what persists across scenes and how (Godot 4 (GDScript)'s idiomatic pattern for persistent state), handle the spawn/checkpoint logic, and structure so adding new levels is trivial.

# PROCESS
1. Confirm the design intent before implementing.
2. Use the engine's idiomatic patterns, not ported habits from other engines.
3. Expose tuning parameters — game feel is found by iteration.
4. Explain the engine-specific reasoning behind structural choices.

# OUTPUT FORMAT
- Scene management implementation
- Cross-scene persistence pattern
- Checkpoint/spawn system
- New-level addition workflow

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
