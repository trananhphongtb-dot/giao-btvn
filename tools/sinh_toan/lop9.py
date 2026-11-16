from thcs import *
import math

def nz(rng, lo=-6, hi=6): return rng.choice([x for x in range(lo, hi + 1) if x])
def can(n):
    """√n dạng a√b."""
    a, b = 1, n
    for k in range(math.isqrt(n), 1, -1):
        if n % (k * k) == 0: a, b = k, n // (k * k); break
    return str(a) if b == 1 else (f"√{b}" if a == 1 else f"{a}√{b}")
def nhieu_can(rng, a, b, dung):
    c = [f"{a + 1}√{b}", f"{max(a - 1, 1)}√{b}", f"{a}√{b + 1}", f"{a * 2}√{b}", f"{a}√{max(b - 1, 2)}"]
    return chon3(rng, c, dung)

# ============ 1. Phương trình và hệ phương trình bậc nhất hai ẩn ============
def a1_nghiem(rng):
    x, y = rng.randint(-4, 5), rng.randint(-4, 5); a, b = nz(rng, -4, 4), nz(rng, -4, 4); c = a * x + b * y
    return M(f"Cặp số nào là nghiệm của phương trình {da2({(1, 0): a, (0, 1): b})} = {c}?", f"({x}; {y})", [f"({x + 1}; {y})", f"({x}; {y + 1})", f"({y}; {x})" if x != y else f"({x - 1}; {y - 1})"], 1)
def a1_he(rng):
    x, y = rng.randint(-3, 5), rng.randint(-3, 5)
    while True:
        a1, b1, a2, b2 = nz(rng, -4, 4), nz(rng, -4, 4), nz(rng, -4, 4), nz(rng, -4, 4)
        if a1 * b2 - a2 * b1 != 0: break
    c1, c2 = a1 * x + b1 * y, a2 * x + b2 * y
    return M(f"Nghiệm của hệ phương trình {{{da2({(1, 0): a1, (0, 1): b1})} = {c1}; {da2({(1, 0): a2, (0, 1): b2})} = {c2}}} là:", f"({x}; {y})", [f"({x + 1}; {y})", f"({x}; {y - 1})", f"({y}; {x})" if x != y else f"({x + 2}; {y})"], 2)
def a1_he2(rng):
    x, y = rng.randint(-3, 5), rng.randint(-3, 5); s, d = x + y, x - y
    return nint(rng, f"Hệ {{x + y = {s}; x - y = {d}}} có nghiệm (x; y). Giá trị của x là:", x, 2, (1, 2, 3))
def a1_he3(rng):
    x, y = rng.randint(-3, 5), rng.randint(-3, 5); s, d = x + y, x - y
    return nint(rng, f"Hệ {{x + y = {s}; x - y = {d}}} có nghiệm (x; y). Giá trị của y là:", y, 2, (1, 2, 3))
def a1_vo(rng):
    a, b, c = rng.randint(1, 4), rng.randint(1, 4), rng.randint(1, 6); k = rng.randint(2, 3)
    return M(f"Hệ {{{a}x + {b}y = {c}; {a * k}x + {b * k}y = {c * k}}} có bao nhiêu nghiệm?", "Vô số nghiệm", ["Một nghiệm duy nhất", "Vô nghiệm", "Đúng hai nghiệm"], 3)
def a1_vn(rng):
    a, b, c = rng.randint(1, 4), rng.randint(1, 4), rng.randint(1, 6); k = rng.randint(2, 3)
    return M(f"Hệ {{{a}x + {b}y = {c}; {a * k}x + {b * k}y = {c * k + 1}}} có bao nhiêu nghiệm?", "Vô nghiệm", ["Một nghiệm duy nhất", "Vô số nghiệm", "Đúng hai nghiệm"], 3)
def a1_bac1(rng):
    a, b, c = nz(rng, -5, 5), nz(rng, -5, 5), rng.randint(-8, 8)
    return M(f"Phương trình nào là phương trình bậc nhất hai ẩn?", f"{da2({(1, 0): a, (0, 1): b})} = {c}", [f"x² + y = {c}", f"{a}x + {b}y² = {c}", f"{a}/x + y = {c}"], 1)
def a1_thuoc(rng):
    a, b, c = nz(rng, -4, 4), nz(rng, -4, 4), rng.randint(-8, 8); x = rng.randint(-3, 3); y = (c - a * x) / b
    if y != int(y): raise ValueError
    y = int(y); return M(f"Với x = {x}, phương trình {da2({(1, 0): a, (0, 1): b})} = {c} cho y bằng:", y, [y + 1, y - 1, -y if y else 2], 2)
def a1_toanloi(rng):
    x, y = rng.randint(3, 15), rng.randint(3, 15); t = x + y; hieu = x - y
    if hieu == 0: raise ValueError
    return nint(rng, f"Tổng của hai số là {t}, hiệu của chúng là {hieu}. Số lớn là:", max(x, y) if hieu > 0 else max(x, y), 2, (1, 2, 3), 0) if hieu > 0 else (_ for _ in ()).throw(ValueError)
def a1_gia(rng):
    a, b = rng.randint(5, 20), rng.randint(5, 20); x, y = rng.randint(2, 6), rng.randint(2, 6)
    if a == b: raise ValueError
    return nint(rng, f"Mua {x} quyển vở và {y} cây bút hết {a * x + b * y} nghìn đồng; biết một quyển vở giá {a} nghìn đồng. Giá một cây bút là (nghìn đồng):", b, 3, (1, 2, 3), 0)
def a1_cong(rng):
    x, y = rng.randint(-3, 5), rng.randint(-3, 5); a = rng.randint(2, 4)
    return nint(rng, f"Hệ {{{a}x + y = {a * x + y}; x - y = {x - y}}}. Cộng hai phương trình theo vế ta được {a + 1}x = ? Giá trị vế phải là:", a * x + y + x - y, 3, (1, 2, 3))
def b1_he(rng):
    x, y = rng.randint(-3, 5), rng.randint(-3, 5)
    while True:
        a1, b1, a2, b2 = nz(rng, -4, 4), nz(rng, -4, 4), nz(rng, -4, 4), nz(rng, -4, 4)
        if a1 * b2 - a2 * b1 != 0: break
    c1, c2 = a1 * x + b1 * y, a2 * x + b2 * y
    return T(f"Giải hệ phương trình {{{da2({(1, 0): a1, (0, 1): b1})} = {c1}; {da2({(1, 0): a2, (0, 1): b2})} = {c2}}}.", f"Dùng phương pháp thế hoặc cộng đại số, tìm được nghiệm duy nhất (x; y) = ({x}; {y}).", 2)
def b1_loi(rng):
    x, y = rng.randint(5, 20), rng.randint(5, 20)
    if x == y: raise ValueError
    return T(f"Tìm hai số biết tổng của chúng bằng {x + y} và hiệu của chúng bằng {abs(x - y)}.", f"Gọi hai số là a, b: a + b = {x + y}, a - b = {abs(x - y)}.\nCộng hai vế: 2a = {x + y + abs(x - y)} ⇒ a = {max(x, y)}; b = {min(x, y)}.", 2)
def b1_dg(rng):
    return T("Nêu các bước giải bài toán bằng cách lập hệ phương trình.", "Bước 1: Chọn ẩn, đặt điều kiện. Bước 2: Lập hệ phương trình từ các dữ kiện. Bước 3: Giải hệ. Bước 4: Đối chiếu điều kiện và kết luận.", 1)
def b1_toan(rng):
    a, b = rng.randint(2, 6), rng.randint(2, 6); x, y = rng.randint(3, 10), rng.randint(3, 10)
    if a == b: raise ValueError
    return T(f"Hai loại bút: loại I giá {a} nghìn đồng, loại II giá {b} nghìn đồng. Mua tổng cộng {x + y} chiếc hết {a * x + b * y} nghìn đồng. Hỏi mỗi loại mua bao nhiêu chiếc?", f"Gọi số bút loại I là x, loại II là y: x + y = {x + y}; {a}x + {b}y = {a * x + b * y}.\nGiải ra x = {x}, y = {y}.", 3)
def b1_hv(rng):
    a, b = rng.randint(3, 12), rng.randint(2, 9)
    if a == b: raise ValueError
    return T(f"Hình chữ nhật có nửa chu vi {a + b} cm và chiều dài hơn chiều rộng {a - b} cm. Tính hai kích thước và diện tích.", f"Dài + rộng = {a + b}; dài - rộng = {a - b} ⇒ dài = {a} cm, rộng = {b} cm.\nDiện tích = {a}·{b} = {a * b} cm².", 2)
