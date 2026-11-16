"""Bộ máy sinh câu hỏi Tiếng Anh từ kho từ vựng/ngữ pháp soạn tay (bám Global Success - KNTT).
Đáp án lấy thẳng từ kho; nhiễu lấy từ mục khác nên không có hai đáp án đúng."""
import random
from core import M, T

def parse_v(s):
    return [tuple(x.strip() for x in p.split("=", 1)) for p in s.strip().split(";") if p.strip()]

def parse_g(s):
    out = []
    for ln in s.strip().splitlines():
        p = [x.strip() for x in ln.split("|")]
        if len(p) == 5: out.append(tuple(p))
    return out

def parse_s(s):
    out = []
    for ln in s.strip().splitlines():
        p = [x.strip() for x in ln.split("|")]
        if len(p) == 2: out.append(tuple(p))
    return out

def _sai(rng, dung, ds, n=3):
    s = [x for x in dict.fromkeys(ds) if x != dung]
    if len(s) < n: raise ValueError
    return rng.sample(s, n)

def unit(vocab, gram, sent, pool_v, pool_s):
    V, G, S = parse_v(vocab), parse_g(gram), parse_s(sent)
    PV_en = [e for e, _ in pool_v]; PV_vi = [v for _, v in pool_v]
    PS_en = [e for _, e in pool_s]
    mcs, tls = [], []
    def nghia(rng):
        e, v = rng.choice(V)
        return M(f"Từ \"{e}\" có nghĩa là:", v, _sai(rng, v, [x for _, x in V if x != v] if len(V) >= 4 else PV_vi), 1)
    def dich(rng):
        e, v = rng.choice(V)
        return M(f"\"{v}\" trong tiếng Anh là:", e, _sai(rng, e, [x for x, _ in V if x != e] if len(V) >= 4 else PV_en), 1)
    mcs += [nghia, dich]
    for st, ok, a, b, c in G:
        mcs.append((lambda st, ok, a, b, c: (lambda rng: M(st, ok, [a, b, c], 2)))(st, ok, a, b, c))
        tls.append((lambda st, ok: (lambda rng: T(f"Hoàn thành câu: {st}", f"Đáp án: {ok}", 2)))(st, ok))
    if S:
        def cau(rng):
            v, e = rng.choice(S)
            return M(f"Câu \"{v}\" trong tiếng Anh là:", e, _sai(rng, e, [x for _, x in S if x != e] + PS_en), 2)
        mcs.append(cau)
        for v, e in S:
            tls.append((lambda v, e: (lambda rng: T(f"Dịch sang tiếng Anh: {v}", e, 2)))(v, e))
            tls.append((lambda v, e: (lambda rng: T(f"Dịch sang tiếng Việt: {e}", v, 2)))(v, e))
    for e, v in V:
        tls.append((lambda e, v: (lambda rng: T(f"Viết tiếng Anh cho từ/cụm từ: \"{v}\"", e, 1)))(e, v))
    return mcs, tls

def make(units):
    """units: [(ten, vocab, gram, sent)] -> CHU_DE"""
    pv = [p for _, v, _, _ in units for p in parse_v(v)]
    ps = [p for _, _, _, s in units for p in parse_s(s)]
    out = []
    for ten, v, g, s in units:
        m, t = unit(v, g, s, pv, ps)
        out.append((ten, m, t))
    return out
