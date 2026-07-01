# -*- coding: utf-8 -*-
"""gen_sounds.py - sintetiza música e efeitos (WAV 22050 Hz, 16-bit mono) de
forma procedural (sem direitos autorais), com cara de jogo de plataforma
divertido e imersivo. Devolve dict nome->(bytes, rate, sampleCount)."""
import numpy as np, io, wave

RATE = 22050


def to_wav(x):
    x = np.clip(x, -1, 1)
    pcm = (x * 32767).astype('<i2')
    buf = io.BytesIO()
    w = wave.open(buf, 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE)
    w.writeframes(pcm.tobytes()); w.close()
    return buf.getvalue(), RATE, len(x)


def tarr(dur): return np.arange(int(dur * RATE)) / RATE
def midi(n):   return 440.0 * 2 ** ((n - 69) / 12.0)


def ar(n, a=0.004, r=0.04):
    e = np.ones(n); ai = max(1, int(a * RATE)); ri = max(1, int(r * RATE))
    e[:ai] = np.linspace(0, 1, ai); e[-ri:] *= np.linspace(1, 0, ri)
    return e


def add(out, seg, st):
    e = min(len(seg), len(out) - st)
    if e > 0:
        out[st:st + e] += seg[:e]


def bell(freq, dur, amp=0.5, decay=6.0):
    t = tarr(dur)
    s = (np.sin(2 * np.pi * freq * t) + 0.5 * np.sin(2 * np.pi * 2 * freq * t)
         + 0.22 * np.sin(2 * np.pi * 3 * freq * t))
    s *= np.exp(-decay * t) * ar(len(t), 0.002, 0.02)
    return amp * s / 1.72


# ---- osciladores chiptune ----
def sq(freq, t, duty=0.5):  return np.where(((freq * t) % 1.0) < duty, 1.0, -1.0)
def tri(freq, t):           return 2.0 / np.pi * np.arcsin(np.sin(2 * np.pi * freq * t))


def lead(freq, dur, amp=0.16, duty=0.5):
    t = tarr(dur)
    return amp * sq(freq, t, duty) * ar(len(t), 0.004, 0.03) * np.exp(-1.4 * t)


def bass(freq, dur, amp=0.24):
    t = tarr(dur)
    return amp * tri(freq, t) * ar(len(t), 0.004, 0.02) * np.exp(-1.0 * t)


def kick():
    t = tarr(0.13); f = np.linspace(150, 48, len(t))
    return 0.7 * np.sin(2 * np.pi * f * t) * np.exp(-16 * t)


def snare():
    t = tarr(0.13); rs = np.random.RandomState(7)
    return 0.35 * rs.randn(len(t)) * np.exp(-26 * t) + 0.2 * np.sin(2 * np.pi * 190 * t) * np.exp(-30 * t)


def hat():
    t = tarr(0.03); rs = np.random.RandomState(11)
    return 0.16 * rs.randn(len(t)) * np.exp(-120 * t)


def sweep(f0, f1, dur, square=False):
    t = tarr(dur); f = np.linspace(f0, f1, len(t))
    ph = 2 * np.pi * np.cumsum(f) / RATE
    return (np.sign(np.sin(ph)) if square else np.sin(ph)), t


# ==========================================================================
def music():           # corrida energética — homenagem ao estilo arcade racer
    bpm = 150; b = 60.0 / bpm; s = b / 4.0          # s = semicolcheia (16th)
    # cadência andaluza Am-G-F-E (i-VII-VI-V): tensão "de corrida", fecha o loop
    prog = [(45, [0, 3, 7]), (43, [0, 4, 7]), (41, [0, 4, 7]), (40, [0, 4, 7])] * 2
    barlen = 16 * s
    out = np.zeros(int(len(prog) * barlen * RATE) + RATE)
    for bi, (r, iv) in enumerate(prog):
        b0 = bi * barlen
        # baixo galopante (semicolcheias): pulso incessante, sensação de velocidade
        bp = [r, r + 12, r, r + 7, r, r + 12, r, r + 7,
              r, r + 12, r, r + 7, r, r + 12, r + 7, r + 12]
        for k, nn in enumerate(bp):
            add(out, bass(midi(nn), s * 1.05, 0.24), int((b0 + k * s) * RATE))
        # power chords (raiz + 5ª) nas semínimas: peso "rock"
        for k in range(4):
            tt = tarr(b * 0.9)
            pc = 0.085 * (sq(midi(r + 12), tt) + sq(midi(r + 19), tt))
            pc *= ar(len(tt), 0.003, 0.05) * np.exp(-2.2 * tt)
            add(out, pc, int((b0 + k * 4 * s) * RATE))
        # lead (colcheias): melodia brilhante voando por cima do galope
        mel = [r + 24 + iv[0], r + 24 + iv[1], r + 24 + iv[2], r + 24 + iv[1],
               r + 24 + iv[2], r + 36, r + 24 + iv[2], r + 24 + iv[1]]
        for k, nn in enumerate(mel):
            add(out, lead(midi(nn), s * 1.9, 0.14, 0.5), int((b0 + k * 2 * s) * RATE))
        # bateria: kick four-on-the-floor, caixa em 2 e 4, chimbais em 16th
        for k in range(16):
            tp = int((b0 + k * s) * RATE)
            if k % 2 == 0: add(out, hat() * 0.4, tp)
            if k in (0, 4, 8, 12): add(out, kick(), tp)
            if k in (4, 12): add(out, snare() * 0.7, tp)
    out = out[:int(len(prog) * barlen * RATE)]
    out *= 0.74 / np.max(np.abs(out))
    f = int(0.004 * RATE); out[:f] *= np.linspace(0, 1, f); out[-f:] *= np.linspace(1, 0, f)
    return to_wav(out)


