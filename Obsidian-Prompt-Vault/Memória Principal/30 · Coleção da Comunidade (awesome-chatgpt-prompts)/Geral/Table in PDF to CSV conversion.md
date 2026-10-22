---
title: "Table in PDF to CSV conversion"
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

# Table in PDF to CSV conversion

> [!info] Como usar
> Prompt da coleção comunitária [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) (licença CC0). Substitua os trechos entre aspas/colchetes pelo seu conteúdo.

## Prompt

```
"Attached is an image of a table listing the model parameters for the ${insert_model_name} model (from [Insert Author/Paper Name]).
Please extract the data and convert it into a CSV code block that I can copy and save directly.
Requirements:
Use the first row as the header.
If cells are merged, repeat the value for each row to ensure the CSV is flat and processable.
Do not include units in the numeric columns (e.g., remove 'ms' or '%'), or keep them consistent in a separate column.
If any text is unclear due to image quality, mark it as '${unclear}' rather than guessing.
Ensure all fields containing commas are properly quoted."
```

— contribuído por `Bornduck`
