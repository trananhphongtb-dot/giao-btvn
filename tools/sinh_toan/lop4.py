from math import gcd
from core import *
from truyen import *

def nh_ps(rng, f):
    f = Fraction(f); n, d = f.numerator, f.denominator
    cand = [Fraction(n + 1, d), Fraction(max(n - 1, 1), d), Fraction(n, d + 1), Fraction(n, max(d - 1, 1)), Fraction(d, n) if n else f, Fraction(n + 2, d), Fraction(n, d + 2)]
    out = []
    for c in cand:
        if c != f and c > 0 and ps(c) not in [ps(x) for x in out] and (c.denominator != 1 or f.denominator == 1):
            out.append(c)
    if len(out) < 3: raise ValueError
    rng.shuffle(out)
    return [ps(x) for x in out[:3]]
def lcm(a, b): return a * b // gcd(a, b)
def rfrac(rng, lo=1, hi=9, rieng=True):
    while True:
        d = rng.randint(2, hi); n = rng.randint(lo, d - 1 if d > lo else d)
        if n < d and (not rieng or gcd(n, d) == 1): return Fraction(n, d)

# 1. Số tự nhiên lớn ----------------------------------------------------------------
def _so(rng, k, kc=True):
    while True:
        n = rng.randint(10 ** (k - 1), 10 ** k - 1)
        if not kc or len(set(str(n))) == k: return n
def tn_doc(rng):
    n = _so(rng, rng.randint(6, 8), False)
    return M(f"Số {fmt(n)} đọc là:", doc_so(n), chon3(rng, [doc_so(n + k) for k in (-1000, 1000, -100, 100, 10000, -10000, 1, -1)], doc_so(n)), 2)
