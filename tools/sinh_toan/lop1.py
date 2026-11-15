from core import *
from truyen import *

def _s(rng, a, b, lo=0, hi=10):
    return rng.randint(lo, hi)

# 1. Các số đến 10 -----------------------------------------------------------
def tn_lien_sau(rng):
    a = rng.randint(0, 9)
    return M(f"Số liền sau của {a} là số nào?", a + 1, so_gan(rng, a + 1, 0, 10, (1, 2)), 1)
def tn_lien_truoc(rng):
    a = rng.randint(1, 10)
    return M(f"Số liền trước của {a} là số nào?", a - 1, so_gan(rng, a - 1, 0, 10, (1, 2)), 1)
def tn_so_sanh(rng):
    a, b = rng.sample(range(0, 11), 2)
    dung = f"{a} > {b}" if a > b else f"{a} < {b}"
    sai = [f"{a} < {b}" if a > b else f"{a} > {b}", f"{a} = {b}", f"{b} {'>' if a > b else '<'} {a}"]
    return M(f"Cách so sánh nào dưới đây đúng?", dung, sai, 1)
def tn_lon_nhat(rng):
    d = rng.sample(range(0, 11), 4)
    m = max(d)
    return M(f"Trong các số {', '.join(map(str, d))}, số nào lớn nhất?", m, [x for x in d if x != m], 2)
def tn_be_nhat(rng):
    d = rng.sample(range(0, 11), 4)
    m = min(d)
    return M(f"Trong các số {', '.join(map(str, d))}, số nào bé nhất?", m, [x for x in d if x != m], 2)
def tn_o_giua(rng):
    a = rng.randint(0, 8)
    return M(f"Số nào nằm giữa {a} và {a + 2}?", a + 1, so_gan(rng, a + 1, 0, 10, (1, 2)), 2)
def tn_doc_so(rng):
    n = rng.randint(0, 10)
    return M(f"Số {n} đọc là gì?", doc_so(n), chon3(rng, [doc_so(x) for x in range(11)], doc_so(n)), 1)
def tn_viet_so(rng):
    n = rng.randint(0, 10)
    return M(f"Số \"{doc_so(n)}\" viết là?", n, so_gan(rng, n, 0, 10, (1, 2)), 1)

def tl_dien_dau(rng):
    cap = [rng.sample(range(0, 11), 2) if rng.random() < .8 else [x, x] for x in [rng.randint(0, 10)] * 3]
    cap = [rng.sample(range(0, 11), 2) for _ in range(3)]
    dt = lambda a, b: ">" if a > b else "<" if a < b else "="
    de = "Điền dấu >, <, = thích hợp vào chỗ chấm:\n" + "; ".join(f"{a} ... {b}" for a, b in cap)
    return T(de, "; ".join(f"{a} {dt(a, b)} {b}" for a, b in cap), 1)
def tl_sap_xep(rng):
    d = rng.sample(range(0, 11), 5)
    bd = rng.choice(["bé đến lớn", "lớn đến bé"])
    s = sorted(d, reverse=(bd == "lớn đến bé"))
    return T(f"Sắp xếp các số {', '.join(map(str, d))} theo thứ tự từ {bd}.", ", ".join(map(str, s)), 2)
def tl_lien_ke(rng):
    d = rng.sample(range(1, 10), 3)
    return T("Viết số liền trước và số liền sau của mỗi số: " + ", ".join(map(str, d)) + ".",
             "\n".join(f"Số liền trước của {x} là {x - 1}; số liền sau của {x} là {x + 1}." for x in d), 1)
def tl_so_ban(rng):
    a, b = rng.sample(range(1, 11), 2)
    x, y = hai_ten(rng); v = vat(rng)
    ai = x if a > b else y
    return T(f"{x} có {a} {v}, {y} có {b} {v}. Bạn nào có nhiều {v} hơn? Bạn nào có ít hơn?",
             f"Vì {max(a, b)} > {min(a, b)} nên {ai} có nhiều {v} hơn, {y if ai == x else x} có ít hơn.", 2)
