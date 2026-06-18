import json, hashlib, os, shutil, sys
sys.path.insert(0,'/tmp/build')
import assets

SRC="/tmp/sb3"               # original extracted sb3
OUT="/tmp/build/project"     # new project dir
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)

# ---- keep original binary assets ----
KEEP = [
 "03a82c2be11da11c2ba3269194ab1339.png", # level2
 "b0fcaf39b6d413c226888d13fab73ab2.png", # level3
 "dddd22507d06382ce01641556b352680.png", # level4
 "0a67a26e0addf684c86113670ba028d9.png", # level5
 "44880a937e12278a93a7e692307e9060.png", # GAME OVER
 "83a9787d4cb6f3b7632b4ddfebf74367.wav", # pop
 "0b1e3033140d094563248e61de4039e5.wav", # chomp
]
for f in KEEP:
    shutil.copy(os.path.join(SRC,f), os.path.join(OUT,f))

def add_svg(svg):
    data=svg.encode("utf-8")
    md5=hashlib.md5(data).hexdigest()
    open(os.path.join(OUT,md5+".svg"),"wb").write(data)
    return md5
HEAD_OUT=add_svg(assets.HEAD_OUT)
HEAD_MID=add_svg(assets.HEAD_MID)
HEAD_IN=add_svg(assets.HEAD_IN)
YOUNG=add_svg(assets.YOUNG_SVG)
MATURE=add_svg(assets.MATURE_SVG)
MENU=add_svg(assets.MENU_SVG)
PILLP=add_svg(assets.PILL_PLAY_SVG)
PILLB=add_svg(assets.PILL_BACK_SVG)
BG=add_svg(assets.BG_SVG)
APPLE=add_svg(assets.APPLE_SVG)
BANANA=add_svg(assets.BANANA_SVG)
CHERRY=add_svg(assets.CHERRY_SVG)
GRAPE=add_svg(assets.GRAPE_SVG)
STAR=add_svg(assets.STAR_SVG)
NIVEL2=add_svg(assets.NIVEL2)
NIVEL3=add_svg(assets.NIVEL3)
NIVEL4=add_svg(assets.NIVEL4)
NIVEL5=add_svg(assets.NIVEL5)

# ========================= block helpers =========================
_c=[0]
def nid():
    _c[0]+=1
    return "k"+str(_c[0])

def mk(tb,opcode,inputs=None,fields=None,shadow=False,top=False,x=0,y=0):
    bid=nid()
    b={"opcode":opcode,"next":None,"parent":None,
       "inputs":inputs or {},"fields":fields or {},
       "shadow":shadow,"topLevel":top}
    if top:
        b["x"]=x; b["y"]=y
    tb[bid]=b
    return bid

# input encoders
def num(v): return [1,[4,str(v)]]
def posn(v): return [1,[5,str(v)]]
def txt(v): return [1,[10,str(v)]]
def col(v): return [1,[9,v]]
def rep(bid): return [3,bid,[4,"0"]]
def boolin(bid): return [2,bid]
def vin(x): return x if isinstance(x,list) else [3,x,[4,'0']]
def sub(bid): return [2,bid]
def menu_in(bid): return [1,bid]
def bcin(name,bid): return [1,[11,name,bid]]

def chain(tb,ids):
    ids=[i for i in ids if i]
    for a,b in zip(ids,ids[1:]):
        tb[a]["next"]=b
    return ids[0] if ids else None

# reporters / blocks builders
def menu(tb,opcode,field,value):
    return mk(tb,opcode,{},{field:[value,None]},shadow=True)
def varrep(tb,name,vid): return mk(tb,"data_variable",{},{"VARIABLE":[name,vid]})
def setvar(tb,name,vid,val): return mk(tb,"data_setvariableto",{"VALUE":vin(val)},{"VARIABLE":[name,vid]})
def changevar(tb,name,vid,val): return mk(tb,"data_changevariableby",{"VALUE":vin(val)},{"VARIABLE":[name,vid]})
def showvar(tb,name,vid): return mk(tb,"data_showvariable",{},{"VARIABLE":[name,vid]})
def hidevar(tb,name,vid): return mk(tb,"data_hidevariable",{},{"VARIABLE":[name,vid]})
def lt(tb,a,b): return mk(tb,"operator_lt",{"OPERAND1":vin(a),"OPERAND2":vin(b)})
def gt(tb,a,b): return mk(tb,"operator_gt",{"OPERAND1":vin(a),"OPERAND2":vin(b)})
def eq(tb,a,b): return mk(tb,"operator_equals",{"OPERAND1":vin(a),"OPERAND2":vin(b)})
def And(tb,a,b): return mk(tb,"operator_and",{"OPERAND1":boolin(a),"OPERAND2":boolin(b)})
def Not(tb,a): return mk(tb,"operator_not",{"OPERAND":boolin(a)})
def cif(tb,cond,substack_first):
    return mk(tb,"control_if",{"CONDITION":boolin(cond),"SUBSTACK":sub(substack_first)})
