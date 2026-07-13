---
title: "Anatomia dos Prompts deste Cofre"
tags:
  - essencial
  - guia
  - essencial
  - anatomia
---
# Anatomia dos Prompts deste Cofre
## Por que os prompts têm esta estrutura

```
# ROLE        → quem a IA é (ativa expertise)
# CONTEXT     → seus dados nos campos {VARIAVEL}
# TASK        → a missão, específica
# PROCESS     → passos numerados (raciocínio guiado)
# OUTPUT FORMAT → entregáveis exatos
# QUALITY BAR → critérios de excelência
+ perguntas de esclarecimento antes de começar
```

Cada seção resolve uma falha comum de IA:

| Seção | Falha que evita |
|---|---|
| ROLE | Respostas rasas de generalista |
| CONTEXT | Suposições erradas sobre sua situação |
| TASK | Desvio do objetivo |
| PROCESS | Pular etapas de raciocínio |
| OUTPUT FORMAT | Resposta em formato inútil |
| QUALITY BAR | Mediocridade "tecnicamente correta" |
| Perguntas | Resposta genérica por falta de dados |

## Adaptando

- **Tarefa simples?** Corte PROCESS e QUALITY BAR — sobra um prompt RTF.
- **Resultado genérico?** Preencha as variáveis com MAIS detalhe, não menos.
- **Quer outro formato?** Reescreva só o OUTPUT FORMAT.
- **Modelo com raciocínio nativo (thinking)?** Pode remover "think step by step" — mas manter não atrapalha.
