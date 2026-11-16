from thcs import *
import math

def nz(rng, lo=-6, hi=6): return rng.choice([x for x in range(lo, hi + 1) if x])
def tt(x): return f"{x:g}".replace(".", ",")

# ===== 1. Mệnh đề và tập hợp =====
def a1_phu(rng):
    n = rng.randint(2, 30); return M(f"Mệnh đề phủ định của \"{n} là số nguyên tố\" là:", f"{n} không là số nguyên tố", [f"{n} là hợp số", f"{n} là số chẵn", f"{n} là số lẻ"], 1)
def a1_dung(rng):
    a = rng.randint(2, 20); return M(f"Mệnh đề nào đúng? (x ∈ ℝ)", "∀x, x² ≥ 0", ["∃x, x² < 0", "∀x, x² > 0", "∀x, x > x²"], 1)
def a1_AuB(rng):
    A = sorted(rng.sample(range(1, 10), 4)); B = sorted(rng.sample(range(1, 10), 4)); u = sorted(set(A) | set(B)); i = sorted(set(A) & set(B)); fa = lambda s: "{" + "; ".join(map(str, s)) + "}"
    return M(f"Cho A = {fa(A)}, B = {fa(B)}. Tập A ∪ B là:", fa(u), [fa(i) if i else "∅", fa(sorted(set(A) - set(B)) or [0]), fa(sorted(set(u) | {10}))], 1)
def a1_AnB(rng):
    A = sorted(rng.sample(range(1, 10), 5)); B = sorted(rng.sample(range(1, 10), 5)); u = sorted(set(A) | set(B)); i = sorted(set(A) & set(B)); fa = lambda s: "{" + "; ".join(map(str, s)) + "}"
    if not i or i == u: raise ValueError
    return M(f"Cho A = {fa(A)}, B = {fa(B)}. Tập A ∩ B là:", fa(i), [fa(u), fa(sorted(set(A) - set(B)) or [0]), fa(sorted(set(B) - set(A)) or [0])], 1)
def a1_hieu(rng):
    A = sorted(rng.sample(range(1, 10), 5)); B = sorted(rng.sample(range(1, 10), 5)); d = sorted(set(A) - set(B)); fa = lambda s: "{" + "; ".join(map(str, s)) + "}"
    if not d or d == A: raise ValueError
    return M(f"Cho A = {fa(A)}, B = {fa(B)}. Tập A \\ B là:", fa(d), [fa(sorted(set(B) - set(A)) or [0]), fa(sorted(set(A) & set(B)) or [0]), fa(sorted(set(A) | set(B)))], 2)
def a1_phantu(rng):
    n = rng.randint(2, 8); return nint(rng, f"Tập hợp A có {n} phần tử. Số tập con của A là:", 2 ** n, 2, (2, 4, 8), 0)
def a1_khoang(rng):
    a, b = sorted(rng.sample(range(-9, 10), 2)); return M(f"Tập hợp {{x ∈ ℝ | {a} < x ≤ {b}}} viết dưới dạng khoảng, nửa khoảng là:", f"({a}; {b}]", [f"[{a}; {b}]", f"[{a}; {b})", f"({a}; {b})"], 1)
def a1_giao_khoang(rng):
    a, b, c = sorted(rng.sample(range(-9, 12), 3)); d = rng.randint(c + 1, c + 5); return M(f"Cho A = [{a}; {c}], B = ({b}; {d}). Tập A ∩ B là:", f"({b}; {c}]", [f"[{b}; {c}]", f"({b}; {c})", f"[{a}; {d})"], 3)
def a1_hop_khoang(rng):
    a, b, c = sorted(rng.sample(range(-9, 12), 3)); d = rng.randint(c + 1, c + 5); return M(f"Cho A = [{a}; {c}], B = ({b}; {d}). Tập A ∪ B là:", f"[{a}; {d})", [f"({a}; {d})", f"[{a}; {d}]", f"({b}; {c}]"], 3)
def a1_keo(rng):
    return M("Kí hiệu P ⇒ Q là mệnh đề sai khi:", "P đúng, Q sai", ["P sai, Q đúng", "P sai, Q sai", "P đúng, Q đúng"], 1)
def a1_tuong(rng):
    return M("Mệnh đề P ⇔ Q đúng khi:", "P và Q cùng đúng hoặc cùng sai", ["P đúng, Q sai", "P sai, Q đúng", "Chỉ khi cả hai đúng"], 2)
def a1_dao(rng):
    return M("Mệnh đề đảo của \"Nếu a = b thì a² = b²\" là:", "Nếu a² = b² thì a = b", ["Nếu a ≠ b thì a² ≠ b²", "Nếu a = b thì a² ≠ b²", "a = b và a² = b²"], 2)
def a1_so(rng):
    n = rng.randint(10, 40); return nint(rng, f"Số phần tử của tập hợp các số nguyên dương nhỏ hơn hoặc bằng {n} là:", n, 1, (1, 2), 0)
