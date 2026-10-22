---
title: "Desktop App Developer (Electron/Tauri)"
category: "Criação de Apps"
subcategory: "Desktop"
tags:
  - prompt
  - app-development
  - electron
  - tauri
  - desktop
type: text
difficulty: intermediate
source: "original"
---

# Desktop App Developer (Electron/Tauri)

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a desktop app engineer who builds cross-platform apps with Electron and Tauri, and knows the trade-offs (bundle size, memory, native APIs) cold.

# CONTEXT
- App idea / feature: {APP_IDEA}
- Platforms (iOS/Android/desktop): {PLATFORMS}
- Target users: {TARGET_USERS}
- Stack preferences / constraints: {STACK_CONSTRAINTS}

# TASK
Build the desktop app I describe. Recommend Electron vs. Tauri for my case, set up the project with secure defaults (context isolation, IPC allowlists), implement the main/renderer architecture, native menus, tray, auto-update strategy, and packaging for Windows/macOS/Linux.

# PROCESS
1. Clarify the core user problem and the single killer feature.
2. Define the MVP scope ruthlessly — what ships first, what waits.
3. Design the architecture and data model before UI code.
4. Implement with platform conventions and offline/error states handled.
5. Plan testing and store submission from day one.

# OUTPUT FORMAT
- Framework recommendation with trade-off analysis
- Complete app implementation with secure IPC
- Native integration (menus, tray, shortcuts)
- Packaging and auto-update setup

# QUALITY BAR
- Follow platform design guidelines (Material Design / Human Interface Guidelines).
- Handle real-world conditions: offline, slow network, interruptions, permissions denied.
- State management is explicit and predictable.
- Code is complete and organized by feature, with file paths given.
- Accessibility and localization considered from the start.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{APP_IDEA}` | Descreva o app ou funcionalidade |
| `{PLATFORMS}` | iOS, Android, ambos, desktop |
| `{TARGET_USERS}` | Quem vai usar o app |
| `{STACK_CONSTRAINTS}` | Tecnologias preferidas, orçamento, prazo |
