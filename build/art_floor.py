# -*- coding: utf-8 -*-
"""art_floor.py - Chão (piso marrom) e Obstáculos por fase.

Ambos são sprites do tamanho do palco (480x360), posicionados em (0,0).
A colisão do platformer usa 'tocando em Chão?' e 'tocando em Obstáculo?',
então a arte = a forma de colisão (pixel a pixel).
"""
from svg_core import *
from phases import PHASES, GROUND_Y

W, H = 480, 360
GROUND_TOP_SVG = 300          # = scratch y -120 (superfície)


def _sx(scx):  # scratch x -> svg x
    return scx + 240


# --------------------------------------------------------------------------
# CHÃO (piso) por fase - faixa marrom texturizada na base do palco
# --------------------------------------------------------------------------
def ground_costume(p):
    top, bot, edge = p["ground_top"], p["ground_bot"], p["ground_edge"]
    key = p["key"]
    gid = f"gr_{p['num']}"
    defs = lingrad(gid, [(0, top, 1), (1, bot, 1)])
    b = [rect(0, GROUND_TOP_SVG, W, H - GROUND_TOP_SVG, f"url(#{gid})")]
    # brilho da borda superior (acento da era)
    b.append(rect(0, GROUND_TOP_SVG, W, 4, edge, opacity=0.95))
    b.append(rect(0, GROUND_TOP_SVG + 4, W, 2, "#000", opacity=0.12))

    if key == "antiga":   # blocos de arenito
        for row, yy in enumerate([312, 336]):
            off = 0 if row % 2 == 0 else 30
            for x in range(-off, W, 60):
                b.append(rect(x + 3, yy, 54, 22, "none", stroke="#5a3a18", sw=1.5))
                b.append(rect(x + 3, yy, 54, 5, "#e7c98c", opacity=0.18))
        # hieróglifos sutis
        for x in range(40, W, 120):
            b.append(circle(x, 326, 2, "#3a2410", 0.5))
            b.append(rect(x + 8, 322, 3, 8, "#3a2410", opacity=0.4))
    elif key == "medieval":   # pedra de catedral
        for row, yy in enumerate([310, 332]):
            off = 0 if row % 2 == 0 else 26
            for x in range(-off, W, 52):
                b.append(rect(x + 2, yy, 48, 24, "none", stroke="#23253a", sw=1.6))
                b.append(rect(x + 2, yy, 48, 6, "#9aa0c4", opacity=0.16))
        for x in range(30, W, 100):
            b.append(path(f"M{x} 348 L{x} 340 Q{x} 334 {x+6} 334 Q{x+12} 334 {x+12} 340 L{x+12} 348 Z",
                          fill="#23253a", opacity=0.3))
    elif key == "cubismo":   # planos facetados terrosos
        pal = p["palette"]
        facets = [[(0,300),(120,300),(80,360),(0,360)],
                  [(120,300),(250,300),(230,360),(80,360)],
                  [(250,300),(370,300),(360,360),(230,360)],
                  [(370,300),(480,300),(480,360),(360,360)]]
        for i, f in enumerate(facets):
            b.append(poly(f, pal[i % len(pal)], 0.9))
            b.append(poly(f, "none", stroke="#3a2f20", sw=1.6))
        b.append(rect(0, GROUND_TOP_SVG, W, 4, edge, opacity=0.95))
    elif key == "moderna":   # piso com dabs de cor
        for row, yy in enumerate([314, 338]):
            off = 0 if row % 2 == 0 else 28
            for x in range(-off, W, 56):
                b.append(rect(x + 2, yy, 52, 22, "none", stroke="#2a153a", sw=1.4))
        import random
        rnd = random.Random(4)
        for c in ["#ffd23f", "#1fb6c9", "#ff6f59", "#f4f1ea"]:
            for _ in range(7):
                b.append(circle(rnd.randint(10, 470), rnd.randint(322, 352),
                                rnd.uniform(1.5, 3.2), c, 0.55))
    else:   # contemporanea - asfalto + neon
        b.append(rect(0, GROUND_TOP_SVG, W, H - GROUND_TOP_SVG, "#16121c", opacity=0.35))
        for x in range(0, W, 46):
            b.append(line(x, 306, x, 360, "#000", 1, 0.25))
        b.append(rect(0, GROUND_TOP_SVG, W, 3, "#39ff14", opacity=0.9))
        b.append(rect(0, GROUND_TOP_SVG + 3, W, 2, "#00e5ff", opacity=0.4))
        for x in range(24, W, 90):
            b.append(circle(x, 330, 2.4, "#ff2bd6", 0.7))
    return svg_doc(W, H, "".join(b), defs)


