from core import *
from truyen import *
import core as _core

def tien(n): return _core.fmt(n)

def fmt(n, tach=True):
    # Lớp 3: số có 4 chữ số viết liền (1234), từ 5 chữ số trở lên tách nghìn (12.345).
    return _core.fmt(n, tach and abs(int(n)) >= 10000)

# 1. Bảng nhân, chia 6, 7, 8, 9 ---------------------------------------------------
def tn_nhan(rng):
    a = rng.randint(6, 9); b = rng.randint(2, 10)
    return M(f"{a} × {b} = ?", a * b, so_gan(rng, a * b, 0, 100, (a, 1, 2)), 1)
def tn_chia(rng):
    a = rng.randint(6, 9); q = rng.randint(2, 10)
    return M(f"{a * q} : {a} = ?", q, so_gan(rng, q, 0, 12, (1, 2)), 1)
def tn_thieu_nhan(rng):
    a = rng.randint(6, 9); b = rng.randint(2, 10)
    return M(f"{a} × ? = {a * b}", b, so_gan(rng, b, 1, 12, (1, 2)), 2)
def tn_thieu_chia(rng):
    a = rng.randint(6, 9); q = rng.randint(2, 10)
    return M(f"? : {a} = {q}", a * q, so_gan(rng, a * q, 0, 100, (a, 1, 2)), 2)
def tn_nhom(rng):
    a = rng.randint(6, 9); n = rng.randint(3, 9)
    c, v = rng.choice([("hộp", "cái bút"), ("thùng", "chai nước"), ("bó", "bông hoa"), ("xe", "học sinh"), ("rổ", "quả cam")])
    return M(f"Mỗi {c} có {a} {v}. {n} {c} như vậy có tất cả bao nhiêu {v}?", a * n, so_gan(rng, a * n, 0, 100, (a, 1, 2)), 2)
def tn_chia_nhom(rng):
    a = rng.randint(6, 9); q = rng.randint(3, 9)
    c, v = rng.choice([("hộp", "cái bút"), ("thùng", "chai nước"), ("bó", "bông hoa"), ("rổ", "quả cam")])
    return M(f"Có {a * q} {v}, xếp đều vào {a} {c}. Mỗi {c} có bao nhiêu {v}?", q, so_gan(rng, q, 1, 12, (1, 2)), 2)
def tn_dung(rng):
    a = rng.randint(6, 9); b = rng.randint(3, 10)
    return M("Phép tính nào dưới đây đúng?", f"{a} × {b} = {a * b}", [f"{a} × {b} = {a * b + a}", f"{a} × {b} = {a * b - b}", f"{a} × {b} = {a * b + 10}"], 2)
def tn_so_pt(rng):
    a, b = rng.randint(6, 9), rng.randint(3, 9); c, d = rng.randint(6, 9), rng.randint(3, 9)
    if a * b == c * d: raise ValueError
    dd = ">" if a * b > c * d else "<"
    return M(f"Chọn dấu thích hợp: {a} × {b} ... {c} × {d}", dd, sai_dau(dd), 3)
def tn_chia_du_ten(rng):
    a = rng.randint(6, 9); q = rng.randint(3, 9); b = rng.randint(2, 20)
    return M(f"{a * q} : {a} + {b} = ?", q + b, so_gan(rng, q + b, 0, 100, (1, 2, 10)), 3)

def tl_nhan_chia(rng):
    ps_ = []
    for _ in range(2):
        a = rng.randint(6, 9); b = rng.randint(2, 10); ps_.append((f"{a} × {b}", a * b))
    for _ in range(2):
        a = rng.randint(6, 9); q = rng.randint(2, 10); ps_.append((f"{a * q} : {a}", q))
    return T("Tính nhẩm:\n" + "; ".join(p for p, _ in ps_), "; ".join(f"{p} = {r}" for p, r in ps_), 1)
def tl_nhom(rng):
    a = rng.randint(6, 9); n = rng.randint(3, 9); x = rng.choice(TEN)
    c, v = rng.choice([("hộp", "cái bút"), ("thùng", "chai nước"), ("bó", "bông hoa"), ("rổ", "quả cam")])
    return T(f"{x} có {n} {c}, mỗi {c} có {a} {v}. Hỏi {x} có tất cả bao nhiêu {v}?", giai(f"{x} có tất cả số {v} là:", f"{a} × {n}", a * n, v), 2)
def tl_chia(rng):
    a = rng.randint(6, 9); q = rng.randint(3, 9)
    c, v = rng.choice([("hộp", "cái bút"), ("thùng", "chai nước"), ("bó", "bông hoa"), ("rổ", "quả cam")])
    return T(f"Có {a * q} {v} xếp đều vào {a} {c}. Hỏi mỗi {c} có bao nhiêu {v}?", giai(f"Mỗi {c} có số {v} là:", f"{a * q} : {a}", q, v), 2)
def tl_chia_so_nhom(rng):
    a = rng.randint(6, 9); q = rng.randint(3, 9)
    c, v = rng.choice([("hộp", "cái bút"), ("thùng", "chai nước"), ("bó", "bông hoa"), ("xe", "học sinh")])
    return T(f"Có {a * q} {v}, mỗi {c} xếp {a} {v}. Hỏi xếp được bao nhiêu {c}?", giai(f"Số {c} xếp được là:", f"{a * q} : {a}", q, c), 2)
def tl_dien(rng):
    a = rng.randint(6, 9); b = rng.randint(3, 10); c = rng.randint(6, 9); q = rng.randint(3, 10)
    return T(f"Điền số thích hợp vào chỗ chấm:\n{a} × ... = {a * b}; ... : {c} = {q}", f"{a} × {b} = {a * b}; {c * q} : {c} = {q}", 2)
def tl_hai_buoc(rng):
    a = rng.randint(6, 9); n = rng.randint(3, 6); k = rng.randint(2, 4); m = a * n
    return T(f"Một cửa hàng có {n} thùng nước, mỗi thùng {a} chai. Cửa hàng đã bán {k * a} chai. Hỏi còn lại bao nhiêu chai nước?",
             f"Bài giải\nCửa hàng có tất cả số chai nước là:\n{a} × {n} = {m} (chai)\nSố chai nước còn lại là:\n{m} - {k * a} = {m - k * a} (chai)\nĐáp số: {m - k * a} chai.", 3)