def a1_chia(rng):
    k = rng.choice([3, 4, 5, 6, 7]); n = rng.randint(30, 100); return nint(rng, f"Số các số tự nhiên từ 1 đến {n} chia hết cho {k} là:", n // k, 1, (1, 2), 0)
def b1_tap(rng):
    A = sorted(rng.sample(range(1, 12), 6)); B = sorted(rng.sample(range(1, 12), 6)); fa = lambda s: "{" + "; ".join(map(str, s)) + "}"
    return T(f"Cho A = {fa(A)}, B = {fa(B)}. Xác định A ∪ B, A ∩ B, A \\ B, B \\ A.", f"A ∪ B = {fa(sorted(set(A) | set(B)))}\nA ∩ B = {fa(sorted(set(A) & set(B)))}\nA \\ B = {fa(sorted(set(A) - set(B)))}\nB \\ A = {fa(sorted(set(B) - set(A)))}", 2)
def b1_phu(rng):
    return T("Lập mệnh đề phủ định của \"∀x ∈ ℝ, x² - 2x + 2 > 0\" và xét tính đúng sai.", "Phủ định: ∃x ∈ ℝ, x² - 2x + 2 ≤ 0. Vì x² - 2x + 2 = (x - 1)² + 1 > 0 nên mệnh đề ban đầu đúng, phủ định sai.", 2)
def b1_khoang(rng):
    a, b, c, d = sorted(rng.sample(range(-9, 12), 4)); return T(f"Cho A = [{a}; {c}], B = ({b}; {d}). Tìm A ∩ B, A ∪ B, A \\ B.", f"A ∩ B = ({b}; {c}]\nA ∪ B = [{a}; {d})\nA \\ B = [{a}; {b}]", 3)
def b1_tap_con(rng):
    return T("Liệt kê tất cả các tập con của tập A = {a; b; c}.", "∅; {a}; {b}; {c}; {a; b}; {a; c}; {b; c}; {a; b; c} (8 tập con).", 1)
def b1_dem(rng):
    n, a, b = rng.randint(40, 60), rng.randint(15, 30), rng.randint(15, 30); c = rng.randint(2, min(a, b) - 1)
    if a + b - c > n: raise ValueError
    return T(f"Lớp có {n} học sinh, {a} em thích bóng đá, {b} em thích bóng chuyền, {c} em thích cả hai. Có bao nhiêu em không thích môn nào?", f"Số em thích ít nhất một môn: {a} + {b} - {c} = {a + b - c}\nKhông thích môn nào: {n} - {a + b - c} = {n - a - b + c}.", 2)
def b1_dk(rng):
    return T("Phát biểu mệnh đề \"P ⇒ Q\" dưới dạng điều kiện đủ, điều kiện cần cho: P: \"tứ giác là hình chữ nhật\", Q: \"tứ giác có hai đường chéo bằng nhau\".", "P là điều kiện đủ để có Q; Q là điều kiện cần để có P.", 2)

# ===== 2. Bất phương trình và hệ bất phương trình bậc nhất hai ẩn =====
def a2_thuoc(rng):
    a, b, c = nz(rng, -4, 4), nz(rng, -4, 4), rng.randint(-6, 6); x, y = rng.randint(-3, 3), rng.randint(-3, 3); v = a * x + b * y
    kq = "thuộc" if v > c else "không thuộc"; return M(f"Điểm ({x}; {y}) {'thuộc' if v > c else 'không thuộc'} miền nghiệm của bất phương trình {da2({(1,0): a, (0,1): b})} > {c}? Chọn câu đúng:", f"Đúng, vì {a}·({x}) + {b}·({y}) = {v} {'>' if v > c else '≤'} {c}", [f"Sai, vì giá trị biểu thức là {v + 1}", f"Chỉ đúng khi {c} < 0", f"Không xác định được"], 2) if False else M(f"Điểm ({x}; {y}) có là nghiệm của bất phương trình {da2({(1,0): a, (0,1): b})} > {c} không?", "Có" if v > c else "Không", ["Không" if v > c else "Có", "Chỉ khi x > 0", "Không xác định"], 1)
def a2_bd(rng):
    return M("Miền nghiệm của bất phương trình ax + by ≤ c (không có biên) là:", "Nửa mặt phẳng có bờ là đường thẳng ax + by = c", ["Đường thẳng ax + by = c", "Toàn bộ mặt phẳng", "Một điểm"], 1)
def a2_bien(rng):
    return M("Đường thẳng ax + by = c được vẽ nét liền khi bất phương trình có dấu:", "≥ hoặc ≤", ["> hoặc <", "= hoặc ≠", "Mọi dấu"], 1)
def a2_goc(rng):
    a, b = nz(rng, -3, 3), nz(rng, -3, 3); c = rng.randint(1, 6); return M(f"Điểm O(0; 0) có thuộc miền nghiệm của {da2({(1,0): a, (0,1): b})} < {c} không?", "Có", ["Không", "Chỉ khi a > 0", "Chỉ khi b > 0"], 1)
def a2_he(rng):
    x, y = rng.randint(1, 4), rng.randint(1, 4); return M(f"Điểm ({x}; {y}) có thuộc miền nghiệm của hệ {{x > 0; y > 0; x + y < {x + y + 1}}} không?", "Có", ["Không", "Chỉ khi x > y", "Không xác định"], 2)
def a2_he2(rng):
    x, y = rng.randint(1, 4), rng.randint(1, 4); return M(f"Điểm ({x}; {y}) có thuộc miền nghiệm của hệ {{x ≥ 0; y ≥ 0; x + y ≤ {x + y - 1}}} không?", "Không", ["Có", "Chỉ khi x = y", "Không xác định"], 2)
def a2_dinh(rng):
    return M("Giá trị lớn nhất của biểu thức F(x; y) = ax + by trên một đa giác lồi đạt tại:", "Một đỉnh của đa giác", ["Điểm trong đa giác", "Trung điểm một cạnh", "Gốc tọa độ"], 2)
def a2_toiuu(rng):
    p = [(0, 0), (4, 0), (0, 3), (2, 2)]; a, b = rng.randint(1, 4), rng.randint(1, 4); v = [a * x + b * y for x, y in p]; return nint(rng, f"Miền đa giác có các đỉnh (0;0), (4;0), (0;3), (2;2). Giá trị lớn nhất của F = {a}x + {b}y là:", max(v), 2, (1, 2, 3), 0)
def a2_toiuu2(rng):
    p = [(0, 0), (4, 0), (0, 3), (2, 2)]; a, b = rng.randint(1, 4), rng.randint(1, 4); v = [a * x + b * y for x, y in p]; return nint(rng, f"Miền đa giác có các đỉnh (0;0), (4;0), (0;3), (2;2). Giá trị nhỏ nhất của F = {a}x + {b}y là:", min(v), 2, (1, 2, 3), 0)
def a2_cat(rng):
    a = rng.randint(1, 6); return M(f"Đường thẳng x = {a} chia mặt phẳng thành mấy nửa mặt phẳng?", 2, [1, 3, 4], 2)
def a2_truc(rng):
    return M("Miền nghiệm của bất phương trình x > 0 là nửa mặt phẳng:", "Bên phải trục tung", ["Bên trái trục tung", "Phía trên trục hoành", "Phía dưới trục hoành"], 1)
def a2_truc2(rng):
    return M("Miền nghiệm của bất phương trình y < 0 là nửa mặt phẳng:", "Phía dưới trục hoành", ["Phía trên trục hoành", "Bên phải trục tung", "Bên trái trục tung"], 1)
def b2_ve(rng):
    a, b, c = nz(rng, -4, 4), nz(rng, -4, 4), rng.randint(-6, 6); return T(f"Biểu diễn miền nghiệm của bất phương trình {da2({(1,0): a, (0,1): b})} ≤ {c}.", f"Vẽ đường thẳng d: {da2({(1,0): a, (0,1): b})} = {c} (nét liền). Lấy điểm O(0; 0): {0} ≤ {c} {'đúng' if 0 <= c else 'sai'} nên miền nghiệm là nửa mặt phẳng bờ d {'chứa' if 0 <= c else 'không chứa'} điểm O (kể cả bờ).", 2)
def b2_loi(rng):
    a, b = rng.randint(2, 5), rng.randint(2, 5); return T(f"Một xưởng làm hai loại sản phẩm. Loại I lãi {a} triệu đồng, loại II lãi {b} triệu đồng. Gọi x, y là số sản phẩm mỗi loại. Viết biểu thức tổng lãi và các điều kiện ràng buộc cơ bản.", f"Tổng lãi F = {a}x + {b}y (triệu đồng); điều kiện x ≥ 0, y ≥ 0 cùng các ràng buộc về nguyên liệu, thời gian.", 2)
def b2_he(rng):
    return T("Biểu diễn miền nghiệm của hệ {x ≥ 0; y ≥ 0; x + y ≤ 4}.", "Là tam giác OAB với O(0;0), A(4;0), B(0;4) (kể cả biên).", 2)
def b2_toiuu(rng):
    a, b = rng.randint(1, 4), rng.randint(1, 4); v = {"O(0;0)": 0, "A(4;0)": 4 * a, "B(0;4)": 4 * b}; return T(f"Trên miền tam giác OAB với O(0;0), A(4;0), B(0;4), tìm giá trị lớn nhất của F = {a}x + {b}y.", f"F(O) = 0; F(A) = {4 * a}; F(B) = {4 * b}. Giá trị lớn nhất là {max(v.values())}.", 3)
def b2_kt(rng):
    return T("Nêu cách xác định miền nghiệm của bất phương trình bậc nhất hai ẩn.", "Vẽ đường thẳng ax + by = c; lấy một điểm không thuộc đường thẳng, thay vào bất phương trình; nếu thỏa mãn thì miền nghiệm là nửa mặt phẳng bờ chứa điểm đó, ngược lại là nửa mặt phẳng còn lại.", 1)

# ===== 3. Hàm số bậc hai =====
def a3_dinh(rng):
    a, b, c = nz(rng, -3, 3), nz(rng, -6, 6), rng.randint(-5, 5)
    if b % (2 * a): raise ValueError
    x = -b // (2 * a); return nint(rng, f"Hoành độ đỉnh của parabol y = {da([a, b, c])} là:", x, 1, (1, 2, 3))
def a3_dinh_y(rng):
    a, p, q = nz(rng, -3, 3), rng.randint(-4, 4), rng.randint(-6, 6); b, c = -2 * a * p, a * p * p + q; return nint(rng, f"Tung độ đỉnh của parabol y = {da([a, b, c])} là:", q, 2, (1, 2, 3))
def a3_truc(rng):
    a, p = nz(rng, -3, 3), rng.randint(-5, 5); b = -2 * a * p; return M(f"Trục đối xứng của parabol y = {da([a, b, 1])} là đường thẳng:", f"x = {p}", [f"x = {-p}", f"y = {p}", f"x = {p + 1}"], 2)
def a3_bien(rng):
    a = nz(rng, -3, 3); return M(f"Hàm số y = {da([a, 2, 1])} đồng biến/nghịch biến thế nào? Bề lõm của parabol hướng:", "lên trên" if a > 0 else "xuống dưới", ["xuống dưới" if a > 0 else "lên trên", "sang trái", "sang phải"], 1)
def a3_giatri(rng):
    a, b, c, x = nz(rng, -3, 3), rng.randint(-5, 5), rng.randint(-5, 5), rng.randint(-3, 4); return nint(rng, f"Giá trị của hàm số y = {da([a, b, c])} tại x = {x} là:", a * x * x + b * x + c, 1, (1, 2, 5))
def a3_cuc(rng):
    a, p, q = nz(rng, -3, 3), rng.randint(-4, 4), rng.randint(-6, 6); b, c = -2 * a * p, a * p * p + q; return M(f"Hàm số y = {da([a, b, c])} có giá trị {'nhỏ' if a > 0 else 'lớn'} nhất bằng:", q, [q + 1, q - 1, -q if q else 2], 2)
def a3_cat(rng):
    c = rng.randint(-8, 8); return M(f"Parabol y = ax² + bx + {c} cắt trục Oy tại điểm:", f"(0; {c})", [f"({c}; 0)", f"(0; {-c})" if c else "(1; 0)", f"({-c}; 0)" if c else "(0; 1)"], 1)
def a3_qua(rng):
    a, b, x = rng.randint(1, 3), rng.randint(-4, 4), rng.randint(1, 3); c = rng.randint(-3, 3); y = a * x * x + b * x + c; return M(f"Parabol y = {da([a, b, c])} đi qua điểm nào?", f"({x}; {y})", [f"({x}; {y + 1})", f"({x + 1}; {y})", f"({x}; {-y if y else 2})"], 2)
def a3_pt(rng):
    a, b, c = 1, rng.randint(-6, 6), rng.randint(-8, 8); return M(f"Parabol y = {da([a, b, c])} cắt trục hoành tại hai điểm phân biệt khi:", "Δ > 0", ["Δ = 0", "Δ < 0", "c > 0"], 1)
def a3_toi(rng):
    a, p, q = rng.randint(1, 3), rng.randint(-4, 4), rng.randint(-6, 6); b, c = -2 * a * p, a * p * p + q; return M(f"Hàm số y = {da([a, b, c])} nghịch biến trên khoảng:", f"(-∞; {p})", [f"({p}; +∞)", f"(-∞; {-p})", f"({-p}; +∞)"], 2)
def a3_delta(rng):
    a, b, c = nz(rng, -3, 3), nz(rng, -6, 6), nz(rng, -6, 6); return nint(rng, f"Biệt thức Δ của y = {da([a, b, c])} là:", b * b - 4 * a * c, 2, (4, 8, 2))
def a3_tdx(rng):
    a, p, q = nz(rng, -3, 3), rng.randint(-4, 4), rng.randint(-6, 6); b, c = -2 * a * p, a * p * p + q; return M(f"Tọa độ đỉnh của parabol y = {da([a, b, c])} là:", f"({p}; {q})", [f"({-p}; {q})", f"({p}; {-q})" if q else f"({p}; 1)", f"({q}; {p})" if q != p else f"({p + 1}; {q})"], 3)
def b3_khao_sat(rng):
    a, p, q = nz(rng, -3, 3), rng.randint(-4, 4), rng.randint(-5, 5); b, c = -2 * a * p, a * p * p + q; return T(f"Khảo sát và vẽ đồ thị hàm số y = {da([a, b, c])}.", f"Đỉnh I({p}; {q}), trục đối xứng x = {p}, bề lõm hướng {'lên' if a > 0 else 'xuống'}.\nGiao Oy: (0; {c}). Lập bảng biến thiên và lấy thêm điểm đối xứng qua trục để vẽ parabol.", 3)
def b3_xd(rng):
    a, b, c = rng.randint(1, 3), rng.randint(-4, 4), rng.randint(-4, 4); x1, x2 = 1, 2
    return T(f"Xác định parabol y = ax² + bx + c biết đồ thị đi qua A(0; {c}), B(1; {a + b + c}), C(-1; {a - b + c}).", f"A: c = {c}. B: a + b + c = {a + b + c}; C: a - b + c = {a - b + c}.\nCộng/trừ: a = {a}, b = {b}. Vậy y = {da([a, b, c])}.", 3)
def b3_max(rng):
    a = rng.randint(2, 6); return T(f"Tìm giá trị lớn nhất của y = -x² + {2 * a}x + 1.", f"y = -(x - {a})² + {a * a + 1} ≤ {a * a + 1}. Giá trị lớn nhất bằng {a * a + 1} tại x = {a}.", 2)
def b3_tt(rng):
    h = rng.randint(2, 6); return T(f"Một quả bóng chuyển động theo quỹ đạo y = -x² + {2 * h}x (x: tầm xa, y: độ cao, đơn vị m). Tìm độ cao cực đại.", f"Đỉnh tại x = {h}, y = {h * h}. Độ cao cực đại là {h * h} m.", 2)
def b3_tuong(rng):
    return T("Nêu cách tìm tọa độ giao điểm của parabol y = ax² + bx + c với trục hoành và trục tung.", "Giao Oy: cho x = 0 ⇒ (0; c). Giao Ox: giải ax² + bx + c = 0.", 1)
def b3_gt(rng):
    m = rng.randint(1, 5); return T(f"Tìm m để parabol y = x² - 4x + m cắt trục hoành tại hai điểm phân biệt.", "Δ' = 4 - m > 0 ⇒ m < 4.", 2)

# ===== 4. Hệ thức lượng trong tam giác =====
def a4_cos(rng):
    a, b, C = rng.choice([(3, 5, 60), (4, 6, 60), (5, 8, 60), (2, 3, 60)]); c2 = a * a + b * b - a * b; return M(f"Tam giác ABC có AC = {a}, BC = {b}, góc C = 60°. AB² bằng:", c2, [a * a + b * b + a * b, a * a + b * b, a * a + b * b - 2 * a * b], 2)
def a4_sin(rng):
    a, A = rng.choice([(6, 30), (10, 30), (8, 30)]); R = a; return nint(rng, f"Tam giác ABC có BC = {a}, góc A = 30°. Bán kính đường tròn ngoại tiếp R = a/(2sinA) bằng:", a, 2, (1, 2, 3), 0)
def a4_dt(rng):
    a, b = rng.randint(3, 12), rng.randint(3, 12); return M(f"Tam giác ABC có AB = {a}, AC = {b}, góc A = 30°. Diện tích tam giác là:", ps(Fraction(a * b, 4)), [ps(Fraction(a * b, 2)), ps(Fraction(a * b)), ps(Fraction(a * b, 3))], 2)
def a4_heron(rng):
    a, b, c = rng.choice([(3, 4, 5), (5, 12, 13), (13, 14, 15), (6, 8, 10), (7, 24, 25)]); p = (a + b + c) / 2; s = math.sqrt(p * (p - a) * (p - b) * (p - c)); return nint(rng, f"Tam giác có ba cạnh {a}, {b}, {c}. Diện tích (công thức Heron) là:", int(round(s)), 3, (1, 2, 3), 0)
def a4_p(rng):
    a, b, c = rng.randint(3, 10), rng.randint(3, 10), rng.randint(3, 10)
    if a + b <= c or a + c <= b or b + c <= a or (a + b + c) % 2: raise ValueError
    return nint(rng, f"Tam giác có ba cạnh {a}, {b}, {c}. Nửa chu vi p là:", (a + b + c) // 2, 1, (1, 2), 0)
def a4_r(rng):
    a, b, c = rng.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (13, 14, 15)]); p = (a + b + c) / 2; s = math.sqrt(p * (p - a) * (p - b) * (p - c)); return M(f"Tam giác có ba cạnh {a}, {b}, {c}. Bán kính đường tròn nội tiếp r = S/p là:", tt(s / p), [tt(s / p + 1), tt(s / p * 2), tt(max(s / p - 1, 0.5))], 3)
