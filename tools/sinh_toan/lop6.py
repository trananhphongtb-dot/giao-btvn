from thcs import *

SN = "Một lớp"
# ============ 1. Tập hợp và các phép tính với số tự nhiên ============
def a1_dem(rng):
    a = rng.randint(0, 9); b = a + rng.randint(4, 14); k = rng.randint(0, 2)
    ds = [("≤", "≤", b - a + 1), ("<", "<", b - a - 1), ("≤", "<", b - a)][k]
    return nint(rng, f"Số phần tử của tập hợp A = {{x ∈ ℕ | {a} {'≤' if k != 1 else '<'} x {ds[1]} {b}}} là:", ds[2], 1, (1, 2))
def a1_luythua(rng):
    a = rng.randint(2, 9); n = rng.randint(2, 4); d = a ** n
    return M(f"Giá trị của {pw(a, n)} là:", d, chon3(rng, [a * n, a ** (n + 1), a ** (n - 1), d + a, d - a, a + n], d), 1)
def a1_nhan(rng):
    a = rng.randint(2, 9); m, n = rng.sample(range(2, 8), 2); d = pw(a, m + n)
    return M(f"{pw(a, m)} · {pw(a, n)} = ?", d, chon3(rng, [pw(a, m * n), pw(a, m + n - 1), pw(a * a, m + n), pw(a, abs(m - n)), pw(a, m + n + 1)], d), 2)
def a1_chia(rng):
    a = rng.randint(2, 9); n = rng.randint(2, 5); m = n + rng.randint(2, 6); d = pw(a, m - n)
    return M(f"{pw(a, m)} : {pw(a, n)} = ?", d, chon3(rng, [pw(a, m + n), pw(a, m * n), pw(a, m - n + 1), pw(a, m - n - 1) if m - n > 1 else "1", pw(a, n)], d), 2)
def a1_tt1(rng):
    a, b, c = rng.randint(2, 20), rng.randint(2, 9), rng.randint(2, 9); d = a + b * c
    return M(f"Giá trị của biểu thức {a} + {b} · {c} là:", d, chon3(rng, [(a + b) * c, a + b + c, a * b + c, d + b, d - c], d), 1)
