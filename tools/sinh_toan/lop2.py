from core import *
from truyen import *

def _nho_cong(rng):
    while True:
        a = rng.randint(15, 89); b = rng.randint(11, 99 - a if 99 - a > 11 else 12)
        if a % 10 + b % 10 >= 10 and a + b <= 100: return a, b
def _nho_tru(rng):
    while True:
        a = rng.randint(21, 99); b = rng.randint(11, a - 1)
        if a % 10 < b % 10: return a, b

# 1. Cộng, trừ có nhớ trong phạm vi 100 ---------------------------------------
def tn_cong(rng):
    a, b = _nho_cong(rng)
    return M(f"{a} + {b} = ?", a + b, so_gan(rng, a + b, 0, 100, (10, 1, 2)), 1)
def tn_tru(rng):
    a, b = _nho_tru(rng)
    return M(f"{a} - {b} = ?", a - b, so_gan(rng, a - b, 0, 100, (10, 1, 2)), 1)
def tn_thieu_cong(rng):
    a, b = _nho_cong(rng)
    return M(f"{a} + ? = {a + b}", b, so_gan(rng, b, 0, 99, (10, 1, 2)), 2)
def tn_thieu_tru(rng):
    a, b = _nho_tru(rng)
    return M(f"? - {b} = {a - b}", a, so_gan(rng, a, 0, 100, (10, 1)), 2)
def tn_dung(rng):
    a, b = _nho_cong(rng)
    return M("Phép tính nào dưới đây đúng?", f"{a} + {b} = {a + b}", [f"{a} + {b} = {a + b - 10}", f"{a} + {b} = {a + b + 10}", f"{a} + {b} = {a + b + 1}"], 2)
def tn_dem(rng):
    a, b = _nho_cong(rng); v = vat(rng)
    return M(f"Có {a} {v}, mua thêm {b} {v}. Có tất cả bao nhiêu {v}?", a + b, so_gan(rng, a + b, 0, 100, (10, 1)), 2)
def tn_bot(rng):
    a, b = _nho_tru(rng); v = vat(rng)
    return M(f"Có {a} {v}, cho đi {b} {v}. Còn lại bao nhiêu {v}?", a - b, so_gan(rng, a - b, 0, 100, (10, 1)), 2)
def tn_ba_so(rng):
    a = rng.randint(10, 40); b = rng.randint(10, 40); c = rng.randint(5, 20)
    return M(f"{a} + {b} - {c} = ?", a + b - c, so_gan(rng, a + b - c, 0, 100, (10, 1, 2)), 3)

def tl_dat(rng):
    ps_ = []
    for _ in range(4):
        if rng.random() < .5:
            a, b = _nho_cong(rng); ps_.append((f"{a} + {b}", a + b))
        else:
            a, b = _nho_tru(rng); ps_.append((f"{a} - {b}", a - b))
    return T("Đặt tính rồi tính:\n" + "; ".join(p for p, _ in ps_), "; ".join(f"{p} = {r}" for p, r in ps_), 1)
def tl_them(rng): return de_them(rng, 15, 49)
def tl_hop(rng): return de_hop(rng, 15, 49)
def tl_bot(rng): return de_bot(rng, 11, 45)
def tl_nhieu(rng): return de_nhieu(rng, 15, 49, kho=2)
def tl_it(rng): return de_it(rng, 11, 45, kho=2)
def tl_ba(rng):
    a = rng.randint(10, 40); b = rng.randint(10, 40); c = rng.randint(5, 20)
    return T(f"Tính: {a} + {b} - {c}", f"{a} + {b} = {a + b}; {a + b} - {c} = {a + b - c}.\nVậy {a} + {b} - {c} = {a + b - c}", 2)

# 2. Bảng nhân 2, 3, 4, 5 -------------------------------------------------------
def tn_nhan(rng):
    a = rng.randint(2, 5); b = rng.randint(1, 10)
    return M(f"{a} × {b} = ?", a * b, so_gan(rng, a * b, 0, 60, (a, 1, 2)), 1)
def tn_thieu_nhan(rng):
    a = rng.randint(2, 5); b = rng.randint(2, 10)
    return M(f"{a} × ? = {a * b}", b, so_gan(rng, b, 1, 12, (1, 2)), 2)
def tn_tong_thanh_nhan(rng):
    a = rng.randint(2, 5); n = rng.randint(3, 6)
    dung = f"{a} × {n}"
    sai = [f"{a} × {n + 1}", f"{a + 1} × {n}", f"{a} + {n}"]
    return M(f"Phép nhân nào bằng tổng {' + '.join([str(a)] * n)}?", dung, sai, 2)
def tn_nhom(rng):
    a = rng.randint(2, 5); n = rng.randint(2, 9)
    ds = [("hộp", "bút chì"), ("đĩa", "quả cam"), ("túi", "cái kẹo"), ("bó", "bông hoa"), ("rổ", "quả trứng")]
    c, v = rng.choice(ds)
    return M(f"Mỗi {c} có {a} {v}. {n} {c} như vậy có tất cả bao nhiêu {v}?", a * n, so_gan(rng, a * n, 0, 60, (a, 1, 2)), 2)
def tn_nhan_dung(rng):
    a = rng.randint(2, 5); b = rng.randint(2, 10)
    return M("Phép tính nào dưới đây đúng?", f"{a} × {b} = {a * b}", [f"{a} × {b} = {a * b + a}", f"{a} × {b} = {a * b - a}", f"{a} × {b} = {a + b}"], 2)
def tn_day_so(rng):
    a = rng.randint(2, 5); s = rng.randint(1, 3)
    day = [a * (s + i) for i in range(4)]
    return M(f"Tìm số thích hợp: {', '.join(map(str, day))}, ?", a * (s + 4), so_gan(rng, a * (s + 4), 0, 80, (a, 1, 2)), 3)
