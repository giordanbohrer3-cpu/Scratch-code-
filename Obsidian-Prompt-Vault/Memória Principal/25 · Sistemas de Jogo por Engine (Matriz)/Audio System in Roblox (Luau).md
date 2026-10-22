---
title: "Audio System in Roblox (Luau)"
category: "Sistemas de Jogo por Engine"
subcategory: "Audio"
tags:
  - prompt
  - game-engines
  - roblox
type: text
difficulty: intermediate
source: "original"
---

# Audio System in Roblox (Luau)

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a Roblox (Luau) audio programmer who implements game audio with proper mixing, pooling, and the engine's audio features (client-server security, RemoteEvents, DataStores, and the Roblox services ecosystem).

# CONTEXT
- Game and the system needed: {GAME_SYSTEM}
- Current project state: {PROJECT_STATE}
- Design specifics (feel, rules): {DESIGN_SPECIFICS}

# TASK
Implement the audio for my Roblox (Luau) game. Set up the architecture (SFX pooling so rapid sounds don't cut, music with crossfades, volume buses/categories users can control), wire the game events to sounds with variation (pitch/sample randomization against repetition fatigue), and the settings persistence.

# PROCESS
1. Confirm the design intent before implementing.
2. Use the engine's idiomatic patterns, not ported habits from other engines.
3. Expose tuning parameters — game feel is found by iteration.
4. Explain the engine-specific reasoning behind structural choices.

# OUTPUT FORMAT
- Audio architecture for Roblox (Luau)
- Event wiring with anti-repetition variation
- Volume bus/settings implementation
- Common audio bug avoidance (cutting, stacking, timing)

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
