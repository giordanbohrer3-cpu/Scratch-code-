# -*- coding: utf-8 -*-
"""sb3lib.py - Mini-compilador de blocos Scratch -> project.json (.sb3).

Escreve a estrutura EXATA que o Scratch 3 usa (verificado contra um .sb3 real):
  - literal número:   [1, [4, "10"]]
  - literal texto:    [1, [10, "oi"]]
  - variável (valor): [3, [12, nome, id], [10, ""]]
  - reporter (valor): [3, blocoId, [10, ""]]
  - booleano:         [2, blocoId]
  - substack:         [2, primeiroId]
  - menu (shadow):    [1, shadowId]

Uso: monta-se a árvore com helpers (statements e reporters), e o compilador
gera os blocos com next/parent corretos.
"""
from __future__ import annotations
import json, hashlib, zipfile, os, random, string

# ===========================================================================
# Geração de IDs
# ===========================================================================
_ALPHA = string.ascii_letters + string.digits + "#%()*+,-./:;=?@[]^_`{|}~"
_counter = [0]


def newid():
    _counter[0] += 1
    return f"b{_counter[0]}_" + "".join(random.choice(string.ascii_letters) for _ in range(4))


# ===========================================================================
# Especificações de expressões (reporters / booleanos / primitivas)
# ===========================================================================
class Rep(dict):
    """Reporter ou booleano. shape in {'reporter','bool'}."""


def _rep(op, inputs=None, fields=None, shape="reporter"):
    return Rep(op=op, inputs=inputs or {}, fields=fields or {}, shape=shape)


# ---- primitivas de dados ----
def var(name):              return Rep(prim="var", name=name, shape="reporter")
def lst(name):              return Rep(prim="list", name=name, shape="reporter")

# ---- operadores ----
def add(a, b):  return _rep("operator_add", {"NUM1": a, "NUM2": b})
def sub(a, b):  return _rep("operator_subtract", {"NUM1": a, "NUM2": b})
def mul(a, b):  return _rep("operator_multiply", {"NUM1": a, "NUM2": b})
def div(a, b):  return _rep("operator_divide", {"NUM1": a, "NUM2": b})
def mod(a, b):  return _rep("operator_mod", {"NUM1": a, "NUM2": b})
def rnd(a, b):  return _rep("operator_random", {"FROM": a, "TO": b})
def eq(a, b):   return _rep("operator_equals", {"OPERAND1": a, "OPERAND2": b}, shape="bool")
def gt(a, b):   return _rep("operator_gt", {"OPERAND1": a, "OPERAND2": b}, shape="bool")
def lt(a, b):   return _rep("operator_lt", {"OPERAND1": a, "OPERAND2": b}, shape="bool")
def and_(a, b): return _rep("operator_and", {"OPERAND1": a, "OPERAND2": b}, shape="bool")
def or_(a, b):  return _rep("operator_or", {"OPERAND1": a, "OPERAND2": b}, shape="bool")
def not_(a):    return _rep("operator_not", {"OPERAND": a}, shape="bool")
def join(a, b): return _rep("operator_join", {"STRING1": a, "STRING2": b})
def mathop(op, v): return _rep("operator_mathop", {"NUM": v}, fields={"OPERATOR": [op, None]})

# ---- motion reporters ----
def xpos():     return _rep("motion_xposition")
def ypos():     return _rep("motion_yposition")
def direction():return _rep("motion_direction")

# ---- sensing ----
def key_pressed(key):
    return _rep("sensing_keypressed",
                {"KEY_OPTION": Rep(menu="sensing_keyoptions", field="KEY_OPTION", value=key)},
                shape="bool")

def touching(spritename):
    return _rep("sensing_touchingobject",
                {"TOUCHINGOBJECTMENU": Rep(menu="sensing_touchingobjectmenu",
                                           field="TOUCHINGOBJECTMENU", value=spritename)},
                shape="bool")

def timer():    return _rep("sensing_timer")
def ge(a, b):   return _rep("operator_not", {"OPERAND": lt(a, b)}, shape="bool")
def le(a, b):   return _rep("operator_not", {"OPERAND": gt(a, b)}, shape="bool")

def of_(prop, target):
    """[ propriedade ] de [ alvo ]  (sensing_of)."""
    return _rep("sensing_of",
                {"OBJECT": Rep(menu="sensing_of_object_menu", field="OBJECT", value=target)},
                fields={"PROPERTY": [prop, None]})


# ===========================================================================
# Especificações de comandos (statements / hats)
# ===========================================================================
def S(op, inputs=None, fields=None, sub=None, sub2=None):
    d = {"op": op, "inputs": inputs or {}, "fields": fields or {}}
    if sub is not None:  d["sub"] = sub
    if sub2 is not None: d["sub2"] = sub2
    return d


