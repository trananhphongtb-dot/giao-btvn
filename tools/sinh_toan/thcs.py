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
