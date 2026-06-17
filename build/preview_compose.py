# -*- coding: utf-8 -*-
"""Compoe uma cena completa por fase (fundo + chao + obstaculos + portas +
itens + personagens) para validar layout e arte ANTES de montar o .sb3."""
import cairosvg, io, os
from PIL import Image
from phases import (PHASES, GROUND_Y, SPAWN_THEO, SPAWN_LIA, DOOR_THEO, DOOR_LIA, ITEM_RISE)
import art_backdrops, art_floor, art_items, art_doors, art_chars

PREV = "/home/user/Scratch-code-/preview"
os.makedirs(PREV, exist_ok=True)


def render(svg, w, h):
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=w, output_height=h)
    return Image.open(io.BytesIO(png)).convert("RGBA")


def to_svg(sx, sy):   # scratch -> svg px
    return (sx + 240, 180 - sy)


def paste_center(base, img, sx, sy, rot_cx, rot_cy):
    """Cola img com seu centro de rotacao (rot_cx,rot_cy) na posicao scratch."""
    vx, vy = to_svg(sx, sy)
    base.alpha_composite(img, (int(vx - rot_cx), int(vy - rot_cy)))


def compose_phase(p):
    base = render(art_backdrops.BG_FUNCS[p["num"]](), 480, 360)
    base.alpha_composite(render(art_floor.ground_costume(p), 480, 360), (0, 0))
    base.alpha_composite(render(art_floor.obstacle_costume(p), 480, 360), (0, 0))
    # portas
    dt = render(art_doors.porta_theo(), art_doors.CW, art_doors.CH)
    dl = render(art_doors.porta_lia(), art_doors.CW, art_doors.CH)
    paste_center(base, dt, *DOOR_THEO, *art_doors.ROT)
    paste_center(base, dl, *DOOR_LIA, *art_doors.ROT)
    # itens
    item_imgs = [render(art_items.RELIC_FUNCS[p["num"]][i](), 48, 48) for i in range(4)]
    for (cx, surf), img in zip(p["layout"]["items"], item_imgs):
        paste_center(base, img, cx, surf + ITEM_RISE, 24, 24)
    # personagens (pes no chao)
    theo = render(art_chars.theo_costumes()[0][1], 48, 60)
    lia = render(art_chars.lia_costumes()[0][1], 48, 60)
    foot_to_center = 27   # pes ~ y57, centro y30
    paste_center(base, theo, SPAWN_THEO[0], GROUND_Y + foot_to_center, 24, 30)
    paste_center(base, lia, SPAWN_LIA[0], GROUND_Y + foot_to_center, 24, 30)
    return base


if __name__ == "__main__":
    sheet = Image.new("RGB", (480, 360 * 5 + 20), (30, 30, 36))
    for i, p in enumerate(PHASES):
        img = compose_phase(p)
        img.convert("RGB").save(f"{PREV}/scene_{p['num']}_{p['key']}.png")
        sheet.paste(img.convert("RGB"), (0, i * 364))
    sheet.save(f"{PREV}/_scenes_all.png")
    print("scenes ok")