def cifelse(tb,cond,sub1,sub2):
    return mk(tb,"control_if_else",{"CONDITION":boolin(cond),"SUBSTACK":sub(sub1),"SUBSTACK2":sub(sub2)})
def forever(tb,substack_first):
    return mk(tb,"control_forever",{"SUBSTACK":sub(substack_first)})
def repeatuntil(tb,cond,substack_first):
    return mk(tb,"control_repeat_until",{"CONDITION":boolin(cond),"SUBSTACK":sub(substack_first)})
def waitsec(tb,val): return mk(tb,"control_wait",{"DURATION":vin(val)})
def waituntil(tb,cond): return mk(tb,"control_wait_until",{"CONDITION":boolin(cond)})
def stopthis(tb):
    bid=mk(tb,"control_stop",{},{"STOP_OPTION":["this script",None]})
    tb[bid]["mutation"]={"tagName":"mutation","children":[],"hasnext":"false"}
    return bid
def broadcast(tb,name,bid_):
    return mk(tb,"event_broadcast",{"BROADCAST_INPUT":bcin(name,bid_)})
def switchbackdrop(tb,name):
    m=menu(tb,"looks_backdrops","BACKDROP",name)
    return mk(tb,"looks_switchbackdropto",{"BACKDROP":menu_in(m)})
def switchcostume(tb,name):
    m=menu(tb,"looks_costume","COSTUME",name)
    return mk(tb,"looks_switchcostumeto",{"COSTUME":menu_in(m)})
def switchcostume_num(tb,reporter_id):
    m=menu(tb,"looks_costume","COSTUME","Apple")
    return mk(tb,"looks_switchcostumeto",{"COSTUME":[3,reporter_id,m]})
def costname(tb): return mk(tb,"looks_costumenumbername",{},{"NUMBER_NAME":["name",None]})
def playsound(tb,name):
    m=menu(tb,"sound_sounds_menu","SOUND_MENU",name)
    return mk(tb,"sound_play",{"SOUND_MENU":menu_in(m)})
def keypressed(tb,key):
    m=menu(tb,"sensing_keyoptions","KEY_OPTION",key)
    return mk(tb,"sensing_keypressed",{"KEY_OPTION":menu_in(m)})
def touchingobj(tb,name):
    m=menu(tb,"sensing_touchingobjectmenu","TOUCHINGOBJECTMENU",name)
    return mk(tb,"sensing_touchingobject",{"TOUCHINGOBJECTMENU":menu_in(m)})
def touchingcolor(tb,color):
    return mk(tb,"sensing_touchingcolor",{"COLOR":col(color)})
def gotoxy(tb,xin,yin): return mk(tb,"motion_gotoxy",{"X":vin(xin),"Y":vin(yin)})
def setx(tb,xin): return mk(tb,"motion_setx",{"X":vin(xin)})
def sety(tb,yin): return mk(tb,"motion_sety",{"Y":vin(yin)})
def movesteps(tb,s): return mk(tb,"motion_movesteps",{"STEPS":vin(s)})
def pointdir(tb,d): return mk(tb,"motion_pointindirection",{"DIRECTION":posn(d) if d>=0 else num(d)})
def xpos(tb): return mk(tb,"motion_xposition")
def ypos(tb): return mk(tb,"motion_yposition")
def direction(tb): return mk(tb,"motion_direction")
def rnd(tb,a,b): return mk(tb,"operator_random",{"FROM":vin(num(a)),"TO":vin(num(b))})
def costnum(tb): return mk(tb,"looks_costumenumbername",{},{"NUMBER_NAME":["number",None]})
def gofront(tb): return mk(tb,"looks_gotofrontback",{},{"FRONT_BACK":["front",None]})
def changesize(tb,v): return mk(tb,"looks_changesizeby",{"CHANGE":num(v)})
def setsize(tb,v): return mk(tb,"looks_setsizeto",{"SIZE":num(v)})
def cleareffects(tb): return mk(tb,"looks_cleargraphiceffects")
def seteffect(tb,eff,v): return mk(tb,"looks_seteffectto",{"VALUE":vin(num(v))},{"EFFECT":[eff,None]})
def changeeffect(tb,eff,v): return mk(tb,"looks_changeeffectby",{"CHANGE":vin(num(v))},{"EFFECT":[eff,None]})
def subtract(tb,a,b): return mk(tb,"operator_subtract",{"NUM1":vin(a),"NUM2":vin(b)})
def repeatn(tb,n,substack_first): return mk(tb,"control_repeat",{"TIMES":num(n),"SUBSTACK":sub(substack_first)})

