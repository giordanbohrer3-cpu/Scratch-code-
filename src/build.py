import json, hashlib, os, shutil, sys
sys.path.insert(0,'/tmp/build')
import assets

SRC="/tmp/sb3"               # original extracted sb3
OUT="/tmp/build/project"     # new project dir
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)

# ---- keep original binary assets ----
KEEP = [
 "67fa25c297d4605eaa15d2739116e9aa.png", # BG
 "03a82c2be11da11c2ba3269194ab1339.png", # level2
 "b0fcaf39b6d413c226888d13fab73ab2.png", # level3
 "dddd22507d06382ce01641556b352680.png", # level4
 "0a67a26e0addf684c86113670ba028d9.png", # level5
 "44880a937e12278a93a7e692307e9060.png", # GAME OVER
 "3826a4091a33e4d26f87a2fac7cf796b.svg", # apple
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
HEAD=add_svg(assets.HEAD_SVG)
YOUNG=add_svg(assets.YOUNG_SVG)
MATURE=add_svg(assets.MATURE_SVG)
MENU=add_svg(assets.MENU_SVG)
PILLP=add_svg(assets.PILL_PLAY_SVG)
PILLB=add_svg(assets.PILL_BACK_SVG)

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
# forever body
mv=movesteps(ctb,rep(Vrep(ctb,V_SPEED)))
# wrap ifs
w1=cif(ctb, gt(ctb,xpos(ctb),num(240)), setx(ctb,num(-240)))
w2=cif(ctb, lt(ctb,xpos(ctb),num(-240)), setx(ctb,num(240)))
w3=cif(ctb, gt(ctb,ypos(ctb),num(176)), sety(ctb,num(-176)))
w4=cif(ctb, lt(ctb,ypos(ctb),num(-176)), sety(ctb,num(176)))
cl=createclone(ctb)
# self collision
deadbc=broadcast(ctb,*BC_OVER)
deadstop=stopthis(ctb)
chain(ctb,[deadbc,deadstop])
deadif=cif(ctb, touchingcolor(ctb,"#FF2D95"), deadbc)
# level ups (highest first)
def levelup(level, speed, backdrop):
    cond=And(ctb, Not(ctb, lt(ctb,Vrep(ctb,V_SCORE),num({5:5,4:15,3:10,2:5}[level] if False else 0))), eq(ctb,num(0),num(0)))
    return cond
# build level ifs explicitly
def lvif(score_th, lvl, speed, backdrop):
    cond=And(ctb,
             Not(ctb, lt(ctb, Vrep(ctb,V_SCORE), num(score_th))),   # score >= th
             lt(ctb, Vrep(ctb,V_LEVEL), num(lvl)))                  # level < lvl
    a=setvar(ctb,V_LEVEL[0],V_LEVEL[1],num(lvl))
    b=setvar(ctb,V_SPEED[0],V_SPEED[1],num(speed))
    c=switchbackdrop(ctb,backdrop)
    d=waitsec(ctb,posn(0.8))
    e=switchbackdrop(ctb,"BG")
    chain(ctb,[a,b,c,d,e])
    return cif(ctb,cond,a)
L5=lvif(20,5,9,"level 5 fim de jogo cobrinha")
L4=lvif(15,4,8,"level 4 cobrinha")
L3=lvif(10,3,7,"level 3 cobrinha")
L2=lvif(5,2,6,"level 2 cobrinha")
chain(ctb,[mv,w1,w2,w3,w4,cl,deadif,L5,L4,L3,L2])
fbody=mv
fev=forever(ctb,fbody)
chain(ctb,[e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,fev])

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

# ---- clone cleanup on start ----
cc0=hat_recv(ctb,*BC_START)
cc1=cif(ctb, gt(ctb,costnum(ctb),num(1)), delclone(ctb))
chain(ctb,[cc0,cc1])

# ---- death fx (only the head/original, not body clones) ----
d0=hat_recv(ctb,*BC_OVER)
d1=setvar(ctb,V_STATE[0],V_STATE[1],txt("fim"))
d2=playsound(ctb,"pop")
d3=cif(ctb, gt(ctb,Vrep(ctb,V_SCORE),Vrep(ctb,V_RECORD)),
        setvar(ctb,V_RECORD[0],V_RECORD[1],rep(Vrep(ctb,V_SCORE))))
chain(ctb,[d1,d2,d3])
dguard=cif(ctb, eq(ctb,costnum(ctb),num(1)), d1)
chain(ctb,[d0,dguard])

# ---- hide on menu ----
h0=hat_recv(ctb,*BC_MENU)
h1=mk(ctb,"looks_hide")
h2=setvar(ctb,V_STATE[0],V_STATE[1],txt("menu"))
chain(ctb,[h0,h1,h2])

fix_parents(ctb)
position_top(ctb,e0,40,40); position_top(ctb,i0,500,40); position_top(ctb,b0,900,40)
position_top(ctb,cc0,1250,40); position_top(ctb,d0,40,760); position_top(ctb,h0,500,760)

# ============================ APPLE ============================
atb={}
a0=hat_recv(atb,*BC_START)
a1=mk(atb,"looks_show")
a2=gotoxy(atb,rnd(atb,-210,210),rnd(atb,-150,150))
# forever eat
eat_play=playsound(atb,"Chomp")
eat_sc=changevar(atb,V_SCORE[0],V_SCORE[1],num(1))
eat_tr=changevar(atb,V_TRAIL[0],V_TRAIL[1],num(0.05))
rep_goto=gotoxy(atb,rnd(atb,-210,210),rnd(atb,-150,150))
rep_loop=repeatuntil(atb, Not(atb,touchingobj(atb,"Cobra")), rep_goto)
chain(atb,[eat_play,eat_sc,eat_tr,rep_loop])
eatif=cif(atb, touchingobj(atb,"Cobra"), eat_play)
af=forever(atb,eatif)
chain(atb,[a0,a1,a2,af])
# hide on menu/over
ah0=hat_recv(atb,*BC_MENU); ah1=mk(atb,"looks_hide"); chain(atb,[ah0,ah1])
ao0=hat_recv(atb,*BC_OVER); ao1=mk(atb,"looks_hide"); chain(atb,[ao0,ao1])
fix_parents(atb)
position_top(atb,a0,40,40); position_top(atb,ah0,40,400); position_top(atb,ao0,360,400)

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

# ============================ ASSEMBLE ============================
stage_vars={
 V_SCORE[1]:[V_SCORE[0],0], V_RECORD[1]:[V_RECORD[0],0], V_LEVEL[1]:[V_LEVEL[0],1],
 V_SPEED[1]:[V_SPEED[0],5], V_TRAIL[1]:[V_TRAIL[0],0.25], V_STATE[1]:[V_STATE[0],"menu"],
}
broadcasts={BC_MENU[1]:BC_MENU[0],BC_START[1]:BC_START[0],BC_OVER[1]:BC_OVER[0]}

stage={
 "isStage":True,"name":"Stage","variables":stage_vars,"lists":{},"broadcasts":broadcasts,
 "blocks":stb,"comments":{},"currentCostume":0,
 "costumes":[
   {"name":"Menu","dataFormat":"svg","assetId":MENU,"md5ext":MENU+".svg","rotationCenterX":240,"rotationCenterY":180},
   {"name":"BG","bitmapResolution":2,"dataFormat":"png","assetId":"67fa25c297d4605eaa15d2739116e9aa","md5ext":"67fa25c297d4605eaa15d2739116e9aa.png","rotationCenterX":479,"rotationCenterY":360},
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
   {"name":"Cabeca","dataFormat":"svg","assetId":HEAD,"md5ext":HEAD+".svg","rotationCenterX":11,"rotationCenterY":11},
   {"name":"Corpo","dataFormat":"svg","assetId":YOUNG,"md5ext":YOUNG+".svg","rotationCenterX":8,"rotationCenterY":8},
   {"name":"CorpoMaduro","dataFormat":"svg","assetId":MATURE,"md5ext":MATURE+".svg","rotationCenterX":8,"rotationCenterY":8},
 ],
 "sounds":[{"name":"pop","assetId":"83a9787d4cb6f3b7632b4ddfebf74367","dataFormat":"wav","format":"","rate":48000,"sampleCount":1123,"md5ext":"83a9787d4cb6f3b7632b4ddfebf74367.wav"}],
 "volume":100,"layerOrder":2,"visible":False,"x":-60,"y":0,"size":100,"direction":90,
 "draggable":False,"rotationStyle":"all around",
}
apple={
 "isStage":False,"name":"Apple","variables":{},"lists":{},"broadcasts":{},"blocks":atb,"comments":{},
 "currentCostume":0,
 "costumes":[{"name":"Apple","bitmapResolution":1,"dataFormat":"svg","assetId":"3826a4091a33e4d26f87a2fac7cf796b","md5ext":"3826a4091a33e4d26f87a2fac7cf796b.svg","rotationCenterX":31,"rotationCenterY":31}],
 "sounds":[{"name":"Chomp","assetId":"0b1e3033140d094563248e61de4039e5","dataFormat":"wav","rate":48000,"sampleCount":12678,"md5ext":"0b1e3033140d094563248e61de4039e5.wav"}],
 "volume":100,"layerOrder":3,"visible":False,"x":0,"y":0,"size":45,"direction":90,
 "draggable":False,"rotationStyle":"all around",
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

def mon(vid,name,x,y,vis):
    return {"id":vid,"mode":"default","opcode":"data_variable","params":{"VARIABLE":name},
            "spriteName":None,"value":0,"width":0,"height":0,"x":x,"y":y,"visible":vis,
            "sliderMin":0,"sliderMax":100,"isDiscrete":True}
monitors=[
  mon(V_SCORE[1],V_SCORE[0],5,5,False),
  mon(V_LEVEL[1],V_LEVEL[0],5,40,False),
  mon(V_RECORD[1],V_RECORD[0],5,5,True),
]

project={"targets":[stage,cobra,apple,press],"monitors":monitors,
         "extensions":[],"meta":{"semver":"3.0.0","vm":"0.2.0","agent":""}}

json.dump(project, open(os.path.join(OUT,"project.json"),"w"), ensure_ascii=False)
print("project.json written, blocks:",len(stb),len(ctb),len(atb),len(ptb))
print("assets:",sorted(os.listdir(OUT)))