def b1_kt(rng):
    x, y = rng.randint(-3, 5), rng.randint(-3, 5); a, b = rng.randint(1, 4), rng.randint(1, 4)
    return T(f"Kiểm tra xem cặp số ({x}; {y}) có là nghiệm của phương trình {a}x + {b}y = {a * x + b * y} không?", f"Thay x = {x}, y = {y}: {a}·({x}) + {b}·({y}) = {a * x + b * y}. Đúng nên ({x}; {y}) là nghiệm.", 1)

# ============ 2. Phương trình và bất phương trình bậc nhất một ẩn ============
def a2_pt(rng):
    a, x = nz(rng, -6, 6), rng.randint(-6, 8); b = rng.randint(-9, 9); return nint(rng, f"Nghiệm của phương trình {da([a, b])} = {a * x + b} là:", x, 1, (1, 2, 3))
def a2_tich(rng):
    a, b = rng.randint(1, 6), rng.randint(1, 6); return M(f"Tập nghiệm của phương trình (x - {a})(x + {b}) = 0 là:", f"{{{a}; -{b}}}", [f"{{-{a}; {b}}}", f"{{{a}; {b}}}", f"{{-{a}; -{b}}}"], 2)
def a2_mau(rng):
    a = rng.randint(1, 6); x = rng.randint(2, 9); k = rng.randint(2, 5)
    return M(f"Điều kiện xác định của phương trình {k}/(x - {a}) = 1 là:", f"x ≠ {a}", [f"x ≠ -{a}", f"x ≠ {k}", f"x ≠ 0"], 2)
def a2_bpt(rng):
    a, c = rng.randint(2, 6), rng.randint(2, 20); b = rng.randint(-5, 8); d = c * a + b
    return M(f"Nghiệm của bất phương trình {a}x + {b} < {d} là:", f"x < {c}", [f"x > {c}", f"x ≤ {c}", f"x ≥ {c}"], 2)
def a2_bpt2(rng):
    a, c = rng.randint(2, 6), rng.randint(2, 15); return M(f"Nghiệm của bất phương trình -{a}x > -{a * c} là:", f"x < {c}", [f"x > {c}", f"x < -{c}", f"x > -{c}"], 3)
def a2_bpt3(rng):
    a, c = rng.randint(2, 6), rng.randint(-6, 9); b = rng.randint(1, 9); return M(f"Nghiệm của bất phương trình {a}x - {b} ≥ {a * c - b} là:", f"x ≥ {c}", [f"x ≤ {c}", f"x > {c}", f"x < {c}"], 2)
def a2_nghiem(rng):
    c = rng.randint(2, 9); return M(f"Số nào là nghiệm của bất phương trình x < {c}?", c - 1, [c, c + 1, c + 2], 1)
def a2_dau(rng):
    return M("Khi nhân hai vế của một bất đẳng thức với một số âm thì:", "Đổi chiều bất đẳng thức", ["Giữ nguyên chiều", "Đổi thành dấu bằng", "Không thực hiện được"], 1)
def a2_cong(rng):
    return M("Nếu a < b thì a + c ... b + c (c là số bất kì). Dấu thích hợp là:", "<", [">", "=", "≥"], 1)
def a2_nguyen(rng):
    c = rng.randint(3, 12); return nint(rng, f"Số nghiệm nguyên dương của bất phương trình x < {c} là:", c - 1, 2, (1, 2), 0)
def a2_maxn(rng):
    a, c = rng.randint(2, 6), rng.randint(3, 20); return nint(rng, f"Số nguyên lớn nhất thỏa mãn {a}x < {a * c} là:", c - 1, 2, (1, 2), 0)
def a2_loi(rng):
    a, b = rng.randint(5, 15), rng.randint(50, 100); n = b // a; return nint(rng, f"Một người có {b} nghìn đồng, mua các quyển vở giá {a} nghìn đồng một quyển. Mua tối đa bao nhiêu quyển?", n, 2, (1, 2), 0)
def b2_pt(rng):
    a, b, c, x = rng.randint(2, 6), rng.randint(1, 8), rng.randint(1, 5), rng.randint(-5, 8)
    if a == c: raise ValueError
    return T(f"Giải phương trình {a}x + {b} = {c}x + {a * x + b - c * x}.", f"({a} - {c})x = {a * x + b - c * x} - {b} ⇒ x = {x}", 2)
def b2_bpt(rng):
    a, c = rng.randint(2, 6), rng.randint(2, 15); b = rng.randint(-5, 8)
    return T(f"Giải bất phương trình {a}x + {b} < {a * c + b} và biểu diễn nghiệm trên trục số.", f"{a}x < {a * c} ⇒ x < {c}\nBiểu diễn: tia gốc {c}, bỏ điểm {c}, hướng về phía trái.", 2)
def b2_loi(rng):
    a, b = rng.randint(20, 60), rng.randint(5, 15); n = rng.randint(3, 8)
    return T(f"Một xưởng sản xuất mỗi ngày làm {b} sản phẩm; cần ít nhất {a} sản phẩm. Hỏi cần ít nhất bao nhiêu ngày?", f"{b}x ≥ {a} ⇒ x ≥ {a / b:.1f}\nVậy cần ít nhất {math.ceil(a / b)} ngày.".replace(".", ","), 2)
def b2_mau(rng):
    a = rng.randint(2, 6)
    return T(f"Giải phương trình 1/(x - {a}) = 2/(x + {a}) (đặt điều kiện xác định).", f"ĐKXĐ: x ≠ {a}, x ≠ -{a}. Quy đồng: x + {a} = 2(x - {a}) ⇒ x = {3 * a} (thỏa mãn).", 3)
def b2_ss(rng):
    return T("So sánh 3a + 5 và 3b + 5 nếu a > b. Giải thích.", "Vì a > b nên 3a > 3b (nhân hai vế với 3 > 0); cộng thêm 5 hai vế: 3a + 5 > 3b + 5.", 1)
def b2_he(rng):
    a, b = rng.randint(1, 5), rng.randint(6, 12)
    return T(f"Giải hệ bất phương trình {{x > {a}; x < {b}}} và liệt kê các nghiệm nguyên.", f"{a} < x < {b}; nghiệm nguyên: " + ", ".join(str(x) for x in range(a + 1, b)), 2)

# ============ 3. Căn bậc hai và căn bậc ba ============
def a3_cbh(rng):
    k = rng.randint(2, 20); return nint(rng, f"Căn bậc hai số học của {k * k} là:", k, 1, (1, 2, 3), 0)
def a3_cbh3(rng):
    k = rng.randint(2, 9); return nint(rng, f"Căn bậc ba của {k ** 3} là:", k, 1, (1, 2, 3), 0)
def a3_cbh3_am(rng):
    k = rng.randint(2, 6); return nint(rng, f"Giá trị của ∛(-{k ** 3}) là:", -k, 2, (1, 2, 3))
def a3_dk(rng):
    a = rng.randint(1, 9); return M(f"Điều kiện xác định của √(x - {a}) là:", f"x ≥ {a}", [f"x > {a}", f"x ≤ {a}", f"x ≥ -{a}"], 1)
def a3_dk2(rng):
    a = rng.randint(1, 9); return M(f"Điều kiện xác định của √({a} - x) là:", f"x ≤ {a}", [f"x ≥ {a}", f"x < {a}", f"x ≤ -{a}"], 1)