def a1_tt2(rng):
    dd = rng.randint(2, 6); k = rng.randint(2, 8); c = dd * k; a, b = rng.randint(5, 15), rng.randint(3, 9); d = a * b - k
    return M(f"Giá trị của biểu thức {a} · {b} - {c} : {dd} là:", d, chon3(rng, [(a * b - c) // dd if (a * b - c) % dd == 0 else d + 1, a * b + k, d + dd, d - 1, a * b - c], d), 2)
def a1_ngoac(rng):
    a, b, c, e = rng.randint(3, 20), rng.randint(3, 20), rng.randint(2, 6), rng.randint(1, 15); d = (a + b) * c - e
    return M(f"Giá trị của biểu thức ({a} + {b}) · {c} - {e} là:", d, chon3(rng, [a + b * c - e, (a + b) * (c - e), d + e, d + c, d - c], d), 2)
def a1_luythua_bt(rng):
    a, b, c = rng.randint(2, 5), rng.randint(2, 3), rng.randint(2, 9); d = a ** 2 + b ** 3 * c
    return M(f"Giá trị của biểu thức {pw(a, 2)} + {pw(b, 3)} · {c} là:", d, chon3(rng, [(a ** 2 + b ** 3) * c, a * 2 + b * 3 * c, d + c, d - a, a ** 2 * b ** 3 * c], d), 3)
def a1_tt(rng):
    a = rng.randint(2, 12); k = rng.choice([4, 5, 8, 20, 25, 50]); b = 100 // k if 100 % k == 0 else 1
    if b == 1: raise ValueError
    d = a * k * b
    return M(f"Tính nhanh {k} · {a} · {b} bằng:", d, chon3(rng, [d + k, d - b, d * 10, a * (k + b), d + 10], d), 1)
def a1_thuoc(rng):
    a = rng.randint(1, 5); b = a + rng.randint(5, 9); k = rng.randint(a + 1, b - 1)
    return M(f"Cho A = {{x ∈ ℕ | {a} ≤ x ≤ {b}}}. Khẳng định nào đúng?", f"{k} ∈ A", [f"{b + 1} ∈ A", f"{a - 1} ∈ A", f"{k} ∉ A"], 1)
def a1_x(rng):
    t = rng.randint(0, 3); a = rng.randint(2, 30); x = rng.randint(3, 40)
    if t == 0: q, d = f"x + {a} = {x + a}", x
    elif t == 1: q, d = f"x - {a} = {x}", x + a
    elif t == 2: q, d = f"{x + a} - x = {a}", x
    else:
        b = rng.randint(2, 9); q, d = f"{b} · x = {b * x}", x
    return nint(rng, f"Tìm số tự nhiên x, biết {q}. Giá trị của x là:", d, 1, (1, 2, 5), 0)
def a1_chan(rng):
    a = 2 * rng.randint(1, 5); b = a + 2 * rng.randint(3, 12)
    return nint(rng, f"Số phần tử của tập hợp các số tự nhiên chẵn từ {a} đến {b} (kể cả {a} và {b}) là:", (b - a) // 2 + 1, 2, (1, 2), 0)

def b1_tinh(rng):
    a, b, c = rng.randint(2, 5), rng.randint(2, 4), rng.randint(2, 9)
    return T(f"Tính giá trị của biểu thức: {pw(a, 3)} + {c} · {pw(b, 2)} - {a * b}.", f"{pw(a, 3)} = {a**3}; {pw(b, 2)} = {b*b}\n{a**3} + {c}·{b*b} - {a*b} = {a**3} + {c*b*b} - {a*b} = {a**3 + c*b*b - a*b}", 2)
def b1_x(rng):
    a, b = rng.randint(3, 20), rng.randint(2, 9); x = rng.randint(a + 1, 40)
    return T(f"Tìm số tự nhiên x, biết (x - {a}) · {b} = {(x - a) * b}.", f"x - {a} = {(x - a) * b} : {b} = {x - a}\nx = {x - a} + {a} = {x}", 2)
def b1_liet_ke(rng):
    a = rng.randint(0, 5); b = a + rng.randint(3, 6)
    return T(f"Viết tập hợp B = {{x ∈ ℕ | {a} < x ≤ {b}}} bằng cách liệt kê các phần tử. Tập hợp B có bao nhiêu phần tử?", f"B = {tap(list(range(a + 1, b + 1)))}; có {b - a} phần tử.", 1)
def b1_luythua(rng):
    a = rng.randint(2, 7); m, n = rng.randint(2, 5), rng.randint(2, 5)
    return T(f"Viết kết quả phép tính dưới dạng một lũy thừa: {pw(a, m)} · {pw(a, n)} và {pw(a, m + n)} : {pw(a, n)}.", f"{pw(a, m)} · {pw(a, n)} = {pw(a, m + n)}; {pw(a, m + n)} : {pw(a, n)} = {pw(a, m)}", 2)
def b1_loi(rng):
    n, a = rng.randint(3, 9), rng.randint(5, 20); k = rng.randint(2, n * a // 3)
    return T(f"Một cửa hàng có {n} hộp bút, mỗi hộp {a} chiếc. Đã bán {k} chiếc. Hỏi cửa hàng còn bao nhiêu chiếc bút?", f"Số bút ban đầu: {n} · {a} = {n * a}\nCòn lại: {n * a} - {k} = {n * a - k} (chiếc)", 1)
def b1_nhanh(rng):
    a = rng.randint(12, 60)
    return T(f"Tính nhanh: 4 · {a} · 25.", f"4 · 25 · {a} = 100 · {a} = {100 * a}", 1)
def b1_dem(rng):
    a = rng.randint(1, 5); b = a + rng.randint(6, 12)
    return T(f"Tập hợp C = {{x ∈ ℕ | {a} ≤ x ≤ {b}}} có bao nhiêu phần tử? Có bao nhiêu phần tử là số lẻ?", f"Số phần tử: {b} - {a} + 1 = {b - a + 1}\nSố lẻ: {len([x for x in range(a, b + 1) if x % 2])}", 2)

# ============ 2. Tính chia hết ============
def a2_ch(rng):
    k = rng.choice([2, 3, 5, 9])
    for _ in range(300):
        ds = [rng.randint(100, 9999) for _ in range(4)]
        ok = [x for x in ds if x % k == 0]
        if len(ok) == 1 and len(set(ds)) == 4:
            return M(f"Số nào dưới đây chia hết cho {k}?", ok[0], [x for x in ds if x != ok[0]], 1)
    raise ValueError
def a2_khong(rng):
    k = rng.choice([2, 3, 5, 9])
    for _ in range(300):
        ds = [rng.randint(100, 9999) for _ in range(4)]
        kh = [x for x in ds if x % k]
        if len(kh) == 1 and len(set(ds)) == 4:
            return M(f"Số nào dưới đây KHÔNG chia hết cho {k}?", kh[0], [x for x in ds if x != kh[0]], 2)
    raise ValueError
def a2_chuso(rng):
    k = rng.choice([3, 9]); a, b = rng.randint(1, 9), rng.randint(0, 9)
    ds = [d for d in range(10) if (a + b + d) % k == 0]
    if not ds: raise ValueError
    d = max(ds)
    return M(f"Chữ số lớn nhất thay cho * để số {a}*{b} chia hết cho {k} là:", d, chon3(rng, [x for x in range(10) if x != d], d), 3)
def a2_nto(rng):
    p = rng.choice([x for x in range(11, 98) if nguyen_to(x)]); ds = [x for x in range(10, 99) if not nguyen_to(x)]
    return M("Số nào dưới đây là số nguyên tố?", p, rng.sample(ds, 3), 1)
def a2_hop(rng):
    h = rng.choice([x for x in range(10, 99) if not nguyen_to(x)]); ds = [x for x in range(10, 99) if nguyen_to(x)]
    return M("Số nào dưới đây là hợp số?", h, rng.sample(ds, 3), 1)
def _ptt(n):
    out, d = {}, 2
    while n > 1:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1; n //= d
        d += 1
    return out
def _ptts(f):
    return " · ".join(str(p) if e == 1 else pw(p, e) for p, e in sorted(f.items()))
def a2_pttsnt(rng):
    ps_ = rng.sample([2, 3, 5, 7], rng.randint(2, 3)); f = {p: rng.randint(1, 3) for p in ps_}; n = 1
    for p, e in f.items(): n *= p ** e
    d = _ptts(f); sai = []
    for _ in range(12):
        g = dict(f); p = rng.choice(list(g)); g[p] = max(1, g[p] + rng.choice([-1, 1]))
        if g != f: sai.append(_ptts(g))
    return M(f"Phân tích số {n} ra thừa số nguyên tố, ta được:", d, chon3(rng, sai, d), 2)
def a2_ucln(rng):
    g = rng.randint(2, 12)
    while True:
        x, y = rng.randint(2, 9), rng.randint(2, 9)
        if x != y and gcd(x, y) == 1: break
    a, b = g * x, g * y
    return M(f"ƯCLN({a}, {b}) bằng:", g, chon3(rng, [lcm(a, b), g + 1, g * 2, max(g - 1, 1), 1], g), 2)
def a2_bcnn(rng):
    g = rng.randint(1, 6)
    while True:
        x, y = rng.randint(2, 9), rng.randint(2, 9)
        if x != y and gcd(x, y) == 1: break
    a, b = g * x, g * y; d = lcm(a, b)
    return M(f"BCNN({a}, {b}) bằng:", d, chon3(rng, [a * b if a * b != d else a * b + g, g, d * 2, d + g, d - g], d), 2)
def a2_souoc(rng):
    n = rng.choice([12, 18, 20, 24, 28, 30, 36, 40, 45, 48, 50, 60])
    return nint(rng, f"Số {n} có bao nhiêu ước?", len(uoc(n)), 2, (1, 2), 0)
def a2_uc(rng):
    g = rng.randint(2, 6); x, y = rng.sample([2, 3, 5, 7], 2); a, b = g * x * 2, g * y * 2
    c = gcd(a, b); d = tap(uoc(c))
    sai = [tap(uoc(c) + [c + 1]), tap(uoc(c)[:-1]), tap(uoc(a))]
    return M(f"Tập hợp ước chung ƯC({a}, {b}) là:", d, sai, 3)
def a2_chia_deu(rng):
    g = rng.randint(3, 12); x, y = rng.sample(range(2, 8), 2); a, b = g * x, g * y
    return nint(rng, f"Cô giáo có {a} quyển vở và {b} cây bút, muốn chia đều thành các phần quà giống nhau (không thừa). Số phần quà nhiều nhất có thể là:", gcd(a, b), 3, (1, 2), 0)
def a2_bcnn_loi(rng):
    a, b = rng.sample([4, 6, 8, 10, 12, 15], 2)
    return nint(rng, f"Hai bạn trực nhật: bạn An cứ {a} ngày một lần, bạn Bình cứ {b} ngày một lần. Hôm nay cả hai cùng trực. Sau ít nhất bao nhiêu ngày thì cả hai lại cùng trực?", lcm(a, b), 3, (1, 2, 6), 0)

def b2_pt(rng):
    f = {2: rng.randint(1, 3), rng.choice([3, 5]): rng.randint(1, 2), 7: 1}; n = 1
    for p, e in f.items(): n *= p ** e
    return T(f"Phân tích số {n} ra thừa số nguyên tố. Số {n} có bao nhiêu ước?", f"{n} = {_ptts(f)}\nSố ước: " + " · ".join(f"({e}+1)" for e in f.values()) + f" = {len(uoc(n))}", 2)
def b2_ucln(rng):
    g = rng.randint(2, 15); x, y = rng.choice([(2, 3), (3, 4), (2, 5), (3, 5), (4, 5), (5, 6)]); a, b = g * x, g * y
    return T(f"Tìm ƯCLN và BCNN của {a} và {b}.", f"Phân tích: {a} = {_ptts(_ptt(a))}; {b} = {_ptts(_ptt(b))}\nƯCLN({a}, {b}) = {g}\nBCNN({a}, {b}) = {lcm(a, b)}", 2)
def b2_chia(rng):
    g = rng.randint(4, 12); x, y = rng.sample(range(3, 9), 2); a, b = g * x, g * y
    return T(f"Một đội có {a} nam và {b} nữ muốn chia thành các nhóm sao cho số nam và số nữ ở mỗi nhóm đều bằng nhau. Có thể chia nhiều nhất thành bao nhiêu nhóm? Khi đó mỗi nhóm có bao nhiêu nam, bao nhiêu nữ?", f"Số nhóm nhiều nhất là ƯCLN({a}, {b}) = {g}\nMỗi nhóm có {a // g} nam và {b // g} nữ.", 3)
def b2_dauhieu(rng):
    a, b = rng.randint(1, 9), rng.randint(0, 9); ds = [d for d in range(10) if (a + b + d) % 9 == 0]
    if not ds: raise ValueError
    return T(f"Tìm chữ số * để số {a}*{b} chia hết cho 9.", f"Tổng các chữ số {a} + * + {b} phải chia hết cho 9.\nVậy * = {ds[0]} (số {a}{ds[0]}{b}).", 2)
def b2_nto(rng):
    a = rng.randint(10, 40); b = a + rng.randint(8, 15)
    ds = [x for x in range(a, b + 1) if nguyen_to(x)]
    return T(f"Liệt kê các số nguyên tố trong khoảng từ {a} đến {b}.", tap(ds) if ds else "Không có số nguyên tố nào.", 2)
def b2_bcnn(rng):
    a, b = rng.sample([6, 8, 9, 10, 12, 15, 18], 2)
    return T(f"Học sinh khối 6 khi xếp hàng {a}, hàng {b} đều vừa đủ. Biết số học sinh trong khoảng từ {lcm(a, b)} đến {lcm(a, b) * 2 - 1}. Tính số học sinh.", f"Số học sinh là bội chung của {a} và {b}, BCNN = {lcm(a, b)}.\nTrong khoảng cho trước chỉ có {lcm(a, b)}. Vậy có {lcm(a, b)} học sinh.", 3)
def b2_tonghieu(rng):
    k = rng.choice([2, 3, 5, 9]); a = rng.randint(100, 900); b = rng.randint(100, 900)
    return T(f"Không tính tổng, hãy cho biết {k * a} + {k * b} có chia hết cho {k} không? Vì sao?", f"Có, vì mỗi số hạng đều chia hết cho {k} nên tổng chia hết cho {k}.", 1)

# ============ 3. Số nguyên ============
def _s(n): return str(n)
def a3_tang(rng):
    ds = rng.sample(range(-15, 16), 4)
    d = ", ".join(map(str, sorted(ds)))
    sai = [", ".join(map(str, sorted(ds, reverse=True))), ", ".join(map(str, sorted(ds, key=abs))), ", ".join(map(str, rng.sample(ds, 4)))]
    return M(f"Sắp xếp các số {', '.join(map(str, ds))} theo thứ tự tăng dần:", d, [s for s in sai], 2)
def a3_min(rng):
    ds = rng.sample(range(-20, 21), 4); t = rng.choice(["nhỏ", "lớn"]); d = min(ds) if t == "nhỏ" else max(ds)
    return M(f"Số nguyên nào {t} nhất trong các số: {', '.join(map(str, ds))}?", d, [x for x in ds if x != d], 1)
def a3_doi(rng):
    a = rng.choice([x for x in range(-30, 31) if x]); return M(f"Số đối của {a} là:", -a, [a, abs(a) + 1, 0], 1)
def a3_gttd(rng):
    a = rng.choice([x for x in range(-30, 31) if x]); return M(f"Giá trị tuyệt đối |{a}| bằng:", abs(a), chon3(rng, [-abs(a), a if a < 0 else -a, 0, abs(a) + 1], abs(a)), 1)
def a3_cong(rng):
    a, b = rng.randint(-25, 25), rng.randint(-25, 25)
    if a >= 0 and b >= 0: raise ValueError
    return nint(rng, f"Kết quả của phép tính ({a}) + ({b}) là:", a + b, 1, (1, 2, 10))
def a3_tru(rng):
    a, b = rng.randint(-20, 20), rng.randint(-20, 20)
    return nint(rng, f"Kết quả của phép tính ({a}) - ({b}) là:", a - b, 2, (1, 2, 10))
def a3_nhan(rng):
    a, b = rng.randint(-12, 12), rng.randint(-12, 12)
    if abs(a) < 2 or abs(b) < 2: raise ValueError
    return nint(rng, f"Kết quả của phép tính ({a}) · ({b}) là:", a * b, 2, (1, 2, 10))
def a3_chia(rng):
    b = rng.choice([x for x in range(-9, 10) if abs(x) > 1]); q = rng.choice([x for x in range(-12, 13) if x])
    return nint(rng, f"Kết quả của phép tính ({b * q}) : ({b}) là:", q, 2, (1, 2))
def a3_bt(rng):
    a, b, c = rng.randint(-10, 10), rng.randint(2, 9), rng.randint(-6, 6)
    return nint(rng, f"Giá trị của biểu thức ({a}) + {b} · ({c}) là:", a + b * c, 3, (1, 2, 5))
def a3_x(rng):
    a, x = rng.randint(-15, 15), rng.randint(-15, 15)
    return nint(rng, f"Tìm x biết x + ({a}) = {x + a}. Giá trị x là:", x, 2, (1, 2, 5))
def a3_nhiet(rng):
    a, b = rng.randint(-8, 5), rng.randint(3, 12)
    return nint(rng, f"Nhiệt độ buổi sáng là {a}°C, buổi trưa tăng thêm {b}°C. Nhiệt độ buổi trưa là (°C):", a + b, 2, (1, 2, 10))
def a3_tong0(rng):
    a = rng.randint(3, 9); return nint(rng, f"Tổng tất cả các số nguyên x thỏa mãn -{a} ≤ x ≤ {a} bằng:", 0, 3, (1, 2, 5))
def a3_ptu(rng):
    a, b = rng.randint(2, 9), rng.randint(2, 9); return nint(rng, f"Tập hợp các số nguyên x thỏa mãn -{a} ≤ x ≤ {b} có bao nhiêu phần tử?", a + b + 1, 3, (1, 2), 0)

def b3_tinh(rng):
    a, b, c = rng.randint(-20, 20), rng.randint(-20, 20), rng.randint(-20, 20)
    return T(f"Tính: ({a}) + ({b}) - ({c}).", f"({a}) + ({b}) = {a + b}\n{a + b} - ({c}) = {a + b - c}", 1)
def b3_nhan(rng):
    a, b, c = rng.randint(-9, 9), rng.randint(2, 9), rng.randint(-9, 9)
    return T(f"Tính: ({a}) · {b} + ({c}) · ({a}).", f"= ({a}) · ({b} + ({c})) = ({a}) · {b + c} = {a * (b + c)}", 2)
def b3_x(rng):
    a, b, x = rng.randint(2, 7), rng.randint(-15, 15), rng.randint(-10, 10)
    return T(f"Tìm số nguyên x, biết {a} · x + ({b}) = {a * x + b}.", f"{a} · x = {a * x + b} - ({b}) = {a * x}\nx = {x}", 2)
def b3_nhiet(rng):
    a, b = rng.randint(-10, -1), rng.randint(5, 12)
    return T(f"Nhiệt độ lúc 6 giờ sáng ở một thành phố là {a}°C. Đến 12 giờ trưa nhiệt độ tăng thêm {b}°C, chiều giảm {b - 2}°C so với buổi trưa. Tính nhiệt độ buổi chiều.", f"Buổi trưa: {a} + {b} = {a + b}°C\nBuổi chiều: {a + b} - {b - 2} = {a + 2}°C", 2)
def b3_ss(rng):
    ds = rng.sample(range(-25, 26), 5)
    return T(f"Sắp xếp các số sau theo thứ tự giảm dần: {', '.join(map(str, ds))}.", ", ".join(map(str, sorted(ds, reverse=True))), 1)
def b3_gt(rng):
    a = rng.randint(2, 15); b = rng.randint(2, 15)
    return T(f"Tìm các số nguyên x biết |x| = {a}. Tính tổng hai giá trị tìm được.", f"x = {a} hoặc x = -{a}\nTổng: {a} + (-{a}) = 0", 2)
def b3_do_cao(rng):
    a, b = rng.randint(50, 300), rng.randint(20, 150)
    return T(f"Một tàu ngầm đang ở độ sâu {a} m (so với mực nước biển), sau đó nổi lên {b} m. Hỏi tàu đang ở độ cao bao nhiêu (viết bằng số nguyên)?", f"Độ cao ban đầu: -{a}\nSau khi nổi: -{a} + {b} = {-a + b} (m)", 2)

# ============ 4. Một số hình phẳng ============
def a4_cv_hcn(rng):
    a, b = rng.randint(3, 25), rng.randint(2, 20)
    if a == b: raise ValueError
    return nint(rng, f"Hình chữ nhật có chiều dài {a} cm, chiều rộng {b} cm. Chu vi hình chữ nhật là (cm):", 2 * (a + b), 1, (2, 4, 10), 0)
def a4_dt_hcn(rng):
    a, b = rng.randint(3, 25), rng.randint(2, 20)
    if a == b: raise ValueError
    return nint(rng, f"Hình chữ nhật có chiều dài {a} cm, chiều rộng {b} cm. Diện tích hình chữ nhật là (cm²):", a * b, 1, (a, b, 2 * (a + b)), 0)
def a4_cv_vuong(rng):
    a = rng.randint(3, 30); return nint(rng, f"Hình vuông có cạnh {a} cm. Chu vi hình vuông là (cm):", 4 * a, 1, (a, 4, 8), 0)
def a4_dt_vuong(rng):
    a = rng.randint(3, 30); return nint(rng, f"Hình vuông có cạnh {a} cm. Diện tích hình vuông là (cm²):", a * a, 1, (a, 2 * a, 4), 0)
def a4_tg_deu(rng):
    a = rng.randint(3, 40); return nint(rng, f"Tam giác đều có cạnh {a} cm. Chu vi tam giác là (cm):", 3 * a, 1, (a, 3, 6), 0)
def a4_luc_giac(rng):
    a = rng.randint(3, 20); return nint(rng, f"Lục giác đều có cạnh {a} cm. Chu vi lục giác đều là (cm):", 6 * a, 1, (a, 6, 12), 0)
def a4_thoi(rng):
    a, b = rng.randint(3, 20), rng.randint(2, 20) * 2
    if a == b: raise ValueError
    return nint(rng, f"Hình thoi có hai đường chéo dài {a * 2} cm và {b} cm. Diện tích hình thoi là (cm²):", a * b, 2, (a, b, 10), 0)
def a4_binh_hanh(rng):
    a, h = rng.randint(4, 25), rng.randint(2, 15)
    return nint(rng, f"Hình bình hành có cạnh đáy {a} cm và chiều cao tương ứng {h} cm. Diện tích hình bình hành là (cm²):", a * h, 2, (a, h, 10), 0)
def a4_cv_bh(rng):
    a, b = rng.randint(3, 25), rng.randint(3, 25)
    if a == b: raise ValueError
    return nint(rng, f"Hình bình hành có hai cạnh liên tiếp dài {a} cm và {b} cm. Chu vi hình bình hành là (cm):", 2 * (a + b), 2, (2, 4, 10), 0)
def a4_thang_can(rng):
    a, b, c = rng.randint(4, 12), rng.randint(14, 24), rng.randint(3, 10)
    return nint(rng, f"Hình thang cân có hai đáy dài {a} cm và {b} cm, cạnh bên dài {c} cm. Chu vi hình thang cân là (cm):", a + b + 2 * c, 2, (c, 2, 10), 0)
def a4_canh(rng):
    a = rng.randint(3, 30); return nint(rng, f"Hình vuông có chu vi {4 * a} cm. Cạnh hình vuông dài (cm):", a, 2, (1, 2, 4), 0)
def a4_rong(rng):
    a, b = rng.randint(6, 25), rng.randint(3, 15)
    if a <= b: raise ValueError
    return nint(rng, f"Hình chữ nhật có diện tích {a * b} cm² và chiều dài {a} cm. Chiều rộng là (cm):", b, 2, (1, 2, 4), 0)
def a4_gach(rng):
    k = rng.randint(2, 5); a, b = rng.randint(2, 8) * k, rng.randint(2, 8) * k
    return nint(rng, f"Nền phòng hình chữ nhật dài {a} m, rộng {b} m, lát bằng gạch hình vuông cạnh {k} m. Cần ít nhất bao nhiêu viên gạch?", (a // k) * (b // k), 3, (1, 2, 4), 0)
def a4_tc(rng):
    return M(rng.choice(["Hình nào dưới đây có bốn cạnh bằng nhau?", "Hình nào sau đây có bốn cạnh bằng nhau và hai đường chéo vuông góc?"]), "Hình thoi", ["Hình chữ nhật (chiều dài khác chiều rộng)", "Hình thang cân", "Tam giác đều"], 1)

def b4_hcn(rng):
    a, b = rng.randint(8, 30), rng.randint(3, 15); a = a if a != b else a + 1
    return T(f"Một mảnh vườn hình chữ nhật có chiều dài {a} m, chiều rộng {b} m. Tính chu vi và diện tích mảnh vườn.", f"Chu vi: 2 · ({a} + {b}) = {2 * (a + b)} m\nDiện tích: {a} · {b} = {a * b} m²", 1)
def b4_hv(rng):
    a = rng.randint(5, 25); return T(f"Một sân hình vuông có chu vi {4 * a} m. Tính diện tích sân.", f"Cạnh sân: {4 * a} : 4 = {a} m\nDiện tích: {a} · {a} = {a * a} m²", 2)
def b4_thoi(rng):
    a, b = rng.randint(3, 14) * 2, rng.randint(3, 14) * 2
    return T(f"Hình thoi ABCD có hai đường chéo AC = {a} cm và BD = {b} cm. Tính diện tích hình thoi.", f"S = (AC · BD) : 2 = ({a} · {b}) : 2 = {a * b // 2} cm²", 2)
def b4_bh(rng):
    a, h = rng.randint(6, 30), rng.randint(3, 14)
    return T(f"Một thửa ruộng hình bình hành có cạnh đáy {a} m, chiều cao {h} m. Tính diện tích thửa ruộng.", f"S = {a} · {h} = {a * h} m²", 1)
def b4_gach(rng):
    k = rng.randint(2, 5); a, b = rng.randint(3, 10) * k, rng.randint(3, 10) * k
    return T(f"Một căn phòng hình chữ nhật dài {a} m, rộng {b} m được lát bằng những viên gạch vuông cạnh {k} m. Tính số viên gạch cần dùng và chu vi căn phòng.", f"Số gạch: ({a} : {k}) · ({b} : {k}) = {(a // k) * (b // k)} viên\nChu vi: 2 · ({a} + {b}) = {2 * (a + b)} m", 2)
def b4_tang(rng):
    a, b = rng.randint(5, 20), rng.randint(3, 12)
    return T(f"Hình chữ nhật có chiều dài {a} cm, chiều rộng {b} cm. Nếu tăng chiều dài thêm 2 cm và giữ nguyên chiều rộng thì diện tích tăng thêm bao nhiêu?", f"Diện tích cũ: {a} · {b} = {a * b}\nDiện tích mới: {a + 2} · {b} = {(a + 2) * b}\nTăng thêm: {2 * b} cm²", 3)
def b4_tl(rng):
    a = rng.randint(4, 15); b = rng.randint(4, 15)
    return T(f"Một hình thang cân có hai đáy {a} cm, {a + b} cm và cạnh bên {rng.randint(3, 9)} cm. Hãy nêu cách tính chu vi và tính chu vi.", "Chu vi = tổng bốn cạnh = đáy nhỏ + đáy lớn + 2 · cạnh bên.", 2) if False else T(f"Cho tam giác đều có chu vi {3 * a} cm. Tính cạnh của tam giác đều đó và chu vi lục giác đều có cùng độ dài cạnh.", f"Cạnh: {3 * a} : 3 = {a} cm\nChu vi lục giác đều: 6 · {a} = {6 * a} cm", 2)

# ============ 5. Tính đối xứng ============
HINH = {  # tên: (số trục, có tâm)
    "tam giác đều": (3, False), "hình vuông": (4, True), "hình chữ nhật (không phải hình vuông)": (2, True), "hình thoi (không phải hình vuông)": (2, True),
    "hình bình hành (không phải hình chữ nhật, hình thoi)": (0, True), "hình thang cân (không phải hình chữ nhật)": (1, False), "lục giác đều": (6, True), "đường tròn": (-1, True),
}
CHU = {"A": (1, False), "H": (1, True), "O": (2, True), "M": (1, False), "T": (1, False), "E": (1, False), "X": (2, True), "S": (0, True), "Z": (0, True), "N": (0, True), "I": (2, True), "L": (0, False), "P": (0, False)}
CHU[ "H" ] = (2, True)
def _trucs(n): return "vô số trục" if n < 0 else f"{n} trục"
def a5_truc(rng):
    ten = rng.choice(list(HINH)); n = HINH[ten][0]; d = _trucs(n)
    return M(f"{ten[0].upper() + ten[1:]} có bao nhiêu trục đối xứng?", d, [x for x in ["0 trục", "1 trục", "2 trục", "3 trục", "4 trục", "6 trục", "vô số trục"] if x != d][:6] and chon3(rng, ["0 trục", "1 trục", "2 trục", "3 trục", "4 trục", "6 trục", "vô số trục"], d), 1)
def a5_tam(rng):
    co = [k for k, v in HINH.items() if v[1]]; khong = [k for k, v in HINH.items() if not v[1]]
    if rng.random() < .5: return M("Hình nào sau đây có tâm đối xứng?", rng.choice(co), rng.sample(khong, 3), 2)
    return M("Hình nào sau đây KHÔNG có tâm đối xứng?", rng.choice(khong), rng.sample(co, 3), 2)
def a5_co_tam(rng):
    ten = rng.choice(list(HINH)); d = "Có" if HINH[ten][1] else "Không"
    return M(f"{ten[0].upper() + ten[1:]} có tâm đối xứng không?", d, ["Không" if d == "Có" else "Có", "Chỉ khi các cạnh bằng nhau", "Chỉ khi có góc vuông"], 2)
def a5_nhieu_truc(rng):
    k = rng.choice([1, 2, 3, 4]); d = [t for t, v in HINH.items() if v[0] == k]
    if not d: raise ValueError
    sai = [t for t, v in HINH.items() if v[0] != k]
    return M(f"Hình nào sau đây có đúng {k} trục đối xứng?", rng.choice(d), rng.sample(sai, 3), 2)
def a5_chu_truc(rng):
    c = rng.choice(list(CHU)); n = CHU[c][0]
    return M(f"Chữ cái in hoa \"{c}\" có bao nhiêu trục đối xứng (dạng chữ in thường dùng trong sách)?", _trucs(n), chon3(rng, ["0 trục", "1 trục", "2 trục", "3 trục", "4 trục"], _trucs(n)), 3)
def a5_chu_co(rng):
    co = [c for c, v in CHU.items() if v[0] >= 1]; khong = [c for c, v in CHU.items() if v[0] == 0]
    return M("Chữ cái in hoa nào sau đây có ít nhất một trục đối xứng?", rng.choice(co), rng.sample(khong, 3), 2)
def a5_ngoai(rng):
    return M("Phát biểu nào đúng về hình có trục đối xứng?", "Gấp hình theo trục đó thì hai phần chồng khít lên nhau", ["Hình luôn có tâm đối xứng", "Hình luôn có bốn cạnh bằng nhau", "Hình luôn có số trục đối xứng bằng số cạnh"], 2)
def a5_ntruc(rng):
    ten = rng.choice(["tam giác đều", "hình vuông", "lục giác đều"]); n = {"tam giác đều": 3, "hình vuông": 4, "lục giác đều": 6}[ten]
    return M(f"Số trục đối xứng của {ten} bằng số cạnh của nó không? Chọn đáp án đúng.", "Có, bằng " + str(n), ["Không, ít hơn số cạnh", "Không, nhiều hơn số cạnh", "Chỉ bằng khi cạnh lẻ"], 3)
def b5_truc(rng):
    ds = rng.sample(list(HINH), 4)
    return T("Cho biết số trục đối xứng của: " + "; ".join(ds) + ".", "\n".join(f"{t}: {_trucs(HINH[t][0])}" for t in ds), 1)
def b5_tam(rng):
    ds = rng.sample(list(HINH), 5)
    return T("Trong các hình sau, hình nào có tâm đối xứng: " + "; ".join(ds) + "?", "Có tâm đối xứng: " + "; ".join(t for t in ds if HINH[t][1]) + "." if any(HINH[t][1] for t in ds) else "Không có hình nào.", 2)
def b5_chu(rng):
    ds = rng.sample(list(CHU), 6)
    return T("Cho biết các chữ cái in hoa nào có trục đối xứng và chỉ rõ số trục: " + ", ".join(ds) + ".", "\n".join(f"{c}: {_trucs(CHU[c][0])}" for c in ds), 2)
def b5_ve(rng):
    return T(rng.choice(["Nêu ba vật dụng hoặc hình ảnh trong thực tế có trục đối xứng và cho biết trục đối xứng của chúng.", "Nêu hai vật trong thực tế có tâm đối xứng."]),
             "Ví dụ: lá cây, cánh bướm, mặt người (một trục); chiếc quạt trần, bánh xe, nút áo (có tâm đối xứng).", 2)
def b5_mc(rng):
    k = rng.choice([1, 2, 3, 4, 6]); d = [t for t, v in HINH.items() if v[0] == k]
    if not d: raise ValueError
    return T(f"Hình nào sau đây có đúng {k} trục đối xứng? Hãy kể tên một hình và nêu đặc điểm của nó.", d[0] + ".", 2)

# ============ 6. Phân số ============
def a6_rutgon(rng):
    f = ngt(rng, 12); k = rng.randint(2, 7); d = ps(f)
    return M(f"Rút gọn phân số {f.numerator * k}/{f.denominator * k} ta được:", d, nh_ps(rng, f), 1)
def a6_ss(rng):
    a, b = ngt(rng, 12), ngt(rng, 12)
    if a == b: raise ValueError
    return M(f"Chọn dấu thích hợp: {ps(a)} ... {ps(b)}", kq_dau(a, b), sai_dau(kq_dau(a, b)), 2)
def a6_cong(rng):
    a, b = ngt(rng, 9), ngt(rng, 9); d = ps(a + b)
    return M(f"{ps(a)} + {ps(b)} = ?", d, nh_ps(rng, a + b), 2)
def a6_tru(rng):
    a, b = ngt(rng, 9), ngt(rng, 9)
    if a <= b: a, b = b, a
    if a == b: raise ValueError
    return M(f"{ps(a)} - {ps(b)} = ?", ps(a - b), nh_ps(rng, a - b), 2)
def a6_nhan(rng):
    a, b = ngt(rng, 9), ngt(rng, 9); return M(f"{ps(a)} · {ps(b)} = ?", ps(a * b), nh_ps(rng, a * b), 2)
def a6_chia(rng):
    a, b = ngt(rng, 9), ngt(rng, 9); return M(f"{ps(a)} : {ps(b)} = ?", ps(a / b), nh_ps(rng, a / b), 3)
def a6_nghich(rng):
    a = ngt(rng, 12); return M(f"Số nghịch đảo của phân số {ps(a)} là:", ps(1 / a), [ps(a), ps(-a) if False else f"-{ps(a)}", ps(1 - a)], 1)
def a6_cua(rng):
    a = ngt(rng, 9); n = a.denominator * rng.randint(2, 12); d = n * a.numerator // a.denominator
    return nint(rng, f"{ps(a)} của {n} bằng:", d, 2, (a.numerator, 2, 5), 0)
def a6_tim_so(rng):
    a = ngt(rng, 9); n = a.denominator * rng.randint(2, 12); m = n * a.numerator // a.denominator
    return nint(rng, f"Biết {ps(a)} của một số bằng {m}. Số đó là:", n, 3, (a.denominator, 2, 5), 0)
def a6_bang(rng):
    f = ngt(rng, 9); k = rng.randint(2, 9); x = f.numerator * k
    return nint(rng, f"Tìm x biết {f.numerator}/{f.denominator} = x/{f.denominator * k}. Giá trị x là:", x, 2, (k, 2, 5), 0)
def a6_tim_x(rng):
    a, b = ngt(rng, 9), ngt(rng, 9)
    return M(f"Tìm x biết x + {ps(a)} = {ps(a + b)}. Giá trị x là:", ps(b), nh_ps(rng, b), 3)
def a6_lon_nhat(rng):
    ds = []
    while len(ds) < 4:
        f = ngt(rng, 12)
        if f not in ds: ds.append(f)
    t = rng.choice(["lớn", "nhỏ"]); d = max(ds) if t == "lớn" else min(ds)
    return M(f"Phân số nào {t} nhất trong các phân số: {', '.join(ps(x) for x in ds)}?", ps(d), [ps(x) for x in ds if x != d], 2)
def a6_hs(rng):
    w = rng.randint(1, 5); f = ngt(rng, 9); t = w + f; n, d = f.numerator, f.denominator
    return M(f"Hỗn số {w} {n}/{d} viết thành phân số là:", ps(t), chon3(rng, [f"{w + n}/{d}", f"{w * n + d}/{d}", f"{w * d + n}/{d + 1}", f"{w * d - n}/{d}"], ps(t)), 2)
def a6_sach(rng):
    n = rng.randint(2, 6) * 8; a = ngt(rng, 8)
    if n % a.denominator: raise ValueError
    r = n - n * a.numerator // a.denominator
    return nint(rng, f"Một quyển sách dày {n} trang. Bạn Lan đã đọc {ps(a)} số trang. Số trang còn lại là:", r, 3, (a.numerator, 2, 4), 0)

def b6_tinh(rng):
    a, b, c = ngt(rng, 8), ngt(rng, 8), ngt(rng, 8)
    return T(f"Tính: {ps(a)} + {ps(b)} · {ps(c)}.", f"{ps(b)} · {ps(c)} = {ps(b * c)}\n{ps(a)} + {ps(b * c)} = {ps(a + b * c)}", 2)
def b6_x(rng):
    a, b, c = ngt(rng, 8), ngt(rng, 8), ngt(rng, 8)
    return T(f"Tìm x, biết x · {ps(b)} = {ps(a * b)}.", f"x = {ps(a * b)} : {ps(b)} = {ps(a)}", 2)
def b6_ss(rng):
    ds = []
    while len(ds) < 4:
        f = ngt(rng, 12)
        if f not in ds: ds.append(f)
    return T(f"Sắp xếp các phân số sau theo thứ tự tăng dần: {', '.join(ps(x) for x in ds)}.", ", ".join(ps(x) for x in sorted(ds)), 2)
def b6_loi(rng):
    n = rng.randint(2, 6) * 12; a, b = Fraction(1, 3), Fraction(1, 4)
    return T(f"Một lớp có {n} học sinh. Số học sinh giỏi chiếm 1/3 số học sinh cả lớp, số học sinh khá chiếm 1/4. Tính số học sinh giỏi, số học sinh khá và số học sinh còn lại.", f"Giỏi: {n} · 1/3 = {n // 3}\nKhá: {n} · 1/4 = {n // 4}\nCòn lại: {n} - {n // 3} - {n // 4} = {n - n // 3 - n // 4}", 2)
def b6_tim_so(rng):
    a = ngt(rng, 9); n = a.denominator * rng.randint(2, 9); m = n * a.numerator // a.denominator
    return T(f"Một người đã đi được {m} km, bằng {ps(a)} quãng đường. Tính cả quãng đường và quãng đường còn lại.", f"Cả quãng đường: {m} : {ps(a)} = {n} km\nCòn lại: {n} - {m} = {n - m} km", 3)
def b6_rutgon(rng):
    f = ngt(rng, 12); k = rng.randint(2, 6); g = rng.randint(2, 5)
    return T(f"Rút gọn các phân số {f.numerator * k}/{f.denominator * k} và {f.numerator * k * g}/{f.denominator * k * g} về phân số tối giản. Hai phân số có bằng nhau không?", f"Cả hai đều bằng {ps(f)}. Vậy hai phân số bằng nhau.", 1)

# ============ 7. Số thập phân và tỉ số phần trăm ============
def a7_cong(rng):
    a, b = rd(rng, 1, 90, 1), rd(rng, 1, 90, 1); d = a + b
    return M(f"{tp(a)} + {tp(b)} = ?", tp(d), [tp(x) for x in dec_gan(rng, d)], 1)
def a7_tru(rng):
    a, b = rd(rng, 10, 90, 2), rd(rng, 1, 9, 2); d = a - b
    return M(f"{tp(a)} - {tp(b)} = ?", tp(d), [tp(x) for x in dec_gan(rng, d)], 1)
def a7_nhan(rng):
    a, b = rd(rng, 1, 20, 1), rd(rng, 2, 9, 1); d = a * b
    return M(f"{tp(a)} × {tp(b)} = ?", tp(d), [tp(x) for x in dec_gan(rng, d)], 2)
def a7_chia(rng):
    b = rd(rng, 2, 9, 0); q = rd(rng, 1, 30, 1); a = b * q
    return M(f"{tp(a)} : {tp(b)} = ?", tp(q), [tp(x) for x in dec_gan(rng, q)], 2)
def a7_ss(rng):
    a, b = rd(rng, 1, 30, 2), rd(rng, 1, 30, 2)
    if a == b: raise ValueError
    d = ">" if a > b else "<"; return M(f"Chọn dấu thích hợp: {tp(a)} ... {tp(b)}", d, sai_dau(d), 1)
def a7_lt(rng):
    x = rd(rng, 1, 90, 3); k = rng.choice([("đến hàng phần trăm", 2), ("đến hàng phần mười", 1), ("đến hàng đơn vị", 0)]); j = k[1]
    d = tpf(x, j)
    sai = [tpf(x.quantize(D(1).scaleb(-i), rounding="ROUND_DOWN"), i) for i in (0, 1, 2)] + [tpf(D(d.replace(",", ".")) + D(1).scaleb(-j), j), tpf(D(d.replace(",", ".")) - D(1).scaleb(-j), j)]
    return M(f"Làm tròn số {tp(x)} {k[0]} ta được:", d, chon3(rng, sai, d), 2)
def a7_pt_cua(rng):
    p = rng.choice([5, 10, 20, 25, 40, 50, 60, 75]); n = rng.randint(2, 12) * 20
    return nint(rng, f"{p}% của {n} bằng:", n * p // 100, 2, (2, 5, 10), 0)
def a7_ti_so(rng):
    p = rng.choice([10, 20, 25, 40, 50, 75, 80]); b = rng.randint(2, 9) * 20; a = b * p // 100
    return M(f"Tỉ số phần trăm của {a} và {b} là:", f"{p}%", chon3(rng, [f"{p + 5}%", f"{p - 5}%", f"{100 - p}%", f"{p * 2}%"], f"{p}%"), 2)
def a7_tim_so(rng):
    p = rng.choice([10, 20, 25, 40, 50]); n = rng.randint(2, 9) * 20; m = n * p // 100
    return nint(rng, f"Biết {p}% của một số bằng {m}. Số đó là:", n, 3, (10, 20, 5), 0)
def a7_giam(rng):
    g = rng.randint(2, 8) * 50000; p = rng.choice([10, 20, 25, 30]); d = g - g * p // 100
    return M(f"Một chiếc áo giá {g} đồng, giảm giá {p}%. Giá sau khi giảm là (đồng):", d, chon3(rng, [g * p // 100, g + g * p // 100, g - p, d + 10000], d), 3)
def a7_ps_pt(rng):
    d = rng.choice([2, 4, 5, 10, 20, 25, 50]); n = rng.randint(1, d - 1); p = n * 100 // d
    return M(f"Viết phân số {n}/{d} dưới dạng tỉ số phần trăm:", f"{p}%", chon3(rng, [f"{p + 10}%", f"{max(p - 10, 5)}%", f"{n}%", f"{d}%"], f"{p}%"), 2)
def a7_tp_pt(rng):
    a = rd(rng, 1, 99, 2); d = f"{tp(a * 100)}%"
    return M(f"Viết số thập phân {tp(a)} dưới dạng tỉ số phần trăm:", d, chon3(rng, [f"{tp(a)}%", f"{tp(a * 10)}%", f"{tp(a / 10)}%", f"{tp(a / 100)}%"], d), 2)

def b7_tinh(rng):
    a, b, c = rd(rng, 1, 30, 1), rd(rng, 1, 9, 1), rd(rng, 1, 9, 1)
    return T(f"Tính: {tp(a)} + {tp(b)} × {tp(c)}.", f"{tp(b)} × {tp(c)} = {tp(b * c)}\n{tp(a)} + {tp(b * c)} = {tp(a + b * c)}", 2)
def b7_x(rng):
    a, x = rd(rng, 1, 30, 1), rd(rng, 1, 30, 1)
    return T(f"Tìm x, biết x + {tp(a)} = {tp(x + a)}.", f"x = {tp(x + a)} - {tp(a)} = {tp(x)}", 1)
def b7_lt(rng):
    x = rd(rng, 1, 90, 3)
    return T(f"Làm tròn số {tp(x)} đến hàng phần mười và đến hàng phần trăm.", f"Đến hàng phần mười: {tpf(x, 1)}\nĐến hàng phần trăm: {tpf(x, 2)}", 1)
def b7_pt(rng):
    n = rng.randint(2, 9) * 20; p = rng.choice([20, 30, 40, 60, 80])
    return T(f"Một lớp có {n} học sinh, trong đó {p}% là học sinh nữ. Tính số học sinh nữ và số học sinh nam.", f"Số học sinh nữ: {n} · {p}% = {n * p // 100}\nSố học sinh nam: {n} - {n * p // 100} = {n - n * p // 100}", 2)
def b7_giam(rng):
    g = rng.randint(2, 9) * 100000; p = rng.choice([10, 15, 20, 25])
    return T(f"Một đôi giày giá {g} đồng, được giảm {p}%. Hỏi phải trả bao nhiêu tiền?", f"Số tiền được giảm: {g} · {p}% = {g * p // 100}\nPhải trả: {g} - {g * p // 100} = {g - g * p // 100} đồng", 2)
def b7_tiso(rng):
    p = rng.choice([20, 25, 40, 60, 75]); b = rng.randint(2, 8) * 20; a = b * p // 100
    return T(f"Trong {b} học sinh có {a} bạn thích đá bóng. Tính tỉ số phần trăm số bạn thích đá bóng so với cả nhóm.", f"{a} : {b} = {p / 100}\nTỉ số phần trăm: {p}%", 2)
def b7_tim(rng):
    p = rng.choice([20, 25, 40, 50]); n = rng.randint(2, 9) * 20; m = n * p // 100
    return T(f"Một người gửi tiết kiệm, sau một năm nhận lãi {m} nghìn đồng, bằng {p}% số tiền gửi. Tính số tiền gửi ban đầu.", f"Số tiền gửi: {m} : {p}% = {n} nghìn đồng", 3)

# ============ 8. Điểm, đường thẳng, đoạn thẳng, góc ============
def a8_cong(rng):
    a, b = rng.randint(2, 15), rng.randint(2, 15)
    return nint(rng, f"Điểm M nằm giữa hai điểm A và B. Biết AM = {a} cm, MB = {b} cm. Độ dài AB là (cm):", a + b, 1, (1, 2, 5), 0)
def a8_tru(rng):
    a, b = rng.randint(8, 25), rng.randint(2, 7)
    return nint(rng, f"Điểm M nằm giữa hai điểm A và B. Biết AB = {a} cm, AM = {b} cm. Độ dài MB là (cm):", a - b, 1, (1, 2, 5), 0)
def a8_trung(rng):
    a = rng.randint(2, 15); return nint(rng, f"M là trung điểm của đoạn thẳng AB. Biết AM = {a} cm. Độ dài AB là (cm):", 2 * a, 1, (a, 2, 4), 0)
def a8_trung2(rng):
    a = rng.randint(2, 15) * 2; return nint(rng, f"M là trung điểm của đoạn thẳng AB dài {a} cm. Độ dài AM là (cm):", a // 2, 1, (1, 2, 4), 0)
def a8_doan(rng):
    n = rng.randint(3, 8); return nint(rng, f"Cho {n} điểm phân biệt, trong đó không có ba điểm nào thẳng hàng. Số đoạn thẳng nối hai trong các điểm đó là:", n * (n - 1) // 2, 3, (1, 2, 5), 0)
def a8_duong(rng):
    n = rng.randint(3, 8); return nint(rng, f"Cho {n} điểm phân biệt, không có ba điểm nào thẳng hàng. Vẽ các đường thẳng đi qua từng cặp điểm. Số đường thẳng vẽ được là:", n * (n - 1) // 2, 3, (1, 2, 5), 0)
def a8_loai(rng):
    x = rng.choice([30, 45, 60, 80, 90, 100, 120, 135, 150, 180, 20, 70]); d = "góc vuông" if x == 90 else "góc bẹt" if x == 180 else "góc nhọn" if x < 90 else "góc tù"
    return M(f"Góc có số đo {x}° là:", d, [y for y in ["góc nhọn", "góc vuông", "góc tù", "góc bẹt"] if y != d], 1)
def a8_ke_bu(rng):
    x = rng.randint(20, 160); return nint(rng, f"Hai góc kề bù, một góc có số đo {x}°. Số đo góc còn lại là (độ):", 180 - x, 2, (10, 20, 30), 0)
def a8_phu(rng):
    x = rng.randint(10, 80); return nint(rng, f"Hai góc phụ nhau, một góc có số đo {x}°. Số đo góc còn lại là (độ):", 90 - x, 2, (10, 20, 5), 0)
def a8_pg(rng):
    x = rng.randint(2, 8) * 20; return nint(rng, f"Tia Oz là tia phân giác của góc xOy có số đo {x}°. Số đo góc xOz là (độ):", x // 2, 2, (10, 20, 5), 0)
def a8_gocgoc(rng):
    a, b = rng.randint(20, 80), rng.randint(20, 80)
    return nint(rng, f"Tia Oy nằm giữa hai tia Ox và Oz. Biết xOy = {a}°, yOz = {b}°. Số đo góc xOz là (độ):", a + b, 2, (10, 20, 5), 0)
def a8_n_tia(rng):
    n = rng.randint(3, 7); return nint(rng, f"Cho {n} tia chung gốc O (không có hai tia nào trùng nhau, không có hai tia đối nhau). Số góc có đỉnh O tạo bởi các tia đó là:", n * (n - 1) // 2, 3, (1, 2, 5), 0)

def b8_doan(rng):
    a, b = rng.randint(4, 12), rng.randint(2, 9)
    return T(f"Trên tia Ox lấy hai điểm A, B sao cho OA = {a} cm, OB = {a + b} cm. Chứng tỏ A nằm giữa O và B rồi tính AB.", f"Vì OA < OB nên A nằm giữa O và B.\nOA + AB = OB ⇒ AB = {a + b} - {a} = {b} cm.", 2)
def b8_trung(rng):
    a = rng.randint(3, 10) * 2
    return T(f"Cho đoạn thẳng AB = {a} cm. Gọi M là trung điểm của AB. Tính AM và MB.", f"AM = MB = AB : 2 = {a} : 2 = {a // 2} cm.", 1)
def b8_goc(rng):
    a = rng.randint(20, 70); b = rng.randint(a + 20, 150)
    return T(f"Trên cùng một nửa mặt phẳng bờ chứa tia Ox, vẽ hai tia Oy, Oz sao cho xOy = {a}°, xOz = {b}°. Tính yOz và cho biết tia nào nằm giữa hai tia còn lại.", f"Vì xOy < xOz nên Oy nằm giữa Ox và Oz.\nxOy + yOz = xOz ⇒ yOz = {b} - {a} = {b - a}°.", 2)
def b8_pg(rng):
    x = rng.randint(2, 8) * 20
    return T(f"Cho góc xOy = {x}°. Vẽ tia phân giác Oz của góc xOy. Tính xOz, zOy.", f"xOz = zOy = {x} : 2 = {x // 2}°.", 1)
def b8_kebu(rng):
    x = rng.randint(30, 150)
    return T(f"Hai góc xOy và yOz kề bù, xOy = {x}°. Tính yOz. Gọi Ot là phân giác của góc xOy, tính xOt.", f"yOz = 180° - {x}° = {180 - x}°\nxOt = {x} : 2 = {x / 2:g}°", 2)
def b8_so(rng):
    n = rng.randint(4, 8)
    return T(f"Cho {n} điểm phân biệt, trong đó không có ba điểm nào thẳng hàng. Hỏi có bao nhiêu đường thẳng đi qua hai trong các điểm đó?", f"Mỗi điểm nối với {n - 1} điểm còn lại; mỗi đường được đếm hai lần.\nSố đường thẳng: {n} · {n - 1} : 2 = {n * (n - 1) // 2}", 3)

# ============ 9. Dữ liệu và xác suất thực nghiệm ============
def a9_xs(rng):
    n = rng.randint(2, 9) * 10; a = rng.randint(n // 5, n // 2); f = Fraction(a, n)
    return M(f"Tung một đồng xu {n} lần, được mặt sấp {a} lần. Xác suất thực nghiệm xuất hiện mặt sấp (viết dưới dạng phân số tối giản) là:", ps(f), nh_ps(rng, f), 2)
def a9_bong(rng):
    n = rng.randint(3, 9) * 10; a = rng.randint(n // 5, n // 2); f = Fraction(a, n)
    return M(f"Lấy ngẫu nhiên một quả bóng từ hộp, ghi màu rồi trả lại. Sau {n} lần lấy, có {a} lần được bóng đỏ. Xác suất thực nghiệm lấy được bóng đỏ (phân số tối giản) là:", ps(f), nh_ps(rng, f), 2)
def a9_kq(rng):
    return M(rng.choice(["Tung một con xúc xắc, số kết quả có thể xảy ra là:", "Gieo một con xúc xắc 6 mặt, có bao nhiêu kết quả có thể?"]), 6, [4, 5, 12], 1)
def a9_kq2(rng):
    return M("Tung đồng thời hai đồng xu, số kết quả có thể xảy ra là:", 4, [2, 3, 6], 2)
def a9_kq3(rng):
    k = rng.randint(3, 8); return nint(rng, f"Trong hộp có {k} quả bóng với {k} màu khác nhau. Lấy ngẫu nhiên một quả bóng, số kết quả có thể xảy ra là:", k, 1, (1, 2), 0)
def _du_lieu(rng):
    ten = ["Bóng đá", "Cầu lông", "Bơi", "Cờ vua", "Đọc sách"]; ten = rng.sample(ten, 4)
    v = [rng.randint(3, 15) for _ in ten]
    return ten, v
def a9_tong(rng):
    ten, v = _du_lieu(rng); s = ", ".join(f"{a}: {b} bạn" for a, b in zip(ten, v))
    return nint(rng, f"Kết quả khảo sát môn yêu thích của một nhóm học sinh: {s}. Số bạn tham gia khảo sát là:", sum(v), 1, (1, 2, 5), 0)
def a9_max(rng):
    ten, v = _du_lieu(rng)
    if v.count(max(v)) > 1: raise ValueError
    s = ", ".join(f"{a}: {b} bạn" for a, b in zip(ten, v))
    return M(f"Kết quả khảo sát môn yêu thích: {s}. Môn được nhiều bạn chọn nhất là:", ten[v.index(max(v))], [t for t in ten if t != ten[v.index(max(v))]], 1)
def a9_hon(rng):
    ten, v = _du_lieu(rng); s = ", ".join(f"{a}: {b} bạn" for a, b in zip(ten, v))
    if v[0] == v[1]: raise ValueError
    return nint(rng, f"Kết quả khảo sát môn yêu thích: {s}. Số bạn chọn {ten[0]} trừ số bạn chọn {ten[1]} bằng:", v[0] - v[1], 2, (1, 2, 3))
def a9_xs2(rng):
    ten, v = _du_lieu(rng); n = sum(v); i = rng.randrange(4); f = Fraction(v[i], n); s = ", ".join(f"{a}: {b}" for a, b in zip(ten, v))
    return M(f"Khảo sát {n} học sinh về môn thể thao yêu thích ({s}). Xác suất thực nghiệm để một bạn chọn ngẫu nhiên thích {ten[i]} (tối giản) là:", ps(f), nh_ps(rng, f), 3)
def a9_xs_tong(rng):
    n = rng.randint(3, 9) * 10; a = rng.randint(2, n // 4); b = rng.randint(2, n // 4); f = Fraction(a + b, n)
    return M(f"Gieo một xúc xắc {n} lần, có {a} lần được mặt 1 chấm và {b} lần được mặt 6 chấm. Xác suất thực nghiệm được mặt 1 chấm hoặc 6 chấm (tối giản) là:", ps(f), nh_ps(rng, f), 3)
def a9_mat(rng):
    n = rng.randint(4, 9) * 10; a = rng.randint(n // 4, n // 2); b = n - a
    return nint(rng, f"Tung một đồng xu {n} lần, được mặt sấp {a} lần. Số lần được mặt ngửa là:", b, 1, (1, 2, 5), 0)
def a9_cot(rng):
    ten, v = _du_lieu(rng); s = ", ".join(f"cột {a} cao {b} ô" for a, b in zip(ten, v))
    if v.count(min(v)) > 1: raise ValueError
    return M(f"Trong biểu đồ cột có: {s}. Cột thấp nhất là cột của:", ten[v.index(min(v))], [t for t in ten if t != ten[v.index(min(v))]], 1)

def b9_xs(rng):
    n = rng.randint(3, 9) * 10; a = rng.randint(n // 5, n // 2); f = Fraction(a, n)
    return T(f"Bạn Nam tung một đồng xu {n} lần, thấy mặt sấp xuất hiện {a} lần. Tính xác suất thực nghiệm của mặt sấp và mặt ngửa.", f"Mặt sấp: {pf(a, n)}\nMặt ngửa: {pf(n - a, n)}", 2)
def b9_bang(rng):
    ten, v = _du_lieu(rng); n = sum(v)
    return T("Bảng sau cho biết số bạn yêu thích mỗi môn: " + ", ".join(f"{a}: {b}" for a, b in zip(ten, v)) + ". Cho biết có bao nhiêu bạn được khảo sát, môn nào được yêu thích nhất và ít nhất.", f"Tổng: {n} bạn\nNhiều nhất: {ten[v.index(max(v))]} ({max(v)} bạn)\nÍt nhất: {ten[v.index(min(v))]} ({min(v)} bạn)", 1)
def b9_xs2(rng):
    ten, v = _du_lieu(rng); n = sum(v); i = rng.randrange(4)
    return T("Khảo sát môn thể thao yêu thích: " + ", ".join(f"{a}: {b}" for a, b in zip(ten, v)) + f". Tính xác suất thực nghiệm để một bạn chọn ngẫu nhiên thích {ten[i]}.", f"Tổng số bạn: {n}\nXác suất: {pf(v[i], n)}", 2)
def b9_ve(rng):
    ten, v = _du_lieu(rng)
    return T("Em hãy vẽ biểu đồ cột biểu diễn số liệu: " + ", ".join(f"{a}: {b}" for a, b in zip(ten, v)) + ".", "Vẽ trục ngang ghi tên môn, trục dọc ghi số bạn; mỗi môn vẽ một cột cao bằng số bạn tương ứng: " + ", ".join(f"{a} cao {b}" for a, b in zip(ten, v)) + ".", 2)
def b9_kq(rng):
    return T(rng.choice(["Liệt kê tất cả các kết quả có thể khi tung đồng thời hai đồng xu.", "Liệt kê các kết quả có thể khi gieo một xúc xắc 6 mặt."]), "Hai đồng xu: SS, SN, NS, NN (4 kết quả). Một xúc xắc: 1, 2, 3, 4, 5, 6 (6 kết quả).", 1)
def b9_xs3(rng):
    n = rng.randint(4, 9) * 10; a = rng.randint(3, n // 3); b = rng.randint(3, n // 3); c = n - a - b
    if c <= 0: raise ValueError
    return T(f"Lấy ngẫu nhiên một viên bi từ hộp {n} lần (có hoàn lại): {a} lần bi đỏ, {b} lần bi xanh, còn lại bi vàng. Tính xác suất thực nghiệm của mỗi màu.", f"Đỏ: {pf(a, n)}\nXanh: {pf(b, n)}\nVàng: {pf(c, n)}", 3)

CHU_DE = [
    ("Chương 1: Tập hợp và các phép tính với số tự nhiên", [a1_dem, a1_luythua, a1_nhan, a1_chia, a1_tt1, a1_tt2, a1_ngoac, a1_luythua_bt, a1_tt, a1_thuoc, a1_x, a1_chan], [b1_tinh, b1_x, b1_liet_ke, b1_luythua, b1_loi, b1_nhanh, b1_dem]),
    ("Chương 2: Tính chia hết trong tập số tự nhiên", [a2_ch, a2_khong, a2_chuso, a2_nto, a2_hop, a2_pttsnt, a2_ucln, a2_bcnn, a2_souoc, a2_uc, a2_chia_deu, a2_bcnn_loi], [b2_pt, b2_ucln, b2_chia, b2_dauhieu, b2_nto, b2_bcnn, b2_tonghieu]),
    ("Chương 3: Số nguyên", [a3_tang, a3_min, a3_doi, a3_gttd, a3_cong, a3_tru, a3_nhan, a3_chia, a3_bt, a3_x, a3_nhiet, a3_tong0, a3_ptu], [b3_tinh, b3_nhan, b3_x, b3_nhiet, b3_ss, b3_gt, b3_do_cao]),
    ("Chương 4: Một số hình phẳng trong thực tiễn", [a4_cv_hcn, a4_dt_hcn, a4_cv_vuong, a4_dt_vuong, a4_tg_deu, a4_luc_giac, a4_thoi, a4_binh_hanh, a4_cv_bh, a4_thang_can, a4_canh, a4_rong, a4_gach, a4_tc], [b4_hcn, b4_hv, b4_thoi, b4_bh, b4_gach, b4_tang, b4_tl]),
    ("Chương 5: Tính đối xứng của hình phẳng trong tự nhiên", [a5_truc, a5_tam, a5_co_tam, a5_nhieu_truc, a5_chu_truc, a5_chu_co, a5_ngoai, a5_ntruc], [b5_truc, b5_tam, b5_chu, b5_ve, b5_mc]),
    ("Chương 6: Phân số", [a6_rutgon, a6_ss, a6_cong, a6_tru, a6_nhan, a6_chia, a6_nghich, a6_cua, a6_tim_so, a6_bang, a6_tim_x, a6_lon_nhat, a6_hs, a6_sach], [b6_tinh, b6_x, b6_ss, b6_loi, b6_tim_so, b6_rutgon]),
    ("Chương 7: Số thập phân", [a7_cong, a7_tru, a7_nhan, a7_chia, a7_ss, a7_lt, a7_pt_cua, a7_ti_so, a7_tim_so, a7_giam, a7_ps_pt, a7_tp_pt], [b7_tinh, b7_x, b7_lt, b7_pt, b7_giam, b7_tiso, b7_tim]),
    ("Chương 8: Những hình học cơ bản (điểm, đường thẳng, đoạn thẳng, góc)", [a8_cong, a8_tru, a8_trung, a8_trung2, a8_doan, a8_duong, a8_loai, a8_ke_bu, a8_phu, a8_pg, a8_gocgoc, a8_n_tia], [b8_doan, b8_trung, b8_goc, b8_pg, b8_kebu, b8_so]),
    ("Chương 9: Dữ liệu và xác suất thực nghiệm", [a9_xs, a9_bong, a9_kq, a9_kq2, a9_kq3, a9_tong, a9_max, a9_hon, a9_xs2, a9_xs_tong, a9_mat, a9_cot], [b9_xs, b9_bang, b9_xs2, b9_ve, b9_kq, b9_xs3]),
]