def hat_flag(tb): return mk(tb,"event_whenflagclicked",top=True)
def hat_recv(tb,name,bid_): return mk(tb,"event_whenbroadcastreceived",{},{"BROADCAST_OPTION":[name,bid_]},top=True)
def hat_clone(tb): return mk(tb,"control_start_as_clone",top=True)
def hat_key(tb,key): return mk(tb,"event_whenkeypressed",{},{"KEY_OPTION":[key,None]},top=True)
def hat_clicked(tb): return mk(tb,"event_whenthisspriteclicked",top=True)
def createclone(tb,what="_myself_"):
    m=menu(tb,"control_create_clone_of_menu","CLONE_OPTION",what)
    return mk(tb,"control_create_clone_of",{"CLONE_OPTION":menu_in(m)})
def delclone(tb): return mk(tb,"control_delete_this_clone")

def position_top(tb,bid,x,y):
    tb[bid]["topLevel"]=True; tb[bid]["x"]=x; tb[bid]["y"]=y

def fix_parents(tb):
    for oid,b in tb.items():
        for name,inp in b.get("inputs",{}).items():
            if not isinstance(inp,list): continue
            for el in inp[1:]:
                if isinstance(el,str) and el in tb:
                    tb[el]["parent"]=oid
            if isinstance(inp[1],str) and inp[1] in tb:
                tb[inp[1]]["parent"]=oid
    # next-chain parents
    for oid,b in tb.items():
        nx=b.get("next")
        if nx and nx in tb:
            tb[nx]["parent"]=oid

# ===================== variable / broadcast ids =====================
V_SCORE=("PONTUACAO","var_score")
V_RECORD=("RECORDE","var_record")
V_LEVEL=("NIVEL","var_level")
V_SPEED=("velocidade","var_speed")
V_TRAIL=("rastro","var_trail")
V_STATE=("ESTADO","var_state")
BC_MENU=("tela inicial","bc_menu")
BC_START=("iniciar jogo","bc_start")
BC_OVER=("game over","bc_over")
BC_LEVELUP=("nivelup","bc_levelup")

def Vrep(tb,V): return varrep(tb,V[0],V[1])

# ============================ STAGE ============================
stb={}
# flag: init
f=hat_flag(stb)
s1=setvar(stb,V_RECORD[0],V_RECORD[1],num(0))
s2=setvar(stb,V_STATE[0],V_STATE[1],txt("menu"))
s3=broadcast(stb,*BC_MENU)
chain(stb,[f,s1,s2,s3])
# menu received
m0=hat_recv(stb,*BC_MENU)
m1=switchbackdrop(stb,"Menu")
m2=hidevar(stb,V_SCORE[0],V_SCORE[1])
m3=hidevar(stb,V_LEVEL[0],V_LEVEL[1])
m4=showvar(stb,V_RECORD[0],V_RECORD[1])
chain(stb,[m0,m1,m2,m3,m4])
# start received
p0=hat_recv(stb,*BC_START)
p1=switchbackdrop(stb,"BG")
p2=showvar(stb,V_SCORE[0],V_SCORE[1])
p3=showvar(stb,V_LEVEL[0],V_LEVEL[1])
p4=hidevar(stb,V_RECORD[0],V_RECORD[1])
chain(stb,[p0,p1,p2,p3,p4])
# over received
o0=hat_recv(stb,*BC_OVER)
o1=switchbackdrop(stb,"GAME OVER")
o2=showvar(stb,V_RECORD[0],V_RECORD[1])
chain(stb,[o0,o1,o2])
fix_parents(stb)
position_top(stb,f,40,40); position_top(stb,m0,40,200); position_top(stb,p0,40,360); position_top(stb,o0,40,520)

