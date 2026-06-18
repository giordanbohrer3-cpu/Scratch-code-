# -*- coding: utf-8 -*-
"""phases.py - Configuração das 5 fases (ordem cronológica da história da arte),
textos educativos, paletas e o LAYOUT do platformer (chão, obstáculos, itens,
portas e posições de início).

Coordenadas do jogo = sistema do Scratch (centro 0,0; x->dir; y->cima).
Palco: x [-240,240], y [-180,180].
"""

STAGE_W, STAGE_H = 480, 360

# Superfície do chão (topo do piso). Os personagens andam sobre y = -120.
GROUND_Y = -120
GY = GROUND_Y

# Posições de início (logo acima do chão; a gravidade assenta).
SPAWN_THEO = (-205, -90)
SPAWN_LIA = (-171, -90)

# Constantes de física do platformer.
WALK = 4
JUMP = 14
GRAV = 1
VY_MIN = -12
PLAYER_XMIN = -232
PLAYER_XMAX = 216   # encosta os dois no portal duplo do fim da fase

# Portal duplo no fim da fase, apoiado no chão (par adjacente).
DOOR_THEO = (188, -100)
DOOR_LIA = (214, -100)

# Deslocamento vertical para o item "pousar" sobre a superfície (sobe do centro).
ITEM_RISE = 16

# Até 3 obstáculos por fase (slots de colisão).
MAX_OBST = 3


def _ob(cx, w, h, kind):
    return {"cx": cx, "w": w, "h": h, "kind": kind,
            "x0": cx - w / 2, "x1": cx + w / 2, "top": GY + h}


# LAYOUTS estilo Super Mario Bros - posições MUDAM a cada fase (tudo solucionável:
# obstáculos com altura <= 52 (o pulo limpa) e itens no chão ou no topo deles).
# kind: "pipe" (cano verde) | "blocks" (tijolos + bloco-?).
LAYOUTS = {
    1: {"obstacles": [_ob(-40, 36, 44, "pipe"), _ob(72, 34, 50, "blocks")],
        "items": [(-135, GY), (-40, GY + 44), (20, GY), (72, GY + 50)]},
    2: {"obstacles": [_ob(-78, 34, 40, "blocks"), _ob(30, 36, 50, "pipe"), _ob(124, 34, 44, "blocks")],
        "items": [(-150, GY), (-78, GY + 40), (30, GY + 50), (124, GY + 44)]},
    3: {"obstacles": [_ob(-62, 36, 48, "pipe"), _ob(66, 34, 44, "blocks")],
        "items": [(-140, GY), (-62, GY + 48), (12, GY), (66, GY + 44)]},
    4: {"obstacles": [_ob(-32, 34, 46, "blocks"), _ob(54, 36, 52, "pipe"), _ob(134, 34, 40, "blocks")],
        "items": [(-150, GY), (-32, GY + 46), (54, GY + 52), (134, GY + 40)]},
    5: {"obstacles": [_ob(-52, 36, 50, "pipe"), _ob(42, 34, 44, "blocks"), _ob(126, 36, 48, "pipe")],
        "items": [(-146, GY), (-52, GY + 50), (42, GY + 44), (126, GY + 48)]},
}


def obstacles(num):  return LAYOUTS[num]["obstacles"]
def items(num):      return LAYOUTS[num]["items"]


def _layout(*a, **k):   # compat: PHASES ainda traz a chave "layout" (não usada)
    return None



