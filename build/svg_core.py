# -*- coding: utf-8 -*-
"""svg_core.py - Pequena biblioteca para gerar SVG limpo e compatível com o
renderizador do Scratch (sem <filter>, sem fontes externas).

Sistema de coordenadas do SVG: origem no topo-esquerda, x->direita, y->baixo.
Tamanho padrão do palco do Scratch: 480 x 360.
"""
from __future__ import annotations
import math

# Fontes embutidas no Scratch (garantem render no player online):
#   "Sans Serif", "Serif", "Handwriting", "Marker", "Curly", "Pixel", "Scratch"
FONT_BODY = "Sans Serif"
FONT_TITLE = "Marker"


def _f(v):
    """Formata número curtinho (sem casas decimais inúteis)."""
    if isinstance(v, (int,)):
        return str(v)
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return s if s not in ("-0", "") else "0"


# --------------------------------------------------------------------------
# Gradientes (devolvem string para por dentro de <defs>)
# --------------------------------------------------------------------------
def lingrad(gid, stops, x1=0, y1=0, x2=0, y2=1):
    """Gradiente linear. stops = [(offset, cor, opacidade), ...]"""
    s = [f'<linearGradient id="{gid}" x1="{_f(x1)}" y1="{_f(y1)}" x2="{_f(x2)}" y2="{_f(y2)}">']
    for off, col, op in stops:
        s.append(f'<stop offset="{_f(off)}" stop-color="{col}" stop-opacity="{_f(op)}"/>')
    s.append('</linearGradient>')
    return "".join(s)


def radgrad(gid, stops, cx=0.5, cy=0.5, r=0.5):
    s = [f'<radialGradient id="{gid}" cx="{_f(cx)}" cy="{_f(cy)}" r="{_f(r)}">']
    for off, col, op in stops:
        s.append(f'<stop offset="{_f(off)}" stop-color="{col}" stop-opacity="{_f(op)}"/>')
    s.append('</radialGradient>')
    return "".join(s)


# --------------------------------------------------------------------------
# Formas
# --------------------------------------------------------------------------
def rect(x, y, w, h, fill, rx=0, opacity=1.0, stroke=None, sw=0):
    a = f'<rect x="{_f(x)}" y="{_f(y)}" width="{_f(w)}" height="{_f(h)}"'
    if rx: a += f' rx="{_f(rx)}" ry="{_f(rx)}"'
    a += f' fill="{fill}"'
    if opacity != 1.0: a += f' fill-opacity="{_f(opacity)}"'
    if stroke: a += f' stroke="{stroke}" stroke-width="{_f(sw)}"'
    return a + '/>'


def circle(cx, cy, r, fill, opacity=1.0, stroke=None, sw=0):
    a = f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="{_f(r)}" fill="{fill}"'
    if opacity != 1.0: a += f' fill-opacity="{_f(opacity)}"'
    if stroke: a += f' stroke="{stroke}" stroke-width="{_f(sw)}"'
    return a + '/>'


def ellipse(cx, cy, rx, ry, fill, opacity=1.0, stroke=None, sw=0):
    a = f'<ellipse cx="{_f(cx)}" cy="{_f(cy)}" rx="{_f(rx)}" ry="{_f(ry)}" fill="{fill}"'
    if opacity != 1.0: a += f' fill-opacity="{_f(opacity)}"'
    if stroke: a += f' stroke="{stroke}" stroke-width="{_f(sw)}"'
    return a + '/>'


def poly(points, fill, opacity=1.0, stroke=None, sw=0, closed=True):
    pts = " ".join(f"{_f(x)},{_f(y)}" for x, y in points)
    tag = "polygon" if closed else "polyline"
    a = f'<{tag} points="{pts}"'
    a += f' fill="{fill}"' if (closed and fill) else ' fill="none"'
    if opacity != 1.0: a += f' fill-opacity="{_f(opacity)}"'
    if stroke: a += f' stroke="{stroke}" stroke-width="{_f(sw)}" stroke-linejoin="round"'
    return a + '/>'


def path(d, fill="none", stroke=None, sw=0, opacity=1.0, cap="round", join="round", dash=None):
    a = f'<path d="{d}"'
    a += f' fill="{fill}"'
    if fill != "none" and opacity != 1.0: a += f' fill-opacity="{_f(opacity)}"'
    if stroke:
        a += f' stroke="{stroke}" stroke-width="{_f(sw)}" stroke-linecap="{cap}" stroke-linejoin="{join}"'
        if fill == "none" and opacity != 1.0: a += f' stroke-opacity="{_f(opacity)}"'
        if dash: a += f' stroke-dasharray="{dash}"'
    return a + '/>'


