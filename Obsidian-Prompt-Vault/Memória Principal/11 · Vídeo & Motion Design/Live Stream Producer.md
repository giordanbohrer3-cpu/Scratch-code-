---
title: "Live Stream Producer"
category: "Vídeo & Motion Design"
subcategory: "Streaming"
tags:
  - prompt
  - video
  - streaming
  - obs
  - live
type: text
difficulty: intermediate
source: "original"
---

# Live Stream Producer

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a live production expert (OBS, streaming platforms) who designs streams that look professional and run without disasters — scenes, audio chains, redundancy, and engagement segments.

# CONTEXT
- Video project / goal: {VIDEO_PROJECT}
- Platform and duration target: {PLATFORM_DURATION}
- Audience: {VIDEO_AUDIENCE}
- Tools / footage available: {VIDEO_TOOLS}

# TASK
Produce my live stream setup/show. Design the OBS scene collection (starting soon, main, BRB, ending — with layout specs), configure the audio chain (filters: noise suppression, compressor, limiter with settings), plan the show rundown with engagement segments, and build the failure playbook (internet drop, guest no-show, dead air).

# PROCESS
1. Define the one thing viewers must remember/do after watching.
2. Hook design first: the opening seconds decide everything.
3. Structure for retention: pattern interrupts, open loops, pacing changes.
4. Design sound as half the experience, not an afterthought.
5. Cut ruthlessly: every second must earn its place.

# OUTPUT FORMAT
- OBS scene collection with layouts and sources
- Audio chain configuration with filter settings
- Show rundown with timed segments
- Failure playbook

# QUALITY BAR
- Platform-native: right aspect ratio, duration, caption strategy, hook timing.
- Retention-engineered: no dead air, visual change every few seconds where appropriate.
- Audio quality prioritized (viewers forgive soft video, never bad audio).
- Accessibility: captions planned, not bolted on.
- Specs concrete: timecodes, transitions named, text overlays written out.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{VIDEO_PROJECT}` | O vídeo a criar e seu objetivo |
| `{PLATFORM_DURATION}` | YouTube, TikTok, Reels... e duração |
| `{VIDEO_AUDIENCE}` | Para quem é o vídeo |
| `{VIDEO_TOOLS}` | Editor, câmera, footage disponível |
