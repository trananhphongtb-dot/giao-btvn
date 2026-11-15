from math import gcd
from core import *
from truyen import *

D = Decimal
def rd(rng, lo, hi, pl):
    return D(rng.randint(lo * 10 ** pl, hi * 10 ** pl)).scaleb(-pl)
def lcm(a, b): return a * b // gcd(a, b)
def rfrac(rng, hi=9, rieng=True):
    while True:
        d = rng.randint(2, hi); n = rng.randint(1, d - 1)
        if not rieng or gcd(n, d) == 1: return Fraction(n, d)
def nh_ps(rng, f):
    f = Fraction(f); n, d = f.numerator, f.denominator
    cand = [Fraction(n + 1, d), Fraction(max(n - 1, 1), d), Fraction(n, d + 1), Fraction(n, max(d - 1, 1)), Fraction(n + 2, d), Fraction(n, d + 2)]
    out = []
    for c in cand:
        if c != f and c > 0 and ps(c) not in [ps(x) for x in out] and (c.denominator != 1 or f.denominator == 1): out.append(c)
    if len(out) < 3: raise ValueError
    rng.shuffle(out); return [ps(x) for x in out[:3]]
def nh_hs(rng, f):
    f = Fraction(f)
    cand = [f + Fraction(1, f.denominator), f - Fraction(1, f.denominator), f + 1, f - 1, f + Fraction(2, f.denominator)]
    out = []
    for c in cand:
        if c != f and c > 0 and hs(c) not in [hs(x) for x in out]: out.append(c)
    if len(out) < 3: raise ValueError
    rng.shuffle(out); return [hs(x) for x in out[:3]]

# 1. Hỗn số và phân số --------------------------------------------------------------------------
def _hn(rng):
    d = rng.randint(2, 9); n = rng.randint(1, d - 1)
    while gcd(n, d) != 1: n = rng.randint(1, d - 1)
    return rng.randint(1, 6), Fraction(n, d)
def tn_hs_ps(rng):
    w, f = _hn(rng); t = w + f; n, d = f.numerator, f.denominator
    cand = [f"{w + n}/{d}", f"{w * n + d}/{d}", f"{w * d + n}/{d + 1}", f"{w * d - n}/{d}", f"{w * d + n + 1}/{d}"]
    return M(f"Hỗn số {hs(t)} viết thành phân số là:", ps(t), chon3(rng, cand, ps(t)), 2)
def tn_ps_hs(rng):
    w, f = _hn(rng); t = w + f
    return M(f"Phân số {ps(t)} viết thành hỗn số là:", hs(t), nh_hs(rng, t), 2)
def tn_ss_hs(rng):
    a, b = _hn(rng), _hn(rng); x, y = a[0] + a[1], b[0] + b[1]
    if x == y: raise ValueError
    d = ">" if x > y else "<"
    return M(f"Chọn dấu thích hợp: {hs(x)} ... {hs(y)}", d, sai_dau(d), 2)
def tn_cong_hs(rng):
    a, b = _hn(rng), _hn(rng); t = a[0] + a[1] + b[0] + b[1]
    return M(f"{hs(a[0] + a[1])} + {hs(b[0] + b[1])} = ?", hs(t), nh_hs(rng, t), 3)
def tn_tru_hs(rng):
    a, b = _hn(rng), _hn(rng); x, y = sorted([a[0] + a[1], b[0] + b[1]], reverse=True)
    if x == y: raise ValueError
    return M(f"{hs(x)} - {hs(y)} = ?", hs(x - y), nh_hs(rng, x - y), 3)
def tn_ps_tp(rng):
    d = rng.choice([10, 100, 1000]); n = rng.randint(1, d - 1)
    if n % 10 == 0: raise ValueError
    return M(f"Phân số thập phân {n}/{d} viết dưới dạng số thập phân là:", tp(D(n) / D(d)), [tp(x) for x in dec_gan(rng, D(n) / D(d))], 2)
def tn_ps_thapphan(rng):
    d = rng.choice([2, 4, 5, 8, 20, 25]); n = rng.randint(1, d - 1)
    f = Fraction(n, d)
    if gcd(n, d) != 1: raise ValueError
    v = D(f.numerator) / D(f.denominator)
    return M(f"Viết phân số {ps(f)} dưới dạng số thập phân:", tp(v), [tp(x) for x in dec_gan(rng, v)], 3)
def tn_nhan_ps(rng):
    a, b = rfrac(rng), rfrac(rng); t = a * b
    return M(f"{ps(a)} × {ps(b)} = ?", ps(t), nh_ps(rng, t), 2)
def tn_chia_ps(rng):
    a, b = rfrac(rng), rfrac(rng); t = a / b
    return M(f"{ps(a)} : {ps(b)} = ?", ps(t), nh_ps(rng, t), 3)
def tn_phan_cua(rng):
    d = rng.randint(2, 9); n = rng.randint(1, d - 1); q = rng.randint(2, 15)
    return M(f"Lớp có {d * q} học sinh, {n}/{d} số học sinh đó là học sinh nữ. Số học sinh nữ là:", f"{n * q} học sinh", [f"{x} học sinh" for x in so_gan(rng, n * q, 1, 300, (q, 1, 2))], 2)

def tl_hs_ps(rng):
    ls = [_hn(rng) for _ in range(3)]
    return T("Viết các hỗn số sau thành phân số: " + ", ".join(hs(w + f) for w, f in ls), "; ".join(f"{hs(w + f)} = {ps(w + f)}" for w, f in ls), 1)
def tl_ps_hs(rng):
    ls = [_hn(rng) for _ in range(3)]
    return T("Viết các phân số sau thành hỗn số: " + ", ".join(ps(w + f) for w, f in ls), "; ".join(f"{ps(w + f)} = {hs(w + f)}" for w, f in ls), 1)
def tl_cong_tru_hs(rng):
    a, b = _hn(rng), _hn(rng); x, y = sorted([a[0] + a[1], b[0] + b[1]], reverse=True)
    if x == y: raise ValueError
    return T(f"Tính: {hs(x)} + {hs(y)};  {hs(x)} - {hs(y)}", f"{hs(x)} + {hs(y)} = {hs(x + y)}\n{hs(x)} - {hs(y)} = {hs(x - y)}", 3)
def tl_ps_tp(rng):
    ds = [rng.choice([2, 4, 5, 8, 20, 25]) for _ in range(3)]
    fs = []
    for d in ds:
        n = rng.randint(1, d - 1); f = Fraction(n, d)
        if f not in fs and gcd(n, d) == 1: fs.append(f)
    if len(fs) < 3: raise ValueError
    return T("Viết các phân số sau thành số thập phân: " + ", ".join(ps(f) for f in fs), "; ".join(f"{ps(f)} = {tp(D(f.numerator) / D(f.denominator))}" for f in fs), 2)
def tl_nhan_chia_ps(rng):
    a, b = rfrac(rng), rfrac(rng)
    return T(f"Tính: {ps(a)} × {ps(b)};  {ps(a)} : {ps(b)}", f"{ps(a)} × {ps(b)} = {ps(a * b)}\n{ps(a)} : {ps(b)} = {ps(a / b)}", 2)
def tl_vai(rng):
    w, f = _hn(rng); x = rng.choice(TEN)
    return T(f"Một mảnh vải dài {hs(w + f)} m. Đã cắt đi {ps(f)} m. Hỏi mảnh vải còn lại dài bao nhiêu mét?", f"Còn lại: {hs(w + f)} - {ps(f)} = {hs(w)} (m)\nĐáp số: {w} m.", 2)

# 2. Số thập phân: đọc, viết, so sánh, làm tròn ----------------------------------------------------
_HANG = {-1: "phần mười", -2: "phần trăm", -3: "phần nghìn", 0: "đơn vị", 1: "chục", 2: "trăm"}
def _td(rng):
    while True:
        a = rng.randint(1, 99); b = rng.randint(100, 999)
        st = f"{a}{b}"
        if len(set(st)) == len(st): return D(f"{a}.{b}")
def tn_hang(rng):
    x = _td(rng); s = tp(x); ip, fp = s.split(",")
    d, hang = rng.choice([(fp[0], "phần mười"), (fp[1], "phần trăm"), (fp[2], "phần nghìn"), (ip[-1], "đơn vị")])
    return M(f"Chữ số {d} trong số {s} thuộc hàng nào?", f"Hàng {hang}", [f"Hàng {h}" for h in ["phần mười", "phần trăm", "phần nghìn", "đơn vị", "chục"] if h != hang][:3], 2)
