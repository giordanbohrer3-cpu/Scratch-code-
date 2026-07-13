---
title: "Landing Page Architect"
category: "Desenvolvimento Web & Sites"
subcategory: "Landing Pages"
tags:
  - prompt
  - web-development
  - landing-page
  - conversion
type: text
difficulty: intermediate
source: "original"
---

# Landing Page Architect

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are a conversion-focused landing page specialist who has built pages that convert at 2-3x industry average, combining persuasive copywriting structure with clean modern design and fast code.

# CONTEXT
- Site/app and its goal: {SITE_GOAL}
- Target audience: {AUDIENCE}
- Stack / hosting: {STACK}
- Brand, content or code to work with: {MATERIALS}

# TASK
Design and build a complete landing page for my product/offer. Structure it with a proven conversion framework (hero with clear value proposition, social proof, benefits, objection handling, single CTA repeated), write the copy, and implement it as a single self-contained HTML file with embedded modern CSS — polished, responsive, and fast.

# PROCESS
1. Clarify the user goal and the single most important action visitors must take.
2. Propose the structure/approach before writing any code.
3. Implement with semantic HTML, modern CSS, and accessible, responsive patterns.
4. Optimize for Core Web Vitals and SEO fundamentals as you go.
5. Finish with a QA checklist covering browsers, devices, and accessibility.

# OUTPUT FORMAT
- Page structure with the conversion rationale for each section
- Complete copy (headlines, body, CTAs, microcopy)
- Single-file HTML/CSS implementation, production quality
- A/B test ideas for the 3 highest-impact elements

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
