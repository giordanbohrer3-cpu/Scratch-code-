# -*- coding: utf-8 -*-
"""art_doors.py - Portais de saída de Theo e Lia. Apoiados no chão (não flutuam).
Canvas 44x64, centro de rotação (22, 40) -> base do portal encosta no chão.
"""
from svg_core import *

CW, CH = 44, 64
ROT = (22, 40)   # base ~ y=58


def _door(panel, panel2, accent, emblem):
    gid = "dr_" + panel.strip("#")
    defs = lingrad(gid, [(0, panel2, 1), (1, panel, 1)])
    defs += radgrad("dglow_" + panel.strip("#"), [(0, accent, 0.6), (1, accent, 0)])
    b = []
    # halo
    b.append(circle(22, 26, 26, f"url(#dglow_{panel.strip('#')})"))
    # moldura de pedra dourada (arco)
    b.append(path("M6 58 L6 24 Q6 6 22 6 Q38 6 38 24 L38 58 Z", fill="#caa055"))
    b.append(path("M6 58 L6 24 Q6 6 22 6 Q38 6 38 24 L38 58 Z", fill="none", stroke="#8a6a2e", sw=2))
    # batente interno
    b.append(path("M10 58 L10 25 Q10 11 22 11 Q34 11 34 25 L34 58 Z", fill="#6e4a22"))
    # porta (painel colorido)
    b.append(path(f"M13 58 L13 26 Q13 14 22 14 Q31 14 31 26 L31 58 Z", fill=f"url(#{gid})"))
    b.append(path("M22 14 L22 58", stroke=accent, sw=1, opacity=0.4))
    # tachas
    for yy in (22, 32, 42, 52):
        b.append(circle(17, yy, 1.2, accent, 0.8)); b.append(circle(27, yy, 1.2, accent, 0.8))
    # emblema central
    b.extend(emblem)
    # maçaneta
    b.append(circle(28, 40, 1.8, "#ffe9a8"))
    # degrau na base
    b.append(rect(4, 56, 36, 5, "#8a6a2e", rx=1))
    b.append(rect(4, 56, 36, 2, "#caa055", rx=1, opacity=0.8))
    # topo ornamental
    b.append(circle(22, 6, 3, accent))
    b.append(star4(22, 6, 3.2, "#fff", 0.5))
    return svg_doc(CW, CH, "".join(b), defs)


def porta_theo():
    # emblema: pincel branco em círculo azul
    em = [circle(22, 33, 7, "#0b2a66"),
          line(20, 37, 25, 28, "#f5f5f5", 2.2),
          circle(25, 27, 2, "#f97316"),
          circle(22, 33, 7, "none", stroke="#bcd4ff", sw=1)]
    return _door("#1d4ed8", "#3b82f6", "#bcd4ff", em)


def porta_lia():
    # emblema: paleta em círculo turquesa
    em = [circle(22, 33, 7, "#0b423d"),
          ellipse(22, 33, 5, 4, "#caa06a"),
          circle(20, 32, 1.1, "#c0234f"), circle(24, 32, 1.1, "#1fb6c9"),
          circle(22, 35, 1.1, "#ffd23f"),
          circle(22, 33, 7, "none", stroke="#9af0e4", sw=1)]
    return _door("#0d9488", "#2dd4bf", "#9af0e4", em)


def doors():
    return [("Porta Theo", porta_theo()), ("Porta Lia", porta_lia())]


if __name__ == "__main__":
    import cairosvg, os
    os.makedirs("/home/user/Scratch-code-/preview", exist_ok=True)
    for name, svg in doors():
        cairosvg.svg2png(bytestring=svg.encode(),
                         write_to=f"/home/user/Scratch-code-/preview/door_{name}.png",
                         output_width=CW*4, output_height=CH*4)
    print("doors ok")