def a3_dua(rng):
    n = rng.choice([x for x in range(8, 100) if math.isqrt(x) ** 2 != x and can(x) != f"√{x}"]); a = int(can(n).split("√")[0] or 1) if can(n)[0].isdigit() else 1
    return M(f"Đưa √{n} về dạng a√b (b không chứa thừa số chính phương), ta được:", can(n), nhieu_can(rng, a, n // (a * a), can(n)), 2)
def a3_cong(rng):
    a, b, c = rng.randint(2, 9), rng.randint(2, 9), rng.choice([2, 3, 5, 7]); return M(f"{a}√{c} + {b}√{c} = ?", f"{a + b}√{c}", [f"{a * b}√{c}", f"{a + b}√{c * c}", f"{a + b + c}"], 2)
def a3_nhan(rng):
    a, b = rng.choice([(2, 8), (3, 12), (2, 18), (5, 20), (3, 27), (6, 24), (2, 50)]); return nint(rng, f"√{a} · √{b} = ?", math.isqrt(a * b), 2, (1, 2, 3), 0)
def a3_chia(rng):
    k, a = rng.randint(2, 9), rng.choice([2, 3, 5, 7]); return nint(rng, f"√{k * k * a} : √{a} = ?", k, 2, (1, 2, 3), 0)
def a3_rutgon(rng):
    a = rng.randint(2, 5); return M(f"Với x ≥ 0, rút gọn √({a * a}x²) ta được:", f"{a}x", [f"{a * a}x", f"{a}x²", f"x{a}"], 2)
def a3_ma(rng):
    a = rng.choice([2, 3, 5]); b = rng.randint(2, 6); return M(f"Trục căn thức ở mẫu: {b}/√{a} = ?", f"{b}√{a}/{a}", [f"{b}/{a}", f"√{a}/{b}", f"{b}√{a}"], 2)
def a3_so(rng):
    a, b = rng.randint(2, 40), rng.randint(2, 40)
    if a == b: raise ValueError
    d = kq_dau(a, b); return M(f"So sánh √{a} và √{b}:", f"√{a} {d} √{b}", [f"√{a} {x} √{b}" for x in sai_dau(d)[:3] if x != "Không so sánh được"] + ["√a = √b chỉ khi a = b"][:1], 1) if len(sai_dau(d)) > 0 else None
def a3_bt(rng):
    a, b = rng.randint(2, 9), rng.randint(2, 9); return nint(rng, f"Giá trị của √{a * a} + ∛{b ** 3} là:", a + b, 1, (1, 2, 3), 0)
def b3_rutgon(rng):
    a, b, c = rng.randint(2, 5), rng.randint(2, 5), rng.choice([2, 3, 5])
    return T(f"Rút gọn: {a}√{c * a * a} + {b}√{c} - √{c * b * b}.", f"= {a}·{a}√{c} + {b}√{c} - {b}√{c} = {a * a}√{c}", 2)
def b3_ma(rng):
    a = rng.choice([2, 3, 5, 7]); b = rng.randint(2, 9)
    return T(f"Trục căn thức ở mẫu của biểu thức {b}/√{a} và {b}/(√{a} + 1).", f"{b}/√{a} = {b}√{a}/{a}\n{b}/(√{a} + 1) = {b}(√{a} - 1)/({a} - 1)", 2)
def b3_x(rng):
    a = rng.randint(2, 9)
    return T(f"Giải phương trình √x = {a}.", f"Điều kiện x ≥ 0; bình phương hai vế: x = {a * a}.", 1)
def b3_dk(rng):
    a, b = rng.randint(1, 6), rng.randint(1, 6)
    return T(f"Tìm điều kiện của x để biểu thức √(x - {a}) + 1/√({b + a} - x) có nghĩa.", f"x - {a} ≥ 0 và {a + b} - x > 0 ⇒ {a} ≤ x < {a + b}.", 2)
def b3_ss(rng):
    ds = rng.sample(range(2, 30), 4); return T("Sắp xếp theo thứ tự tăng dần: " + ", ".join(f"√{x}" for x in ds) + ".", ", ".join(f"√{x}" for x in sorted(ds)), 1)
def b3_cbh3(rng):
    a = rng.randint(2, 6); return T(f"Tính: ∛{a ** 3} + ∛(-{a ** 3}) · 2.", f"= {a} + (-{a})·2 = {-a}", 2)

# ============ 4. Hệ thức lượng trong tam giác vuông ============
def a4_pyta(rng):
    a, b = rng.choice([(3, 4), (5, 12), (8, 15), (6, 8), (7, 24), (9, 12)]); return nint(rng, f"Tam giác ABC vuông tại A, AB = {a} cm, AC = {b} cm. Độ dài BC là (cm):", math.isqrt(a * a + b * b), 1, (1, 2, 3), 0)
def a4_goc(rng):
    a, c = rng.choice([(3, 5), (5, 13), (8, 17), (6, 10), (12, 20)]); b = math.isqrt(c * c - a * a); return nint(rng, f"Tam giác ABC vuông tại A, AB = {a} cm, BC = {c} cm. Độ dài AC là (cm):", b, 1, (1, 2, 3), 0)
def a4_cao(rng):
    a, b, c = rng.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15)]); h = Fraction(a * b, c)
    return M(f"Tam giác ABC vuông tại A, AB = {a} cm, AC = {b} cm, đường cao AH. Độ dài AH là (cm):", ps(h), nh_ps(rng, h) if h < 5 else [ps(h + 1), ps(h - 1), ps(h * 2)], 3)
def a4_ah2(rng):
    p, q = rng.choice([(2, 8), (3, 12), (4, 9), (1, 16), (4, 25), (9, 16), (2, 18)]); return nint(rng, f"Tam giác ABC vuông tại A, đường cao AH chia BC thành BH = {p} cm, HC = {q} cm. Độ dài AH là (cm):", math.isqrt(p * q), 3, (1, 2, 3), 0)
def a4_ab2(rng):
    p, q = rng.choice([(4, 5), (9, 16), (3, 13), (4, 21), (1, 24)]); bc = p + q; return M(f"Tam giác ABC vuông tại A, đường cao AH, BH = {p}, BC = {bc}. Biết AB² = BH·BC. Giá trị AB² là:", p * bc, [q * bc, p * q, bc * bc], 2)
def a4_sin(rng):
    a, c = rng.choice([(3, 5), (5, 13), (8, 17), (7, 25), (20, 29)]); return M(f"Tam giác ABC vuông tại A, AB = {a}, BC = {c}. sin C bằng:", ps(Fraction(a, c)), [ps(Fraction(c, a)), ps(Fraction(math.isqrt(c * c - a * a), c)), ps(Fraction(a, math.isqrt(c * c - a * a)))], 2)
def a4_cos(rng):
    a, b, c = rng.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]); return M(f"Tam giác ABC vuông tại A, AB = {a}, AC = {b}, BC = {c}. cos B bằng:", ps(Fraction(a, c)), [ps(Fraction(b, c)), ps(Fraction(a, b)), ps(Fraction(c, a))], 2)
def a4_tan(rng):
    a, b = rng.choice([(3, 4), (5, 12), (8, 15), (7, 24)]); return M(f"Tam giác ABC vuông tại A, AB = {a}, AC = {b}. tan B bằng:", ps(Fraction(b, a)), [ps(Fraction(a, b)), ps(Fraction(b, math.isqrt(a * a + b * b))), ps(Fraction(a, math.isqrt(a * a + b * b)))], 2)
def a4_gtlg(rng):
    return M(rng.choice(["sin 30° bằng:", "Giá trị của sin 30° là:"]), "1/2", ["√3/2", "√2/2", "1"], 1)
def a4_gtlg2(rng):
    return M("cos 60° bằng:", "1/2", ["√3/2", "√2/2", "0"], 1)
def a4_tan45(rng):
    return M("tan 45° bằng:", "1", ["0", "√3", "1/2"], 1)
def a4_goc2(rng):
    a = rng.randint(20, 70); return nint(rng, f"Tam giác ABC vuông tại A có góc B = {a}°. Số đo góc C là (độ):", 90 - a, 1, (10, 20, 5), 0)
def a4_phu(rng):
    return M("Trong tam giác ABC vuông tại A, sin B bằng:", "cos C", ["sin C", "tan C", "cot B"], 2)
