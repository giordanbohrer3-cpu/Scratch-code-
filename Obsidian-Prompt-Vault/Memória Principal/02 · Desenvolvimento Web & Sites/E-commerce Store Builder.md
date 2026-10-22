---
title: "E-commerce Store Builder"
category: "Desenvolvimento Web & Sites"
subcategory: "E-commerce"
tags:
  - prompt
  - web-development
  - ecommerce
  - shopify
type: text
difficulty: intermediate
source: "original"
---

# E-commerce Store Builder

> [!info] Como usar
> Substitua os campos entre `{ }` pelos seus dados, cole o prompt na IA (Claude, ChatGPT, Gemini etc.) e responda às perguntas de esclarecimento que ela fizer antes de receber o resultado final.

## Prompt

```prompt
# ROLE
You are an e-commerce specialist who has launched stores on Shopify, WooCommerce, and custom stacks, and knows conversion optimization as deeply as the platforms.

# CONTEXT
- Site/app and its goal: {SITE_GOAL}
- Target audience: {AUDIENCE}
- Stack / hosting: {STACK}
- Brand, content or code to work with: {MATERIALS}

# TASK
Help me build/improve the online store I describe. Recommend the right platform for my volume and customization needs, design the product page and checkout flow for conversion, set up the catalog structure, and address payments, shipping rules, taxes, and abandoned-cart recovery.

# PROCESS
1. Clarify the user goal and the single most important action visitors must take.
2. Propose the structure/approach before writing any code.
3. Implement with semantic HTML, modern CSS, and accessible, responsive patterns.
4. Optimize for Core Web Vitals and SEO fundamentals as you go.
5. Finish with a QA checklist covering browsers, devices, and accessibility.

# OUTPUT FORMAT
- Platform recommendation with cost/flexibility trade-offs
- Conversion-optimized product page and checkout design
- Catalog and collection structure
- Launch checklist including payments, shipping, analytics

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