def a4_cosA(rng):
    a, b, c = rng.choice([(3, 4, 5), (5, 12, 13), (5, 7, 8)]); num = b * b + c * c - a * a; den = 2 * b * c; f = Fraction(num, den); return M(f"Tam giác ABC có a = BC = {a}, b = CA = {b}, c = AB = {c}. cos A bằng:", ps(f), nh_ps(rng, f) if abs(f) < 1 and f > 0 else [ps(f + 1), ps(-f), ps(f * 2)], 3)
def a4_trung(rng):
    a, b, c = rng.choice([(6, 8, 10), (4, 6, 8), (6, 6, 6), (10, 12, 14)]); m2 = Fraction(2 * (b * b + c * c) - a * a, 4); return M(f"Tam giác ABC có a = {a}, b = {b}, c = {c}. Độ dài trung tuyến AM thỏa m² = (2b² + 2c² - a²)/4. Giá trị m² là:", ps(m2), [ps(m2 + 1), ps(m2 * 2), ps(m2 - 1)], 3)
def a4_gtlg(rng):
    return M("Với 0° < α < 180°, sin α = sin(…)?", "180° - α", ["α - 180°", "90° - α", "α + 180°"], 1)
def a4_cosphu(rng):
    return M("cos(180° - α) bằng:", "-cos α", ["cos α", "sin α", "-sin α"], 1)
def a4_goc(rng):
    A, B = rng.randint(30, 80), rng.randint(30, 80); return nint(rng, f"Tam giác ABC có góc A = {A}°, B = {B}°. Số đo góc C là (độ):", 180 - A - B, 1, (5, 10, 20), 0)
def a4_ban(rng):
    return M("Định lí sin trong tam giác ABC: a/sinA = b/sinB = c/sinC bằng:", "2R", ["R", "R/2", "4R"], 1)
def b4_giai(rng):
    a, b = rng.randint(4, 10), rng.randint(4, 10); return T(f"Tam giác ABC có AB = {a}, AC = {b}, góc A = 60°. Tính BC và diện tích.", f"BC² = {a}² + {b}² - 2·{a}·{b}·cos60° = {a * a + b * b - a * b} ⇒ BC = √{a * a + b * b - a * b}\nS = (1/2)·{a}·{b}·sin60° = {ps(Fraction(a * b, 4))}√3", 3)
