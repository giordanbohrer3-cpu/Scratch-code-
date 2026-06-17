# -*- coding: utf-8 -*-
"""art_ui.py - Botao iniciar, selos animados da intro, contagem regressiva,
banner de fase completa, confete e o ponto invisivel do Diretor."""
from svg_core import *
from art_intro import motif_icon
from phases import PHASES


# ---- Botao COMECAR ----
BTN_W, BTN_H = 200, 58


def start_button():
    defs = lingrad("btn", [(0, "#7CFC8A", 1), (1, "#1faa3d", 1)])
    b = [rect(6, 8, BTN_W - 12, BTN_H - 12, "#0a3d1a", rx=24, opacity=0.5)]   # sombra
    b.append(rect(4, 4, BTN_W - 12, BTN_H - 12, "url(#btn)", rx=22))
    b.append(rect(4, 4, BTN_W - 12, BTN_H - 12, "none", rx=22, stroke="#0a3d1a", sw=2))
    b.append(rect(14, 10, BTN_W - 32, 12, "#ffffff", rx=8, opacity=0.35))     # brilho
    b.append(poly([(34, 20), (34, 38), (50, 29)], "#0a3d1a"))                 # play
    b.append(text(112, 38, 24, "COMEÇAR", "#0a3d1a", "900", "middle", font=FONT_TITLE))
    return svg_doc(BTN_W, BTN_H, "".join(b), defs)


# ---- Selo animado (motivo por era) ----
SEL = 120


def selo_costume(num):
    body = motif_icon(num, 60, 60, 46)
    body += circle(60, 60, 46, "none", stroke="#ffffff", sw=2, opacity=0.45)
    body += circle(60, 60, 52, "none", stroke="#ffffff", sw=1, opacity=0.2)
    return svg_doc(SEL, SEL, body)


def selo_all():
    return [(f"Selo {p['num']}", selo_costume(p["num"])) for p in PHASES]


# ---- Contagem regressiva ----
CW, CH = 300, 170


def _count(face):
    defs = radgrad("cg", [(0, "#ffffff", 0.16), (1, "#ffffff", 0)])
    b = [circle(150, 85, 80, "url(#cg)")]
    if face == "Prepare":
        b.append(rect(20, 56, 260, 58, "#0b0b14", rx=29, opacity=0.78))
        b.append(rect(20, 56, 260, 58, "none", rx=29, stroke="#ffd98a", sw=2.5))
        b.append(text(150, 94, 30, "PREPARE-SE!", "#ffd98a", "900", "middle", font=FONT_TITLE))
    else:
        b.append(circle(150, 85, 56, "#0b0b14", 0.78))
        b.append(circle(150, 85, 56, "none", stroke="#ffd98a", sw=3))
        b.append(text(150, 112, 78, face, "#ffffff", "900", "middle", font=FONT_TITLE))
    return svg_doc(CW, CH, "".join(b), defs)


def count_all():
    return [("Prepare", _count("Prepare")), ("3", _count("3")),
            ("2", _count("2")), ("1", _count("1"))]


# ---- Banner FASE COMPLETA ----
BW, BH = 380, 120


def banner_costume():
    defs = lingrad("bn", [(0, "#ffe9a8", 1), (1, "#f6c150", 1)])
    b = [rect(20, 30, BW - 40, 60, "#0b0b14", rx=30, opacity=0.85)]
    b.append(rect(20, 30, BW - 40, 60, "none", rx=30, stroke="#ffe9a8", sw=3))
    b.append(text(BW / 2, 70, 28, "FASE COMPLETA!", "url(#bn)", "900", "middle", font=FONT_TITLE))
    for x in (40, BW - 40):
        b.append(star4(x, 60, 12, "#ffe34d", 0.95))
        b.append(star4(x, 60, 7, "#ff2bd6", 0.9))
    return svg_doc(BW, BH, "".join(b), defs)


# ---- Confete (para a vitoria) ----
def confetti_costume(color):
    return svg_doc(12, 16, rect(1, 1, 8, 12, color, rx=2))


CONFETTI_COLORS = ["#ffd23f", "#ff2bd6", "#39ff14", "#00e5ff", "#f4cd5e", "#ff6f59"]


def confetti_all():
    return [(f"c{i}", confetti_costume(c)) for i, c in enumerate(CONFETTI_COLORS)]


# ---- Ponto invisivel (Diretor) ----
def dot_costume():
    return svg_doc(8, 8, rect(0, 0, 8, 8, "#000000", opacity=0))


if __name__ == "__main__":
    import cairosvg, os
    os.makedirs("/home/user/Scratch-code-/preview/ui", exist_ok=True)
    items = [("botao", start_button()), ("banner", banner_costume())]
    items += [(f"selo{n}", selo_costume(n)) for n in range(1, 6)]
    items += [(f"count_{f}", _count(f)) for f in ["Prepare", "3", "2", "1"]]
    for name, svg in items:
        cairosvg.svg2png(bytestring=svg.encode(),
                         write_to=f"/home/user/Scratch-code-/preview/ui/{name}.png",
                         output_width=300, output_height=170)
    print("ui ok")
