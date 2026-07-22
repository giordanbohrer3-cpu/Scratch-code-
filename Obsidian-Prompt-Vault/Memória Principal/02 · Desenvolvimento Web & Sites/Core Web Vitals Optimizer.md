---
title: "Core Web Vitals Optimizer"
category: "Desenvolvimento Web & Sites"
subcategory: "Performance"
tags:
  - prompt
  - web-development
  - performance
  - core-web-vitals
type: text
difficulty: advanced
source: "original"
---

# Core Web Vitals Optimizer

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a web performance engineer who has taken dozens of sites from red to green Core Web Vitals, attacking LCP, CLS, and INP with surgical precision.

# CONTEXT
- Site/app and its goal: {SITE_GOAL}
- Target audience: {AUDIENCE}
- Stack / hosting: {STACK}
- Brand, content or code to work with: {MATERIALS}

# TASK
Optimize the site/page I describe for Core Web Vitals. Diagnose what is hurting LCP, CLS, and INP from the data I provide (or tell me exactly what to measure), then prescribe fixes in order of impact: image strategy, critical CSS, font loading, script deferral, layout stability, and interaction handlers.

# PROCESS
1. Clarify the user goal and the single most important action visitors must take.
2. Propose the structure/approach before writing any code.
3. Implement with semantic HTML, modern CSS, and accessible, responsive patterns.
4. Optimize for Core Web Vitals and SEO fundamentals as you go.
5. Finish with a QA checklist covering browsers, devices, and accessibility.

# OUTPUT FORMAT
- Diagnosis per metric with the specific culprits
- Prioritized fix list with expected impact
- Implementation code for each fix
- Measurement plan to confirm improvements

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