def tl_viet_day(rng):
    a = rng.randint(0, 4); b = a + rng.randint(4, 6)
    return T(f"Viết các số từ {a} đến {b}, rồi khoanh vào số lớn nhất.", f"{', '.join(map(str, range(a, b + 1)))}. Số lớn nhất là {b}.", 1)

# 2. Cộng, trừ trong phạm vi 10 ---------------------------------------------
def tn_cong10(rng):
    a = rng.randint(1, 8); b = rng.randint(1, 10 - a)
    return M(f"{a} + {b} = ?", a + b, so_gan(rng, a + b, 0, 12, (1, 2)), 1)
def tn_tru10(rng):
    a = rng.randint(2, 10); b = rng.randint(1, a)
    return M(f"{a} - {b} = ?", a - b, so_gan(rng, a - b, 0, 10, (1, 2)), 1)
def tn_thieu_cong(rng):
    a = rng.randint(1, 8); c = rng.randint(a + 1, 10)
    return M(f"{a} + ? = {c}", c - a, so_gan(rng, c - a, 0, 10, (1, 2)), 2)
def tn_thieu_tru(rng):
    b = rng.randint(1, 8); c = rng.randint(0, 10 - b)
    return M(f"? - {b} = {c}", b + c, so_gan(rng, b + c, 0, 10, (1, 2)), 2)
def tn_pheptinh_bang(rng):
    k = rng.randint(3, 9)
    x = rng.randint(1, k - 1)
    dung = f"{x} + {k - x}"
    sai = []
    while len(sai) < 3:
        u = rng.randint(1, 8); v = rng.randint(1, 10 - u)
        if u + v != k and f"{u} + {v}" not in sai: sai.append(f"{u} + {v}")
    return M(f"Phép tính nào có kết quả bằng {k}?", dung, sai, 2)
def tn_dem_them(rng):
    a = rng.randint(1, 7); b = rng.randint(1, 10 - a); v = vat(rng)
    return M(f"Có {a} {v}, thêm {b} {v} nữa. Có tất cả bao nhiêu {v}?", a + b, so_gan(rng, a + b, 0, 12, (1, 2)), 2)
def tn_an_bot(rng):
    a = rng.randint(3, 10); b = rng.randint(1, a - 1); v = vat(rng)
    return M(f"Có {a} {v}, lấy đi {b} {v}. Còn lại bao nhiêu {v}?", a - b, so_gan(rng, a - b, 0, 10, (1, 2)), 2)
def tn_so_pt(rng):
    a = rng.randint(1, 5); b = rng.randint(1, 5); c = rng.randint(1, 5); d = rng.randint(1, 5)
    if a + b == c + d: raise ValueError
    dung = ">" if a + b > c + d else "<"
    return M(f"Chọn dấu thích hợp: {a} + {b} ... {c} + {d}", dung, sai_dau(dung), 3)

def tl_tinh_nham(rng):
    ps_ = []
    for _ in range(4):
        if rng.random() < .5:
            a = rng.randint(1, 8); b = rng.randint(1, 10 - a); ps_.append((f"{a} + {b}", a + b))
        else:
            a = rng.randint(2, 10); b = rng.randint(1, a); ps_.append((f"{a} - {b}", a - b))
    return T("Tính nhẩm:\n" + "; ".join(p for p, _ in ps_), "; ".join(f"{p} = {r}" for p, r in ps_), 1)
def tl_dien_so(rng):
    a = rng.randint(1, 8); c = rng.randint(a + 1, 10); d = rng.randint(1, 9); e = rng.randint(0, 10 - d)
    return T(f"Điền số thích hợp vào chỗ chấm:\n{a} + ... = {c}; ... - {d} = {e}",
             f"{a} + {c - a} = {c}; {d + e} - {d} = {e}", 2)
def tl_do_them(rng): return de_them(rng, 1, 5, "ngan")
def tl_do_bot(rng): return de_bot(rng, 1, 5, "ngan")
def tl_do_hop(rng): return de_hop(rng, 1, 5, "ngan")