# ---- eventos (hats) ----
def on_flag():                  return S("event_whenflagclicked")
def on_broadcast(msg):          return S("event_whenbroadcastreceived", fields={"BROADCAST_OPTION": [msg, "__bc__"]})
def on_clicked():               return S("event_whenthisspriteclicked")
def on_clone():                 return S("control_start_as_clone")
def on_key(key):                return S("event_whenkeypressed", fields={"KEY_OPTION": [key, None]})

# ---- controle ----
def forever(body):              return S("control_forever", sub=body)
def repeat(n, body):            return S("control_repeat", {"TIMES": n}, sub=body)
def repeat_until(cond, body):   return S("control_repeat_until", {"CONDITION": cond}, sub=body)
def if_(cond, body):            return S("control_if", {"CONDITION": cond}, sub=body)
def if_else(cond, a, b):        return S("control_if_else", {"CONDITION": cond}, sub=a, sub2=b)
def wait(secs):                 return S("control_wait", {"DURATION": secs})
def wait_until(cond):           return S("control_wait_until", {"CONDITION": cond})
def stop(opt="all"):            return S("control_stop", fields={"STOP_OPTION": [opt, None]})
def create_clone_self():
    return S("control_create_clone_of",
             {"CLONE_OPTION": Rep(menu="control_create_clone_of_menu", field="CLONE_OPTION", value="_myself_")})
def delete_clone():             return S("control_delete_this_clone")

# ---- eventos broadcast ----
def broadcast(msg):             return S("event_broadcast", {"BROADCAST_INPUT": Rep(prim="broadcast", name=msg)})
def broadcast_wait(msg):        return S("event_broadcastandwait", {"BROADCAST_INPUT": Rep(prim="broadcast", name=msg)})

# ---- dados ----
def set_var(name, val):         return S("data_setvariableto", {"VALUE": val}, fields={"VARIABLE": [name, "__var__"]})
def change_var(name, val):      return S("data_changevariableby", {"VALUE": val}, fields={"VARIABLE": [name, "__var__"]})
def show_var(name):             return S("data_showvariable", fields={"VARIABLE": [name, "__var__"]})
def hide_var(name):             return S("data_hidevariable", fields={"VARIABLE": [name, "__var__"]})

# ---- movimento ----
def goto_xy(x, y):              return S("motion_gotoxy", {"X": x, "Y": y})
def glide_xy(secs, x, y):       return S("motion_glidesecstoxy", {"SECS": secs, "X": x, "Y": y})
def change_x(dx):               return S("motion_changexby", {"DX": dx})
def change_y(dy):               return S("motion_changeyby", {"DY": dy})
def set_x(x):                   return S("motion_setx", {"X": x})
def set_y(y):                   return S("motion_sety", {"Y": y})
def point_dir(d):               return S("motion_pointindirection", {"DIRECTION": d})
def turn_right(d):              return S("motion_turnright", {"DEGREES": d})

# ---- aparência ----
def show():                     return S("looks_show")
def hide():                     return S("looks_hide")
def say(msg):                   return S("looks_say", {"MESSAGE": msg})
def say_for(msg, secs):         return S("looks_sayforsecs", {"MESSAGE": msg, "SECS": secs})
def switch_costume(name):
    if isinstance(name, (Rep,)) or isinstance(name, (int, float)):
        return S("looks_switchcostumeto", {"COSTUME": _costume_menu(name)})
    return S("looks_switchcostumeto", {"COSTUME": Rep(menu="looks_costume", field="COSTUME", value=name)})
def next_costume():             return S("looks_nextcostume")
def switch_backdrop(name):
    return S("looks_switchbackdropto", {"BACKDROP": Rep(menu="looks_backdrops", field="BACKDROP", value=name)})
def set_size(p):                return S("looks_setsizeto", {"SIZE": p})
def change_size(p):             return S("looks_changesizeby", {"CHANGE": p})
def set_effect(eff, v):         return S("looks_seteffectto", {"VALUE": v}, fields={"EFFECT": [eff, None]})
def change_effect(eff, v):      return S("looks_changeeffectby", {"CHANGE": v}, fields={"EFFECT": [eff, None]})
def clear_effects():            return S("looks_cleargraphiceffects")
def goto_front():               return S("looks_gotofrontback", fields={"FRONT_BACK": ["front", None]})
def goto_back():                return S("looks_gotofrontback", fields={"FRONT_BACK": ["back", None]})

# ---- som ----
def play_sound(name):
    return S("sound_play", {"SOUND_MENU": Rep(menu="sound_sounds_menu", field="SOUND_MENU", value=name)})
def play_sound_until_done(name):
    return S("sound_playuntildone", {"SOUND_MENU": Rep(menu="sound_sounds_menu", field="SOUND_MENU", value=name)})