def tn_nhan_cham(rng):
    a = rng.randint(2, 5); b = rng.randint(2, 9)
    return M(f"{a} × {b} - {a} = ?", a * b - a, so_gan(rng, a * b - a, 0, 60, (a, 1, 2)), 3)

def tl_nhan_tinh(rng):
    ps_ = rng.sample([(a, b) for a in range(2, 6) for b in range(1, 11)], 4)
    return T("Tính nhẩm:\n" + "; ".join(f"{a} × {b}" for a, b in ps_), "; ".join(f"{a} × {b} = {a * b}" for a, b in ps_), 1)
def tl_nhan_do(rng):
    a = rng.randint(2, 5); n = rng.randint(3, 9); x = rng.choice(TEN)
    c, v = rng.choice([("hộp", "bút chì"), ("đĩa", "quả cam"), ("túi", "cái kẹo"), ("bó", "bông hoa")])
    return T(f"{x} có {n} {c}, mỗi {c} có {a} {v}. Hỏi {x} có tất cả bao nhiêu {v}?",
             f"Bài giải\n{x} có tất cả số {v} là:\n{a} × {n} = {a * n} ({v})\nĐáp số: {a * n} {v}.", 2)
def tl_tong_nhan(rng):
    a = rng.randint(2, 5); n = rng.randint(3, 7)
    return T(f"Viết tổng sau thành phép nhân rồi tính: {' + '.join([str(a)] * n)}", f"{' + '.join([str(a)] * n)} = {a} × {n} = {a * n}", 1)
def tl_day(rng):
    a = rng.randint(2, 5); s = rng.randint(1, 3)
    day = [a * (s + i) for i in range(4)]
    return T(f"Viết tiếp 3 số vào dãy số: {', '.join(map(str, day))}, ...",
             f"Dãy số tăng dần, mỗi số hơn số liền trước {a} đơn vị.\nTiếp theo là: {a*(s+4)}, {a*(s+5)}, {a*(s+6)}", 2)
def tl_xe(rng):
    a = rng.choice([2, 4]); n = rng.randint(3, 9)
    ten = {2: ("xe đạp", "bánh xe"), 4: ("ô tô", "bánh xe")}[a]
    return T(f"Mỗi {ten[0]} có {a} {ten[1]}. Hỏi {n} {ten[0]} có tất cả bao nhiêu {ten[1]}?",
             f"Bài giải\n{n} {ten[0]} có tất cả số {ten[1]} là:\n{a} × {n} = {a * n} ({ten[1]})\nĐáp số: {a * n} {ten[1]}.", 2)

# 3. Bảng chia 2, 3, 4, 5 --------------------------------------------------------
def tn_chia(rng):
    a = rng.randint(2, 5); q = rng.randint(1, 10)
    return M(f"{a * q} : {a} = ?", q, so_gan(rng, q, 0, 12, (1, 2)), 1)
def tn_thieu_chia(rng):
    a = rng.randint(2, 5); q = rng.randint(2, 10)
    return M(f"? : {a} = {q}", a * q, so_gan(rng, a * q, 0, 60, (a, 1, 2)), 2)
def tn_chia_dung(rng):
    a = rng.randint(2, 5); q = rng.randint(2, 10)
    return M("Phép tính nào dưới đây đúng?", f"{a * q} : {a} = {q}", [f"{a * q} : {a} = {q + 1}", f"{a * q} : {a} = {q - 1}", f"{a * q} : {a} = {a * q - a}"], 2)
def tn_chia_deu(rng):
    a = rng.randint(2, 5); q = rng.randint(2, 9)
    c, v = rng.choice([("đĩa", "quả cam"), ("bạn", "cái kẹo"), ("hộp", "bút chì"), ("túi", "viên bi")])
    return M(f"Chia đều {a * q} {v} vào {a} {c}. Mỗi {c} có bao nhiêu {v}?", q, so_gan(rng, q, 1, 12, (1, 2)), 2)
def tn_chia_nhom(rng):
    a = rng.randint(2, 5); q = rng.randint(2, 9)
    c, v = rng.choice([("hộp", "bút chì"), ("túi", "quả cam"), ("bó", "bông hoa"), ("rổ", "quả trứng")])
    return M(f"Có {a * q} {v}, xếp mỗi {c} {a} {v}. Xếp được bao nhiêu {c}?", q, so_gan(rng, q, 1, 12, (1, 2)), 2)
def tn_nhan_chia(rng):
    a = rng.randint(2, 5); b = rng.randint(2, 9)
    return M(f"Từ phép nhân {a} × {b} = {a * b}, ta có phép chia nào đúng?", f"{a * b} : {a} = {b}",
             [f"{a * b} : {a * b} = {a}", f"{a} : {b} = {a * b}", f"{a * b} : {b + 1} = {a}"], 3)
def tn_chia_bot(rng):
    a = rng.randint(2, 5); q = rng.randint(2, 9); b = rng.randint(1, 9)
    return M(f"{a * q} : {a} + {b} = ?", q + b, so_gan(rng, q + b, 0, 30, (1, 2)), 3)

def tl_chia_tinh(rng):
    ps_ = []
    for _ in range(4):
        a = rng.randint(2, 5); q = rng.randint(1, 10); ps_.append((a * q, a, q))
    return T("Tính nhẩm:\n" + "; ".join(f"{x} : {a}" for x, a, _ in ps_), "; ".join(f"{x} : {a} = {q}" for x, a, q in ps_), 1)
