---
title: "Frameworks de Prompt (RTF, CRISPE, RISEN e outros)"
tags:
  - essencial
  - guia
  - essencial
  - frameworks
---
# Frameworks de Prompt (RTF, CRISPE, RISEN e outros)
## Frameworks rápidos para montar prompts

### RTF — Role, Task, Format
O mínimo viável. `As a [role], do [task]. Output as [format].`
Use para tarefas simples e rápidas.

### CRISPE — Capacity, Insight, Statement, Personality, Experiment
- **C**apacity: papel/capacidade da IA
- **R**insight: contexto e bastidores
- **I**Statement: a tarefa central
- **S**Personality: tom e estilo da resposta
- **P**Experiment: peça variações para comparar

### RISEN — Role, Instructions, Steps, End goal, Narrowing
Adiciona **passos explícitos** e **restrições** — ótimo para tarefas técnicas.

### APE — Action, Purpose, Expectation
`Do [action]. The purpose is [why]. I expect [outcome].`
O "porquê" ajuda a IA a tomar decisões alinhadas quando o prompt não cobre tudo.

### Chain-of-Density (resumos)
Peça um resumo, depois: "Rewrite denser: same length, add 2 missing key entities." Repita 3x. Resumos progressivamente melhores.

### O padrão deste cofre
Os prompts deste cofre usam a estrutura **ROLE → CONTEXT → TASK → PROCESS → OUTPUT FORMAT → QUALITY BAR → perguntas de esclarecimento** — uma síntese de RISEN + CRISPE otimizada para resultados profissionais em uma passada.
