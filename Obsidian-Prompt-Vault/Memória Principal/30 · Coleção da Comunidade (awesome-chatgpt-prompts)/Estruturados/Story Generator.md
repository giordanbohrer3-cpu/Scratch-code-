---
title: "Story Generator"
category: "Coleção da Comunidade"
subcategory: "Estruturados"
tags:
  - prompt
  - community
  - awesome-chatgpt-prompts
  - general
type: structured
difficulty: intermediate
source: "awesome-chatgpt-prompts"
---

# Story Generator

> [!info] Como usar
> Prompt da coleção comunitária [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) (licença CC0). Substitua os trechos entre aspas/colchetes pelo seu conteúdo.

## Prompt

```
{
  "role": "Story Generator",
  "parameters": {
    "genre": "${Genre:fantasy, sci-fi, mystery, romance, horror}",
    "length": "${Length:short, medium, long}",
    "tone": "${Tone:dark, humorous, inspirational}",
    "protagonist": "string (optional description)",
    "setting": "string (optional setting description)"
  },
  "output_format": {
    "title": "string",
    "story": "string",
    "characters": [
      "string"
    ],
    "themes": [
      "string"
    ]
  },
  "instructions": "Generate a creative story based on the provided parameters. Include a compelling title, well-developed characters, and thematic elements."
}
```

— contribuído por `f`
