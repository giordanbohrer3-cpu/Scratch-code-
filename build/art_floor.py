# -*- coding: utf-8 -*-
"""art_floor.py - Chão e obstáculos no estilo SUPER MARIO BROS.
- Chão: blocos de terra (tan) com bisel e entalhes + arbusto/morro de cenário.
- Obstáculos: canos verdes e pilhas de tijolos com bloco-? (posições MUDAM por fase).
A colisão é por matemática (retângulos), desenhada exatamente sobre a arte.
"""
from svg_core import *
from phases import LAYOUTS, obstacles

W, H = 480, 360
G = 300                    # topo do chão em SVG (= scratch y -120)


def sx(scx):               # scratch x -> svg x
    return scx + 240


# paleta SMB ---------------------------------------------------------------
GR, GR_D, GR_L, GR_HI, GR_O = "#C76B2A", "#8a3f12", "#E59A52", "#F6C078", "#5e2b0a"
PI, PI_D, PI_L, PI_O = "#34a832", "#1c6b1c", "#8ce08c", "#0c3a0c"
BR, BR_D, BR_L, BR_M = "#C8551C", "#7a2e0e", "#e8884a", "#5a2208"
QB, QB_D, QB_L, QB_O = "#F2A81C", "#9c5a00", "#ffd86a", "#5a3300"


# ---- bloco de chão (estilo Mario) ----
def _gblock(x, y, s):
    return (rect(x, y, s, s, GR)
            + rect(x, y, s, 3, GR_HI, opacity=0.9)
            + rect(x, y, 3, s, GR_L, opacity=0.55)
            + rect(x + s - 3, y, 3, s, GR_D, opacity=0.55)
            + rect(x, y + s - 3, s, 3, GR_D, opacity=0.55)
            + rect(x, y, s, s, "none", stroke=GR_O, sw=1.5)
            + rect(x + 3, y + 4, 3, 3, GR_O)        # entalhe esq
            + rect(x + s - 6, y + 4, 3, 3, GR_O))   # entalhe dir


def _hill(cx):
    return (path(f"M{cx-46} {G} Q{cx-46} {G-34} {cx-18} {G-36} Q{cx} {G-58} {cx+18} {G-36} "
                 f"Q{cx+46} {G-34} {cx+46} {G} Z", fill="#3a9d3a")
            + path(f"M{cx-46} {G} Q{cx-46} {G-34} {cx-18} {G-36} Q{cx} {G-58} {cx+18} {G-36} "
                   f"Q{cx+46} {G-34} {cx+46} {G} Z", fill="none", stroke="#2c7a2c", sw=2)
            + ellipse(cx - 10, G - 22, 3, 5, "#2c7a2c") + ellipse(cx + 10, G - 22, 3, 5, "#2c7a2c"))


def _bush(cx):
    y = G - 12
    return (circle(cx - 14, y, 12, "#54c054") + circle(cx + 14, y, 12, "#54c054")
            + circle(cx, y - 5, 15, "#54c054")
            + circle(cx, y - 5, 15, "none", stroke="#2c7a2c", sw=1.5)
            + circle(cx - 14, y, 12, "none", stroke="#2c7a2c", sw=1.5)
            + circle(cx + 14, y, 12, "none", stroke="#2c7a2c", sw=1.5))


DECOR = {1: (_hill, sx(-185), _bush, sx(150)), 2: (_bush, sx(-180), _hill, sx(155)),
         3: (_hill, sx(-185), _bush, sx(152)), 4: (_bush, sx(-185), _hill, sx(150)),
         5: (_hill, sx(-185), _bush, sx(156))}


def ground_costume(num):
    b = []
    # cenário (atrás do piso)
    d = DECOR[num]
    b.append(d[0](d[1])); b.append(d[2](d[3]))
    # faixa de blocos de terra (2 linhas)
    for y in (G, G + 30):
        for x in range(0, W, 30):
            b.append(_gblock(x, y, 30))
    b.append(rect(0, G - 2, W, 3, GR_HI, opacity=0.8))   # brilho da superfície
    return svg_doc(W, H, "".join(b))


# ---- cano verde ----
def _pipe(cxs, w, h):
    y0 = G - h
    x = cxs - w / 2
    s = [rect(x, y0 + 13, w, h - 13, PI),
         rect(x + 3, y0 + 13, 5, h - 13, PI_L, opacity=0.85),
         rect(x + w - 7, y0 + 13, 5, h - 13, PI_D, opacity=0.7),
         rect(x, y0 + 13, w, h - 13, "none", stroke=PI_O, sw=2),
         rect(x - 5, y0, w + 10, 14, PI, rx=3),
         rect(x - 5, y0, w + 10, 5, PI_L, rx=3, opacity=0.85),
         rect(x - 5, y0 + 9, w + 10, 4, PI_D, opacity=0.55),
         rect(x - 5, y0, w + 10, 14, "none", rx=3, stroke=PI_O, sw=2)]
    return "".join(s)


# ---- tijolo ----
def _brick(x, y, w, h):
    return (rect(x, y, w, h, BR) + rect(x, y, w, 2, BR_L, opacity=0.7)
            + line(x, y + h / 2, x + w, y + h / 2, BR_M, 1.5)
            + line(x + w / 2, y, x + w / 2, y + h / 2, BR_M, 1.2)
            + line(x + w / 4, y + h / 2, x + w / 4, y + h, BR_M, 1.2)
            + line(x + 3 * w / 4, y + h / 2, x + 3 * w / 4, y + h, BR_M, 1.2)
            + rect(x, y, w, h, "none", stroke=BR_D, sw=1.5))


# ---- bloco "?" ----
def _qblock(x, y, w, h):
    return (rect(x, y, w, h, QB, rx=2) + rect(x, y, w, 3, QB_L, rx=2, opacity=0.85)
            + rect(x + 2, y + h - 3, w - 4, 2, QB_D, opacity=0.7)
            + rect(x + 3, y + 3, 2, 2, QB_O) + rect(x + w - 5, y + 3, 2, 2, QB_O)
            + rect(x + 3, y + h - 5, 2, 2, QB_O) + rect(x + w - 5, y + h - 5, 2, 2, QB_O)
            + rect(x, y, w, h, "none", rx=2, stroke=QB_O, sw=2)
            + text(x + w / 2, y + h * 0.72, h * 0.6, "?", QB_O, "900", "middle"))


def _blocks(cxs, w, h):
    n = max(1, round(h / 18.0))
    bh = h / n
    x = cxs - w / 2
    s = []
    for i in range(n):
        yb = G - (i + 1) * bh
        s.append(_qblock(x, yb, w, bh) if i == n - 1 else _brick(x, yb, w, bh))
    return "".join(s)


def obstacle_costume(num):
    b = []
    for o in obstacles(num):
        cxs = sx(o["cx"])
        b.append(_pipe(cxs, o["w"], o["h"]) if o["kind"] == "pipe"
                 else _blocks(cxs, o["w"], o["h"]))
    return svg_doc(W, H, "".join(b))


def ground_all():     return [(f"Chao {n}", ground_costume(n)) for n in range(1, 6)]
def obstacle_all():   return [(f"Obst {n}", obstacle_costume(n)) for n in range(1, 6)]


if __name__ == "__main__":
    import cairosvg
    import os
    os.makedirs("/home/user/Scratch-code-/preview/floor", exist_ok=True)
    for name, svg in ground_all() + obstacle_all():
        cairosvg.svg2png(bytestring=svg.encode(),
                         write_to=f"/home/user/Scratch-code-/preview/floor/{name}.png",
                         output_width=W, output_height=H)
    print("mario floor ok")
