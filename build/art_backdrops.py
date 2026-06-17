# -*- coding: utf-8 -*-
"""art_backdrops.py - Os 5 fundos imersivos (apenas cenário, sem chão).
O sprite Chão cobre a faixa inferior (y 300..360), então estes desenhos
servem de pano de fundo com a arte de cada era. 480x360.
"""
from svg_core import *
import math

W, H = 480, 360


# =====================================================================
# 1) ARTE ANTIGA - Egito + Grécia: pirâmides, sol, templo, palmeiras
# =====================================================================
def bg_antiga():
    defs = lingrad("skyA", [(0, "#241606", 1), (0.5, "#8a5a24", 1), (1, "#e7b86a", 1)])
    defs += radgrad("sunA", [(0, "#fff3cf", 0.95), (0.55, "#f6c768", 0.5), (1, "#f6c768", 0)])
    b = [rect(0, 0, W, H, "url(#skyA)")]
    # sol e raios
    b.append(circle(372, 96, 78, "url(#sunA)"))
    for ang in range(0, 360, 20):
        x2 = 372 + 120 * math.cos(math.radians(ang)); y2 = 96 + 120 * math.sin(math.radians(ang))
        b.append(line(372, 96, x2, y2, "#ffe9b0", 1.3, 0.16))
    b.append(circle(372, 96, 34, "#ffe9b0", 0.95))
    # dunas distantes
    b.append(path("M0 250 Q120 220 240 248 T480 244 L480 360 L0 360 Z", fill="#a9763a", opacity=0.7))
    b.append(path("M0 280 Q160 256 300 280 T480 276 L480 360 L0 360 Z", fill="#8a5a2e", opacity=0.7))
    # pirâmides
    b.append(poly([(40, 280), (150, 150), (260, 280)], "#9a6630", 0.95))
    b.append(poly([(150, 280), (150, 150), (260, 280)], "#7a4e22", 0.9))
    b.append(poly([(120, 280), (170, 210), (220, 280)], "#3a2410", 0.4))
    # templo grego (direita)
    tx = 320
    b.append(rect(tx - 12, 150, 150, 8, "#e7c98c"))          # entablamento
    b.append(poly([(tx - 16, 150), (tx + 154, 150), (tx + 69, 120)], "#f1dba8"))  # frontão
    b.append(poly([(tx - 16, 150), (tx + 154, 150), (tx + 69, 120)], "none", stroke="#b9905a", sw=1.5))
    for i in range(6):
        cx = tx + i * 28
        b.append(rect(cx - 7, 158, 14, 92, "#e7c98c"))
        b.append(rect(cx - 7, 158, 3, 92, "#fff3cf", opacity=0.4))
        b.append(rect(cx - 9, 250, 18, 6, "#caa468"))
        b.append(rect(cx - 9, 152, 18, 7, "#f1dba8"))
    # palmeira (esquerda)
    b.append(path("M70 280 q-6 -50 4 -86", stroke="#5a3a18", sw=7))
    for a in (-50, -20, 10, 40, 70, 110):
        b.append(path(f"M74 196 q{18*math.cos(math.radians(a)):.0f} {-8+10*math.sin(math.radians(a)):.0f} {34*math.cos(math.radians(a)):.0f} {6+14*math.sin(math.radians(a)):.0f}",
                      stroke="#3f7d3a", sw=5, opacity=0.9))
    # parede de hieróglifos (faixa baixa)
    b.append(rect(0, 286, W, 18, "#caa468", opacity=0.5))
    for x in range(12, W, 34):
        b.append(circle(x, 295, 2.4, "#3a2410", 0.6))
        b.append(rect(x + 9, 290, 3, 10, "#3a2410", opacity=0.5))
        b.append(path(f"M{x+18} 290 q4 4 0 9", stroke="#3a2410", sw=1.6, opacity=0.5))
    # aves
    b.append(path("M90 70 q7 -7 14 0 q7 -7 14 0", stroke="#2a1c0c", sw=2, opacity=0.5))
    b.append(path("M130 92 q5 -5 10 0 q5 -5 10 0", stroke="#2a1c0c", sw=2, opacity=0.4))
    return svg_doc(W, H, "".join(b), defs)


