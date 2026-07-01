# -*- coding: utf-8 -*-
"""art_items.py - 20 relíquias coletáveis (4 por fase), caprichadas e temáticas.
Canvas 48x48, centro (24,24). Cada uma com um leve brilho de fundo.
"""
from svg_core import *
from phases import PHASES

C = 24  # centro


def _wrap(inner, accent, defs_extra=""):
    gid = f"gl_{abs(hash(inner))%99999}"
    defs = radgrad(gid, [(0, accent, 0.55), (0.6, accent, 0.18), (1, accent, 0)]) + defs_extra
    glow = circle(C, C, 23, f"url(#{gid})")
    return svg_doc(48, 48, glow + inner, defs)


# ===================== FASE 1 - ARTE ANTIGA =====================
def anfora():
    b = []
    b.append(path("M24 8 q-3 0 -3 4 q0 3 3 4 q-9 2 -9 14 q0 10 9 12 q9 -2 9 -12 q0 -12 -9 -14 q3 -1 3 -4 q0 -4 -3 -4 Z",
                  fill="#c8743a"))
    b.append(path("M16 18 q-6 2 -6 8", stroke="#9a531f", sw=2.4))   # alça
    b.append(path("M32 18 q6 2 6 8", stroke="#9a531f", sw=2.4))
    b.append(path("M15 26 q9 5 18 0", stroke="#3a2410", sw=2))      # faixa grega
    b.append(rect(18, 30, 12, 2, "#2b1c0c"))
    b.append(rect(20, 33, 8, 2, "#2b1c0c"))
    b.append(ellipse(20, 20, 2, 3, "#f1dba8", 0.6))
    return _wrap("".join(b), "#f4cd5e")


def coluna():
    b = []
    b.append(rect(15, 38, 18, 5, "#caa468"))                       # base
    b.append(rect(17, 12, 14, 26, "#e7c98c"))                      # fuste
    for x in range(19, 31, 3):
        b.append(line(x, 13, x, 37, "#b9905a", 1.4, 0.7))          # caneluras
    b.append(path("M14 12 q10 -4 20 0 q-2 -5 -10 -5 q-8 0 -10 5", fill="#f1dba8"))  # capitel jônico
    b.append(circle(16, 11, 3, "#caa468")); b.append(circle(32, 11, 3, "#caa468"))  # volutas
    return _wrap("".join(b), "#f4cd5e")


def mascara():
    b = []
    b.append(path("M24 9 q-12 0 -12 14 q0 14 12 18 q12 -4 12 -18 q0 -14 -12 -14 Z", fill="#f4cd5e"))
    b.append(path("M24 9 q-12 0 -12 14 q0 14 12 18 q12 -4 12 -18 q0 -14 -12 -14 Z",
                  fill="none", stroke="#b8860b", sw=1.5))
    b.append(rect(13, 18, 22, 4, "#1565c0", opacity=0.85))         # faixa azul
    b.append(path("M18 17 q6 -3 12 0", stroke="#1565c0", sw=2))    # sobrancelha
    b.append(ellipse(19, 20, 3, 2.2, "#1b1b2a")); b.append(ellipse(29, 20, 3, 2.2, "#1b1b2a"))
    b.append(path("M21 30 q3 2 6 0", stroke="#9a531f", sw=2))
    b.append(rect(22, 33, 4, 8, "#1565c0"))                        # barba postiça
    return _wrap("".join(b), "#f4cd5e")


def vaso_canopo():
    b = []
    b.append(path("M16 22 q0 16 8 18 q8 -2 8 -18 Z", fill="#d9b779"))   # corpo
    b.append(rect(16, 20, 16, 3, "#b8945a"))
    b.append(circle(24, 14, 8, "#e7c98c"))                          # cabeça
    b.append(path("M16 14 q0 -8 8 -8 q8 0 8 8 q-8 -4 -16 0", fill="#1565c0"))  # nemes
    b.append(line(18, 13, 30, 13, "#caa468", 2))
    b.append(circle(21, 15, 1.4, "#1b1b2a")); b.append(circle(27, 15, 1.4, "#1b1b2a"))
    b.append(path("M22 26 q4 6 0 12", stroke="#9a531f", sw=1.4, opacity=0.6))
    return _wrap("".join(b), "#f4cd5e")


