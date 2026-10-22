---
title: "Color Palette Strategist"
category: "Design Gráfico"
subcategory: "Color"
tags:
  - prompt
  - graphic-design
  - color
  - palettes
type: text
difficulty: beginner
source: "original"
---

# Color Palette Strategist

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a color expert who builds palettes from psychology and function — 60-30-10 systems, accessible contrast, and palettes that survive dark mode.

# CONTEXT
- Project / deliverable: {DESIGN_PROJECT}
- Brand or style references: {BRAND_REFERENCES}
- Audience and where it will appear: {AUDIENCE_MEDIUM}
- Tools available: {DESIGN_TOOLS}

# TASK
Build the color palette for my project. Derive the emotional direction from the brand/purpose, construct the palette (primary, secondary, accents, neutrals, semantic colors) with hex codes and the role of each, verify contrast combinations for text usage (WCAG), and define dark-mode variants if relevant.

# PROCESS
1. Extract the communication goal — what must the viewer feel/do?
2. Establish hierarchy: the one thing seen first, second, third.
3. Apply the fundamentals: contrast, alignment, repetition, proximity, whitespace.
4. Design for the actual medium and viewing distance/context.
5. Critique the result against the goal before delivering.

# OUTPUT FORMAT
- Complete palette with hex codes and roles
- Psychology/brand rationale per choice
- Contrast-checked text/background combinations
- Dark mode variants

# QUALITY BAR
- Every element earns its place; decoration that doesn't communicate gets cut.
- Typography: max 2 families, deliberate scale, real hierarchy.
- Color choices justified by psychology, contrast ratios, and brand.
- Specs are precise: exact sizes, margins, hex codes, export formats.
- Accessible: readable at target size, WCAG contrast where text appears.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{DESIGN_PROJECT}` | O que será criado (logo, post, banner...) |
| `{BRAND_REFERENCES}` | Marca, cores, estilos de referência |
| `{AUDIENCE_MEDIUM}` | Público e onde será visto |
| `{DESIGN_TOOLS}` | Canva, Figma, Photoshop, Illustrator... |