# =====================================================================
# 2) ARTE MEDIEVAL - catedral gótica, rosácea, vitrais, estandartes
# =====================================================================
def bg_medieval():
    defs = lingrad("skyM", [(0, "#05060f", 1), (0.5, "#162a5e", 1), (1, "#33477f", 1)])
    defs += radgrad("glowM", [(0, "#ffe9a8", 0.5), (1, "#ffe9a8", 0)])
    b = [rect(0, 0, W, H, "url(#skyM)")]
    b.append(circle(240, 50, 130, "url(#glowM)"))
    # lua
    b.append(circle(410, 56, 20, "#f3edd0", 0.9))
    b.append(circle(404, 52, 18, "#162a5e", 0.6))
    # silhueta da catedral
    b.append(rect(40, 120, 400, 184, "#0c1430", opacity=0.92))
    # torres
    for txx in (40, 410):
        b.append(rect(txx - 4, 78, 38, 46, "#0c1430"))
        b.append(poly([(txx - 8, 78), (txx + 38, 78), (txx + 15, 40)], "#0a1126"))
    # rosácea
    cx, cy = 240, 110
    b.append(circle(cx, cy, 34, "#1c2a55"))
    cols = ["#7c2dd6", "#1fb6c9", "#e8c552", "#c0234f", "#2e7d32", "#ef6c00"]
    for i in range(12):
        a0 = math.radians(i * 30); a1 = math.radians((i + 1) * 30)
        x0, y0 = cx + 30 * math.cos(a0), cy + 30 * math.sin(a0)
        x1, y1 = cx + 30 * math.cos(a1), cy + 30 * math.sin(a1)
        b.append(path(f"M{cx} {cy} L{x0:.1f} {y0:.1f} A30 30 0 0 1 {x1:.1f} {y1:.1f} Z",
                      fill=cols[i % len(cols)], opacity=0.55))
    b.append(circle(cx, cy, 34, "none", stroke="#e8c552", sw=2))
    b.append(circle(cx, cy, 8, "#e8c552", 0.7))
    # janelas em arco com vitrais
    glass = ["#7c2dd6", "#1fb6c9", "#e8c552", "#c0234f"]
    for i, jx in enumerate([95, 165, 315, 385]):
        top = 165
        b.append(path(f"M{jx-22} 304 L{jx-22} {top+26} Q{jx-22} {top} {jx} {top} Q{jx+22} {top} {jx+22} {top+26} L{jx+22} 304 Z",
                      fill=glass[i % 4], opacity=0.55))
        b.append(path(f"M{jx-22} 304 L{jx-22} {top+26} Q{jx-22} {top} {jx} {top} Q{jx+22} {top} {jx+22} {top+26} L{jx+22} 304 Z",
                      fill="none", stroke="#0c1430", sw=3))
        b.append(line(jx, top, jx, 304, "#0c1430", 2, 0.7))
        b.append(line(jx - 22, top + 60, jx + 22, top + 60, "#0c1430", 2, 0.6))
        b.append(circle(jx, top + 18, 4, "#fff3cf", 0.7))
    # estandartes
    for i, bx in enumerate([150, 330]):
        c = ["#c0234f", "#1d4ed8"][i]
        b.append(poly([(bx - 10, 150), (bx + 10, 150), (bx + 10, 196), (bx, 188), (bx - 10, 196)], c, 0.9))
        b.append(star4(bx, 168, 5, "#e8c552", 0.9))
    # poeira de luz
    for (x, y, r) in [(120, 150, 2), (350, 180, 2.4), (210, 130, 1.6), (300, 220, 2)]:
        b.append(circle(x, y, r, "#ffe9a8", 0.5))
    return svg_doc(W, H, "".join(b), defs)