def stop_all_sounds():          return S("sound_stopallsounds")
def set_volume(v):              return S("sound_setvolumeto", {"VOLUME": v})
def change_volume(v):           return S("sound_changevolumeby", {"VOLUME": v})
def go_forward(n):              return S("looks_goforwardbackwardlayers", {"NUM": n}, fields={"FORWARD_BACKWARD": ["forward", None]})
def go_backward(n):             return S("looks_goforwardbackwardlayers", {"NUM": n}, fields={"FORWARD_BACKWARD": ["backward", None]})


def _costume_menu(val):
    # quando trocamos por número/variável, ainda precisamos do shadow do menu
    return Rep(menu="looks_costume", field="COSTUME", value="costume1", obscured=val)


# ===========================================================================
# Alvo (Stage ou Sprite)
# ===========================================================================
class Target:
    def __init__(self, name, is_stage=False):
        self.name = name
        self.is_stage = is_stage
        self.costumes = []   # dicts
        self.sounds = []
        self.blocks = {}
        self.scripts = []    # listas de statements (cada uma começa com hat)
        self.x = 0; self.y = 0; self.size = 100; self.direction = 90
        self.visible = True; self.draggable = False; self.rotation_style = "all around"
        self.current_costume = 0
        self.layer = 1

    def add_costume(self, name, svg_text, cx, cy):
        md5 = hashlib.md5(svg_text.encode("utf-8")).hexdigest()
        self.costumes.append({
            "name": name, "dataFormat": "svg", "assetId": md5,
            "md5ext": md5 + ".svg", "rotationCenterX": cx, "rotationCenterY": cy,
            "_svg": svg_text,
        })

    def add_sound(self, name, wav_bytes, rate, sample_count):
        md5 = hashlib.md5(wav_bytes).hexdigest()
        self.sounds.append({
            "name": name, "assetId": md5, "dataFormat": "wav", "format": "",
            "rate": rate, "sampleCount": sample_count, "md5ext": md5 + ".wav",
            "_bytes": wav_bytes,
        })

    def script(self, *stmts):
        self.scripts.append(list(stmts))


