# -*- coding: utf-8 -*-
"""art_intro.py - Telas de Stage: introducao de cada fase (com objetivo e
curiosidade), tela inicial e tela de vitoria. 480x360.
A animacao de 7s e feita por sprites (ver art_ui / logica), aqui fica a base.
"""
from svg_core import *
from phases import PHASES
import math

W, H = 480, 360


# --------------------------------------------------------------------------
# Selo redondo com o motivo de cada era (reutilizado em varios lugares)
# --------------------------------------------------------------------------
def motif_icon(num, cx, cy, r):
    s = ""
    if num == 1:      # Antiga: piramide + sol
        s += circle(cx, cy, r, "#3a2410", 0.95)
        s += circle(cx, cy - r * 0.5, r * 0.26, "#ffe9b0")
        s += poly([(cx - r * 0.6, cy + r * 0.5), (cx, cy - r * 0.45), (cx + r * 0.6, cy + r * 0.5)], "#e8c98c")
        s += poly([(cx, cy - r * 0.45), (cx + r * 0.6, cy + r * 0.5), (cx, cy + r * 0.5)], "#b9905a")
    elif num == 2:    # Medieval: vitral em arco
        s += circle(cx, cy, r, "#0c1430", 0.95)
        s += path(f"M{cx-r*0.5} {cy+r*0.5} L{cx-r*0.5} {cy-r*0.05} Q{cx-r*0.5} {cy-r*0.5} {cx} {cy-r*0.5} Q{cx+r*0.5} {cy-r*0.5} {cx+r*0.5} {cy-r*0.05} L{cx+r*0.5} {cy+r*0.5} Z", fill="#e8c552", opacity=0.85)
        s += line(cx, cy - r * 0.5, cx, cy + r * 0.5, "#0c1430", 2)
        s += line(cx - r * 0.5, cy + r * 0.05, cx + r * 0.5, cy + r * 0.05, "#0c1430", 2)
    elif num == 3:    # Cubismo: facetas
        s += circle(cx, cy, r, "#3a2f20", 0.95)
        s += poly([(cx - r * 0.5, cy - r * 0.4), (cx + r * 0.1, cy - r * 0.5), (cx + r * 0.2, cy), (cx - r * 0.3, cy + r * 0.1)], "#e8d9b0")
        s += poly([(cx + r * 0.1, cy - r * 0.5), (cx + r * 0.55, cy - r * 0.2), (cx + r * 0.45, cy + r * 0.35), (cx + r * 0.2, cy)], "#cdb285")
        s += poly([(cx - r * 0.3, cy + r * 0.1), (cx + r * 0.2, cy), (cx + r * 0.1, cy + r * 0.5), (cx - r * 0.45, cy + r * 0.4)], "#8a7355")
    elif num == 4:    # Moderna: relogio derretido + lua
        s += circle(cx, cy, r, "#5b2168", 0.95)
        s += circle(cx + r * 0.4, cy - r * 0.4, r * 0.18, "#ffd23f")
        s += ellipse(cx, cy - r * 0.02, r * 0.44, r * 0.3, "#e8d9b0")
        s += circle(cx, cy - r * 0.02, r * 0.06, "#5b2168")
        s += path(f"M{cx-r*0.42} {cy+r*0.12} q{r*0.12} {r*0.4} {r*0.32} {r*0.48}", stroke="#e8d9b0", sw=4)
    else:             # Contemporanea: pop star
        s += circle(cx, cy, r, "#16121c", 0.95)
        s += star(cx, cy, r * 0.7, r * 0.42, 10, "#ffe34d", 0.95)
        s += star(cx, cy, r * 0.5, r * 0.3, 10, "#ff2bd6", 0.95)
        s += circle(cx, cy, r * 0.22, "#39ff14")
    return s


def _wrap(s, width):
    words, lines, cur = s.split(" "), [], ""
    for w in words:
        if len(cur) + len(w) + 1 <= width:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


# --------------------------------------------------------------------------
# Tela de introducao da fase
# --------------------------------------------------------------------------
def intro_screen(p):
    top, bot, accent = p["sky_top"], p["sky_bot"], p["accent"]
    defs = lingrad("introbg", [(0, top, 1), (1, bot, 1)])
    defs += radgrad("introglow", [(0, accent, 0.32), (1, accent, 0)])
    b = [rect(0, 0, W, H, "url(#introbg)")]
    b.append(circle(W * 0.8, 70, 150, "url(#introglow)"))
    # motivo grande e esmaecido no fundo
    b.append(group(motif_icon(p["num"], 380, 250, 120), opacity=0.12))
    # painel central
    b.append(rect(26, 40, W - 52, H - 80, "#0b0b14", rx=20, opacity=0.62))
    b.append(rect(26, 40, W - 52, H - 80, "none", rx=20, stroke=accent, sw=2))
    b.append(path(f"M26 60 Q26 40 46 40 L{W-46} 40 Q{W-26} 40 {W-26} 60", fill="none", stroke=accent, sw=3, opacity=0.6))
    # selo da era
    b.append(motif_icon(p["num"], 84, 118, 46))
    b.append(circle(84, 118, 46, "none", stroke=accent, sw=2.5))
    # cabecalho
    b.append(text(150, 92, 13.5, f"FASE {p['num']} DE 5", accent, "800", spacing=1.5))
    b.append(text(W - 50, 92, 12.5, p["period"], "#ffffff", "600", anchor="end", opacity=0.7))
    b.append(text(150, 126, 30, p["title"], "#ffffff", "900"))
    b.append(text(150, 150, 15, p["subtitle"], accent, "600", italic=True))
    b.append(line(150, 162, W - 50, 162, accent, 1.5, 0.35))
    # objetivo
    b.append(text(52, 206, 14, "OBJETIVO", accent, "800", spacing=1))
    for i, ln in enumerate(_wrap(p["objective"], 50)[:2]):
        b.append(text(52, 230 + i * 22, 16, ln, "#ffffff", "600"))
    # curiosidade
    b.append(text(52, 290, 13, "VOCÊ SABIA?", accent, "800", spacing=1))
    for i, ln in enumerate(_wrap(p["fact"], 56)[:2]):
        b.append(text(52, 312 + i * 19, 14.5, ln, "#e8e8f0", "500", italic=True))
    return svg_doc(W, H, "".join(b), defs)


