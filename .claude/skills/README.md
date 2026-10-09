# Skills do projeto

Origem: [rtadewald/skills](https://github.com/rtadewald/skills) @ `99d0b39` (o repo de origem não tem arquivo de licença).

| Skill | Uso | Observação |
|---|---|---|
| `img-to-html` | `/img-to-html` + imagem do mock | Pipeline em 5 etapas com aprovação |
| `to-wireframe` | `/to-wireframe format=ascii image=...` | Dependência obrigatória da etapa 1 |
| `openrouter-img` | `/openrouter-img` | Gera assets; exige `uv` e `OPENROUTER_API_KEY` no `.env` |

Ajustes locais em relação à origem:

- Caminho do script: `~/.agents/skills/openrouter-img/...` → `.claude/skills/openrouter-img/...` (rodar da raiz do repo).
- `img-to-html` lê o `SKILL.md` da `to-wireframe` em vez de invocá-la, porque ela tem `disable-model-invocation`.
- `agents/openai.yaml` (formato do Codex) não foi copiado.