# ===================== FASE 2 - ARTE MEDIEVAL =====================
def vitral():
    b = []
    cols = ["#c0234f", "#1fb6c9", "#e8c552", "#7c2dd6", "#2e7d32", "#ef6c00"]
    import math
    b.append(circle(C, C, 16, "#23253a"))
    for i in range(8):
        a0 = math.radians(i * 45); a1 = math.radians((i + 1) * 45)
        x0, y0 = C + 14 * math.cos(a0), C + 14 * math.sin(a0)
        x1, y1 = C + 14 * math.cos(a1), C + 14 * math.sin(a1)
        b.append(path(f"M{C} {C} L{x0:.1f} {y0:.1f} A14 14 0 0 1 {x1:.1f} {y1:.1f} Z",
                      fill=cols[i % len(cols)], opacity=0.9))
    b.append(circle(C, C, 16, "none", stroke="#23253a", sw=2))
    b.append(circle(C, C, 4, "#e8c552"))
    for i in range(8):
        a = math.radians(i * 45)
        b.append(line(C, C, C + 14 * math.cos(a), C + 14 * math.sin(a), "#23253a", 1.4))
    return _wrap("".join(b), "#e8c552")


def calice():
    b = []
    b.append(path("M15 12 q9 14 18 0 Z", fill="#e8c552"))           # taça
    b.append(path("M15 12 q9 14 18 0", fill="none", stroke="#b8860b", sw=1.4))
    b.append(rect(22, 22, 4, 10, "#caa055"))                        # haste
    b.append(circle(24, 24, 2.4, "#c0234f"))                        # nó com gema
    b.append(path("M16 36 q8 -5 16 0 q-8 4 -16 0", fill="#e8c552"))  # base
    b.append(rect(18, 14, 12, 2.4, "#fff7d6", opacity=0.7))
    b.append(circle(24, 9, 2.4, "#c0234f"))                         # gema topo
    return _wrap("".join(b), "#e8c552")


def pergaminho():
    b = []
    b.append(rect(13, 12, 22, 24, "#f3e7c4", rx=2))
    b.append(path("M13 12 q-4 12 0 24", fill="none", stroke="#caa055", sw=3))  # rolo esq
    b.append(path("M35 12 q4 12 0 24", fill="none", stroke="#caa055", sw=3))
    b.append(rect(17, 16, 5, 5, "#c0234f"))                         # letra capitular
    b.append(text(18.5, 20.2, 5, "A", "#fff", "900"))
    for yy in range(17, 33, 4):
        b.append(line(24, yy, 32, yy, "#7a6a44", 1, 0.7))
    b.append(circle(31, 33, 2, "#c0234f", 0.8))                     # selo
    return _wrap("".join(b), "#e8c552")


def escudo():
    b = []
    b.append(path("M24 9 L37 13 Q37 30 24 39 Q11 30 11 13 Z", fill="#7c2dd6"))
    b.append(path("M24 9 L37 13 Q37 30 24 39 Q11 30 11 13 Z", fill="none", stroke="#e8c552", sw=2))
    b.append(path("M24 9 L24 39", stroke="#e8c552", sw=1.4, opacity=0.7))
    b.append(path("M11 22 L37 22", stroke="#e8c552", sw=1.4, opacity=0.7))
    # leão heráldico simplificado
    b.append(path("M20 17 q4 -3 8 0 q-1 5 -4 6 q-3 -1 -4 -6", fill="#e8c552"))
    b.append(circle(24, 28, 3, "#e8c552"))
    return _wrap("".join(b), "#e8c552")


# ===================== FASE 3 - CUBISMO =====================
def violao_cub():
    b = []
    b.append(poly([(20, 8), (30, 10), (33, 22), (28, 40), (18, 38), (16, 22)], "#a9824e", 0.95))
    b.append(poly([(20, 8), (30, 10), (24, 24)], "#cdb285", 0.9))
    b.append(poly([(28, 40), (18, 38), (24, 24)], "#6f5b3e", 0.9))
    b.append(circle(24, 26, 5, "#2a2018"))                         # boca
    b.append(line(22, 8, 22, 24, "#3a2f20", 1.4))                  # braço
    for yy in range(12, 20, 3):
        b.append(line(20, yy, 26, yy, "#3a2f20", 1))               # trastes
    b.append(poly([(16, 22), (24, 24), (18, 38)], "none", stroke="#e8d9b0", sw=1, ))
    return _wrap("".join(b), "#e8d9b0")


def rosto_facetado():
    b = []
    b.append(poly([(16, 12), (30, 9), (34, 24), (28, 39), (16, 36), (13, 22)], "#cdb285"))
    b.append(poly([(24, 9), (30, 9), (34, 24), (24, 22)], "#e8d9b0", 0.95))   # meia-face clara
    b.append(poly([(13, 22), (24, 22), (28, 39), (16, 36)], "#8a7355", 0.95))  # meia-face escura
    b.append(line(24, 9, 24, 39, "#3a2f20", 1.2, 0.6))
    b.append(ellipse(20, 21, 2.4, 1.6, "#1a140c"))                  # olho de frente
    b.append(circle(29, 20, 1.6, "#1a140c"))                        # olho de perfil
    b.append(path("M22 30 q3 2 6 -1", stroke="#3a2f20", sw=1.6))
    b.append(poly([(28, 22), (33, 24), (29, 28)], "#6f5b3e"))       # nariz angular
    return _wrap("".join(b), "#e8d9b0")