def b4_heron(rng):
    a, b, c = rng.choice([(13, 14, 15), (5, 12, 13), (3, 4, 5), (7, 8, 9)]); p = (a + b + c) / 2; s = math.sqrt(p * (p - a) * (p - b) * (p - c)); return T(f"Tam giác ABC có a = {a}, b = {b}, c = {c}. Tính diện tích, bán kính nội tiếp r và ngoại tiếp R.", f"p = {tt(p)}; S = {tt(round(s, 2))}\nr = S/p = {tt(round(s / p, 2))}; R = abc/(4S) = {tt(round(a * b * c / (4 * s), 2))}", 3)
def b4_goc(rng):
    a, b, c = rng.choice([(5, 7, 8), (4, 5, 6), (6, 7, 8)]); return T(f"Tam giác ABC có a = {a}, b = {b}, c = {c}. Tính cos A.", f"cos A = (b² + c² - a²)/(2bc) = ({b * b + c * c - a * a})/{2 * b * c} = {pf(b * b + c * c - a * a, 2 * b * c)}", 2)
def b4_do_cao(rng):
    a = rng.randint(10, 30); B = rng.choice([30, 45, 60]); return T(f"Từ hai điểm A, B cách nhau {a} m, đo góc nhìn đỉnh tháp là α = {B}° và β = 90° tại hai điểm. Nêu hướng áp dụng định lí sin hoặc cosin để tính khoảng cách.", "Lập tam giác có đỉnh là chân đo và đỉnh tháp, tính các góc còn lại, áp dụng định lí sin: x/sinα = AB/sin(góc đối) rồi suy ra chiều cao.", 2)
def b4_phat(rng):
    return T("Phát biểu định lí cosin và định lí sin trong tam giác.", "a² = b² + c² - 2bc·cosA (và tương tự); a/sinA = b/sinB = c/sinC = 2R.", 1)
def b4_ct(rng):
    return T("Nêu các công thức tính diện tích tam giác theo a, b, c và R, r.", "S = (1/2)ab·sinC = abc/(4R) = pr = √(p(p-a)(p-b)(p-c)).", 1)

# ===== 5. Vectơ =====
def a5_cong(rng):
    a, b = rng.randint(-5, 5), rng.randint(-5, 5); c, d = rng.randint(-5, 5), rng.randint(-5, 5); return M(f"Cho u = ({a}; {b}), v = ({c}; {d}). Tọa độ u + v là:", f"({a + c}; {b + d})", [f"({a - c}; {b - d})", f"({a + c}; {b - d})", f"({a * c}; {b * d})"], 1)
def a5_hieu(rng):
    a, b, c, d = [rng.randint(-5, 5) for _ in range(4)]; return M(f"Cho u = ({a}; {b}), v = ({c}; {d}). Tọa độ u - v là:", f"({a - c}; {b - d})", [f"({a + c}; {b + d})", f"({c - a}; {d - b})" if (c - a, d - b) != (a - c, b - d) else f"({a}; {b})", f"({a - c}; {b + d})"], 1)
def a5_nhan(rng):
    a, b, k = rng.randint(-5, 5), rng.randint(-5, 5), nz(rng, -4, 4); return M(f"Cho u = ({a}; {b}). Tọa độ {k}u là:", f"({k * a}; {k * b})", [f"({a + k}; {b + k})", f"({k * a}; {b})", f"({a}; {k * b})"], 1)
def a5_dai(rng):
    a, b = rng.choice([(3, 4), (5, 12), (6, 8), (8, 15)]); return nint(rng, f"Độ dài của vectơ u = ({a}; {b}) là:", math.isqrt(a * a + b * b), 1, (1, 2, 3), 0)
def a5_ab(rng):
    xa, ya, xb, yb = [rng.randint(-5, 6) for _ in range(4)]; return M(f"Cho A({xa}; {ya}), B({xb}; {yb}). Tọa độ AB là:", f"({xb - xa}; {yb - ya})", [f"({xa - xb}; {ya - yb})", f"({xa + xb}; {ya + yb})", f"({xb - xa}; {ya - yb})"], 1)
def a5_trungdiem(rng):
    xa, ya = rng.randint(-4, 4) * 2, rng.randint(-4, 4) * 2; xb, yb = rng.randint(-4, 4) * 2, rng.randint(-4, 4) * 2; return M(f"Trung điểm M của A({xa}; {ya}), B({xb}; {yb}) có tọa độ:", f"({(xa + xb) // 2}; {(ya + yb) // 2})", [f"({xa + xb}; {ya + yb})", f"({xb - xa}; {yb - ya})", f"({(xa + xb) // 2}; {(ya - yb) // 2})"], 1)
def a5_trongtam(rng):
    xs, ys = [rng.randint(-4, 4) * 3 for _ in range(3)], [rng.randint(-4, 4) * 3 for _ in range(3)]; return M(f"Tam giác ABC có A({xs[0]}; {ys[0]}), B({xs[1]}; {ys[1]}), C({xs[2]}; {ys[2]}). Tọa độ trọng tâm G là:", f"({sum(xs) // 3}; {sum(ys) // 3})", [f"({sum(xs)}; {sum(ys)})", f"({sum(xs) // 3}; {-sum(ys) // 3})" if sum(ys) else f"({sum(xs) // 3}; 1)", f"({sum(xs) // 2}; {sum(ys) // 2})"], 2)
def a5_tichvo(rng):
    a, b, c, d = [rng.randint(-5, 5) for _ in range(4)]; return nint(rng, f"Cho u = ({a}; {b}), v = ({c}; {d}). Tích vô hướng u·v bằng:", a * c + b * d, 1, (1, 2, 3))
def a5_vuong(rng):
    a, b = nz(rng, -5, 5), nz(rng, -5, 5); return M(f"Vectơ nào vuông góc với u = ({a}; {b})?", f"({-b}; {a})", [f"({b}; {a})" if b != -b or a != a else f"({a}; {b})", f"({a}; {b})", f"({-a}; {-b})"], 2) if a * a != b * b or True else None
def a5_cungphuong(rng):
    a, b, k = rng.randint(1, 5), rng.randint(1, 5), rng.randint(2, 4); return M(f"Hai vectơ u = ({a}; {b}) và v = ({k * a}; {k * b}) là:", "Cùng phương", ["Vuông góc", "Đối nhau", "Bằng nhau"], 1)
def a5_hbh(rng):
    return M("Với hình bình hành ABCD, vectơ AB + AD bằng:", "AC", ["BD", "DB", "CA"], 1)
def a5_chasles(rng):
    return M("Với ba điểm A, B, C bất kì, AB + BC bằng:", "AC", ["CA", "BA", "AB"], 1)
def a5_goc(rng):
    return M("Tích vô hướng a·b = |a||b|cos(a, b). Khi a ⊥ b thì a·b bằng:", 0, [1, -1, "|a||b|"], 1)
def b5_toado(rng):
    xa, ya, xb, yb, xc, yc = [rng.randint(-5, 6) for _ in range(6)]; return T(f"Cho A({xa}; {ya}), B({xb}; {yb}), C({xc}; {yc}). Tìm tọa độ AB, AC và trung điểm BC.", f"AB = ({xb - xa}; {yb - ya}); AC = ({xc - xa}; {yc - ya})\nTrung điểm BC: ({tt((xb + xc) / 2)}; {tt((yb + yc) / 2)})", 2)
def b5_hbh(rng):
    xa, ya, xb, yb, xc, yc = [rng.randint(-4, 5) for _ in range(6)]; return T(f"Cho A({xa}; {ya}), B({xb}; {yb}), C({xc}; {yc}). Tìm tọa độ D để ABCD là hình bình hành.", f"AB = DC ⇒ D = A + C - B = ({xa + xc - xb}; {ya + yc - yb})", 3)
def b5_goc(rng):
    a, b, c, d = rng.choice([(1, 0, 1, 1), (1, 1, 1, 0), (1, 2, 2, 1), (2, 1, 1, 3)]); n = a * c + b * d; return T(f"Tính cosin góc giữa hai vectơ u = ({a}; {b}) và v = ({c}; {d}).", f"u·v = {n}; |u| = √{a * a + b * b}; |v| = √{c * c + d * d}.\ncos(u, v) = {n}/√{(a * a + b * b) * (c * c + d * d)}", 3)
def b5_cm(rng):
    return T("Chứng minh với I là trung điểm AB thì MA + MB = 2MI với mọi điểm M.", "MA + MB = (MI + IA) + (MI + IB) = 2MI + (IA + IB) = 2MI vì IA + IB = 0.", 2)