# --------------------------------------------------------------------------
# OBSTÁCULOS por fase - blocos marrons que sobem do chão (pular por cima)
# --------------------------------------------------------------------------
def _block(cx, w, h, main, dark, light, edge, key):
    """Um bloco-obstáculo apoiado no chão (svg coords)."""
    x0 = cx - w / 2
    y0 = GROUND_TOP_SVG - h
    s = []
    s.append(rect(x0, y0, w, h, dark))                       # sombra/base
    s.append(rect(x0, y0, w - 3, h, main, rx=4))             # corpo
    s.append(rect(x0, y0, w - 3, 5, light, rx=2, opacity=0.85))   # topo iluminado
    s.append(rect(x0, y0, w - 3, h, "none", rx=4, stroke=dark, sw=2))
    if key in ("antiga",):       # tambor de coluna
        for yy in range(int(y0) + 10, int(GROUND_TOP_SVG), 12):
            s.append(line(x0 + 3, yy, x0 + w - 6, yy, dark, 1.2, 0.5))
        s.append(ellipse(cx - 1.5, y0 + 3, (w - 3) / 2 - 1, 3, light, 0.7))
    elif key == "medieval":      # bloco de pedra com ameia
        s.append(line(cx - 1.5, y0 + 6, cx - 1.5, GROUND_TOP_SVG - 4, dark, 1.4, 0.6))
        s.append(line(x0 + 3, y0 + h / 2, x0 + w - 6, y0 + h / 2, dark, 1.4, 0.6))
        s.append(rect(x0 + 2, y0 - 5, 5, 6, main)); s.append(rect(x0 + w - 10, y0 - 5, 5, 6, main))
    elif key == "cubismo":       # cubo facetado
        s.append(poly([(x0, y0), (x0 + w - 3, y0), (cx - 1.5, y0 + 14)], light, 0.5))
        s.append(poly([(x0, y0), (cx - 1.5, y0 + 14), (x0, GROUND_TOP_SVG)], dark, 0.35))
        s.append(line(cx - 1.5, y0 + 14, cx - 1.5, GROUND_TOP_SVG, dark, 1.2, 0.5))
    elif key == "moderna":       # bloco com faixa de cor
        s.append(rect(x0 + 3, y0 + h * 0.45, w - 9, 6, edge, opacity=0.8))
        s.append(circle(cx, y0 + h * 0.7, 4, "#1fb6c9", 0.7))
    else:                         # contemporanea - concreto + grafite neon
        s.append(rect(x0, y0, w - 3, h, "none", rx=4, stroke=edge, sw=2, ))
        s.append(path(f"M{x0+5} {y0+h-8} q{w/2} -14 {w-12} 0", stroke="#ff2bd6", sw=2.2, opacity=0.8))
        s.append(circle(cx, y0 + 9, 3, "#00e5ff", 0.9))
    return "".join(s)


def obstacle_costume(p):
    main, dark, light = p["obstacle_main"], p["obstacle_dark"], p["obstacle_light"]
    edge = p["ground_edge"]
    b = []
    for ob in p["layout"]["obstacles"]:
        b.append(_block(_sx(ob["cx"]), ob["w"], ob["h"], main, dark, light, edge, p["key"]))
    return svg_doc(W, H, "".join(b))


def ground_all():
    return [(f"Chao {p['num']}", ground_costume(p)) for p in PHASES]


def obstacle_all():
    return [(f"Obst {p['num']}", obstacle_costume(p)) for p in PHASES]


if __name__ == "__main__":
    import cairosvg, os
    os.makedirs("/home/user/Scratch-code-/preview/floor", exist_ok=True)
    for name, svg in ground_all() + obstacle_all():
        cairosvg.svg2png(bytestring=svg.encode(),
                         write_to=f"/home/user/Scratch-code-/preview/floor/{name}.png",
                         output_width=W, output_height=H)
    print("floor ok")