# ===========================================================================
# Projeto
# ===========================================================================
class Project:
    def __init__(self):
        self.stage = Target("Stage", is_stage=True)
        self.sprites = []
        self.global_vars = {}     # name -> id
        self.var_init = {}        # name -> valor inicial
        self.global_lists = {}
        self.broadcasts = {}      # name -> id
        self.monitors = []

    def add_sprite(self, sp):
        self.sprites.append(sp); return sp

    def add_var(self, name, value=0):
        if name not in self.global_vars:
            self.global_vars[name] = "var_" + _slug(name)
        self.var_init[name] = value
        return name

    def add_broadcast(self, name):
        if name not in self.broadcasts:
            self.broadcasts[name] = "bc_" + _slug(name)
        return name

    # ---------------------------------------------------------------
    def _resolve_var(self, name):
        return self.global_vars.get(name, "var_" + _slug(name))

    def _resolve_bc(self, name):
        if name not in self.broadcasts:
            self.add_broadcast(name)
        return self.broadcasts[name]

    # ---------------------------------------------------------------
    def _compile_target(self, t: Target):
        blocks = {}

        def emit_input(value, parent):
            # devolve o array de input do Scratch
            if isinstance(value, bool):
                value = 1 if value else 0
            if isinstance(value, (int, float)):
                return [1, [4, _num(value)]]
            if isinstance(value, str):
                return [1, [10, value]]
            if isinstance(value, Rep):
                if value.get("prim") == "var":
                    return [3, [12, value["name"], self._resolve_var(value["name"])], [10, ""]]
                if value.get("prim") == "list":
                    return [3, [13, value["name"], self.global_lists.get(value["name"], "list_" + _slug(value["name"]))], [10, ""]]
                if value.get("prim") == "broadcast":
                    return [1, [11, value["name"], self._resolve_bc(value["name"])]]
                if value.get("menu"):
                    mid = emit_menu(value, parent)
                    ob = value.get("obscured")
                    if ob is not None:
                        # algo (variável/reporter/número) obscurecendo o menu shadow
                        if isinstance(ob, Rep) and ob.get("prim") == "var":
                            return [3, [12, ob["name"], self._resolve_var(ob["name"])], mid]
                        if isinstance(ob, Rep):
                            bid = emit_block(ob, parent, shadow=False)
                            return [3, bid, mid]
                        return [3, [4, _num(ob)], mid]
                    return [1, mid]
                # reporter/boolean -> bloco
                bid = emit_block(value, parent, shadow=False)
                if value.get("shape") == "bool":
                    return [2, bid]
                return [3, bid, [10, ""]]
            raise ValueError(f"input inválido: {value!r}")

        def emit_menu(value, parent):
            mid = newid()
            blocks[mid] = {
                "opcode": value["menu"], "next": None, "parent": parent,
                "inputs": {}, "fields": {value["field"]: [value["value"], None]},
                "shadow": True, "topLevel": False,
            }
            return mid

        def emit_block(spec, parent, shadow=False):
            bid = newid()
            b = {"opcode": spec["op"], "next": None, "parent": parent,
                 "inputs": {}, "fields": {}, "shadow": shadow, "topLevel": False}
            blocks[bid] = b
            for k, v in spec.get("inputs", {}).items():
                b["inputs"][k] = emit_input(v, bid)
            for k, v in spec.get("fields", {}).items():
                b["fields"][k] = _field(self, v)
            return bid

        def emit_stmt(spec, parent):
            bid = newid()
            b = {"opcode": spec["op"], "next": None, "parent": parent,
                 "inputs": {}, "fields": {}, "shadow": False, "topLevel": False}
            blocks[bid] = b
            for k, v in spec.get("inputs", {}).items():
                b["inputs"][k] = emit_input(v, bid)
            for k, v in spec.get("fields", {}).items():
                b["fields"][k] = _field(self, v)
            if "sub" in spec:
                first = emit_stack(spec["sub"], bid)
                if first: b["inputs"]["SUBSTACK"] = [2, first]
            if "sub2" in spec:
                first = emit_stack(spec["sub2"], bid)
                if first: b["inputs"]["SUBSTACK2"] = [2, first]
            return bid

        def emit_stack(stmts, parent):
            first = None; prev = None
            for st in stmts:
                bid = emit_stmt(st, parent if prev is None else prev)
                if prev is None:
                    first = bid
                else:
                    blocks[prev]["next"] = bid
                prev = bid
            return first

        # cada script: primeiro é hat (topLevel)
        sx, sy = 30, 30
        for stmts in t.scripts:
            first = emit_stack(stmts, None)
            if first:
                blocks[first]["topLevel"] = True
                blocks[first]["parent"] = None
                blocks[first]["x"] = sx
                blocks[first]["y"] = sy
                sy += 600
        return blocks

    # ---------------------------------------------------------------
    def build_json(self):
        targets = []

        # Stage primeiro (todas as variáveis são globais aqui)
        stage_vars = {self.global_vars[n]: [n, self.var_init.get(n, 0)] for n in self.global_vars}
        self.stage.blocks = self._compile_target(self.stage)
        targets.append(self._target_json(self.stage, stage_vars, is_stage=True))

        for sp in self.sprites:
            sp.blocks = self._compile_target(sp)
            targets.append(self._target_json(sp, {}, is_stage=False))

        return {
            "targets": targets,
            "monitors": self.monitors,
            "extensions": [],
            "meta": {"semver": "3.0.0", "vm": "11.1.0",
                     "agent": "DuplaDasArtes-generator"},
        }

    def _target_json(self, t, variables, is_stage):
        broadcasts = {self.broadcasts[n]: n for n in self.broadcasts} if is_stage else {}
        j = {
            "isStage": is_stage,
            "name": t.name,
            "variables": variables,
            "lists": {},
            "broadcasts": broadcasts,
            "blocks": t.blocks,
            "comments": {},
            "currentCostume": t.current_costume,
            "costumes": [{k: v for k, v in c.items() if k != "_svg"} for c in t.costumes],
            "sounds": [{k: v for k, v in s.items() if k != "_bytes"} for s in t.sounds],
            "volume": 100,
            "layerOrder": 0 if is_stage else t.layer,
        }
        if is_stage:
            j.update({"tempo": 60, "videoTransparency": 50, "videoState": "off", "textToSpeechLanguage": None})
        else:
            j.update({"visible": t.visible, "x": t.x, "y": t.y, "size": t.size,
                      "direction": t.direction, "draggable": t.draggable,
                      "rotationStyle": t.rotation_style})
        return j

    # ---------------------------------------------------------------
    def write_sb3(self, path):
        data = self.build_json()
        assets = {}
        for t in [self.stage] + self.sprites:
            for c in t.costumes:
                assets[c["md5ext"]] = c["_svg"].encode("utf-8")
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            z.writestr("project.json", json.dumps(data, ensure_ascii=False))
            for fn, blob in assets.items():
                z.writestr(fn, blob)
        return data


# ===========================================================================
# Helpers internos
# ===========================================================================
def _slug(s):
    return "".join(ch if ch.isalnum() else "_" for ch in s).strip("_").lower()


def _num(v):
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return str(v)


def _field(project, v):
    """Resolve campos especiais (VARIABLE, BROADCAST) com ids reais."""
    if isinstance(v, list) and len(v) == 2:
        name, marker = v
        if marker == "__var__":
            return [name, project._resolve_var(name)]
        if marker == "__bc__":
            return [name, project._resolve_bc(name)]
    return v
