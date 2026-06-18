# SVG assets for Cobrinha PRO  (v2: cenarios + frutas + cobra melhorada)
import math

# ----------------------------- SNAKE -----------------------------
# Head with a parametric tongue so it can flick in and out (3 frames).
def head_svg(tongue):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="30" height="22" viewBox="0 0 30 22">'
    '<defs><radialGradient id="hg" cx="38%" cy="32%" r="80%">'
    '<stop offset="0%" stop-color="#FFC766"/><stop offset="55%" stop-color="#FF7A12"/><stop offset="100%" stop-color="#DD5400"/>'
    '</radialGradient></defs>'
    + tongue +
    '<circle cx="11" cy="11" r="10" fill="url(#hg)" stroke="#B83F00" stroke-width="1.7"/>'
    '<path d="M3 8 Q11 3 19 8" stroke="#FFD9A0" stroke-width="1.2" fill="none" opacity="0.6" stroke-linecap="round"/>'
    '<circle cx="17.5" cy="13.3" r="0.7" fill="#9b3b00"/><circle cx="17.5" cy="8.7" r="0.7" fill="#9b3b00"/>'
    '<circle cx="14.3" cy="6.8" r="3.2" fill="#ffffff"/><circle cx="14.3" cy="15.2" r="3.2" fill="#ffffff"/>'
    '<circle cx="15.7" cy="6.8" r="1.6" fill="#1a1a1a"/><circle cx="15.7" cy="15.2" r="1.6" fill="#1a1a1a"/>'
    '<circle cx="15.1" cy="6.1" r="0.6" fill="#ffffff"/><circle cx="15.1" cy="14.5" r="0.6" fill="#ffffff"/>'
    '</svg>')

_TONGUE_OUT = '<path d="M19 11 L25 11 M25 11 L29.2 8.0 M25 11 L29.2 14.0" stroke="#E11D2A" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
_TONGUE_MID = '<path d="M19 11 L23 11 M23 11 L25.6 9.4 M23 11 L25.6 12.6" stroke="#E11D2A" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
_TONGUE_IN  = '<path d="M19.5 11 L21.2 11 M21.2 11 L22.2 10.3 M21.2 11 L22.2 11.7" stroke="#E11D2A" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'

HEAD_OUT = head_svg(_TONGUE_OUT)
HEAD_MID = head_svg(_TONGUE_MID)
HEAD_IN  = head_svg(_TONGUE_IN)
HEAD_SVG = HEAD_OUT  # backwards-compat alias

YOUNG_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
<defs><radialGradient id="yg" cx="36%" cy="32%" r="78%"><stop offset="0%" stop-color="#FFE0A0"/><stop offset="60%" stop-color="#FFA836"/><stop offset="100%" stop-color="#F08A14"/></radialGradient></defs>
<circle cx="8" cy="8" r="7.1" fill="url(#yg)" stroke="#D9760E" stroke-width="1.2"/>
<ellipse cx="5.6" cy="5.4" rx="2.4" ry="1.8" fill="#ffffff" opacity="0.45"/></svg>'''

MATURE_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
<defs><radialGradient id="mg" cx="36%" cy="32%" r="80%"><stop offset="0%" stop-color="#FF73B6"/><stop offset="45%" stop-color="#FF2D95"/><stop offset="100%" stop-color="#E81E83"/></radialGradient></defs>
<circle cx="8" cy="8" r="7.2" fill="url(#mg)" stroke="#B01570" stroke-width="1.2"/>
<circle cx="8" cy="8" r="3.4" fill="#FF2D95"/>
<ellipse cx="5.6" cy="5.4" rx="2.3" ry="1.7" fill="#ffffff" opacity="0.40"/></svg>'''