def tn_gia_tri(rng):
    x = _td(rng); s = tp(x); ip, fp = s.split(",")
    d = int(fp[0]); k = 0
    if d == 0: raise ValueError
    return M(f"Chữ số {d} trong số {s} có giá trị là:", f"{d}/10", [f"{d}/100", f"{d}/1000", f"{d}"], 2)
def tn_ss(rng):
    a, b = rd(rng, 1, 99, 2), rd(rng, 1, 99, 2)
    if a == b: raise ValueError
    d = ">" if a > b else "<"
    return M(f"Chọn dấu thích hợp: {tp(a)} ... {tp(b)}", d, sai_dau(d), 1)
def tn_lon_nhat(rng):
    ds = []
    while len(ds) < 4:
        x = rd(rng, 1, 30, 2)
        if x not in ds: ds.append(x)
    m = max(ds)
    return M(f"Số nào lớn nhất trong các số {', '.join(tp(x) for x in ds)}?", tp(m), [tp(x) for x in ds if x != m], 2)
def tn_be_nhat(rng):
    ds = []
    while len(ds) < 4:
        x = rd(rng, 1, 30, 2)
        if x not in ds: ds.append(x)
    m = min(ds)
    return M(f"Số nào bé nhất trong các số {', '.join(tp(x) for x in ds)}?", tp(m), [tp(x) for x in ds if x != m], 2)
def tn_lt_phanmuoi(rng):
    x = rd(rng, 1, 99, 2); t = (x * 10).quantize(D(1), rounding="ROUND_HALF_UP") / 10
    return M(f"Làm tròn số {tp(x)} đến hàng phần mười được:", tp(t), [tp(v) for v in dec_gan(rng, t)], 3)
def tn_lt_nguyen(rng):
    x = rd(rng, 1, 99, 1)
    if x % 1 == 0: raise ValueError
    t = x.quantize(D(1), rounding="ROUND_HALF_UP")
    return M(f"Làm tròn số {tp(x)} đến số tự nhiên gần nhất được:", tp(t), [tp(t + 1), tp(t - 1), tp(t + 2)], 2)
def tn_bang(rng):
    x = rd(rng, 1, 99, 1)
    if x % 1 == 0: raise ValueError
    return M(f"Số nào bằng {tp(x)}?", f"{tp(x)}0", [tp(x * 10), tp(x / 10), tp(x + D('0.1'))], 2)
def tn_viet_tp(rng):
    d = rng.choice([10, 100, 1000]); n = rng.randint(1, d - 1)
    if n % 10 == 0: raise ValueError
    v = D(n) / D(d)
    return M(f"Viết {n}/{d} thành số thập phân:", tp(v), [tp(x) for x in dec_gan(rng, v)], 2)
def tn_xep(rng):
    ds = []
    while len(ds) < 3:
        x = rd(rng, 1, 20, 2)
        if x not in ds: ds.append(x)
    s = sorted(ds); t = ", ".join(tp(x) for x in s)
    return M(f"Sắp xếp các số {', '.join(tp(x) for x in ds)} theo thứ tự từ bé đến lớn:", t,
             [", ".join(tp(x) for x in s[::-1]), ", ".join(tp(x) for x in [s[1], s[0], s[2]]), ", ".join(tp(x) for x in [s[0], s[2], s[1]])], 3)

def tl_hang(rng):
    x = _td(rng); s = tp(x); ip, fp = s.split(",")
    return T(f"Trong số {s}, hãy nêu tên hàng của mỗi chữ số: {ip[-1]}, {fp[0]}, {fp[1]}, {fp[2]}.", f"Chữ số {ip[-1]}: hàng đơn vị; chữ số {fp[0]}: hàng phần mười; chữ số {fp[1]}: hàng phần trăm; chữ số {fp[2]}: hàng phần nghìn.", 2)
def tl_sap_xep(rng):
    ds = []
    while len(ds) < 5:
        x = rd(rng, 1, 30, 2)
        if x not in ds: ds.append(x)
    bd = rng.choice(["bé đến lớn", "lớn đến bé"])
    return T(f"Sắp xếp các số {', '.join(tp(x) for x in ds)} theo thứ tự từ {bd}.", ", ".join(tp(x) for x in sorted(ds, reverse=bd == "lớn đến bé")), 1)
def tl_so_sanh(rng):
    cap = [(rd(rng, 1, 50, 2), rd(rng, 1, 50, 2)) for _ in range(3)]
    if any(a == b for a, b in cap): raise ValueError
    return T("Điền dấu >, < thích hợp vào chỗ chấm:\n" + "; ".join(f"{tp(a)} ... {tp(b)}" for a, b in cap), "; ".join(f"{tp(a)} {'>' if a > b else '<'} {tp(b)}" for a, b in cap), 1)
def tl_lam_tron(rng):
    ds = [rd(rng, 1, 99, 2) for _ in range(3)]
    lt = lambda x, p: (x * 10 ** p).quantize(D(1), rounding="ROUND_HALF_UP") / 10 ** p
    return T("Làm tròn các số sau đến hàng phần mười: " + ", ".join(tp(x) for x in ds), "; ".join(f"{tp(x)} ≈ {tp(lt(x, 1))}" for x in ds), 3)
def tl_ps_tp_2(rng):
    ds = [(rng.randint(1, 99), rng.choice([100, 1000])) for _ in range(3)]
    return T("Viết các phân số thập phân sau thành số thập phân: " + ", ".join(f"{n}/{d}" for n, d in ds), "; ".join(f"{n}/{d} = {tp(D(n) / D(d))}" for n, d in ds), 2)
def tl_phan_tich(rng):
    x = rd(rng, 1, 99, 2)
    s = tp(x); ip, fp = s.split(",") if "," in s else (s, "")
    return T(f"Viết số {s} dưới dạng tổng của phần nguyên và phần thập phân.", f"{s} = {ip} + 0,{fp}" if fp else f"{s} = {s}", 2)

# 3. Cộng, trừ số thập phân --------------------------------------------------------------------------
def tn_cong(rng):
    a, b = rd(rng, 1, 90, 2), rd(rng, 1, 90, 1)
    return M(f"{tp(a)} + {tp(b)} = ?", tp(a + b), [tp(x) for x in dec_gan(rng, a + b)], 2)
def tn_cong1(rng):
    a, b = rd(rng, 1, 90, 1), rd(rng, 1, 90, 1)
    return M(f"{tp(a)} + {tp(b)} = ?", tp(a + b), [tp(x) for x in dec_gan(rng, a + b)], 1)
def tn_tru(rng):
    a, b = sorted([rd(rng, 1, 99, 2), rd(rng, 1, 99, 1)], reverse=True)
    if a == b: raise ValueError
    return M(f"{tp(a)} - {tp(b)} = ?", tp(a - b), [tp(x) for x in dec_gan(rng, a - b)], 2)
def tn_tru1(rng):
    a, b = sorted([rd(rng, 1, 99, 1), rd(rng, 1, 99, 1)], reverse=True)
    if a == b: raise ValueError
    return M(f"{tp(a)} - {tp(b)} = ?", tp(a - b), [tp(x) for x in dec_gan(rng, a - b)], 1)
def tn_x_cong(rng):
    a, x = rd(rng, 1, 50, 1), rd(rng, 1, 50, 1)
    return M(f"Tìm x: x + {tp(a)} = {tp(a + x)}", tp(x), [tp(v) for v in dec_gan(rng, x)], 3)
def tn_x_tru(rng):
    a, x = rd(rng, 1, 50, 1), rd(rng, 1, 50, 1)
    return M(f"Tìm x: x - {tp(a)} = {tp(x)}", tp(a + x), [tp(v) for v in dec_gan(rng, a + x)], 3)
def tn_dai(rng):
    a, b = rd(rng, 1, 30, 2), rd(rng, 1, 30, 2)
    return M(f"Đoạn dây thứ nhất dài {tp(a)} m, đoạn dây thứ hai dài {tp(b)} m. Cả hai đoạn dây dài bao nhiêu mét?", f"{tp(a + b)} m", [f"{tp(x)} m" for x in dec_gan(rng, a + b)], 2)
def tn_nang(rng):
    a, b = sorted([rd(rng, 5, 60, 1), rd(rng, 1, 40, 1)], reverse=True)
    if a == b: raise ValueError
    return M(f"Bao gạo nặng {tp(a)} kg, bao ngô nặng {tp(b)} kg. Bao gạo nặng hơn bao ngô bao nhiêu ki-lô-gam?", f"{tp(a - b)} kg", [f"{tp(x)} kg" for x in dec_gan(rng, a - b)], 2)
