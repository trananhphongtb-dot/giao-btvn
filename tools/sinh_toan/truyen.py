"""Bài toán có lời văn dùng chung (cộng, trừ, nhiều hơn, ít hơn)."""
from core import TEN, VAT, T, giai, hai_ten, vat


def _kq(kieu, loi, phep, kq, dv, tl):
    if kieu == "ngan":
        return f"Phép tính: {phep} = {kq}\nTrả lời: {tl.format(kq=kq)}"
    return giai(loi, phep, kq, dv)


def de_hop(rng, lo, hi, kieu="giai", kho=1):
    a, b = rng.randint(lo, hi), rng.randint(lo, hi)
    x, y = hai_ten(rng)
    v = vat(rng)
    de = f"{x} có {a} {v}, {y} có {b} {v}. Hỏi cả hai bạn có tất cả bao nhiêu {v}?"
    return T(de, _kq(kieu, f"Cả hai bạn có tất cả số {v} là:", f"{a} + {b}", a + b, v, f"Cả hai bạn có tất cả {{kq}} {v}."), kho)


def de_them(rng, lo, hi, kieu="giai", kho=1):
    a, b = rng.randint(lo, hi), rng.randint(lo, hi)
    x, y = hai_ten(rng)
    v = vat(rng)
    de = f"{x} có {a} {v}. {y} cho {x} thêm {b} {v}. Hỏi {x} có tất cả bao nhiêu {v}?"
    return T(de, _kq(kieu, f"{x} có tất cả số {v} là:", f"{a} + {b}", a + b, v, f"{x} có tất cả {{kq}} {v}."), kho)


def de_bot(rng, lo, hi, kieu="giai", kho=1):
    b = rng.randint(lo, hi)
    a = b + rng.randint(max(lo, 1), hi)
    x, y = hai_ten(rng)
    v = vat(rng)
    de = f"{x} có {a} {v}. {x} cho {y} {b} {v}. Hỏi {x} còn lại bao nhiêu {v}?"
    return T(de, _kq(kieu, f"{x} còn lại số {v} là:", f"{a} - {b}", a - b, v, f"{x} còn lại {{kq}} {v}."), kho)


def de_nhieu(rng, lo, hi, kieu="giai", kho=2):
    a, b = rng.randint(lo, hi), rng.randint(max(lo, 1), hi)
    x, y = hai_ten(rng)
    v = vat(rng)
    de = f"{x} có {a} {v}. {y} có nhiều hơn {x} {b} {v}. Hỏi {y} có bao nhiêu {v}?"
    return T(de, _kq(kieu, f"{y} có số {v} là:", f"{a} + {b}", a + b, v, f"{y} có {{kq}} {v}."), kho)


def de_it(rng, lo, hi, kieu="giai", kho=2):
    b = rng.randint(max(lo, 1), hi)
    a = b + rng.randint(max(lo, 1), hi)
    x, y = hai_ten(rng)
    v = vat(rng)
    de = f"{x} có {a} {v}. {y} có ít hơn {x} {b} {v}. Hỏi {y} có bao nhiêu {v}?"
    return T(de, _kq(kieu, f"{y} có số {v} là:", f"{a} - {b}", a - b, v, f"{y} có {{kq}} {v}."), kho)
