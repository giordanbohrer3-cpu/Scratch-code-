---
title: "Action Items"
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

# Action Items

> [!info] Como usar
> Prompt avançado da [LLM-Prompt-Library](https://github.com/abilzerian/LLM-Prompt-Library) (licença MIT). Muitos são system prompts completos — cole como primeira mensagem ou instrução de projeto.

## Prompt

````
# Action Items

```markdown
I will give you text content, you will find action items from it and output them in bullet point format. Identify only the action items that need the reader to take action, and exclude action items requiring action from anyone other than the reader.
Only give me the output and nothing else.
Now, using the concepts above, find action items from the following text. Respond in the same language variety or dialect of the following text:

"""
{{text}}
"""
```
````
