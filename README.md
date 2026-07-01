# 🎨 A Dupla das Artes

Um jogo de plataforma educativo feito em **Scratch (.sb3)**, no estilo
**Fogo & Água / Super Mario**, que leva **Theo** e **Lia** numa viagem pela
**história da arte** — em ordem cronológica.

> **Jogue agora:** baixe `Dupla_das_Artes.sb3` e abra em
> [scratch.mit.edu](https://scratch.mit.edu) (Criar → Arquivo → Carregar do seu
> computador) ou em [turbowarp.org](https://turbowarp.org). Funciona online e offline.

---

## 🕹️ Como jogar

Cada personagem tem **controles próprios** (estilo Fogo & Água):

| Personagem | Mover | Pular |
|------------|-------|-------|
| **Theo** | **A** / **D** | **W** |
| **Lia** | **←** / **→** | **↑** |
| **Os dois juntos** | — | **ESPAÇO** (pulam ao mesmo tempo!) |

Clique no botão verde **COMEÇAR**. Em cada fase:

1. Assista à **tela animada de 7 segundos** que apresenta a era, o **objetivo** e
   uma **curiosidade** sobre a arte.
2. **Ande e pule** pelo chão marrom, **saltando por cima dos obstáculos**.
3. **Colete as 4 relíquias** da era (algumas ficam no topo dos obstáculos!).
4. Leve **Theo e Lia até os portais** no fim da fase.

Complete as 5 fases para abrir o **Museu Completo!** 🏛️

## 🖼️ As 5 eras (ordem cronológica)

| # | Fase | Destaque |
|---|------|----------|
| 1 | **Arte Antiga** | Egito, Grécia e Roma — pirâmides, templo, máscara de ouro |
| 2 | **Arte Medieval** | Catedrais e vitrais — rosácea, cálice, pergaminho |
| 3 | **Cubismo** | Picasso e Braque — violão e rosto facetados, cubo |
| 4 | **Arte Moderna** | Sonhos e cores — relógio derretido, girassol, Mondrian |
| 5 | **Arte Contemporânea** | Pop Art e grafite — balão POP, lata, spray neon |

## ✨ O que tem no jogo

- **Plataforma de verdade:** gravidade, pulo e colisão (chão + obstáculos).
- **Os dois personagens pulam juntos** com a tecla Espaço.
- **Cenários imersivos** e caprichados, um para cada era.
- **Personagens, portas e coletáveis** desenhados com carinho.
- **Animações** ao coletar relíquias, ao entrar nas portas e ao passar de fase.
- **Tela animada de 7s** antes de cada fase (objetivo + curiosidade).
- **Placar** de pontos e relíquias.

---

## 🛠️ Como o jogo é gerado (para quem quiser editar)

O `.sb3` é **gerado por código Python** (arte em SVG + blocos do Scratch),
o que mantém tudo organizado e sem erros. A pasta `build/` contém:

| Arquivo | Função |
|---------|--------|
| `svg_core.py` | mini-biblioteca de desenho SVG |
| `phases.py` | configuração das 5 fases + layout do platformer |
| `art_backdrops.py` | os 5 fundos imersivos |
| `art_intro.py` | telas de intro, título e vitória |
| `art_chars.py` | Theo e Lia (parado / andar / pular) |
| `art_floor.py` | chão marrom e obstáculos por fase |
| `art_items.py` | as 20 relíquias coletáveis |
| `art_doors.py` | os portais de Theo e Lia |
| `art_ui.py` | botão, selos, contagem, banner, confete |
| `sb3lib.py` | compilador de blocos → `project.json` → `.sb3` |
| `build_project.py` | monta o jogo completo |

Para regenerar o `.sb3`:

```bash
cd build
python3 build_project.py      # gera ../Dupla_das_Artes.sb3
```

A colisão usa **matemática de coordenadas** (retângulos) em vez de "tocando em
cor/sprite", o que torna o jogo **robusto e idêntico** no editor, no site e
offline.

Feito com 💛 para ensinar arte brincando.
