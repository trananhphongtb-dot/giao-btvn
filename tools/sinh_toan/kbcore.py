"""Bộ máy sinh câu hỏi cho các môn soạn tay theo cặp 'khái niệm = đáp án' (mỗi chương >=10 cặp).
mode 'kn'  : A = B là khái niệm/định nghĩa; sinh 2 trắc nghiệm (xuôi, ngược) + 1 tự luận.
mode 'hoi' : A là một câu hỏi (kết thúc bằng ?), B là đáp án; sinh 1 trắc nghiệm + 1 tự luận.
mode 'en'  : từ vựng tiếng Anh A = nghĩa B.
Dòng mỗi cặp ngăn cách bằng xuống dòng; có thể đặt mode riêng cho từng dòng bằng tiền tố 'h:' (hỏi) hoặc 'k:' (khái niệm)."""
import random
from core import M, T

def _sai(rng, dung, ds, n=3):
    s = [x for x in dict.fromkeys(ds) if x != dung]
    if len(s) < n: raise ValueError
    return rng.sample(s, n)

def parse(text, mode):
    out = []
    for ln in text.strip().splitlines():
        ln = ln.strip()
        if not ln or "=" not in ln: continue
        m = mode
        if ln[:2] in ("h:", "k:", "e:"):
            m = {"h": "hoi", "k": "kn", "e": "en"}[ln[0]]; ln = ln[2:].strip()
        a, b = ln.split("=", 1)
        out.append((a.strip(), b.strip(), m))
    return out

def chapter(text, mode="kn"):
    P = parse(text, mode)
    KB = [b for _, b, m in P if m == 'kn']; KA = [a for a, _, m in P if m == 'kn']
    HB = [b for _, b, m in P if m == 'hoi']; EB = [b for _, b, m in P if m == 'en']; EA = [a for a, _, m in P if m == 'en']
    HP = [(a, b) for a, b, m in P if m == 'hoi']
    from collections import Counter
    dem = Counter(b for _, b in HP)
    mcs, tls = [], []
    for a, b, m in P:
        if m == "hoi":
            if dem[b] == 1 and len(HP) >= 5:
                mcs.append((lambda a, b: (lambda rng: M(f"Nội dung \"{b}\" là câu trả lời cho câu hỏi nào?", a, _sai(rng, a, [q for q, x in HP if x != b]), 2)))(a, b))
            mcs.append((lambda a, b: (lambda rng: M(a, b, _sai(rng, b, HB), 2)))(a, b))
            tls.append((lambda a, b: (lambda rng: T(a, b, 2)))(a, b))
        elif m == "en":
            mcs.append((lambda a, b: (lambda rng: M(f"Từ \"{a}\" có nghĩa là:", b, _sai(rng, b, EB), 1)))(a, b))
            mcs.append((lambda a, b: (lambda rng: M(f"\"{b}\" trong tiếng Anh là:", a, _sai(rng, a, EA), 1)))(a, b))
            tls.append((lambda a, b: (lambda rng: T(f"Viết tiếng Anh cho: \"{b}\"", a, 1)))(a, b))
        else:
            mcs.append((lambda a, b: (lambda rng: M(f"Phát biểu nào đúng khi nói về \"{a}\"?", b, _sai(rng, b, KB), 2)))(a, b))
            mcs.append((lambda a, b: (lambda rng: M(f"Phát biểu: \"{b}\" nói về khái niệm nào?", a, _sai(rng, a, KA), 2)))(a, b))
            tls.append((lambda a, b: (lambda rng: T(f"Trình bày: {a}", b, 2)))(a, b))
    return mcs, tls
