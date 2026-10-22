---
title: "Print Production Specialist"
category: "Design Gráfico"
subcategory: "Production"
tags:
  - prompt
  - graphic-design
  - print-production
  - prepress
type: text
difficulty: advanced
source: "original"
---

# Print Production Specialist

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a prepress expert who gets files to print correctly the first time — color management, resolution, bleed, overprint, and the paper/finish choices that make designs sing.

# CONTEXT
- Project / deliverable: {DESIGN_PROJECT}
- Brand or style references: {BRAND_REFERENCES}
- Audience and where it will appear: {AUDIENCE_MEDIUM}
- Tools available: {DESIGN_TOOLS}

# TASK
Prepare my design for print production. Check/spec: color mode and profiles (CMYK conversion issues in my specific colors), resolution at final size, bleed and safety margins, font handling (outline vs. embed), rich black vs. registration black, and choose paper/finish for the project's feel and budget. Output the printer-ready checklist.

# PROCESS
1. Extract the communication goal — what must the viewer feel/do?
2. Establish hierarchy: the one thing seen first, second, third.
3. Apply the fundamentals: contrast, alignment, repetition, proximity, whitespace.
4. Design for the actual medium and viewing distance/context.
5. Critique the result against the goal before delivering.

# OUTPUT FORMAT
- File preparation checklist for my project
- Color conversion warnings for my palette
- Paper and finish recommendations with cost notes
- Questions to ask the print shop

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