def click():           # clicar em Jogar
    t = tarr(0.10)
    s = np.sin(2 * np.pi * np.linspace(820, 1500, len(t)) * t) * np.exp(-26 * t)
    s += 0.3 * np.sin(2 * np.pi * np.linspace(1640, 3000, len(t)) * t) * np.exp(-32 * t)
    return to_wav(0.5 * s * ar(len(t), 0.001, 0.02))


def collect():         # coletar item (arpejo brilhante E5 G5 C6)
    out = np.zeros(int(0.36 * RATE))
    for i, nn in enumerate([76, 79, 84]):
        add(out, bell(midi(nn), 0.3, 0.5, 7), int(i * 0.07 * RATE))
    return to_wav(0.85 * out / np.max(np.abs(out)))


def jump():            # pulo (sweep ascendente, "boing")
    t = tarr(0.17); f = np.linspace(320, 700, len(t))
    s = (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t)) * np.exp(-7 * t)
    return to_wav(0.34 * s * ar(len(t), 0.002, 0.03))


def step():            # passo: "tap" curto, redondo e natural (não-ruidoso)
    t = tarr(0.05)
    body = (np.sin(2 * np.pi * 230 * t) + 0.4 * np.sin(2 * np.pi * 460 * t)) * np.exp(-55 * t)
    click_ = np.convolve(np.random.RandomState(2).randn(len(t)), np.ones(28) / 28, mode='same') * np.exp(-78 * t)
    s = (0.75 * body + 0.35 * click_) * ar(len(t), 0.001, 0.012)
    return to_wav(0.15 * s / (np.max(np.abs(s)) + 1e-9))


def door():            # entrar na porta (warp mágico: sweep + brilho + whoosh)
    out = np.zeros(int(0.6 * RATE))
    s, t = sweep(260, 1000, 0.42)
    add(out, 0.32 * s * np.exp(-3.4 * t), 0)
    for i, nn in enumerate([84, 88, 91]):
        add(out, bell(midi(nn), 0.4, 0.26, 7), int((0.12 + i * 0.06) * RATE))
    nz = np.convolve(np.random.RandomState(4).randn(len(out)), np.ones(28) / 28, mode='same')
    env = (np.linspace(0, 1, len(out)) ** 1.5) * np.exp(-2.2 * np.linspace(0, 1, len(out)))
    out += nz * env * 0.22
    return to_wav(0.85 * out / np.max(np.abs(out)))


def unlock():          # destravar porta (clack + chime subindo)
    out = np.zeros(int(0.55 * RATE))
    for i, st in enumerate([0.0, 0.08]):
        t = tarr(0.05); nz = np.convolve(np.random.RandomState(i + 5).randn(len(t)), np.ones(8) / 8, mode='same')
        cl = nz * np.exp(-48 * t) + 0.5 * np.sin(2 * np.pi * 175 * t) * np.exp(-38 * t)
        add(out, 0.4 * cl, int(st * RATE))
    for i, nn in enumerate([79, 84]):
        add(out, bell(midi(nn), 0.35, 0.5, 6), int((0.18 + i * 0.12) * RATE))
    return to_wav(0.8 * out / np.max(np.abs(out)))


def phase():           # passar de fase (flourish curto e alegre)
    out = np.zeros(int(0.62 * RATE))
    for i, nn in enumerate([79, 84, 88]):
        add(out, bell(midi(nn), 0.45, 0.45, 5), int(i * 0.085 * RATE))
    add(out, bell(midi(91), 0.4, 0.22, 8), int(0.27 * RATE))
    return to_wav(0.82 * out / np.max(np.abs(out)))


def party():           # festa/confete ao zerar
    dur = 1.8; out = np.zeros(int(dur * RATE))
    for nn, st in [(72, 0.0), (76, 0.12), (79, 0.24), (84, 0.36)]:
        add(out, bell(midi(nn), 0.9, 0.45, 3), int(st * RATE))
    t = tarr(dur - 0.5)
    ch = sum(0.11 * np.sin(2 * np.pi * midi(m) * t) for m in [72, 76, 79, 84]) * np.exp(-1.2 * t)
    add(out, ch, int(0.5 * RATE))
    rs = np.random.RandomState(3)
    for _ in range(26):
        add(out, bell(midi(rs.choice([84, 86, 88, 91, 93])), 0.25, 0.17, 10), int(rs.uniform(0.1, dur - 0.2) * RATE))
    nz = np.convolve(rs.randn(len(out)), np.ones(4) / 4, mode='same')
    out += nz * np.clip(np.sin(2 * np.pi * 9 * np.arange(len(out)) / RATE), 0, 1) * 0.05
    return to_wav(0.85 * out / np.max(np.abs(out)))


def all_sounds():
    return {"musica": music(), "clique": click(), "coletar": collect(),
            "pulo": jump(), "passo": step(), "porta": door(),
            "destravar": unlock(), "fase": phase(), "festa": party()}


if __name__ == "__main__":
    import os
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(repo_root, "preview", "snd")
    os.makedirs(out_dir, exist_ok=True)
    for name, (data, rate, sc) in all_sounds().items():
        open(os.path.join(out_dir, f"{name}.wav"), "wb").write(data)
        print(f"{name}: {sc} samples, {sc/rate:.2f}s, {len(data)} bytes")