# 2. Nhân, chia số có nhiều chữ số với (cho) số có một chữ số ---------------------------
def tn_nhan2(rng):
    a = rng.randint(12, 99); b = rng.randint(2, 9)
    return M(f"{a} × {b} = ?", a * b, so_gan(rng, a * b, 0, 1000, (10, 1, 2)), 1)
def tn_nhan3(rng):
    a = rng.randint(101, 999); b = rng.randint(2, 9)
    return M(f"{a} × {b} = ?", a * b, so_gan(rng, a * b, 0, 10000, (10, 100, 1)), 2)
def tn_nhan4(rng):
    a = rng.randint(1001, 3000); b = rng.randint(2, 6)
    return M(f"{fmt(a)} × {b} = ?", fmt(a * b), [fmt(x, False) for x in so_gan(rng, a * b, 0, 20000, (10, 100, 1000))], 3)
def tn_chia2(rng):
    b = rng.randint(2, 9); q = rng.randint(11, 99)
    return M(f"{b * q} : {b} = ?", q, so_gan(rng, q, 0, 200, (10, 1, 2)), 1)
def tn_chia3(rng):
    b = rng.randint(2, 9); q = rng.randint(101, 999 // b if 999 // b > 101 else 102)
    return M(f"{b * q} : {b} = ?", q, so_gan(rng, q, 0, 1000, (10, 100, 1)), 2)
def tn_chia_du(rng):
    b = rng.randint(3, 9); q = rng.randint(11, 150); r = rng.randint(1, b - 1)
    n = b * q + r
    sai = [f"{q} (dư {x})" for x in range(1, b) if x != r] + [f"{q + 1} (dư {r})", f"{q - 1} (dư {r})"]
    return M(f"{n} : {b} = ? (dư ?)", f"{q} (dư {r})", chon3(rng, sai, f"{q} (dư {r})"), 3)
def tn_thieu(rng):
    b = rng.randint(2, 9); a = rng.randint(11, 150)
    return M(f"{a} × ? = {a * b}", b, so_gan(rng, b, 1, 12, (1, 2)), 2)
def tn_dem(rng):
    a = rng.randint(101, 400); b = rng.randint(2, 6); v = rng.choice(["viên gạch", "quyển sách", "cái bánh"])
    return M(f"Mỗi hộp có {a} {v}. {b} hộp như vậy có tất cả bao nhiêu {v}?", a * b, so_gan(rng, a * b, 0, 3000, (10, 100, 1)), 2)

def tl_dat_nhan(rng):
    ps_ = [(rng.randint(12, 99), rng.randint(2, 9)), (rng.randint(101, 999), rng.randint(2, 9)), (rng.randint(1001, 2500), rng.randint(2, 4))]
    return T("Đặt tính rồi tính:\n" + "; ".join(f"{a} × {b}" for a, b in ps_), "; ".join(f"{a} × {b} = {a * b}" for a, b in ps_), 1)
def tl_dat_chia(rng):
    ps_ = []
    for _ in range(3):
        b = rng.randint(2, 9); q = rng.randint(11, 400); ps_.append((b * q, b, q))
    return T("Đặt tính rồi tính:\n" + "; ".join(f"{n} : {b}" for n, b, _ in ps_), "; ".join(f"{n} : {b} = {q}" for n, b, q in ps_), 1)
def tl_chia_du(rng):
    b = rng.randint(3, 9); q = rng.randint(21, 150); r = rng.randint(1, b - 1); n = b * q + r
    return T(f"Đặt tính rồi tính: {n} : {b}", f"{n} : {b} = {q} (dư {r}).\nThử lại: {q} × {b} + {r} = {n}", 2)
def tl_nhan_do(rng):
    a = rng.randint(120, 450); b = rng.randint(2, 6); x = rng.choice(TEN)
    return T(f"Một xe chở được {a} kg gạo. Hỏi {b} xe như vậy chở được bao nhiêu ki-lô-gam gạo?", giai("Số ki-lô-gam gạo chở được là:", f"{a} × {b}", a * b, "kg"), 2)
def tl_chia_do(rng):
    b = rng.randint(2, 9); q = rng.randint(101, 300)
    return T(f"Có {b * q} quyển vở chia đều cho {b} lớp. Hỏi mỗi lớp được bao nhiêu quyển vở?", giai("Mỗi lớp được số quyển vở là:", f"{b * q} : {b}", q, "quyển vở"), 2)
def tl_hai_buoc2(rng):
    a = rng.randint(100, 300); b = rng.randint(2, 5); c = rng.randint(2, 5)
    return T(f"Mỗi ngày một cửa hàng bán được {a} lít dầu. Hỏi trong {b} ngày bán được bao nhiêu lít dầu? Nếu có {a * b * c} lít dầu thì bán trong bao nhiêu ngày với mức bán như vậy?",
             f"Số lít dầu bán trong {b} ngày: {a} × {b} = {a * b} (lít)\nSố ngày bán hết {a * b * c} lít: {a * b * c} : {a} = {b * c} (ngày)\nĐáp số: {a * b} lít; {b * c} ngày.", 3)

# 3. Các số đến 10 000 và 100 000 -------------------------------------------------------
def _so4(rng):
    while True:
        n = rng.randint(1100, 9999)
        if n % 10 and n // 10 % 10 and n // 100 % 10: return n
def _so5(rng):
    while True:
        n = rng.randint(11000, 99999)
        if n % 10 and n // 10 % 10 and n // 100 % 10 and n // 1000 % 10: return n
def tn_doc4(rng):
    n = _so4(rng)
    return M(f"Số {fmt(n)} đọc là gì?", doc_so(n), chon3(rng, [doc_so(n + k) for k in (-10, 10, -100, 100, -1, 1)], doc_so(n)), 2)
def tn_doc5(rng):
    n = _so5(rng)
    return M(f"Số {fmt(n)} đọc là gì?", doc_so(n), chon3(rng, [doc_so(n + k) for k in (-1000, 1000, -100, 100, -10, 10)], doc_so(n)), 3)
def tn_hang(rng):
    n = _so5(rng); i, ten = rng.choice([(1, "hàng nghìn"), (2, "hàng trăm"), (0, "hàng chục nghìn")])
    ch = str(n)[{0: 0, 1: 1, 2: 2}[i]]
    return M(f"Chữ số {ten} của số {fmt(n)} là chữ số nào?", ch, chon3(rng, [str(n)[k] for k in range(5)] + [str((int(ch) + 1) % 10), str((int(ch) + 2) % 10)], ch), 2)
def tn_lien(rng):
    n = rng.randint(1000, 99998)
    if rng.random() < .5:
        return M(f"Số liền sau của {fmt(n)} là số nào?", fmt(n + 1), [fmt(x) for x in so_gan(rng, n + 1, 0, 100000, (1, 10, 100))], 1)
    return M(f"Số liền trước của {fmt(n)} là số nào?", fmt(n - 1), [fmt(x) for x in so_gan(rng, n - 1, 0, 100000, (1, 10, 100))], 1)
def tn_lon(rng):
    d = rng.sample(range(10000, 100000), 4); m = max(d)
    return M(f"Số nào lớn nhất trong các số {', '.join(fmt(x) for x in d)}?", fmt(m), [fmt(x) for x in d if x != m], 2)
def tn_be(rng):
    d = rng.sample(range(1000, 10000), 4); m = min(d)
    return M(f"Số nào bé nhất trong các số {', '.join(fmt(x) for x in d)}?", fmt(m), [fmt(x) for x in d if x != m], 2)
def tn_tron_tram(rng):
    n = rng.randint(1100, 99900)
    tron = n // 100 * 100 + (100 if n % 100 >= 50 else 0)
    return M(f"Làm tròn số {fmt(n)} đến hàng trăm được số nào?", fmt(tron), [fmt(x) for x in [tron + 100, tron - 100, n // 10 * 10] if x != tron], 3)
def tn_tron_chuc(rng):
    n = rng.randint(1101, 9999)
    if n % 10 == 0: raise ValueError
    tron = n // 10 * 10 + (10 if n % 10 >= 5 else 0)
    return M(f"Làm tròn số {fmt(n)} đến hàng chục được số nào?", fmt(tron), [fmt(x) for x in [tron + 10, tron - 10, n // 100 * 100] if x != tron], 3)
def tn_tong_gia_tri(rng):
    n = _so4(rng); a, b, c, d = n // 1000, n // 100 % 10, n // 10 % 10, n % 10
    return M(f"{a * 1000} + {b * 100} + {c * 10} + {d} = ?", fmt(n), [fmt(x) for x in [n + 10, n - 100, n + 1000, n - 1] if x != n][:3], 2)

def tl_viet_so(rng):
    d = [_so5(rng) for _ in range(2)] + [_so4(rng)]
    return T("Đọc các số sau: " + ", ".join(fmt(x) for x in d) + ".", "\n".join(f"{fmt(x)}: {doc_so(x)}" for x in d), 2)
def tl_phan_tich(rng):
    n = _so5(rng); m = _so4(rng)
    def tong(x):
        s = str(x); return " + ".join(f"{int(ch) * 10 ** (len(s) - 1 - i)}" for i, ch in enumerate(s) if ch != "0")
    return T(f"Viết các số sau thành tổng của các trăm, chục, đơn vị...: {fmt(n)}, {fmt(m)}.", f"{fmt(n)} = {tong(n)}\n{fmt(m)} = {tong(m)}", 2)
def tl_sap(rng):
    d = rng.sample(range(1000, 100000), 5); bd = rng.choice(["bé đến lớn", "lớn đến bé"])
    return T(f"Sắp xếp các số {', '.join(fmt(x) for x in d)} theo thứ tự từ {bd}.", ", ".join(fmt(x) for x in sorted(d, reverse=bd == "lớn đến bé")), 1)
def tl_dau(rng):
    cap = [rng.sample(range(1000, 100000), 2) for _ in range(3)]
    return T("Điền dấu >, < thích hợp vào chỗ chấm:\n" + "; ".join(f"{fmt(a)} ... {fmt(b)}" for a, b in cap),
             "; ".join(f"{fmt(a)} {'>' if a > b else '<'} {fmt(b)}" for a, b in cap), 1)
def tl_lam_tron(rng):
    d = [rng.randint(1100, 9999) for _ in range(3)]
    def lt(n): return n // 100 * 100 + (100 if n % 100 >= 50 else 0)
    return T("Làm tròn các số sau đến hàng trăm: " + ", ".join(fmt(x) for x in d) + ".", "\n".join(f"{fmt(x)} làm tròn đến hàng trăm là {fmt(lt(x))}" for x in d), 3)
def tl_day(rng):
    a = rng.randint(1000, 9000) // 1000 * 1000; k = rng.choice([100, 1000, 10000])
    day = [a + k * i for i in range(4)]
    return T(f"Viết tiếp hai số vào dãy số: {', '.join(fmt(x) for x in day)}, ..., ...", f"Mỗi số hơn số liền trước {fmt(k)}: {fmt(a + 4 * k)}, {fmt(a + 5 * k)}", 2)

# 4. Chu vi, diện tích hình chữ nhật, hình vuông -----------------------------------------------
def _hcn(rng):
    a = rng.randint(5, 30); b = rng.randint(3, a - 1); return a, b
def tn_cv_hcn(rng):
    a, b = _hcn(rng)
    return M(f"Hình chữ nhật có chiều dài {a} cm, chiều rộng {b} cm. Chu vi hình chữ nhật là:", f"{(a + b) * 2} cm", [f"{x} cm" for x in [a * b, a + b, (a + b) * 2 + 2, a * 2 + b][:3]], 1)
def tn_dt_hcn(rng):
    a, b = _hcn(rng)
    return M(f"Hình chữ nhật có chiều dài {a} cm, chiều rộng {b} cm. Diện tích hình chữ nhật là:", f"{a * b} cm²", [f"{x} cm²" for x in so_gan(rng, a * b, 1, 1000, (a, b, 1))], 1)
def tn_cv_hv(rng):
    a = rng.randint(3, 25)
    return M(f"Hình vuông có cạnh dài {a} cm. Chu vi hình vuông là:", f"{4 * a} cm", [f"{x} cm" for x in [a * a, 2 * a, a + 4]], 1)
def tn_dt_hv(rng):
    a = rng.randint(3, 25)
    return M(f"Hình vuông có cạnh dài {a} cm. Diện tích hình vuông là:", f"{a * a} cm²", [f"{x} cm²" for x in [4 * a, 2 * a, a * a + a]], 1)
def tn_rong(rng):
    a, b = _hcn(rng)
    return M(f"Hình chữ nhật có diện tích {a * b} cm², chiều dài {a} cm. Chiều rộng là:", f"{b} cm", [f"{x} cm" for x in so_gan(rng, b, 1, 60, (1, 2, 3))], 3)
def tn_canh_hv(rng):
    a = rng.randint(3, 25)
    return M(f"Hình vuông có chu vi {4 * a} cm. Cạnh của hình vuông dài:", f"{a} cm", [f"{x} cm" for x in so_gan(rng, a, 1, 60, (1, 2, 4))], 2)
def tn_dai_tu_cv(rng):
    a, b = _hcn(rng)
    return M(f"Hình chữ nhật có chu vi {(a + b) * 2} cm, chiều rộng {b} cm. Chiều dài là:", f"{a} cm", [f"{x} cm" for x in so_gan(rng, a, 1, 60, (1, 2, b))], 3)
def tn_so_dt(rng):
    a, b = _hcn(rng); c = rng.randint(3, 15)
    if a * b == c * c: raise ValueError
    return M(f"Hình chữ nhật có chiều dài {a} cm, chiều rộng {b} cm; hình vuông có cạnh {c} cm. Hình nào có diện tích lớn hơn?",
             "Hình chữ nhật" if a * b > c * c else "Hình vuông", ["Hình vuông" if a * b > c * c else "Hình chữ nhật", "Bằng nhau", "Không so sánh được"], 3)
def tn_dt_m2(rng):
    a, b = _hcn(rng)
    return M(f"Mảnh vườn hình chữ nhật có chiều dài {a} m, chiều rộng {b} m. Diện tích mảnh vườn là:", f"{a * b} m²", [f"{x} m²" for x in so_gan(rng, a * b, 1, 1000, (a, b, 1))], 2)

def tl_cv_dt_hcn(rng):
    a, b = _hcn(rng)
    return T(f"Một hình chữ nhật có chiều dài {a} cm, chiều rộng {b} cm. Tính chu vi và diện tích hình chữ nhật đó.",
             f"Chu vi: ({a} + {b}) × 2 = {(a + b) * 2} (cm)\nDiện tích: {a} × {b} = {a * b} (cm²)\nĐáp số: {(a + b) * 2} cm; {a * b} cm².", 1)
def tl_cv_dt_hv(rng):
    a = rng.randint(3, 25)
    return T(f"Một hình vuông có cạnh dài {a} cm. Tính chu vi và diện tích hình vuông đó.",
             f"Chu vi: {a} × 4 = {4 * a} (cm)\nDiện tích: {a} × {a} = {a * a} (cm²)\nĐáp số: {4 * a} cm; {a * a} cm².", 1)
def tl_vuon(rng):
    a, b = _hcn(rng)
    return T(f"Một mảnh vườn hình chữ nhật có chiều dài {a} m, chiều rộng {b} m. Người ta muốn rào xung quanh vườn. Hỏi hàng rào dài bao nhiêu mét? Diện tích mảnh vườn là bao nhiêu mét vuông?",
             f"Hàng rào dài (chu vi): ({a} + {b}) × 2 = {(a + b) * 2} (m)\nDiện tích vườn: {a} × {b} = {a * b} (m²)\nĐáp số: {(a + b) * 2} m; {a * b} m².", 2)
def tl_rong(rng):
    a, b = _hcn(rng)
    return T(f"Một hình chữ nhật có diện tích {a * b} cm², chiều dài {a} cm. Tính chiều rộng và chu vi hình chữ nhật.",
             f"Chiều rộng: {a * b} : {a} = {b} (cm)\nChu vi: ({a} + {b}) × 2 = {(a + b) * 2} (cm)\nĐáp số: {b} cm; {(a + b) * 2} cm.", 3)
def tl_so_sanh_dt(rng):
    a, b = _hcn(rng); c = rng.randint(3, 15)
    if a * b == c * c: raise ValueError
    lon = "hình chữ nhật" if a * b > c * c else "hình vuông"
    return T(f"Hình chữ nhật có chiều dài {a} cm, chiều rộng {b} cm. Hình vuông có cạnh {c} cm. Hình nào có diện tích lớn hơn?",
             f"Diện tích hình chữ nhật: {a} × {b} = {a * b} (cm²)\nDiện tích hình vuông: {c} × {c} = {c * c} (cm²)\nVậy {lon} có diện tích lớn hơn.", 3)
def tl_tam_bia(rng):
    c = rng.randint(4, 12)
    return T(f"Một tấm bìa hình vuông có chu vi {4 * c} cm. Tính diện tích tấm bìa đó.", f"Cạnh hình vuông: {4 * c} : 4 = {c} (cm)\nDiện tích: {c} × {c} = {c * c} (cm²)\nĐáp số: {c * c} cm².", 3)

# 5. Giá trị của biểu thức -------------------------------------------------------------------------
def _bt(rng):
    k = rng.randint(0, 7)
    if k == 0:
        a, b, c = rng.randint(10, 60), rng.randint(2, 9), rng.randint(2, 9)
        return f"{a} + {b} × {c}", a + b * c, f"{b} × {c} = {b * c}; {a} + {b * c} = {a + b * c}"
    if k == 1:
        b, c = rng.randint(2, 9), rng.randint(2, 9); a = b * c + rng.randint(5, 40)
        return f"{a} - {b} × {c}", a - b * c, f"{b} × {c} = {b * c}; {a} - {b * c} = {a - b * c}"
    if k == 2:
        a, b, c = rng.randint(2, 9), rng.randint(2, 9), rng.randint(5, 60)
        return f"{a} × {b} + {c}", a * b + c, f"{a} × {b} = {a * b}; {a * b} + {c} = {a * b + c}"
    if k == 3:
        a, b = rng.randint(3, 9), rng.randint(3, 9); c = rng.randint(2, a * b - 1)
        return f"{a} × {b} - {c}", a * b - c, f"{a} × {b} = {a * b}; {a * b} - {c} = {a * b - c}"
    if k == 4:
        b, q, c = rng.randint(2, 9), rng.randint(2, 12), rng.randint(5, 50)
        return f"{b * q} : {b} + {c}", q + c, f"{b * q} : {b} = {q}; {q} + {c} = {q + c}"
    if k == 5:
        a, b, c = rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 9)
        return f"({a} + {b}) × {c}", (a + b) * c, f"{a} + {b} = {a + b}; {a + b} × {c} = {(a + b) * c}"
    if k == 6:
        c, q = rng.randint(2, 9), rng.randint(2, 12); s = c * q; a = rng.randint(1, s - 1); b = s - a
        return f"({a} + {b}) : {c}", q, f"{a} + {b} = {s}; {s} : {c} = {q}"
    a, b, c = rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 9)
    return f"{a} × ({b} + {c})", a * (b + c), f"{b} + {c} = {b + c}; {a} × {b + c} = {a * (b + c)}"
def tn_bt(rng):
    t, v, _ = _bt(rng)
    return M(f"Giá trị của biểu thức {t} là:", v, so_gan(rng, v, 0, 400, (1, 2, 10)), 2)
def tn_bt_thu_tu(rng):
    a, b, c = rng.randint(10, 50), rng.randint(2, 9), rng.randint(2, 9)
    return M(f"Khi tính {a} + {b} × {c}, ta phải làm phép tính nào trước?", f"{b} × {c}", [f"{a} + {b}", "Làm từ trái sang phải", "Phép cộng"], 1)
def tn_bt_ngoac(rng):
    a, b, c = rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 9)
    return M(f"({a} + {b}) × {c} = ?", (a + b) * c, [a + b * c, (a + b) + c, (a + b) * c + c], 2)
def tn_bt_so_sanh(rng):
    t1, v1, _ = _bt(rng); t2, v2, _ = _bt(rng)
    if v1 == v2: raise ValueError
    d = ">" if v1 > v2 else "<"
    return M(f"Chọn dấu thích hợp: {t1} ... {t2}", d, sai_dau(d), 3)
def tn_bt_dung(rng):
    t, v, _ = _bt(rng)
    return M("Phép tính nào dưới đây đúng?", f"{t} = {v}", [f"{t} = {x}" for x in so_gan(rng, v, 0, 400, (1, 2, 10))], 3)
def tn_bt_tim(rng):
    a, b = rng.randint(2, 9), rng.randint(2, 9); c = rng.randint(2, 9); x = rng.randint(2, 9)
    return M(f"Tìm x: x × {a} + {b} = {x * a + b}", x, so_gan(rng, x, 1, 15, (1, 2)), 3)

def tl_bt(rng):
    ls = [_bt(rng) for _ in range(3)]
    return T("Tính giá trị của biểu thức:\n" + "\n".join(t for t, _, _ in ls), "\n".join(f"{t}: {s}  →  {t} = {v}" for t, v, s in ls), 1)
def tl_bt2(rng):
    ls = [_bt(rng) for _ in range(4)]
    return T("Tính giá trị của biểu thức:\n" + "; ".join(t for t, _, _ in ls), "\n".join(f"{t} = {v}  ({s})" for t, v, s in ls), 2)
def tl_bt_toan(rng):
    a = rng.randint(3, 9); n = rng.randint(3, 9); b = rng.randint(2, 9); c = rng.randint(3, 6)
    return T(f"Một cửa hàng có {n} thùng sữa, mỗi thùng có {a} hộp. Cửa hàng nhập thêm {b * c} hộp sữa. Hỏi cửa hàng có tất cả bao nhiêu hộp sữa? (Viết thành một biểu thức rồi tính)",
             f"Số hộp sữa có tất cả là: {a} × {n} + {b * c} = {a * n} + {b * c} = {a * n + b * c} (hộp)\nĐáp số: {a * n + b * c} hộp.", 3)
def tl_dien_dau(rng):
    a, b, c = rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 9)
    return T(f"Điền dấu >, <, = thích hợp vào chỗ chấm:\n{a} + {b} × {c} ... ({a} + {b}) × {c}",
             f"{a} + {b} × {c} = {a + b * c}; ({a} + {b}) × {c} = {(a + b) * c}. " + (f"Vậy {a + b * c} {'>' if a + b * c > (a + b) * c else '<' if a + b * c < (a + b) * c else '='} {(a + b) * c}."), 3)
def tl_tim_x(rng):
    a, b = rng.randint(2, 9), rng.randint(2, 9); x = rng.randint(2, 12)
    return T(f"Tìm x: x × {a} + {b} = {x * a + b}", f"x × {a} = {x * a + b} - {b} = {x * a}\nx = {x * a} : {a} = {x}", 3)
def tl_bt_chia(rng):
    ls = [_bt(rng) for _ in range(2)]
    return T("Tính giá trị của biểu thức và ghi rõ từng bước:\n" + "\n".join(t for t, _, _ in ls), "\n".join(f"{t}: {s} → {v}" for t, v, s in ls), 2)

# 6. Gấp, giảm, so sánh số lần ---------------------------------------------------------------------------
def tn_gap(rng):
    a, b = rng.randint(3, 25), rng.randint(2, 9)
    return M(f"Gấp {a} lên {b} lần được số nào?", a * b, so_gan(rng, a * b, 0, 300, (a, 1, 2)), 1)
def tn_giam(rng):
    a, b = rng.randint(3, 25), rng.randint(2, 9)
    return M(f"Giảm {a * b} đi {b} lần được số nào?", a, so_gan(rng, a, 0, 100, (1, 2, b)), 1)
def tn_gap_may(rng):
    b, k = rng.randint(3, 15), rng.randint(2, 9)
    return M(f"Số {b * k} gấp mấy lần số {b}?", f"{k} lần", [f"{x} lần" for x in so_gan(rng, k, 1, 15, (1, 2))], 2)
def tn_gap_story(rng):
    a, k = rng.randint(3, 20), rng.randint(2, 6)
    v1, v2 = rng.choice([("gà", "vịt"), ("bò", "trâu"), ("xe máy", "ô tô")])
    return M(f"Đàn {v1} có {a} con. Đàn {v2} có số con gấp {k} lần đàn {v1}. Đàn {v2} có bao nhiêu con?", a * k, so_gan(rng, a * k, 0, 200, (a, 1, 2)), 2)
def tn_giam_story(rng):
    a, k = rng.randint(3, 20), rng.randint(2, 6)
    return M(f"Có {a * k} lít nước mắm đựng trong các chai. Giảm số lít đó đi {k} lần thì còn bao nhiêu lít?", f"{a} lít", [f"{x} lít" for x in so_gan(rng, a, 1, 100, (1, 2, k))], 2)
def tn_so_lan(rng):
    b, k = rng.randint(3, 12), rng.randint(2, 8)
    x, y = hai_ten(rng)
    return M(f"{x} có {b * k} viên bi, {y} có {b} viên bi. Số bi của {x} gấp mấy lần số bi của {y}?", f"{k} lần", [f"{n} lần" for n in so_gan(rng, k, 1, 15, (1, 2))], 2)
def tn_hon_kem(rng):
    b, k = rng.randint(3, 12), rng.randint(2, 6)
    return M(f"Con gấu nặng {b * k} kg, con khỉ nặng {b} kg. Con khỉ nhẹ bằng một phần mấy con gấu?", f"1/{k}", [f"1/{x}" for x in so_gan(rng, k, 2, 12, (1, 2))], 3)
def tn_gap_them(rng):
    a, k, b = rng.randint(3, 15), rng.randint(2, 6), rng.randint(2, 15)
    return M(f"Gấp {a} lên {k} lần rồi cộng thêm {b}, kết quả là bao nhiêu?", a * k + b, so_gan(rng, a * k + b, 0, 200, (b, 1, 2)), 3)

def tl_gap(rng):
    a, k = rng.randint(3, 20), rng.randint(2, 7); x = rng.choice(TEN)
    return T(f"Thùng thứ nhất có {a} lít dầu. Thùng thứ hai có số lít dầu gấp {k} lần thùng thứ nhất. Hỏi thùng thứ hai có bao nhiêu lít dầu?", giai("Thùng thứ hai có số lít dầu là:", f"{a} × {k}", a * k, "lít"), 1)
def tl_giam(rng):
    a, k = rng.randint(3, 20), rng.randint(2, 7)
    return T(f"Một sợi dây dài {a * k} m. Cắt đi để chiều dài giảm {k} lần. Hỏi sợi dây sau khi cắt dài bao nhiêu mét?", giai("Sợi dây sau khi cắt dài số mét là:", f"{a * k} : {k}", a, "m"), 1)
def tl_so_lan(rng):
    b, k = rng.randint(3, 12), rng.randint(2, 8); x, y = hai_ten(rng)
    return T(f"{x} có {b * k} quyển truyện, {y} có {b} quyển truyện. Hỏi số truyện của {x} gấp mấy lần số truyện của {y}?", giai(f"Số truyện của {x} gấp số truyện của {y} số lần là:", f"{b * k} : {b}", k, "lần"), 2)
def tl_nhieu_hon(rng):
    a, k, b = rng.randint(3, 15), rng.randint(2, 6), rng.randint(2, 15)
    return T(f"Hà có {a} nhãn vở. Lan có số nhãn vở gấp {k} lần của Hà và thêm {b} nhãn nữa. Hỏi Lan có bao nhiêu nhãn vở?",
             f"Gấp {k} lần số nhãn vở của Hà: {a} × {k} = {a * k} (nhãn)\nLan có: {a * k} + {b} = {a * k + b} (nhãn)\nĐáp số: {a * k + b} nhãn vở.", 3)
def tl_phan_biet(rng):
    a, k, b = rng.randint(5, 20), rng.randint(2, 6), rng.randint(2, 15)
    return T(f"Phân biệt: \"hơn {b} đơn vị\" và \"gấp {k} lần\". Số {a} hơn {b} đơn vị là số nào? Số gấp {k} lần số {a} là số nào?", f"Hơn {b} đơn vị: {a} + {b} = {a + b}\nGấp {k} lần: {a} × {k} = {a * k}", 2)
def tl_tuoi(rng):
    a, k = rng.randint(5, 10), rng.randint(3, 5)
    return T(f"Năm nay con {a} tuổi, tuổi mẹ gấp {k} lần tuổi con. Hỏi năm nay mẹ bao nhiêu tuổi? Mẹ hơn con bao nhiêu tuổi?",
             f"Tuổi mẹ: {a} × {k} = {a * k} (tuổi)\nMẹ hơn con: {a * k} - {a} = {a * k - a} (tuổi)\nĐáp số: {a * k} tuổi; {a * k - a} tuổi.", 3)

# 7. Một phần mấy của một số ------------------------------------------------------------------------------------
_WORD = {2: "hai", 3: "ba", 4: "tư", 5: "năm", 6: "sáu", 7: "bảy", 8: "tám", 9: "chín"}
def tn_doc_pn(rng):
    n = rng.randint(2, 9)
    return M(f"Phân số 1/{n} đọc là gì?", f"Một phần {_WORD[n]}", [f"Một phần {_WORD[x]}" for x in range(2, 10) if x != n][:3], 1)
def tn_viet_pn(rng):
    n = rng.randint(2, 9)
    return M(f"\"Một phần {_WORD[n]}\" viết là:", f"1/{n}", [f"1/{x}" for x in range(2, 10) if x != n][:2] + [f"{n}/1"], 1)
def tn_mot_phan(rng):
    n = rng.randint(2, 9); q = rng.randint(2, 12)
    return M(f"1/{n} của {n * q} là:", q, so_gan(rng, q, 1, 120, (1, 2, n)), 2)
def tn_so_hs(rng):
    n = rng.choice([2, 3, 4, 5, 6]); q = rng.randint(3, 10)
    return M(f"Lớp có {n * q} học sinh, 1/{n} số học sinh đi trực nhật. Số học sinh đi trực nhật là:", f"{q} học sinh", [f"{x} học sinh" for x in so_gan(rng, q, 1, 60, (1, 2, n))], 2)
def tn_tim_so(rng):
    n = rng.randint(2, 9); q = rng.randint(2, 12)
    return M(f"1/{n} của một số bằng {q}. Số đó là:", n * q, so_gan(rng, n * q, 0, 150, (q, 1, 2)), 3)
def tn_chia_phan(rng):
    n = rng.randint(2, 9)
    return M(f"Một hình được chia thành {n} phần bằng nhau. Mỗi phần bằng bao nhiêu của hình đó?", f"1/{n}", [f"1/{x}" for x in range(2, 10) if x != n][:2] + [f"{n}/1"], 2)
def tn_qua(rng):
    n = rng.choice([2, 3, 4, 5, 6, 8, 9]); q = rng.randint(2, 9)
    return M(f"Mẹ có {n * q} quả cam, biếu bà 1/{n} số cam. Mẹ biếu bà bao nhiêu quả cam?", f"{q} quả", [f"{x} quả" for x in so_gan(rng, q, 1, 60, (1, 2, n))], 2)
def tn_con_lai(rng):
    n = rng.choice([2, 3, 4, 5]); q = rng.randint(3, 9)
    return M(f"Có {n * q} cái kẹo, cho bạn 1/{n} số kẹo. Số kẹo còn lại là:", f"{n * q - q} cái", [f"{x} cái" for x in so_gan(rng, n * q - q, 1, 80, (q, 1, 2))], 3)
def tn_so_pn(rng):
    a, b = rng.sample(range(2, 10), 2)
    return M(f"Phân số nào lớn hơn: 1/{a} hay 1/{b}?", f"1/{min(a, b)}", [f"1/{max(a, b)}", "Bằng nhau", "Không so sánh được"], 3)

def tl_mot_phan(rng):
    ps_ = []
    for _ in range(3):
        n = rng.randint(2, 9); q = rng.randint(2, 10); ps_.append((n, n * q, q))
    return T("Tính:\n" + "; ".join(f"1/{n} của {t}" for n, t, _ in ps_), "; ".join(f"1/{n} của {t} là {t} : {n} = {q}" for n, t, q in ps_), 1)
def tl_lop(rng):
    n = rng.choice([2, 3, 4, 5, 6]); q = rng.randint(3, 10)
    return T(f"Lớp 3A có {n * q} học sinh, trong đó 1/{n} số học sinh là học sinh giỏi. Hỏi lớp 3A có bao nhiêu học sinh giỏi?", giai("Số học sinh giỏi của lớp 3A là:", f"{n * q} : {n}", q, "học sinh"), 2)
def tl_qua(rng):
    n = rng.choice([2, 3, 4, 5, 6, 8, 9]); q = rng.randint(2, 9)
    return T(f"Mẹ mua {n * q} quả cam, đã biếu bà 1/{n} số cam đó. Hỏi mẹ còn lại bao nhiêu quả cam?", f"Số cam biếu bà: {n * q} : {n} = {q} (quả)\nSố cam còn lại: {n * q} - {q} = {n * q - q} (quả)\nĐáp số: {n * q - q} quả.", 3)
def tl_tim_so(rng):
    n = rng.randint(2, 9); q = rng.randint(2, 12)
    return T(f"1/{n} của một số bằng {q}. Tìm số đó.", f"Số đó là: {q} × {n} = {n * q}\n(Kiểm tra: 1/{n} của {n * q} là {n * q} : {n} = {q})", 3)
def tl_doan(rng):
    n = rng.randint(2, 9); q = rng.randint(2, 12)
    return T(f"Một đoạn dây dài {n * q} cm. Cắt lấy 1/{n} đoạn dây. Hỏi đoạn dây cắt ra dài bao nhiêu xăng-ti-mét?", giai("Đoạn dây cắt ra dài số xăng-ti-mét là:", f"{n * q} : {n}", q, "cm"), 2)
def tl_so_sanh(rng):
    a, b = rng.sample(range(2, 10), 2); k = rng.randint(2, 6); t = a * b * k
    return T(f"Lấy 1/{a} của {t} và 1/{b} của {t}. Số nào lớn hơn?", f"1/{a} của {t} là {t // a}; 1/{b} của {t} là {t // b}.\n" + (f"Vậy 1/{a} của {t} lớn hơn." if t // a > t // b else f"Vậy 1/{b} của {t} lớn hơn."), 3)

# 8. Đo lường: mm, g, ml, tiền, thời gian ---------------------------------------------------------------------
def tn_mm(rng):
    a = rng.randint(2, 30); return M(f"{a} cm = ... mm", a * 10, [a, a * 100, a * 10 + 10], 1)
def tn_g(rng):
    a = rng.randint(2, 9); return M(f"{a} kg = ... g", a * 1000, [a * 100, a * 10, a * 1000 + 100], 1)
def tn_ml(rng):
    a = rng.randint(2, 9); return M(f"{a} l = ... ml", a * 1000, [a * 100, a * 10, a * 1000 + 100], 1)
def tn_gio(rng):
    a = rng.randint(2, 6); return M(f"{a} giờ = ... phút", a * 60, [a * 100, a * 30, a * 60 + 10], 1)
def tn_g_cong(rng):
    a = rng.randint(100, 500); b = rng.randint(100, 400)
    return M(f"Gói bột nặng {a} g, gói đường nặng {b} g. Cả hai gói nặng bao nhiêu gam?", f"{a + b} g", [f"{x} g" for x in so_gan(rng, a + b, 1, 2000, (10, 100, 1))], 2)
def tn_ml_chia(rng):
    n = rng.randint(2, 6); q = rng.choice([100, 150, 200, 250])
    return M(f"Chai nước có {n * q} ml, rót đều vào {n} cốc. Mỗi cốc có bao nhiêu mi-li-lít?", f"{q} ml", [f"{x} ml" for x in so_gan(rng, q, 1, 2000, (50, 100, 10))], 2)
def tn_tien(rng):
    a = rng.randint(2, 9) * 1000; b = rng.randint(2, 9) * 1000
    return M(f"Mua một quyển vở giá {tien(a)} đồng và một cái bút giá {tien(b)} đồng. Phải trả tất cả bao nhiêu tiền?", f"{tien(a + b)} đồng", [f"{tien(x)} đồng" for x in so_gan(rng, a + b, 1000, 40000, (1000, 2000, 500))], 2)
def tn_tra_lai(rng):
    a = rng.randint(2, 9) * 1000 + rng.choice([0, 500]); t = rng.choice([10000, 20000])
    if a >= t: raise ValueError
    return M(f"Mua một món đồ giá {tien(a)} đồng, đưa người bán hàng tờ {tien(t)} đồng. Người bán hàng phải trả lại bao nhiêu tiền?", f"{tien(t - a)} đồng", [f"{tien(x)} đồng" for x in so_gan(rng, t - a, 500, 40000, (500, 1000, 2000))], 3)
def tn_thoigian(rng):
    h = rng.randint(6, 10); p = rng.choice([10, 15, 20, 30]); k = rng.choice([15, 20, 25, 30])
    if p + k >= 60: raise ValueError
    return M(f"Bạn An bắt đầu làm bài lúc {h} giờ {p} phút và làm xong lúc {h} giờ {p + k} phút. An làm bài trong bao lâu?", f"{k} phút", [f"{x} phút" for x in so_gan(rng, k, 5, 60, (5, 10, 15))], 2)
def tn_ngay(rng):
    n = rng.randint(2, 5)
    return M(f"{n} tuần lễ có bao nhiêu ngày?", f"{7 * n} ngày", [f"{x} ngày" for x in so_gan(rng, 7 * n, 7, 60, (1, 7, 2))], 1)
def tn_thang(rng):
    t = rng.choice([(4, 30), (6, 30), (9, 30), (11, 30), (1, 31), (3, 31), (5, 31), (7, 31), (8, 31), (10, 31), (12, 31)])
    return M(f"Tháng {t[0]} có bao nhiêu ngày?", f"{t[1]} ngày", [f"{x} ngày" for x in (28, 29, 30, 31) if x != t[1]][:3], 2)

def tl_doi(rng):
    a, b, c, d = rng.randint(2, 20), rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 5)
    return T(f"Viết số thích hợp vào chỗ chấm:\n{a} cm = ... mm; {b} kg = ... g; {c} l = ... ml; {d} giờ = ... phút",
             f"{a} cm = {a * 10} mm; {b} kg = {b * 1000} g; {c} l = {c * 1000} ml; {d} giờ = {d * 60} phút", 1)
def tl_g(rng):
    a = rng.randint(200, 800); b = rng.randint(100, 500)
    return T(f"Quả cam nặng {a} g, quả bưởi nặng {a + b} g. Hỏi quả bưởi nặng hơn quả cam bao nhiêu gam? Cả hai quả nặng bao nhiêu gam?",
             f"Bưởi nặng hơn cam: {a + b} - {a} = {b} (g)\nCả hai quả nặng: {a} + {a + b} = {2 * a + b} (g)\nĐáp số: {b} g; {2 * a + b} g.", 2)
def tl_tien(rng):
    a = rng.randint(3, 9) * 1000; b = rng.randint(3, 9) * 1000; t = rng.choice([20000, 50000])
    return T(f"Mai mua một quyển vở giá {tien(a)} đồng và một hộp bút giá {tien(b)} đồng. Mai đưa cô bán hàng tờ {tien(t)} đồng. Hỏi cô bán hàng phải trả lại Mai bao nhiêu tiền?",
             f"Số tiền phải trả: {tien(a)} + {tien(b)} = {tien(a + b)} (đồng)\nSố tiền cô trả lại: {tien(t)} - {tien(a + b)} = {tien(t - a - b)} (đồng)\nĐáp số: {tien(t - a - b)} đồng.", 3)
def tl_ml(rng):
    n = rng.randint(3, 6); q = rng.choice([100, 150, 200, 250])
    return T(
        f"Mỗi hộp sữa có {q} ml. Hỏi {n} hộp sữa như vậy có tất cả bao nhiêu mi-li-lít?", giai("Số mi-li-lít sữa có tất cả là:", f"{q} × {n}", n * q, "ml"), 2)
def tl_thoi_gian(rng):
    h = rng.randint(6, 10); p = rng.choice([10, 15, 20, 30]); k = rng.choice([15, 20, 25, 30, 45])
    t = h * 60 + p + k
    return T(f"Một buổi học bắt đầu lúc {h} giờ {p} phút và kéo dài {k} phút. Hỏi buổi học kết thúc lúc mấy giờ, mấy phút?",
             f"{h} giờ {p} phút + {k} phút = {t // 60} giờ {t % 60} phút\nVậy buổi học kết thúc lúc {t // 60} giờ {t % 60} phút.", 3)
def tl_tuan(rng):
    n = rng.randint(2, 6)
    return T(f"Một tuần lễ có 7 ngày. Hỏi {n} tuần lễ có bao nhiêu ngày? Nếu hôm nay là thứ hai thì sau {n} tuần là thứ mấy?", f"{n} tuần lễ có: 7 × {n} = {7 * n} (ngày)\nSau đúng {n} tuần thì vẫn là thứ hai.", 2)

CHU_DE = [
    ("Bảng nhân, bảng chia 6, 7, 8, 9", [tn_nhan, tn_chia, tn_thieu_nhan, tn_thieu_chia, tn_nhom, tn_chia_nhom, tn_dung, tn_so_pt, tn_chia_du_ten],
     [tl_nhan_chia, tl_nhom, tl_chia, tl_chia_so_nhom, tl_dien, tl_hai_buoc]),
    ("Nhân, chia số có nhiều chữ số với (cho) số có một chữ số", [tn_nhan2, tn_nhan3, tn_nhan4, tn_chia2, tn_chia3, tn_chia_du, tn_thieu, tn_dem],
     [tl_dat_nhan, tl_dat_chia, tl_chia_du, tl_nhan_do, tl_chia_do, tl_hai_buoc2]),
    ("Các số đến 10 000 và 100 000", [tn_doc4, tn_doc5, tn_hang, tn_lien, tn_lon, tn_be, tn_tron_tram, tn_tron_chuc, tn_tong_gia_tri],
     [tl_viet_so, tl_phan_tich, tl_sap, tl_dau, tl_lam_tron, tl_day]),
    ("Chu vi, diện tích hình chữ nhật, hình vuông", [tn_cv_hcn, tn_dt_hcn, tn_cv_hv, tn_dt_hv, tn_rong, tn_canh_hv, tn_dai_tu_cv, tn_so_dt, tn_dt_m2],
     [tl_cv_dt_hcn, tl_cv_dt_hv, tl_vuon, tl_rong, tl_so_sanh_dt, tl_tam_bia]),
    ("Giá trị của biểu thức", [tn_bt, tn_bt_thu_tu, tn_bt_ngoac, tn_bt_so_sanh, tn_bt_dung, tn_bt_tim],
     [tl_bt, tl_bt2, tl_bt_toan, tl_dien_dau, tl_tim_x, tl_bt_chia]),
    ("Gấp một số lên nhiều lần, giảm một số đi nhiều lần", [tn_gap, tn_giam, tn_gap_may, tn_gap_story, tn_giam_story, tn_so_lan, tn_hon_kem, tn_gap_them],
     [tl_gap, tl_giam, tl_so_lan, tl_nhieu_hon, tl_phan_biet, tl_tuoi]),
    ("Một phần mấy của một số", [tn_doc_pn, tn_viet_pn, tn_mot_phan, tn_so_hs, tn_tim_so, tn_chia_phan, tn_qua, tn_con_lai, tn_so_pn],
     [tl_mot_phan, tl_lop, tl_qua, tl_tim_so, tl_doan, tl_so_sanh]),
    ("Đo lường: mm, g, ml, tiền Việt Nam, thời gian", [tn_mm, tn_g, tn_ml, tn_gio, tn_g_cong, tn_ml_chia, tn_tien, tn_tra_lai, tn_thoigian, tn_ngay, tn_thang],
     [tl_doi, tl_g, tl_tien, tl_ml, tl_thoi_gian, tl_tuan]),
]
