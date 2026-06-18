# SVG assets for Cobrinha PRO
import math

HEAD_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="30" height="22" viewBox="0 0 30 22">
<defs><radialGradient id="hg" cx="40%" cy="35%" r="75%">
<stop offset="0%" stop-color="#FFB04A"/><stop offset="60%" stop-color="#FF6A00"/><stop offset="100%" stop-color="#E85A00"/>
</radialGradient></defs>
<path d="M19 11 L25 11 M25 11 L29 8.5 M25 11 L29 13.5" stroke="#E11D2A" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="11" cy="11" r="10" fill="url(#hg)" stroke="#C24A00" stroke-width="1.6"/>
<circle cx="14.5" cy="6.8" r="3.1" fill="#ffffff"/><circle cx="14.5" cy="15.2" r="3.1" fill="#ffffff"/>
<circle cx="15.8" cy="6.8" r="1.5" fill="#1a1a1a"/><circle cx="15.8" cy="15.2" r="1.5" fill="#1a1a1a"/>
<circle cx="15.3" cy="6.2" r="0.5" fill="#ffffff"/><circle cx="15.3" cy="14.6" r="0.5" fill="#ffffff"/>
</svg>'''

YOUNG_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
<defs><radialGradient id="yg" cx="38%" cy="35%" r="75%"><stop offset="0%" stop-color="#FFD27A"/><stop offset="100%" stop-color="#FF9E2D"/></radialGradient></defs>
<circle cx="8" cy="8" r="7" fill="url(#yg)" stroke="#E07A12" stroke-width="1.3"/></svg>'''

MATURE_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
<circle cx="8" cy="8" r="7.2" fill="#FF2D95" stroke="#C0186E" stroke-width="1.3"/>
<circle cx="6" cy="6" r="2.2" fill="#FF6FB6" opacity="0.6"/></svg>'''

PILL_PLAY_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="340" height="76" viewBox="0 0 340 76">
<defs><linearGradient id="pg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#FF6FB6"/><stop offset="100%" stop-color="#FF2D95"/></linearGradient></defs>
<rect x="4" y="4" width="332" height="68" rx="34" fill="url(#pg)" stroke="#ffffff" stroke-width="3"/>
<path d="M40 26 L40 50 L62 38 Z" fill="#ffffff"/>
<text x="190" y="48" font-family="Helvetica, Arial, sans-serif" font-size="25" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="1">PRESSIONE ESPACO</text>
</svg>'''

PILL_BACK_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="340" height="76" viewBox="0 0 340 76">
<defs><linearGradient id="pb" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#7AD0FF"/><stop offset="100%" stop-color="#1E8BFF"/></linearGradient></defs>
<rect x="4" y="4" width="332" height="68" rx="34" fill="url(#pb)" stroke="#ffffff" stroke-width="3"/>
<text x="170" y="47" font-family="Helvetica, Arial, sans-serif" font-size="24" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="1">ESPACO = MENU</text>
</svg>'''

def deco_snake():
    parts=[]
    n=18
    for i in range(n):
        t=i/(n-1)
        x=70 + i*20
        y=312 + 16*math.sin(i*0.55)
        r=12-3*t
        g=int(110+(45-110)*t); b=int(0+(149-0)*t)
        parts.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#%02X%02X%02X" stroke="#00000022" stroke-width="1"/>'%(x,y,r,255,g,b))
    hx=70+(n-1)*20; hy=312+16*math.sin((n-1)*0.55)
    parts.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="#fff"/><circle cx="%.1f" cy="%.1f" r="1.3" fill="#111"/>'%(hx+5,hy-3.5,hx+6.3,hy-3.5))
    parts.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="#fff"/><circle cx="%.1f" cy="%.1f" r="1.3" fill="#111"/>'%(hx+5,hy+3.5,hx+6.3,hy+3.5))
    parts.append('<path d="M%.1f %.1f L%.1f %.1f M%.1f %.1f L%.1f %.1f M%.1f %.1f L%.1f %.1f" stroke="#E11D2A" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'%(hx+11,hy,hx+19,hy,hx+19,hy,hx+24,hy-3,hx+19,hy,hx+24,hy+3))
    return "\n".join(parts)

MENU_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="360" viewBox="0 0 480 360">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#0c3b1e"/><stop offset="55%" stop-color="#11572b"/><stop offset="100%" stop-color="#0a2f18"/>
</linearGradient>
<linearGradient id="title" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#FFE36A"/><stop offset="100%" stop-color="#FF9E2D"/>
</linearGradient>
<linearGradient id="pro" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#FF6FB6"/><stop offset="100%" stop-color="#FF2D95"/>
</linearGradient>
<linearGradient id="flame" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#FFE36A"/><stop offset="55%" stop-color="#FF8A1E"/><stop offset="100%" stop-color="#E2331B"/>
</linearGradient>
<pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
<rect width="30" height="30" fill="none"/><path d="M30 0 L0 0 0 30" fill="none" stroke="#ffffff" stroke-opacity="0.05" stroke-width="1"/>
</pattern>
<filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="0.45"/></filter>
</defs>
<rect width="480" height="360" fill="url(#bg)"/>
<rect width="480" height="360" fill="url(#grid)"/>
<ellipse cx="240" cy="320" rx="280" ry="55" fill="#1bd15f" opacity="0.10"/>
__DECO__
<g transform="translate(410,300)"><circle r="15" fill="#EC1C2C" stroke="#9c1119" stroke-width="2"/><ellipse cx="-5" cy="-5" rx="3.5" ry="5" fill="#ffffff" opacity="0.55"/><rect x="-2" y="-21" width="4" height="9" rx="2" fill="#7a4a1d"/><path d="M2 -18 q9 -4 12 3 q-9 1 -12 -3" fill="#2e9d3a"/></g>
<g filter="url(#sh)" font-family="Helvetica, Arial, sans-serif" text-anchor="middle">
<text x="232" y="120" font-size="76" font-weight="900" fill="url(#title)" stroke="#5a3500" stroke-width="2" letter-spacing="2">COBRINHA</text>
<text x="208" y="184" font-size="60" font-weight="900" fill="url(#pro)" stroke="#6e1146" stroke-width="2" letter-spacing="6">PRO</text>
<path d="M300 188 q-16 -10 -6 -30 q4 14 14 12 q-10 12 4 22 q-9 4 -12 -4 z" fill="url(#flame)" stroke="#9a2a10" stroke-width="1.5"/>
</g>
<g font-family="Helvetica, Arial, sans-serif" text-anchor="middle" fill="#eafff0">
<text x="240" y="224" font-size="19" font-weight="bold">Use as SETAS para guiar a cobra</text>
<text x="240" y="250" font-size="15" opacity="0.92">Coma as macas para crescer e subir de nivel</text>
<text x="240" y="272" font-size="15" opacity="0.92">Atravesse as bordas, mas nao bata em si mesmo!</text>
</g>
</svg>'''.replace("__DECO__", deco_snake())