# =====================================================================
# 3) CUBISMO - planos geométricos fragmentados, violão e rosto
# =====================================================================
def bg_cubismo():
    defs = lingrad("skyC", [(0, "#2a2118", 1), (1, "#b3955f", 1)])
    b = [rect(0, 0, W, H, "url(#skyC)")]
    palette = ["#8a7355", "#cdb285", "#5c4a35", "#e8d9b0", "#6f5b3e", "#a9824e"]
    facets = [
        [(0, 0), (170, 0), (90, 150), (0, 100)],
        [(170, 0), (330, 0), (270, 130), (90, 150)],
        [(330, 0), (480, 0), (480, 120), (270, 130)],
        [(0, 100), (90, 150), (60, 280), (0, 250)],
        [(90, 150), (270, 130), (240, 280), (60, 280)],
        [(270, 130), (480, 120), (480, 270), (240, 280)],
    ]
    for i, f in enumerate(facets):
        b.append(poly(f, palette[i % len(palette)], 0.82))
        b.append(poly(f, "none", stroke="#1a140c", sw=1.6))
    # sol/lua geométrico
    b.append(poly([(380, 60), (420, 50), (430, 92), (392, 100)], "#e8d9b0", 0.6))
    b.append(circle(404, 74, 16, "#f1dba8", 0.4))
    # violão fragmentado
    b.append(group(
        poly([(300, 120), (350, 108), (378, 158), (360, 230), (392, 290), (340, 300), (312, 240), (286, 180)], "#3a2f20", 0.32)
        + circle(338, 196, 26, "#1a140c", 0.3)
        + line(300, 120, 392, 290, "#1a140c", 2, 0.3)
        + line(286, 180, 360, 230, "#1a140c", 2, 0.25)))
    # rosto multifacetado (esquerda)
    b.append(group(
        poly([(60, 90), (130, 82), (150, 150), (120, 220), (66, 232), (44, 160)], "#e8d9b0", 0.42)
        + poly([(95, 90), (140, 110), (130, 180), (96, 210)], "#cdb285", 0.5)
        + circle(100, 140, 6, "#1a140c", 0.6) + circle(78, 150, 5, "#1a140c", 0.4)
        + line(95, 82, 96, 232, "#1a140c", 1.5, 0.4)
        + poly([(120, 150), (150, 165), (124, 188)], "#6f5b3e", 0.6)))
    return svg_doc(W, H, "".join(b), defs)


# =====================================================================
# 4) ARTE MODERNA - céu onírico em espiral, blocos de cor, relógio
# =====================================================================
def bg_moderna():
    defs = lingrad("skyMo", [(0, "#160d2e", 1), (0.5, "#5b2168", 1), (1, "#c4263d", 1)])
    defs += radgrad("moonMo", [(0, "#ffd23f", 0.95), (1, "#ffd23f", 0)])
    b = [rect(0, 0, W, H, "url(#skyMo)")]
    # espirais oníricas (Noite Estrelada)
    for cx, cy, col, op, sc in [(110, 90, "#1fb6c9", 0.55, 0.11), (360, 70, "#ffd23f", 0.5, 0.12),
                                 (230, 150, "#ff6f59", 0.4, 0.09)]:
        pts = []
        for t in range(0, 720, 16):
            r = 2 + t * sc
            a = math.radians(t)
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        b.append(path(d, fill="none", stroke=col, sw=2.6, opacity=op))
    b.append(circle(360, 70, 30, "url(#moonMo)"))
    b.append(circle(360, 70, 16, "#ffe9a8", 0.9))
    # estrelas
    for (x, y) in [(60, 60), (180, 50), (300, 120), (440, 150), (90, 200), (410, 60)]:
        b.append(star4(x, y, 4, "#ffe9a8", 0.8))
    # blocos de cor (Mondrian/Kandinsky)
    for x, y, w, h, c in [(40, 210, 70, 50, "#ffd23f"), (140, 246, 52, 60, "#1fb6c9"),
                          (380, 200, 64, 54, "#c4263d"), (300, 252, 44, 44, "#f4f1ea")]:
        b.append(rect(x, y, w, h, c, 8, 0.9))
        b.append(rect(x, y, w, h, "none", 8, stroke="#1a1033", sw=2))
    # relógio derretido
    b.append(ellipse(228, 116, 28, 20, "#e8d9b0", 0.9))
    b.append(path("M200 124 q6 30 18 38 q-10 5 -8 20", fill="none", stroke="#e8d9b0", sw=7, opacity=0.9))
    b.append(circle(228, 116, 14, "#f4f1ea", 0.9))
    b.append(circle(228, 116, 3, "#1a1033"))
    b.append(line(228, 116, 238, 106, "#1a1033", 2)); b.append(line(228, 116, 224, 104, "#1a1033", 2))
    return svg_doc(W, H, "".join(b), defs)


