# -*- coding: utf-8 -*-
"""build_project.py - Monta o jogo completo "A Dupla das Artes" em .sb3.

Plataforma estilo Fogo & Água / Mario:
  - física com gravidade, pulo e colisão por matemática (chão + obstáculos)
  - controles separados: Theo = WASD, Lia = setas; ESPAÇO = os dois pulam
  - 5 fases em ordem cronológica, cada uma com tela animada de 7s
  - chão/obstáculos por fase, fundo animado (astro + partículas), rótulo da era
  - coletáveis, portas no chão, animações de coleta / porta / fim de fase
"""
from sb3lib import *
from svg_core import circle
import art_backdrops, art_intro, art_floor, art_items, art_chars, art_doors, art_ui, art_fx
from phases import (PHASES, GROUND_Y, SPAWN_THEO, SPAWN_LIA,
                    WALK, JUMP, GRAV, VY_MIN, PLAYER_XMIN, PLAYER_XMAX,
                    obstacles, platforms, items, door_theo, door_lia,
                    MAX_OBST, MAX_PLAT, ITEM_RISE, ASTRO_POS)

# ---- Geometria de colisão (em coordenadas do Scratch) ----------------------
# Colisão por matemática (retângulos). Cada fase tem ATÉ 3 obstáculos cujas
# coordenadas o Diretor grava em variáveis (mudam por fase). A arte (Chão/
# Obstáculo) é desenhada exatamente sobre esses retângulos.
GY = GROUND_Y                 # topo do chão (superfície)
FOOT = 26                     # distância do centro do personagem até os pés
HW = 12                       # meia-largura do corpo
ITEM_R2 = 40 * 40             # raio² de coleta (pega ao pular por cima)
DOOR_R2 = 34 * 34             # raio² para o personagem estar "na porta"
# variáveis dos 3 slots de obstáculo SÓLIDO e 6 de plataforma (one-way): (x0,x1,topo)
OBV = [("o1x0", "o1x1", "o1t"), ("o2x0", "o2x1", "o2t"), ("o3x0", "o3x1", "o3t")]
QV = [(f"q{i}x0", f"q{i}x1", f"q{i}t") for i in range(1, MAX_PLAT + 1)]


def ov_xv(x0v, x1v):          # corpo do jogador cruza a faixa [x0,x1] (variáveis)?
    return and_(gt(add(xpos(), HW), var(x0v)), lt(sub(xpos(), HW), var(x1v)))


def intro_name(p): return f"Intro {p['num']} - {p['title']}"
def fase_name(p):  return f"Fase {p['num']} - {p['title']}"


# expressões reutilizáveis -------------------------------------------------
def playing():   return eq(var("modo"), 2)
def in_phase():  return and_(gt(var("fase"), 0), lt(var("fase"), 6))
def visible_phase():  # durante jogo ou transição
    return and_(in_phase(), or_(eq(var("modo"), 2), eq(var("modo"), 3)))
def pulse(base, amp, speed):
    return add(base, mul(amp, mathop("sin", mul(timer(), speed))))
def sq(v):       return mul(v, v)
def overlap_x(x0, x1):   # corpo do jogador cruza a faixa [x0,x1]?
    return and_(gt(add(xpos(), HW), x0), lt(sub(xpos(), HW), x1))