# ----------------------------- FRUITS -----------------------------
APPLE_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
<defs><radialGradient id="ap" cx="38%" cy="34%" r="72%"><stop offset="0%" stop-color="#FF6A6A"/><stop offset="60%" stop-color="#E51E25"/><stop offset="100%" stop-color="#B00C12"/></radialGradient></defs>
<path d="M32 14 q5 -7 12 -5 q-2 6 -8 7" fill="#3aa84a" stroke="#2c7d38" stroke-width="1"/>
<rect x="30.5" y="9" width="3" height="9" rx="1.5" fill="#7a4a1d"/>
<path d="M32 18 C20 16 12 24 12 36 C12 50 22 56 32 52 C42 56 52 50 52 36 C52 24 44 16 32 18 Z" fill="url(#ap)" stroke="#8f0a10" stroke-width="1.5"/>
<ellipse cx="23" cy="30" rx="5" ry="8" fill="#ffffff" opacity="0.35"/></svg>'''

BANANA_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
<defs><linearGradient id="bn" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FFE45C"/><stop offset="100%" stop-color="#F2C020"/></linearGradient></defs>
<path d="M14 20 C16 40 30 52 50 50 C52 50 54 48 53 46 C36 47 24 36 22 19 C22 17 15 16 14 20 Z" fill="url(#bn)" stroke="#C99A10" stroke-width="2"/>
<path d="M18 22 C22 38 32 47 48 47" fill="none" stroke="#E8B41C" stroke-width="1.5" opacity="0.7"/>
<path d="M50 50 l5 -2 l-3 4 z" fill="#6b4a14"/><path d="M19 18 l-3 -3 l5 1 z" fill="#6b4a14"/></svg>'''

CHERRY_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
<defs><radialGradient id="ch" cx="38%" cy="34%" r="70%"><stop offset="0%" stop-color="#FF5C7A"/><stop offset="100%" stop-color="#D5102F"/></radialGradient></defs>
<path d="M30 16 C30 30 18 30 16 40" fill="none" stroke="#3aa84a" stroke-width="2.5" stroke-linecap="round"/>
<path d="M34 16 C36 30 46 32 48 42" fill="none" stroke="#3aa84a" stroke-width="2.5" stroke-linecap="round"/>
<path d="M30 14 q6 -6 12 -2 q-3 7 -10 6 q9 3 4 9 q-9 -1 -6 -13 Z" fill="#3aa84a" stroke="#2c7d38" stroke-width="1"/>
<circle cx="16" cy="46" r="11" fill="url(#ch)" stroke="#8f0a1c" stroke-width="1.5"/>
<circle cx="48" cy="47" r="11" fill="url(#ch)" stroke="#8f0a1c" stroke-width="1.5"/>
<ellipse cx="12.5" cy="42.5" rx="3" ry="4.5" fill="#fff" opacity="0.45"/>
<ellipse cx="44.5" cy="43.5" rx="3" ry="4.5" fill="#fff" opacity="0.45"/></svg>'''

GRAPE_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
<defs><radialGradient id="gr" cx="36%" cy="32%" r="75%"><stop offset="0%" stop-color="#B98CFF"/><stop offset="100%" stop-color="#7A2FD0"/></radialGradient></defs>
<rect x="30" y="8" width="3" height="9" rx="1.5" fill="#7a4a1d"/>
<path d="M33 12 q8 -5 13 0 q-6 4 -12 1" fill="#3aa84a" stroke="#2c7d38" stroke-width="1"/>'''+ "".join(
 '<circle cx="%d" cy="%d" r="6.5" fill="url(#gr)" stroke="#5a1ba0" stroke-width="1"/>'%(x,y)
 for (x,y) in [(26,24),(38,24),(20,33),(32,33),(44,33),(26,42),(38,42),(32,51)]) + '''
<circle cx="24" cy="22" r="1.8" fill="#fff" opacity="0.5"/></svg>'''

