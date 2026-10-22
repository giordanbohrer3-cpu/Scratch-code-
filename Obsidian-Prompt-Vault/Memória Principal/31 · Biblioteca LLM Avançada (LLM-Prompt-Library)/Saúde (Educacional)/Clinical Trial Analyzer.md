---
title: "Clinical Trial Analyzer"
category: "Biblioteca LLM Avançada"
subcategory: "Saúde (Educacional)"
tags:
  - prompt
  - community
  - llm-prompt-library
type: text
difficulty: intermediate
source: "llm-prompt-library"
---

# Clinical Trial Analyzer

> [!info] Como usar
> Prompt avançado da [LLM-Prompt-Library](https://github.com/abilzerian/LLM-Prompt-Library) (licença MIT). Muitos são system prompts completos — cole como primeira mensagem ou instrução de projeto.

## Prompt

````
# Clinical Trial Analyzer

```markdown
`no apologies`
`no self-reference`

Analyze clinical trial data.

1. Review the trial report between triple quotes, noting study design, sample size and inclusion criteria.
2. Summarize primary and secondary outcomes with relevant statistics (e.g., risk ratios, p-values) when provided.
3. Highlight strengths such as randomization or blinding, and limitations like small cohorts or high attrition.
4. Point out potential sources of bias but do not offer treatment advice.

"""
{{trial}}
"""

### Example

Trial: randomized placebo-controlled study on new antihypertensive drug.

- Double-blind design with 200 participants
- Primary endpoint: reduction in systolic blood pressure
- Result: significant 10 mmHg drop versus placebo
- Limitation: follow-up only 8 weeks
```
````
