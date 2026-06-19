# -*- coding: utf-8 -*-
"""add_sounds.py - Adiciona EFEITOS DE SOM ao jogo SEM tocar em nada do que já
existe (blocos, cenários, atores, textos). Faz isso anexando 2 novos sprites
invisíveis ("Musica" e "Som") que apenas OBSERVAM as variáveis/broadcasts do
jogo e tocam os sons. Nenhum sprite/bloco/fantasia/backdrop existente é alterado.

Uso: python3 add_sounds.py entrada.sb3 saida.sb3
"""
import sys, json, zipfile
from sb3lib import (Project, Target, on_flag, on_broadcast, forever, wait, wait_until,
                    if_else, play_sound, play_sound_until_done, set_volume,
                    var, eq, gt, lt, ge, and_, or_, not_)
import gen_sounds
import art_ui

IN = sys.argv[1] if len(sys.argv) > 1 else "in.sb3"
OUT = sys.argv[2] if len(sys.argv) > 2 else "/home/user/Scratch-code-/Dupla_das_Artes.sb3"

snd = gen_sounds.all_sounds()
dot = art_ui.dot_costume()
P = Project()

# ---------------------------------------------------------------- MÚSICA ----
musica = Target("Musica")
musica.add_costume("dot", dot, 4, 4)
musica.add_sound("musica", *snd["musica"])
musica.visible = False
musica.script(                          # toca em loop, baixinho e imersivo
    on_flag(), set_volume(55),
    forever([play_sound_until_done("musica")]),
)

# ------------------------------------------------------------------ SFX ------
som = Target("Som")
som.add_costume("dot", dot, 4, 4)
for nm in ["clique", "coletar", "pulo", "passo", "destravar", "festa"]:
    som.add_sound(nm, *snd[nm])
som.visible = False

# clicar em Jogar (o botão verde dispara "comecar")
som.script(on_broadcast("comecar"), play_sound("clique"))
# festa/confete ao zerar (broadcast "vitoria")
som.script(on_broadcast("vitoria"), play_sound("festa"))
# coletar cada item (item vira 1 quando o dono pega; reseta a 0 na próxima fase)
for it in ["item1", "item2", "item3", "item4"]:
    som.script(on_flag(), forever([
        wait_until(eq(var(it), 1)), play_sound("coletar"), wait_until(eq(var(it), 0)),
    ]))
# pulo de cada personagem (vy salta para 14 ao pular)
for vy in ["vy_theo", "vy_lia"]:
    som.script(on_flag(), forever([
        wait_until(gt(var(vy), 5)), play_sound("pulo"), wait_until(lt(var(vy), 6)),
    ]))
# destravar portas (todos os itens coletados -> Relíquias = 4)
som.script(on_flag(), forever([
    wait_until(ge(var("Relíquias"), 4)), play_sound("destravar"), wait_until(lt(var("Relíquias"), 4)),
]))
# passos enquanto algum personagem anda no chão (durante o jogo)
walking = or_(and_(not_(eq(var("dx_theo"), 0)), eq(var("no_theo"), 1)),
              and_(not_(eq(var("dx_lia"), 0)), eq(var("no_lia"), 1)))
som.script(on_flag(), forever([
    if_else(and_(eq(var("modo"), 2), walking),
            [play_sound("passo"), wait(0.3)],
            [wait(0.05)]),
]))

# ---- compila só os 2 sprites novos (ids de variáveis/broadcasts batem) ----
musica.blocks = P._compile_target(musica)
som.blocks = P._compile_target(som)

src = zipfile.ZipFile(IN)
proj = json.loads(src.read("project.json"))
maxlayer = max((t.get("layerOrder", 0) for t in proj["targets"]), default=0)

mj = P._target_json(musica, {}, False); mj["layerOrder"] = maxlayer + 1
sj = P._target_json(som, {}, False); sj["layerOrder"] = maxlayer + 2
proj["targets"].append(mj)
proj["targets"].append(sj)

# novos assets (costume transparente + WAVs)
new_assets = {}
for c in musica.costumes + som.costumes:
    new_assets[c["md5ext"]] = c["_svg"].encode("utf-8")
for s in musica.sounds + som.sounds:
    new_assets[s["md5ext"]] = s["_bytes"]

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as out:
    out.writestr("project.json", json.dumps(proj, ensure_ascii=False))
    for n in src.namelist():                 # mantém TODOS os assets originais
        if n != "project.json":
            out.writestr(n, src.read(n))
    for fn, blob in new_assets.items():       # adiciona só os novos
        if fn not in src.namelist():
            out.writestr(fn, blob)
src.close()

n_sounds = len(musica.sounds) + len(som.sounds)
print(f"OK -> {OUT}")
print(f"sprites novos: Musica, Som | sons adicionados: {n_sounds} | "
      f"targets totais: {len(proj['targets'])}")