# 3. Các số đến 100 -----------------------------------------------------------
def tn_chuc_dv(rng):
    n = rng.randint(11, 99)
    if n % 10 == 0: raise ValueError
    c, d = n // 10, n % 10
    dung = f"{c} chục {d} đơn vị"
    sai = [f"{d} chục {c} đơn vị", f"{c} chục {(d + 1) % 10} đơn vị", f"{(c % 9) + 1} chục {d} đơn vị"]
    return M(f"Số {n} gồm mấy chục và mấy đơn vị?", dung, sai, 1)
def tn_ghep_so(rng):
    c = rng.randint(1, 9); d = rng.randint(1, 9)
    n = c * 10 + d
    return M(f"Số gồm {c} chục và {d} đơn vị là số nào?", n, [d * 10 + c, n + 10 if c < 9 else n - 10, n + 1 if d < 9 else n - 1], 1)
def tn_lien_sau100(rng):
    a = rng.randint(10, 98)
    return M(f"Số liền sau của {a} là số nào?", a + 1, so_gan(rng, a + 1, 0, 100, (1, 2, 10)), 1)
def tn_lien_truoc100(rng):
    a = rng.randint(11, 99)
    return M(f"Số liền trước của {a} là số nào?", a - 1, so_gan(rng, a - 1, 0, 100, (1, 2, 10)), 1)