def cubo_analitico():
    b = []
    b.append(poly([(14, 18), (24, 12), (34, 18), (24, 24)], "#e8d9b0"))   # topo
    b.append(poly([(14, 18), (24, 24), (24, 38), (14, 32)], "#8a7355"))   # esq
    b.append(poly([(34, 18), (24, 24), (24, 38), (34, 32)], "#5c4a35"))   # dir
    b.append(poly([(14, 18), (24, 12), (34, 18), (24, 24)], "none", stroke="#3a2f20", sw=1.2))
    b.append(line(24, 24, 24, 38, "#3a2f20", 1, 0.6))
    b.append(line(14, 18, 14, 32, "#3a2f20", 1, 0.4))
    return _wrap("".join(b), "#e8d9b0")


def jornal_colado():
    b = []
    b.append(rect(13, 14, 22, 22, "#e8e0c8", rx=1.5))              # papel
    b.append(poly([(13, 14), (35, 16), (33, 36), (15, 34)], "#d8cfae", 0.5))   # leve distorção
    b.append(rect(15, 16, 18, 4, "#3a2f20", opacity=0.85))        # manchete
    for yy in range(22, 34, 3):
        b.append(line(15, yy, 31, yy, "#6f5b3e", 1, 0.7))
    b.append(rect(24, 24, 9, 8, "#a9824e", opacity=0.6))          # foto
    b.append(text(16.5, 19.3, 3.4, "LE JOURNAL", "#e8e0c8", "900"))
    return _wrap("".join(b), "#e8d9b0")


# ===================== FASE 4 - ARTE MODERNA =====================
def relogio_derretido():
    b = []
    b.append(path("M14 14 q12 -6 20 2 q6 8 -2 16 q-2 8 -10 12 q4 -10 -2 -16 q-8 -6 -6 -14 Z",
                  fill="#e8d9b0"))
    b.append(path("M14 14 q12 -6 20 2 q6 8 -2 16 q-2 8 -10 12", fill="none", stroke="#b8945a", sw=1.6))
    b.append(circle(23, 19, 8, "#f4f1ea"))
    b.append(circle(23, 19, 8, "none", stroke="#caa055", sw=1.4))
    for i in range(12):
        import math
        a = math.radians(i * 30)
        b.append(line(23 + 6.5 * math.cos(a), 19 + 6.5 * math.sin(a),
                      23 + 7.8 * math.cos(a), 19 + 7.8 * math.sin(a), "#7a6a44", 0.8))
    b.append(line(23, 19, 23, 14, "#1a1033", 1.4)); b.append(line(23, 19, 27, 21, "#1a1033", 1.4))
    return _wrap("".join(b), "#ffd23f")


def girassol():
    import math
    b = []
    for i in range(12):
        a = math.radians(i * 30)
        x = C + 14 * math.cos(a); y = 22 + 14 * math.sin(a)
        b.append(ellipse(x, y, 4, 2.2, "#ffb703", 0.95))
        b.append(group("", ))
    for i in range(12):
        a = math.radians(i * 30 + 15)
        x = C + 11 * math.cos(a); y = 22 + 11 * math.sin(a)
        b.append(ellipse(x, y, 3, 2, "#ffd23f"))
    b.append(circle(C, 22, 8, "#7a4a1e"))
    for ox in (-3, 0, 3):
        for oy in (-3, 0, 3):
            b.append(circle(C + ox, 22 + oy, 1, "#4a2e12"))
    b.append(line(C, 30, C, 42, "#2e7d32", 2.4))
    b.append(path("M24 36 q-6 -2 -7 -7", stroke="#2e7d32", sw=2.4))
    return _wrap("".join(b), "#ffd23f")


def mondrian():
    b = []
    b.append(rect(13, 12, 22, 24, "#f4f1ea", rx=1))
    b.append(rect(13, 12, 13, 13, "#c4263d"))                      # vermelho
    b.append(rect(28, 26, 7, 10, "#1d4ed8"))                       # azul
    b.append(rect(28, 12, 7, 6, "#ffd23f"))                        # amarelo
    b.append(line(26, 12, 26, 36, "#0a0a0a", 2.4))
    b.append(line(13, 25, 35, 25, "#0a0a0a", 2.4))
    b.append(rect(13, 12, 22, 24, "none", rx=1, stroke="#0a0a0a", sw=2))
    return _wrap("".join(b), "#ffd23f")


