---
title: "3D to 2D Floor Plan Converter"
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

# 3D to 2D Floor Plan Converter

> [!info] Como usar
> Prompt da coleção comunitária [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) (licença CC0). Substitua os trechos entre aspas/colchetes pelo seu conteúdo.

## Prompt

```
{
  "task": "image_to_image",
  "description": "Convert a furnished 3D interior render into a clean 2D architectural floor plan drawing",
  "input_image": "3d_render_of_apartment_interior.png",
  "prompt": "top-down 2D architectural floor plan, black and white technical drawing, clean vector-style lines, precise wall thickness, clearly defined rooms, labeled spaces with room names and square meter areas, doors with swing arcs, windows shown as breaks in walls, minimal shading, no perspective, orthographic projection, architectural blueprint style, professional residential floor plan, similar to CAD drawing",
  "negative_prompt": "3d perspective, isometric view, realistic lighting, shadows, textures, furniture rendering, people, depth, photorealism, colors, gradients, soft edges, artistic sketch, hand drawn style",
  "settings": {
    "model": "sdxl",
    "sampler": "DPM++ 2M Karras",
    "steps": 30,
    "cfg_scale": 7,
    "denoising_strength": 0.65,
    "resolution": {
      "width": 1024,
      "height": 1024
    }
  },
  "output_expectation": "flat 2D floor plan similar to architectural plan drawings, suitable for real estate listings or construction documents"
}
```

— contribuído por `senoldak`
