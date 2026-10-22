---
title: "Tarih-olay- Görsel oluşturma"
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

# Tarih-olay- Görsel oluşturma

> [!info] Como usar
> Prompt da coleção comunitária [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) (licença CC0). Substitua os trechos entre aspas/colchetes pelo seu conteúdo.

## Prompt

```
{
  "meta": {
    "model": "nano-banana-pro",
    "mode": "thinking",
    "use_search_grounding": true,
    "language": "tr"
  },
  "input": {
    "location": "${Location: Location}",
    "date": "${Date: YYYY-MM-DD}",
    "aspectRatio": "${Aspect Ratio: 16:9 | 4:3 | 1:1 | 9:16}",
    "timeOfDay": "${Time of the Day}",
    "mood": "${Mood: epic | solemn | celebratory | tense | melancholic}"
  },
  "prompt": {
    "positive": "Konum: ${Location: Location}\nTarih: ${Date: YYYY-MM-DD}\n\nÖnce güvenilir kaynaklarla arama yap ve bu tarihte bu konumda gerçekleşen en önemli tarihsel olayı belirle. Sonra bu olayı temsil eden tek bir foto-gerçekçi, ultra detaylı, sinematik kare üret.\n\nDönem doğruluğu zorunlu: mimari, kıyafet, silah/araç ve şehir dokusu tarihle tutarlı olsun. Modern hiçbir obje, bina, araç veya tabela görünmesin. Tek sahne, tek an, gerçek kamera fiziği, doğal insan oranları, yüksek mikro detay.",
    "negative": "modern buildings, cars, asphalt, neon, smartphones, wrong era clothing/armor, fantasy, anime, cartoon, text overlay, blurry, low-res, extra limbs"
  },
  "render": {
    "quality": "ultra",
    "resolution": "4k"
  },
  "name": "My Workflow",
  "steps": []
}
```

— contribuído por `stiva1979@gmail.com`