def tn_ba(rng):
    a, b, c = rd(rng, 1, 30, 1), rd(rng, 1, 30, 1), rd(rng, 1, 30, 1)
    return M(f"{tp(a)} + {tp(b)} + {tp(c)} = ?", tp(a + b + c), [tp(x) for x in dec_gan(rng, a + b + c)], 3)
def tn_thuan(rng):
    a = rd(rng, 1, 9, 1); b = rd(rng, 1, 40, 2)
    return M(f"Tính bằng cách thuận tiện: {tp(a)} + {tp(b)} + {tp(10 - a)} = ?", tp(10 + b), [tp(x) for x in dec_gan(rng, 10 + b)], 3)

def tl_dat(rng):
    a, b = rd(rng, 1, 90, 2), rd(rng, 1, 90, 2); c, d = sorted([rd(rng, 1, 90, 2), rd(rng, 1, 90, 1)], reverse=True)
    if c == d: raise ValueError
    return T(f"Đặt tính rồi tính: {tp(a)} + {tp(b)};  {tp(c)} - {tp(d)}", f"{tp(a)} + {tp(b)} = {tp(a + b)}\n{tp(c)} - {tp(d)} = {tp(c - d)}", 1)
def tl_x(rng):
    a, x = rd(rng, 1, 50, 1), rd(rng, 1, 50, 1); b, y = rd(rng, 1, 50, 1), rd(rng, 1, 50, 1)
    return T(f"Tìm x: x + {tp(a)} = {tp(a + x)};  x - {tp(b)} = {tp(y)}", f"x = {tp(a + x)} - {tp(a)} = {tp(x)}\nx = {tp(y)} + {tp(b)} = {tp(b + y)}", 2)
def tl_dai(rng):
    a, b = rd(rng, 1, 30, 2), rd(rng, 1, 30, 2); x = rng.choice(TEN)
    return T(f"Một sợi dây dài {tp(a)} m, sợi dây thứ hai dài {tp(b)} m. Hỏi cả hai sợi dây dài bao nhiêu mét? Sợi nào dài hơn và dài hơn bao nhiêu mét?", f"Cả hai sợi dài: {tp(a)} + {tp(b)} = {tp(a + b)} (m)\nSợi dài hơn: {'thứ nhất' if a > b else 'thứ hai' if b > a else 'bằng nhau'}, dài hơn {tp(abs(a - b))} m.", 2)
def tl_nang(rng):
    a, b, c = rd(rng, 5, 40, 1), rd(rng, 5, 40, 1), rd(rng, 1, 30, 1)
    if c > a + b: raise ValueError
    return T(f"Một cửa hàng có {tp(a)} kg đường nhập về và {tp(b)} kg đường tồn kho. Cửa hàng đã bán {tp(c)} kg đường. Hỏi còn lại bao nhiêu ki-lô-gam đường?",
             f"Tổng số đường: {tp(a)} + {tp(b)} = {tp(a + b)} (kg)\nCòn lại: {tp(a + b)} - {tp(c)} = {tp(a + b - c)} (kg)\nĐáp số: {tp(a + b - c)} kg.", 3)
def tl_thuan(rng):
    a = rd(rng, 1, 9, 1); b = rd(rng, 1, 40, 2)
    return T(f"Tính bằng cách thuận tiện: {tp(a)} + {tp(b)} + {tp(10 - a)}", f"{tp(a)} + {tp(b)} + {tp(10 - a)} = ({tp(a)} + {tp(10 - a)}) + {tp(b)} = 10 + {tp(b)} = {tp(10 + b)}", 3)

# 4. Nhân, chia số thập phân --------------------------------------------------------------------------
def tn_nhan_nguyen(rng):
    a = rd(rng, 1, 50, 1); b = rng.randint(2, 9)
    return M(f"{tp(a)} × {b} = ?", tp(a * b), [tp(x) for x in dec_gan(rng, a * b)], 1)
def tn_nhan_tp(rng):
    a = rd(rng, 1, 20, 1); b = rd(rng, 1, 10, 1)
    return M(f"{tp(a)} × {tp(b)} = ?", tp(a * b), [tp(x) for x in dec_gan(rng, a * b)], 2)
def tn_nhan10(rng):
    a = rd(rng, 1, 99, 2); k = rng.choice([10, 100, 1000])
    return M(f"{tp(a)} × {k} = ?", tp(a * k), [tp(a * k * 10), tp(a * k / 10), tp(a)], 1)
def tn_chia10(rng):
    a = rd(rng, 10, 999, 1); k = rng.choice([10, 100, 1000])
    return M(f"{tp(a)} : {k} = ?", tp(a / k), [tp(a * k), tp(a / k * 10), tp(a / k / 10)], 2)
def tn_chia_nguyen(rng):
    q = rd(rng, 1, 30, 1); b = rng.randint(2, 9)
    return M(f"{tp(q * b)} : {b} = ?", tp(q), [tp(x) for x in dec_gan(rng, q)], 2)
def tn_chia_tp(rng):
    q = rd(rng, 1, 20, 0); b = rd(rng, 1, 5, 1)
    if b == 0 or b % 1 == 0: raise ValueError
    return M(f"{tp(q * b)} : {tp(b)} = ?", tp(q), [tp(x) for x in dec_gan(rng, q)], 3)
def tn_nhan_bai(rng):
    a = rd(rng, 1, 30, 1); n = rng.randint(2, 9)
    return M(f"Mỗi can chứa {tp(a)} lít dầu. {n} can như vậy chứa bao nhiêu lít dầu?", f"{tp(a * n)} lít", [f"{tp(x)} lít" for x in dec_gan(rng, a * n)], 2)
def tn_chia_bai(rng):
    q = rd(rng, 1, 20, 1); n = rng.randint(2, 9)
    return M(f"Có {tp(q * n)} kg gạo chia đều vào {n} túi. Mỗi túi có bao nhiêu ki-lô-gam gạo?", f"{tp(q)} kg", [f"{tp(x)} kg" for x in dec_gan(rng, q)], 2)
def tn_x_nhan(rng):
    a = rd(rng, 1, 9, 1); x = rd(rng, 1, 9, 0)
    if a % 1 == 0: raise ValueError
    return M(f"Tìm x: x × {tp(a)} = {tp(a * x)}", tp(x), [tp(v) for v in dec_gan(rng, x)], 3)
def tn_dien_tich(rng):
    a, b = rd(rng, 1, 20, 1), rd(rng, 1, 10, 1)
    return M(f"Mảnh vườn hình chữ nhật có chiều dài {tp(a)} m, chiều rộng {tp(b)} m. Diện tích mảnh vườn là:", f"{tp(a * b)} m²", [f"{tp(x)} m²" for x in dec_gan(rng, a * b)], 2)

def tl_nhan_chia(rng):
    a = rd(rng, 1, 30, 1); b = rng.randint(2, 9); q = rd(rng, 1, 30, 1)
    return T(f"Tính: {tp(a)} × {b};  {tp(q * b)} : {b}", f"{tp(a)} × {b} = {tp(a * b)}\n{tp(q * b)} : {b} = {tp(q)}", 1)
def tl_nhan_tp(rng):
    a = rd(rng, 1, 20, 1); b = rd(rng, 1, 10, 1)
    return T(f"Đặt tính rồi tính: {tp(a)} × {tp(b)}", f"{tp(a)} × {tp(b)} = {tp(a * b)}", 2)
def tl_chia_tp(rng):
    q = rd(rng, 1, 20, 0); b = rd(rng, 1, 5, 1)
    if b % 1 == 0: raise ValueError
    return T(f"Đặt tính rồi tính: {tp(q * b)} : {tp(b)}", f"{tp(q * b)} : {tp(b)} = {tp(q)}", 3)
def tl_vai_2(rng):
    a = rd(rng, 1, 20, 1); n = rng.randint(3, 9)
    return T(f"Mỗi can chứa {tp(a)} lít dầu. Hỏi {n} can như vậy chứa bao nhiêu lít dầu?", giai("Số lít dầu có là:", f"{tp(a)} × {n}", tp(a * n), "lít"), 2)
def tl_chia_tui(rng):
    q = rd(rng, 1, 20, 1); n = rng.randint(2, 9)
    return T(f"Có {tp(q * n)} kg gạo chia đều vào {n} túi. Hỏi mỗi túi có bao nhiêu ki-lô-gam gạo?", giai("Mỗi túi có số ki-lô-gam gạo là:", f"{tp(q * n)} : {n}", tp(q), "kg"), 2)