# ============================ COBRA ============================
ctb={}
# ---- ENGINE (on start) ----
e0=hat_recv(ctb,*BC_START)
e1=setvar(ctb,V_STATE[0],V_STATE[1],txt("jogo"))
e2=setvar(ctb,V_SCORE[0],V_SCORE[1],num(0))
e3=setvar(ctb,V_LEVEL[0],V_LEVEL[1],num(1))
e4=setvar(ctb,V_SPEED[0],V_SPEED[1],num(5))
e5=setvar(ctb,V_TRAIL[0],V_TRAIL[1],num(0.25))
e6=pointdir(ctb,90)
e7=gotoxy(ctb,num(-60),num(0))
e8=switchcostume(ctb,"Cabeca")
e9=cleareffects(ctb)
e10=mk(ctb,"looks_show")
e11=waitsec(ctb,posn(0.2))
# forever body (no waits -> never pauses)
mv=movesteps(ctb,rep(Vrep(ctb,V_SPEED)))
# wrap-around (thresholds inside Scratch's 15px fence so they reliably fire on all 4 sides)
w1=cif(ctb, gt(ctb,xpos(ctb),num(236)), setx(ctb,num(-236)))
w2=cif(ctb, lt(ctb,xpos(ctb),num(-236)), setx(ctb,num(236)))
w3=cif(ctb, gt(ctb,ypos(ctb),num(172)), sety(ctb,num(-172)))
w4=cif(ctb, lt(ctb,ypos(ctb),num(-172)), sety(ctb,num(172)))
cl=createclone(ctb)
# self collision
deadbc=broadcast(ctb,*BC_OVER)
deadstop=stopthis(ctb)
chain(ctb,[deadbc,deadstop])
deadif=cif(ctb, touchingcolor(ctb,"#FF2D95"), deadbc)
chain(ctb,[mv,w1,w2,w3,w4,cl,deadif])
fev=forever(ctb,mv)
chain(ctb,[e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,fev])

# ---- LEVEL MANAGER (parallel thread -> changing level never pauses the game) ----
lm0=hat_recv(ctb,*BC_START)
def lvif(score_th, lvl, speed):
    cond=And(ctb,
             Not(ctb, lt(ctb, Vrep(ctb,V_SCORE), num(score_th))),   # score >= th
             lt(ctb, Vrep(ctb,V_LEVEL), num(lvl)))                  # level < lvl
    a=setvar(ctb,V_LEVEL[0],V_LEVEL[1],num(lvl))
    b=setvar(ctb,V_SPEED[0],V_SPEED[1],num(speed))
    c=broadcast(ctb,*BC_LEVELUP)
    chain(ctb,[a,b,c])
    return cif(ctb,cond,a)
LM5=lvif(20,5,9); LM4=lvif(15,4,8); LM3=lvif(10,3,7); LM2=lvif(5,2,6)
chain(ctb,[LM5,LM4,LM3,LM2])
lmf=forever(ctb,LM5)
chain(ctb,[lm0,lmf])

# ---- TONGUE FLICK (parallel thread on the head/original only) ----
tg0=hat_recv(ctb,*BC_START)
tg_in1=switchcostume(ctb,"CabecaDentro"); tg_w1=waitsec(ctb,posn(0.7))
tg_mid1=switchcostume(ctb,"CabecaMeio"); tg_w2=waitsec(ctb,posn(0.06))
tg_out=switchcostume(ctb,"Cabeca"); tg_w3=waitsec(ctb,posn(0.12))
tg_mid2=switchcostume(ctb,"CabecaMeio"); tg_w4=waitsec(ctb,posn(0.06))
tg_in2=switchcostume(ctb,"CabecaDentro"); tg_w5=waitsec(ctb,posn(0.12))
tg_mid3=switchcostume(ctb,"CabecaMeio"); tg_w6=waitsec(ctb,posn(0.06))
tg_out2=switchcostume(ctb,"Cabeca"); tg_w7=waitsec(ctb,posn(0.12))
tg_mid4=switchcostume(ctb,"CabecaMeio"); tg_w8=waitsec(ctb,posn(0.06))
chain(ctb,[tg_in1,tg_w1,tg_mid1,tg_w2,tg_out,tg_w3,tg_mid2,tg_w4,tg_in2,tg_w5,tg_mid3,tg_w6,tg_out2,tg_w7,tg_mid4,tg_w8])
tgf=forever(ctb,tg_in1)
chain(ctb,[tg0,tgf])

# ---- INPUT (on start) ----
i0=hat_recv(ctb,*BC_START)
def turn(key, dirv, opp):
    inner=pointdir(ctb,dirv)
    cond=And(ctb, keypressed(ctb,key), Not(ctb, eq(ctb,direction(ctb),num(opp))))
    return cif(ctb,cond,inner)
