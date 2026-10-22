---
title: "Angular Directive Generator"
category: "Coleção da Comunidade"
subcategory: "Geral"
tags:
  - prompt
  - community
  - awesome-chatgpt-prompts
  - general
type: text
difficulty: intermediate
source: "awesome-chatgpt-prompts"
---

# Angular Directive Generator

> [!info] Como usar
> Prompt da coleção comunitária [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) (licença CC0). Substitua os trechos entre aspas/colchetes pelo seu conteúdo.

## Prompt

```
You are an expert Angular developer. Generate a complete Angular directive based on the following description:

Directive Description: ${description}
Directive Type: [structural | attribute]
Selector Name: [e.g. appHighlight, *appIf]
Inputs needed: [list any @Input() properties]
Target element behavior: ${what_should_happen_to_the_host_element}

Generate:
1. The full directive TypeScript class with proper decorators
2. Any required imports
3. Host bindings or listeners if needed
4. A usage example in a template
5. A brief explanation of how it works

Use Angular 17+ standalone directive syntax. Follow Angular style guide conventions.
```

— contribuído por `satishbirhade16@gmail.com`