# --------------------------------------------------------------------------
# As 5 fases. num = ordem cronológica.
# accent: cor de destaque da era. sky_top/sky_bot: gradiente do fundo.
# palette: tons usados na arte daquela era.
# relics: nomes das 4 relíquias (também viram os "nomes" educativos).
# --------------------------------------------------------------------------
PHASES = [
    {
        "num": 1,
        "key": "antiga",
        "title": "Arte Antiga",
        "subtitle": "Egito, Grécia e Roma",
        "period": "3000 a.C. — 476 d.C.",
        "objective": "Recolha as 4 relíquias antigas e leve Theo e Lia até os portais dourados.",
        "fact": "No Egito as figuras eram pintadas de perfil, e o ouro honrava os deuses e faraós.",
        "accent": "#f4cd5e",  # dourado
        "sky_top": "#1b1206", "sky_bot": "#d9a85c",
        "ground_top": "#b07a3c", "ground_bot": "#6e4a22", "ground_edge": "#e7c98c",
        "obstacle_main": "#caa468", "obstacle_dark": "#7a5226", "obstacle_light": "#f1dba8",
        "palette": ["#e7c98c", "#caa468", "#8a5a2e", "#6b4422", "#f1dba8", "#3a2410"],
        "relics": ["Ânfora Grega", "Coluna Jônica", "Máscara de Ouro", "Vaso Canopo"],
        "layout": _layout(46, 56),
    },
    {
        "num": 2,
        "key": "medieval",
        "title": "Arte Medieval",
        "subtitle": "Catedrais e Vitrais",
        "period": "Séc. V — XV",
        "objective": "Reúna os 4 tesouros medievais e conduza a dupla até os portais.",
        "fact": "Os vitrais góticos contavam histórias da Bíblia usando luz colorida nas catedrais.",
        "accent": "#e8c552",
        "sky_top": "#070a1c", "sky_bot": "#3a4f8f",
        "ground_top": "#6d6f86", "ground_bot": "#3a3c52", "ground_edge": "#9aa0c4",
        "obstacle_main": "#5a5d78", "obstacle_dark": "#2c2e44", "obstacle_light": "#9aa0c4",
        "palette": ["#7c2dd6", "#1fb6c9", "#e8c552", "#c0234f", "#2c2e44", "#9aa0c4"],
        "relics": ["Vitral Rosácea", "Cálice Sagrado", "Pergaminho", "Escudo Brasonado"],
        "layout": _layout(50, 58),
    },
    {
        "num": 3,
        "key": "cubismo",
        "title": "Cubismo",
        "subtitle": "Picasso e Braque",
        "period": "1907 — 1920",
        "objective": "Junte as 4 formas cubistas e leve Theo e Lia até os portais.",
        "fact": "O Cubismo mostra o mesmo objeto de vários ângulos ao mesmo tempo, em facetas.",
        "accent": "#e8d9b0",
        "sky_top": "#2a2118", "sky_bot": "#b3955f",
        "ground_top": "#9a8156", "ground_bot": "#5c4a35", "ground_edge": "#e8d9b0",
        "obstacle_main": "#8a7355", "obstacle_dark": "#3a2f20", "obstacle_light": "#e8d9b0",
        "palette": ["#8a7355", "#cdb285", "#5c4a35", "#e8d9b0", "#6f5b3e", "#3a2f20"],
        "relics": ["Violão Cubista", "Rosto Facetado", "Cubo Analítico", "Jornal Colado"],
        "layout": _layout(48, 54),
    },
    {
        "num": 4,
        "key": "moderna",
        "title": "Arte Moderna",
        "subtitle": "Sonhos e Cores Livres",
        "period": "1860 — 1970",
        "objective": "Colete as 4 obras modernas e leve a dupla até os portais.",
        "fact": "Os modernos pintavam emoções, sonhos e cores livres — não apenas a realidade.",
        "accent": "#ffd23f",
        "sky_top": "#1a1033", "sky_bot": "#c4263d",
        "ground_top": "#6b3f7a", "ground_bot": "#3a1d4a", "ground_edge": "#ffd23f",
        "obstacle_main": "#7e4a8f", "obstacle_dark": "#2a153a", "obstacle_light": "#ffd23f",
        "palette": ["#ffd23f", "#1fb6c9", "#ff6f59", "#c4263d", "#5b2168", "#f4f1ea"],
        "relics": ["Relógio Derretido", "Girassol", "Bloco Mondrian", "Noite Estrelada"],
        "layout": _layout(46, 58),
    },
    {
        "num": 5,
        "key": "contemporanea",
        "title": "Arte Contemporânea",
        "subtitle": "Pop Art e Grafite",
        "period": "1970 — hoje",
        "objective": "Recolha os 4 ícones contemporâneos e alcance os portais neon.",
        "fact": "A Pop Art transformou quadrinhos e latas de sopa em arte cheia de cor!",
        "accent": "#ff2bd6",
        "sky_top": "#0d0d12", "sky_bot": "#2a0d33",
        "ground_top": "#2b2b3a", "ground_bot": "#141420", "ground_edge": "#39ff14",
        "obstacle_main": "#23232f", "obstacle_dark": "#0c0c14", "obstacle_light": "#00e5ff",
        "palette": ["#ff2bd6", "#00e5ff", "#39ff14", "#ffe34d", "#16121c", "#f4f1ea"],
        "relics": ["Balão POP", "Lata Pop Art", "Spray de Grafite", "Coração Neon"],
        "layout": _layout(48, 56),
    },
]
# Posição (Scratch x,y) do "Astro" animado em cada fase, escolhida para
# complementar o elemento celeste do fundo (sem duplicar de forma estranha).
ASTRO_POS = {
    1: (132, 86),    # sobre o sol do Egito -> sol animado
    2: (168, 122),   # sobre a lua da catedral -> lua animada
    3: (164, 104),   # sobre o sol geométrico do cubismo
    4: (132, 104),   # lado direito (as espirais do fundo ficam à esquerda)
    5: (140, 108),   # lado direito (o "POP" do fundo fica à esquerda)
}

PHASE_BY_NUM = {p["num"]: p for p in PHASES}