STAR_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
<defs><radialGradient id="st" cx="50%" cy="40%" r="60%"><stop offset="0%" stop-color="#FFF7B0"/><stop offset="60%" stop-color="#FFD21E"/><stop offset="100%" stop-color="#F5A300"/></radialGradient>
<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#FFE36A" stop-opacity="0.7"/><stop offset="100%" stop-color="#FFE36A" stop-opacity="0"/></radialGradient></defs>
<circle cx="32" cy="32" r="30" fill="url(#glow)"/>
<path d="M32 8 L39.6 24.2 L57 26.4 L44.2 38.6 L47.6 56 L32 47.4 L16.4 56 L19.8 38.6 L7 26.4 L24.4 24.2 Z" fill="url(#st)" stroke="#C98200" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M30 20 L34 20 L33 30 L31 30 Z" fill="#fff" opacity="0.5"/></svg>'''

# ----------------------------- MENU -----------------------------
def deco_snake():
    parts=[]
    n=18
    for i in range(n):
        t=i/(n-1)
        x=70 + i*20
        y=315 + 14*math.sin(i*0.55)
        r=12-3*t
        g=int(110+(45-110)*t); b=int(0+(149-0)*t)
        parts.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#%02X%02X%02X" stroke="#00000022" stroke-width="1"/>'%(x,y,r,255,g,b))
    hx=70+(n-1)*20; hy=315+14*math.sin((n-1)*0.55)
    parts.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="#fff"/><circle cx="%.1f" cy="%.1f" r="1.3" fill="#111"/>'%(hx+5,hy-3.5,hx+6.3,hy-3.5))
    parts.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="#fff"/><circle cx="%.1f" cy="%.1f" r="1.3" fill="#111"/>'%(hx+5,hy+3.5,hx+6.3,hy+3.5))
    parts.append('<path d="M%.1f %.1f L%.1f %.1f M%.1f %.1f L%.1f %.1f M%.1f %.1f L%.1f %.1f" stroke="#E11D2A" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'%(hx+11,hy,hx+19,hy,hx+19,hy,hx+24,hy-3,hx+19,hy,hx+24,hy+3))
    return "\n".join(parts)

def sparkles():
    pts=[(60,70,2),(120,40,1.5),(200,55,2.5),(300,38,1.5),(380,66,2),(430,48,2.5),
         (40,150,1.5),(450,160,2),(95,205,1.5),(395,210,1.5),(250,32,1.8),(160,80,1.4)]
    out=[]
    for x,y,r in pts:
        out.append('<g transform="translate(%d,%d)"><path d="M0 -%d L%.1f 0 L0 %d L-%.1f 0 Z" fill="#ffffff" opacity="0.8"/></g>'%(x,y,int(r*2),r,int(r*2),r))
    return "\n".join(out)

# little fruit icons row for the menu legend
def fruit_icon(kind):
    if kind=='apple':
        return '<rect x="-1.2" y="-9" width="2.4" height="6" rx="1" fill="#7a4a1d"/><path d="M-9 -2 C-9 -8 9 -8 9 -2 C9 6 4 9 0 7 C-4 9 -9 6 -9 -2 Z" fill="#E51E25" stroke="#8f0a10" stroke-width="1"/>'
    if kind=='cherry':
        return '<circle cx="-4" cy="4" r="5.5" fill="#D5102F" stroke="#8f0a1c" stroke-width="1"/><circle cx="5" cy="5" r="5.5" fill="#D5102F" stroke="#8f0a1c" stroke-width="1"/><path d="M-4 -2 C-3 -8 4 -8 5 0" fill="none" stroke="#3aa84a" stroke-width="1.6"/>'
    if kind=='grape':
        return "".join('<circle cx="%d" cy="%d" r="3" fill="#7A2FD0"/>'%(x,y) for x,y in [(-4,-2),(2,-2),(-7,2),(-1,2),(5,2),(-4,6),(2,6)])
    if kind=='star':
        return '<path d="M0 -9 L2.6 -2.6 L9 -2 L4 2.4 L5.4 9 L0 5.2 L-5.4 9 L-4 2.4 L-9 -2 L-2.6 -2.6 Z" fill="#FFD21E" stroke="#C98200" stroke-width="1"/>'
    return ''