tR=turn("right arrow",90,-90)
tL=turn("left arrow",-90,90)
tU=turn("up arrow",0,180)
tD=turn("down arrow",180,0)
chain(ctb,[tR,tL,tU,tD])
inpf=forever(ctb,tR)
chain(ctb,[i0,inpf])

# ---- BODY clone ----
b0=hat_clone(ctb)
b1=switchcostume(ctb,"Corpo")
b2=waitsec(ctb,posn(0.15))
b3=switchcostume(ctb,"CorpoMaduro")
b4=waitsec(ctb,rep(Vrep(ctb,V_TRAIL)))
b5=delclone(ctb)
chain(ctb,[b0,b1,b2,b3,b4,b5])

# ---- clone cleanup on start (body clones are costumes 4-5; heads are 1-3) ----
cc0=hat_recv(ctb,*BC_START)
cc1=cif(ctb, gt(ctb,costnum(ctb),num(3)), delclone(ctb))
chain(ctb,[cc0,cc1])

# ---- death fx (only the head/original, not body clones) ----
d0=hat_recv(ctb,*BC_OVER)
d1=setvar(ctb,V_STATE[0],V_STATE[1],txt("fim"))
d2=playsound(ctb,"pop")
d3=cif(ctb, gt(ctb,Vrep(ctb,V_SCORE),Vrep(ctb,V_RECORD)),
        setvar(ctb,V_RECORD[0],V_RECORD[1],rep(Vrep(ctb,V_SCORE))))
chain(ctb,[d1,d2,d3])
dguard=cif(ctb, lt(ctb,costnum(ctb),num(4)), d1)   # only the head (costumes 1-3), not body clones
chain(ctb,[d0,dguard])

# ---- hide on menu ----
h0=hat_recv(ctb,*BC_MENU)
h1=mk(ctb,"looks_hide")
h2=setvar(ctb,V_STATE[0],V_STATE[1],txt("menu"))
chain(ctb,[h0,h1,h2])

fix_parents(ctb)
position_top(ctb,e0,40,40); position_top(ctb,i0,520,40); position_top(ctb,b0,1000,40)
position_top(ctb,cc0,1360,40); position_top(ctb,d0,40,900); position_top(ctb,h0,520,900)
position_top(ctb,lm0,1700,40); position_top(ctb,tg0,2050,40)

# ============================ FRUTA (Apple/Banana/Uva/Cereja/Estrela) ============================
# costume order: 1=Apple 2=Banana 3=Uva 4=Cereja 5=Estrela
atb={}
a0=hat_recv(atb,*BC_START)
a1=switchcostume_num(atb, rnd(atb,1,5))
a2=mk(atb,"looks_show")
a3=gotoxy(atb,rnd(atb,-210,210),rnd(atb,-150,150))
# --- eat sequence ---
eat_play=playsound(atb,"Chomp")
# points by costume name: Estrela +3, Cereja +2, others +1
inner_else=changevar(atb,V_SCORE[0],V_SCORE[1],num(1))   # default fruits
cereja_branch=changevar(atb,V_SCORE[0],V_SCORE[1],num(2))
nested=cifelse(atb, eq(atb,costname(atb),txt("Cereja")), cereja_branch, inner_else)
estrela_branch=changevar(atb,V_SCORE[0],V_SCORE[1],num(3))
pts=cifelse(atb, eq(atb,costname(atb),txt("Estrela")), estrela_branch, nested)
eat_tr=changevar(atb,V_TRAIL[0],V_TRAIL[1],num(0.05))
new_cost=switchcostume_num(atb, rnd(atb,1,5))
rep_goto=gotoxy(atb,rnd(atb,-210,210),rnd(atb,-150,150))
rep_loop=repeatuntil(atb, Not(atb,touchingobj(atb,"Cobra")), rep_goto)
chain(atb,[eat_play,pts,eat_tr,new_cost,rep_loop])
eatif=cif(atb, touchingobj(atb,"Cobra"), eat_play)
af=forever(atb,eatif)
chain(atb,[a0,a1,a2,a3,af])
# hide on menu/over
ah0=hat_recv(atb,*BC_MENU); ah1=mk(atb,"looks_hide"); chain(atb,[ah0,ah1])
ao0=hat_recv(atb,*BC_OVER); ao1=mk(atb,"looks_hide"); chain(atb,[ao0,ao1])
fix_parents(atb)
position_top(atb,a0,40,40); position_top(atb,ah0,40,520); position_top(atb,ao0,360,520)