# =====================================================================
# 5) ARTE CONTEMPORÂNEA - cidade neon, meio-tom, grafite POP
# =====================================================================
def bg_contemporanea():
    defs = lingrad("skyCo", [(0, "#0c0c12", 1), (1, "#2a0d33", 1)])
    b = [rect(0, 0, W, H, "url(#skyCo)")]
    import random
    rnd = random.Random(3)
    # meio-tom pop
    for gy in range(36, 180, 15):
        for gx in range(280, 470, 15):
            r = rnd.uniform(1.2, 5.5) * (1 - (gy - 36) / 200)
            if r > 0.6:
                b.append(circle(gx, gy, r, "#ff2bd6", 0.45))
    # skyline neon
    rnd2 = random.Random(11)
    bx = 0
    while bx < W:
        bw = rnd2.choice([36, 48, 60]); bh = rnd2.choice([90, 130, 170, 210])
        b.append(rect(bx, 304 - bh, bw, bh, "#16121c"))
        b.append(rect(bx, 304 - bh, bw, 3, rnd2.choice(["#39ff14", "#00e5ff", "#ff2bd6"]), opacity=0.8))
        for wy in range(304 - bh + 12, 300, 20):
            for wx in range(bx + 6, bx + bw - 6, 13):
                if rnd2.random() > 0.45:
                    b.append(rect(wx, wy, 5, 8, rnd2.choice(["#39ff14", "#00e5ff", "#ff2bd6", "#ffe34d"]), opacity=0.85))
        bx += bw + 5
    # explosão POP
    b.append(star(110, 86, 48, 30, 12, "#ffe34d", 0.9))
    b.append(star(110, 86, 34, 22, 12, "#ff2bd6", 0.95))
    b.append(text(110, 94, 24, "POP", "#0d0d12", "900", "middle"))
    # grafite neon
    b.append(path("M20 230 q40 -34 80 0 t80 0", fill="none", stroke="#39ff14", sw=4, opacity=0.6))
    b.append(path("M250 250 q34 -44 64 0", fill="none", stroke="#00e5ff", sw=4, opacity=0.55))
    b.append(path("M300 150 q20 24 -6 40", fill="none", stroke="#ff2bd6", sw=3.5, opacity=0.5))
    return svg_doc(W, H, "".join(b), defs)


BG_FUNCS = {1: bg_antiga, 2: bg_medieval, 3: bg_cubismo, 4: bg_moderna, 5: bg_contemporanea}


if __name__ == "__main__":
    import cairosvg, os
    os.makedirs("/home/user/Scratch-code-/preview", exist_ok=True)
    for n, fn in BG_FUNCS.items():
        cairosvg.svg2png(bytestring=fn().encode(),
                         write_to=f"/home/user/Scratch-code-/preview/bg{n}.png",
                         output_width=W, output_height=H)
    print("backdrops ok")
