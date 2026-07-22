---
title: "Engenharia de Prompts 101"
tags:
  - essencial
  - guia
  - essencial
  - prompt-engineering
---
# Engenharia de Prompts 101
## Os 7 elementos de um prompt profissional

1. **Papel (Role)** — diga quem a IA deve ser: `You are a senior backend engineer...`. Ativa o vocabulário e os padrões daquele domínio.
2. **Contexto** — dados, restrições, público, situação. A IA não adivinha o que você não disser.
3. **Tarefa** — o verbo principal, claro e único. "Analise", "Escreva", "Projete".
4. **Processo** — os passos que ela deve seguir. Passos numerados reduzem atalhos preguiçosos.
5. **Formato de saída** — estrutura exata do que você quer receber (tabela, lista, código, JSON).
6. **Critérios de qualidade** — o que separa uma resposta boa de uma medíocre.
7. **Protocolo de perguntas** — `Ask me up to 3 clarifying questions before starting`. Evita respostas genéricas.

## Técnicas que mais melhoram resultados

| Técnica | Quando usar | Como |
|---|---|---|
| Few-shot (exemplos) | Formato/estilo específico | Mostre 1-3 exemplos de entrada→saída |
| Chain-of-thought | Problemas de raciocínio | "Think step by step before answering" |
| Decomposição | Tarefas grandes | Peça o plano primeiro, depois execute por partes |
| Auto-crítica | Qualidade máxima | "Now review your answer as a hostile expert and fix the flaws" |
| Saída estruturada | Dados para processar | Defina o schema JSON exato |
| Persona negativa | Evitar vícios | "Do not use clichés like 'in today's fast-paced world'" |

## Erros comuns

- **Prompt vago** → resposta genérica. Especifique público, tom, tamanho, formato.
- **Tudo em uma mensagem** → divida tarefas grandes em etapas conversacionais.
- **Aceitar a primeira resposta** → itere: "torne mais específico", "corte 30%", "mais exemplos".
- **Não dar exemplos** → estilo é mais fácil de mostrar do que descrever.
- **Ignorar o contexto da conversa** → modelos usam o histórico; limpe a conversa quando mudar de assunto.