def tn_chuc_cua(rng):
    n = rng.randint(21, 98)
    return M(f"Chữ số hàng chục của số {n} là chữ số nào?", n // 10, chon3(rng, [n % 10, n // 10 + 1, n // 10 - 1, 0], n // 10), 1)
def tn_lon_nhat100(rng):
    d = rng.sample(range(10, 100), 4)
    m = max(d)
    return M(f"Số nào lớn nhất trong các số {', '.join(map(str, d))}?", m, [x for x in d if x != m], 2)
def tn_tron_chuc(rng):
    k = rng.randint(1, 9) * 10
    nhieu = [k + rng.randint(1, 9) for _ in range(3)]
    return M("Số nào dưới đây là số tròn chục?", k, nhieu, 1)
def tn_doc100(rng):
    n = rng.randint(21, 99)
    return M(f"Số {n} đọc là gì?", doc_so(n), chon3(rng, [doc_so(n + k) for k in (-10, -1, 1, 9, 10, -9)], doc_so(n)), 2)

def tl_phan_tich(rng):
    d = rng.sample(range(11, 100), 3)
    d = [x for x in d if x % 10]
    if len(d) < 3: raise ValueError
    return T("Viết (theo mẫu 35 = 30 + 5) các số: " + ", ".join(map(str, d)) + ".",
             "\n".join(f"{x} = {x // 10 * 10} + {x % 10}" for x in d), 2)
def tl_chuc_dv(rng):
    d = rng.sample(range(11, 100), 3)
    return T("Viết các số sau thành \"... chục ... đơn vị\": " + ", ".join(map(str, d)) + ".",
             "\n".join(f"{x} gồm {x // 10} chục {x % 10} đơn vị" for x in d), 1)
def tl_sap_xep100(rng):
    d = rng.sample(range(1, 100), 5)
    bd = rng.choice(["bé đến lớn", "lớn đến bé"])
    return T(f"Sắp xếp các số {', '.join(map(str, d))} theo thứ tự từ {bd}.", ", ".join(map(str, sorted(d, reverse=bd == 'lớn đến bé'))), 2)
def tl_dau100(rng):
    cap = [rng.sample(range(10, 100), 2) for _ in range(3)]
    dt = lambda a, b: ">" if a > b else "<"
    return T("Điền dấu >, < thích hợp vào chỗ chấm:\n" + "; ".join(f"{a} ... {b}" for a, b in cap),
             "; ".join(f"{a} {dt(a, b)} {b}" for a, b in cap), 1)
def tl_doc_viet(rng):
    d = rng.sample(range(21, 100), 3)
    return T("Viết các số sau bằng chữ: " + ", ".join(map(str, d)) + ".", "\n".join(f"{x}: {doc_so(x)}" for x in d), 2)

# 4. Cộng, trừ trong phạm vi 20 -------------------------------------------------
def tn_cong20(rng):
    a = rng.randint(2, 9); b = rng.randint(11 - a, 9)
    return M(f"{a} + {b} = ?", a + b, so_gan(rng, a + b, 0, 20, (1, 2, 10)), 1)
def tn_tru20(rng):
    a = rng.randint(11, 18); b = rng.randint(a % 10 + 1, 9)
    return M(f"{a} - {b} = ?", a - b, so_gan(rng, a - b, 0, 20, (1, 2, 10)), 1)
def tn_thieu20(rng):
    a = rng.randint(3, 9); c = rng.randint(11, 18)
    if c - a > 9: raise ValueError
    return M(f"{a} + ? = {c}", c - a, so_gan(rng, c - a, 0, 20, (1, 2)), 2)
def tn_thieu_tru20(rng):
    b = rng.randint(2, 9); c = rng.randint(2, 9)
    return M(f"? - {b} = {c}", b + c, so_gan(rng, b + c, 0, 20, (1, 2, 10)), 2)
def tn_dung20(rng):
    a = rng.randint(2, 9); b = rng.randint(11 - a, 9)
    dung = f"{a} + {b} = {a + b}"
    sai = [f"{a} + {b} = {a + b + 1}", f"{a} + {b} = {a + b - 1}", f"{a} + {b} = {a + b + 10}"]
    return M("Phép tính nào dưới đây đúng?", dung, sai, 2)
def tn_ba_so(rng):
    a = rng.randint(1, 8); b = rng.randint(1, 8); c = rng.randint(1, 9)
    if a + b + c > 20: raise ValueError
    return M(f"{a} + {b} + {c} = ?", a + b + c, so_gan(rng, a + b + c, 0, 20, (1, 2, 10)), 3)
def tn_dem20(rng):
    a = rng.randint(8, 12); b = rng.randint(3, 8); v = vat(rng)
    return M(f"Lớp có {a} {v}, thêm {b} {v}. Lớp có tất cả bao nhiêu {v}?", a + b, so_gan(rng, a + b, 0, 20, (1, 2, 10)), 2)

def tl_tinh20(rng):
    ps_ = []
    for _ in range(4):
        if rng.random() < .5:
            a = rng.randint(2, 9); b = rng.randint(11 - a, 9); ps_.append((f"{a} + {b}", a + b))
        else:
            a = rng.randint(11, 18); b = rng.randint(a % 10 + 1, 9); ps_.append((f"{a} - {b}", a - b))
    return T("Tính:\n" + "; ".join(p for p, _ in ps_), "; ".join(f"{p} = {r}" for p, r in ps_), 1)
def tl_20_them(rng): return de_them(rng, 6, 12, "ngan")
def tl_20_bot(rng): return de_bot(rng, 3, 9, "ngan")
def tl_20_hop(rng): return de_hop(rng, 6, 12, "ngan")
def tl_ba_so(rng):
    a = rng.randint(1, 8); b = rng.randint(1, 8); c = rng.randint(1, 9)
    if a + b + c > 20: raise ValueError
    return T(f"Tính: {a} + {b} + {c} = ?", f"{a} + {b} = {a + b}; {a + b} + {c} = {a + b + c}. Vậy {a} + {b} + {c} = {a + b + c}", 2)

# 5. Cộng, trừ không nhớ trong phạm vi 100 -------------------------------------
def _cong_khong_nho(rng):
    a = rng.randint(1, 8) * 10 + rng.randint(0, 8); b = rng.randint(1, 9 - a // 10) * 10 + rng.randint(0, 9 - a % 10)
    return a, b
def tn_cong100(rng):
    a, b = _cong_khong_nho(rng)
    return M(f"{a} + {b} = ?", a + b, so_gan(rng, a + b, 0, 100, (1, 10, 2)), 1)
def tn_tru100(rng):
    a = rng.randint(2, 9) * 10 + rng.randint(1, 9); b = rng.randint(1, a // 10 - 1) * 10 + rng.randint(0, a % 10)
    return M(f"{a} - {b} = ?", a - b, so_gan(rng, a - b, 0, 100, (1, 10, 2)), 1)
def tn_chuc_tron(rng):
    a = rng.randint(1, 4) * 10; b = rng.randint(1, 9 - a // 10 + 1) * 10
    if a + b > 90: raise ValueError
    return M(f"{a} + {b} = ?", a + b, so_gan(rng, a + b, 0, 100, (10, 1)), 1)
def tn_thieu100(rng):
    a, b = _cong_khong_nho(rng)
    return M(f"{a} + ? = {a + b}", b, so_gan(rng, b, 0, 99, (1, 10, 2)), 2)
def tn_dem100(rng):
    a, b = _cong_khong_nho(rng); v = vat(rng)
    return M(f"Có {a} {v}, mua thêm {b} {v}. Có tất cả bao nhiêu {v}?", a + b, so_gan(rng, a + b, 0, 100, (1, 10)), 2)
def tn_lop100(rng):
    a = rng.randint(4, 9) * 10 + rng.randint(1, 9); b = rng.randint(1, a // 10 - 1) * 10 + rng.randint(0, a % 10); v = vat(rng)
    return M(f"Có {a} {v}, bớt đi {b} {v}. Còn lại bao nhiêu {v}?", a - b, so_gan(rng, a - b, 0, 100, (1, 10)), 2)
def tn_so_pt100(rng):
    a, b = _cong_khong_nho(rng); c, d = _cong_khong_nho(rng)
    if a + b == c + d: raise ValueError
    d_ = ">" if a + b > c + d else "<"
    return M(f"Chọn dấu thích hợp: {a} + {b} ... {c} + {d}", d_, sai_dau(d_), 3)

def tl_dat_tinh(rng):
    ps_ = []
    for _ in range(4):
        if rng.random() < .5:
            a, b = _cong_khong_nho(rng); ps_.append((f"{a} + {b}", a + b))
        else:
            a = rng.randint(2, 9) * 10 + rng.randint(1, 9); b = rng.randint(1, a // 10 - 1) * 10 + rng.randint(0, a % 10)
            ps_.append((f"{a} - {b}", a - b))
    return T("Đặt tính rồi tính:\n" + "; ".join(p for p, _ in ps_), "; ".join(f"{p} = {r}" for p, r in ps_), 1)
def tl_100_them(rng): return de_them(rng, 10, 45, "ngan")
def tl_100_hop(rng): return de_hop(rng, 10, 45, "ngan")
def tl_100_bot(rng): return de_bot(rng, 10, 45, "ngan")
def tl_100_it(rng): return de_it(rng, 10, 45, "ngan")

# 6. Đo độ dài và xem giờ ------------------------------------------------------
def tn_ngay_mai(rng):
    i = rng.randint(0, 6)
    return M(f"Hôm nay là {THU[i].lower()}. Ngày mai là thứ mấy?", THU[(i + 1) % 7], [THU[(i + k) % 7] for k in (2, 6, 3)], 1)
def tn_hom_qua(rng):
    i = rng.randint(0, 6)
    return M(f"Hôm qua là {THU[i].lower()}. Hôm nay là thứ mấy?", THU[(i + 1) % 7], [THU[(i + k) % 7] for k in (2, 6, 3)], 2)
def tn_dong_ho(rng):
    h = rng.randint(1, 12)
    return M(f"Đồng hồ có kim ngắn chỉ số {h}, kim dài chỉ số 12. Đồng hồ chỉ mấy giờ?", f"{h} giờ",
             [f"{(h + k - 1) % 12 + 1} giờ" for k in (1, 3, 5)], 1)
def tn_day_cat(rng):
    a = rng.randint(10, 20); b = rng.randint(2, a - 1)
    return M(f"Sợi dây dài {a} cm, cắt đi {b} cm. Sợi dây còn lại dài bao nhiêu xăng-ti-mét?", f"{a - b} cm", [f"{x} cm" for x in so_gan(rng, a - b, 1, 30, (1, 2, 10))], 2)
def tn_dai_hon(rng):
    a, b = rng.sample(range(5, 25), 2)
    dung = "Bút chì" if a > b else "Bút mực"
    return M(f"Bút chì dài {a} cm, bút mực dài {b} cm. Bút nào dài hơn?", dung,
             ["Bút mực" if a > b else "Bút chì", "Hai bút dài bằng nhau", "Không so sánh được"], 1)
def tn_tuan(rng):
    return M("Một tuần lễ có mấy ngày?", "7 ngày", ["5 ngày", "6 ngày", "10 ngày"], 1)
def tn_cm_noi(rng):
    a = rng.randint(2, 9); b = rng.randint(2, 9)
    return M(f"Đoạn thẳng AB dài {a} cm, đoạn thẳng BC dài {b} cm. Hai đoạn thẳng nối liền nhau dài tất cả bao nhiêu xăng-ti-mét?", f"{a + b} cm",
             [f"{x} cm" for x in so_gan(rng, a + b, 1, 30, (1, 2))], 2)
def tn_sau_ngay(rng):
    i = rng.randint(0, 6); k = rng.randint(2, 4)
    return M(f"Hôm nay là {THU[i].lower()}. Sau {k} ngày nữa là thứ mấy?", THU[(i + k) % 7], [THU[(i + k + d) % 7] for d in (1, -1, 2)], 3)

def tl_day_noi(rng):
    a = rng.randint(5, 20); b = rng.randint(5, 20)
    return T(f"Đoạn dây xanh dài {a} cm, đoạn dây đỏ dài {b} cm. Hỏi hai đoạn dây dài tất cả bao nhiêu xăng-ti-mét?",
             f"Phép tính: {a} + {b} = {a + b}\nTrả lời: Hai đoạn dây dài tất cả {a + b} cm.", 1)
def tl_day_cat(rng):
    b = rng.randint(3, 12); a = b + rng.randint(3, 15)
    return T(f"Một sợi dây dài {a} cm, cắt đi {b} cm. Hỏi sợi dây còn lại dài bao nhiêu xăng-ti-mét?",
             f"Phép tính: {a} - {b} = {a - b}\nTrả lời: Sợi dây còn lại dài {a - b} cm.", 1)
def tl_thu(rng):
    i = rng.randint(0, 6); k = rng.randint(2, 5)
    return T(f"Hôm nay là {THU[i].lower()}. Hỏi sau {k} ngày nữa là thứ mấy? Viết tên các thứ lần lượt từ ngày mai.",
             "Lần lượt: " + ", ".join(THU[(i + j) % 7] for j in range(1, k + 1)) + f".\nVậy sau {k} ngày nữa là {THU[(i + k) % 7].lower()}.", 2)
def tl_gio(rng):
    h = rng.randint(1, 9); k = rng.randint(1, 3)
    return T(f"Lúc {h} giờ mẹ bắt đầu nấu cơm. Sau {k} giờ thì cơm chín. Hỏi cơm chín lúc mấy giờ?",
             f"Phép tính: {h} + {k} = {h + k}\nTrả lời: Cơm chín lúc {h + k} giờ.", 2)
def tl_so_thuoc(rng):
    a, b = rng.sample(range(8, 30), 2)
    return T(f"Bút chì dài {a} cm, bút mực dài {b} cm. Bút nào dài hơn và dài hơn bao nhiêu xăng-ti-mét?",
             f"Vì {max(a,b)} > {min(a,b)} nên {'bút chì' if a > b else 'bút mực'} dài hơn.\nPhép tính: {max(a,b)} - {min(a,b)} = {abs(a - b)}\nTrả lời: Dài hơn {abs(a - b)} cm.", 2)

# 7. Hình học -------------------------------------------------------------
_SH = {"hình tam giác": (3, 3), "hình vuông": (4, 4), "hình chữ nhật": (4, 4)}
def tn_hinh_canh(rng):
    h = rng.choice(list(_SH))
    return M(f"{h.capitalize()} có mấy cạnh?", _SH[h][0], [x for x in (3, 4, 5, 0, 6) if x != _SH[h][0]][:3], 1)
def tn_hinh_dinh(rng):
    h = rng.choice(list(_SH))
    return M(f"{h.capitalize()} có mấy đỉnh?", _SH[h][1], [x for x in (3, 4, 5, 0, 6) if x != _SH[h][1]][:3], 1)
def tn_hinh_nao3(rng):
    return M("Hình nào có 3 cạnh?", "Hình tam giác", ["Hình vuông", "Hình tròn", "Hình chữ nhật"], 1)
def tn_hinh_bang(rng):
    return M("Hình nào có 4 cạnh bằng nhau?", "Hình vuông", ["Hình tam giác", "Hình tròn", "Hình chữ nhật"], 2)
def tn_khong_canh(rng):
    return M("Hình nào không có cạnh và không có đỉnh?", "Hình tròn", ["Hình tam giác", "Hình vuông", "Hình chữ nhật"], 1)
def tn_do_vat(rng):
    cap = [("Mặt đồng hồ treo tường", "hình tròn"), ("Mặt bàn học (phần lớn)", "hình chữ nhật"), ("Biển báo cấm đỗ xe", "hình tròn"),
           ("Tờ giấy ô vuông gập đôi theo đường chéo cho ra", "hình tam giác"), ("Viên gạch lát nền", "hình vuông"), ("Cái đĩa", "hình tròn")]
    dv, h = rng.choice(cap)
    return M(f"{dv} có dạng hình gì?", h.capitalize(), [x.capitalize() for x in ("hình tam giác", "hình vuông", "hình tròn", "hình chữ nhật") if x != h][:3], 2)
def tn_dem_hinh(rng):
    a = rng.randint(2, 9); b = rng.randint(2, 9)
    return M(f"Có {a} hình tam giác và {b} hình vuông. Có tất cả bao nhiêu hình?", a + b, so_gan(rng, a + b, 0, 30, (1, 2)), 1)
def tn_canh_nhieu(rng):
    n = rng.randint(2, 5)
    return M(f"Mỗi hình tam giác có 3 cạnh. {n} hình tam giác có tất cả bao nhiêu cạnh?", 3 * n, so_gan(rng, 3 * n, 0, 30, (1, 2, 3)), 3)
def tn_dinh_nhieu(rng):
    n = rng.randint(2, 5)
    return M(f"Mỗi hình vuông có 4 đỉnh. {n} hình vuông có tất cả bao nhiêu đỉnh?", 4 * n, so_gan(rng, 4 * n, 0, 30, (1, 2, 4)), 3)

def tl_ke_ten(rng):
    h = rng.choice(["tròn", "vuông", "chữ nhật", "tam giác"]); k = rng.choice([2, 3])
    ex = {"tròn": "mặt đồng hồ, cái đĩa, bánh xe, đồng xu", "vuông": "viên gạch lát nền, ô cửa sổ, khăn tay, bàn cờ",
          "chữ nhật": "cuốn vở, cánh cửa, mặt bàn, màn hình ti vi", "tam giác": "khăn quàng đỏ, mái nhà, cờ đuôi nheo, ê ke"}[h]
    return T(f"Kể tên {k} đồ vật có dạng hình {h}.", f"Ví dụ: {ex}. (Chọn {k} đồ vật bất kì cho đúng).", 1)
def tl_dem_hinh(rng):
    a = rng.randint(2, 9); b = rng.randint(2, 9); c = rng.randint(2, 9)
    return T(f"Trên bảng có {a} hình tròn, {b} hình vuông và {c} hình tam giác. Hỏi trên bảng có tất cả bao nhiêu hình?",
             f"Phép tính: {a} + {b} + {c} = {a + b + c}\nTrả lời: Có tất cả {a + b + c} hình.", 2)
def tl_canh(rng):
    n = rng.randint(2, 5)
    return T(f"Mỗi hình tam giác có 3 cạnh. Hỏi {n} hình tam giác có tất cả bao nhiêu cạnh?",
             f"Phép tính: {' + '.join(['3'] * n)} = {3 * n}\nTrả lời: {n} hình tam giác có tất cả {3 * n} cạnh.", 2)
def tl_dinh(rng):
    n = rng.randint(2, 5)
    return T(f"Mỗi hình vuông có 4 đỉnh. Hỏi {n} hình vuông có tất cả bao nhiêu đỉnh?",
             f"Phép tính: {' + '.join(['4'] * n)} = {4 * n}\nTrả lời: {n} hình vuông có tất cả {4 * n} đỉnh.", 2)
def tl_nhieu_it(rng):
    a = rng.randint(5, 15); b = rng.randint(3, 12)
    ten = "hình vuông" if a >= b else "hình tam giác"
    return T(f"Có {a} hình vuông và {b} hình tam giác. Hình nào nhiều hơn? Nhiều hơn bao nhiêu hình?",
             f"Vì {max(a,b)} > {min(a,b)} nên {ten} nhiều hơn.\nPhép tính: {max(a,b)} - {min(a,b)} = {abs(a-b)}\nTrả lời: Nhiều hơn {abs(a-b)} hình.", 2)

CHU_DE = [
    ("Các số đến 10", [tn_lien_sau, tn_lien_truoc, tn_so_sanh, tn_lon_nhat, tn_be_nhat, tn_o_giua, tn_doc_so, tn_viet_so],
     [tl_dien_dau, tl_sap_xep, tl_lien_ke, tl_so_ban, tl_viet_day]),
    ("Cộng, trừ trong phạm vi 10", [tn_cong10, tn_tru10, tn_thieu_cong, tn_thieu_tru, tn_pheptinh_bang, tn_dem_them, tn_an_bot, tn_so_pt],
     [tl_tinh_nham, tl_dien_so, tl_do_them, tl_do_bot, tl_do_hop]),
    ("Các số đến 100", [tn_chuc_dv, tn_ghep_so, tn_lien_sau100, tn_lien_truoc100, tn_chuc_cua, tn_lon_nhat100, tn_tron_chuc, tn_doc100],
     [tl_phan_tich, tl_chuc_dv, tl_sap_xep100, tl_dau100, tl_doc_viet]),
    ("Cộng, trừ trong phạm vi 20", [tn_cong20, tn_tru20, tn_thieu20, tn_thieu_tru20, tn_dung20, tn_ba_so, tn_dem20],
     [tl_tinh20, tl_20_them, tl_20_bot, tl_20_hop, tl_ba_so]),
    ("Cộng, trừ không nhớ trong phạm vi 100", [tn_cong100, tn_tru100, tn_chuc_tron, tn_thieu100, tn_dem100, tn_lop100, tn_so_pt100],
     [tl_dat_tinh, tl_100_them, tl_100_hop, tl_100_bot, tl_100_it]),
    ("Xem giờ, ngày trong tuần và độ dài (cm)", [tn_ngay_mai, tn_hom_qua, tn_dong_ho, tn_day_cat, tn_dai_hon, tn_tuan, tn_cm_noi, tn_sau_ngay],
     [tl_day_noi, tl_day_cat, tl_thu, tl_gio, tl_so_thuoc]),
    ("Hình vuông, hình tròn, hình tam giác, hình chữ nhật", [tn_hinh_canh, tn_hinh_dinh, tn_hinh_nao3, tn_hinh_bang, tn_khong_canh, tn_do_vat, tn_dem_hinh, tn_canh_nhieu, tn_dinh_nhieu],
     [tl_ke_ten, tl_dem_hinh, tl_canh, tl_dinh, tl_nhieu_it]),
]
