---
title: "Short Summary"
category: "Biblioteca LLM Avançada"
subcategory: "Extraction Summarization"
tags:
  - prompt
  - community
  - llm-prompt-library
type: text
difficulty: intermediate
source: "llm-prompt-library"
---

# Short Summary

> [!info] Como usar
> Prompt avançado da [LLM-Prompt-Library](https://github.com/abilzerian/LLM-Prompt-Library) (licença MIT). Muitos são system prompts completos — cole como primeira mensagem ou instrução de projeto.

## Prompt

````
# Short Summary

```markdown
`reset`
`no quotes`
`no explanations`
`no prompt`
`no self-reference`
`no apologies`
`no filler`
`just answer`
Create advanced bullet-point notes summarizing the important parts of the reading or topic. Include all essential information, such as vocabulary terms and key concepts, which should be bolded with asterisks. Remove any extraneous language, focusing only on the critical aspects of the passage or topic. Strictly base your notes on the provided text, without adding any external information.

"""
{{text}}
"""
```
````