def b5_phat(rng):
    return T("Nêu quy tắc ba điểm, quy tắc hình bình hành và quy tắc trừ vectơ.", "AB + BC = AC; ABCD là hình bình hành thì AB + AD = AC; AB - AC = CB.", 1)
def b5_tichvo(rng):
    a, b = rng.randint(2, 8), rng.randint(2, 8); return T(f"Cho |a| = {a}, |b| = {b}, góc giữa hai vectơ là 60°. Tính a·b và |a + b|².", f"a·b = {a}·{b}·cos60° = {tt(a * b / 2)}\n|a + b|² = {a * a} + {b * b} + 2·{tt(a * b / 2)} = {a * a + b * b + a * b}", 3)

# ===== 6. Thống kê =====
def _s(rng, n=7): return sorted(rng.randint(2, 20) for _ in range(n))
def a6_tb(rng):
    xs = _s(rng, 5)
    if sum(xs) % 5: raise ValueError
    return nint(rng, f"Số trung bình cộng của {', '.join(map(str, xs))} là:", sum(xs) // 5, 2, (1, 2), 0)
def a6_med(rng):
    xs = _s(rng, 7); return nint(rng, f"Trung vị của mẫu số liệu {', '.join(map(str, xs))} là:", xs[3], 2, (1, 2), 0)
def a6_med2(rng):
    xs = _s(rng, 6)
    if (xs[2] + xs[3]) % 2: raise ValueError
    return nint(rng, f"Trung vị của mẫu số liệu {', '.join(map(str, xs))} là:", (xs[2] + xs[3]) // 2, 2, (1, 2), 0)
def a6_mot(rng):
    xs = _s(rng, 8); k = xs[2]; xs = sorted(xs + [k, k]) 
    from collections import Counter; c = Counter(xs)
    if c.most_common(2)[0][1] == c.most_common(2)[1][1]: raise ValueError
    return nint(rng, f"Mốt của mẫu số liệu {', '.join(map(str, xs))} là:", c.most_common(1)[0][0], 2, (1, 2), 0)
def a6_kt(rng):
    xs = _s(rng, 6); return nint(rng, f"Khoảng biến thiên của mẫu {', '.join(map(str, xs))} là:", xs[-1] - xs[0], 1, (1, 2), 0)
def a6_q(rng):
    xs = sorted(rng.sample(range(1, 30), 8)); q1 = (xs[1] + xs[2]) / 2; return M(f"Mẫu số liệu {', '.join(map(str, xs))}. Tứ phân vị thứ nhất Q₁ là:", tt(q1), [tt(q1 + 1), tt(q1 - 1), tt(xs[3])], 3)
def a6_q3(rng):
    xs = sorted(rng.sample(range(1, 30), 8)); q3 = (xs[5] + xs[6]) / 2; return M(f"Mẫu số liệu {', '.join(map(str, xs))}. Tứ phân vị thứ ba Q₃ là:", tt(q3), [tt(q3 + 1), tt(q3 - 1), tt(xs[4])], 3)
def a6_dq(rng):
    xs = sorted(rng.sample(range(1, 30), 8)); q1 = (xs[1] + xs[2]) / 2; q3 = (xs[5] + xs[6]) / 2; return M(f"Mẫu số liệu {', '.join(map(str, xs))}. Khoảng tứ phân vị ΔQ là:", tt(q3 - q1), [tt(q3 - q1 + 2), tt(q3 + q1), tt(xs[-1] - xs[0])], 3)
def a6_pv(rng):
    xs = [rng.randint(3, 10) for _ in range(6)]; m = sum(xs) / 6; v = sum((x - m) ** 2 for x in xs) / 6; return M(f"Phương sai của mẫu {', '.join(map(str, xs))} (làm tròn đến 0,01) là:", f"{v:.2f}".replace(".", ","), [f"{v + 1:.2f}".replace(".", ","), f"{math.sqrt(v):.2f}".replace(".", ",") if v != math.sqrt(v) else f"{v + 2:.2f}".replace(".", ","), f"{v * 2:.2f}".replace(".", ",")], 3)
def a6_sd(rng):
    return M("Độ lệch chuẩn của mẫu số liệu bằng:", "Căn bậc hai của phương sai", ["Bình phương phương sai", "Phương sai chia 2", "Hiệu giá trị lớn nhất và nhỏ nhất"], 1)
def a6_outlier(rng):
    return M("Giá trị bất thường của mẫu số liệu là giá trị nằm ngoài khoảng:", "(Q₁ - 1,5ΔQ; Q₃ + 1,5ΔQ)", ["(Q₁; Q₃)", "(x_min; x_max)", "(Q₁ - ΔQ; Q₃ + ΔQ)"], 3)
def a6_mau(rng):
    return M("Số liệu thống kê nào bị ảnh hưởng nhiều nhất bởi giá trị bất thường?", "Số trung bình", ["Trung vị", "Mốt", "Tứ phân vị"], 2)
def b6_tb(rng):
    xs = [rng.randint(4, 10) for _ in range(8)]; m = sum(xs) / 8; v = sum((x - m) ** 2 for x in xs) / 8; return T(f"Điểm 8 bài kiểm tra: {', '.join(map(str, xs))}. Tính trung bình, phương sai và độ lệch chuẩn.", f"Trung bình = {tt(round(m, 2))}\nPhương sai = {tt(round(v, 2))}\nĐộ lệch chuẩn = {tt(round(math.sqrt(v), 2))}", 2)
def b6_q(rng):
    xs = sorted(rng.sample(range(1, 30), 9)); q1 = (xs[1] + xs[2]) / 2; q2 = xs[4]; q3 = (xs[6] + xs[7]) / 2; return T(f"Cho mẫu số liệu {', '.join(map(str, xs))}. Tìm các tứ phân vị và khoảng tứ phân vị.", f"Q₂ = {q2}; Q₁ = {tt(q1)}; Q₃ = {tt(q3)}; ΔQ = {tt(q3 - q1)}", 2)
def b6_ngoai(rng):
    xs = sorted(rng.sample(range(1, 20), 7)) + [60]; return T(f"Mẫu số liệu {', '.join(map(str, xs))}. Cho biết 60 có phải là giá trị bất thường không (xét theo quy tắc 1,5ΔQ).", "Tính Q₁, Q₃, ΔQ; so sánh 60 với Q₃ + 1,5ΔQ; vì 60 lớn hơn giới hạn nên là giá trị bất thường.", 3)
def b6_so(rng):
    return T("Khi nào nên dùng trung vị thay cho số trung bình để đại diện cho mẫu số liệu?", "Khi mẫu có giá trị bất thường (quá lớn/quá nhỏ), vì trung vị không bị ảnh hưởng nhiều.", 1)
def b6_dt(rng):
    return T("Nêu ý nghĩa của khoảng biến thiên, khoảng tứ phân vị, phương sai và độ lệch chuẩn.", "Đều đo mức độ phân tán của số liệu: giá trị càng lớn thì số liệu càng phân tán; khoảng tứ phân vị ít bị ảnh hưởng bởi giá trị bất thường.", 1)

# ===== 7. Bất phương trình bậc hai một ẩn / tam thức =====
def a7_dau(rng):
    return M("Tam thức f(x) = ax² + bx + c với a > 0, Δ < 0 thì:", "f(x) > 0 với mọi x", ["f(x) < 0 với mọi x", "f(x) có hai nghiệm", "f(x) ≥ 0 chỉ tại một điểm"], 1)
def xs(a): return f"(x - {a})" if a >= 0 else f"(x + {-a})"
def a7_bpt(rng):
    a, b = sorted(rng.sample(range(-8, 9), 2)); return M(f"Tập nghiệm của bất phương trình {xs(a)}{xs(b)} < 0 là:", f"({a}; {b})", [f"(-∞; {a}) ∪ ({b}; +∞)", f"[{a}; {b}]", f"({b}; {a})"], 2) if a != b else None
def a7_bpt2(rng):
    a, b = sorted(rng.sample(range(-8, 9), 2)); return M(f"Tập nghiệm của bất phương trình {xs(a)}{xs(b)} > 0 là:", f"(-∞; {a}) ∪ ({b}; +∞)", [f"({a}; {b})", f"[{a}; {b}]", f"(-∞; {a}] ∪ [{b}; +∞)"], 2)
def a7_pt(rng):
    p, q = rng.randint(1, 8), rng.randint(1, 8); return M(f"Giải phương trình √(x + {p * p}) = x (x ≥ 0). Bình phương hai vế ta được phương trình:", f"x² - x - {p * p} = 0", [f"x² + x - {p * p} = 0", f"x² - x + {p * p} = 0", f"x² - {p * p} = 0"], 3)
def a7_delta(rng):
    a, b, c = nz(rng, -3, 3), nz(rng, -5, 5), nz(rng, -5, 5); return nint(rng, f"Biệt thức Δ của f(x) = {da([a, b, c])} là:", b * b - 4 * a * c, 2, (4, 8, 2))
def a7_vn(rng):
    a = rng.randint(1, 5); return M(f"Bất phương trình x² + {a * a} > 0 có tập nghiệm là:", "ℝ", ["∅", f"(-{a}; {a})", f"(0; +∞)"], 1)
def a7_vo(rng):
    a = rng.randint(1, 5); return M(f"Bất phương trình x² + {a} < 0 có tập nghiệm là:", "∅", ["ℝ", "(-∞; 0)", "(0; +∞)"], 1)
def a7_nghiem_nguyen(rng):
    a = rng.randint(2, 8); return nint(rng, f"Số nghiệm nguyên của bất phương trình x² < {a * a} là:", 2 * a - 1, 2, (1, 2), 0)
def a7_dk(rng):
    m = rng.randint(1, 6); return M(f"Tìm điều kiện của m để x² - 2x + m > 0 với mọi x:", "m > 1", ["m < 1", "m ≥ 1", "m > 2"], 2)
def a7_toi(rng):
    a, b = sorted(rng.sample(range(1, 9), 2)); return M(f"Số nghiệm nguyên dương của bất phương trình x² - {a + b}x + {a * b} ≤ 0 là:", b - a + 1, [b - a, b - a + 2, b + 1], 2)
def a7_pt_vo(rng):
    r = rng.randint(2, 8); return M(f"Phương trình √(2x + {r}) = x + 1 sau khi bình phương hai vế (bỏ qua điều kiện) cho:", f"x² = {r - 1}", [f"x² = {r + 1}", f"x² + 2x = {r}", f"x² = {r}"], 3)
def a7_hs(rng):
    return M("Tập nghiệm của bất phương trình x² ≥ 0 là:", "ℝ", ["(0; +∞)", "[0; +∞)", "∅"], 1)
def b7_giai(rng):
    a, b = sorted(rng.sample(range(-6, 8), 2)); return T(f"Giải bất phương trình {da([1, -(a + b), a * b])} ≤ 0.", f"Nghiệm: x = {a}, x = {b}. Vì hệ số a = 1 > 0 nên tập nghiệm là [{a}; {b}].", 2)
def b7_dk(rng):
    return T("Tìm m để x² + 2mx + 4 > 0 với mọi x ∈ ℝ.", "Δ' = m² - 4 < 0 ⇒ -2 < m < 2.", 3)
def b7_pt(rng):
    a = rng.randint(1, 6); return T(f"Giải phương trình x = √(x + {a * a - a}) (với x ≥ 0).", f"Bình phương: x² - x - {a * a - a} = 0 ⇒ x = {a} hoặc x = {1 - a}; chỉ nhận x = {a} (x ≥ 0).", 3)
def b7_lap(rng):
    return T("Giải thích cách lập bảng xét dấu tam thức bậc hai.", "Tìm nghiệm của tam thức, đặt trên trục số, dấu của f(x) ngoài khoảng hai nghiệm cùng dấu với a, trong khoảng hai nghiệm trái dấu với a.", 1)
def b7_loi(rng):
    return T("Một vật được ném lên theo h = -5t² + 20t. Hỏi trong khoảng thời gian nào vật ở độ cao trên 15 m?", "-5t² + 20t > 15 ⇔ t² - 4t + 3 < 0 ⇔ 1 < t < 3 (giây).", 3)

# ===== 8. Đại số tổ hợp =====
def a8_hv(rng):
    n = rng.randint(3, 8); return nint(rng, f"Số hoán vị của {n} phần tử là:", math.factorial(n), 3, (1, 2, 10), 0)
def a8_chinh(rng):
    n = rng.randint(5, 10); k = rng.randint(2, 4); return nint(rng, f"Số chỉnh hợp chập {k} của {n} phần tử là:", math.perm(n, k), 3, (1, 2, 6), 0)
def a8_tohop(rng):
    n = rng.randint(6, 12); k = rng.randint(2, 4); return nint(rng, f"Số tổ hợp chập {k} của {n} phần tử là:", math.comb(n, k), 3, (1, 2, 6), 0)
def a8_quytac(rng):
    a, b = rng.randint(2, 8), rng.randint(2, 8); return nint(rng, f"Có {a} cách chọn áo và {b} cách chọn quần. Số cách chọn một bộ quần áo là:", a * b, 1, (1, 2, 3), 0)
def a8_cong(rng):
    a, b = rng.randint(3, 12), rng.randint(3, 12); return nint(rng, f"Có {a} cuốn sách Toán và {b} cuốn sách Văn. Số cách chọn một cuốn sách là:", a + b, 1, (1, 2, 3), 0)
def a8_xep(rng):
    n = rng.randint(3, 7); return nint(rng, f"Xếp {n} học sinh vào một hàng dọc. Số cách xếp là:", math.factorial(n), 3, (1, 2, 6), 0)
def a8_so(rng):
    return nint(rng, "Từ các chữ số 1, 2, 3, 4, 5 lập được bao nhiêu số tự nhiên có 3 chữ số khác nhau?", 60, 3, (6, 10, 12), 0)
def a8_chon(rng):
    n, k = rng.randint(8, 15), rng.randint(2, 4); return nint(rng, f"Chọn {k} học sinh từ nhóm {n} học sinh để đi lao động. Số cách chọn là:", math.comb(n, k), 3, (1, 2, 6), 0)
def a8_ct(rng):
    return M("Công thức tổ hợp C(n, k) bằng:", "n!/(k!(n - k)!)", ["n!/(n - k)!", "n!/k!", "k!/(n!)"], 1)
def a8_nhithuc(rng):
    n = rng.randint(3, 6); return nint(rng, f"Trong khai triển (a + b)^{n}, số hạng tổng quát là C({n}, k)·a^({n}-k)·b^k. Số số hạng của khai triển là:", n + 1, 1, (1, 2), 0)
def a8_dx(rng):
    n, k = rng.randint(6, 12), rng.randint(2, 4); return M(f"C({n}, {k}) bằng:", f"C({n}, {n - k})", [f"C({n}, {k + 1})", f"C({n - 1}, {k})", f"C({n + 1}, {k})"], 2)
def a8_binom(rng):
    n = rng.randint(2, 5); return nint(rng, f"Hệ số của x² trong khai triển (1 + x)^{n} là:", math.comb(n, 2), 2, (1, 2, 3), 0)
def b8_so(rng):
    return T("Từ các chữ số 1, 2, 3, 4, 5, 6 lập được bao nhiêu số tự nhiên chẵn có 3 chữ số khác nhau?", "Chữ số hàng đơn vị chẵn: 3 cách (2, 4, 6); hàng trăm: 5 cách; hàng chục: 4 cách ⇒ 3·5·4 = 60.", 3)
def b8_chon(rng):
    n, m, k = rng.randint(5, 8), rng.randint(4, 7), rng.randint(2, 3); return T(f"Một nhóm có {n} nam và {m} nữ. Chọn {k} nam và 1 nữ. Có bao nhiêu cách?", f"C({n},{k})·C({m},1) = {math.comb(n, k)}·{m} = {math.comb(n, k) * m}", 2)
def b8_hoan(rng):
    n = rng.randint(4, 7); return T(f"Có bao nhiêu cách xếp {n} bạn ngồi quanh một bàn tròn (hoán vị vòng)?", f"({n} - 1)! = {math.factorial(n - 1)}", 3)
def b8_nhi(rng):
    n = rng.randint(3, 6); return T(f"Khai triển (x + 2)^{n} (dạng đủ).", " + ".join(f"{math.comb(n, k) * 2 ** k}x^{n - k}" for k in range(n + 1)).replace("x^1", "x").replace("x^0", "") , 3) if True else None
def b8_pt(rng):
    return T("Giải phương trình A(n, 2) = 20 (n ∈ ℕ*, n ≥ 2).", "n(n - 1) = 20 ⇒ n² - n - 20 = 0 ⇒ n = 5 (nhận), n = -4 (loại).", 3)
def b8_phan(rng):
    return T("Phân biệt khi nào dùng quy tắc cộng, khi nào dùng quy tắc nhân.", "Cộng: công việc chia thành các phương án rời nhau. Nhân: công việc gồm nhiều bước liên tiếp.", 1)

# ===== 9. Phương pháp tọa độ trong mặt phẳng =====
def a9_ptdt(rng):
    a, b, c = nz(rng, -4, 4), nz(rng, -4, 4), rng.randint(-8, 8); x, y = rng.randint(-3, 3), rng.randint(-3, 3); d = -(a * x + b * y); return M(f"Đường thẳng đi qua M({x}; {y}) nhận n = ({a}; {b}) làm vectơ pháp tuyến có phương trình:", da2({(1, 0): a, (0, 1): b, (0, 0): d}) + " = 0", [da2({(1, 0): a, (0, 1): b, (0, 0): -d}) + " = 0", da2({(1, 0): b, (0, 1): a, (0, 0): d}) + " = 0", da2({(1, 0): a, (0, 1): b, (0, 0): d + 1}) + " = 0"], 2) if d != -d or True else None
def a9_kc(rng):
    a, b, x, y, c = rng.choice([(3, 4, 0, 0, 10), (3, 4, 1, 2, 5), (5, 12, 0, 0, 26), (6, 8, 0, 0, 20)]); d = abs(a * x + b * y + c) / math.sqrt(a * a + b * b); return nint(rng, f"Khoảng cách từ M({x}; {y}) đến đường thẳng {a}x + {b}y + {c} = 0 là:", int(round(d)), 2, (1, 2, 3), 0) if abs(d - round(d)) < 1e-9 else None
def a9_song(rng):
    a, b, c = nz(rng, -4, 4), nz(rng, -4, 4), rng.randint(-8, 8); return M(f"Đường thẳng nào song song với {da2({(1, 0): a, (0, 1): b})} + {c} = 0?" if c >= 0 else f"Đường thẳng nào song song với {da2({(1, 0): a, (0, 1): b})} - {-c} = 0?", f"{da2({(1, 0): a, (0, 1): b})} + {c + 3} = 0" if c + 3 >= 0 else f"{da2({(1, 0): a, (0, 1): b})} - {-(c + 3)} = 0", [f"{da2({(1, 0): b, (0, 1): -a})} + {c} = 0" if c >= 0 else f"{da2({(1, 0): b, (0, 1): -a})} - {-c} = 0", f"{da2({(1, 0): b, (0, 1): a})} = 0", "x = 0 và y = 0"], 2)
def a9_tron(rng):
    a, b, r = rng.randint(-5, 5), rng.randint(-5, 5), rng.randint(1, 7); return M(f"Đường tròn tâm I({a}; {b}), bán kính {r} có phương trình:", f"(x {'-' if a >= 0 else '+'} {abs(a)})² + (y {'-' if b >= 0 else '+'} {abs(b)})² = {r * r}", [f"(x {'+' if a >= 0 else '-'} {abs(a)})² + (y {'+' if b >= 0 else '-'} {abs(b)})² = {r * r}", f"(x {'-' if a >= 0 else '+'} {abs(a)})² + (y {'-' if b >= 0 else '+'} {abs(b)})² = {r}", f"(x {'-' if a >= 0 else '+'} {abs(a)}) + (y {'-' if b >= 0 else '+'} {abs(b)}) = {r * r}"], 2) if a != 0 and b != 0 else None
def a9_tam(rng):
    a, b = rng.randint(-5, 5), rng.randint(-5, 5); r = rng.randint(1, 6); return M(f"Đường tròn x² + y² {'-' if a >= 0 else '+'} {abs(2 * a)}x {'-' if b >= 0 else '+'} {abs(2 * b)}y + {a * a + b * b - r * r} = 0 có tâm là:", f"({a}; {b})", [f"({-a}; {-b})", f"({2 * a}; {2 * b})", f"({b}; {a})" if a != b else f"({a + 1}; {b})"], 2) if a != 0 and b != 0 else None
def a9_ban(rng):
    a, b, r = rng.randint(-4, 4), rng.randint(-4, 4), rng.randint(1, 7); return nint(rng, f"Đường tròn (x - {a})² + (y - {b})² = {r * r} có bán kính là:", r, 1, (1, 2, 3), 0) if a >= 0 and b >= 0 else None
def a9_ellip(rng):
    a, b = rng.choice([(5, 3), (13, 5), (10, 6), (5, 4), (17, 8)]); c = math.isqrt(a * a - b * b); return nint(rng, f"Elip x²/{a * a} + y²/{b * b} = 1 có tiêu cự 2c bằng (c² = a² - b²):", 2 * c, 3, (2, 4, 6), 0) if c * c == a * a - b * b else None
def a9_hypebol(rng):
    a, b = rng.choice([(3, 4), (5, 12), (6, 8), (8, 6)]); c = math.isqrt(a * a + b * b); return nint(rng, f"Hypebol x²/{a * a} - y²/{b * b} = 1 có tiêu cự 2c bằng (c² = a² + b²):", 2 * c, 3, (2, 4, 6), 0)
def a9_parabol(rng):
    p = rng.randint(1, 8); return M(f"Parabol y² = {2 * p}x có tiêu điểm là:", f"F({tt(p / 2)}; 0)", [f"F(0; {tt(p / 2)})", f"F({p}; 0)", f"F({tt(-p / 2)}; 0)"], 2)
def a9_giao(rng):
    return M("Hai đường thẳng a₁x + b₁y + c₁ = 0 và a₂x + b₂y + c₂ = 0 song song khi:", "a₁/a₂ = b₁/b₂ ≠ c₁/c₂", ["a₁/a₂ ≠ b₁/b₂", "a₁a₂ + b₁b₂ = 0", "a₁ = a₂ và b₁ = b₂ và c₁ = c₂"], 2)
def a9_vg(rng):
    return M("Hai đường thẳng vuông góc khi tích vô hướng hai vectơ pháp tuyến bằng:", 0, [1, -1, 2], 1)
def a9_tt(rng):
    r = rng.randint(2, 9); return M(f"Đường thẳng d tiếp xúc đường tròn tâm I bán kính {r} khi khoảng cách d(I, d) bằng:", r, [r + 1, r - 1, 2 * r], 2)
def b9_ptdt(rng):
    xa, ya, xb, yb = [rng.randint(-5, 5) for _ in range(4)]
    if (xa, ya) == (xb, yb): raise ValueError
    a, b = yb - ya, xa - xb; c = -(a * xa + b * ya); return T(f"Lập phương trình đường thẳng đi qua A({xa}; {ya}) và B({xb}; {yb}).", f"Vectơ chỉ phương AB = ({xb - xa}; {yb - ya}) ⇒ vectơ pháp tuyến ({a}; {b}).\nPhương trình: {da2({(1, 0): a, (0, 1): b, (0, 0): c})} = 0.", 2)
def b9_tron(rng):
    a, b, r = rng.randint(-4, 5), rng.randint(-4, 5), rng.randint(2, 6); return T(f"Lập phương trình đường tròn tâm I({a}; {b}) và tiếp xúc với đường thẳng cách tâm một khoảng {r}.", f"Bán kính R = {r}\n(x - ({a}))² + (y - ({b}))² = {r * r}.", 2)
def b9_kc(rng):
    return T("Tính khoảng cách từ điểm M(1; 2) đến đường thẳng 3x + 4y - 2 = 0.", "d = |3·1 + 4·2 - 2|/√(3² + 4²) = 9/5.", 2)
def b9_tt(rng):
    return T("Viết phương trình tiếp tuyến của đường tròn (x - 1)² + (y - 2)² = 25 tại điểm M(4; 6).", "Tâm I(1; 2). IM = (3; 4) là vectơ pháp tuyến. Tiếp tuyến: 3(x - 4) + 4(y - 6) = 0 ⇔ 3x + 4y - 36 = 0.", 3)
def b9_elip(rng):
    return T("Cho elip x²/25 + y²/9 = 1. Tìm độ dài các trục và tiêu cự.", "a = 5, b = 3, c = √(25 - 9) = 4. Trục lớn 10, trục nhỏ 6, tiêu cự 8.", 2)
def b9_parabol(rng):
    return T("Cho parabol y² = 8x. Tìm tiêu điểm và đường chuẩn.", "2p = 8 ⇒ p = 4; tiêu điểm F(2; 0); đường chuẩn x = -2.", 2)

# ===== 10. Xác suất =====
def a10_tap(rng):
    n = rng.randint(4, 10); return nint(rng, f"Chọn ngẫu nhiên một số từ 1 đến {n * 5}. Số phần tử của không gian mẫu là:", n * 5, 1, (1, 2, 5), 0)
def a10_chia(rng):
    n, k = rng.randint(20, 60), rng.choice([2, 3, 5]); f = Fraction(n // k, n); return M(f"Chọn ngẫu nhiên một số từ 1 đến {n}. Xác suất số đó chia hết cho {k} là:", ps(f), nh_ps(rng, f), 2)
def a10_xuc(rng):
    s = rng.randint(2, 12); c = 6 - abs(s - 7); f = Fraction(c, 36); return M(f"Gieo hai con xúc xắc. Xác suất tổng hai mặt bằng {s} là:", ps(f), nh_ps(rng, f), 2)
def a10_chon(rng):
    n, m = rng.randint(4, 8), rng.randint(3, 6); f = Fraction(math.comb(n, 2), math.comb(n + m, 2)); return M(f"Hộp có {n} bi đỏ và {m} bi xanh. Chọn ngẫu nhiên 2 viên. Xác suất cả hai đỏ là:", ps(f), nh_ps(rng, f), 3)
def a10_doi(rng):
    p = rng.choice([Fraction(1, 5), Fraction(3, 8), Fraction(2, 7), Fraction(1, 3)]); return M(f"Xác suất biến cố A là {ps(p)}. Xác suất biến cố đối của A là:", ps(1 - p), nh_ps(rng, 1 - p), 1)
def a10_hop(rng):
    a, b = Fraction(1, rng.randint(3, 6)), Fraction(1, rng.randint(7, 10)); return M(f"A, B xung khắc, P(A) = {ps(a)}, P(B) = {ps(b)}. P(A ∪ B) bằng:", ps(a + b), nh_ps(rng, a + b) if a + b < 1 else [ps(a * b), ps(abs(a - b)), ps(a)], 2)
def a10_dl(rng):
    a, b = Fraction(1, rng.randint(2, 4)), Fraction(1, rng.randint(2, 5)); return M(f"A, B độc lập, P(A) = {ps(a)}, P(B) = {ps(b)}. P(AB) bằng:", ps(a * b), [ps(a + b) if a + b < 1 else ps(a), ps(abs(a - b)) if a != b else ps(a), ps(a / b if a / b < 1 else b / a)], 2)
def a10_xs_tong(rng):
    return M("Xác suất của một biến cố bất kì luôn thuộc đoạn:", "[0; 1]", ["[-1; 1]", "(0; 1)", "[0; 100]"], 1)
def a10_chacchan(rng):
    return M("Xác suất của biến cố chắc chắn bằng:", 1, [0, "1/2", "Không xác định"], 1)
def a10_khongthe(rng):
    return M("Xác suất của biến cố không thể bằng:", 0, [1, "1/2", "-1"], 1)
def a10_dongxu(rng):
    n = rng.randint(2, 5); return M(f"Tung {n} đồng xu cân đối. Số phần tử không gian mẫu là:", 2 ** n, [n * 2, n ** 2, 2 ** (n + 1)], 1)
def a10_tl(rng):
    n, m = rng.randint(5, 9), rng.randint(3, 7); f = Fraction(n * m, math.comb(n + m, 2)); return M(f"Hộp có {n} bi đỏ và {m} bi xanh. Chọn ngẫu nhiên 2 viên. Xác suất được 1 đỏ 1 xanh là:", ps(f), nh_ps(rng, f), 3)
def b10_xuc(rng):
    s = rng.randint(2, 12); c = 6 - abs(s - 7); return T(f"Gieo một con xúc xắc hai lần. Tính xác suất để tổng số chấm bằng {s}.", f"Không gian mẫu 36; thuận lợi {c}. P = {pf(c, 36)}.", 2)
def b10_hop(rng):
    n, m, k = rng.randint(4, 7), rng.randint(3, 6), 3; f = Fraction(math.comb(n, 3), math.comb(n + m, 3)); return T(f"Hộp có {n} bi đỏ, {m} bi xanh. Chọn ngẫu nhiên 3 viên. Tính xác suất cả 3 viên đều đỏ.", f"|Ω| = C({n + m},3) = {math.comb(n + m, 3)}; thuận lợi C({n},3) = {math.comb(n, 3)}. P = {ps(f)}", 3)
def b10_doi(rng):
    return T("Tung ba đồng xu. Tính xác suất có ít nhất một mặt sấp.", "P(đối) = 1/8; P = 1 - 1/8 = 7/8.", 2)
def b10_hoc(rng):
    return T("Chọn ngẫu nhiên 2 học sinh từ tổ 4 nam, 3 nữ. Tính xác suất được 1 nam 1 nữ.", "|Ω| = C(7,2) = 21; thuận lợi 4·3 = 12. P = 12/21 = 4/7.", 3)
def b10_ct(rng):
    return T("Nêu công thức cộng xác suất và công thức nhân xác suất cho hai biến cố độc lập.", "P(A ∪ B) = P(A) + P(B) - P(A ∩ B); với A, B độc lập: P(A ∩ B) = P(A)·P(B).", 1)
def b10_so(rng):
    return T("Chọn ngẫu nhiên một số tự nhiên có hai chữ số. Tính xác suất số đó chia hết cho 5.", "Có 90 số; chia hết cho 5: 18 số. P = 18/90 = 1/5.", 2)

CHU_DE = [
    ("Chương 1: Mệnh đề và tập hợp", [a1_phu, a1_dung, a1_AuB, a1_AnB, a1_hieu, a1_phantu, a1_khoang, a1_giao_khoang, a1_hop_khoang, a1_keo, a1_tuong, a1_dao, a1_so, a1_chia], [b1_tap, b1_phu, b1_khoang, b1_tap_con, b1_dem, b1_dk]),
    ("Chương 2: Bất phương trình và hệ bất phương trình bậc nhất hai ẩn", [a2_thuoc, a2_bd, a2_bien, a2_goc, a2_he, a2_he2, a2_dinh, a2_toiuu, a2_toiuu2, a2_cat, a2_truc, a2_truc2], [b2_ve, b2_loi, b2_he, b2_toiuu, b2_kt]),
    ("Chương 3: Hàm số bậc hai", [a3_dinh, a3_dinh_y, a3_truc, a3_bien, a3_giatri, a3_cuc, a3_cat, a3_qua, a3_pt, a3_toi, a3_delta, a3_tdx], [b3_khao_sat, b3_xd, b3_max, b3_tt, b3_tuong, b3_gt]),
    ("Chương 4: Hệ thức lượng trong tam giác", [a4_cos, a4_sin, a4_dt, a4_heron, a4_p, a4_r, a4_cosA, a4_trung, a4_gtlg, a4_cosphu, a4_goc, a4_ban], [b4_giai, b4_heron, b4_goc, b4_do_cao, b4_phat, b4_ct]),
    ("Chương 5: Vectơ", [a5_cong, a5_hieu, a5_nhan, a5_dai, a5_ab, a5_trungdiem, a5_trongtam, a5_tichvo, a5_vuong, a5_cungphuong, a5_hbh, a5_chasles, a5_goc], [b5_toado, b5_hbh, b5_goc, b5_cm, b5_phat, b5_tichvo]),
    ("Chương 6: Các số đặc trưng của mẫu số liệu", [a6_tb, a6_med, a6_med2, a6_mot, a6_kt, a6_q, a6_q3, a6_dq, a6_pv, a6_sd, a6_outlier, a6_mau], [b6_tb, b6_q, b6_ngoai, b6_so, b6_dt]),
    ("Chương 7: Tam thức bậc hai và bất phương trình bậc hai một ẩn", [a7_dau, a7_bpt, a7_bpt2, a7_pt, a7_delta, a7_vn, a7_vo, a7_nghiem_nguyen, a7_dk, a7_toi, a7_pt_vo, a7_hs], [b7_giai, b7_dk, b7_pt, b7_lap, b7_loi]),
    ("Chương 8: Đại số tổ hợp", [a8_hv, a8_chinh, a8_tohop, a8_quytac, a8_cong, a8_xep, a8_so, a8_chon, a8_ct, a8_nhithuc, a8_dx, a8_binom], [b8_so, b8_chon, b8_hoan, b8_nhi, b8_pt, b8_phan]),
    ("Chương 9: Phương pháp tọa độ trong mặt phẳng", [a9_ptdt, a9_kc, a9_song, a9_tron, a9_tam, a9_ban, a9_ellip, a9_hypebol, a9_parabol, a9_giao, a9_vg, a9_tt], [b9_ptdt, b9_tron, b9_kc, b9_tt, b9_elip, b9_parabol]),
    ("Chương 10: Xác suất của biến cố", [a10_tap, a10_chia, a10_xuc, a10_chon, a10_doi, a10_hop, a10_dl, a10_xs_tong, a10_chacchan, a10_khongthe, a10_dongxu, a10_tl], [b10_xuc, b10_hop, b10_doi, b10_hoc, b10_ct, b10_so]),
]

def _w(f):
    def g(rng):
        r = f(rng)
        if r is None: raise ValueError
        return r
    g.__name__ = f.__name__
    return g
CHU_DE = [(t, [_w(f) for f in m], [_w(f) for f in l]) for t, m, l in CHU_DE]