# ===========================================================================
def build():
    P = Project()
    # ---- variáveis globais ----
    for v in ["fase", "modo", "Pontos", "Relíquias",
              "item1", "item2", "item3", "item4", "Theo_ok", "Lia_ok", "intro_n",
              "vy_theo", "no_theo", "passo_theo", "dx_theo", "pf_theo", "sf_theo",
              "vy_lia", "no_lia", "passo_lia", "dx_lia", "pf_lia", "sf_lia",
              "o1x0", "o1x1", "o1t", "o2x0", "o2x1", "o2t", "o3x0", "o3x1", "o3t",
              "dtx", "dty", "dlx", "dly", "cadT", "cadL"]:
        P.add_var(v, 0)
    for (x0, x1, t) in QV:
        P.add_var(x0, 9999); P.add_var(x1, 9999); P.add_var(t, -999)
    # ---- broadcasts ----
    for m in ["comecar", "carregar_fase", "jogar", "entrar_porta",
              "fase_completa", "banner_fim", "vitoria"]:
        P.add_broadcast(m)

    # =====================================================================
    # STAGE (backdrops)
    # =====================================================================
    st = P.stage
    st.add_costume("Tela Inicial", art_intro.title_screen(), 240, 180)
    for p in PHASES:
        st.add_costume(intro_name(p), art_intro.intro_screen(p), 240, 180)
    for p in PHASES:
        st.add_costume(fase_name(p), art_backdrops.BG_FUNCS[p["num"]](), 240, 180)
    st.add_costume("Vitoria", art_intro.victory_screen(), 240, 180)
    st.current_costume = 0
    # o Stage não precisa de scripts (o Diretor controla tudo)

    # =====================================================================
    # CHÃO  (piso marrom por fase)
    # =====================================================================
    chao = Target("Chao")
    for name, svg in art_floor.ground_all():
        chao.add_costume(name, svg, 240, 180)
    chao.x, chao.y, chao.layer = 0, 0, 3
    chao.script(
        on_flag(), goto_xy(0, 0), set_size(100),
        forever([
            if_else(visible_phase(),
                    [switch_costume(var("fase")), goto_xy(0, 0), show()],
                    [hide()]),
        ]),
    )
    P.add_sprite(chao)

    # =====================================================================
    # OBSTÁCULO (blocos para pular por cima)
    # =====================================================================
    obst = Target("Obstaculo")
    for name, svg in art_floor.obstacle_all():
        obst.add_costume(name, svg, 240, 180)
    obst.x, obst.y, obst.layer = 0, 0, 4
    obst.script(
        on_flag(), goto_xy(0, 0), set_size(100),
        forever([
            if_else(visible_phase(),
                    [switch_costume(var("fase")), goto_xy(0, 0), show()],
                    [hide()]),
        ]),
    )
    P.add_sprite(obst)

    # =====================================================================
    # PORTAS  (no chão, par adjacente no fim)
    # =====================================================================
    def make_door(name, svg, dxv, dyv, layer):
        d = Target(name)
        d.add_costume(name, svg, art_doors.ROT[0], art_doors.ROT[1])
        d.x, d.y, d.layer = 188, -100, layer
        d.visible = False
        d.script(
            on_flag(), set_size(100), hide(),
            forever([
                if_else(visible_phase(),
                        [goto_xy(var(dxv), var(dyv)),
                         set_effect("ghost", pulse(10, 8, 200)), show()],
                        [hide()]),
            ]),
        )
        return d
    P.add_sprite(make_door("Porta Theo", art_doors.porta_theo(), "dtx", "dty", 5))
    P.add_sprite(make_door("Porta Lia", art_doors.porta_lia(), "dlx", "dly", 6))

    # ---- Cadeados: trancam as portas até TODOS os itens serem coletados ----
    def make_padlock(name, dxv, dyv, cadvar, layer):
        pad = Target(name)
        for cn, svg in art_ui.padlock_all():
            pad.add_costume(cn, svg, art_ui.PADW / 2, art_ui.PADH / 2)
        pad.x, pad.y, pad.layer = 188, -70, layer
        pad.visible = False
        pad.script(
            on_flag(), hide(), set_size(100), clear_effects(),
            forever([
                if_else(visible_phase(), [
                    if_else(ge(var("Relíquias"), 4), [
                        # destrancou: abre o cadeado UMA vez, sobe e some
                        if_else(eq(var(cadvar), 0), [
                            goto_xy(var(dxv), add(var(dyv), 24)),
                            switch_costume("aberto"), clear_effects(), set_size(112), show(),
                            repeat(10, [change_y(2), change_effect("ghost", 12)]),
                            hide(), set_var(cadvar, 1),
                        ], [hide()]),
                    ], [
                        # trancado: cadeado fechado balançando sobre a porta
                        switch_costume("fechado"), clear_effects(), set_size(100),
                        goto_xy(var(dxv), add(var(dyv), add(24, mul(2, mathop("sin", mul(timer(), 200)))))),
                        show(),
                    ]),
                ], [hide()]),
            ]),
        )
        return pad
    P.add_sprite(make_padlock("CadeadoT", "dtx", "dty", "cadT", 13))
    P.add_sprite(make_padlock("CadeadoL", "dlx", "dly", "cadL", 14))

    # =====================================================================
    # OBJETOS COLETÁVEIS (4 sprites, 5 costumes cada)
    # =====================================================================
    def near(who):   # distância² do jogador até a posição ATUAL do item
        return lt(add(sq(sub(of_("x position", who), xpos())),
                      sq(sub(of_("y position", who), ypos()))), ITEM_R2)

    def owner_ring(svg, color):   # anel colorido = de quem é o item
        extra = (circle(24, 24, 22, "none", stroke=color, sw=3)
                 + circle(24, 6, 3.6, color) + circle(24, 6, 3.6, "none", stroke="#fff", sw=1))
        return svg.replace("</svg>", extra + "</svg>")

    # Theo coleta itens 1 e 2 (anel azul); Lia coleta 3 e 4 (anel rosa).
    OWN = {1: ("Theo", "#1d4ed8"), 2: ("Theo", "#1d4ed8"),
           3: ("Lia", "#db2777"), 4: ("Lia", "#db2777")}
    for slot in range(1, 5):
        owner, ocol = OWN[slot]
        ob = Target(f"Objeto{slot}")
        for name, svg in art_items.items_for_slot(slot):
            ob.add_costume(name, owner_ring(svg, ocol), 24, 24)
        ix0, surf0 = items(1)[slot - 1]
        ob.x, ob.y, ob.layer = ix0, surf0 + ITEM_RISE, 6 + slot
        ob.visible = False
        itemvar = f"item{slot}"
        # posição por fase (no chão ou no topo do obstáculo) + leve flutuação
        pos_chain = [if_(eq(var("fase"), n),
                         [goto_xy(items(n)[slot - 1][0],
                                  add(items(n)[slot - 1][1] + ITEM_RISE,
                                      mul(4, mathop("sin", mul(timer(), 170)))))])
                     for n in range(1, 6)]
        ob.script(
            on_flag(), hide(), set_size(100), clear_effects(),
            forever([
                if_else(and_(playing(), in_phase()), [
                    switch_costume(var("fase")),
                    if_else(eq(var(itemvar), 0), [
                        *pos_chain,
                        show(),
                        if_(near(owner), [        # só o DONO pega (2 itens cada)
                            set_var(itemvar, 1),
                            change_var("Pontos", 5),
                            # animação de coleta: cresce e some
                            repeat(7, [change_size(8), change_effect("ghost", 14)]),
                            hide(), set_size(100), clear_effects(),
                        ]),
                    ], [hide()]),
                ], [hide()]),
            ]),
        )
        P.add_sprite(ob)

    # =====================================================================
    # JOGADORES (Theo e Lia) - motor do platformer
    # =====================================================================
    def make_player(name, costumes, spawn, dxv, dyv, ok_var, vy, no, passo, dx, pf, sf,
                    left_key, right_key, up_key, layer):
        c_idle, c_walk, c_jump = costumes
        sp = Target(name)
        for cn, svg in (art_chars.theo_costumes() if name == "Theo" else art_chars.lia_costumes()):
            sp.add_costume(cn, svg, art_chars.ROT[0], art_chars.ROT[1])
        sp.x, sp.y = spawn
        sp.size = 100
        sp.visible = False
        sp.rotation_style = "left-right"
        sp.layer = layer

        # Controles INDIVIDUAIS: Theo = WASD, Lia = setas.
        # Pulo: ESPAÇO faz os dois pularem juntos (cada um também pula na sua
        # tecla de cima -> W / seta para cima).
        right = key_pressed(right_key)
        left = key_pressed(left_key)
        jumpk = or_(key_pressed("space"), key_pressed(up_key))
        feet = sub(ypos(), FOOT)

        # motor principal (colisão por matemática contra chão + 2 obstáculos)
        sp.script(
            on_flag(),
            point_dir(90), hide(),
            set_var(vy, 0), set_var(no, 0), set_var(passo, 0), set_var(dx, 0),
            forever([
                if_else(playing(), [
                    show(), change_var(passo, 1),
                    # ---------- HORIZONTAL ----------
                    set_var(dx, 0),
                    if_(right, [set_var(dx, WALK), point_dir(90)]),
                    if_(left, [set_var(dx, -WALK), point_dir(-90)]),
                    change_x(var(dx)),
                    if_(gt(xpos(), PLAYER_XMAX), [set_x(PLAYER_XMAX)]),
                    if_(lt(xpos(), PLAYER_XMIN), [set_x(PLAYER_XMIN)]),
                    # bloqueio lateral pelos obstáculos (só se os pés estão abaixo do topo)
                    *[if_(and_(ov_xv(x0, x1), lt(feet, sub(var(t), 2))), [
                        if_(gt(var(dx), 0), [set_x(sub(var(x0), HW))]),
                        if_(lt(var(dx), 0), [set_x(add(var(x1), HW))]),
                    ]) for (x0, x1, t) in OBV],
                    # ---------- VERTICAL / GRAVIDADE ----------
                    set_var(pf, feet),                       # pés antes de cair
                    change_var(vy, -GRAV),
                    if_(lt(var(vy), VY_MIN), [set_var(vy, VY_MIN)]),
                    change_y(var(vy)),
                    set_var(sf, GY),                         # superfície sob o jogador
                    # topo dos obstáculos sólidos + das plataformas flutuantes
                    # (one-way: só pousa vindo de cima, pf >= topo)
                    *[if_(and_(ov_xv(x0, x1), ge(var(pf), sub(var(t), 2))),
                          [if_(gt(var(t), var(sf)), [set_var(sf, var(t))])])
                      for (x0, x1, t) in OBV + QV],
                    if_else(le(feet, var(sf)), [
                        set_y(add(var(sf), FOOT)),
                        if_(le(var(vy), 0), [set_var(no, 1)]),
                        set_var(vy, 0),
                    ], [set_var(no, 0)]),
                    # ---------- PULO (os dois leem ESPAÇO -> pulam juntos) ----------
                    if_(and_(jumpk, eq(var(no), 1)), [set_var(vy, JUMP), set_var(no, 0)]),
                    # ---------- ANIMAÇÃO DE COSTUME ----------
                    if_else(eq(var(no), 0),
                            [switch_costume(c_jump)],
                            [if_else(not_(eq(var(dx), 0)),
                                     [if_else(lt(mod(var(passo), 12), 6),
                                              [switch_costume(c_walk)], [switch_costume(c_idle)])],
                                     [switch_costume(c_idle)])]),
                    # ---------- CHEGOU NA SUA PORTA? (no chão/plataforma, pertinho) ----------
                    if_else(and_(eq(var(no), 1),
                                 lt(add(sq(sub(xpos(), var(dxv))),
                                        sq(sub(ypos(), var(dyv)))), DOOR_R2)),
                            [set_var(ok_var, 1)], [set_var(ok_var, 0)]),
                ], [
                    if_(not_(or_(eq(var("modo"), 2), eq(var("modo"), 3))), [hide()]),
                ]),
            ]),
        )
        # nascer / mostrar ao iniciar a fase
        sp.script(
            on_broadcast("jogar"),
            goto_xy(spawn[0], spawn[1]), point_dir(90),
            set_var(vy, 0), set_var(no, 0),
            clear_effects(), set_size(100), switch_costume(c_idle), show(),
        )
        # animação de entrar na porta
        sp.script(
            on_broadcast("entrar_porta"),
            if_(eq(var("modo"), 3), [
                point_dir(90), set_var(vy, 0), set_var(no, 0),
                glide_xy(0.4, var(dxv), var(dyv)),
                repeat(10, [change_size(-9), turn_right(36), change_effect("ghost", 9)]),
                hide(), set_size(100), clear_effects(),
            ]),
        )
        return sp

    P.add_sprite(make_player(
        "Theo", ("Theo parado", "Theo andar", "Theo pular"),
        SPAWN_THEO, "dtx", "dty", "Theo_ok",
        "vy_theo", "no_theo", "passo_theo", "dx_theo", "pf_theo", "sf_theo",
        "a", "d", "w", 11))                       # Theo = WASD
    P.add_sprite(make_player(
        "Lia", ("Lia parada", "Lia andar", "Lia pular"),
        SPAWN_LIA, "dlx", "dly", "Lia_ok",
        "vy_lia", "no_lia", "passo_lia", "dx_lia", "pf_lia", "sf_lia",
        "left arrow", "right arrow", "up arrow", 12))   # Lia = setas

    # =====================================================================
    # BOTÃO COMEÇAR
    # =====================================================================
    btn = Target("Botao")
    btn.add_costume("Comecar", art_ui.start_button(), art_ui.BTN_W / 2, art_ui.BTN_H / 2)
    btn.x, btn.y, btn.layer = 0, -8, 16
    btn.script(
        on_flag(), goto_xy(0, -8), set_size(100), goto_front(),
        forever([
            if_else(eq(var("modo"), 0),
                    [show(), set_size(pulse(102, 4, 240))],
                    [hide()]),
        ]),
    )
    btn.script(
        on_clicked(),
        if_(eq(var("modo"), 0), [broadcast("comecar")]),
    )
    P.add_sprite(btn)

    # =====================================================================
    # SELO ANIMADO (motivo da era na intro)
    # =====================================================================
    selo = Target("Selo")
    for name, svg in art_ui.selo_all():
        selo.add_costume(name, svg, art_ui.SEL / 2, art_ui.SEL / 2)
    selo.x, selo.y, selo.layer = 150, -60, 17
    selo.visible = False
    selo.script(
        on_flag(), hide(), set_size(100), goto_xy(150, -60), point_dir(90),
        forever([
            if_else(eq(var("modo"), 1), [
                switch_costume(var("fase")), goto_xy(150, -60),
                point_dir(pulse(90, 8, 150)), set_size(pulse(105, 10, 220)), show(),
            ], [hide(), point_dir(90)]),
        ]),
    )
    P.add_sprite(selo)

    # =====================================================================
    # CONTAGEM REGRESSIVA (Prepare-se / 3 / 2 / 1)
    # =====================================================================
    cont = Target("Contagem")
    for name, svg in art_ui.count_all():
        cont.add_costume(name, svg, art_ui.CW / 2, art_ui.CH / 2)
    cont.x, cont.y, cont.layer = 0, 0, 18
    cont.visible = False
    cont.script(
        on_flag(), hide(), set_size(100), goto_xy(0, 0),
        forever([
            if_else(and_(eq(var("modo"), 1), gt(var("intro_n"), 0)), [
                if_(eq(var("intro_n"), 99), [switch_costume("Prepare")]),
                if_(eq(var("intro_n"), 3), [switch_costume("3")]),
                if_(eq(var("intro_n"), 2), [switch_costume("2")]),
                if_(eq(var("intro_n"), 1), [switch_costume("1")]),
                goto_xy(0, 0), show(), set_size(pulse(104, 8, 400)),
            ], [hide()]),
        ]),
    )
    P.add_sprite(cont)

    # =====================================================================
    # BANNER "FASE COMPLETA"
    # =====================================================================
    aviso = Target("Aviso")
    aviso.add_costume("Fase Completa", art_ui.banner_costume(), art_ui.BW / 2, art_ui.BH / 2)
    aviso.x, aviso.y, aviso.layer = 0, 40, 19
    aviso.visible = False
    aviso.script(on_flag(), hide())
    aviso.script(
        on_broadcast("banner_fim"),
        if_(eq(var("modo"), 3), [
            goto_xy(0, 40), set_size(40), clear_effects(), show(),
            repeat(10, [change_size(8)]),
            wait(0.7),
            repeat(6, [change_effect("ghost", 16)]),
            hide(), set_size(100), clear_effects(),
        ]),
    )
    P.add_sprite(aviso)

    # =====================================================================
    # CONFETE (vitória)
    # =====================================================================
    conf = Target("Confete")
    for name, svg in art_ui.confetti_all():
        conf.add_costume(name, svg, 6, 8)
    conf.x, conf.y, conf.layer = 0, 200, 20
    conf.visible = False
    conf.script(on_flag(), hide())
    conf.script(
        on_broadcast("vitoria"),
        repeat(50, [
            goto_xy(rnd(-230, 230), 195), switch_costume(rnd(1, 6)),
            create_clone_self(), wait(0.06),
        ]),
    )
    conf.script(
        on_clone(),
        show(), set_size(rnd(55, 110)), point_dir(rnd(-25, 25)),
        repeat_until(lt(ypos(), -185), [
            change_y(-5), change_x(rnd(-3, 3)), turn_right(18),
        ]),
        delete_clone(),
    )
    P.add_sprite(conf)

    # =====================================================================
    # ASTRO - elemento celeste animado no fundo (muda por era)
    # =====================================================================
    astro = Target("Astro")
    for name, svg in art_fx.astro_all():
        astro.add_costume(name, svg, art_fx.AC, art_fx.AC)
    astro.x, astro.y, astro.layer = ASTRO_POS[1][0], ASTRO_POS[1][1], 1
    astro.visible = False

    def astro_bob(by):   # sobe e desce suave
        return add(by, mul(7, mathop("sin", mul(timer(), 55))))
    pos_chain = [if_(eq(var("fase"), n),
                     [goto_xy(ASTRO_POS[n][0], astro_bob(ASTRO_POS[n][1]))])
                 for n in range(1, 6)]
    astro.script(
        on_flag(), hide(), set_size(100), point_dir(90),
        forever([
            if_else(visible_phase(), [
                switch_costume(var("fase")),
                *pos_chain,
                turn_right(0.6),                 # giro lento (arte em movimento)
                set_size(pulse(102, 6, 80)),     # pulsa
                show(),
            ], [hide()]),
        ]),
    )
    P.add_sprite(astro)

    # =====================================================================
    # PARTÍCULAS - motes que flutuam no fundo (clones que derivam)
    # =====================================================================
    part = Target("Particula")
    for name, svg in art_fx.part_all():
        part.add_costume(name, svg, 10, 10)
    part.x, part.y, part.layer = 0, 0, 2
    part.visible = False
    part.script(
        on_flag(), hide(),
        repeat(16, [goto_xy(rnd(-230, 230), rnd(-50, 150)), create_clone_self()]),
    )
    part.script(
        on_clone(),
        set_size(rnd(70, 150)),
        forever([
            if_else(visible_phase(), [
                switch_costume(var("fase")), set_effect("ghost", 40), show(),
                # deriva p/ esquerda com parallax (mais alto = mais rápido) + gira
                change_x(sub(0, add(0.6, div(add(ypos(), 180), 220)))),
                turn_right(2),
                if_(lt(xpos(), -238), [set_x(238), set_y(rnd(-50, 150))]),
            ], [hide()]),
        ]),
    )
    P.add_sprite(part)

    # =====================================================================
    # RÓTULO - texto da era + período (topo, durante a fase)
    # =====================================================================
    rot = Target("Rotulo")
    for name, svg in art_fx.rotulo_all():
        rot.add_costume(name, svg, art_fx.RW / 2, art_fx.RH / 2)
    rot.x, rot.y, rot.layer = 0, 150, 15
    rot.visible = False
    rot.script(
        on_flag(), hide(), set_size(100), goto_xy(0, 150),
        forever([
            if_else(playing(),
                    [switch_costume(var("fase")), goto_xy(0, 150), show()],
                    [hide()]),
        ]),
    )
    P.add_sprite(rot)

    # =====================================================================
    # DIRETOR (controla o fluxo)  -- invisível
    # =====================================================================
    dirc = Target("Diretor")
    dirc.add_costume("dot", art_ui.dot_costume(), 4, 4)
    dirc.x, dirc.y, dirc.layer = 240, 175, 21
    dirc.visible = False

    def reset_items():
        return [set_var("item1", 0), set_var("item2", 0), set_var("item3", 0),
                set_var("item4", 0), set_var("Theo_ok", 0), set_var("Lia_ok", 0),
                set_var("Relíquias", 0), set_var("cadT", 0), set_var("cadL", 0)]

    all_done = and_(
        and_(and_(eq(var("item1"), 1), eq(var("item2"), 1)),
             and_(eq(var("item3"), 1), eq(var("item4"), 1))),
        and_(eq(var("Theo_ok"), 1), eq(var("Lia_ok"), 1)))

    def set_level_chain():   # grava obstáculos, plataformas e portas da fase
        chain = []
        for n in range(1, 6):
            obs, pls = obstacles(n), platforms(n)
            dt, dl = door_theo(n), door_lia(n)
            stmts = []
            for i in range(MAX_OBST):
                x0n, x1n, tn = OBV[i]
                if i < len(obs):
                    o = obs[i]
                    stmts += [set_var(x0n, o["x0"]), set_var(x1n, o["x1"]), set_var(tn, o["top"])]
                else:
                    stmts += [set_var(x0n, 9999), set_var(x1n, 9999), set_var(tn, -999)]
            for i in range(MAX_PLAT):
                x0n, x1n, tn = QV[i]
                if i < len(pls):
                    p = pls[i]
                    stmts += [set_var(x0n, p["x0"]), set_var(x1n, p["x1"]), set_var(tn, p["top"])]
                else:
                    stmts += [set_var(x0n, 9999), set_var(x1n, 9999), set_var(tn, -999)]
            stmts += [set_var("dtx", dt[0]), set_var("dty", dt[1]),
                      set_var("dlx", dl[0]), set_var("dly", dl[1])]
            chain.append(if_(eq(var("fase"), n), stmts))
        return chain

    # init
    dirc.script(
        on_flag(),
        hide(), set_var("modo", 0), set_var("fase", 0),
        set_var("Pontos", 0), *reset_items(), set_var("intro_n", 0),
        switch_backdrop("Tela Inicial"),
    )
    # checagem de vitória da fase
    dirc.script(
        on_flag(),
        forever([
            if_(playing(), [
                set_var("Relíquias", add(add(var("item1"), var("item2")),
                                          add(var("item3"), var("item4")))),
                if_(all_done, [set_var("modo", 3), broadcast("fase_completa")]),
            ]),
        ]),
    )
    # começar
    dirc.script(
        on_broadcast("comecar"),
        set_var("Pontos", 0), set_var("fase", 1), broadcast("carregar_fase"),
    )
    # carregar fase + intro de 7s
    intro_switch = [if_(eq(var("fase"), p["num"]), [switch_backdrop(intro_name(p))]) for p in PHASES]
    game_switch = [if_(eq(var("fase"), p["num"]), [switch_backdrop(fase_name(p))]) for p in PHASES]
    dirc.script(
        on_broadcast("carregar_fase"),
        set_var("modo", 1), *reset_items(), set_var("intro_n", 0),
        *intro_switch,
        set_var("intro_n", 99), wait(1),
        set_var("intro_n", 0), wait(3),
        set_var("intro_n", 3), wait(1),
        set_var("intro_n", 2), wait(1),
        set_var("intro_n", 1), wait(1),
        set_var("intro_n", 0),
        *game_switch,
        *set_level_chain(),              # obstáculos + plataformas + portas da fase
        set_var("modo", 2), broadcast("jogar"),
    )
    # fase completa -> animações -> próxima
    dirc.script(
        on_broadcast("fase_completa"),
        broadcast("entrar_porta"), wait(1),
        broadcast("banner_fim"), wait(1.4),
        change_var("Pontos", 15),
        if_else(eq(var("fase"), 5), [
            set_var("fase", 6), set_var("modo", 4),
            switch_backdrop("Vitoria"), broadcast("vitoria"),
        ], [
            change_var("fase", 1), broadcast("carregar_fase"),
        ]),
    )
    P.add_sprite(dirc)

    # =====================================================================
    # MONITORES (HUD: Pontos e Relíquias)
    # =====================================================================
    P.monitors = [
        _monitor(P, "Pontos", 5, 5),
        _monitor(P, "Relíquias", 5, 32),
    ]
    return P


def door_pos(door):
    return DOOR_THEO if door == "Porta Theo" else DOOR_LIA


def _monitor(P, name, x, y):
    return {
        "id": P.global_vars[name], "mode": "default", "opcode": "data_variable",
        "params": {"VARIABLE": name}, "spriteName": None, "value": 0,
        "width": 0, "height": 0, "x": x, "y": y, "visible": True,
        "sliderMin": 0, "sliderMax": 100, "isDiscrete": True,
    }


if __name__ == "__main__":
    import os, sys
    proj = build()
    # caminho de saída relativo à raiz do repositório (pasta acima de build/),
    # ou o 1º argumento da linha de comando -> funciona em qualquer clone.
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(repo_root, "Dupla_das_Artes.sb3")
    data = proj.write_sb3(out)
    n_blocks = sum(len(t["blocks"]) for t in data["targets"])
    print(f"OK -> {out}")
    print(f"targets: {len(data['targets'])}, blocks: {n_blocks}")
    print("sprites:", ", ".join(t["name"] for t in data["targets"]))