def tl_dt(rng):
    a, b = rd(rng, 1, 20, 1), rd(rng, 1, 10, 1)
    return T(f"Một mảnh vườn hình chữ nhật có chiều dài {tp(a)} m, chiều rộng {tp(b)} m. Tính chu vi và diện tích mảnh vườn.", f"Chu vi: ({tp(a)} + {tp(b)}) × 2 = {tp((a + b) * 2)} (m)\nDiện tích: {tp(a)} × {tp(b)} = {tp(a * b)} (m²)", 3)
def tl_nhanh(rng):
    a = rd(rng, 1, 20, 1); k = rng.choice([10, 100, 1000])
    return T(f"Tính nhẩm: {tp(a)} × {k};  {tp(a * k)} : {k}", f"{tp(a)} × {k} = {tp(a * k)}\n{tp(a * k)} : {k} = {tp(a)}", 1)

# 5. Tỉ số phần trăm -----------------------------------------------------------------------------------------
def tn_pt_cua(rng):
    p = rng.choice([5, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 80]); b = rng.choice([20, 40, 60, 80, 100, 120, 200, 240, 300, 400, 500])
    v = D(p) * b / 100
    return M(f"{p}% của {b} là:", tp(v), [tp(x) for x in dec_gan(rng, v)], 2)
def tn_ti_le(rng):
    p = rng.choice([5, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 80]); b = rng.choice([20, 40, 80, 100, 200, 400, 500])
    a = D(p) * b / 100
    if a % 1: raise ValueError
    return M(f"Tỉ số phần trăm của {int(a)} và {b} là:", f"{p}%", [f"{x}%" for x in so_gan(rng, p, 1, 200, (5, 10, 1))], 2)
def tn_tim_so(rng):
    p = rng.choice([10, 20, 25, 40, 50, 75, 80]); b = rng.choice([20, 40, 80, 100, 200, 400, 500])
    a = D(p) * b / 100
    if a % 1: raise ValueError
    return M(f"{p}% của một số bằng {int(a)}. Số đó là:", b, so_gan(rng, b, 1, 1000, (10, 20, 5)), 3)
def tn_ps_pt(rng):
    f = rng.choice([Fraction(1, 2), Fraction(1, 4), Fraction(3, 4), Fraction(1, 5), Fraction(2, 5), Fraction(3, 5), Fraction(4, 5), Fraction(1, 10), Fraction(3, 10), Fraction(7, 10), Fraction(1, 20), Fraction(3, 20), Fraction(1, 25), Fraction(7, 20)])
    p = f * 100
    return M(f"Viết phân số {ps(f)} dưới dạng tỉ số phần trăm:", f"{tp(D(p.numerator) / D(p.denominator))}%", [f"{tp(x)}%" for x in dec_gan(rng, D(p.numerator) / D(p.denominator))], 2)
def tn_tp_pt(rng):
    x = rd(rng, 1, 99, 2)
    if (x * 100) % 1: raise ValueError
    return M(f"Viết số thập phân {tp(x)} dưới dạng phần trăm:", f"{tp(x * 100)}%", [f"{tp(v)}%" for v in dec_gan(rng, x * 100)], 2)
def tn_giam_gia(rng):
    g = rng.choice([100, 150, 200, 250, 300, 400, 500, 800]) * 1000; p = rng.choice([10, 20, 25, 30, 40, 50])
    v = D(g) * p / 100
    return M(f"Một chiếc áo giá {fmt(g)} đồng, được giảm giá {p}%. Giá chiếc áo sau khi giảm là:", f"{fmt(int(g - v))} đồng", [f"{fmt(int(x))} đồng" for x in (v, g + v, g - 2 * v if g - 2 * v > 0 else g - v / 2)], 3)
def tn_hoc_sinh(rng):
    n = rng.choice([20, 25, 40, 50, 80, 100, 200]); p = rng.choice([10, 20, 25, 30, 40, 60, 75]); k = D(p) * n / 100
    if k % 1: raise ValueError
    return M(f"Lớp có {n} học sinh, trong đó {p}% là học sinh nữ. Số học sinh nữ là:", f"{int(k)} học sinh", [f"{x} học sinh" for x in so_gan(rng, int(k), 1, 300, (5, 1, 10))], 2)
def tn_lai(rng):
    g = rng.choice([1, 2, 5, 10, 20]) * 1000000; p = rng.choice([0.5, 1, 2, 5]); v = D(g) * D(str(p)) / 100
    return M(f"Gửi tiết kiệm {fmt(g)} đồng, lãi suất {tp(D(str(p)))}% một tháng. Sau một tháng tiền lãi là:", f"{fmt(int(v))} đồng", [f"{fmt(int(x))} đồng" for x in (v * 10, v / 10, v * 2)], 3)

def tl_pt_cua(rng):
    p = rng.choice([5, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 80]); b = rng.choice([40, 60, 80, 100, 120, 200, 240, 300, 400, 500])
    v = D(p) * b / 100
    return T(f"Tính {p}% của {b}.", f"{p}% của {b} là: {b} × {p} : 100 = {tp(v)}", 1)
def tl_ti_so(rng):
    p = rng.choice([5, 10, 20, 25, 30, 40, 50, 60, 75, 80]); b = rng.choice([20, 40, 80, 100, 200, 400, 500]); a = D(p) * b / 100
    if a % 1: raise ValueError
    return T(f"Một lớp có {b} học sinh, trong đó có {int(a)} học sinh giỏi. Hỏi số học sinh giỏi chiếm bao nhiêu phần trăm số học sinh của lớp?", f"Tỉ số phần trăm: {int(a)} : {b} = {tp(a / b)} = {p}%\nĐáp số: {p}%.", 2)
def tl_giam_gia(rng):
    g = rng.choice([100, 150, 200, 250, 300, 400, 500, 800]) * 1000; p = rng.choice([10, 20, 25, 30, 40, 50]); v = D(g) * p / 100
    return T(f"Một chiếc cặp giá {fmt(g)} đồng, cửa hàng giảm giá {p}%. Hỏi sau khi giảm, giá chiếc cặp là bao nhiêu đồng?", f"Số tiền được giảm: {fmt(g)} × {p} : 100 = {fmt(int(v))} (đồng)\nGiá sau khi giảm: {fmt(g)} - {fmt(int(v))} = {fmt(int(g - v))} (đồng)\nĐáp số: {fmt(int(g - v))} đồng.", 3)
def tl_tim_so(rng):
    p = rng.choice([10, 20, 25, 40, 50, 75, 80]); b = rng.choice([20, 40, 80, 100, 200, 400, 500]); a = D(p) * b / 100
    if a % 1: raise ValueError
    return T(f"Biết {p}% của một số bằng {int(a)}. Tìm số đó.", f"Số đó là: {int(a)} × 100 : {p} = {b}", 3)
def tl_lai(rng):
    g = rng.choice([1, 2, 5, 10]) * 1000000; p = rng.choice([1, 2, 5]); v = g * p // 100
    return T(f"Bác Hoa gửi tiết kiệm {fmt(g)} đồng với lãi suất {p}% một tháng. Hỏi sau một tháng, cả vốn lẫn lãi bác Hoa nhận được bao nhiêu tiền?", f"Tiền lãi sau một tháng: {fmt(g)} × {p} : 100 = {fmt(v)} (đồng)\nTổng số tiền: {fmt(g)} + {fmt(v)} = {fmt(g + v)} (đồng)\nĐáp số: {fmt(g + v)} đồng.", 3)
def tl_ps_pt(rng):
    fs = rng.sample([Fraction(1, 2), Fraction(1, 4), Fraction(3, 4), Fraction(1, 5), Fraction(2, 5), Fraction(3, 5), Fraction(1, 10), Fraction(3, 20)], 3)
    return T("Viết các phân số sau dưới dạng tỉ số phần trăm: " + ", ".join(ps(f) for f in fs), "; ".join(f"{ps(f)} = {tp(D(f.numerator) * 100 / D(f.denominator))}%" for f in fs), 2)