# ============================ PRESS START ============================
ptb={}
# show on menu
ps0=hat_recv(ptb,*BC_MENU)
ps1=switchcostume(ptb,"Jogar")
ps2=gotoxy(ptb,num(0),num(-152))
ps3=mk(ptb,"looks_show")
ps4=gofront(ptb)
chain(ptb,[ps0,ps1,ps2,ps3,ps4])
# hide on start
ph0=hat_recv(ptb,*BC_START); ph1=mk(ptb,"looks_hide"); chain(ptb,[ph0,ph1])
# show back on over
pb0=hat_recv(ptb,*BC_OVER)
pb1=switchcostume(ptb,"Voltar")
pb2=gotoxy(ptb,num(0),num(-152))
pb3=mk(ptb,"looks_show")
pb4=gofront(ptb)
chain(ptb,[pb0,pb1,pb2,pb3,pb4])
# pulse
pu0=hat_flag(ptb)
pu1=setsize(ptb,100)
inc=changesize(ptb,1.3); incw=waitsec(ptb,posn(0.03)); chain(ptb,[inc,incw])
rup=repeatn(ptb,9,inc)
dec=changesize(ptb,-1.3); decw=waitsec(ptb,posn(0.03)); chain(ptb,[dec,decw])
rdn=repeatn(ptb,9,dec)
chain(ptb,[rup,rdn])
puf=forever(ptb,rup)
chain(ptb,[pu0,pu1,puf])
# space key
sk0=hat_key(ptb,"space")
sk_start=broadcast(ptb,*BC_START)
sk_if_menu=cif(ptb, eq(ptb,Vrep(ptb,V_STATE),txt("menu")), sk_start)
sk_menu=broadcast(ptb,*BC_MENU)
sk_if_fim=cif(ptb, eq(ptb,Vrep(ptb,V_STATE),txt("fim")), sk_menu)
chain(ptb,[sk0,sk_if_menu,sk_if_fim])
# click
ck0=hat_clicked(ptb)
ck_start=broadcast(ptb,*BC_START)
ck_if_menu=cif(ptb, eq(ptb,Vrep(ptb,V_STATE),txt("menu")), ck_start)
ck_menu=broadcast(ptb,*BC_MENU)
ck_if_fim=cif(ptb, eq(ptb,Vrep(ptb,V_STATE),txt("fim")), ck_menu)
chain(ptb,[ck0,ck_if_menu,ck_if_fim])
fix_parents(ptb)
position_top(ptb,ps0,40,40); position_top(ptb,ph0,40,300); position_top(ptb,pb0,360,300)
position_top(ptb,pu0,40,520); position_top(ptb,sk0,40,760); position_top(ptb,ck0,500,760)

# ============================ NIVEL (banner de subida de nivel) ============================
# costumes: 1=NIVEL2 2=NIVEL3 3=NIVEL4 4=NIVEL5  -> costume index = NIVEL-1
ntb={}
# hide in menu/start/over
nh0=hat_recv(ntb,*BC_MENU); nh1=mk(ntb,"looks_hide"); chain(ntb,[nh0,nh1])
ns0=hat_recv(ntb,*BC_START); ns1=mk(ntb,"looks_hide"); chain(ntb,[ns0,ns1])
no0=hat_recv(ntb,*BC_OVER); no1=mk(ntb,"looks_hide"); chain(ntb,[no0,no1])
# animate on level up (own thread -> non-blocking)
na0=hat_recv(ntb,*BC_LEVELUP)
na1=switchcostume_num(ntb, subtract(ntb, Vrep(ntb,V_LEVEL), num(1)))
na2=seteffect(ntb,"ghost",0)
na3=setsize(ntb,40)
na4=gotoxy(ntb,num(0),num(120))
na5=mk(ntb,"looks_show")
na6=gofront(ntb)
grow=changesize(ntb,9); rgrow=repeatn(ntb,8,grow)
settle=changesize(ntb,-3.4); rsettle=repeatn(ntb,5,settle)
na7=waitsec(ntb,posn(0.5))
fade=changeeffect(ntb,"ghost",10); rfade=repeatn(ntb,10,fade)
na8=mk(ntb,"looks_hide")
chain(ntb,[na0,na1,na2,na3,na4,na5,na6,rgrow,rsettle,na7,rfade,na8])
fix_parents(ntb)
position_top(ntb,nh0,40,40); position_top(ntb,ns0,360,40); position_top(ntb,no0,680,40); position_top(ntb,na0,40,200)