# --------------------------------------------------------------------------
# Tela inicial
# --------------------------------------------------------------------------
def title_screen():
    defs = lingrad("titlebg", [(0, "#0c0c16", 1), (0.5, "#3a1860", 1), (1, "#c4263d", 1)])
    defs += radgrad("titleglow", [(0, "#ffd98a", 0.4), (1, "#ffd98a", 0)])
    b = [rect(0, 0, W, H, "url(#titlebg)")]
    b.append(circle(240, 120, 220, "url(#titleglow)"))
    # faixa de eras no topo
    for i, c in enumerate(["#f4cd5e", "#e8c552", "#e8d9b0", "#ffd23f", "#ff2bd6"]):
        b.append(rect(i * (W / 5), 0, W / 5, 8, c, opacity=0.95))
    # selos das 5 eras na base
    for i, cx in enumerate([78, 168, 258, 348, 420]):
        b.append(motif_icon(i + 1, cx, 296, 30))
        b.append(circle(cx, 296, 30, "none", stroke="#ffffff", sw=1, opacity=0.3))
    b.append(text(240, 124, 40, "A DUPLA DAS ARTES", "#ffffff", "900", "middle", font=FONT_TITLE))
    b.append(text(240, 124, 40, "A DUPLA DAS ARTES", "none", "900", "middle", font=FONT_TITLE))
    b.append(text(240, 156, 16, "Uma aventura pela história da arte", "#ffd98a", "600", "middle", italic=True))
    b.append(text(240, 232, 13, "Theo & Lia  •  5 eras  •  20 relíquias", "#ffffff", "700", "middle", opacity=0.85))
    b.append(text(240, 252, 12.5, "Theo: W A D     Lia: ← → setas", "#ffffff", "700", "middle", opacity=0.8))
    b.append(text(240, 270, 12, "ESPAÇO: os dois pulam juntos!", "#ffd98a", "700", "middle", opacity=0.85))
    return svg_doc(W, H, "".join(b), defs)


# --------------------------------------------------------------------------
# Tela de vitoria
# --------------------------------------------------------------------------
def victory_screen():
    defs = lingrad("vicbg", [(0, "#0c0c16", 1), (0.45, "#5b2168", 1), (1, "#1fb6c9", 1)])
    defs += radgrad("vicglow", [(0, "#ffe9a8", 0.6), (1, "#ffe9a8", 0)])
    b = [rect(0, 0, W, H, "url(#vicbg)")]
    b.append(circle(240, 110, 180, "url(#vicglow)"))
    # arco de selos
    for i in range(5):
        ang = -60 + i * 30
        cx = 240 + 150 * math.sin(math.radians(ang))
        cy = 96 - 36 * math.cos(math.radians(ang))
        b.append(motif_icon(i + 1, cx, cy, 26))
    # confete
    import random
    rnd = random.Random(7)
    for _ in range(40):
        x, y = rnd.randint(10, 470), rnd.randint(150, 350)
        c = rnd.choice(["#ffd23f", "#ff2bd6", "#39ff14", "#00e5ff", "#f4cd5e"])
        b.append(rect(x, y, 5, 8, c, opacity=0.8))
    b.append(text(240, 196, 36, "MUSEU COMPLETO!", "#ffffff", "900", "middle", font=FONT_TITLE))
    b.append(text(240, 226, 15, "Theo e Lia percorreram toda a história da arte!", "#fff3cf", "600", "middle"))
    b.append(text(240, 262, 12.5, "Antiga → Medieval → Cubismo → Moderna → Contemporânea", "#e8e8f0", "700", "middle"))
    b.append(rect(240 - 120, 286, 240, 40, "#000", rx=20, opacity=0.35))
    b.append(text(240, 312, 16, "Bandeira verde para jogar de novo", "#ffe9a8", "700", "middle"))
    return svg_doc(W, H, "".join(b), defs)


def stage_backdrops():
    """Ordem (indices 1..12):
    1 Tela Inicial | 2..6 Intro 1..5 | 7..11 Fase 1..5 | 12 Vitoria"""
    import art_backdrops
    out = [("Tela Inicial", title_screen())]
    for p in PHASES:
        out.append((f"Intro {p['num']} - {p['title']}", intro_screen(p)))
    for p in PHASES:
        out.append((f"Fase {p['num']} - {p['title']}", art_backdrops.BG_FUNCS[p["num"]]()))
    out.append(("Vitoria", victory_screen()))
    return out


if __name__ == "__main__":
    import cairosvg
    import os
    os.makedirs("/home/user/Scratch-code-/preview", exist_ok=True)
    for name, svg in [("titulo", title_screen()), ("vitoria", victory_screen())] + \
            [(f"intro{p['num']}", intro_screen(p)) for p in PHASES]:
        cairosvg.svg2png(bytestring=svg.encode(),
                         write_to=f"/home/user/Scratch-code-/preview/{name}.png",
                         output_width=W, output_height=H)
    print("intro/title/victory ok")
