"""Hàm dùng chung cho Toán THCS/THPT (lớp 6–12). Đáp án luôn do code tính."""
from math import gcd, isqrt
from core import *

D = Decimal
SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def lcm(a, b):
    return a * b // gcd(a, b)


def pw(a, n):
    return f"{a}{str(n).translate(SUP)}"


def rd(rng, lo, hi, pl):
    return D(rng.randint(lo * 10 ** pl, hi * 10 ** pl)).scaleb(-pl)


def nint(rng, q, d, kho=1, buoc=(1, 2, 10), lo=-10 ** 9):
    return M(q, d, [str(x) for x in so_gan(rng, d, lo, None, buoc)], kho)


def ngt(rng, hi=9, rieng=True):
    while True:
        d = rng.randint(2, hi)
        n = rng.randint(1, d - 1)
        if not rieng or gcd(n, d) == 1:
            return Fraction(n, d)


def nh_ps(rng, f):
    f = Fraction(f)
    n, d = f.numerator, f.denominator
    cand = [Fraction(n + 1, d), Fraction(max(n - 1, 1), d), Fraction(n, d + 1), Fraction(n, max(d - 1, 1)),
            Fraction(n + 2, d), Fraction(n, d + 2)] + ([Fraction(d, n)] if f > 1 else [])
    out = []
    for c in cand:
        if c != f and c > 0 and (f >= 1 or c < 1) and ps(c) not in [ps(x) for x in out]:
            out.append(c)
    if len(out) < 3:
        raise ValueError
    rng.shuffle(out)
    return [ps(x) for x in out[:3]]


def kq_dau(a, b):
    return ">" if a > b else "<" if a < b else "="


def tap(ds):
    """{1; 2; 3}"""
    return "{" + "; ".join(str(x) for x in ds) + "}"


def uoc(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def nguyen_to(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def sgn(n):
    return f"{n}" if n >= 0 else f"{n}"


def pf(a, n):
    """a/n kèm dạng rút gọn nếu khác."""
    f = Fraction(a, n)
    return f"{a}/{n}" if (f.numerator, f.denominator) == (a, n) else f"{a}/{n} = {ps(f)}"


def tpf(x, k):
    """Số thập phân cố định k chữ số sau dấu phẩy, kiểu Việt Nam."""
    return format(D(x).quantize(D(1).scaleb(-k), rounding="ROUND_HALF_UP"), "f").replace(".", ",")


def nq(rng, f, kho_dau=True):
    """3 nhiễu cho số hữu tỉ (có thể âm): đổi dấu, lệch tử/mẫu."""
    f = Fraction(f)
    n, d = f.numerator, f.denominator
    cand = [-f, Fraction(n + 1, d), Fraction(n - 1, d), Fraction(n, d + 1), Fraction(n, max(d - 1, 1)), Fraction(n + 2, d), Fraction(-n + 1, d), Fraction(n * 2, d + 1) if d else f]
    out = []
    for c in cand:
        if c != f and ps(c) not in [ps(x) for x in out]:
            out.append(c)
    if len(out) < 3:
        raise ValueError
    rng.shuffle(out)
    return [ps(x) for x in out[:3]]


def qr(rng, hi=9, dau=True):
    """Số hữu tỉ ngẫu nhiên (có thể âm), khác 0."""
    f = ngt(rng, hi)
    return -f if dau and rng.random() < .5 else f


def hang(c, bien, bac):
    """Hạng tử c·x^bac, bỏ hệ số 1; trả chuỗi không dấu đầu, và dấu."""
    a = abs(c)
    xs = "" if bac == 0 else (bien if bac == 1 else pw(bien, bac))
    if bac == 0:
        return str(a)
    return (xs if a == 1 else f"{a}{xs}")


def da(cs, bien="x"):
    """Đa thức từ hệ số giảm dần: [2,-3,1] -> 2x² - 3x + 1."""
    n = len(cs) - 1
    out = ""
    for i, c in enumerate(cs):
        if c == 0:
            continue
        bac = n - i
        h = hang(c, bien, bac)
        if not out:
            out = ("-" if c < 0 else "") + h
        else:
            out += (" - " if c < 0 else " + ") + h
    return out or "0"


def dmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def dadd(a, b, s=1):
    n = max(len(a), len(b)); a = [0] * (n - len(a)) + list(a); b = [0] * (n - len(b)) + list(b)
    return [x + s * y for x, y in zip(a, b)]


def dval(cs, x):
    r = 0
    for c in cs:
        r = r * x + c
    return r


def rpoly(rng, bac, lo=-6, hi=6):
    cs = [rng.randint(lo, hi) for _ in range(bac + 1)]
    while cs[0] == 0:
        cs[0] = rng.randint(lo, hi)
    return cs


def lay_sai_da(rng, cs, n=3):
    """Nhiễu đa thức: đổi dấu/hệ số một hạng tử."""
    out = []
    for _ in range(40):
        c2 = list(cs); i = rng.randrange(len(c2)); c2[i] += rng.choice([-2, -1, 1, 2])
        if c2[0] == 0: continue
        s = da(c2)
        if c2 != list(cs) and s != da(cs) and s not in out: out.append(s)
        if len(out) >= n: return out
    raise ValueError


def mono(c, i, j, a="x", b="y"):
    s = (a if i == 1 else pw(a, i) if i > 1 else "") + (b if j == 1 else pw(b, j) if j > 1 else "")
    return (str(abs(c)) if (abs(c) != 1 or not s) else "") + s


def da2(terms, a="x", b="y"):
    """terms: dict (i,j)->c ; xếp theo bậc x giảm dần rồi bậc y giảm dần."""
    out = ""
    for (i, j) in sorted(terms, key=lambda k: (-k[0], -k[1])):
        c = terms[(i, j)]
        if c == 0:
            continue
        m = mono(c, i, j, a, b)
        out += (("-" if c < 0 else "") + m) if not out else ((" - " if c < 0 else " + ") + m)
    return out or "0"


def pmul2(p, q):
    r = {}
    for (i, j), c in p.items():
        for (k, l), d in q.items():
            r[(i + k, j + l)] = r.get((i + k, j + l), 0) + c * d
    return {k: v for k, v in r.items() if v}


def padd2(p, q, s=1):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + s * v
    return {k: v for k, v in r.items() if v}


def sai_da2(rng, p, n=3):
    out = []
    for _ in range(60):
        q = dict(p); k = rng.choice(list(q)); q[k] += rng.choice([-2, -1, 1, 2])
        if q[k] == 0: del q[k]
        if not q: continue
        s = da2(q)
        if s != da2(p) and s not in out: out.append(s)
        if len(out) >= n: return out
    raise ValueError