def tl_chia_deu(rng):
    a = rng.randint(2, 5); q = rng.randint(3, 9); x = rng.choice(TEN)
    c, v = rng.choice([("đĩa", "quả cam"), ("bạn", "cái kẹo"), ("hộp", "bút chì"), ("túi", "viên bi")])
    return T(f"{x} có {a * q} {v}, chia đều vào {a} {c}. Hỏi mỗi {c} có bao nhiêu {v}?",
             f"Bài giải\nMỗi {c} có số {v} là:\n{a * q} : {a} = {q} ({v})\nĐáp số: {q} {v}.", 2)
def tl_chia_nhom(rng):
    a = rng.randint(2, 5); q = rng.randint(3, 9)
    c, v = rng.choice([("hộp", "bút chì"), ("túi", "quả cam"), ("bó", "bông hoa"), ("rổ", "quả trứng")])
    return T(f"Có {a * q} {v}, xếp vào các {c}, mỗi {c} {a} {v}. Hỏi xếp được bao nhiêu {c}?",
             f"Bài giải\nSố {c} xếp được là:\n{a * q} : {a} = {q} ({c})\nĐáp số: {q} {c}.", 2)
def tl_nhan_chia(rng):
    a = rng.randint(2, 5); b = rng.randint(2, 9)
    return T(f"Từ phép nhân {a} × {b} = {a * b}, hãy viết hai phép chia tương ứng.", f"{a * b} : {a} = {b}; {a * b} : {b} = {a}", 2)
def tl_thieu(rng):
    a = rng.randint(2, 5); q = rng.randint(2, 9)
    return T(f"Tìm số thích hợp: ... : {a} = {q}; {a} × ... = {a * q}", f"{a * q} : {a} = {q}; {a} × {q} = {a * q}", 2)

# 4. Các số đến 1000 -----------------------------------------------------------------
def _ba(rng):
    while True:
        n = rng.randint(101, 999)
        if n % 10 and n // 10 % 10: return n
def tn_doc(rng):
    n = _ba(rng)
    return M(f"Số {n} đọc là gì?", doc_so(n), chon3(rng, [doc_so(n + k) for k in (-10, 10, -1, 1, 100, -100)], doc_so(n)), 2)
def tn_viet(rng):
    n = _ba(rng)
    return M(f"Số \"{doc_so(n)}\" viết là?", n, [n + 10, n - 10, n + 100], 2)
def tn_tram_chuc_dv(rng):
    n = _ba(rng); t, c, d = n // 100, n // 10 % 10, n % 10
    return M(f"Số {n} gồm mấy trăm, mấy chục, mấy đơn vị?", f"{t} trăm {c} chục {d} đơn vị",
             [f"{c} trăm {t} chục {d} đơn vị", f"{t} trăm {d} chục {c} đơn vị", f"{d} trăm {c} chục {t} đơn vị"], 1)