def tn_gia_tri(rng):
    k = rng.randint(5, 8); n = _so(rng, k); st = str(n); i = rng.randrange(k)
    d = int(st[i])
    if d == 0: raise ValueError
    v = d * 10 ** (k - 1 - i)
    cand = [v * 10, v * 100, v * 1000, d]
    if v >= 10: cand.append(v // 10)
    if v >= 100: cand.append(v // 100)
    return M(f"Giá trị của chữ số {d} trong số {fmt(n)} là:", fmt(v), [fmt(x) for x in chon3(rng, cand, v)], 2)
def tn_tron(rng):
    n = rng.randint(100001, 9999999); hang = rng.choice([("nghìn", 1000), ("chục nghìn", 10000), ("trăm nghìn", 100000)])
    b = hang[1]; t = (n + b // 2) // b * b
    cand = [t + b, t - b, n // (b // 10) * (b // 10), t + 2 * b]
    return M(f"Làm tròn số {fmt(n)} đến hàng {hang[0]} được số:", fmt(t), [fmt(x) for x in chon3(rng, cand, t)], 3)
def tn_lon(rng):
    d = rng.sample(range(100000, 9999999), 4); m = max(d)
    return M(f"Số nào lớn nhất trong các số {', '.join(fmt(x) for x in d)}?", fmt(m), [fmt(x) for x in d if x != m], 2)
def tn_be(rng):
    d = rng.sample(range(100000, 9999999), 4); m = min(d)
    return M(f"Số nào bé nhất trong các số {', '.join(fmt(x) for x in d)}?", fmt(m), [fmt(x) for x in d if x != m], 2)
def tn_ghep(rng):
    a, b, c = rng.sample(range(1, 10), 3)
    n = a * 100000 + b * 10000 + c * 1000 + 5
    cand = [b * 100000 + a * 10000 + c * 1000 + 5, a * 100000 + c * 10000 + b * 1000 + 5, n + 45, n + 495, a * 10000 + b * 1000 + c * 100 + 5]
    return M(f"Số gồm {a} trăm nghìn, {b} chục nghìn, {c} nghìn và 5 đơn vị viết là:", fmt(n), [fmt(x) for x in chon3(rng, cand, n)], 2)
def tn_so_ch(rng):
    k = rng.randint(4, 8)
    return M(f"Số lớn nhất có {k} chữ số là:", fmt(10 ** k - 1), [fmt(10 ** k), fmt(10 ** (k - 1)), fmt(10 ** k - 10)], 1)
def tn_so_bn(rng):
    k = rng.randint(4, 8)
    return M(f"Số bé nhất có {k} chữ số là:", fmt(10 ** (k - 1)), [fmt(10 ** (k - 1) - 1), fmt(10 ** (k - 1) + 1), fmt(10 ** k)], 1)
def tn_so_sanh(rng):
    a, b = rng.sample(range(100000, 9999999), 2); d = ">" if a > b else "<"
    return M(f"Chọn dấu thích hợp: {fmt(a)} ... {fmt(b)}", d, sai_dau(d), 1)
def tn_hang_lop(rng):
    n = _so(rng, 7); s = str(n)
    ten, i = rng.choice([("hàng chục nghìn", 2), ("hàng trăm nghìn", 1), ("hàng nghìn", 3), ("hàng triệu", 0)])
    return M(f"Chữ số {ten} của số {fmt(n)} là chữ số nào?", s[i], chon3(rng, list(s), s[i]), 2)

def tl_doc_viet(rng):
    n = _so(rng, rng.randint(6, 8), False); m = _so(rng, 5, False)
    return T(f"Đọc các số: {fmt(n)}; {fmt(m)}.", f"{fmt(n)}: {doc_so(n)}\n{fmt(m)}: {doc_so(m)}", 2)
def tl_viet_so(rng):
    n = _so(rng, rng.randint(5, 7), False)
    return T(f"Viết số: \"{doc_so(n)}\".", f"{fmt(n)}", 2)
def tl_phan_tich(rng):
    n = _so(rng, rng.randint(5, 7)); s = str(n); k = len(s)
    return T(f"Viết số {fmt(n)} thành tổng (theo mẫu 4 305 = 4 000 + 300 + 5).", f"{fmt(n)} = " + " + ".join(f"{fmt(int(ch) * 10 ** (k - 1 - i))}" for i, ch in enumerate(s) if ch != "0"), 2)
def tl_sap_xep(rng):
    d = rng.sample(range(10000, 9999999), 5); bd = rng.choice(["bé đến lớn", "lớn đến bé"])
    return T(f"Sắp xếp các số {', '.join(fmt(x) for x in d)} theo thứ tự từ {bd}.", ", ".join(fmt(x) for x in sorted(d, reverse=bd == "lớn đến bé")), 1)
def tl_lam_tron(rng):
    d = [rng.randint(100001, 9999999) for _ in range(3)]; b = rng.choice([("nghìn", 1000), ("chục nghìn", 10000)])
    f = lambda n: (n + b[1] // 2) // b[1] * b[1]
    return T(f"Làm tròn các số sau đến hàng {b[0]}: {', '.join(fmt(x) for x in d)}.", "\n".join(f"{fmt(x)} ≈ {fmt(f(x))}" for x in d), 3)
def tl_gia_tri(rng):
    n = _so(rng, rng.randint(6, 7)); s = str(n); k = len(s)
    ds = [i for i in range(k) if s[i] != "0"][:2]
    return T(f"Trong số {fmt(n)}, nêu giá trị của chữ số {s[ds[0]]} và của chữ số {s[ds[1]]}.", "\n".join(f"Chữ số {s[i]} có giá trị {fmt(int(s[i]) * 10 ** (k - 1 - i))}" for i in ds), 2)

# 2. Bốn phép tính với số tự nhiên -------------------------------------------------------
def tn_cong(rng):
    a = rng.randint(10000, 600000); b = rng.randint(10000, 300000)
    return M(f"{fmt(a)} + {fmt(b)} = ?", fmt(a + b), [fmt(x) for x in so_gan(rng, a + b, 0, 10 ** 7, (1000, 100, 10))], 1)
def tn_tru(rng):
    a = rng.randint(200000, 900000); b = rng.randint(10000, a - 10000)
    return M(f"{fmt(a)} - {fmt(b)} = ?", fmt(a - b), [fmt(x) for x in so_gan(rng, a - b, 0, 10 ** 7, (1000, 100, 10))], 1)
def tn_nhan(rng):
    a = rng.randint(101, 999); b = rng.randint(11, 60)
    return M(f"{a} × {b} = ?", fmt(a * b), [fmt(x) for x in so_gan(rng, a * b, 0, 10 ** 6, (10, 100, 1000))], 2)
def tn_chia(rng):
    b = rng.randint(11, 60); q = rng.randint(21, 300)
    return M(f"{fmt(b * q)} : {b} = ?", fmt(q), [fmt(x) for x in so_gan(rng, q, 1, 1000, (1, 10, 2))], 2)
def tn_thuan_tien(rng):
    a, c = rng.choice([(25, 4), (5, 2), (125, 8), (50, 2), (20, 5)]); b = rng.randint(3, 19)
    return M(f"Tính bằng cách thuận tiện nhất: {a} × {b} × {c} = ?", fmt(a * b * c), [fmt(x) for x in so_gan(rng, a * b * c, 0, 10 ** 5, (a, c, b))], 3)
def tn_bt(rng):
    a = rng.randint(10, 99); b = rng.randint(2, 9); c = rng.randint(10, 99)
    return M(f"{a} × {b} + {c} = ?", a * b + c, so_gan(rng, a * b + c, 0, 2000, (10, 1, b)), 2)
def tn_x(rng):
    a = rng.randint(11, 99); x = rng.randint(11, 99)
    return M(f"Tìm x: x × {a} = {fmt(a * x)}", x, so_gan(rng, x, 1, 200, (1, 10, 2)), 3)
def tn_story(rng):
    a = rng.randint(120, 600); b = rng.randint(12, 40)
    return M(f"Mỗi ngày một xưởng làm được {a} sản phẩm. Hỏi trong {b} ngày xưởng làm được bao nhiêu sản phẩm?", fmt(a * b), [fmt(x) for x in so_gan(rng, a * b, 0, 10 ** 6, (10, 100, a))], 2)
def tn_story2(rng):
    b = rng.randint(12, 40); q = rng.randint(30, 200)
    return M(f"Có {fmt(b * q)} quyển vở chia đều cho {b} lớp. Mỗi lớp được bao nhiêu quyển vở?", fmt(q), [fmt(x) for x in so_gan(rng, q, 1, 1000, (1, 10, 2))], 2)

def tl_dat(rng):
    a = rng.randint(10000, 400000); b = rng.randint(10000, 300000); c = rng.randint(101, 999); d = rng.randint(11, 60)
    return T(f"Đặt tính rồi tính:\n{fmt(a)} + {fmt(b)}; {fmt(a + b)} - {fmt(b)}; {c} × {d}", f"{fmt(a)} + {fmt(b)} = {fmt(a + b)}; {fmt(a + b)} - {fmt(b)} = {fmt(a)}; {c} × {d} = {fmt(c * d)}", 1)
def tl_chia(rng):
    b = rng.randint(11, 60); q = rng.randint(31, 300); r = rng.randint(1, b - 1)
    return T(f"Đặt tính rồi tính: {fmt(b * q)} : {b} và {fmt(b * q + r)} : {b}", f"{fmt(b * q)} : {b} = {fmt(q)}\n{fmt(b * q + r)} : {b} = {fmt(q)} (dư {r})", 2)
def tl_thuan(rng):
    a, c = rng.choice([(25, 4), (5, 2), (125, 8), (50, 2), (20, 5)]); b = rng.randint(3, 19)
    return T(f"Tính bằng cách thuận tiện: {a} × {b} × {c}", f"{a} × {b} × {c} = ({a} × {c}) × {b} = {a * c} × {b} = {a * b * c}", 2)
def tl_thuan2(rng):
    a = rng.randint(2, 9) * 100 + rng.randint(1, 9) * 10; b = rng.randint(11, 99)
    return T(f"Tính bằng cách thuận tiện: {a} + {b} + {1000 - a}", f"{a} + {b} + {1000 - a} = ({a} + {1000 - a}) + {b} = 1000 + {b} = {1000 + b}", 3)
def tl_story(rng):
    a = rng.randint(120, 600); b = rng.randint(12, 40)
    return T(f"Mỗi ngày một xưởng may được {a} cái áo. Hỏi trong {b} ngày xưởng may được bao nhiêu cái áo?", giai("Số áo may được là:", f"{a} × {b}", fmt(a * b), "cái áo"), 2)
def tl_story2(rng):
    b = rng.randint(12, 40); q = rng.randint(30, 200)
    return T(f"Một kho có {fmt(b * q)} kg gạo, chia đều vào {b} bao. Hỏi mỗi bao có bao nhiêu ki-lô-gam gạo?", giai("Mỗi bao có số ki-lô-gam gạo là:", f"{fmt(b * q)} : {b}", fmt(q), "kg"), 2)
def tl_hon_hop(rng):
    a = rng.randint(20, 60); b = rng.randint(11, 30); c = rng.randint(100, 900)
    return T(f"Tính giá trị biểu thức: {a} × {b} + {c}", f"{a} × {b} = {a * b}; {a * b} + {c} = {a * b + c}", 2)

# 3. Trung bình cộng --------------------------------------------------------------------------
def _tbc(rng, n):
    m = rng.randint(10, 80)
    ds = [m + rng.randint(-8, 8) for _ in range(n - 1)]
    ds.append(m * n - sum(ds))
    if min(ds) < 1: raise ValueError
    return m, ds
def tn_tbc3(rng):
    m, ds = _tbc(rng, 3)
    return M(f"Trung bình cộng của các số {', '.join(map(str, ds))} là:", m, so_gan(rng, m, 1, 200, (1, 2, 3)), 1)
def tn_tbc2(rng):
    m, ds = _tbc(rng, 2)
    return M(f"Trung bình cộng của {ds[0]} và {ds[1]} là:", m, so_gan(rng, m, 1, 200, (1, 2, 3)), 1)
def tn_tbc4(rng):
    m, ds = _tbc(rng, 4)
    return M(f"Trung bình cộng của các số {', '.join(map(str, ds))} là:", m, so_gan(rng, m, 1, 200, (1, 2, 3)), 2)
def tn_tong_tu_tbc(rng):
    m, n = rng.randint(10, 60), rng.randint(3, 6)
    return M(f"Trung bình cộng của {n} số là {m}. Tổng của {n} số đó là:", m * n, so_gan(rng, m * n, 1, 500, (m, 1, n)), 2)
def tn_so_con_lai(rng):
    m, ds = _tbc(rng, 3)
    return M(f"Trung bình cộng của ba số là {m}. Hai trong ba số đó là {ds[0]} và {ds[1]}. Số thứ ba là:", ds[2], so_gan(rng, ds[2], 1, 300, (1, 2, 3)), 3)
def tn_tbc_story(rng):
    m, ds = _tbc(rng, 3); x = rng.sample(TEN, 3)
    return M(f"{x[0]} cân nặng {ds[0]} kg, {x[1]} cân nặng {ds[1]} kg, {x[2]} cân nặng {ds[2]} kg. Trung bình mỗi bạn cân nặng bao nhiêu ki-lô-gam?", f"{m} kg", [f"{x} kg" for x in so_gan(rng, m, 1, 200, (1, 2, 3))], 2)
def tn_tbc_lop(rng):
    m, ds = _tbc(rng, 4)
    return M(f"Bốn lớp trồng được số cây lần lượt là {', '.join(map(str, ds))}. Trung bình mỗi lớp trồng được bao nhiêu cây?", m, so_gan(rng, m, 1, 200, (1, 2, 3)), 2)
def tn_tbc_thoi(rng):
    a, b = rng.sample(range(5, 40), 2)
    if (a + b) % 2: raise ValueError
    return M(f"Một xe đi giờ đầu được {a} km, giờ sau được {b} km. Trung bình mỗi giờ xe đi được bao nhiêu ki-lô-mét?", f"{(a + b) // 2} km", [f"{x} km" for x in so_gan(rng, (a + b) // 2, 1, 100, (1, 2, 3))], 2)

def tl_tbc(rng):
    m, ds = _tbc(rng, rng.choice([3, 4]))
    return T(f"Tìm trung bình cộng của các số: {', '.join(map(str, ds))}.", f"Tổng các số: {' + '.join(map(str, ds))} = {sum(ds)}\nTrung bình cộng: {sum(ds)} : {len(ds)} = {m}", 1)
def tl_tbc_hs(rng):
    m, ds = _tbc(rng, 3)
    return T(f"Ba tổ thu gom giấy vụn được {ds[0]} kg, {ds[1]} kg và {ds[2]} kg. Hỏi trung bình mỗi tổ thu gom được bao nhiêu ki-lô-gam giấy vụn?", f"Bài giải\nTổng số ki-lô-gam giấy vụn: {ds[0]} + {ds[1]} + {ds[2]} = {sum(ds)} (kg)\nTrung bình mỗi tổ: {sum(ds)} : 3 = {m} (kg)\nĐáp số: {m} kg.", 2)
def tl_tim_so(rng):
    m, ds = _tbc(rng, 3)
    return T(f"Trung bình cộng của ba số là {m}. Biết hai số là {ds[0]} và {ds[1]}, tìm số thứ ba.", f"Tổng ba số: {m} × 3 = {m * 3}\nTổng hai số đã biết: {ds[0]} + {ds[1]} = {ds[0] + ds[1]}\nSố thứ ba: {m * 3} - {ds[0] + ds[1]} = {ds[2]}", 3)
def tl_thang(rng):
    m, ds = _tbc(rng, 4)
    return T(f"Bốn tháng đầu năm một cửa hàng bán được {', '.join(map(str, ds))} chiếc xe đạp. Hỏi trung bình mỗi tháng cửa hàng bán được bao nhiêu chiếc xe đạp?", f"Tổng số xe bán được: {' + '.join(map(str, ds))} = {sum(ds)} (chiếc)\nTrung bình mỗi tháng: {sum(ds)} : 4 = {m} (chiếc)", 2)
def tl_diem(rng):
    m = rng.randint(6, 9); a, b, c = [rng.randint(max(m - 2, 1), 10) for _ in range(3)]; d = 4 * m - a - b - c
    if not 0 <= d <= 10: raise ValueError
    return T(f"Bốn bài kiểm tra Toán của Nam được {a}, {b}, {c} và {d} điểm. Hỏi điểm trung bình bốn bài kiểm tra của Nam là bao nhiêu?", f"Tổng điểm: {a} + {b} + {c} + {d} = {4 * m}\nĐiểm trung bình: {4 * m} : 4 = {m}", 2)

# 4. Tổng và hiệu ----------------------------------------------------------------------------------
def _th(rng, lo=20, hi=200):
    lon = rng.randint(lo, hi); be = rng.randint(5, lon - 3)
    return lon + be, lon - be, lon, be
def tn_th_lon(rng):
    s, h, lon, be = _th(rng)
    return M(f"Hai số có tổng là {s}, hiệu là {h}. Số lớn là:", lon, so_gan(rng, lon, 1, 300, (1, 2, 10)), 1)
def tn_th_be(rng):
    s, h, lon, be = _th(rng)
    return M(f"Hai số có tổng là {s}, hiệu là {h}. Số bé là:", be, so_gan(rng, be, 1, 300, (1, 2, 10)), 1)
def tn_th_cthuc(rng):
    s, h, lon, be = _th(rng)
    return M(f"Biết tổng của hai số là {s} và hiệu của chúng là {h}. Cách tìm số lớn là:", f"({s} + {h}) : 2", [f"({s} - {h}) : 2", f"{s} - {h}", f"{s} : 2"], 2)
def tn_th_story(rng):
    s, h, lon, be = _th(rng, 20, 90); x, y = hai_ten(rng); v = vat(rng)
    return M(f"{x} và {y} có tất cả {s} {v}. {x} có nhiều hơn {y} {h} {v}. {x} có bao nhiêu {v}?", lon, so_gan(rng, lon, 1, 200, (1, 2, 10)), 2)
def tn_th_tuoi(rng):
    s, h, lon, be = _th(rng, 25, 40)
    return M(f"Tổng số tuổi của hai mẹ con là {s} tuổi, mẹ hơn con {h} tuổi. Con bao nhiêu tuổi?", f"{be} tuổi", [f"{x} tuổi" for x in so_gan(rng, be, 1, 80, (1, 2, 3))], 2)
def tn_th_hop(rng):
    s, h, lon, be = _th(rng, 20, 90)
    return M(f"Hai thùng dầu chứa tổng cộng {s} lít, thùng to hơn thùng nhỏ {h} lít. Thùng nhỏ chứa bao nhiêu lít?", f"{be} lít", [f"{x} lít" for x in so_gan(rng, be, 1, 200, (1, 2, 10))], 2)
def tn_th_kt(rng):
    s, h, lon, be = _th(rng)
    return M(f"Hai số có tổng là {s}, hiệu là {h}. Hãy chọn cặp số đúng:", f"{lon} và {be}", [f"{lon + 1} và {be - 1}" if be > 1 else f"{lon + 2} và {be}", f"{be} và {be}", f"{lon + 2} và {be + 2}"], 3)
def tn_th_chu_vi(rng):
    d, r = rng.randint(10, 60), rng.randint(5, 40)
    if r >= d: raise ValueError
    return M(f"Nửa chu vi hình chữ nhật là {d + r} m, chiều dài hơn chiều rộng {d - r} m. Chiều dài là:", f"{d} m", [f"{x} m" for x in so_gan(rng, d, 1, 200, (1, 2, 5))], 3)

def tl_th(rng):
    s, h, lon, be = _th(rng, 20, 100); x, y = hai_ten(rng); v = vat(rng)
    return T(f"{x} và {y} có tất cả {s} {v}. {x} có nhiều hơn {y} {h} {v}. Hỏi mỗi bạn có bao nhiêu {v}?", f"Bài giải\nSố {v} của {x} là: ({s} + {h}) : 2 = {lon} ({v})\nSố {v} của {y} là: {s} - {lon} = {be} ({v})\nĐáp số: {x} {lon} {v}; {y} {be} {v}.", 2)
def tl_th2(rng):
    s, h, lon, be = _th(rng, 20, 100)
    return T(f"Tìm hai số, biết tổng của chúng bằng {s} và hiệu của chúng bằng {h}.", f"Số lớn: ({s} + {h}) : 2 = {lon}\nSố bé: ({s} - {h}) : 2 = {be} (hoặc {s} - {lon} = {be})\nĐáp số: {lon} và {be}.", 1)
def tl_th_tuoi(rng):
    s, h, lon, be = _th(rng, 25, 45)
    return T(f"Tổng số tuổi của hai bố con là {s} tuổi. Bố hơn con {h} tuổi. Tính tuổi của mỗi người.", f"Tuổi bố: ({s} + {h}) : 2 = {lon} (tuổi)\nTuổi con: {s} - {lon} = {be} (tuổi)\nĐáp số: Bố {lon} tuổi; con {be} tuổi.", 2)
def tl_th_vuon(rng):
    d, r = rng.randint(15, 80), rng.randint(5, 40)
    if r >= d: raise ValueError
    return T(f"Một mảnh vườn hình chữ nhật có nửa chu vi là {d + r} m, chiều dài hơn chiều rộng {d - r} m. Tính chiều dài, chiều rộng và diện tích mảnh vườn.",
             f"Chiều dài: ({d + r} + {d - r}) : 2 = {d} (m)\nChiều rộng: {d + r} - {d} = {r} (m)\nDiện tích: {d} × {r} = {d * r} (m²)\nĐáp số: {d} m; {r} m; {d * r} m².", 3)
def tl_th_lop(rng):
    s, h, lon, be = _th(rng, 20, 60)
    return T(f"Hai lớp 4A và 4B có tất cả {s} học sinh. Lớp 4A nhiều hơn lớp 4B {h} học sinh. Hỏi mỗi lớp có bao nhiêu học sinh?", f"Số học sinh lớp 4A: ({s} + {h}) : 2 = {lon} (học sinh)\nSố học sinh lớp 4B: {s} - {lon} = {be} (học sinh)\nĐáp số: 4A {lon} học sinh; 4B {be} học sinh.", 2)

# 5. Tổng (hiệu) và tỉ số -----------------------------------------------------------------------------
_TI = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5), (3, 5), (1, 5), (4, 5)]
def _tong_ti(rng):
    p, q = rng.choice(_TI); k = rng.randint(3, 20); return p, q, k, k * (p + q)
def tn_ti_tong_be(rng):
    p, q, k, s = _tong_ti(rng)
    return M(f"Tổng của hai số là {s}. Tỉ số của hai số là {p}/{q}. Số bé là:", p * k, so_gan(rng, p * k, 1, 300, (1, k, 2)), 2)
def tn_ti_tong_lon(rng):
    p, q, k, s = _tong_ti(rng)
    return M(f"Tổng của hai số là {s}. Tỉ số của số bé và số lớn là {p}/{q}. Số lớn là:", q * k, so_gan(rng, q * k, 1, 300, (1, k, 2)), 2)
def tn_ti_phan(rng):
    p, q, k, s = _tong_ti(rng)
    return M(f"Tổng của hai số là {s}, số bé bằng {p}/{q} số lớn. Tổng số phần bằng nhau là:", p + q, so_gan(rng, p + q, 2, 20, (1, 2)), 1)
def tn_ti_hieu_lon(rng):
    p, q = rng.choice(_TI); k = rng.randint(3, 20); h = k * (q - p)
    return M(f"Hiệu của hai số là {h}. Tỉ số của số bé và số lớn là {p}/{q}. Số lớn là:", q * k, so_gan(rng, q * k, 1, 300, (1, k, 2)), 3)
def tn_ti_hieu_be(rng):
    p, q = rng.choice(_TI); k = rng.randint(3, 20); h = k * (q - p)
    return M(f"Hiệu của hai số là {h}. Tỉ số của số bé và số lớn là {p}/{q}. Số bé là:", p * k, so_gan(rng, p * k, 1, 300, (1, k, 2)), 3)
def tn_ti_so(rng):
    a, b = rng.choice([(3, 5), (2, 7), (4, 9), (5, 8), (3, 7), (2, 9), (5, 6)]); 
    return M(f"Tỉ số của {a} và {b} là:", f"{a}/{b}", [f"{b}/{a}", f"{a + b}/{b}", f"{a}/{a + b}"], 1)
def tn_ti_story(rng):
    p, q, k, s = _tong_ti(rng); x, y = hai_ten(rng)
    return M(f"{x} và {y} có tất cả {s} viên bi. Số bi của {x} bằng {p}/{q} số bi của {y}. {y} có bao nhiêu viên bi?", q * k, so_gan(rng, q * k, 1, 300, (1, k, 2)), 2)
def tn_ti_vuon(rng):
    p, q, k, s = _tong_ti(rng)
    return M(f"Một đội có {s} người, số nữ bằng {p}/{q} số nam. Số nam là:", q * k, so_gan(rng, q * k, 1, 300, (1, k, 2)), 3)

def tl_ti_tong(rng):
    p, q, k, s = _tong_ti(rng); x, y = hai_ten(rng)
    return T(f"Hai số có tổng là {s}. Số thứ nhất bằng {p}/{q} số thứ hai. Tìm hai số đó.", f"Bài giải\nTổng số phần bằng nhau: {p} + {q} = {p + q} (phần)\nGiá trị một phần: {s} : {p + q} = {k}\nSố thứ nhất: {k} × {p} = {k * p}\nSố thứ hai: {k} × {q} = {k * q}\nĐáp số: {k * p} và {k * q}.", 2)
def tl_ti_hieu(rng):
    p, q = rng.choice(_TI); k = rng.randint(3, 15); h = k * (q - p)
    return T(f"Hai số có hiệu là {h}. Số bé bằng {p}/{q} số lớn. Tìm hai số đó.", f"Bài giải\nHiệu số phần bằng nhau: {q} - {p} = {q - p} (phần)\nGiá trị một phần: {h} : {q - p} = {k}\nSố bé: {k} × {p} = {k * p}\nSố lớn: {k} × {q} = {k * q}\nĐáp số: {k * p} và {k * q}.", 3)
def tl_ti_vuon(rng):
    p, q, k, s = _tong_ti(rng)
    return T(f"Tổng của hai chiều dài hai tấm vải là {s} m. Tấm thứ nhất bằng {p}/{q} tấm thứ hai. Hỏi mỗi tấm vải dài bao nhiêu mét?", f"Tổng số phần: {p} + {q} = {p + q}\nMột phần: {s} : {p + q} = {k} (m)\nTấm thứ nhất: {k} × {p} = {k * p} (m)\nTấm thứ hai: {k} × {q} = {k * q} (m)", 2)
def tl_ti_tuoi(rng):
    p, q = rng.choice([(1, 3), (1, 4), (2, 5), (1, 5)]); k = rng.randint(3, 12); h = k * (q - p)
    return T(f"Mẹ hơn con {h} tuổi. Tuổi con bằng {p}/{q} tuổi mẹ. Tính tuổi của mỗi người.", f"Hiệu số phần: {q} - {p} = {q - p}\nMột phần: {h} : {q - p} = {k}\nTuổi con: {k} × {p} = {k * p}\nTuổi mẹ: {k} × {q} = {k * q}\nĐáp số: con {k * p} tuổi; mẹ {k * q} tuổi.", 3)
def tl_ti_so(rng):
    ds = [rng.choice([(3, 5), (2, 7), (4, 9), (5, 8), (3, 7), (2, 9), (5, 6), (4, 7)]) for _ in range(3)]
    return T("Viết tỉ số của:\n" + "; ".join(f"{a} và {b}" for a, b in ds), "; ".join(f"{a} và {b}: {a}/{b}" for a, b in ds), 1)

# 6. Phân số: rút gọn, quy đồng, so sánh ----------------------------------------------------------------
def tn_rg(rng):
    g = rng.randint(2, 6); f = rfrac(rng, 1, 8); a, b = f.numerator * g, f.denominator * g
    return M(f"Rút gọn phân số {a}/{b} được phân số tối giản:", ps(f), nh_ps(rng, f), 1)
def tn_bang(rng):
    f = rfrac(rng, 1, 8); k = rng.randint(2, 5)
    return M(f"Phân số nào bằng phân số {ps(f)}?", f"{f.numerator * k}/{f.denominator * k}", [f"{f.numerator * k + 1}/{f.denominator * k}", f"{f.numerator * k}/{f.denominator * k + 1}", f"{f.numerator + k}/{f.denominator + k}"], 2)
def tn_ss(rng):
    a, b = rfrac(rng, 1, 9, False), rfrac(rng, 1, 9, False)
    if a == b: raise ValueError
    d = ">" if a > b else "<"
    return M(f"Chọn dấu thích hợp: {ps(a)} ... {ps(b)}", d, sai_dau(d), 2)
def tn_lon_nhat(rng):
    ds = []
    while len(ds) < 4:
        f = rfrac(rng, 1, 12, False)
        if f not in ds: ds.append(f)
    m = max(ds)
    return M(f"Phân số nào lớn nhất trong các phân số {', '.join(ps(x) for x in ds)}?", ps(m), [ps(x) for x in ds if x != m], 3)
def tn_be_nhat(rng):
    ds = []
    while len(ds) < 4:
        f = rfrac(rng, 1, 12, False)
        if f not in ds: ds.append(f)
    m = min(ds)
    return M(f"Phân số nào bé nhất trong các phân số {', '.join(ps(x) for x in ds)}?", ps(m), [ps(x) for x in ds if x != m], 3)
def tn_qd(rng):
    b, d = rng.sample([2, 3, 4, 5, 6, 8, 9, 10, 12], 2); a = rng.randint(1, b - 1); c = rng.randint(1, d - 1)
    L = lcm(b, d); x, y = a * (L // b), c * (L // d)
    dung = f"{x}/{L} và {y}/{L}"
    cand = [f"{x + 1}/{L} và {y}/{L}", f"{x}/{L} và {y + 1}/{L}", f"{a * d}/{b * d} và {c * b}/{b * d}", f"{a}/{L} và {c}/{L}", f"{x}/{L + 1} và {y}/{L + 1}"]
    return M(f"Quy đồng mẫu số hai phân số {a}/{b} và {c}/{d} (mẫu số chung nhỏ nhất) được:", dung, chon3(rng, cand, dung), 3)
def tn_toi_gian(rng):
    f = rfrac(rng, 1, 12, True); ks = rng.sample([2, 3, 4, 5], 3)
    return M("Phân số nào dưới đây là phân số tối giản?", ps(f), [f"{f.numerator * x}/{f.denominator * x}" for x in ks], 2)
def tn_ss1(rng):
    d = rng.randint(3, 9); a = rng.randint(1, d - 1); b = d + rng.randint(1, 4)
    return M(f"Phân số nào lớn hơn 1?", f"{b}/{d}", [f"{a}/{d}", f"{a}/{b}", f"{d - 1}/{d}"], 1)
def tn_so_dau_ngoac(rng):
    d = rng.randint(3, 12); a, b = rng.sample(range(1, d), 2); dd = ">" if a > b else "<"
    return M(f"Chọn dấu thích hợp: {a}/{d} ... {b}/{d}", dd, sai_dau(dd), 1)
def tn_mau_chung(rng):
    b, d = rng.sample([2, 3, 4, 5, 6, 8, 9, 10, 12], 2); L = lcm(b, d)
    return M(f"Mẫu số chung nhỏ nhất của hai phân số có mẫu số {b} và {d} là:", L, chon3(rng, [b * d, b + d, max(b, d), L * 2, L + b], L), 3)
def tl_rg(rng):
    ls = []
    for _ in range(3):
        g = rng.randint(2, 6); f = rfrac(rng, 1, 8); ls.append((f.numerator * g, f.denominator * g, f))
    return T("Rút gọn các phân số: " + ", ".join(f"{a}/{b}" for a, b, _ in ls), "; ".join(f"{a}/{b} = {ps(f)}" for a, b, f in ls), 1)
def tl_qd(rng):
    b, d = rng.sample([2, 3, 4, 5, 6, 8, 9, 10, 12], 2); a = rng.randint(1, b - 1); c = rng.randint(1, d - 1); L = lcm(b, d)
    return T(f"Quy đồng mẫu số hai phân số {a}/{b} và {c}/{d}.", f"Mẫu số chung nhỏ nhất: {L}\n{a}/{b} = {a * (L // b)}/{L}\n{c}/{d} = {c * (L // d)}/{L}", 2)
def tl_ss(rng):
    cap = [(rfrac(rng, 1, 9, False), rfrac(rng, 1, 9, False)) for _ in range(3)]
    if any(a == b for a, b in cap): raise ValueError
    return T("So sánh các cặp phân số:\n" + "; ".join(f"{ps(a)} và {ps(b)}" for a, b in cap), "\n".join(f"{ps(a)} {'>' if a > b else '<'} {ps(b)}" for a, b in cap), 2)
def tl_sap_xep_ps(rng):
    ds = []
    while len(ds) < 4:
        f = rfrac(rng, 1, 12, False)
        if f not in ds: ds.append(f)
    return T(f"Sắp xếp các phân số {', '.join(ps(x) for x in ds)} theo thứ tự từ bé đến lớn.", ", ".join(ps(x) for x in sorted(ds)), 3)
def tl_bang(rng):
    f = rfrac(rng, 1, 8); k = rng.sample([2, 3, 4, 5], 3)
    return T(f"Viết ba phân số bằng phân số {ps(f)}.", "Nhân (hoặc chia) cả tử số và mẫu số với cùng một số khác 0, ví dụ: " + "; ".join(f"{ps(f)} = {f.numerator * x}/{f.denominator * x}" for x in k), 2)
def tl_toi_gian(rng):
    ds = [Fraction(rng.randint(2, 20), rng.randint(2, 20)) for _ in range(3)]
    return T(f"Rút gọn: {', '.join(f'{x.numerator * 3}/{x.denominator * 3}' for x in ds)}", "; ".join(f"{x.numerator * 3}/{x.denominator * 3} = {ps(x)}" for x in ds), 2)

# 7. Cộng, trừ, nhân, chia phân số --------------------------------------------------------------------------
def tn_cong_ps(rng):
    a, b = rfrac(rng, 1, 9, False), rfrac(rng, 1, 9, False); s = a + b
    return M(f"{ps(a)} + {ps(b)} = ?", ps(s), nh_ps(rng, s), 2)
def tn_cong_cmau(rng):
    d = rng.randint(3, 12); a, b = rng.randint(1, d - 1), rng.randint(1, d - 1); s = Fraction(a + b, d)
    return M(f"{a}/{d} + {b}/{d} = ?", ps(s), nh_ps(rng, s), 1)
def tn_tru_ps(rng):
    a, b = sorted([rfrac(rng, 1, 9, False), rfrac(rng, 1, 9, False)], reverse=True)
    if a == b: raise ValueError
    s = a - b
    return M(f"{ps(a)} - {ps(b)} = ?", ps(s), nh_ps(rng, s), 2)
def tn_nhan_ps(rng):
    a, b = rfrac(rng, 1, 9, False), rfrac(rng, 1, 9, False); s = a * b
    return M(f"{ps(a)} × {ps(b)} = ?", ps(s), nh_ps(rng, s), 2)
def tn_chia_ps(rng):
    a, b = rfrac(rng, 1, 9, False), rfrac(rng, 1, 9, False); s = a / b
    return M(f"{ps(a)} : {ps(b)} = ?", ps(s), nh_ps(rng, s), 3)
def tn_nhan_so(rng):
    a = rfrac(rng, 1, 9, False); k = rng.randint(2, 9); s = a * k
    return M(f"{ps(a)} × {k} = ?", ps(s), nh_ps(rng, s), 2)
def tn_phan_cua(rng):
    d = rng.randint(2, 9); n = rng.randint(1, d - 1); q = rng.randint(2, 12)
    return M(f"{n}/{d} của {d * q} là:", n * q, so_gan(rng, n * q, 1, 200, (1, q, 2)), 2)
def tn_story_doc(rng):
    a, b = rfrac(rng, 1, 8), rfrac(rng, 1, 8)
    if a + b >= 1: raise ValueError
    s = a + b
    return M(f"Ngày đầu Hà đọc được {ps(a)} cuốn truyện, ngày thứ hai đọc được {ps(b)} cuốn truyện. Cả hai ngày Hà đọc được bao nhiêu phần cuốn truyện?", ps(s), nh_ps(rng, s), 2)
def tn_story_con(rng):
    a = rfrac(rng, 1, 9)
    s = 1 - a
    return M(f"Một thùng nước đã dùng hết {ps(a)} thùng. Còn lại bao nhiêu phần thùng nước?", ps(s), nh_ps(rng, s), 2)

def tl_cong_tru(rng):
    a, b = sorted([rfrac(rng, 1, 9, False), rfrac(rng, 1, 9, False)], reverse=True)
    if a == b: raise ValueError
    return T(f"Tính: {ps(a)} + {ps(b)};  {ps(a)} - {ps(b)}", f"{ps(a)} + {ps(b)} = {ps(a + b)}\n{ps(a)} - {ps(b)} = {ps(a - b)}", 2)
def tl_nhan_chia(rng):
    a, b = rfrac(rng, 1, 9, False), rfrac(rng, 1, 9, False)
    return T(f"Tính: {ps(a)} × {ps(b)};  {ps(a)} : {ps(b)}", f"{ps(a)} × {ps(b)} = {ps(a * b)}\n{ps(a)} : {ps(b)} = {ps(a / b)}", 2)
def tl_story_ps(rng):
    a, b = rfrac(rng, 1, 8), rfrac(rng, 1, 8)
    if a + b >= 1: raise ValueError
    x = rng.choice(TEN)
    return T(f"{x} đọc sách: ngày đầu đọc được {ps(a)} cuốn sách, ngày thứ hai đọc được {ps(b)} cuốn sách. Hỏi sau hai ngày {x} đã đọc được bao nhiêu phần cuốn sách và còn lại bao nhiêu phần?", f"Đã đọc: {ps(a)} + {ps(b)} = {ps(a + b)} (cuốn sách)\nCòn lại: 1 - {ps(a + b)} = {ps(1 - a - b)} (cuốn sách)", 3)
def tl_vai(rng):
    d = rng.randint(2, 9); n = rng.randint(1, d - 1); q = rng.randint(3, 12)
    return T(f"Cửa hàng có {d * q} m vải, đã bán {n}/{d} số vải đó. Hỏi cửa hàng đã bán bao nhiêu mét vải? Còn lại bao nhiêu mét vải?", f"Số mét vải đã bán: {d * q} : {d} × {n} = {n * q} (m)\nSố mét vải còn lại: {d * q} - {n * q} = {(d - n) * q} (m)\nĐáp số: {n * q} m; {(d - n) * q} m.", 3)
def tl_hcn(rng):
    a, b = rfrac(rng, 1, 9, False), rfrac(rng, 1, 9, False)
    return T(f"Một hình chữ nhật có chiều dài {ps(a)} m, chiều rộng {ps(b)} m. Tính diện tích hình chữ nhật đó.", f"Diện tích: {ps(a)} × {ps(b)} = {ps(a * b)} (m²)", 2)
def tl_chia_do(rng):
    a = rfrac(rng, 1, 9, False); k = rng.randint(2, 6)
    return T(f"Có {ps(a)} lít nước mắm chia đều vào {k} chai. Hỏi mỗi chai có bao nhiêu lít nước mắm?", f"Mỗi chai có: {ps(a)} : {k} = {ps(a / k)} (lít)", 2)

# 8. Đổi đơn vị đo ----------------------------------------------------------------------------------------------
def roman(n):
    m = [(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]; s = ""
    for v, r in [(20, "XX")] + m:
        while n >= v: s += r; n -= v
    return s
def tn_yen(rng):
    a = rng.randint(2, 9); return M(f"{a} yến = ... kg", a * 10, [a * 100, a, a * 10 + 10], 1)
def tn_ta(rng):
    a = rng.randint(2, 9); return M(f"{a} tạ = ... kg", a * 100, [a * 10, a * 1000, a * 100 + 10], 1)
def tn_tan(rng):
    a = rng.randint(2, 9); return M(f"{a} tấn = ... kg", fmt(a * 1000), [fmt(a * 100), fmt(a * 10), fmt(a * 1000 + 100)], 1)
def tn_tan_ta(rng):
    a = rng.randint(2, 9); return M(f"{a} tấn = ... tạ", a * 10, [a * 100, a, a * 10 + 10], 2)
def tn_m2(rng):
    a = rng.randint(2, 9); return M(f"{a} m² = ... dm²", a * 100, [a * 10, a * 1000, a * 100 + 10], 2)
def tn_phut(rng):
    a = rng.randint(2, 9); return M(f"{a} phút = ... giây", a * 60, [a * 100, a * 30, a * 60 + 10], 1)
def tn_the_ki(rng):
    a = rng.randint(2, 9); return M(f"{a} thế kỉ = ... năm", a * 100, [a * 10, a * 1000, a * 100 + 10], 1)
def tn_nam_tk(rng):
    n = rng.choice([1945, 1954, 1975, 1802, 1930, 2000, 1010, 1789, 1288, 1428, 2024, 1400])
    tk = (n - 1) // 100 + 1
    sai = [roman(tk + d) for d in (1, -1, 2) if tk + d > 0]
    return M(f"Năm {n} thuộc thế kỉ nào?", roman(tk), sai, 3)
def tn_kg_tong(rng):
    a = rng.randint(1, 9); b = rng.randint(1, 9)
    return M(f"{a} tấn {b} tạ = ... kg", fmt(a * 1000 + b * 100), [fmt(a * 100 + b * 10), fmt(a * 1000 + b * 10), fmt(a * 100 + b * 100)], 3)
def tn_gio_phut(rng):
    a = rng.randint(1, 5); b = rng.choice([10, 15, 20, 30, 45])
    return M(f"{a} giờ {b} phút = ... phút", a * 60 + b, [a * 60 + b + 10, a * 100 + b, a + b], 3)
def tn_nhan_don_vi(rng):
    a = rng.randint(2, 9); b = rng.randint(2, 9)
    return M(f"Một xe chở {a} tạ gạo. {b} xe như vậy chở bao nhiêu ki-lô-gam gạo?", f"{fmt(a * b * 100)} kg", [f"{fmt(a * b * 10)} kg", f"{fmt(a * b * 1000)} kg", f"{fmt(a * b)} kg"], 3)

def tl_doi(rng):
    a, b, c, d = rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 9)
    return T(f"Điền số thích hợp vào chỗ chấm:\n{a} yến = ... kg; {b} tạ = ... kg; {c} tấn = ... kg; {d} m² = ... dm²",
             f"{a} yến = {a * 10} kg; {b} tạ = {b * 100} kg; {c} tấn = {fmt(c * 1000)} kg; {d} m² = {d * 100} dm²", 1)
def tl_thoi_gian(rng):
    a, b, c = rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 6)
    return T(f"Điền số thích hợp vào chỗ chấm:\n{a} phút = ... giây; {b} thế kỉ = ... năm; {c} giờ = ... phút", f"{a} phút = {a * 60} giây; {b} thế kỉ = {b * 100} năm; {c} giờ = {c * 60} phút", 1)
def tl_xe(rng):
    a = rng.randint(2, 9); b = rng.randint(2, 6)
    return T(f"Một xe tải chở {a} tạ gạo. Hỏi {b} xe như vậy chở được bao nhiêu ki-lô-gam gạo? Bằng bao nhiêu tạ, bao nhiêu tấn (nếu đổi được)?", f"Số tạ gạo chở được: {a} × {b} = {a * b} (tạ)\nĐổi: {a * b} tạ = {fmt(a * b * 100)} kg" + (f" = {a * b // 10} tấn" if a * b % 10 == 0 else f" = {Fraction(a * b, 10)} tấn"), 3)
def tl_nam(rng):
    ns = rng.sample([1945, 1954, 1975, 1802, 1930, 2000, 1010, 1789, 1288, 1428, 2024, 1400], 3)
    return T("Mỗi năm sau thuộc thế kỉ nào? " + ", ".join(map(str, ns)), "\n".join(f"Năm {n} thuộc thế kỉ {roman((n - 1) // 100 + 1)}" for n in ns), 3)
def tl_dt(rng):
    A = rng.randint(6, 40); k = rng.choice([2, 5, 10])
    n = A * 100 // (k * k)
    if (A * 100) % (k * k): raise ValueError
    return T(f"Một căn phòng hình chữ nhật có diện tích {A} m². Người ta lát nền bằng những viên gạch hình vuông cạnh {k} dm. Hỏi cần bao nhiêu viên gạch để lát kín nền phòng?", f"Đổi: {A} m² = {A * 100} dm²\nDiện tích một viên gạch: {k} × {k} = {k * k} (dm²)\nSố viên gạch cần: {A * 100} : {k * k} = {n} (viên)\nĐáp số: {n} viên gạch.", 3)
def tl_cap(rng):
    a = rng.randint(2, 9); b = rng.randint(1, 9)
    return T(f"Điền số thích hợp vào chỗ chấm: {a} tấn {b} tạ = ... kg", f"{a} tấn = {a * 1000} kg; {b} tạ = {b * 100} kg\nVậy {a} tấn {b} tạ = {a * 1000 + b * 100} kg", 2)

# 9. Dấu hiệu chia hết ------------------------------------------------------------------------------------------------
def _lay(rng, ok, k=4, lo=100, hi=9999):
    dung = None
    while dung is None:
        n = rng.randint(lo, hi)
        if ok(n): dung = n
    sai = []
    while len(sai) < k - 1:
        n = rng.randint(lo, hi)
        if not ok(n) and n not in sai: sai.append(n)
    return dung, sai
def tn_chia2(rng):
    d, s = _lay(rng, lambda n: n % 2 == 0)
    return M("Số nào dưới đây chia hết cho 2?", d, s, 1)
def tn_chia5(rng):
    d, s = _lay(rng, lambda n: n % 5 == 0)
    return M("Số nào dưới đây chia hết cho 5?", d, s, 1)
def tn_chia3(rng):
    d, s = _lay(rng, lambda n: n % 3 == 0)
    return M("Số nào dưới đây chia hết cho 3?", d, s, 2)
def tn_chia9(rng):
    d, s = _lay(rng, lambda n: n % 9 == 0)
    return M("Số nào dưới đây chia hết cho 9?", d, s, 2)
def tn_chia25(rng):
    d, s = _lay(rng, lambda n: n % 10 == 0)
    return M("Số nào dưới đây chia hết cho cả 2 và 5?", d, s, 2)
def tn_chia_3_ko9(rng):
    d, s = _lay(rng, lambda n: n % 3 == 0 and n % 9 != 0)
    return M("Số nào dưới đây chia hết cho 3 nhưng không chia hết cho 9?", d, s, 3)
def tn_ko_chia2(rng):
    return M("Số nào dưới đây không chia hết cho 2?", rng.choice([n for n in range(101, 9999) if n % 2]), [rng.randrange(100, 9999, 2) for _ in range(3)], 1)
def tn_dien_9(rng):
    a = rng.randint(1, 8); b = rng.randint(1, 8)
    if (a + b) % 9 == 0: raise ValueError
    x = (-(a + b)) % 9
    if x == 0: raise ValueError
    return M(f"Thay dấu * bằng chữ số thích hợp để số {a}*{b} chia hết cho 9:", x, chon3(rng, [i for i in range(10) if i != x and (a + b + i) % 9 != 0], x), 3)
def tn_dien_5(rng):
    a = rng.randint(1, 9); b = rng.randint(1, 9)
    if rng.random() < .5:
        return M(f"Thay dấu * bằng chữ số thích hợp để số {a}{b}* chia hết cho cả 2 và 5:", 0, [2, 5, 4], 2)
    return M(f"Thay dấu * bằng chữ số thích hợp để số {a}{b}* chia hết cho 5 nhưng không chia hết cho 2:", 5, [0, 2, 4], 3)

def tl_phan_loai(rng):
    ds = rng.sample(range(100, 2000), 6)
    cs = lambda n: [t for t, ok in (("2", n % 2 == 0), ("3", n % 3 == 0), ("5", n % 5 == 0), ("9", n % 9 == 0)) if ok]
    return T(f"Trong các số {', '.join(map(str, ds))}, số nào chia hết cho 2? chia hết cho 5? chia hết cho 3? chia hết cho 9?",
             "\n".join(f"{n}: " + (("chia hết cho " + ", ".join(cs(n))) if cs(n) else "không chia hết cho 2, 3, 5, 9") for n in ds), 2)
def tl_viet_so9(rng):
    a = rng.randint(1, 9); b = rng.randint(1, 9)
    k = rng.choice([("2", lambda n: n % 2 == 0), ("5", lambda n: n % 5 == 0), ("3", lambda n: n % 3 == 0), ("9", lambda n: n % 9 == 0)])
    ds = [n for n in range(100 * a + 10 * b, 100 * a + 10 * b + 10) if k[1](n)]
    if not ds: raise ValueError
    return T(f"Viết tất cả các số có ba chữ số dạng {a}{b}* (* là chữ số) chia hết cho {k[0]}.", ", ".join(map(str, ds)), 3)
def tl_dien_chu(rng):
    a = rng.randint(1, 8); b = rng.randint(1, 8)
    if (a + b) % 9 == 0: raise ValueError
    x = (-(a + b)) % 9
    return T(f"Tìm chữ số thích hợp thay dấu * để số {a}*{b} chia hết cho 9.", f"Tổng các chữ số: {a} + * + {b} = {a + b} + *\nĐể chia hết cho 9, {a + b} + * phải chia hết cho 9 nên * = {x}\nSố cần tìm: {a}{x}{b}", 3)
def tl_dung_sai(rng):
    n = rng.randint(100, 999); 
    cs = [("chia hết cho 2", n % 2 == 0), ("chia hết cho 5", n % 5 == 0), ("chia hết cho 3", n % 3 == 0), ("chia hết cho 9", n % 9 == 0)]
    return T(f"Số {n} có chia hết cho 2, 3, 5, 9 không? Giải thích bằng dấu hiệu chia hết.", f"Tổng các chữ số của {n} là {sum(map(int, str(n)))}; chữ số tận cùng là {n % 10}.\n" + "; ".join(f"{n} {'' if ok else 'không '}{t}" for t, ok in cs), 2)
def tl_so_nhom(rng):
    k = rng.choice([2, 5, 3, 9]); n = rng.randint(2, 4)
    return T(f"Viết {n} số có ba chữ số chia hết cho {k}.", f"Ví dụ: " + ", ".join(str(x) for x in rng.sample([m for m in range(100, 1000) if m % k == 0], n)), 1)

# 10. Hình bình hành, hình thoi -----------------------------------------------------------------------------------------------
def tn_dt_hbh(rng):
    a, h = rng.randint(5, 30), rng.randint(3, 20)
    return M(f"Hình bình hành có độ dài đáy {a} cm, chiều cao {h} cm. Diện tích hình bình hành là:", f"{a * h} cm²", [f"{x} cm²" for x in so_gan(rng, a * h, 1, 1000, (a, h, 1))], 1)
def tn_cv_hbh(rng):
    a, b = rng.randint(5, 30), rng.randint(3, 25)
    return M(f"Hình bình hành có hai cạnh liên tiếp dài {a} cm và {b} cm. Chu vi hình bình hành là:", f"{(a + b) * 2} cm", [f"{x} cm" for x in [a * b, a + b, (a + b) * 2 + 2][:3]], 2)
def tn_dt_thoi(rng):
    m, n = rng.randint(4, 30), rng.randint(4, 30)
    if m * n % 2: raise ValueError
    return M(f"Hình thoi có độ dài hai đường chéo là {m} cm và {n} cm. Diện tích hình thoi là:", f"{m * n // 2} cm²", [f"{x} cm²" for x in [m * n, m + n, m * n // 2 + m][:3]], 2)
def tn_cv_thoi(rng):
    a = rng.randint(3, 30)
    return M(f"Hình thoi có cạnh dài {a} cm. Chu vi hình thoi là:", f"{4 * a} cm", [f"{x} cm" for x in [2 * a, a * a, a + 4]], 1)
def tn_cao_hbh(rng):
    a, h = rng.randint(5, 30), rng.randint(3, 20)
    return M(f"Hình bình hành có diện tích {a * h} cm², độ dài đáy {a} cm. Chiều cao là:", f"{h} cm", [f"{x} cm" for x in so_gan(rng, h, 1, 100, (1, 2, 3))], 3)
def tn_canh_thoi(rng):
    a = rng.randint(3, 30)
    return M(f"Hình thoi có chu vi {4 * a} cm. Cạnh của hình thoi dài:", f"{a} cm", [f"{x} cm" for x in so_gan(rng, a, 1, 100, (1, 2, 4))], 2)
def tn_tinh_chat(rng):
    return M("Hình thoi có đặc điểm nào sau đây?", "Bốn cạnh bằng nhau", ["Chỉ có hai cạnh bằng nhau", "Bốn góc đều là góc vuông", "Chỉ có một cặp cạnh song song"], 1)
def tn_dt_hbh_m(rng):
    a, h = rng.randint(5, 40), rng.randint(3, 25)
    return M(f"Một mảnh đất hình bình hành có độ dài đáy {a} m, chiều cao {h} m. Diện tích mảnh đất là:", f"{a * h} m²", [f"{x} m²" for x in so_gan(rng, a * h, 1, 1500, (a, h, 1))], 2)
def tn_dt_thoi_m(rng):
    m, n = rng.randint(4, 30), rng.randint(4, 30)
    if m * n % 2: raise ValueError
    return M(f"Một miếng bìa hình thoi có hai đường chéo dài {m} dm và {n} dm. Diện tích miếng bìa là:", f"{m * n // 2} dm²", [f"{x} dm²" for x in [m * n, m + n, m * n // 2 + n]], 3)

def tl_dt_hbh(rng):
    a, h = rng.randint(5, 30), rng.randint(3, 20)
    return T(f"Một hình bình hành có độ dài đáy {a} cm, chiều cao {h} cm. Tính diện tích hình bình hành đó.", f"Diện tích: {a} × {h} = {a * h} (cm²)\nĐáp số: {a * h} cm².", 1)
def tl_dt_thoi(rng):
    m, n = rng.randint(4, 30), rng.randint(4, 30)
    if m * n % 2: raise ValueError
    return T(f"Một hình thoi có độ dài hai đường chéo là {m} cm và {n} cm. Tính diện tích hình thoi đó.", f"Diện tích: ({m} × {n}) : 2 = {m * n // 2} (cm²)\nĐáp số: {m * n // 2} cm².", 2)
def tl_cv_hbh(rng):
    a, b = rng.randint(5, 30), rng.randint(3, 25)
    return T(f"Một hình bình hành có hai cạnh liên tiếp dài {a} cm và {b} cm. Tính chu vi hình bình hành.", f"Chu vi: ({a} + {b}) × 2 = {(a + b) * 2} (cm)", 1)
def tl_dat_hbh(rng):
    a, h = rng.randint(8, 40), rng.randint(5, 25)
    return T(f"Một thửa ruộng hình bình hành có độ dài đáy {a} m, chiều cao bằng {h} m. Biết cứ mỗi mét vuông thu hoạch được 2 kg thóc, hỏi cả thửa ruộng thu hoạch được bao nhiêu ki-lô-gam thóc?", f"Diện tích thửa ruộng: {a} × {h} = {a * h} (m²)\nSố ki-lô-gam thóc: {a * h} × 2 = {a * h * 2} (kg)\nĐáp số: {a * h * 2} kg.", 3)
def tl_cao_hbh(rng):
    a, h = rng.randint(5, 30), rng.randint(3, 20)
    return T(f"Một hình bình hành có diện tích {a * h} cm² và độ dài đáy {a} cm. Tính chiều cao của hình bình hành.", f"Chiều cao: {a * h} : {a} = {h} (cm)", 3)
def tl_canh_thoi(rng):
    a = rng.randint(3, 25); m, n = rng.randint(4, 24), rng.randint(4, 24)
    if m * n % 2: raise ValueError
    return T(f"Hình thoi có chu vi {4 * a} cm. Tính độ dài cạnh hình thoi. Biết hình thoi khác có hai đường chéo {m} cm và {n} cm, tính diện tích hình thoi đó.", f"Cạnh hình thoi: {4 * a} : 4 = {a} (cm)\nDiện tích hình thoi còn lại: ({m} × {n}) : 2 = {m * n // 2} (cm²)", 3)

CHU_DE = [
    ("Số tự nhiên lớn: đọc, viết, so sánh, làm tròn", [tn_doc, tn_gia_tri, tn_tron, tn_lon, tn_be, tn_so_ch, tn_so_bn, tn_so_sanh, tn_hang_lop],
     [tl_doc_viet, tl_viet_so, tl_phan_tich, tl_sap_xep, tl_lam_tron, tl_gia_tri]),
    ("Bốn phép tính với số tự nhiên", [tn_cong, tn_tru, tn_nhan, tn_chia, tn_thuan_tien, tn_bt, tn_x, tn_story, tn_story2],
     [tl_dat, tl_chia, tl_thuan, tl_thuan2, tl_story, tl_story2, tl_hon_hop]),
    ("Trung bình cộng", [tn_tbc3, tn_tbc2, tn_tbc4, tn_tong_tu_tbc, tn_so_con_lai, tn_tbc_story, tn_tbc_lop, tn_tbc_thoi],
     [tl_tbc, tl_tbc_hs, tl_tim_so, tl_thang]),
    ("Tìm hai số khi biết tổng và hiệu", [tn_th_lon, tn_th_be, tn_th_cthuc, tn_th_story, tn_th_tuoi, tn_th_hop, tn_th_kt, tn_th_chu_vi],
     [tl_th, tl_th2, tl_th_tuoi, tl_th_vuon, tl_th_lop]),
    ("Tìm hai số khi biết tổng (hoặc hiệu) và tỉ số", [tn_ti_tong_be, tn_ti_tong_lon, tn_ti_phan, tn_ti_hieu_lon, tn_ti_hieu_be, tn_ti_so, tn_ti_story, tn_ti_vuon],
     [tl_ti_tong, tl_ti_hieu, tl_ti_vuon, tl_ti_tuoi, tl_ti_so]),
    ("Phân số: rút gọn, quy đồng, so sánh", [tn_rg, tn_bang, tn_ss, tn_lon_nhat, tn_be_nhat, tn_qd, tn_ss1, tn_so_dau_ngoac, tn_mau_chung],
     [tl_rg, tl_qd, tl_ss, tl_sap_xep_ps, tl_bang, tl_toi_gian]),
    ("Cộng, trừ, nhân, chia phân số", [tn_cong_ps, tn_cong_cmau, tn_tru_ps, tn_nhan_ps, tn_chia_ps, tn_nhan_so, tn_phan_cua, tn_story_doc, tn_story_con],
     [tl_cong_tru, tl_nhan_chia, tl_story_ps, tl_vai, tl_hcn, tl_chia_do]),
    ("Đổi đơn vị đo: yến, tạ, tấn, dm², m², giây, thế kỉ", [tn_yen, tn_ta, tn_tan, tn_tan_ta, tn_m2, tn_phut, tn_the_ki, tn_nam_tk, tn_kg_tong, tn_gio_phut, tn_nhan_don_vi],
     [tl_doi, tl_thoi_gian, tl_xe, tl_nam, tl_cap]),
    ("Dấu hiệu chia hết cho 2, 3, 5, 9", [tn_chia2, tn_chia5, tn_chia3, tn_chia9, tn_chia25, tn_chia_3_ko9, tn_ko_chia2, tn_dien_9, tn_dien_5],
     [tl_phan_loai, tl_viet_so9, tl_dien_chu, tl_dung_sai, tl_so_nhom]),
    ("Hình bình hành, hình thoi", [tn_dt_hbh, tn_cv_hbh, tn_dt_thoi, tn_cv_thoi, tn_cao_hbh, tn_canh_thoi, tn_tinh_chat, tn_dt_hbh_m, tn_dt_thoi_m],
     [tl_dt_hbh, tl_dt_thoi, tl_cv_hbh, tl_dat_hbh, tl_cao_hbh, tl_canh_thoi]),
]
