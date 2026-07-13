---
title: "Rewrite"
category: "Biblioteca LLM Avançada"
subcategory: "Editing Revision"
tags:
  - prompt
  - community
  - llm-prompt-library
type: text
difficulty: intermediate
source: "llm-prompt-library"
---

# Rewrite

> [!info] Como usar
> Prompt avançado da [LLM-Prompt-Library](https://github.com/abilzerian/LLM-Prompt-Library) (licença MIT). Muitos são system prompts completos — cole como primeira mensagem ou instrução de projeto.

## Prompt

````
# Rewrite

```markdown
I will give you text content, you will rewrite it and output a better version of my text.
Keep the meaning the same. Make sure the re-written content's number of characters is the same as the original text's number of characters. Do not alter the original structure and formatting outlined in any way. Only give me the output and nothing else.
Now, using the concepts above, re-write the following text. Respond in the same language variety or dialect of the following text:

"""
{{text}}
"""
```
````