def noite_estrelada():
    import math
    b = []
    b.append(circle(C, C, 15, "#1a2a6c"))
    # espiral
    d = "M24 24 "
    pts = []
    for t in range(0, 540, 20):
        r = 1 + t * 0.022
        a = math.radians(t)
        pts.append((24 + r * math.cos(a), 24 + r * math.sin(a)))
    d += "L" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    b.append(path(d, fill="none", stroke="#7ec8e3", sw=2))
    b.append(circle(33, 16, 3.5, "#ffd23f"))                       # lua/estrela
    for (x, y) in [(15, 15), (16, 30), (33, 31)]:
        b.append(star4(x, y, 2.4, "#ffe9a8"))
    b.append(circle(C, C, 15, "none", stroke="#0d1b4c", sw=1.5))
    return _wrap("".join(b), "#ffd23f")


# ===================== FASE 5 - ARTE CONTEMPORÂNEA =====================
def balao_pop():
    b = []
    b.append(star(C, 22, 18, 13, 10, "#ffe34d", 0.95))             # explosão cômic
    b.append(star(C, 22, 14, 10, 10, "#ff2bd6", 0.95))
    b.append(circle(C, 22, 9, "#0d0d12"))
    b.append(text(C, 25, 7.5, "POP", "#ffe34d", "900", "middle"))
    return _wrap("".join(b), "#ff2bd6")


def lata_pop():
    b = []
    b.append(rect(16, 12, 16, 26, "#f4f1ea", rx=2))                # lata
    b.append(rect(16, 12, 16, 8, "#c4263d", rx=2))                 # topo vermelho
    b.append(rect(16, 18, 16, 3, "#caa055"))                       # faixa dourada
    b.append(rect(16, 28, 16, 10, "#c4263d", opacity=0.9))
    b.append(text(C, 26, 4.2, "POP", "#c4263d", "900", "middle"))
    b.append(text(C, 35, 3.4, "ART", "#f4f1ea", "900", "middle"))
    b.append(ellipse(24, 12, 8, 2.4, "#cfcabb"))
    return _wrap("".join(b), "#ff2bd6")


def spray():
    b = []
    b.append(rect(18, 16, 12, 22, "#00e5ff", rx=2))                # corpo da lata
    b.append(rect(18, 16, 12, 6, "#0a8fa0", rx=2))
    b.append(rect(21, 10, 6, 6, "#16121c"))                        # tampa
    b.append(rect(22, 8, 4, 3, "#16121c"))                         # bico
    # jato de tinta neon
    for r, op in [(3, 0.7), (5, 0.4), (7, 0.2)]:
        b.append(circle(35, 9, r, "#ff2bd6", op))
    b.append(circle(35, 9, 1.6, "#ff2bd6"))
    b.append(text(24, 30, 4, "ART", "#16121c", "900", "middle"))
    return _wrap("".join(b), "#ff2bd6")


def coracao_neon():
    heart = "M24 37 q-13 -9 -13 -18 q0 -6 6 -6 q5 0 7 5 q2 -5 7 -5 q6 0 6 6 q0 9 -13 18 Z"
    b = []
    # halo neon (mesmo coração, traços grossos e translúcidos)
    for sw, op in [(8, 0.18), (5, 0.32)]:
        b.append(path(heart, fill="none", stroke="#ff2bd6", sw=sw, opacity=op))
    b.append(path(heart, fill="#ff2bd6"))
    b.append(path(heart, fill="none", stroke="#00e5ff", sw=1.6))
    b.append(path("M19 19 q-2 3 0 7", stroke="#ffd9f4", sw=1.8, opacity=0.9))   # brilho
    return _wrap("".join(b), "#ff2bd6")


RELIC_FUNCS = {
    1: [anfora, coluna, mascara, vaso_canopo],
    2: [vitral, calice, pergaminho, escudo],
    3: [violao_cub, rosto_facetado, cubo_analitico, jornal_colado],
    4: [relogio_derretido, girassol, mondrian, noite_estrelada],
    5: [balao_pop, lata_pop, spray, coracao_neon],
}


def items_for_slot(slot):
    """slot 1..4 -> lista de 5 costumes (uma por fase) para o sprite Objeto{slot}."""
    out = []
    for p in PHASES:
        fn = RELIC_FUNCS[p["num"]][slot - 1]
        out.append((f"F{p['num']} {p['relics'][slot-1]}", fn()))
    return out


if __name__ == "__main__":
    import cairosvg, os
    os.makedirs("/home/user/Scratch-code-/preview/items", exist_ok=True)
    for p in PHASES:
        for i, fn in enumerate(RELIC_FUNCS[p["num"]]):
            cairosvg.svg2png(bytestring=fn().encode(),
                             write_to=f"/home/user/Scratch-code-/preview/items/F{p['num']}_{i+1}.png",
                             output_width=144, output_height=144)
    print("items ok")