def a4_tinhcanh(rng):
    c = rng.choice([10, 20, 30, 40]); return nint(rng, f"Tam giác ABC vuông tại A, BC = {c} cm, góc B = 30°. Cạnh AC dài (cm) (dùng AC = BC·sin B):", c // 2, 3, (1, 2, 5), 0)
def b4_giai(rng):
    a, b = rng.choice([(3, 4), (5, 12), (8, 15), (6, 8)])
    return T(f"Tam giác ABC vuông tại A, AB = {a} cm, AC = {b} cm. Tính BC, các tỉ số lượng giác sin B, cos B.", f"BC = √({a}² + {b}²) = {math.isqrt(a * a + b * b)} cm\nsin B = AC/BC = {ps(Fraction(b, math.isqrt(a * a + b * b)))}\ncos B = AB/BC = {ps(Fraction(a, math.isqrt(a * a + b * b)))}", 2)
def b4_cao(rng):
    p, q = rng.choice([(2, 8), (3, 12), (4, 9), (4, 25), (9, 16)])
    return T(f"Tam giác ABC vuông tại A, đường cao AH, BH = {p} cm, HC = {q} cm. Tính AH, AB, AC.", f"AH² = BH·HC = {p * q} ⇒ AH = {math.isqrt(p * q)} cm\nAB² = BH·BC = {p * (p + q)} ⇒ AB = √{p * (p + q)}\nAC² = HC·BC = {q * (p + q)} ⇒ AC = √{q * (p + q)}", 3)
def b4_goc(rng):
    a = rng.randint(20, 70); c = rng.choice([10, 20, 30])
    return T(f"Tam giác ABC vuông tại A, BC = {c} cm, góc B = {a}°. Viết các hệ thức tính AB, AC theo BC và góc B.", f"AB = BC·cos B = {c}·cos {a}°; AC = BC·sin B = {c}·sin {a}°.", 2)
def b4_toa(rng):
    h = rng.randint(5, 20); a = rng.choice([30, 45, 60])
    return T(f"Một cái thang dài {h} m dựa vào tường, tạo với mặt đất góc {a}°. Viết công thức tính độ cao thang chạm tường.", f"Độ cao = {h}·sin {a}° (sin {a}° = {'1/2' if a == 30 else '√2/2' if a == 45 else '√3/2'}).", 2)
def b4_bang(rng):
    return T("Hoàn thành bảng giá trị lượng giác của các góc đặc biệt 30°, 45°, 60° (sin, cos, tan).", "sin: 1/2, √2/2, √3/2\ncos: √3/2, √2/2, 1/2\ntan: √3/3, 1, √3", 1)
def b4_pg(rng):
    return T("Phát biểu các hệ thức về cạnh và đường cao trong tam giác vuông.", "b² = a·b'; c² = a·c'; h² = b'·c'; a·h = b·c; 1/h² = 1/b² + 1/c² (a là cạnh huyền; b, c là hai cạnh góc vuông; b', c' là hình chiếu; h là đường cao).", 1)

# ============ 5. Đường tròn ============
def a5_duong_kinh(rng):
    r = rng.randint(2, 15); return nint(rng, f"Đường tròn có bán kính {r} cm. Đường kính là (cm):", 2 * r, 1, (r, 2, 4), 0)
def a5_tam(rng):
    return M("Đường kính là dây:", "Lớn nhất của đường tròn", ["Nhỏ nhất của đường tròn", "Không đi qua tâm", "Bằng bán kính"], 1)
def a5_vt(rng):
    r = rng.randint(3, 12); d = rng.choice([r - 1, r, r + 1, r + 3]) if r > 1 else r + 1
    kq = "Điểm nằm trong đường tròn" if d < r else "Điểm nằm trên đường tròn" if d == r else "Điểm nằm ngoài đường tròn"
    return M(f"Cho đường tròn (O; {r} cm) và điểm M có OM = {d} cm. Vị trí của M là:", kq, [x for x in ["Điểm nằm trong đường tròn", "Điểm nằm trên đường tròn", "Điểm nằm ngoài đường tròn", "Điểm là tâm"] if x != kq][:3], 1)
def a5_dd(rng):
    r = rng.randint(3, 12); d = rng.choice([r - 2 if r > 2 else 1, r, r + 2]); kq = "Cắt nhau" if d < r else "Tiếp xúc" if d == r else "Không giao nhau"
    return M(f"Đường thẳng d cách tâm O của đường tròn (O; {r} cm) một khoảng {d} cm. Vị trí tương đối của d và đường tròn là:", kq, [x for x in ["Cắt nhau", "Tiếp xúc", "Không giao nhau", "Trùng nhau"] if x != kq][:3], 2)
def a5_tiep(rng):
    return M("Tiếp tuyến của đường tròn vuông góc với:", "Bán kính đi qua tiếp điểm", ["Đường kính bất kì", "Dây bất kì", "Tâm đường tròn"], 2)
def a5_goc_tam(rng):
    a = rng.randint(20, 170); return nint(rng, f"Góc ở tâm chắn cung có số đo {a}° thì số đo cung là (độ):", a, 1, (10, 20, 30), 0)
def a5_noi_tiep(rng):
    a = rng.randint(2, 17) * 10; return nint(rng, f"Số đo góc nội tiếp chắn cung {a}° là (độ):", a // 2, 2, (5, 10, 20), 0)
def a5_noi_tiep2(rng):
    return M("Góc nội tiếp chắn nửa đường tròn có số đo bằng:", "90°", ["60°", "180°", "45°"], 2)
def a5_day(rng):
    r = rng.choice([5, 10, 13, 15, 25]); h = rng.choice([x for x in [3, 4, 5, 6, 8, 12, 9, 10] if x < r]); 
    d = math.isqrt(r * r - h * h)
    if d * d != r * r - h * h: raise ValueError
    return nint(rng, f"Đường tròn (O; {r} cm), dây AB cách tâm {h} cm. Độ dài dây AB là (cm):", 2 * d, 3, (2, 4, 6), 0)
def a5_cung(rng):
    n = rng.randint(2, 18) * 10; r = rng.randint(2, 9); return M(f"Đường tròn bán kính {r}, cung có số đo {n}° chiếm bao nhiêu phần đường tròn?", ps(Fraction(n, 360)), nh_ps(rng, Fraction(n, 360)), 2)
def a5_chuvi(rng):
    r = rng.randint(2, 15); return M(f"Chu vi đường tròn bán kính {r} cm là:", f"{2 * r}π cm", [f"{r}π cm", f"{r * r}π cm", f"{4 * r}π cm"], 1)
def a5_dt(rng):
    r = rng.randint(2, 15); return M(f"Diện tích hình tròn bán kính {r} cm là:", f"{r * r}π cm²", [f"{2 * r}π cm²", f"{r}π cm²", f"{4 * r * r}π cm²"], 1)
def b5_cung(rng):
    a = rng.randint(2, 17) * 10
    return T(f"Trong đường tròn (O), góc ở tâm AOB = {a}°. Tính số đo cung nhỏ AB và số đo cung lớn AB; góc nội tiếp chắn cung AB.", f"Cung nhỏ AB = {a}°; cung lớn AB = {360 - a}°\nGóc nội tiếp chắn cung nhỏ AB = {a // 2}°", 2)
def b5_day(rng):
    r = rng.choice([5, 10, 13, 15]); h = rng.choice([x for x in [3, 4, 5, 6, 8, 12, 9] if x < r]); d = math.isqrt(r * r - h * h)
    if d * d != r * r - h * h: raise ValueError
    return T(f"Đường tròn (O; {r} cm) có dây AB cách tâm O một khoảng {h} cm. Tính độ dài AB.", f"Gọi H là trung điểm AB, OH ⊥ AB. AH = √({r}² - {h}²) = {d} cm ⇒ AB = {2 * d} cm.", 2)
def b5_tt(rng):
    r = rng.randint(3, 10); d = rng.randint(r + 2, r + 10)
    return T(f"Từ điểm M cách tâm O của đường tròn (O; {r} cm) một khoảng {d} cm, kẻ tiếp tuyến MA (A là tiếp điểm). Tính MA.", f"MA ⊥ OA ⇒ MA = √(OM² - OA²) = √({d}² - {r}²) = √{d * d - r * r} cm.", 3)
def b5_vi_tri(rng):
    return T("Nêu các vị trí tương đối của đường thẳng và đường tròn kèm hệ thức giữa khoảng cách d từ tâm đến đường thẳng và bán kính R.", "Cắt nhau: d < R (2 điểm chung). Tiếp xúc: d = R (1 điểm chung). Không giao nhau: d > R.", 1)
def b5_cv(rng):
    r = rng.randint(2, 12); return T(f"Tính chu vi và diện tích hình tròn bán kính {r} cm (để dưới dạng π).", f"C = 2π·{r} = {2 * r}π cm\nS = π·{r}² = {r * r}π cm²", 1)
def b5_tt2(rng):
    return T("Phát biểu tính chất hai tiếp tuyến cắt nhau của đường tròn.", "Nếu hai tiếp tuyến của một đường tròn cắt nhau tại một điểm thì điểm đó cách đều hai tiếp điểm; tia kẻ từ điểm đó đến tâm là phân giác của góc tạo bởi hai tiếp tuyến; tia kẻ từ tâm đến điểm đó là phân giác của góc tạo bởi hai bán kính đi qua tiếp điểm.", 2)

# ============ 6. Hàm số y = ax² và phương trình bậc hai một ẩn ============
def a6_gt(rng):
    a, x = nz(rng, -3, 3), rng.randint(-4, 4); return nint(rng, f"Cho hàm số y = {a}x². Giá trị của y khi x = {x} là:", a * x * x, 1, (1, 2, 5))
def a6_thuoc(rng):
    a, x = rng.randint(1, 3), rng.randint(1, 4); y = a * x * x; return M(f"Điểm nào thuộc đồ thị hàm số y = {a}x²?", f"({x}; {y})", [f"({x}; {y + 1})", f"({x + 1}; {y})", f"({x}; -{y})"], 2)
def a6_a(rng):
    a, x = rng.randint(1, 4), rng.randint(1, 4); y = a * x * x; return nint(rng, f"Đồ thị hàm số y = ax² đi qua điểm ({x}; {y}). Hệ số a bằng:", a, 2, (1, 2), 0)
def a6_bien(rng):
    a = rng.choice([-3, -2, -1, 1, 2, 3]); return M(f"Hàm số y = {a}x² có giá trị nhỏ nhất bằng 0 khi:", "a > 0 (x = 0)" if a > 0 else "không có (hàm có GTLN bằng 0)", ["a < 0 (x = 0)", "Luôn dương", "Không xác định"], 2) if False else M(f"Hàm số y = {a}x² đạt giá trị {'nhỏ' if a > 0 else 'lớn'} nhất bằng:", 0, [1, -1, a], 2)
def a6_delta(rng):
    a, b, c = nz(rng, -4, 4), nz(rng, -6, 6), nz(rng, -6, 6); d = b * b - 4 * a * c; return nint(rng, f"Biệt thức Δ của phương trình {da([a, b, c])} = 0 là:", d, 2, (4, 8, 2))
def a6_nghiem(rng):
    x1, x2 = rng.randint(-5, 6), rng.randint(-5, 6)
    if x1 == x2: raise ValueError
    s, p = x1 + x2, x1 * x2
    return M(f"Tập nghiệm của phương trình {da([1, -s, p])} = 0 là:", f"{{{min(x1, x2)}; {max(x1, x2)}}}", [f"{{{-x1}; {-x2}}}", f"{{{x1 + 1}; {x2}}}", f"{{{x1}; {x2 + 1}}}"], 2)
def a6_vieta_s(rng):
    x1, x2 = rng.randint(-5, 7), rng.randint(-5, 7); return nint(rng, f"Phương trình {da([1, -(x1 + x2), x1 * x2])} = 0 có hai nghiệm x₁, x₂. Tổng x₁ + x₂ bằng:", x1 + x2, 2, (1, 2, 3))
def a6_vieta_p(rng):
    x1, x2 = rng.randint(-5, 7), rng.randint(-5, 7); return nint(rng, f"Phương trình {da([1, -(x1 + x2), x1 * x2])} = 0 có hai nghiệm x₁, x₂. Tích x₁·x₂ bằng:", x1 * x2, 2, (1, 2, 3))
def a6_nghiem_so(rng):
    a, b, c = rng.choice([(1, 2, 1), (1, 0, 4), (1, -4, 4), (1, 1, 5), (2, 4, 2), (1, -2, 3), (1, 3, 2), (1, 0, -9)]); d = b * b - 4 * a * c; k = 2 if d > 0 else 1 if d == 0 else 0
    return M(f"Phương trình {da([a, b, c])} = 0 có bao nhiêu nghiệm thực?", k, [x for x in [0, 1, 2] if x != k] + [3], 2)
def a6_tdt(rng):
    x1, x2 = rng.randint(1, 6), rng.randint(1, 6); return nint(rng, f"Hai số có tổng {x1 + x2} và tích {x1 * x2} là nghiệm của phương trình nào? Hệ số tự do của phương trình bậc hai tương ứng (x² - Sx + P = 0) là:", x1 * x2, 2, (1, 2, 3), 0)
def a6_hs_c(rng):
    a, b, c = nz(rng, -4, 4), nz(rng, -6, 6), nz(rng, -6, 6); return nint(rng, f"Hệ số a, b, c của phương trình {da([a, b, c])} = 0. Giá trị của b là:", b, 1, (1, 2, 3))
def a6_hinhchunhat(rng):
    a, b = rng.randint(2, 6), rng.randint(2, 6); s = a * b; p = 2 * (a + b)
    if a == b: raise ValueError
    return M(f"Hình chữ nhật có nửa chu vi {a + b} cm và diện tích {s} cm². Kích thước hai cạnh là nghiệm của phương trình:", da([1, -(a + b), s]) + " = 0", [da([1, a + b, s]) + " = 0", da([1, -(a + b), a + b]) + " = 0", da([1, -s, a + b]) + " = 0"], 3)
def b6_giai(rng):
    x1, x2 = rng.randint(-5, 6), rng.randint(-5, 6)
    if x1 == x2: raise ValueError
    return T(f"Giải phương trình {da([1, -(x1 + x2), x1 * x2])} = 0.", f"Δ = ({-(x1 + x2)})² - 4·{x1 * x2} = {(x1 - x2) ** 2}\nx₁ = {x1}; x₂ = {x2}", 2)
def b6_vieta(rng):
    x1, x2 = rng.randint(-4, 6), rng.randint(-4, 6)
    return T(f"Cho phương trình {da([1, -(x1 + x2), x1 * x2])} = 0 có hai nghiệm x₁, x₂. Không giải phương trình, tính x₁ + x₂, x₁x₂ và x₁² + x₂².", f"x₁ + x₂ = {x1 + x2}; x₁x₂ = {x1 * x2}\nx₁² + x₂² = ({x1 + x2})² - 2·{x1 * x2} = {(x1 + x2) ** 2 - 2 * x1 * x2}", 3)
def b6_do_thi(rng):
    a = rng.randint(1, 3); return T(f"Lập bảng giá trị của hàm số y = {a}x² với x = -2, -1, 0, 1, 2 và nhận xét về hình dạng đồ thị.", f"x: -2, -1, 0, 1, 2 ⇒ y: {4 * a}, {a}, 0, {a}, {4 * a}\nĐồ thị là parabol, đỉnh O(0; 0), đối xứng qua trục Oy.", 1)
def b6_loi(rng):
    a, b = rng.randint(3, 8), rng.randint(2, 6)
    return T(f"Một mảnh đất hình chữ nhật có chiều dài hơn chiều rộng {a} m và diện tích {b * (b + a)} m². Tính các kích thước.", f"Gọi chiều rộng x (m): x(x + {a}) = {b * (b + a)} ⇒ x² + {a}x - {b * (b + a)} = 0 ⇒ x = {b} (nhận).\nVậy rộng {b} m, dài {a + b} m.", 3)
def b6_dk(rng):
    m = rng.randint(2, 6)
    return T(f"Tìm m để phương trình x² - {2 * m}x + m = 0 có nghiệm.", f"Δ' = {m * m} - m ≥ 0 ⇒ m(m - 1) ≥ 0 ⇒ m ≤ 0 hoặc m ≥ 1.", 3)
def b6_pt(rng):
    a = rng.randint(2, 6); return T(f"Giải phương trình {a}x² - {a * a * 2}x = 0.", f"{a}x(x - {a * 2}) = 0 ⇒ x = 0 hoặc x = {a * 2}.", 1)

# ============ 7. Tần số và tần số tương đối ============
def _dl(rng):
    ten = ["A", "B", "C", "D"]; v = [rng.randint(3, 15) for _ in ten]; return ten, v
def a7_tong(rng):
    t, v = _dl(rng); return nint(rng, f"Tần số của các giá trị {', '.join(t)} lần lượt là {', '.join(map(str, v))}. Tổng số quan sát (cỡ mẫu) là:", sum(v), 1, (1, 2, 5), 0)
def a7_tsdt(rng):
    t, v = _dl(rng); n = sum(v); i = rng.randrange(4); f = Fraction(v[i], n)
    return M(f"Tần số của các giá trị {', '.join(t)} lần lượt là {', '.join(map(str, v))}. Tần số tương đối của {t[i]} (phân số tối giản) là:", ps(f), nh_ps(rng, f), 2)
def a7_pt(rng):
    n = rng.choice([20, 25, 40, 50, 100]); a = rng.randint(1, n // 2); 
    if (a * 100) % n: raise ValueError
    return M(f"Giá trị x xuất hiện {a} lần trong mẫu {n} số liệu. Tần số tương đối của x tính theo phần trăm là:", f"{a * 100 // n}%", chon3(rng, [f"{a * 100 // n + 5}%", f"{max(a * 100 // n - 5, 1)}%", f"{a}%", f"{n}%"], f"{a * 100 // n}%"), 2)
def a7_tong_tsdt(rng):
    return M("Tổng các tần số tương đối của một bảng tần số bằng:", "1 (hay 100%)", ["0", "Số lượng giá trị", "Cỡ mẫu"], 1)
def a7_tong_tan(rng):
    return M("Tổng các tần số của một mẫu số liệu bằng:", "Cỡ mẫu", ["1", "Giá trị lớn nhất", "Giá trị trung bình"], 1)
def a7_mot(rng):
    t, v = _dl(rng)
    if v.count(max(v)) > 1: raise ValueError
    return M(f"Tần số của A, B, C, D lần lượt là {', '.join(map(str, v))}. Giá trị có tần số lớn nhất (mốt) là:", t[v.index(max(v))], [x for x in t if x != t[v.index(max(v))]], 1)
def a7_tb(rng):
    xs = [rng.randint(5, 10) for _ in range(5)]; 
    if sum(xs) % 5: raise ValueError
    return nint(rng, f"Trung bình cộng của các số {', '.join(map(str, xs))} là:", sum(xs) // 5, 2, (1, 2), 0)
def a7_nhom(rng):
    a = rng.randint(1, 5) * 5; w = rng.choice([5, 10]); return M(f"Với nhóm số liệu [{a}; {a + w}), độ rộng của nhóm là:", w, [a, a + w, w * 2], 2) if False else nint(rng, f"Nhóm số liệu [{a}; {a + w}) có độ rộng là:", w, 1, (1, 2, 5), 0)
def a7_tg(rng):
    a = rng.randint(1, 5) * 10; w = rng.choice([10, 20]); return nint(rng, f"Giá trị đại diện của nhóm số liệu [{a}; {a + w}) là:", a + w // 2, 2, (1, 2, 5), 0)
def a7_bd(rng):
    return M("Biểu đồ tần số tương đối dạng cột biểu diễn:", "Tỉ lệ (phần trăm) của mỗi giá trị trong mẫu", ["Tổng các giá trị", "Giá trị lớn nhất", "Số nhóm"], 2)
def a7_cong(rng):
    a, b = rng.randint(3, 12), rng.randint(3, 12); return nint(rng, f"Hai nhóm có tần số {a} và {b}. Tần số của hai nhóm cộng lại là:", a + b, 1, (1, 2, 3), 0)
def a7_hieu(rng):
    a, b = rng.randint(8, 20), rng.randint(2, 7); return nint(rng, f"Tần số của giá trị M là {a}, của giá trị N là {b}. Tần số của M nhiều hơn của N là:", a - b, 1, (1, 2, 3), 0)
def b7_bang(rng):
    t, v = _dl(rng); n = sum(v)
    return T(f"Tần số của các giá trị {', '.join(t)} lần lượt là {', '.join(map(str, v))}. Lập bảng tần số tương đối (làm tròn đến hàng phần trăm).", "\n".join(f"{x}: {c}/{n} ≈ {c * 100 / n:.1f}%".replace(".", ",") for x, c in zip(t, v)), 2)
def b7_tb(rng):
    xs = [rng.randint(4, 10) for _ in range(8)]
    return T(f"Điểm 8 bài kiểm tra: {', '.join(map(str, xs))}. Lập bảng tần số và tính điểm trung bình.", f"Điểm trung bình = {sum(xs)}/8 = {sum(xs) / 8:.2f}".replace(".", ","), 2)
def b7_mot(rng):
    xs = [rng.randint(5, 8) for _ in range(12)]; from collections import Counter; c = Counter(xs); m = c.most_common(1)[0]
    if list(c.values()).count(m[1]) > 1: raise ValueError
    return T(f"Cho mẫu số liệu: {', '.join(map(str, xs))}. Tìm mốt và tần số của mốt.", f"Mốt: {m[0]} (xuất hiện {m[1]} lần).", 1)
def b7_nhom(rng):
    return T("Giải thích cách chia nhóm số liệu để lập bảng tần số ghép nhóm.", "Chọn các nhóm có độ rộng bằng nhau, nhóm dạng [a; b), mỗi giá trị thuộc đúng một nhóm; đếm số giá trị mỗi nhóm để có tần số.", 1)
def b7_ts(rng):
    n = rng.choice([20, 25, 40, 50]); a = rng.randint(2, n // 3)
    return T(f"Trong mẫu {n} số liệu, giá trị 7 xuất hiện {a} lần. Tính tần số tương đối của giá trị 7 (phân số và phần trăm).", f"{pf(a, n)} = {a * 100 / n:g}%".replace(".", ","), 1)
def b7_bd(rng):
    return T("Nêu hai loại biểu đồ thường dùng để biểu diễn bảng tần số tương đối và cho biết khi nào dùng.", "Biểu đồ cột (so sánh các giá trị rời rạc); biểu đồ hình quạt (tỉ lệ các phần trong tổng thể).", 1)

# ============ 8. Xác suất của biến cố ============
def a8_xuc(rng):
    return M("Gieo hai con xúc xắc cân đối. Tổng số kết quả có thể xảy ra là:", 36, [12, 24, 6], 1)
def a8_tong(rng):
    s = rng.randint(2, 12); c = 6 - abs(s - 7); f = Fraction(c, 36); return M(f"Gieo hai con xúc xắc. Xác suất để tổng số chấm bằng {s} là:", ps(f), nh_ps(rng, f), 2)
def a8_doi(rng):
    a, b = rng.randint(1, 6), rng.randint(1, 6); return M("Gieo hai con xúc xắc. Xác suất để hai mặt có cùng số chấm là:", "1/6", ["1/36", "1/3", "1/2"], 2)
def a8_hop(rng):
    d, x = rng.randint(2, 8), rng.randint(2, 8); n = d + x; f = Fraction(d, n); return M(f"Hộp có {d} bi đỏ và {x} bi xanh. Lấy ngẫu nhiên một viên. Xác suất lấy được bi đỏ là:", ps(f), nh_ps(rng, f), 1)
def a8_hai(rng):
    d, x = rng.randint(2, 6), rng.randint(2, 6); n = d + x; f = Fraction(d * (d - 1), n * (n - 1)); return M(f"Hộp có {d} bi đỏ và {x} bi xanh. Lấy ngẫu nhiên lần lượt hai viên không hoàn lại. Xác suất cả hai bi đỏ (tối giản) là:", ps(f), nh_ps(rng, f), 3)
def a8_dong(rng):
    return M("Tung ba đồng xu. Số kết quả có thể là:", 8, [6, 4, 9], 2)
def a8_dong2(rng):
    return M("Tung ba đồng xu. Xác suất cả ba đồng cùng sấp là:", "1/8", ["1/3", "1/4", "3/8"], 2)
def a8_it_nhat(rng):
    return M("Tung ba đồng xu. Xác suất có ít nhất một đồng ngửa là:", "7/8", ["1/8", "3/4", "1/2"], 3)
def a8_the(rng):
    n = rng.randint(10, 30); k = rng.choice([2, 3, 5]); c = n // k; f = Fraction(c, n); return M(f"Rút ngẫu nhiên một thẻ từ {n} thẻ đánh số 1 đến {n}. Xác suất số trên thẻ chia hết cho {k} là:", ps(f), nh_ps(rng, f), 2)
def a8_doi_p(rng):
    p = rng.choice([Fraction(1, 6), Fraction(2, 5), Fraction(1, 4), Fraction(3, 10)]); return M(f"Xác suất của biến cố A là {ps(p)}. Xác suất của biến cố đối là:", ps(1 - p), nh_ps(rng, 1 - p), 1)
def a8_ban(rng):
    a = rng.randint(3, 9) * 10; k = rng.randint(2, a // 3); f = Fraction(k, a); return M(f"Một xạ thủ bắn {a} phát, trúng {k} phát. Xác suất thực nghiệm để bắn trúng (tối giản) là:", ps(f), nh_ps(rng, f), 2)
def a8_nhanh(rng):
    return M("Với phép thử có n kết quả đồng khả năng và k kết quả thuận lợi cho biến cố A thì P(A) bằng:", "k/n", ["n/k", "k·n", "k + n"], 1)
def b8_xuc(rng):
    s = rng.randint(2, 12); c = 6 - abs(s - 7)
    return T(f"Gieo hai con xúc xắc cân đối. Tính xác suất để tổng số chấm bằng {s}.", f"Không gian mẫu có 36 kết quả; có {c} kết quả thuận lợi.\nP = {pf(c, 36)}", 2)
def b8_hop(rng):
    d, x, v = rng.randint(2, 6), rng.randint(2, 6), rng.randint(1, 5); n = d + x + v
    return T(f"Hộp có {d} bi đỏ, {x} bi xanh, {v} bi vàng. Lấy ngẫu nhiên một viên. Tính xác suất lấy được bi xanh hoặc bi vàng.", f"Số kết quả thuận lợi: {x + v}\nP = {pf(x + v, n)}", 2)
def b8_hai(rng):
    d, x = rng.randint(2, 5), rng.randint(2, 5); n = d + x
    return T(f"Hộp có {d} bi đỏ và {x} bi xanh. Lấy ngẫu nhiên đồng thời 2 viên. Tính xác suất lấy được 2 bi đỏ.", f"Số cách chọn 2 viên: C({n},2) = {n * (n - 1) // 2}; số cách chọn 2 bi đỏ: C({d},2) = {d * (d - 1) // 2}\nP = {pf(d * (d - 1) // 2, n * (n - 1) // 2)}", 3)
def b8_cay(rng):
    return T("Tung đồng thời hai đồng xu. Tính xác suất để hai đồng xu có mặt giống nhau.", "Không gian mẫu: SS, SN, NS, NN (4 kết quả). Thuận lợi: SS, NN (2 kết quả).\nP = 2/4 = 1/2.", 2)
def b8_doi(rng):
    return T("Tung ba đồng xu. Tính xác suất có ít nhất một mặt sấp bằng cách dùng biến cố đối.", "Biến cố đối: cả ba đều ngửa, xác suất 1/8.\nP(ít nhất một sấp) = 1 - 1/8 = 7/8.", 3)
def b8_so(rng):
    n = rng.choice([20, 30, 40, 50]); k = rng.choice([3, 4, 5, 6, 7])
    return T(f"Chọn ngẫu nhiên một số nguyên từ 1 đến {n}. Tính xác suất để số đó chia hết cho {k}.", f"Số kết quả thuận lợi: {n // k}\nP = {pf(n // k, n)}", 2)

# ============ 9. Đường tròn ngoại tiếp và nội tiếp ============
def a9_ngoai_tam(rng):
    return M("Tâm đường tròn ngoại tiếp tam giác là giao điểm của ba đường:", "Trung trực", ["Phân giác", "Trung tuyến", "Đường cao"], 1)
def a9_noi_tam(rng):
    return M("Tâm đường tròn nội tiếp tam giác là giao điểm của ba đường:", "Phân giác", ["Trung trực", "Trung tuyến", "Đường cao"], 1)
def a9_vuong(rng):
    a, b = rng.choice([(3, 4), (6, 8), (5, 12), (8, 15)]); c = math.isqrt(a * a + b * b); return M(f"Tam giác vuông có hai cạnh góc vuông {a} cm, {b} cm. Bán kính đường tròn ngoại tiếp là (cm):", ps(Fraction(c, 2)), nh_ps(rng, Fraction(c, 2)) if Fraction(c, 2) < 1 else [ps(Fraction(c, 2) + 1), ps(Fraction(c, 2) - 1), ps(Fraction(c))], 2)
def a9_deu(rng):
    return M("Tam giác đều cạnh a có bán kính đường tròn nội tiếp là:", "a√3/6", ["a√3/3", "a/2", "a√3/2"], 3)
def a9_deu2(rng):
    return M("Tam giác đều cạnh a có bán kính đường tròn ngoại tiếp là:", "a√3/3", ["a√3/6", "a/2", "a√3/2"], 3)
def a9_vuong_cang(rng):
    return M("Tứ giác nội tiếp đường tròn có tổng hai góc đối bằng:", "180°", ["90°", "360°", "270°"], 1)
def a9_goc_tgnt(rng):
    a = rng.randint(50, 130); return nint(rng, f"Tứ giác ABCD nội tiếp đường tròn, góc A = {a}°. Số đo góc C là (độ):", 180 - a, 2, (10, 20, 30), 0)
def a9_vuong_tg(rng):
    a, b, c = rng.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17)]); r = Fraction(a + b - c, 2); return M(f"Tam giác vuông có ba cạnh {a}, {b}, {c}. Bán kính đường tròn nội tiếp (r = (a + b - c)/2) là:", ps(r), nh_ps(rng, r) if r < 1 else [ps(r + 1), ps(r + Fraction(1, 2)), ps(r * 2)], 3)
def a9_nt_hv(rng):
    a = rng.randint(2, 10); return M(f"Hình vuông cạnh {a} cm có đường tròn nội tiếp bán kính (cm):", ps(Fraction(a, 2)), [ps(Fraction(a)), ps(Fraction(a, 3)), ps(Fraction(2 * a))], 2)
def a9_hcn(rng):
    return M("Hình chữ nhật luôn nội tiếp được đường tròn vì:", "Tổng hai góc đối bằng 180°", ["Hai đường chéo vuông góc", "Các cạnh bằng nhau", "Có hai cặp cạnh song song"], 2)
def a9_thoi(rng):
    return M("Hình thoi (không là hình vuông) có đường tròn nội tiếp không?", "Có", ["Không", "Chỉ khi các góc bằng nhau", "Chỉ khi đường chéo bằng nhau"], 2)
def a9_dcdt(rng):
    return M("Đa giác đều luôn có:", "Đường tròn ngoại tiếp và đường tròn nội tiếp cùng tâm", ["Chỉ đường tròn ngoại tiếp", "Chỉ đường tròn nội tiếp", "Hai tâm khác nhau"], 2)
def a9_luc(rng):
    a = rng.randint(2, 10); return nint(rng, f"Lục giác đều cạnh {a} cm nội tiếp đường tròn bán kính (cm):", a, 2, (1, 2, 3), 0)
def b9_vuong(rng):
    a, b = rng.choice([(3, 4), (6, 8), (5, 12), (8, 15)]); c = math.isqrt(a * a + b * b)
    return T(f"Tam giác ABC vuông tại A, AB = {a} cm, AC = {b} cm. Tính bán kính đường tròn ngoại tiếp và nội tiếp.", f"BC = {c} cm\nR = BC/2 = {ps(Fraction(c, 2))} cm\nr = (AB + AC - BC)/2 = {ps(Fraction(a + b - c, 2))} cm", 3)
def b9_tgnt(rng):
    a = rng.randint(50, 130)
    return T(f"Tứ giác ABCD nội tiếp đường tròn có góc A = {a}°, góc B = {a - 20 if a > 70 else a + 10}°. Tính góc C và D.", f"C = 180° - A = {180 - a}°\nD = 180° - B = {180 - (a - 20 if a > 70 else a + 10)}°", 2)
def b9_cm(rng):
    return T("Chứng minh rằng tâm đường tròn ngoại tiếp tam giác vuông là trung điểm cạnh huyền.", "Gọi M là trung điểm cạnh huyền BC của ΔABC vuông tại A. Theo tính chất trung tuyến ứng với cạnh huyền, MA = MB = MC = BC/2. Vậy M cách đều ba đỉnh, nên M là tâm đường tròn ngoại tiếp.", 2)
def b9_dd(rng):
    a = rng.randint(2, 9); return T(f"Tính bán kính đường tròn ngoại tiếp và nội tiếp của hình vuông cạnh {a * 2} cm.", f"Bán kính ngoại tiếp = nửa đường chéo = {a}√2 cm; bán kính nội tiếp = {a} cm.", 2)
def b9_dk(rng):
    return T("Nêu điều kiện để một tứ giác nội tiếp được đường tròn.", "Tứ giác có tổng hai góc đối bằng 180°, hoặc có góc ngoài tại một đỉnh bằng góc trong ở đỉnh đối, hoặc có hai đỉnh cùng nhìn một cạnh dưới hai góc bằng nhau.", 1)
def b9_cv(rng):
    r = rng.randint(3, 12); return T(f"Tam giác đều nội tiếp đường tròn bán kính {r} cm. Tính cạnh tam giác.", f"Cạnh = R√3 = {r}√3 cm.", 2)

# ============ 10. Hình trụ, hình nón, hình cầu ============
def a10_tru_v(rng):
    r, h = rng.randint(2, 8), rng.randint(3, 15); return M(f"Hình trụ có bán kính đáy {r} cm, chiều cao {h} cm. Thể tích là:", f"{r * r * h}π cm³", [f"{2 * r * h}π cm³", f"{r * h}π cm³", f"{r * r * h * 2}π cm³"], 1)
def a10_tru_sxq(rng):
    r, h = rng.randint(2, 8), rng.randint(3, 15); return M(f"Hình trụ có bán kính đáy {r} cm, chiều cao {h} cm. Diện tích xung quanh là:", f"{2 * r * h}π cm²", [f"{r * h}π cm²", f"{r * r * h}π cm²", f"{2 * r * (r + h)}π cm²"], 2)
def a10_non_v(rng):
    r, h = rng.randint(2, 6), rng.randint(3, 4) * 3; return M(f"Hình nón có bán kính đáy {r} cm, chiều cao {h} cm. Thể tích là:", f"{r * r * h // 3}π cm³", [f"{r * r * h}π cm³", f"{r * h}π cm³", f"{r * r * h // 2}π cm³"], 2)
def a10_non_sxq(rng):
    r, l = rng.randint(2, 9), rng.randint(10, 20); return M(f"Hình nón có bán kính đáy {r} cm, đường sinh {l} cm. Diện tích xung quanh là:", f"{r * l}π cm²", [f"{2 * r * l}π cm²", f"{r * r * l}π cm²", f"{r * (r + l)}π cm²"], 2)
def a10_cau_v(rng):
    r = rng.randint(1, 6) * 3; return M(f"Hình cầu bán kính {r} cm có thể tích là:", f"{4 * r ** 3 // 3}π cm³", [f"{4 * r * r}π cm³", f"{r ** 3}π cm³", f"{2 * r ** 3 // 3}π cm³"], 2) if (4 * r ** 3) % 3 == 0 else (_ for _ in ()).throw(ValueError)
def a10_cau_s(rng):
    r = rng.randint(2, 12); return M(f"Hình cầu bán kính {r} cm có diện tích mặt cầu là:", f"{4 * r * r}π cm²", [f"{r * r}π cm²", f"{2 * r * r}π cm²", f"{4 * r ** 3 // 3}π cm²"], 2)
def a10_dg(rng):
    r, l = rng.randint(3, 12), rng.randint(13, 25); h = math.isqrt(l * l - r * r)
    if h * h != l * l - r * r: raise ValueError
    return nint(rng, f"Hình nón có bán kính đáy {r} cm, đường sinh {l} cm. Chiều cao là (cm):", h, 3, (1, 2, 3), 0)
def a10_truc(rng):
    r = rng.randint(2, 9); return nint(rng, f"Hình trụ có bán kính đáy {r} cm. Đường kính đáy là (cm):", 2 * r, 1, (1, 2, 4), 0)
def a10_dtqt(rng):
    r, h = rng.randint(2, 6), rng.randint(3, 10); return M(f"Hình trụ có bán kính đáy {r} cm, chiều cao {h} cm. Diện tích toàn phần là:", f"{2 * r * (r + h)}π cm²", [f"{2 * r * h}π cm²", f"{r * r * h}π cm²", f"{r * (r + h)}π cm²"], 3)
def a10_hcn_quay(rng):
    return M("Quay hình chữ nhật một vòng quanh một cạnh cố định ta được:", "Hình trụ", ["Hình nón", "Hình cầu", "Hình chóp"], 1)
def a10_tg_quay(rng):
    return M("Quay tam giác vuông một vòng quanh một cạnh góc vuông cố định ta được:", "Hình nón", ["Hình trụ", "Hình cầu", "Hình chóp"], 1)
def a10_nua(rng):
    return M("Quay nửa hình tròn một vòng quanh đường kính cố định ta được:", "Hình cầu", ["Hình trụ", "Hình nón", "Hình elip"], 1)
def a10_duong(rng):
    r, h = rng.randint(2, 6), rng.randint(2, 6); return nint(rng, f"Nước trong hình trụ bán kính đáy {r}, cao {h} (π ≈ 3). Thể tích gần đúng (cm³):", 3 * r * r * h, 3, (r, h, 10), 0)
def b10_tru(rng):
    r, h = rng.randint(2, 8), rng.randint(3, 15)
    return T(f"Hình trụ có bán kính đáy {r} cm, chiều cao {h} cm. Tính diện tích xung quanh, diện tích toàn phần và thể tích (để dưới dạng π).", f"Sxq = 2π·{r}·{h} = {2 * r * h}π cm²\nStp = 2π·{r}·({r} + {h}) = {2 * r * (r + h)}π cm²\nV = π·{r}²·{h} = {r * r * h}π cm³", 2)
def b10_non(rng):
    r, h = rng.choice([(3, 4), (6, 8), (5, 12), (8, 6), (9, 12)]); l = math.isqrt(r * r + h * h)
    return T(f"Hình nón có bán kính đáy {r} cm, chiều cao {h} cm. Tính đường sinh, diện tích xung quanh và thể tích.", f"l = √({r}² + {h}²) = {l} cm\nSxq = π·{r}·{l} = {r * l}π cm²\nV = (1/3)π·{r}²·{h} = {r * r * h // 3 if (r * r * h) % 3 == 0 else ps(Fraction(r * r * h, 3))}π cm³", 3)
def b10_cau(rng):
    r = rng.randint(2, 9)
    return T(f"Hình cầu có bán kính {r} cm. Tính diện tích mặt cầu và thể tích (dạng π).", f"S = 4π·{r}² = {4 * r * r}π cm²\nV = (4/3)π·{r}³ = {ps(Fraction(4 * r ** 3, 3))}π cm³", 2)
def b10_loi(rng):
    r, h = rng.randint(2, 5), rng.randint(5, 12)
    return T(f"Một cốc nước hình trụ có bán kính đáy {r} cm, cao {h} cm. Tính thể tích nước khi đầy (π ≈ 3,14, làm tròn đến hàng đơn vị).", f"V = 3,14·{r}²·{h} = {3.14 * r * r * h:.0f} cm³".replace(".", ","), 2)
def b10_phan(rng):
    return T("Nêu công thức tính diện tích xung quanh và thể tích của hình trụ, hình nón, hình cầu.", "Hình trụ: Sxq = 2πrh; V = πr²h.\nHình nón: Sxq = πrl; V = (1/3)πr²h.\nHình cầu: S = 4πr²; V = (4/3)πr³.", 1)
def b10_cn(rng):
    return T("Tại sao khi quay một hình chữ nhật quanh một cạnh ta được hình trụ? Nêu tên các yếu tố của hình trụ nhận được.", "Cạnh làm trục quay tạo thành trục (chiều cao h); cạnh kề tạo thành bán kính đáy r; cạnh đối diện tạo mặt xung quanh.", 1)

CHU_DE = [
    ("Chương 1: Phương trình và hệ phương trình bậc nhất hai ẩn", [a1_nghiem, a1_he, a1_he2, a1_he3, a1_vo, a1_vn, a1_bac1, a1_thuoc, a1_toanloi, a1_gia, a1_cong], [b1_he, b1_loi, b1_dg, b1_toan, b1_hv, b1_kt]),
    ("Chương 2: Phương trình và bất phương trình bậc nhất một ẩn", [a2_pt, a2_tich, a2_mau, a2_bpt, a2_bpt2, a2_bpt3, a2_nghiem, a2_dau, a2_cong, a2_nguyen, a2_maxn, a2_loi], [b2_pt, b2_bpt, b2_loi, b2_mau, b2_ss, b2_he]),
    ("Chương 3: Căn bậc hai và căn bậc ba", [a3_cbh, a3_cbh3, a3_cbh3_am, a3_dk, a3_dk2, a3_dua, a3_cong, a3_nhan, a3_chia, a3_rutgon, a3_ma, a3_bt], [b3_rutgon, b3_ma, b3_x, b3_dk, b3_ss, b3_cbh3]),
    ("Chương 4: Hệ thức lượng trong tam giác vuông", [a4_pyta, a4_goc, a4_cao, a4_ah2, a4_ab2, a4_sin, a4_cos, a4_tan, a4_gtlg, a4_gtlg2, a4_tan45, a4_goc2, a4_phu, a4_tinhcanh], [b4_giai, b4_cao, b4_goc, b4_toa, b4_bang, b4_pg]),
    ("Chương 5: Đường tròn", [a5_duong_kinh, a5_tam, a5_vt, a5_dd, a5_tiep, a5_goc_tam, a5_noi_tiep, a5_noi_tiep2, a5_day, a5_cung, a5_chuvi, a5_dt], [b5_cung, b5_day, b5_tt, b5_vi_tri, b5_cv, b5_tt2]),
    ("Chương 6: Hàm số y = ax² và phương trình bậc hai một ẩn", [a6_gt, a6_thuoc, a6_a, a6_bien, a6_delta, a6_nghiem, a6_vieta_s, a6_vieta_p, a6_nghiem_so, a6_tdt, a6_hs_c, a6_hinhchunhat], [b6_giai, b6_vieta, b6_do_thi, b6_loi, b6_dk, b6_pt]),
    ("Chương 7: Tần số và tần số tương đối", [a7_tong, a7_tsdt, a7_pt, a7_tong_tsdt, a7_tong_tan, a7_mot, a7_tb, a7_nhom, a7_tg, a7_bd, a7_cong, a7_hieu], [b7_bang, b7_tb, b7_mot, b7_nhom, b7_ts, b7_bd]),
    ("Chương 8: Xác suất của biến cố trong một số mô hình xác suất đơn giản", [a8_xuc, a8_tong, a8_doi, a8_hop, a8_hai, a8_dong, a8_dong2, a8_it_nhat, a8_the, a8_doi_p, a8_ban, a8_nhanh], [b8_xuc, b8_hop, b8_hai, b8_cay, b8_doi, b8_so]),
    ("Chương 9: Đường tròn ngoại tiếp và đường tròn nội tiếp", [a9_ngoai_tam, a9_noi_tam, a9_vuong, a9_deu, a9_deu2, a9_vuong_cang, a9_goc_tgnt, a9_vuong_tg, a9_nt_hv, a9_hcn, a9_thoi, a9_dcdt, a9_luc], [b9_vuong, b9_tgnt, b9_cm, b9_dd, b9_dk, b9_cv]),
    ("Chương 10: Một số hình khối trong thực tiễn (hình trụ, hình nón, hình cầu)", [a10_tru_v, a10_tru_sxq, a10_non_v, a10_non_sxq, a10_cau_v, a10_cau_s, a10_dg, a10_truc, a10_dtqt, a10_hcn_quay, a10_tg_quay, a10_nua], [b10_tru, b10_non, b10_cau, b10_loi, b10_phan, b10_cn]),
]