def tn_chu_so_hang(rng):
    n = _ba(rng)
    h = rng.choice([("trăm", n // 100), ("chục", n // 10 % 10), ("đơn vị", n % 10)])
    return M(f"Chữ số hàng {h[0]} của số {n} là chữ số nào?", h[1], chon3(rng, [n // 100, n // 10 % 10, n % 10, (h[1] + 1) % 10, (h[1] + 2) % 10], h[1]), 1)
def tn_lien_ke(rng):
    n = rng.randint(100, 998)
    if rng.random() < .5:
        return M(f"Số liền sau của {n} là số nào?", n + 1, so_gan(rng, n + 1, 0, 1000, (1, 10, 100)), 1)
    return M(f"Số liền trước của {n} là số nào?", n - 1, so_gan(rng, n - 1, 0, 1000, (1, 10, 100)), 1)
def tn_lon_nhat(rng):
    d = rng.sample(range(100, 1000), 4); m = max(d)
    return M(f"Số nào lớn nhất trong các số {', '.join(map(str, d))}?", m, [x for x in d if x != m], 2)
def tn_tong_gia_tri(rng):
    t = rng.randint(1, 9); c = rng.randint(1, 9); d = rng.randint(1, 9)
    return M(f"{t * 100} + {c * 10} + {d} = ?", t * 100 + c * 10 + d, [t * 100 + d * 10 + c, c * 100 + t * 10 + d, t * 100 + c * 10 + d + 10], 2)
def tn_tron_tram(rng):
    k = rng.randint(1, 9) * 100
    return M("Số nào dưới đây là số tròn trăm?", k, [k + rng.randint(1, 9) * 10 + rng.randint(1, 9) for _ in range(3)], 1)
def tn_chia_khoang(rng):
    a, b = sorted(rng.sample(range(100, 1000), 2))
    if b - a < 6: raise ValueError
    x = rng.randint(a + 1, b - 1)
    return M(f"Số nào lớn hơn {a} và bé hơn {b}?", x, [a - 1, b + 1, a], 3)

def tl_phan_tich3(rng):
    d = [_ba(rng) for _ in range(3)]
    return T("Viết các số sau thành tổng của trăm, chục, đơn vị (theo mẫu 354 = 300 + 50 + 4): " + ", ".join(map(str, d)) + ".",
             "\n".join(f"{x} = {x // 100 * 100} + {x // 10 % 10 * 10} + {x % 10}" for x in d), 2)
def tl_doc3(rng):
    d = [_ba(rng) for _ in range(3)]
    return T("Viết các số sau bằng chữ: " + ", ".join(map(str, d)) + ".", "\n".join(f"{x}: {doc_so(x)}" for x in d), 2)
def tl_sap3(rng):
    d = rng.sample(range(100, 1000), 5); bd = rng.choice(["bé đến lớn", "lớn đến bé"])
    return T(f"Sắp xếp các số {', '.join(map(str, d))} theo thứ tự từ {bd}.", ", ".join(map(str, sorted(d, reverse=bd == "lớn đến bé"))), 1)
def tl_dau3(rng):
    cap = [rng.sample(range(100, 1000), 2) for _ in range(3)]
    return T("Điền dấu >, < thích hợp vào chỗ chấm:\n" + "; ".join(f"{a} ... {b}" for a, b in cap),
             "; ".join(f"{a} {'>' if a > b else '<'} {b}" for a, b in cap), 1)
def tl_lien_ke3(rng):
    d = [rng.randint(101, 998) for _ in range(3)]
    return T("Viết số liền trước và số liền sau của mỗi số: " + ", ".join(map(str, d)) + ".",
             "\n".join(f"Số liền trước của {x} là {x - 1}; số liền sau của {x} là {x + 1}." for x in d), 1)
def tl_dem_cach(rng):
    a = rng.randint(1, 8) * 100 + rng.randint(0, 5) * 10; k = rng.choice([10, 100])
    day = [a + k * i for i in range(4)]
    return T(f"Viết số thích hợp vào chỗ chấm: {', '.join(map(str, day))}, ..., ...", f"Đếm thêm {k} đơn vị: {a + 4 * k}, {a + 5 * k}", 2)

# 5. Cộng, trừ trong phạm vi 1000 ------------------------------------------------------
def tn_cong3(rng):
    a = rng.randint(120, 700); b = rng.randint(110, 999 - a)
    return M(f"{a} + {b} = ?", a + b, so_gan(rng, a + b, 0, 1000, (10, 100, 1)), 1)
def tn_tru3(rng):
    a = rng.randint(300, 999); b = rng.randint(110, a - 10)
    return M(f"{a} - {b} = ?", a - b, so_gan(rng, a - b, 0, 1000, (10, 100, 1)), 1)
def tn_cong_tron(rng):
    a = rng.randint(1, 5) * 100 + rng.randint(1, 9) * 10; b = rng.randint(1, 4) * 100 + rng.randint(1, 8) * 10
    return M(f"{a} + {b} = ?", a + b, so_gan(rng, a + b, 0, 1000, (10, 100)), 1)
def tn_thieu3(rng):
    a = rng.randint(120, 700); b = rng.randint(110, 999 - a)
    return M(f"{a} + ? = {a + b}", b, so_gan(rng, b, 0, 999, (10, 100, 1)), 2)
def tn_dem3(rng):
    a = rng.randint(120, 600); b = rng.randint(110, 380); v = rng.choice(["quyển sách", "cái bút", "quả cam", "viên gạch", "cây giống"])
    return M(f"Cửa hàng có {a} {v}, nhập thêm {b} {v}. Cửa hàng có tất cả bao nhiêu {v}?", a + b, so_gan(rng, a + b, 0, 1000, (10, 100, 1)), 2)
def tn_ban3(rng):
    a = rng.randint(400, 900); b = rng.randint(110, a - 100); v = rng.choice(["quyển sách", "cái bút", "quả cam", "viên gạch", "cây giống"])
    return M(f"Cửa hàng có {a} {v}, đã bán {b} {v}. Còn lại bao nhiêu {v}?", a - b, so_gan(rng, a - b, 0, 1000, (10, 100, 1)), 2)
def tn_so_pt3(rng):
    a = rng.randint(100, 400); b = rng.randint(100, 400); c = rng.randint(100, 400); d = rng.randint(100, 400)
    if a + b == c + d: raise ValueError
    d_ = ">" if a + b > c + d else "<"
    return M(f"Chọn dấu thích hợp: {a} + {b} ... {c} + {d}", d_, sai_dau(d_), 3)
def tn_ba3(rng):
    a = rng.randint(200, 500); b = rng.randint(100, 300); c = rng.randint(50, 150)
    return M(f"{a} + {b} - {c} = ?", a + b - c, so_gan(rng, a + b - c, 0, 1000, (10, 100, 1)), 3)

def tl_dat3(rng):
    ps_ = []
    for _ in range(4):
        if rng.random() < .5:
            a = rng.randint(120, 700); b = rng.randint(110, 999 - a); ps_.append((f"{a} + {b}", a + b))
        else:
            a = rng.randint(300, 999); b = rng.randint(110, a - 10); ps_.append((f"{a} - {b}", a - b))
    return T("Đặt tính rồi tính:\n" + "; ".join(p for p, _ in ps_), "; ".join(f"{p} = {r}" for p, r in ps_), 1)
def tl_them3(rng): return de_them(rng, 120, 480)
def tl_hop3(rng): return de_hop(rng, 120, 480)
def tl_bot3(rng): return de_bot(rng, 110, 400)
def tl_nhieu3(rng): return de_nhieu(rng, 120, 480, kho=2)
def tl_ba3(rng):
    a = rng.randint(200, 500); b = rng.randint(100, 300); c = rng.randint(50, 150)
    return T(f"Tính: {a} + {b} - {c}", f"{a} + {b} = {a + b}; {a + b} - {c} = {a + b - c}.\nVậy {a} + {b} - {c} = {a + b - c}", 2)

# 6. Đo lường -----------------------------------------------------------------------------
_DV = [("Chiều dài cây bút chì khoảng 15", "cm"), ("Chiều cao cánh cửa ra vào khoảng 2", "m"), ("Quãng đường từ nhà đến trường dài khoảng 2", "km"),
       ("Một con gà nặng khoảng 2", "kg"), ("Một can nước chứa khoảng 5", "lít"), ("Chiều dài sân trường khoảng 50", "m"),
       ("Quãng đường từ Thái Bình đến Hà Nội dài khoảng 110", "km"), ("Một bao gạo nặng 10", "kg"), ("Một bình nước chứa 2", "lít"),
       ("Chiều dài quyển vở khoảng 24", "cm")]
def tn_chon_dv(rng):
    q, dv = rng.choice(_DV)
    return M(f"Chọn đơn vị thích hợp: {q} ... ?", dv, rng.sample([x for x in ("cm", "dm", "m", "km", "kg", "lít") if x != dv], 3), 2)
def tn_doi_dm(rng):
    a = rng.randint(2, 9); return M(f"{a} m = ... dm", a * 10, [a * 100, a, a * 10 + 10], 2)
def tn_doi_cm(rng):
    a = rng.randint(2, 9); return M(f"{a} m = ... cm", a * 100, [a * 10, a * 1000, a * 100 + 10], 2)
def tn_doi_dm_cm(rng):
    a = rng.randint(2, 9); return M(f"{a} dm = ... cm", a * 10, [a, a * 100, a * 10 + 10], 1)
def tn_doi_km(rng):
    a = rng.randint(2, 9); return M(f"{a} km = ... m", a * 1000, [a * 100, a * 10, a * 10000], 2)
def tn_kg(rng):
    a = rng.randint(10, 50); b = rng.randint(5, 40); x, y = hai_ten(rng)
    return M(f"{x} cân nặng {a} kg, {y} cân nặng {b} kg. Hai bạn cân nặng tất cả bao nhiêu ki-lô-gam?", f"{a + b} kg", [f"{n} kg" for n in so_gan(rng, a + b, 1, 120, (1, 10, 2))], 2)
def tn_lit(rng):
    a = rng.randint(20, 60); b = rng.randint(5, a - 5)
    return M(f"Thùng có {a} lít nước, dùng hết {b} lít. Thùng còn lại bao nhiêu lít nước?", f"{a - b} lít", [f"{n} lít" for n in so_gan(rng, a - b, 1, 100, (1, 10, 2))], 2)
def tn_cm_dm(rng):
    a = rng.randint(2, 9)
    return M(f"Đoạn thẳng dài {a} dm. Đoạn thẳng đó dài bao nhiêu xăng-ti-mét?", f"{a * 10} cm", [f"{a} cm", f"{a * 100} cm", f"{a * 10 + 10} cm"], 3)
def tn_so_do(rng):
    a = rng.randint(2, 9); b = rng.randint(11, 90)
    dung = ">" if a * 10 > b else "<"
    if a * 10 == b: raise ValueError
    return M(f"Chọn dấu thích hợp: {a} dm ... {b} cm", dung, sai_dau(dung), 3)

def tl_doi(rng):
    a, b, c = rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 9)
    return T(f"Điền số thích hợp vào chỗ chấm:\n{a} m = ... dm; {b} dm = ... cm; {c} km = ... m",
             f"{a} m = {a * 10} dm; {b} dm = {b * 10} cm; {c} km = {c * 1000} m", 1)
def tl_kg(rng):
    a = rng.randint(10, 40); b = rng.randint(10, 40); c = rng.randint(5, 30)
    return T(f"Bao gạo thứ nhất nặng {a} kg, bao gạo thứ hai nặng {b} kg. Cả hai bao gạo nặng bao nhiêu ki-lô-gam? Nếu lấy ra {c} kg thì còn lại bao nhiêu ki-lô-gam?",
             f"Cả hai bao nặng: {a} + {b} = {a + b} (kg)\nCòn lại: {a + b} - {c} = {a + b - c} (kg)\nĐáp số: {a + b} kg; {a + b - c} kg.", 2)
def tl_lit(rng):
    a = rng.randint(8, 30); b = rng.randint(8, 30)
    return T(f"Thùng thứ nhất chứa {a} lít dầu, thùng thứ hai chứa {b} lít dầu. Hỏi cả hai thùng chứa bao nhiêu lít dầu?",
             giai("Cả hai thùng chứa số lít dầu là:", f"{a} + {b}", a + b, "lít"), 1)
def tl_day_dm(rng):
    a = rng.randint(2, 9); b = rng.randint(2, 9)
    return T(f"Sợi dây xanh dài {a} dm, sợi dây đỏ dài {b} dm. Hỏi hai sợi dây dài tất cả bao nhiêu xăng-ti-mét?",
             f"Hai sợi dây dài: {a} + {b} = {a + b} (dm)\nĐổi: {a + b} dm = {(a + b) * 10} cm\nĐáp số: {(a + b) * 10} cm.", 3)
def tl_chon(rng):
    cap = rng.sample(_DV, 3)
    return T("Chọn đơn vị đo thích hợp (cm, m, km, kg, lít):\n" + "\n".join(f"{q} ..." for q, _ in cap), "\n".join(f"{q} {dv}" for q, dv in cap), 2)

# 7. Chu vi tam giác, tứ giác ------------------------------------------------------------------
def tn_cv_tg(rng):
    a, b, c = rng.randint(3, 15), rng.randint(3, 15), rng.randint(3, 15)
    return M(f"Hình tam giác ABC có AB = {a} cm, BC = {b} cm, CA = {c} cm. Chu vi hình tam giác ABC là:", f"{a + b + c} cm", [f"{n} cm" for n in so_gan(rng, a + b + c, 3, 60, (1, 2, 3))], 1)
def tn_cv_tu(rng):
    a, b, c, d = [rng.randint(3, 15) for _ in range(4)]
    return M(f"Tứ giác MNPQ có các cạnh MN = {a} cm, NP = {b} cm, PQ = {c} cm, QM = {d} cm. Chu vi tứ giác MNPQ là:", f"{a + b + c + d} cm", [f"{n} cm" for n in so_gan(rng, a + b + c + d, 4, 80, (1, 2, 4))], 1)
def tn_cv_deu(rng):
    a = rng.randint(3, 15)
    return M(f"Hình tam giác có ba cạnh đều bằng {a} cm. Chu vi hình tam giác đó là:", f"{3 * a} cm", [f"{n} cm" for n in so_gan(rng, 3 * a, 3, 60, (1, 2, 3))], 2)
def tn_cv_thieu(rng):
    a, b, c = rng.randint(3, 15), rng.randint(3, 15), rng.randint(3, 15)
    return M(f"Chu vi hình tam giác là {a + b + c} cm, hai cạnh dài {a} cm và {b} cm. Cạnh còn lại dài:", f"{c} cm", [f"{n} cm" for n in so_gan(rng, c, 1, 60, (1, 2, 3))], 3)
def tn_cv_hv(rng):
    a = rng.randint(3, 15)
    return M(f"Hình tứ giác có bốn cạnh đều bằng {a} cm. Chu vi hình tứ giác đó là:", f"{4 * a} cm", [f"{n} cm" for n in so_gan(rng, 4 * a, 4, 80, (1, 2, 4))], 2)
def tn_cv_cach(rng):
    a, b, c = rng.randint(3, 15), rng.randint(3, 15), rng.randint(3, 15)
    return M(f"Cách tính chu vi hình tam giác có độ dài các cạnh {a} cm, {b} cm, {c} cm là:", f"{a} + {b} + {c}", [f"{a} × {b} × {c}", f"{a} + {b} - {c}", f"{a} × 3"], 2)
def tn_so_cv(rng):
    a, b, c = [rng.randint(3, 12) for _ in range(3)]; d, e, f = [rng.randint(3, 12) for _ in range(3)]
    if a + b + c == d + e + f: raise ValueError
    return M(f"Tam giác ABC có các cạnh {a} cm, {b} cm, {c} cm. Tam giác DEF có các cạnh {d} cm, {e} cm, {f} cm. Tam giác nào có chu vi lớn hơn?",
             "Tam giác ABC" if a + b + c > d + e + f else "Tam giác DEF", ["Tam giác DEF" if a + b + c > d + e + f else "Tam giác ABC", "Hai tam giác có chu vi bằng nhau", "Không so sánh được"], 3)

def tl_cv_tg(rng):
    a, b, c = rng.randint(3, 20), rng.randint(3, 20), rng.randint(3, 20)
    return T(f"Tính chu vi hình tam giác ABC có độ dài các cạnh AB = {a} cm, BC = {b} cm, CA = {c} cm.", f"Chu vi hình tam giác ABC là:\n{a} + {b} + {c} = {a + b + c} (cm)\nĐáp số: {a + b + c} cm.", 1)
def tl_cv_tu(rng):
    a, b, c, d = [rng.randint(3, 20) for _ in range(4)]
    return T(f"Tính chu vi tứ giác MNPQ có MN = {a} cm, NP = {b} cm, PQ = {c} cm, QM = {d} cm.", f"Chu vi tứ giác MNPQ là:\n{a} + {b} + {c} + {d} = {a + b + c + d} (cm)\nĐáp số: {a + b + c + d} cm.", 1)
def tl_cv_deu(rng):
    a = rng.randint(4, 20)
    return T(f"Một mảnh vườn hình tam giác có ba cạnh bằng nhau, mỗi cạnh dài {a} m. Tính chu vi mảnh vườn đó.", f"Chu vi mảnh vườn là:\n{a} + {a} + {a} = {3 * a} (m)\n(hoặc {a} × 3 = {3 * a} m)\nĐáp số: {3 * a} m.", 2)
def tl_canh_thieu(rng):
    a, b, c = rng.randint(4, 15), rng.randint(4, 15), rng.randint(4, 15)
    return T(f"Hình tam giác có chu vi {a + b + c} cm, hai cạnh dài {a} cm và {b} cm. Tính độ dài cạnh còn lại.", f"Tổng hai cạnh đã biết: {a} + {b} = {a + b} (cm)\nCạnh còn lại dài: {a + b + c} - {a + b} = {c} (cm)\nĐáp số: {c} cm.", 3)
def tl_rao(rng):
    a = rng.randint(5, 20); b = rng.randint(5, 20); c = rng.randint(5, 20)
    return T(f"Bác nông dân rào mảnh đất hình tam giác có các cạnh dài {a} m, {b} m, {c} m. Hỏi hàng rào dài bao nhiêu mét?", f"Hàng rào dài:\n{a} + {b} + {c} = {a + b + c} (m)\nĐáp số: {a + b + c} m.", 2)

# 8. Tìm số hạng, số bị trừ, số trừ... -----------------------------------------------------------
def tn_x_cong(rng):
    x = rng.randint(5, 60); a = rng.randint(5, 35)
    return M(f"Tìm x: x + {a} = {x + a}", x, so_gan(rng, x, 0, 100, (1, 10, 2)), 1)
def tn_x_cong2(rng):
    x = rng.randint(5, 60); a = rng.randint(5, 35)
    return M(f"Tìm x: {a} + x = {x + a}", x, so_gan(rng, x, 0, 100, (1, 10, 2)), 1)
def tn_x_tru(rng):
    x = rng.randint(20, 90); a = rng.randint(5, x - 5)
    return M(f"Tìm x: x - {a} = {x - a}", x, so_gan(rng, x, 0, 100, (1, 10, 2)), 2)
def tn_x_tru2(rng):
    a = rng.randint(30, 99); x = rng.randint(5, a - 5)
    return M(f"Tìm x: {a} - x = {a - x}", x, so_gan(rng, x, 0, 100, (1, 10, 2)), 2)
def tn_x_nhan(rng):
    a = rng.randint(2, 5); x = rng.randint(2, 10)
    return M(f"Tìm x: x × {a} = {a * x}", x, so_gan(rng, x, 1, 12, (1, 2)), 2)
def tn_x_chia(rng):
    a = rng.randint(2, 5); q = rng.randint(2, 10)
    return M(f"Tìm x: x : {a} = {q}", a * q, so_gan(rng, a * q, 0, 60, (a, 1, 2)), 3)
def tn_x_chia2(rng):
    a = rng.randint(2, 5); q = rng.randint(2, 10)
    return M(f"Tìm x: {a * q} : x = {q}", a, so_gan(rng, a, 1, 12, (1, 2)), 3)
def tn_x_tp(rng):
    x = rng.randint(5, 40); a = rng.randint(5, 30); b = rng.randint(5, 20)
    return M(f"Tìm x: x + {a} = {x + a + b}", x + b, so_gan(rng, x + b, 0, 100, (1, 10, 2)), 3)
def tn_ten_goi(rng):
    return M("Trong phép cộng 12 + 25 = 37, số 37 gọi là gì?", "Tổng", ["Số hạng", "Hiệu", "Số trừ"], 1)
def tn_ten_goi2(rng):
    return M("Trong phép trừ 48 - 15 = 33, số 48 gọi là gì?", "Số bị trừ", ["Số trừ", "Hiệu", "Số hạng"], 1)

def tl_tim_x(rng):
    xs = []
    for _ in range(2):
        x = rng.randint(5, 50); a = rng.randint(5, 40)
        xs.append((f"x + {a} = {x + a}", f"x = {x + a} - {a} = {x}"))
    for _ in range(1):
        a = rng.randint(30, 99); x = rng.randint(5, a - 5)
        xs.append((f"{a} - x = {a - x}", f"x = {a} - {a - x} = {x}"))
    return T("Tìm x:\n" + "; ".join(p for p, _ in xs), "\n".join(f"{p}: {g}" for p, g in xs), 2)
def tl_tim_x_nhan(rng):
    a = rng.randint(2, 5); x = rng.randint(2, 10); b = rng.randint(2, 5); y = rng.randint(2, 10)
    return T(f"Tìm x:\nx × {a} = {a * x}; x : {b} = {y}", f"x × {a} = {a * x}: x = {a * x} : {a} = {x}\nx : {b} = {y}: x = {y} × {b} = {y * b}", 3)
def tl_dien_thieu(rng):
    x = rng.randint(5, 40); a = rng.randint(5, 40)
    return T(f"Tìm số thích hợp điền vào ô trống: ☐ + {a} = {x + a}; {x + a} - ☐ = {x}", f"☐ = {x + a} - {a} = {x}; ☐ = {x + a} - {x} = {a}", 2)
def tl_toan_x(rng):
    x = rng.randint(10, 40); a = rng.randint(5, 30); n = rng.choice(TEN); v = vat(rng)
    return T(f"{n} có một số {v}. Sau khi được cho thêm {a} {v} thì {n} có {x + a} {v}. Hỏi lúc đầu {n} có bao nhiêu {v}?",
             f"Gọi số {v} lúc đầu là x. Ta có: x + {a} = {x + a}\nx = {x + a} - {a} = {x}\nĐáp số: {x} {v}.", 3)
def tl_toan_x2(rng):
    a = rng.randint(30, 80); b = rng.randint(5, a - 10); n = rng.choice(TEN); v = vat(rng)
    return T(f"{n} có {a} {v}. Sau khi cho bạn một số {v} thì {n} còn {a - b} {v}. Hỏi {n} đã cho bạn bao nhiêu {v}?",
             f"Số {v} đã cho bạn là:\n{a} - {a - b} = {b} ({v})\nĐáp số: {b} {v}.", 2)

# 9. Bài toán nhiều hơn, ít hơn ------------------------------------------------------------------------
def tn_nh_nhieu(rng):
    a = rng.randint(10, 60); b = rng.randint(5, 30); x, y = hai_ten(rng); v = vat(rng)
    return M(f"{x} có {a} {v}. {y} có nhiều hơn {x} {b} {v}. {y} có bao nhiêu {v}?", a + b, so_gan(rng, a + b, 0, 120, (b, 1, 10)), 1)
def tn_nh_it(rng):
    b = rng.randint(5, 30); a = b + rng.randint(10, 50); x, y = hai_ten(rng); v = vat(rng)
    return M(f"{x} có {a} {v}. {y} có ít hơn {x} {b} {v}. {y} có bao nhiêu {v}?", a - b, so_gan(rng, a - b, 0, 120, (b, 1, 10)), 1)
def tn_nh_hieu(rng):
    a, b = rng.sample(range(20, 90), 2); x, y = hai_ten(rng); v = vat(rng)
    return M(f"{x} có {max(a, b)} {v}, {y} có {min(a, b)} {v}. {x} có nhiều hơn {y} bao nhiêu {v}?", abs(a - b), so_gan(rng, abs(a - b), 0, 100, (1, 10, 2)), 2)
def tn_nh_cung(rng):
    a = rng.randint(15, 60); b = rng.randint(5, 20); x, y = hai_ten(rng); v = vat(rng)
    return M(f"{x} có {a} {v}. {y} có ít hơn {x} {b} {v}. Hai bạn có tất cả bao nhiêu {v}?", a + a - b, so_gan(rng, 2 * a - b, 0, 150, (b, 1, 10)), 3)
def tn_nh_kho(rng):
    a = rng.randint(10, 50); b = rng.randint(5, 20); x, y = hai_ten(rng); v = vat(rng)
    return M(f"{x} có {a} {v}. {y} có nhiều hơn {x} {b} {v}. Hỏi {y} hơn {x} bao nhiêu {v}?", b, so_gan(rng, b, 1, 100, (1, 2, 10)), 2)
def tn_nh_cm(rng):
    a = rng.randint(30, 90); b = rng.randint(5, 25)
    return M(f"Sợi dây thứ nhất dài {a} cm, sợi dây thứ hai ngắn hơn sợi dây thứ nhất {b} cm. Sợi dây thứ hai dài bao nhiêu xăng-ti-mét?", f"{a - b} cm", [f"{n} cm" for n in so_gan(rng, a - b, 1, 130, (b, 1, 10))], 2)
def tn_nh_kg(rng):
    a = rng.randint(20, 50); b = rng.randint(3, 15)
    return M(f"Bao ngô nặng {a} kg, bao gạo nặng hơn bao ngô {b} kg. Bao gạo nặng bao nhiêu ki-lô-gam?", f"{a + b} kg", [f"{n} kg" for n in so_gan(rng, a + b, 1, 130, (b, 1, 10))], 2)

def tl_nh_nhieu(rng): return de_nhieu(rng, 10, 60)
def tl_nh_it(rng): return de_it(rng, 10, 50)
def tl_nh_hieu(rng):
    a, b = rng.sample(range(20, 95), 2); x, y = hai_ten(rng); v = vat(rng)
    return T(f"{x} có {max(a, b)} {v}, {y} có {min(a, b)} {v}. Hỏi {x} có nhiều hơn {y} bao nhiêu {v}?",
             giai(f"{x} có nhiều hơn {y} số {v} là:", f"{max(a, b)} - {min(a, b)}", abs(a - b), v), 2)
def tl_nh_hai(rng):
    a = rng.randint(15, 60); b = rng.randint(5, 20); x, y = hai_ten(rng); v = vat(rng)
    return T(f"{x} có {a} {v}. {y} có nhiều hơn {x} {b} {v}. Hỏi cả hai bạn có tất cả bao nhiêu {v}?",
             f"Bài giải\n{y} có số {v} là:\n{a} + {b} = {a + b} ({v})\nCả hai bạn có tất cả số {v} là:\n{a} + {a + b} = {2 * a + b} ({v})\nĐáp số: {2 * a + b} {v}.", 3)
def tl_nh_cm(rng):
    a = rng.randint(30, 80); b = rng.randint(5, 25)
    return T(f"Cây thước dài {a} cm. Cây bút ngắn hơn cây thước {b} cm. Hỏi cây bút dài bao nhiêu xăng-ti-mét?",
             giai("Cây bút dài số xăng-ti-mét là:", f"{a} - {b}", a - b, "cm"), 2)
def tl_nh_tuoi(rng):
    a = rng.randint(6, 9); b = rng.randint(20, 35); n = rng.choice(TEN)
    return T(f"{n} {a} tuổi. Mẹ của {n} hơn {n} {b} tuổi. Hỏi mẹ của {n} bao nhiêu tuổi?", giai(f"Mẹ của {n} có số tuổi là:", f"{a} + {b}", a + b, "tuổi"), 2)

CHU_DE = [
    ("Cộng, trừ có nhớ trong phạm vi 100", [tn_cong, tn_tru, tn_thieu_cong, tn_thieu_tru, tn_dung, tn_dem, tn_bot, tn_ba_so],
     [tl_dat, tl_them, tl_hop, tl_bot, tl_nhieu, tl_it, tl_ba]),
    ("Bảng nhân 2, 3, 4, 5", [tn_nhan, tn_thieu_nhan, tn_tong_thanh_nhan, tn_nhom, tn_nhan_dung, tn_day_so, tn_nhan_cham],
     [tl_nhan_tinh, tl_nhan_do, tl_tong_nhan, tl_day, tl_xe]),
    ("Bảng chia 2, 3, 4, 5", [tn_chia, tn_thieu_chia, tn_chia_dung, tn_chia_deu, tn_chia_nhom, tn_nhan_chia, tn_chia_bot],
     [tl_chia_tinh, tl_chia_deu, tl_chia_nhom, tl_nhan_chia, tl_thieu]),
    ("Các số đến 1000", [tn_doc, tn_viet, tn_tram_chuc_dv, tn_chu_so_hang, tn_lien_ke, tn_lon_nhat, tn_tong_gia_tri, tn_tron_tram, tn_chia_khoang],
     [tl_phan_tich3, tl_doc3, tl_sap3, tl_dau3, tl_lien_ke3, tl_dem_cach]),
    ("Cộng, trừ trong phạm vi 1000", [tn_cong3, tn_tru3, tn_cong_tron, tn_thieu3, tn_dem3, tn_ban3, tn_so_pt3, tn_ba3],
     [tl_dat3, tl_them3, tl_hop3, tl_bot3, tl_nhieu3, tl_ba3]),
    ("Đo lường: dm, m, km, kg, lít", [tn_chon_dv, tn_doi_dm, tn_doi_cm, tn_doi_dm_cm, tn_doi_km, tn_kg, tn_lit, tn_cm_dm, tn_so_do],
     [tl_doi, tl_kg, tl_lit, tl_day_dm, tl_chon]),
    ("Chu vi hình tam giác, hình tứ giác", [tn_cv_tg, tn_cv_tu, tn_cv_deu, tn_cv_thieu, tn_cv_hv, tn_cv_cach, tn_so_cv],
     [tl_cv_tg, tl_cv_tu, tl_cv_deu, tl_canh_thieu, tl_rao]),
    ("Tìm số hạng, số bị trừ, số trừ, thừa số, số bị chia", [tn_x_cong, tn_x_cong2, tn_x_tru, tn_x_tru2, tn_x_nhan, tn_x_chia, tn_x_chia2, tn_x_tp, tn_ten_goi, tn_ten_goi2],
     [tl_tim_x, tl_tim_x_nhan, tl_dien_thieu, tl_toan_x, tl_toan_x2]),
    ("Bài toán nhiều hơn, ít hơn", [tn_nh_nhieu, tn_nh_it, tn_nh_hieu, tn_nh_cung, tn_nh_kho, tn_nh_cm, tn_nh_kg],
     [tl_nh_nhieu, tl_nh_it, tl_nh_hieu, tl_nh_hai, tl_nh_cm, tl_nh_tuoi]),
]
