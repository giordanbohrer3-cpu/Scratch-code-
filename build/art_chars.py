# -*- coding: utf-8 -*-
"""art_chars.py - Theo e Lia, a dupla das artes. Personagens caprichados,
voltados para a direita (usam rotationStyle left-right no jogo).

Canvas 48 x 60, centro de rotação (24, 30). Pés por volta de y=57.
Poses: 'idle', 'andar', 'pular'.
"""
from svg_core import *

CANVAS_W, CANVAS_H = 48, 60
ROT = (24, 30)


def _legs(pose, pants, shoe):
    s = []
    if pose == "idle":
        s.append(path("M20 44 L19 55", stroke=pants, sw=7))
        s.append(path("M28 44 L29 55", stroke=pants, sw=7))
        s.append(path("M15 56 q4 -3 9 0", stroke=shoe, sw=6))   # sapato esq
        s.append(path("M25 56 q4 -3 9 0", stroke=shoe, sw=6))   # sapato dir
    elif pose == "andar":
        s.append(path("M21 44 L14 54", stroke=pants, sw=7))     # perna atrás
        s.append(path("M27 44 L33 54", stroke=pants, sw=7))     # perna à frente
        s.append(path("M11 55 q3 -3 8 -1", stroke=shoe, sw=6))
        s.append(path("M30 54 q5 -2 8 1", stroke=shoe, sw=6))
    else:  # pular - joelhos dobrados
        s.append(path("M21 44 q-6 4 -3 10", stroke=pants, sw=7))
        s.append(path("M28 44 q6 4 3 10", stroke=pants, sw=7))
        s.append(path("M15 53 q4 -2 7 1", stroke=shoe, sw=6))
        s.append(path("M27 54 q4 -2 7 -1", stroke=shoe, sw=6))
    return "".join(s)


def _kid(skin, hair, hat, hat2, shirt, shirt2, pants, shoe, beret=True,
         ponytail=False, accessory="brush", pose="idle"):
    b = []
    gid = f"sh_{abs(hash((shirt,pose)))%9999}"
    defs = lingrad(gid, [(0, shirt2, 1), (1, shirt, 1)])
    # ---- pernas (atrás do corpo) ----
    b.append(_legs(pose, pants, shoe))
    # ---- braço de trás ----
    if pose == "pular":
        b.append(path("M18 30 q-9 -6 -11 -14", stroke=skin, sw=6))   # braço p/ cima
    elif pose == "andar":
        b.append(path("M18 31 q-8 5 -9 13", stroke=skin, sw=6))
    else:
        b.append(path("M18 31 q-8 3 -8 12", stroke=skin, sw=6))
    # ---- ponytail atrás (Lia) ----
    if ponytail:
        b.append(path("M33 12 q14 4 10 22 q-2 8 -8 9", fill=hair, opacity=1))
        b.append(circle(34, 11, 3, hat2))
    # ---- torso / jaleco de artista ----
    b.append(path(f"M16 28 q8 -5 16 0 l2 16 q-10 5 -20 0 Z", fill=f"url(#{gid})"))
    b.append(path("M24 27 L24 44", stroke=shirt2, sw=1.4, opacity=0.5))   # fecho
    b.append(circle(24, 33, 1.4, shirt2)); b.append(circle(24, 38, 1.4, shirt2))
    # mancha de tinta no jaleco
    b.append(circle(19, 36, 2.4, shirt2, 0.9))
    # ---- cabeça ----
    b.append(circle(24, 16, 11, skin))
    # orelha
    b.append(circle(15, 17, 2.2, skin))
    # cabelo base
    if ponytail:
        b.append(path("M13 16 q1 -14 12 -14 q12 0 11 14 q-4 -6 -11 -6 q-8 0 -12 6", fill=hair))
    else:
        b.append(path("M13 15 q1 -13 11 -13 q11 0 11 13 q-3 -7 -11 -7 q-8 0 -11 7", fill=hair))
    # rosto
    b.append(circle(22, 16, 1.7, "#26201c"))
    b.append(circle(28, 16, 1.7, "#26201c"))
    b.append(circle(22.6, 15.4, 0.6, "#fff"))
    b.append(circle(28.6, 15.4, 0.6, "#fff"))
    b.append(path("M21 22 q3.5 3 7 0", stroke="#a0522d", sw=1.6))      # sorriso
    b.append(circle(18, 20, 2.2, "#ff9a8d", 0.5))                       # bochecha
    b.append(circle(30, 20, 2.2, "#ff9a8d", 0.5))
    # ---- boina de artista ----
    if beret:
        b.append(ellipse(24, 6, 13, 6, hat))
        b.append(path("M12 7 q12 -8 24 0 q-2 -5 -12 -5 q-10 0 -12 5", fill=hat2, opacity=0.9))
        b.append(circle(24, 1, 2.2, hat2))                              # nó da boina
    else:  # capuz/lenço
        b.append(path("M12 9 q12 -12 24 0 q-3 -7 -12 -7 q-9 0 -12 7", fill=hat))
        b.append(path("M12 9 q12 -7 24 0", stroke=hat2, sw=2, opacity=0.8))
    # ---- braço da frente + acessório ----
    if accessory == "brush":
        # segura um pincel
        b.append(path("M30 31 q9 2 13 -3", stroke=skin, sw=6))
        b.append(line(41, 30, 47, 22, "#8a5a2e", 2.4))
        b.append(circle(47, 21, 2.4, shirt2))                           # tinta na ponta
    elif accessory == "palette":
        # segura uma paleta
        b.append(path("M30 32 q8 4 12 1", stroke=skin, sw=6))
        b.append(ellipse(45, 31, 6, 4.5, "#caa06a"))
        b.append(circle(43, 30, 1.3, "#c0234f")); b.append(circle(47, 30, 1.3, "#1fb6c9"))
        b.append(circle(45, 33, 1.3, "#ffd23f"))
    else:
        b.append(path("M30 31 q9 4 10 12", stroke=skin, sw=6))
    return svg_doc(CANVAS_W, CANVAS_H, "".join(b), defs)


# ---- Theo: menino, boina azul, jaleco laranja, segura pincel ----
def theo_costumes():
    common = dict(skin="#f1c69b", hair="#3a2a1c", hat="#1d4ed8", hat2="#2563eb",
                  shirt="#f97316", shirt2="#fdba74", pants="#1e3a8a", shoe="#7c2d12",
                  beret=True, ponytail=False, accessory="brush")
    return [
        ("Theo parado", _kid(pose="idle", **common)),
        ("Theo andar", _kid(pose="andar", **common)),
        ("Theo pular", _kid(pose="pular", **common)),
    ]


# ---- Lia: menina, boina magenta, jaleco turquesa, rabo de cavalo, paleta ----
def lia_costumes():
    common = dict(skin="#f6cdb0", hair="#5b3a1e", hat="#db2777", hat2="#f472b6",
                  shirt="#0d9488", shirt2="#5eead4", pants="#0f766e", shoe="#134e4a",
                  beret=True, ponytail=True, accessory="palette")
    return [
        ("Lia parada", _kid(pose="idle", **common)),
        ("Lia andar", _kid(pose="andar", **common)),
        ("Lia pular", _kid(pose="pular", **common)),
    ]


if __name__ == "__main__":
    import cairosvg, os
    os.makedirs("../preview/chars", exist_ok=True)
    for name, svg in theo_costumes() + lia_costumes():
        cairosvg.svg2png(bytestring=svg.encode(), write_to=f"../preview/chars/{name}.png",
                         output_width=CANVAS_W*4, output_height=CANVAS_H*4)
    print("chars ok")
