# 🐍 Cobrinha PRO

Versão turbinada do **Jogo da Cobrinha** feito no Scratch, exportada em `.sb3`
pronta para baixar e jogar (arraste o arquivo para [scratch.mit.edu](https://scratch.mit.edu/projects/editor/)
ou para o [TurboWarp](https://turbowarp.org)).

➡️ **Arquivo do jogo:** [`Cobrinha PRO.sb3`](./Cobrinha%20PRO.sb3)

## ✨ O que há de novo

| Recurso | Descrição |
|---|---|
| 🎬 **Tela inicial caprichada** | Menu com título, cobra decorativa, instruções e botão pulsante "Pressione Espaço". |
| 💀 **Morre ao bater em si mesma** | Colisão com o próprio corpo usando a técnica de cor (corpo rosa-choque detectado pela cabeça, com período de carência nos segmentos novos para evitar falso-positivo). |
| ⚡ **Velocidade por nível** | A variável `velocidade` agora é usada de verdade: sobe de 5 → 9 conforme o nível (5/10/15/20 pontos). |
| 🔄 **Wrap-around** | Atravessa uma borda e reaparece do outro lado (em vez de game over na borda). |
| 🎨 **Cenários e atores Pró** | Fundos HD originais mantidos + nova cobra "neon" vetorial (cabeça laranja com olhos/língua, corpo em degradê âmbar → rosa) e maçã. |
| 🏆 **Recorde** | Guarda a maior pontuação da sessão, exibida no menu e no game over. |

## 🎮 Como jogar
- **Setas** para guiar a cobra (não dá para inverter 180° direto).
- Coma as **maçãs** para crescer e subir de nível.
- Não bata no próprio corpo.
- **Espaço / clique** para começar e para voltar ao menu.

## 🛠️ Como foi feito
Os scripts e os assets vetoriais (SVG) são gerados por código em [`src/build.py`](./src/build.py)
(usa [`src/assets.py`](./src/assets.py)), que reescreve o `project.json` do `.sb3` original.
O resultado foi validado com o `scratch-parser` oficial e carregado/executado no `scratch-vm`.

### Pré-visualização
![Menu](./assets_preview/menu.png)
![Cobra](./assets_preview/snake.png)
