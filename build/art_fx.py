# -*- coding: utf-8 -*-
"""art_fx.py - Elementos animados de fundo (Astro + Partículas) e o rótulo de
era (texto com nome da arte + período) que aparece durante a fase.
Uma costume por era (índice = fase).
"""
from svg_core import *
from phases import PHASES
import math


# ===========================================================================
# ASTRO - elemento celeste grande no céu (anima com pulso/giro leve)
# Canvas 150x150, centro (75,75).
# ===========================================================================
AW = 150
AC = 75


def _astro(num):
    b = []
    if num == 1:      # Sol radiante (Antiga)
        defs = radgrad("sunfx", [(0, "#fff6d8", 1), (0.5, "#ffd271", 0.9), (1, "#ffd271", 0)])
        for a in range(0, 360, 15):
            x = AC + 70 * math.cos(math.radians(a)); y = AC + 70 * math.sin(math.radians(a))
            b.append(line(AC, AC, x, y, "#ffe9b0", 2, 0.5))
        b.append(circle(AC, AC, 60, "url(#sunfx)"))
        b.append(circle(AC, AC, 34, "#ffe9b0", 0.95))
        return svg_doc(AW, AW, "".join(b), defs)
    if num == 2:      # Lua crescente + estrelas (Medieval)
        defs = radgrad("moonfx", [(0, "#f5efd6", 0.5), (1, "#f5efd6", 0)])
        b.append(circle(AC, AC, 60, "url(#moonfx)"))
        b.append(circle(AC, AC, 34, "#f3edd0"))
        b.append(circle(AC + 14, AC - 8, 30, "#16223f"))
        for (dx, dy) in [(-46, -36), (44, -30), (40, 40), (-40, 38)]:
            b.append(star4(AC + dx, AC + dy, 5, "#fff3cf", 0.9))
        return svg_doc(AW, AW, "".join(b))
    if num == 3:      # Sol facetado (Cubismo)
        pal = ["#e8d9b0", "#cdb285", "#a9824e", "#6f5b3e"]
        for i in range(8):
            a0 = math.radians(i * 45); a1 = math.radians((i + 1) * 45)
            x0, y0 = AC + 52 * math.cos(a0), AC + 52 * math.sin(a0)
            x1, y1 = AC + 52 * math.cos(a1), AC + 52 * math.sin(a1)
            b.append(poly([(AC, AC), (x0, y0), (x1, y1)], pal[i % 4], 0.9))
            b.append(poly([(AC, AC), (x0, y0), (x1, y1)], "none", stroke="#3a2f20", sw=1))
        b.append(circle(AC, AC, 16, "#f1dba8"))
        return svg_doc(AW, AW, "".join(b))
    if num == 4:      # Espiral onírica (Moderna)
        defs = radgrad("swirl", [(0, "#ffd23f", 0.9), (1, "#ffd23f", 0)])
        b.append(circle(AC, AC, 64, "url(#swirl)"))
        for col, off in [("#1fb6c9", 0), ("#ff6f59", 180)]:
            pts = []
            for t in range(0, 540, 14):
                r = 3 + t * 0.09
                a = math.radians(t + off)
                pts.append((AC + r * math.cos(a), AC + r * math.sin(a)))
            d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
            b.append(path(d, fill="none", stroke=col, sw=3.5, opacity=0.8))
        b.append(circle(AC, AC, 10, "#ffe9a8"))
        return svg_doc(AW, AW, "".join(b), defs)
    # Explosão neon (Contemporânea)
    b.append(star(AC, AC, 64, 40, 12, "#ffe34d", 0.9))
    b.append(star(AC, AC, 46, 28, 12, "#ff2bd6", 0.95))
    b.append(star(AC, AC, 30, 18, 6, "#00e5ff", 0.95))
    b.append(circle(AC, AC, 12, "#39ff14"))
    return svg_doc(AW, AW, "".join(b))


def astro_all():
    return [(f"Astro {p['num']}", _astro(p["num"])) for p in PHASES]


# ===========================================================================
# PARTÍCULA - pequena mote que flutua no fundo. Canvas 20x20, centro (10,10).
# ===========================================================================
def _part(num):
    if num == 1:   return svg_doc(20, 20, circle(10, 10, 5, "#f1dba8", 0.9))      # areia
    if num == 2:   return svg_doc(20, 20, circle(10, 10, 5, "#ffe9a8", 0.9) + circle(10, 10, 2.5, "#fff", 0.9))  # luz
    if num == 3:   return svg_doc(20, 20, poly([(10, 3), (17, 15), (3, 15)], "#cdb285", 0.9))  # faceta
    if num == 4:   return svg_doc(20, 20, star4(10, 10, 6, "#ffd23f", 0.95))      # estrela
    return svg_doc(20, 20, circle(10, 10, 5, "#ff2bd6", 0.95) + circle(10, 10, 2.5, "#00e5ff", 0.9))  # neon


def part_all():
    return [(f"Part {p['num']}", _part(p["num"])) for p in PHASES]


# ===========================================================================
# RÓTULO - texto com nome da arte + período (aparece no topo durante a fase).
# Canvas 360x48, centro (180,24).
# ===========================================================================
RW, RH = 304, 48


def _rotulo(p):
    accent = p["accent"]
    b = [rect(6, 6, RW - 12, RH - 12, "#0b0b14", rx=18, opacity=0.72)]
    b.append(rect(6, 6, RW - 12, RH - 12, "none", rx=18, stroke=accent, sw=2))
    b.append(circle(26, RH / 2, 6, accent, 0.9))
    b.append(text(42, 22, 15, p["title"], "#ffffff", "900"))
    b.append(text(42, 38, 11.5, p["period"], accent, "700"))
    return svg_doc(RW, RH, "".join(b))


def rotulo_all():
    return [(f"Rotulo {p['num']}", _rotulo(p)) for p in PHASES]


if __name__ == "__main__":
    import cairosvg, os
    os.makedirs("/home/user/Scratch-code-/preview/fx", exist_ok=True)
    for name, svg in astro_all() + rotulo_all() + part_all():
        cairosvg.svg2png(bytestring=svg.encode(),
                         write_to=f"/home/user/Scratch-code-/preview/fx/{name}.png",
                         output_width=300, output_height=120)
    print("fx ok")