def line(x1, y1, x2, y2, stroke, sw=1, opacity=1.0, cap="round", dash=None):
    a = (f'<line x1="{_f(x1)}" y1="{_f(y1)}" x2="{_f(x2)}" y2="{_f(y2)}"'
         f' stroke="{stroke}" stroke-width="{_f(sw)}" stroke-linecap="{cap}"')
    if opacity != 1.0: a += f' stroke-opacity="{_f(opacity)}"'
    if dash: a += f' stroke-dasharray="{dash}"'
    return a + '/>'


def text(x, y, size, content, fill, weight="700", anchor="start",
         italic=False, font=FONT_BODY, opacity=1.0, spacing=None):
    esc = (content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    a = (f'<text x="{_f(x)}" y="{_f(y)}" font-family="{font}" font-size="{_f(size)}"'
         f' font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"')
    if italic: a += ' font-style="italic"'
    if opacity != 1.0: a += f' fill-opacity="{_f(opacity)}"'
    if spacing is not None: a += f' letter-spacing="{_f(spacing)}"'
    return a + f'>{esc}</text>'


def group(inner, transform=None, opacity=1.0):
    a = '<g'
    if transform: a += f' transform="{transform}"'
    if opacity != 1.0: a += f' opacity="{_f(opacity)}"'
    return a + f'>{inner}</g>'


# --------------------------------------------------------------------------
# Formas compostas úteis
# --------------------------------------------------------------------------
def star(cx, cy, r_out, r_in, points, fill, opacity=1.0, rot=-90, stroke=None, sw=0):
    pts = []
    for i in range(points * 2):
        rr = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180.0 / points)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return poly(pts, fill, opacity, stroke, sw)


def star4(cx, cy, r, fill, opacity=1.0):
    """Estrela de 4 pontas (estilo cômic/pop)."""
    k = r * 0.36
    pts = [(cx, cy - r), (cx + k, cy - k), (cx + r, cy), (cx + k, cy + k),
           (cx, cy + r), (cx - k, cy + k), (cx - r, cy), (cx - k, cy - k)]
    return poly(pts, fill, opacity)


def burst(cx, cy, r, spikes, fill, opacity=1.0, inner=0.62):
    return star(cx, cy, r, r * inner, spikes, fill, opacity)


def ring(cx, cy, r, stroke, sw, opacity=1.0, dash=None):
    return circle(cx, cy, r, "none", 1.0, stroke, sw) if not dash else \
        f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="{_f(r)}" fill="none" stroke="{stroke}" stroke-width="{_f(sw)}" stroke-dasharray="{dash}" stroke-opacity="{_f(opacity)}"/>'


def rounded_panel(x, y, w, h, fill, rx, opacity=1.0, stroke=None, sw=0):
    return rect(x, y, w, h, fill, rx, opacity, stroke, sw)


def arc_path(cx, cy, r, a0, a1):
    """Caminho de arco (graus)."""
    x0 = cx + r * math.cos(math.radians(a0)); y0 = cy + r * math.sin(math.radians(a0))
    x1 = cx + r * math.cos(math.radians(a1)); y1 = cy + r * math.sin(math.radians(a1))
    large = 1 if abs(a1 - a0) > 180 else 0
    return f"M{_f(x0)} {_f(y0)} A{_f(r)} {_f(r)} 0 {large} 1 {_f(x1)} {_f(y1)}"


# --------------------------------------------------------------------------
# Documento
# --------------------------------------------------------------------------
def svg_doc(w, h, body, defs="", extra_attr=""):
    d = f'<defs>{defs}</defs>' if defs else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{_f(w)}" height="{_f(h)}" '
            f'viewBox="0 0 {_f(w)} {_f(h)}"{(" " + extra_attr) if extra_attr else ""}>'
            f'{d}{body}</svg>')


# Conversão de coordenadas SVG (480x360, topo-esq) -> Scratch (centro, y p/ cima)
def to_scratch(svg_x, svg_y, W=480, H=360):
    return (svg_x - W / 2.0, H / 2.0 - svg_y)


def from_scratch(sx, sy, W=480, H=360):
    return (sx + W / 2.0, H / 2.0 - sy)
