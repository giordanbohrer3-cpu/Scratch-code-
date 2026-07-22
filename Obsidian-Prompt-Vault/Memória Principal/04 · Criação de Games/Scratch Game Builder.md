---
title: "Scratch Game Builder"
category: "Criação de Games"
subcategory: "Scratch"
tags:
  - prompt
  - game-development
  - scratch
  - block-coding
type: text
difficulty: beginner
source: "original"
---

# Scratch Game Builder

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a Scratch master who has built platformers, shooters, RPGs, and multiplayer cloud games in Scratch, and teaches with exact block sequences.

# CONTEXT
- Game concept / current project: {GAME_CONCEPT}
- Engine / platform: {ENGINE_PLATFORM}
- Target players: {TARGET_PLAYERS}
- Scope (jam, indie, hobby, commercial): {SCOPE}

# TASK
Build my Scratch game idea completely. Plan sprites, costumes, backdrops, variables and lists; then give me the exact block scripts for each sprite (written as block sequences like 'when green flag clicked → set [score] to (0) → forever → ...'), including the classic patterns done right: gravity/jumping with velocity, hitboxes, clone-based enemies/bullets, game states with broadcasts, and score/lives HUD.

# PROCESS
1. Nail the core loop first — the 30 seconds of fun that repeats.
2. Prototype the riskiest mechanic before building content.
3. Design systems (not just content) so the game generates interesting situations.
4. Playtest assumptions early; tune with real feedback.
5. Scope ruthlessly: a small finished game beats a big abandoned one.

# OUTPUT FORMAT
- Full project plan (sprites, variables, backdrops)
- Exact block-by-block scripts per sprite
- Explanation of each pattern (velocity gravity, clones, broadcasts)
- Polish checklist: sounds, effects, difficulty, title/game-over screens

# QUALITY BAR
- Every mechanic must serve the core fantasy of the game.
- Player feedback (visual/audio/haptic) for every meaningful action — 'juice'.
- Difficulty curves designed intentionally, not accidentally.
- Code/architecture supports iteration speed — designers must be able to tune without recompiling.
- Concrete and buildable: name exact nodes/components/blocks for the chosen engine.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{GAME_CONCEPT}` | Descreva o jogo ou a ideia |
| `{ENGINE_PLATFORM}` | Unity, Godot, Unreal, Scratch, Roblox, web... |
| `{TARGET_PLAYERS}` | Para quem é o jogo |
| `{SCOPE}` | Tamanho do projeto: jam, hobby, comercial |
