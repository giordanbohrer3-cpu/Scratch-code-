---
title: "Claude Code Skill (Slash Command): review-and-commit.md"
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

# Claude Code Skill (Slash Command): review-and-commit.md

> [!info] Como usar
> Prompt da coleção comunitária [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) (licença CC0). Substitua os trechos entre aspas/colchetes pelo seu conteúdo.

## Prompt

```
---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
description: Create a git commit
---

## Context

- Current git status: !`git status`
- Current git diff (staged and unstaged changes): !`git diff HEAD`
- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -10`

## Your task

Review the existing changes and then create a git commit following the conventional commit format. If you think there are more than one distinct change you can create multiple commits.
```

— contribuído por `DoguD`
