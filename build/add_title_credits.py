# -*- coding: utf-8 -*-
"""add_title_credits.py — Acrescenta os créditos acadêmicos (instituição/projeto,
grupo, integrantes e o objeto de aprendizagem) APENAS no cenário da tela inicial
('Tela Inicial'). Nada mais é tocado: nenhum outro ator, bloco ou cenário muda.

Os textos entram no MESMO grupo de coordenadas do palco (0..480 x 0..360), num
cartão translúcido logo acima do botão COMEÇAR e numa legenda de rodapé.

Uso: python3 add_title_credits.py entrada.sb3 saida.sb3
"""
import sys, re, json, hashlib, zipfile


def txt(x, y, size, fill, weight, s, op=1.0):
    fo = f' fill-opacity="{op}"' if op != 1.0 else ""
    return (f'<text transform="translate({x},{y})" font-size="{size}" xml:space="preserve" '
            f'fill="{fill}"{fo} fill-rule="nonzero" stroke="none" stroke-width="1" '
            f'stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" '
            f'stroke-dasharray="" stroke-dashoffset="0" font-family="Sans Serif" '
            f'font-weight="{weight}" text-anchor="middle" style="mix-blend-mode: normal">'
            f'<tspan x="0" dy="0">{s}</tspan></text>')


def rrect(x, y, w, h, r, fill, fop, stroke="none", sop=0.0, sw=0):
    d = (f"M{x+r},{y} h{w-2*r} a{r},{r} 0 0 1 {r},{r} v{h-2*r} a{r},{r} 0 0 1 {-r},{r} "
         f"h{-(w-2*r)} a{r},{r} 0 0 1 {-r},{-r} v{-(h-2*r)} a{r},{r} 0 0 1 {r},{-r} z")
    sattr = (f' stroke="{stroke}" stroke-opacity="{sop}" stroke-width="{sw}" '
             f'stroke-linejoin="round"') if sw else ' stroke="none"'
    return f'<path d="{d}" fill="{fill}" fill-opacity="{fop}"{sattr}></path>'


def credits_snippet():
    s = ""
    # cartão de créditos, na faixa livre logo acima do botão COMEÇAR
    s += rrect(54, 119, 372, 42, 11, "#0b0b14", 0.60, "#ffd98a", 0.55, 1.2)
    s += txt(240, 131, 8.5, "#ffd98a", 800, "PROJETO INTEGRADOR  ·  UNIJUÍ")
    s += txt(240, 145, 11.5, "#ffffff", 800, "Grupo QuantumDev")
    s += txt(240, 156, 8, "#ffffff", 600,
             "Giordan Bohrer · Eduardo Palaese · João Gabriel · Poliana Pautz", op=0.9)
    # legenda do objeto de aprendizagem no rodapé (abaixo dos selos das eras)
    s += rrect(97, 342, 286, 20, 10, "#000000", 0.34)
    s += txt(240, 355.5, 9, "#ffe9b0", 700, "Objeto de Aprendizagem: A Dupla das Artes")
    return s


def inject(svg):
    # embrulha os créditos no MESMO translate do grupo de conteúdo, antes de </svg>,
    # para que as coordenadas do palco (0..480 x 0..360) fiquem corretas.
    m = re.search(r'<g transform="(translate\([^"]*\))"', svg)
    tf = m.group(1) if m else "translate(0,0)"
    wrap = f'<g transform="{tf}">{credits_snippet()}</g>'
    i = svg.rfind("</svg>")
    return svg[:i] + wrap + svg[i:]


def main(inp, outp):
    src = zipfile.ZipFile(inp)
    proj = json.loads(src.read("project.json"))
    stage = next(t for t in proj["targets"] if t["isStage"])
    cos = next(c for c in stage["costumes"] if c["name"] == "Tela Inicial")
    old = cos["md5ext"]

    new_svg = inject(src.read(old).decode("utf-8")).encode("utf-8")
    new_md5 = hashlib.md5(new_svg).hexdigest()
    cos["assetId"] = new_md5
    cos["md5ext"] = new_md5 + ".svg"

    # o SVG antigo ainda é usado por algum outro fantasia? (não deveria)
    still_used = any(c.get("md5ext") == old
                     for t in proj["targets"] for c in t.get("costumes", []))

    with zipfile.ZipFile(outp, "w", zipfile.ZIP_DEFLATED) as out:
        out.writestr("project.json", json.dumps(proj, ensure_ascii=False))
        for n in src.namelist():
            if n == "project.json":
                continue
            if n == old and not still_used:
                continue                      # remove o SVG antigo da capa
            out.writestr(n, src.read(n))
        out.writestr(cos["md5ext"], new_svg)  # adiciona a capa nova
    src.close()
    print(f"OK -> {outp}")
    print(f"tela inicial: {old} -> {cos['md5ext']}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