# 6. Diện tích hình tam giác, hình thang ----------------------------------------------------------------------
def tn_tg(rng):
    a, h = rng.randint(4, 30), rng.randint(4, 30)
    if a * h % 2: raise ValueError
    return M(f"Hình tam giác có độ dài đáy {a} cm, chiều cao {h} cm. Diện tích hình tam giác là:", f"{a * h // 2} cm²", [f"{x} cm²" for x in [a * h, a + h, a * h // 2 + a][:3]], 1)
def tn_thang(rng):
    a, b, h = rng.randint(4, 30), rng.randint(4, 30), rng.randint(4, 20)
    if (a + b) * h % 2: raise ValueError
    return M(f"Hình thang có hai đáy dài {a} cm và {b} cm, chiều cao {h} cm. Diện tích hình thang là:", f"{(a + b) * h // 2} cm²", [f"{x} cm²" for x in [(a + b) * h, a * b * h // 2 + 1, (a + b) * h // 2 + h]], 2)
def tn_cao_tg(rng):
    a, h = rng.randint(4, 30), rng.randint(4, 30)
    if a * h % 2: raise ValueError
    return M(f"Hình tam giác có diện tích {a * h // 2} cm², độ dài đáy {a} cm. Chiều cao tương ứng là:", f"{h} cm", [f"{x} cm" for x in so_gan(rng, h, 1, 100, (1, 2, 4))], 3)
def tn_day_tg(rng):
    a, h = rng.randint(4, 30), rng.randint(4, 30)
    if a * h % 2: raise ValueError
    return M(f"Hình tam giác có diện tích {a * h // 2} cm², chiều cao {h} cm. Độ dài đáy tương ứng là:", f"{a} cm", [f"{x} cm" for x in so_gan(rng, a, 1, 100, (1, 2, 4))], 3)
def tn_tg_vuong(rng):
    a, b = rng.randint(3, 20), rng.randint(3, 20)
    if a * b % 2: raise ValueError
    return M(f"Tam giác vuông có hai cạnh góc vuông dài {a} cm và {b} cm. Diện tích tam giác vuông đó là:", f"{a * b // 2} cm²", [f"{x} cm²" for x in [a * b, a + b, a * b // 2 + a]], 2)
def tn_cao_thang(rng):
    a, b, h = rng.randint(4, 30), rng.randint(4, 30), rng.randint(4, 20)
    if (a + b) * h % 2: raise ValueError
    return M(f"Hình thang có diện tích {(a + b) * h // 2} cm², tổng hai đáy {a + b} cm. Chiều cao là:", f"{h} cm", [f"{x} cm" for x in so_gan(rng, h, 1, 100, (1, 2, 4))], 3)
def tn_dt_m(rng):
    a, h = rng.randint(4, 40), rng.randint(4, 30)
    if a * h % 2: raise ValueError
    return M(f"Một mảnh đất hình tam giác có đáy {a} m, chiều cao {h} m. Diện tích mảnh đất là:", f"{a * h // 2} m²", [f"{x} m²" for x in [a * h, a + h, a * h // 2 + a]], 2)
def tn_thang_m(rng):
    a, b, h = rng.randint(5, 40), rng.randint(5, 40), rng.randint(4, 20)
    if (a + b) * h % 2: raise ValueError
    return M(f"Một thửa ruộng hình thang có đáy lớn {max(a, b)} m, đáy bé {min(a, b)} m, chiều cao {h} m. Diện tích thửa ruộng là:", f"{(a + b) * h // 2} m²", [f"{x} m²" for x in [(a + b) * h, (a + b) * h // 2 + h, max(a, b) * h // 2]], 2)

def tl_tg(rng):
    a, h = rng.randint(4, 30), rng.randint(4, 30)
    if a * h % 2: raise ValueError
    return T(f"Tính diện tích hình tam giác có độ dài đáy {a} cm và chiều cao {h} cm.", f"Diện tích: ({a} × {h}) : 2 = {a * h // 2} (cm²)", 1)
def tl_thang(rng):
    a, b, h = rng.randint(4, 30), rng.randint(4, 30), rng.randint(4, 20)
    if (a + b) * h % 2: raise ValueError
    return T(f"Tính diện tích hình thang có hai đáy dài {a} cm, {b} cm và chiều cao {h} cm.", f"Diện tích: (({a} + {b}) × {h}) : 2 = {(a + b) * h // 2} (cm²)", 2)
def tl_thua(rng):
    a, b, h = rng.randint(10, 40), rng.randint(10, 40), rng.randint(5, 20)
    if (a + b) * h % 2: raise ValueError
    return T(f"Một thửa ruộng hình thang có đáy lớn {max(a, b)} m, đáy bé {min(a, b)} m, chiều cao {h} m. Hỏi diện tích thửa ruộng là bao nhiêu mét vuông? Nếu mỗi mét vuông thu hoạch 2 kg thóc thì cả thửa thu hoạch được bao nhiêu ki-lô-gam thóc?",
             f"Diện tích: (({a} + {b}) × {h}) : 2 = {(a + b) * h // 2} (m²)\nSố thóc thu hoạch: {(a + b) * h // 2} × 2 = {(a + b) * h} (kg)", 3)
def tl_cao(rng):
    a, h = rng.randint(4, 30), rng.randint(4, 30)
    if a * h % 2: raise ValueError
    return T(f"Hình tam giác có diện tích {a * h // 2} cm² và độ dài đáy {a} cm. Tính chiều cao của hình tam giác.", f"Chiều cao: ({a * h // 2} × 2) : {a} = {h} (cm)", 3)
def tl_dat_2(rng):
    a, h = rng.randint(6, 40), rng.randint(6, 30)
    if a * h % 2: raise ValueError
    return T(f"Một mảnh đất hình tam giác có độ dài đáy {a} m, chiều cao {h} m. Tính diện tích mảnh đất.", f"Diện tích mảnh đất: ({a} × {h}) : 2 = {a * h // 2} (m²)", 2)
def tl_so(rng):
    a, h = rng.randint(4, 20), rng.randint(4, 20); b = rng.randint(4, 20)
    if a * h % 2 or (a + b) * h % 2: raise ValueError
    return T(f"Tam giác có đáy {a} cm, chiều cao {h} cm. Hình thang có hai đáy {a} cm và {b} cm, chiều cao {h} cm. Hình nào có diện tích lớn hơn?", f"Diện tích tam giác: {a * h // 2} cm²\nDiện tích hình thang: {(a + b) * h // 2} cm²\nVậy hình thang có diện tích lớn hơn.", 3)

# 7. Chu vi, diện tích hình tròn --------------------------------------------------------------------------------
PI = D("3.14")
def tn_cv_r(rng):
    r = rng.randint(2, 20)
    return M(f"Hình tròn có bán kính {r} cm. Chu vi hình tròn là (lấy π = 3,14):", f"{tp(2 * r * PI)} cm", [f"{tp(x)} cm" for x in (r * r * PI, r * PI, 2 * r * r * PI)], 2)
def tn_cv_d(rng):
    d = rng.randint(3, 40)
    return M(f"Hình tròn có đường kính {d} cm. Chu vi hình tròn là (lấy π = 3,14):", f"{tp(d * PI)} cm", [f"{tp(x)} cm" for x in (d * d * PI, 2 * d * PI, d * PI / 2)], 2)
def tn_dt_r(rng):
    r = rng.randint(2, 20)
    return M(f"Hình tròn có bán kính {r} cm. Diện tích hình tròn là (lấy π = 3,14):", f"{tp(r * r * PI)} cm²", [f"{tp(x)} cm²" for x in (2 * r * PI, r * PI, 2 * r * r * PI)], 2)
def tn_dt_d(rng):
    d = rng.choice([4, 6, 8, 10, 12, 14, 16, 20, 24, 30]); r = d // 2
    return M(f"Hình tròn có đường kính {d} cm. Diện tích hình tròn là (lấy π = 3,14):", f"{tp(r * r * PI)} cm²", [f"{tp(x)} cm²" for x in (d * d * PI, d * PI, r * PI)], 3)
def tn_d_cv(rng):
    d = rng.randint(3, 40)
    return M(f"Hình tròn có chu vi {tp(d * PI)} cm. Đường kính hình tròn là (lấy π = 3,14):", f"{d} cm", [f"{x} cm" for x in so_gan(rng, d, 1, 80, (1, 2, 3))], 3)
def tn_r_cv(rng):
    r = rng.randint(2, 20)
    return M(f"Hình tròn có chu vi {tp(2 * r * PI)} cm. Bán kính hình tròn là (lấy π = 3,14):", f"{r} cm", [f"{x} cm" for x in so_gan(rng, r, 1, 40, (1, 2, 3))], 3)
def tn_banh_xe(rng):
    d = rng.choice([40, 50, 60, 70, 80]); n = rng.randint(2, 5)
    return M(f"Bánh xe đạp có đường kính {d} cm. Khi bánh xe lăn {n} vòng thì xe đi được quãng đường (lấy π = 3,14) là:", f"{tp(d * PI * n)} cm", [f"{tp(x)} cm" for x in (d * PI, d * d * PI * n / 2, d * PI * n * 2)], 3)
def tn_ao(rng):
    r = rng.randint(2, 10)
    return M(f"Một cái ao hình tròn có bán kính {r} m. Diện tích mặt ao là (lấy π = 3,14):", f"{tp(r * r * PI)} m²", [f"{tp(x)} m²" for x in (2 * r * PI, r * r * PI * 2, r * PI)], 2)

def tl_cv_dt(rng):
    r = rng.randint(2, 15)
    return T(f"Một hình tròn có bán kính {r} cm. Tính chu vi và diện tích hình tròn đó (lấy π = 3,14).", f"Chu vi: {r} × 2 × 3,14 = {tp(2 * r * PI)} (cm)\nDiện tích: {r} × {r} × 3,14 = {tp(r * r * PI)} (cm²)", 2)
def tl_cv_d(rng):
    d = rng.randint(4, 40)
    return T(f"Một hình tròn có đường kính {d} cm. Tính chu vi hình tròn đó (π = 3,14).", f"Chu vi: {d} × 3,14 = {tp(d * PI)} (cm)", 1)
def tl_ao(rng):
    r = rng.randint(2, 12)
    return T(f"Một cái ao hình tròn có bán kính {r} m. Tính diện tích mặt ao (π = 3,14).", f"Diện tích mặt ao: {r} × {r} × 3,14 = {tp(r * r * PI)} (m²)", 2)
def tl_r_tu_cv(rng):
    r = rng.randint(3, 20)
    return T(f"Một hình tròn có chu vi {tp(2 * r * PI)} cm. Tính bán kính và diện tích hình tròn đó (π = 3,14).", f"Đường kính: {tp(2 * r * PI)} : 3,14 = {2 * r} (cm)\nBán kính: {2 * r} : 2 = {r} (cm)\nDiện tích: {r} × {r} × 3,14 = {tp(r * r * PI)} (cm²)", 3)
def tl_banh(rng):
    d = rng.choice([40, 50, 60, 70, 80]); n = rng.randint(2, 6)
    return T(f"Bánh xe của một chiếc xe đạp có đường kính {d} cm. Hỏi xe đi được bao nhiêu xăng-ti-mét khi bánh xe lăn {n} vòng? (π = 3,14)", f"Chu vi bánh xe: {d} × 3,14 = {tp(d * PI)} (cm)\nQuãng đường đi được: {tp(d * PI)} × {n} = {tp(d * PI * n)} (cm)", 3)
def tl_so_sanh_2(rng):
    r = rng.randint(3, 12); a = rng.randint(2 * r - 2, 2 * r + 4)
    return T(f"Hình tròn bán kính {r} cm và hình vuông cạnh {a} cm. Hình nào có diện tích lớn hơn? (π = 3,14)", f"Diện tích hình tròn: {r} × {r} × 3,14 = {tp(r * r * PI)} (cm²)\nDiện tích hình vuông: {a} × {a} = {a * a} (cm²)\nVậy " + ("hình tròn" if r * r * PI > a * a else "hình vuông") + " có diện tích lớn hơn.", 3)

# 8. Thể tích hình hộp chữ nhật, hình lập phương -------------------------------------------------------------------------
def tn_v_hop(rng):
    a, b, c = rng.randint(2, 15), rng.randint(2, 12), rng.randint(2, 10)
    return M(f"Hình hộp chữ nhật có chiều dài {a} cm, chiều rộng {b} cm, chiều cao {c} cm. Thể tích hình hộp là:", f"{a * b * c} cm³", [f"{x} cm³" for x in [a * b + c, (a + b + c) * 2, a * b * c + a * b][:3]], 1)
def tn_v_lap(rng):
    a = rng.randint(2, 12)
    return M(f"Hình lập phương có cạnh {a} cm. Thể tích hình lập phương là:", f"{a ** 3} cm³", [f"{x} cm³" for x in (a * a, 3 * a, 6 * a * a)], 1)
def tn_sxq(rng):
    a, b, c = rng.randint(3, 15), rng.randint(2, 12), rng.randint(2, 10)
    return M(f"Hình hộp chữ nhật có chiều dài {a} cm, chiều rộng {b} cm, chiều cao {c} cm. Diện tích xung quanh là:", f"{(a + b) * 2 * c} cm²", [f"{x} cm²" for x in ((a + b) * 2 * c + 2 * a * b, a * b * c, (a + b) * c)], 2)
def tn_stp(rng):
    a, b, c = rng.randint(3, 15), rng.randint(2, 12), rng.randint(2, 10)
    return M(f"Hình hộp chữ nhật có chiều dài {a} cm, chiều rộng {b} cm, chiều cao {c} cm. Diện tích toàn phần là:", f"{(a + b) * 2 * c + 2 * a * b} cm²", [f"{x} cm²" for x in ((a + b) * 2 * c, a * b * c, (a + b) * 2 * c + a * b)], 3)
def tn_dt_lap(rng):
    a = rng.randint(2, 15)
    return M(f"Hình lập phương có cạnh {a} cm. Diện tích toàn phần của hình lập phương là:", f"{6 * a * a} cm²", [f"{x} cm²" for x in (4 * a * a, a ** 3, 3 * a * a)], 2)
def tn_cao(rng):
    a, b, c = rng.randint(2, 15), rng.randint(2, 12), rng.randint(2, 10)
    return M(f"Hình hộp chữ nhật có thể tích {a * b * c} cm³, đáy là hình chữ nhật có chiều dài {a} cm, chiều rộng {b} cm. Chiều cao là:", f"{c} cm", [f"{x} cm" for x in so_gan(rng, c, 1, 50, (1, 2, 3))], 3)
def tn_lit(rng):
    a, b, c = rng.randint(2, 10) * 10, rng.randint(2, 8) * 10, rng.randint(2, 8) * 10
    return M(f"Một bể nước hình hộp chữ nhật có chiều dài {a} dm, chiều rộng {b} dm, chiều cao {c} dm. Bể chứa được bao nhiêu lít nước? (1 dm³ = 1 lít)", f"{fmt(a * b * c)} lít", [f"{fmt(x)} lít" for x in (a * b * c // 10, a * b * c * 10, a * b)], 3)
def tn_doi_the_tich(rng):
    a = rng.randint(2, 9)
    return M(f"{a} m³ = ... dm³", fmt(a * 1000), [fmt(a * 100), fmt(a * 10), fmt(a * 10000)], 2)
def tn_doi_the_tich2(rng):
    a = rng.randint(2, 9)
    return M(f"{a} dm³ = ... cm³", fmt(a * 1000), [fmt(a * 100), fmt(a * 10), fmt(a * 10000)], 2)

def tl_v_hop(rng):
    a, b, c = rng.randint(3, 20), rng.randint(2, 15), rng.randint(2, 12)
    return T(f"Một hình hộp chữ nhật có chiều dài {a} cm, chiều rộng {b} cm, chiều cao {c} cm. Tính thể tích hình hộp đó.", f"Thể tích: {a} × {b} × {c} = {a * b * c} (cm³)", 1)
def tl_sxq(rng):
    a, b, c = rng.randint(3, 20), rng.randint(2, 15), rng.randint(2, 12)
    return T(f"Một hình hộp chữ nhật có chiều dài {a} cm, chiều rộng {b} cm, chiều cao {c} cm. Tính diện tích xung quanh và diện tích toàn phần của hình hộp đó.", f"Diện tích xung quanh: ({a} + {b}) × 2 × {c} = {(a + b) * 2 * c} (cm²)\nDiện tích toàn phần: {(a + b) * 2 * c} + {a} × {b} × 2 = {(a + b) * 2 * c + 2 * a * b} (cm²)", 2)
def tl_lap(rng):
    a = rng.randint(2, 15)
    return T(f"Một hình lập phương có cạnh {a} cm. Tính diện tích toàn phần và thể tích hình lập phương đó.", f"Diện tích toàn phần: {a} × {a} × 6 = {6 * a * a} (cm²)\nThể tích: {a} × {a} × {a} = {a ** 3} (cm³)", 2)
def tl_be(rng):
    a, b, c = rng.randint(2, 10) * 10, rng.randint(2, 8) * 10, rng.randint(2, 8) * 10
    return T(f"Một bể nước hình hộp chữ nhật có chiều dài {a} dm, chiều rộng {b} dm, chiều cao {c} dm. Hỏi bể chứa được nhiều nhất bao nhiêu lít nước? (1 dm³ = 1 lít)", f"Thể tích bể: {a} × {b} × {c} = {fmt(a * b * c)} (dm³)\nĐổi: {fmt(a * b * c)} dm³ = {fmt(a * b * c)} lít\nĐáp số: {fmt(a * b * c)} lít.", 3)
def tl_cao_2(rng):
    a, b, c = rng.randint(3, 20), rng.randint(2, 15), rng.randint(2, 12)
    return T(f"Một hình hộp chữ nhật có thể tích {a * b * c} cm³, chiều dài {a} cm, chiều rộng {b} cm. Tính chiều cao hình hộp.", f"Diện tích đáy: {a} × {b} = {a * b} (cm²)\nChiều cao: {a * b * c} : {a * b} = {c} (cm)", 3)
def tl_son(rng):
    a = rng.randint(2, 12)
    return T(f"Người ta sơn tất cả các mặt ngoài của một cái hộp hình lập phương có cạnh {a} dm. Hỏi diện tích cần sơn là bao nhiêu đề-xi-mét vuông?", f"Diện tích cần sơn (diện tích toàn phần): {a} × {a} × 6 = {6 * a * a} (dm²)", 2)

# 9. Chuyển động đều -------------------------------------------------------------------------------------------------------
def tn_v(rng):
    v, t = rng.randint(5, 80), rng.randint(2, 6)
    return M(f"Một ô tô đi quãng đường {v * t} km trong {t} giờ. Vận tốc của ô tô là:", f"{v} km/giờ", [f"{x} km/giờ" for x in so_gan(rng, v, 1, 200, (1, 5, 10))], 1)
def tn_s(rng):
    v, t = rng.randint(5, 80), rng.randint(2, 6)
    return M(f"Một xe máy đi với vận tốc {v} km/giờ trong {t} giờ. Quãng đường xe đi được là:", f"{v * t} km", [f"{x} km" for x in so_gan(rng, v * t, 1, 600, (v, t, 10))], 1)
def tn_t(rng):
    v, t = rng.randint(5, 80), rng.randint(2, 8)
    return M(f"Một người đi xe đạp với vận tốc {v} km/giờ, quãng đường đi được là {v * t} km. Thời gian đi là:", f"{t} giờ", [f"{x} giờ" for x in so_gan(rng, t, 1, 20, (1, 2))], 2)
def tn_t_ruoi(rng):
    v, t = rng.choice([20, 30, 40, 50, 60, 80]), rng.choice([D("1.5"), D("2.5"), D("3.5")])
    return M(f"Một ô tô đi với vận tốc {v} km/giờ trong {tp(t)} giờ. Quãng đường ô tô đi được là:", f"{tp(v * t)} km", [f"{tp(x)} km" for x in dec_gan(rng, v * t)], 3)
def tn_nguoc_chieu(rng):
    v1, v2, t = rng.randint(20, 50), rng.randint(20, 50), rng.randint(2, 5)
    return M(f"Hai ô tô xuất phát cùng lúc từ hai địa điểm cách nhau {(v1 + v2) * t} km, đi ngược chiều để gặp nhau. Vận tốc lần lượt là {v1} km/giờ và {v2} km/giờ. Sau mấy giờ hai xe gặp nhau?", f"{t} giờ", [f"{x} giờ" for x in so_gan(rng, t, 1, 20, (1, 2))], 3)
def tn_doi_vt(rng):
    v = rng.randint(2, 20) * 3
    return M(f"Vận tốc {v} km/giờ bằng bao nhiêu mét trên phút? (1 km = 1000 m, 1 giờ = 60 phút)", f"{tp(D(v) * 1000 / 60)} m/phút", [f"{tp(x)} m/phút" for x in dec_gan(rng, D(v) * 1000 / 60)], 3)
def tn_phut(rng):
    v = rng.choice([30, 40, 60, 90, 120]); t = rng.choice([30, 45, 15])
    s = D(v) * t / 60
    return M(f"Một xe đi với vận tốc {v} km/giờ trong {t} phút. Quãng đường xe đi được là:", f"{tp(s)} km", [f"{tp(x)} km" for x in dec_gan(rng, s)], 3)
def tn_so_sanh_v(rng):
    v1, v2 = rng.sample(range(10, 70), 2)
    return M(f"Xe thứ nhất đi với vận tốc {v1} km/giờ, xe thứ hai đi với vận tốc {v2} km/giờ. Xe nào đi nhanh hơn?", "Xe thứ nhất" if v1 > v2 else "Xe thứ hai", ["Xe thứ hai" if v1 > v2 else "Xe thứ nhất", "Hai xe đi nhanh như nhau", "Không so sánh được"], 1)

def tl_v(rng):
    v, t = rng.randint(10, 80), rng.randint(2, 6)
    return T(f"Một ô tô đi quãng đường {v * t} km hết {t} giờ. Tính vận tốc của ô tô.", f"Vận tốc của ô tô: {v * t} : {t} = {v} (km/giờ)\nĐáp số: {v} km/giờ.", 1)
def tl_s(rng):
    v, t = rng.randint(10, 80), rng.randint(2, 6)
    return T(f"Một xe máy đi với vận tốc {v} km/giờ trong {t} giờ. Tính quãng đường xe máy đi được.", f"Quãng đường xe máy đi được: {v} × {t} = {v * t} (km)\nĐáp số: {v * t} km.", 1)
def tl_t(rng):
    v, t = rng.randint(10, 60), rng.randint(2, 8)
    return T(f"Một xe đạp đi với vận tốc {v} km/giờ. Hỏi xe đi hết quãng đường {v * t} km trong bao lâu?", f"Thời gian đi: {v * t} : {v} = {t} (giờ)\nĐáp số: {t} giờ.", 2)
def tl_nguoc(rng):
    v1, v2, t = rng.randint(20, 50), rng.randint(20, 50), rng.randint(2, 5)
    return T(f"Hai ô tô xuất phát cùng lúc từ hai địa điểm cách nhau {(v1 + v2) * t} km, đi ngược chiều để gặp nhau. Vận tốc xe thứ nhất {v1} km/giờ, xe thứ hai {v2} km/giờ. Hỏi sau bao lâu hai xe gặp nhau?", f"Tổng vận tốc hai xe: {v1} + {v2} = {v1 + v2} (km/giờ)\nThời gian để gặp nhau: {(v1 + v2) * t} : {v1 + v2} = {t} (giờ)\nĐáp số: {t} giờ.", 3)
def tl_ruoi(rng):
    v, t = rng.choice([20, 30, 40, 50, 60, 80]), rng.choice([D("1.5"), D("2.5"), D("3.5")])
    return T(f"Một ô tô đi với vận tốc {v} km/giờ trong {tp(t)} giờ. Tính quãng đường ô tô đi được.", f"Quãng đường: {v} × {tp(t)} = {tp(v * t)} (km)", 2)
def tl_hai_chang(rng):
    v1, t1, v2, t2 = rng.randint(30, 60), rng.randint(1, 3), rng.randint(30, 60), rng.randint(1, 3)
    return T(f"Một ô tô đi trong {t1} giờ đầu với vận tốc {v1} km/giờ, sau đó đi tiếp {t2} giờ với vận tốc {v2} km/giờ. Tính quãng đường ô tô đã đi và vận tốc trung bình.", f"Quãng đường chặng đầu: {v1} × {t1} = {v1 * t1} (km)\nQuãng đường chặng sau: {v2} × {t2} = {v2 * t2} (km)\nTổng quãng đường: {v1 * t1 + v2 * t2} (km)\nTổng thời gian: {t1 + t2} giờ\nVận tốc trung bình: {v1 * t1 + v2 * t2} : {t1 + t2} = {tp(D(v1 * t1 + v2 * t2) / (t1 + t2))} (km/giờ)", 3)
def tl_doi(rng):
    v = rng.randint(2, 20) * 3
    return T(f"Đổi vận tốc {v} km/giờ ra mét trên phút (1 km = 1000 m).", f"{v} km/giờ = {v * 1000} m/giờ\n{v * 1000} : 60 = {tp(D(v * 1000) / 60)} m/phút", 3)

# 10. Đổi đơn vị đo ---------------------------------------------------------------------------------------------------------
def tn_m_cm(rng):
    a = rd(rng, 1, 20, 2); return M(f"{tp(a)} m = ... cm", tp(a * 100), [tp(x) for x in dec_gan(rng, a * 100)], 1)
def tn_km_m(rng):
    a = rd(rng, 1, 20, 2); return M(f"{tp(a)} km = ... m", tp(a * 1000), [tp(x) for x in dec_gan(rng, a * 1000)], 1)
def tn_kg_g(rng):
    a = rd(rng, 1, 20, 2); return M(f"{tp(a)} kg = ... g", tp(a * 1000), [tp(x) for x in dec_gan(rng, a * 1000)], 1)
def tn_tan_kg(rng):
    a = rd(rng, 1, 20, 2); return M(f"{tp(a)} tấn = ... kg", tp(a * 1000), [tp(x) for x in dec_gan(rng, a * 1000)], 1)
def tn_ha(rng):
    a = rd(rng, 1, 20, 1); return M(f"{tp(a)} ha = ... m²", fmt(int(a * 10000)), [fmt(int(x)) for x in (a * 1000, a * 100000, a * 100)], 2)
def tn_m2_ha(rng):
    a = rng.randint(1, 9) * 5000
    return M(f"{fmt(a)} m² = ... ha", tp(D(a) / 10000), [tp(D(a) / 1000), tp(D(a) / 100000), tp(D(a) / 100)], 3)
def tn_gio_phut(rng):
    a = rd(rng, 1, 5, 1); 
    if a % 1 == 0: raise ValueError
    return M(f"{tp(a)} giờ = ... phút", tp(a * 60), [tp(x) for x in dec_gan(rng, a * 60)], 2)
def tn_ghep_km(rng):
    k, m = rng.randint(1, 9), rng.randint(1, 9) * 100 + rng.randint(0, 9) * 10
    return M(f"{k} km {m} m = ... km", tp(D(k) + D(m) / 1000), [tp(x) for x in dec_gan(rng, D(k) + D(m) / 1000)], 3)
def tn_ghep_m(rng):
    m, cm = rng.randint(1, 9), rng.randint(1, 99)
    return M(f"{m} m {cm} cm = ... m", tp(D(m) + D(cm) / 100), [tp(x) for x in dec_gan(rng, D(m) + D(cm) / 100)], 3)
def tn_cm_m(rng):
    a = rng.randint(101, 999)
    return M(f"{a} cm = ... m", tp(D(a) / 100), [tp(x) for x in dec_gan(rng, D(a) / 100)], 2)
def tn_g_kg(rng):
    a = rng.randint(1100, 9500)
    if a % 10 == 0: raise ValueError
    return M(f"{fmt(a)} g = ... kg", tp(D(a) / 1000), [tp(x) for x in dec_gan(rng, D(a) / 1000)], 2)

def tl_doi_2(rng):
    a, b, c, d = rd(rng, 1, 20, 2), rd(rng, 1, 20, 2), rd(rng, 1, 20, 2), rd(rng, 1, 20, 2)
    return T(f"Viết số thích hợp vào chỗ chấm:\n{tp(a)} m = ... cm; {tp(b)} km = ... m; {tp(c)} kg = ... g; {tp(d)} tấn = ... kg", f"{tp(a)} m = {tp(a * 100)} cm; {tp(b)} km = {tp(b * 1000)} m; {tp(c)} kg = {tp(c * 1000)} g; {tp(d)} tấn = {tp(d * 1000)} kg", 1)
def tl_ghep(rng):
    k, m = rng.randint(1, 9), rng.randint(1, 9) * 100 + rng.randint(1, 9) * 10; a, b = rng.randint(1, 9), rng.randint(1, 99)
    return T(f"Viết thành số đo có một đơn vị:\n{k} km {m} m = ... km; {a} m {b} cm = ... m", f"{k} km {m} m = {tp(D(k) + D(m) / 1000)} km\n{a} m {b} cm = {tp(D(a) + D(b) / 100)} m", 2)
def tl_ruong(rng):
    a = rd(rng, 1, 20, 1)
    return T(f"Một thửa ruộng có diện tích {tp(a)} ha. Hỏi diện tích thửa ruộng đó bằng bao nhiêu mét vuông?", f"{tp(a)} ha = {tp(a)} × 10 000 = {fmt(int(a * 10000))} (m²)", 2)
def tl_xe(rng):
    a = rd(rng, 1, 9, 1); b = rng.randint(2, 6)
    return T(f"Mỗi xe chở {tp(a)} tấn hàng. Hỏi {b} xe chở được bao nhiêu ki-lô-gam hàng?", f"{b} xe chở được: {tp(a)} × {b} = {tp(a * b)} (tấn)\nĐổi: {tp(a * b)} tấn = {tp(a * b * 1000)} kg", 3)
def tl_giay(rng):
    g = rd(rng, 1, 5, 1)
    if g % 1 == 0: raise ValueError
    return T(f"Đổi {tp(g)} giờ ra phút và ra giây.", f"{tp(g)} giờ = {tp(g)} × 60 = {tp(g * 60)} phút\n{tp(g * 60)} phút = {tp(g * 60)} × 60 = {tp(g * 3600)} giây", 3)
def tl_so_sanh_3(rng):
    a = rd(rng, 1, 9, 2); b = rng.randint(100, 999)
    if a * 100 == b: raise ValueError
    d = ">" if a * 100 > b else "<"
    return T(f"Điền dấu >, <, = thích hợp vào chỗ chấm: {tp(a)} m ... {b} cm", f"{tp(a)} m = {tp(a * 100)} cm; {tp(a * 100)} {d} {b}. Vậy {tp(a)} m {d} {b} cm.", 3)

CHU_DE = [
    ("Hỗn số, phân số và phân số thập phân", [tn_hs_ps, tn_ps_hs, tn_ss_hs, tn_cong_hs, tn_tru_hs, tn_ps_tp, tn_ps_thapphan, tn_nhan_ps, tn_chia_ps, tn_phan_cua],
     [tl_hs_ps, tl_ps_hs, tl_cong_tru_hs, tl_ps_tp, tl_nhan_chia_ps, tl_vai]),
    ("Số thập phân: đọc, viết, so sánh, làm tròn", [tn_hang, tn_gia_tri, tn_ss, tn_lon_nhat, tn_be_nhat, tn_lt_phanmuoi, tn_lt_nguyen, tn_bang, tn_viet_tp, tn_xep],
     [tl_hang, tl_sap_xep, tl_so_sanh, tl_lam_tron, tl_ps_tp_2, tl_phan_tich]),
    ("Cộng, trừ số thập phân", [tn_cong, tn_cong1, tn_tru, tn_tru1, tn_x_cong, tn_x_tru, tn_dai, tn_nang, tn_ba, tn_thuan],
     [tl_dat, tl_x, tl_dai, tl_nang, tl_thuan]),
    ("Nhân, chia số thập phân", [tn_nhan_nguyen, tn_nhan_tp, tn_nhan10, tn_chia10, tn_chia_nguyen, tn_chia_tp, tn_nhan_bai, tn_chia_bai, tn_x_nhan, tn_dien_tich],
     [tl_nhan_chia, tl_nhan_tp, tl_chia_tp, tl_vai_2, tl_chia_tui, tl_dt, tl_nhanh]),
    ("Tỉ số phần trăm", [tn_pt_cua, tn_ti_le, tn_tim_so, tn_ps_pt, tn_tp_pt, tn_giam_gia, tn_hoc_sinh, tn_lai],
     [tl_pt_cua, tl_ti_so, tl_giam_gia, tl_tim_so, tl_lai, tl_ps_pt]),
    ("Diện tích hình tam giác, hình thang", [tn_tg, tn_thang, tn_cao_tg, tn_day_tg, tn_tg_vuong, tn_cao_thang, tn_dt_m, tn_thang_m],
     [tl_tg, tl_thang, tl_thua, tl_cao, tl_dat_2, tl_so]),
    ("Chu vi và diện tích hình tròn", [tn_cv_r, tn_cv_d, tn_dt_r, tn_dt_d, tn_d_cv, tn_r_cv, tn_banh_xe, tn_ao],
     [tl_cv_dt, tl_cv_d, tl_ao, tl_r_tu_cv, tl_banh, tl_so_sanh_2]),
    ("Thể tích hình hộp chữ nhật, hình lập phương", [tn_v_hop, tn_v_lap, tn_sxq, tn_stp, tn_dt_lap, tn_cao, tn_lit, tn_doi_the_tich, tn_doi_the_tich2],
     [tl_v_hop, tl_sxq, tl_lap, tl_be, tl_cao_2, tl_son]),
    ("Chuyển động đều (vận tốc, quãng đường, thời gian)", [tn_v, tn_s, tn_t, tn_t_ruoi, tn_nguoc_chieu, tn_doi_vt, tn_phut, tn_so_sanh_v],
     [tl_v, tl_s, tl_t, tl_nguoc, tl_ruoi, tl_hai_chang, tl_doi]),
    ("Đổi đơn vị đo: độ dài, khối lượng, diện tích, thời gian", [tn_m_cm, tn_km_m, tn_kg_g, tn_tan_kg, tn_ha, tn_m2_ha, tn_gio_phut, tn_ghep_km, tn_ghep_m, tn_cm_m, tn_g_kg],
     [tl_doi_2, tl_ghep, tl_ruong, tl_xe, tl_giay, tl_so_sanh_3]),
]