# ============================ ASSEMBLE ============================
stage_vars={
 V_SCORE[1]:[V_SCORE[0],0], V_RECORD[1]:[V_RECORD[0],0], V_LEVEL[1]:[V_LEVEL[0],1],
 V_SPEED[1]:[V_SPEED[0],5], V_TRAIL[1]:[V_TRAIL[0],0.25], V_STATE[1]:[V_STATE[0],"menu"],
}
broadcasts={BC_MENU[1]:BC_MENU[0],BC_START[1]:BC_START[0],BC_OVER[1]:BC_OVER[0],BC_LEVELUP[1]:BC_LEVELUP[0]}

stage={
 "isStage":True,"name":"Stage","variables":stage_vars,"lists":{},"broadcasts":broadcasts,
 "blocks":stb,"comments":{},"currentCostume":0,
 "costumes":[
   {"name":"Menu","dataFormat":"svg","assetId":MENU,"md5ext":MENU+".svg","rotationCenterX":240,"rotationCenterY":180},
   {"name":"BG","dataFormat":"svg","assetId":BG,"md5ext":BG+".svg","rotationCenterX":240,"rotationCenterY":180},
   {"name":"level 2 cobrinha","bitmapResolution":2,"dataFormat":"png","assetId":"03a82c2be11da11c2ba3269194ab1339","md5ext":"03a82c2be11da11c2ba3269194ab1339.png","rotationCenterX":480,"rotationCenterY":360},
   {"name":"level 3 cobrinha","bitmapResolution":2,"dataFormat":"png","assetId":"b0fcaf39b6d413c226888d13fab73ab2","md5ext":"b0fcaf39b6d413c226888d13fab73ab2.png","rotationCenterX":480,"rotationCenterY":360},
   {"name":"level 4 cobrinha","bitmapResolution":2,"dataFormat":"png","assetId":"dddd22507d06382ce01641556b352680","md5ext":"dddd22507d06382ce01641556b352680.png","rotationCenterX":480,"rotationCenterY":360},
   {"name":"level 5 fim de jogo cobrinha","bitmapResolution":2,"dataFormat":"png","assetId":"0a67a26e0addf684c86113670ba028d9","md5ext":"0a67a26e0addf684c86113670ba028d9.png","rotationCenterX":480,"rotationCenterY":360},
   {"name":"GAME OVER","bitmapResolution":2,"dataFormat":"png","assetId":"44880a937e12278a93a7e692307e9060","md5ext":"44880a937e12278a93a7e692307e9060.png","rotationCenterX":479,"rotationCenterY":360},
 ],
 "sounds":[{"name":"pop","assetId":"83a9787d4cb6f3b7632b4ddfebf74367","dataFormat":"wav","format":"","rate":48000,"sampleCount":1123,"md5ext":"83a9787d4cb6f3b7632b4ddfebf74367.wav"}],
 "volume":100,"layerOrder":0,"tempo":60,"videoTransparency":50,"videoState":"on","textToSpeechLanguage":None,
}
cobra={
 "isStage":False,"name":"Cobra","variables":{},"lists":{},"broadcasts":{},"blocks":ctb,"comments":{},
 "currentCostume":0,
 "costumes":[
   {"name":"Cabeca","dataFormat":"svg","assetId":HEAD_OUT,"md5ext":HEAD_OUT+".svg","rotationCenterX":11,"rotationCenterY":11},
   {"name":"CabecaMeio","dataFormat":"svg","assetId":HEAD_MID,"md5ext":HEAD_MID+".svg","rotationCenterX":11,"rotationCenterY":11},
   {"name":"CabecaDentro","dataFormat":"svg","assetId":HEAD_IN,"md5ext":HEAD_IN+".svg","rotationCenterX":11,"rotationCenterY":11},
   {"name":"Corpo","dataFormat":"svg","assetId":YOUNG,"md5ext":YOUNG+".svg","rotationCenterX":8,"rotationCenterY":8},
   {"name":"CorpoMaduro","dataFormat":"svg","assetId":MATURE,"md5ext":MATURE+".svg","rotationCenterX":8,"rotationCenterY":8},
 ],
 "sounds":[{"name":"pop","assetId":"83a9787d4cb6f3b7632b4ddfebf74367","dataFormat":"wav","format":"","rate":48000,"sampleCount":1123,"md5ext":"83a9787d4cb6f3b7632b4ddfebf74367.wav"}],
 "volume":100,"layerOrder":2,"visible":False,"x":-60,"y":0,"size":100,"direction":90,
 "draggable":False,"rotationStyle":"all around",
}
apple={
 "isStage":False,"name":"Fruta","variables":{},"lists":{},"broadcasts":{},"blocks":atb,"comments":{},
 "currentCostume":0,
 "costumes":[
   {"name":"Apple","dataFormat":"svg","assetId":APPLE,"md5ext":APPLE+".svg","rotationCenterX":32,"rotationCenterY":32},
   {"name":"Banana","dataFormat":"svg","assetId":BANANA,"md5ext":BANANA+".svg","rotationCenterX":32,"rotationCenterY":32},
   {"name":"Uva","dataFormat":"svg","assetId":GRAPE,"md5ext":GRAPE+".svg","rotationCenterX":32,"rotationCenterY":32},
   {"name":"Cereja","dataFormat":"svg","assetId":CHERRY,"md5ext":CHERRY+".svg","rotationCenterX":32,"rotationCenterY":32},
   {"name":"Estrela","dataFormat":"svg","assetId":STAR,"md5ext":STAR+".svg","rotationCenterX":32,"rotationCenterY":32},
 ],
 "sounds":[{"name":"Chomp","assetId":"0b1e3033140d094563248e61de4039e5","dataFormat":"wav","rate":48000,"sampleCount":12678,"md5ext":"0b1e3033140d094563248e61de4039e5.wav"}],
 "volume":100,"layerOrder":3,"visible":False,"x":0,"y":0,"size":48,"direction":90,
 "draggable":False,"rotationStyle":"don't rotate",
}
press={
 "isStage":False,"name":"PressStart","variables":{},"lists":{},"broadcasts":{},"blocks":ptb,"comments":{},
 "currentCostume":0,
 "costumes":[
   {"name":"Jogar","dataFormat":"svg","assetId":PILLP,"md5ext":PILLP+".svg","rotationCenterX":170,"rotationCenterY":38},
   {"name":"Voltar","dataFormat":"svg","assetId":PILLB,"md5ext":PILLB+".svg","rotationCenterX":170,"rotationCenterY":38},
 ],
 "sounds":[],
 "volume":100,"layerOrder":1,"visible":False,"x":0,"y":-152,"size":100,"direction":90,
 "draggable":False,"rotationStyle":"all around",
}
nivel={
 "isStage":False,"name":"Nivel","variables":{},"lists":{},"broadcasts":{},"blocks":ntb,"comments":{},
 "currentCostume":0,
 "costumes":[
   {"name":"N2","dataFormat":"svg","assetId":NIVEL2,"md5ext":NIVEL2+".svg","rotationCenterX":150,"rotationCenterY":60},
   {"name":"N3","dataFormat":"svg","assetId":NIVEL3,"md5ext":NIVEL3+".svg","rotationCenterX":150,"rotationCenterY":60},
   {"name":"N4","dataFormat":"svg","assetId":NIVEL4,"md5ext":NIVEL4+".svg","rotationCenterX":150,"rotationCenterY":60},
   {"name":"N5","dataFormat":"svg","assetId":NIVEL5,"md5ext":NIVEL5+".svg","rotationCenterX":150,"rotationCenterY":60},
 ],
 "sounds":[],
 "volume":100,"layerOrder":4,"visible":False,"x":0,"y":120,"size":100,"direction":90,
 "draggable":False,"rotationStyle":"don't rotate",
}

def mon(vid,name,x,y,vis):
    return {"id":vid,"mode":"default","opcode":"data_variable","params":{"VARIABLE":name},
            "spriteName":None,"value":0,"width":0,"height":0,"x":x,"y":y,"visible":vis,
            "sliderMin":0,"sliderMax":100,"isDiscrete":True}
monitors=[
  mon(V_SCORE[1],V_SCORE[0],5,5,False),
  mon(V_LEVEL[1],V_LEVEL[0],5,40,False),
  mon(V_RECORD[1],V_RECORD[0],5,5,True),
]

project={"targets":[stage,cobra,apple,press,nivel],"monitors":monitors,
         "extensions":[],"meta":{"semver":"3.0.0","vm":"0.2.0","agent":""}}

json.dump(project, open(os.path.join(OUT,"project.json"),"w"), ensure_ascii=False)
print("project.json written, blocks:",len(stb),len(ctb),len(atb),len(ptb),len(ntb))
print("assets:",sorted(os.listdir(OUT)))