MENU_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
<defs>
<radialGradient id="bg" cx="50%" cy="36%" r="80%">
<stop offset="0%" stop-color="#16713a"/><stop offset="60%" stop-color="#0f5128"/><stop offset="100%" stop-color="#072e16"/>
</radialGradient>
<linearGradient id="title" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FFF1A0"/><stop offset="55%" stop-color="#FFD21E"/><stop offset="100%" stop-color="#FF9E2D"/></linearGradient>
<linearGradient id="pro" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FF8AC6"/><stop offset="100%" stop-color="#FF2D95"/></linearGradient>
<linearGradient id="flame" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FFE36A"/><stop offset="55%" stop-color="#FF8A1E"/><stop offset="100%" stop-color="#E2331B"/></linearGradient>
<filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="0.5"/></filter>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="480" height="360" fill="url(#bg)"/>
__GRID__
__SPARKLES__
<rect x="10" y="10" width="460" height="340" rx="22" fill="none" stroke="#2effa6" stroke-opacity="0.35" stroke-width="3" filter="url(#glow)"/>
<rect x="10" y="10" width="460" height="340" rx="22" fill="none" stroke="#b6ffe0" stroke-opacity="0.5" stroke-width="1.4"/>
<ellipse cx="240" cy="322" rx="300" ry="50" fill="#1bd15f" opacity="0.10"/>
__DECO__
<g filter="url(#sh)" font-family="Helvetica, Arial, sans-serif" text-anchor="middle">
<text x="232" y="120" font-size="76" font-weight="900" fill="url(#title)" stroke="#5a3500" stroke-width="2" letter-spacing="2">COBRINHA</text>
<text x="208" y="182" font-size="58" font-weight="900" fill="url(#pro)" stroke="#6e1146" stroke-width="2" letter-spacing="6">PRO</text>
<path d="M298 186 q-16 -10 -6 -30 q4 14 14 12 q-10 12 4 22 q-9 4 -12 -4 z" fill="url(#flame)" stroke="#9a2a10" stroke-width="1.5"/>
</g>
<g font-family="Helvetica, Arial, sans-serif" text-anchor="middle" fill="#eafff0">
<text x="240" y="214" font-size="18" font-weight="bold">Use as SETAS  -  atravesse as 4 bordas!</text>
<text x="240" y="236" font-size="14" opacity="0.92">Colete as frutas e nao bata no proprio corpo</text>
</g>
<g font-family="Helvetica, Arial, sans-serif" fill="#fff" font-size="13" text-anchor="middle">
<g transform="translate(150,262)">__FA__<text x="0" y="22">+1</text></g>
<g transform="translate(205,262)">__FC__<text x="0" y="22">+2</text></g>
<g transform="translate(260,262)">__FG__<text x="0" y="22">+1</text></g>
<g transform="translate(322,262)">__FS__<text x="0" y="22">+3</text></g>
</g>
</svg>'''
# subtle grid lines (explicit, no <pattern>)
_grid=[]
for gx in range(0,481,40): _grid.append('<line x1="%d" y1="0" x2="%d" y2="360" stroke="#ffffff" stroke-opacity="0.04" stroke-width="1"/>'%(gx,gx))
for gy in range(0,361,40): _grid.append('<line x1="0" y1="%d" x2="480" y2="%d" stroke="#ffffff" stroke-opacity="0.04" stroke-width="1"/>'%(gy,gy))
MENU_SVG=(MENU_SVG.replace("__GRID__","\n".join(_grid)).replace("__SPARKLES__",sparkles())
          .replace("__DECO__",deco_snake())
          .replace("__FA__",fruit_icon('apple')).replace("__FC__",fruit_icon('cherry'))
          .replace("__FG__",fruit_icon('grape')).replace("__FS__",fruit_icon('star')))

# ----------------------------- IN-GAME BACKGROUND -----------------------------
def _bg():
    tiles=[]
    cols=16; rows=12; w=480/cols; h=360/rows
    for r in range(rows):
        for c in range(cols):
            col = "#8CC62E" if (r+c)%2==0 else "#A6E04A"
            tiles.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>'%(c*w,r*h,w+0.5,h+0.5,col))
    return "\n".join(tiles)
BG_SVG='''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
<defs>
<radialGradient id="vig" cx="50%" cy="48%" r="70%"><stop offset="60%" stop-color="#000000" stop-opacity="0"/><stop offset="100%" stop-color="#0a3010" stop-opacity="0.55"/></radialGradient>
<linearGradient id="frame" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#2effa6"/><stop offset="100%" stop-color="#19c2ff"/></linearGradient>
<filter id="fglow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter>
</defs>
__TILES__
<rect width="480" height="360" fill="url(#vig)"/>
<rect x="6" y="6" width="468" height="348" rx="16" fill="none" stroke="url(#frame)" stroke-opacity="0.6" stroke-width="5" filter="url(#fglow)"/>
<rect x="6" y="6" width="468" height="348" rx="16" fill="none" stroke="#eafff7" stroke-opacity="0.7" stroke-width="1.6"/>
</svg>'''.replace("__TILES__",_bg())

# ----------------------------- PRESS START PILL -----------------------------
PILL_PLAY_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="340" height="76" viewBox="0 0 340 76">
<defs><linearGradient id="pg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FF8AC6"/><stop offset="100%" stop-color="#FF2D95"/></linearGradient></defs>
<rect x="4" y="4" width="332" height="68" rx="34" fill="url(#pg)" stroke="#ffffff" stroke-width="3"/>
<path d="M40 26 L40 50 L62 38 Z" fill="#ffffff"/>
<text x="190" y="48" font-family="Helvetica, Arial, sans-serif" font-size="25" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="1">PRESSIONE ESPACO</text>
</svg>'''
PILL_BACK_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="340" height="76" viewBox="0 0 340 76">
<defs><linearGradient id="pb" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#7AD0FF"/><stop offset="100%" stop-color="#1E8BFF"/></linearGradient></defs>
<rect x="4" y="4" width="332" height="68" rx="34" fill="url(#pb)" stroke="#ffffff" stroke-width="3"/>
<text x="170" y="47" font-family="Helvetica, Arial, sans-serif" font-size="24" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="1">ESPACO = MENU</text>
</svg>'''

# ----------------------------- LEVEL-UP BANNER -----------------------------
def level_badge(n, c1, c2):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="300" height="120" viewBox="0 0 300 120">'
    '<defs>'
    '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="C1"/><stop offset="100%" stop-color="C2"/></linearGradient>'
    '<filter id="g" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="5"/></filter>'
    '</defs>'
    '<rect x="22" y="34" width="256" height="58" rx="29" fill="C2" opacity="0.55" filter="url(#g)"/>'
    '<rect x="24" y="30" width="252" height="58" rx="29" fill="url(#bg)" stroke="#ffffff" stroke-width="3.5"/>'
    '<path d="M150 8 l4 9 l10 1 l-7 7 l2 10 l-9 -5 l-9 5 l2 -10 l-7 -7 l10 -1 z" fill="#FFE36A" stroke="#caa400" stroke-width="1.2"/>'
    '<text x="150" y="70" font-family="Helvetica, Arial, sans-serif" font-size="34" font-weight="900" fill="#ffffff" text-anchor="middle" stroke="#00000033" stroke-width="0.6" letter-spacing="2">NIVEL NUM</text>'
    '</svg>').replace("NUM", str(n)).replace("C1", c1).replace("C2", c2)

NIVEL2 = level_badge(2, "#5BE584", "#1Fae54")   # green
NIVEL3 = level_badge(3, "#6FD0FF", "#1E8BFF")   # blue
NIVEL4 = level_badge(4, "#C79BFF", "#7A2FD0")   # purple
NIVEL5 = level_badge(5, "#FFE36A", "#F5A300")   # gold
