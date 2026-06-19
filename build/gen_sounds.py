# -*- coding: utf-8 -*-
"""gen_sounds.py - sintetiza os efeitos sonoros e a música (WAV 22050 Hz, 16-bit
mono) de forma procedural (sem direitos autorais). Devolve dict nome->(bytes,
rate, sampleCount)."""
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
    e[:ai] = np.linspace(0, 1, ai)
    e[-ri:] *= np.linspace(1, 0, ri)
    return e


def bell(freq, dur, amp=0.5, decay=6.0):
    t = tarr(dur)
    s = (np.sin(2 * np.pi * freq * t) + 0.5 * np.sin(2 * np.pi * 2 * freq * t)
         + 0.22 * np.sin(2 * np.pi * 3 * freq * t))
    s *= np.exp(-decay * t) * ar(len(t), 0.002, 0.02)
    return amp * s / 1.72


def add(out, seg, st):
    e = min(len(seg), len(out) - st)
    if e > 0:
        out[st:st + e] += seg[:e]


# --------------------------------------------------------------------------
def music():           # ~16s calmo e imersivo (C - G - Am - F em loop)
    prog = [(48, [0, 4, 7]), (43, [0, 4, 7]), (45, [0, 3, 7]), (41, [0, 4, 7])]
    cd = 4.0
    out = np.zeros(int(cd * 4 * RATE)); pos = 0
    for root, ints in prog:
        n = int(cd * RATE); t = np.arange(n) / RATE; seg = np.zeros(n)
        for iv in ints:                                   # pad com leve detune
            f = midi(root + iv)
            seg += 0.10 * np.sin(2 * np.pi * (f - 0.4) * t)
            seg += 0.10 * np.sin(2 * np.pi * (f + 0.4) * t)
            seg += 0.05 * np.sin(2 * np.pi * midi(root + iv + 12) * t)
        pe = np.minimum(1, np.linspace(0, 1, n) * 3) * np.minimum(1, np.linspace(1, 0, n) * 4 + 0.25)
        seg *= pe * 0.6
        seg += 0.16 * np.sin(2 * np.pi * midi(root - 12) * t) * np.exp(-1.3 * t)   # baixo
        arp = [root + 12 + ints[0], root + 12 + ints[1], root + 12 + ints[2], root + 24 + ints[0]]
        for k in range(8):                                # arpejo de sininhos
            add(seg, bell(midi(arp[k % 4]), 0.62, 0.30, 5), int(k * (cd / 8) * RATE))
        add(out, seg, pos); pos += n
    out *= 0.62 / np.max(np.abs(out))
    f = int(0.02 * RATE); out[:f] *= np.linspace(0, 1, f); out[-f:] *= np.linspace(1, 0, f)
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


def jump():            # pulo (sweep ascendente)
    t = tarr(0.17); f = np.linspace(320, 700, len(t))
    s = (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t)) * np.exp(-7 * t)
    return to_wav(0.34 * s * ar(len(t), 0.002, 0.03))


def step():            # passo (suave)
    t = tarr(0.06); rs = np.random.RandomState(2)
    nz = np.convolve(rs.randn(len(t)), np.ones(18) / 18, mode='same')
    s = nz * np.exp(-38 * t) + 0.25 * np.sin(2 * np.pi * 120 * t) * np.exp(-45 * t)
    s *= ar(len(t), 0.001, 0.01)
    return to_wav(0.22 * s / (np.max(np.abs(s)) + 1e-9))


def unlock():          # destravar porta (clack + chime subindo)
    out = np.zeros(int(0.55 * RATE))
    for i, st in enumerate([0.0, 0.08]):
        t = tarr(0.05); nz = np.convolve(np.random.RandomState(i + 5).randn(len(t)), np.ones(8) / 8, mode='same')
        cl = nz * np.exp(-48 * t) + 0.5 * np.sin(2 * np.pi * 175 * t) * np.exp(-38 * t)
        add(out, 0.4 * cl, int(st * RATE))
    for i, nn in enumerate([79, 84]):
        add(out, bell(midi(nn), 0.35, 0.5, 6), int((0.18 + i * 0.12) * RATE))
    return to_wav(0.8 * out / np.max(np.abs(out)))


def party():           # festa/confete ao zerar
    dur = 1.8; out = np.zeros(int(dur * RATE))
    for nn, st in [(72, 0.0), (76, 0.12), (79, 0.24), (84, 0.36)]:
        add(out, bell(midi(nn), 0.9, 0.45, 3), int(st * RATE))
    t = tarr(dur - 0.5)
    ch = sum(0.11 * np.sin(2 * np.pi * midi(m) * t) for m in [72, 76, 79, 84]) * np.exp(-1.2 * t)
    add(out, ch, int(0.5 * RATE))
    rs = np.random.RandomState(3)
    for _ in range(26):                                   # confete (sininhos altos)
        add(out, bell(midi(rs.choice([84, 86, 88, 91, 93])), 0.25, 0.17, 10), int(rs.uniform(0.1, dur - 0.2) * RATE))
    nz = np.convolve(rs.randn(len(out)), np.ones(4) / 4, mode='same')   # chocalho
    out += nz * np.clip(np.sin(2 * np.pi * 9 * np.arange(len(out)) / RATE), 0, 1) * 0.05
    return to_wav(0.85 * out / np.max(np.abs(out)))


def all_sounds():
    return {"musica": music(), "clique": click(), "coletar": collect(),
            "pulo": jump(), "passo": step(), "destravar": unlock(), "festa": party()}


if __name__ == "__main__":
    import os
    os.makedirs("/home/user/Scratch-code-/preview/snd", exist_ok=True)
    for name, (data, rate, sc) in all_sounds().items():
        open(f"/home/user/Scratch-code-/preview/snd/{name}.wav", "wb").write(data)
        print(f"{name}: {sc} samples, {sc/rate:.2f}s, {len(data)} bytes")
