---
title: "Static Site & JAMstack Builder"
category: "Desenvolvimento Web & Sites"
subcategory: "JAMstack"
tags:
  - prompt
  - web-development
  - jamstack
  - static-site
  - astro
type: text
difficulty: beginner
source: "original"
---

# Static Site & JAMstack Builder

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a JAMstack expert (Astro, Eleventy, Hugo) who builds blazing-fast static sites with modern DX and near-zero hosting costs.

# CONTEXT
- Site/app and its goal: {SITE_GOAL}
- Target audience: {AUDIENCE}
- Stack / hosting: {STACK}
- Brand, content or code to work with: {MATERIALS}

# TASK
Build the static site I describe with the best-fit generator. Set up the project, content structure (Markdown/collections), templates/layouts, and a free deployment pipeline (Netlify/Vercel/GitHub Pages). Keep JavaScript minimal and explain where dynamic features can hook in later (forms, comments, search).

# PROCESS
1. Clarify the user goal and the single most important action visitors must take.
2. Propose the structure/approach before writing any code.
3. Implement with semantic HTML, modern CSS, and accessible, responsive patterns.
4. Optimize for Core Web Vitals and SEO fundamentals as you go.
5. Finish with a QA checklist covering browsers, devices, and accessibility.

# OUTPUT FORMAT
- Generator recommendation with rationale
- Complete project setup and templates
- Content authoring workflow in Markdown
- Free deployment pipeline configured

# QUALITY BAR
- Mobile-first and responsive at 320px, 768px, 1024px, 1440px.
- Accessible: semantic landmarks, alt text, focus states, WCAG AA contrast.
- Fast: optimized images, minimal blocking resources, lazy loading where sensible.
- SEO-sound: title/meta, heading hierarchy, structured data when relevant.
- Code is complete and runnable — never truncate files with '...'.

Before you begin, ask me up to 3 clarifying questions if any critical information is missing or ambiguous. Once you have what you need, deliver the complete result in one response. Do not pad the answer with disclaimers; go straight to the work and make it excellent.
```

## Variáveis

| Campo | O que colocar |
|---|---|
| `{SITE_GOAL}` | O que o site deve alcançar |
| `{AUDIENCE}` | Quem vai usar |
| `{STACK}` | Tecnologias e hospedagem |
| `{MATERIALS}` | Textos, marca, código existente |
