from thcs import *
import math
def nz(rng, lo=-6, hi=6): return rng.choice([x for x in range(lo, hi + 1) if x])
def tt(x): return f"{x:g}".replace(".", ",")
def vec(a): return f"({a[0]}; {a[1]}; {a[2]})"

# ===== 1. Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số =====
def a1_dbien(rng):
    a = rng.randint(1, 4); b = rng.randint(-6, 6); return M(f"Hàm số y = {a}x {'+' if b >= 0 else '-'} {abs(b)} (a > 0) là hàm:", "Đồng biến trên ℝ", ["Nghịch biến trên ℝ", "Không đơn điệu", "Là hàm hằng"], 1)
def a1_ct(rng):
    a, b = rng.randint(1, 4), rng.randint(-8, 8); x = Fraction(-b, 2 * a); return M(f"Hàm số y = {da([a, b, 1])} đạt cực tiểu tại x bằng:", ps(x), [ps(-x) if x else ps(Fraction(1)), ps(x + 1), ps(x * 2) if x else ps(Fraction(2))], 2)
def a1_cd(rng):
    a, b = rng.randint(1, 4), rng.randint(-8, 8); x = Fraction(b, 2 * a); return M(f"Hàm số y = {da([-a, b, 1])} đạt cực đại tại x bằng:", ps(x), [ps(-x) if x else ps(Fraction(1)), ps(x + 1), ps(x * 2) if x else ps(Fraction(2))], 2)
def a1_cubic(rng):
    a, b = rng.randint(1, 3), rng.randint(1, 4); return M(f"Số điểm cực trị của hàm số y = x³ - {3 * a * a}x + {b} là:", 2, [0, 1, 3], 2)
def a1_cubic_x(rng):
    a = rng.randint(1, 4); return M(f"Hàm số y = x³ - {3 * a * a}x + 1 đạt cực đại tại x bằng:", -a, [a, 0, 2 * a], 3)
def a1_gtln(rng):
    a = rng.randint(1, 5); return nint(rng, f"Giá trị lớn nhất của hàm số y = -x² + {2 * a}x trên ℝ là:", a * a, 2, (1, 2, 3), 0)
def a1_gtnn(rng):
    a = rng.randint(1, 5); return nint(rng, f"Giá trị nhỏ nhất của hàm số y = x² - {2 * a}x + {a * a + 1} trên ℝ là:", 1, 1, (1, 2, 3), 0)
def a1_doan(rng):
    a = rng.randint(1, 4); return nint(rng, f"Giá trị lớn nhất của y = x² trên đoạn [-{a}; {a + 1}] là:", (a + 1) ** 2, 2, (1, 2, 3), 0)
def a1_tcd(rng):
    a, b = rng.randint(1, 5), rng.randint(1, 5); return M(f"Đồ thị hàm số y = ({a}x + 1)/(x - {b}) có tiệm cận đứng là:", f"x = {b}", [f"x = -{b}", f"y = {b}", f"x = {a}"], 2)
def a1_tcn(rng):
    a, b = rng.randint(1, 5), rng.randint(1, 5); return M(f"Đồ thị hàm số y = ({a}x + 1)/(x - {b}) có tiệm cận ngang là:", f"y = {a}", [f"y = {b}", f"y = -{a}", f"x = {a}"], 2)
def a1_giao(rng):
    return M("Số giao điểm của đồ thị y = x² và đường thẳng y = 4 là:", 2, [0, 1, 3], 1)
def a1_hsgoc(rng):
    a, x = rng.randint(1, 4), rng.randint(1, 3); return nint(rng, f"Hệ số góc tiếp tuyến của y = x³ tại điểm có hoành độ {x} là:", 3 * x * x, 2, (1, 2, 3), 0)
def a1_dau(rng):
    return M("Nếu f'(x) > 0 trên khoảng (a; b) thì hàm số f(x) trên khoảng đó:", "Đồng biến", ["Nghịch biến", "Không đổi", "Có cực đại"], 1)
def a1_ct_dk(rng):
    return M("Nếu f'(x₀) = 0 và f'(x) đổi dấu từ dương sang âm khi qua x₀ thì x₀ là điểm:", "Cực đại", ["Cực tiểu", "Uốn", "Không là cực trị"], 1)
def b1_khaosat(rng):
    a = rng.randint(1, 3); return T(f"Khảo sát và vẽ đồ thị hàm số y = x³ - {3 * a}x² + 1.", f"y' = 3x² - {6 * a}x = 0 ⇒ x = 0 hoặc x = {2 * a}.\nCực đại tại x = 0 (y = 1); cực tiểu tại x = {2 * a} (y = {8 * a ** 3 - 12 * a ** 3 + 1}). Lập bảng biến thiên và vẽ.", 3)
def b1_max(rng):
    a = rng.randint(1, 4); return T(f"Tìm giá trị lớn nhất, nhỏ nhất của y = x³ - 3x trên đoạn [0; {a + 1}].", f"y' = 3x² - 3 = 0 ⇒ x = 1 (thuộc đoạn).\ny(0) = 0; y(1) = -2; y({a + 1}) = {(a + 1) ** 3 - 3 * (a + 1)}. Min = -2, Max = {(a + 1) ** 3 - 3 * (a + 1)}.", 3)
def b1_tcn(rng):
    a, b = rng.randint(1, 4), rng.randint(1, 4); return T(f"Tìm các đường tiệm cận của đồ thị y = ({a}x + 1)/(x - {b}).", f"Tiệm cận đứng x = {b}; tiệm cận ngang y = {a}.", 2)
def b1_loi(rng):
    a = rng.randint(10, 40); return T(f"Một tấm tôn hình chữ nhật có chu vi {2 * a} m. Tìm kích thước để diện tích lớn nhất.", f"Gọi một cạnh x: S = x({a} - x), x ∈ (0; {a}). S' = {a} - 2x = 0 ⇒ x = {tt(a / 2)}.\nDiện tích lớn nhất khi hình vuông cạnh {tt(a / 2)} m.", 3)
def b1_tt(rng):
    x = rng.randint(1, 3); return T(f"Viết phương trình tiếp tuyến của đồ thị y = x³ - 3x tại điểm có hoành độ {x}.", f"y' = 3x² - 3 ⇒ k = {3 * x * x - 3}; y({x}) = {x ** 3 - 3 * x}.\nTiếp tuyến: y = {3 * x * x - 3}(x - {x}) + {x ** 3 - 3 * x}.", 2)
def b1_bbt(rng):
    return T("Nêu các bước khảo sát sự biến thiên và vẽ đồ thị hàm số.", "Tìm tập xác định; tính y', tìm cực trị, xét dấu, lập bảng biến thiên; tìm tiệm cận (nếu có); tìm điểm đặc biệt; vẽ đồ thị.", 1)

# ===== 2. Vectơ và hệ trục tọa độ trong không gian =====
def _v(rng, lo=-5, hi=5): return [rng.randint(lo, hi) for _ in range(3)]
def a2_cong(rng):
    a, b = _v(rng), _v(rng); return M(f"Cho a = {vec(a)}, b = {vec(b)}. Tọa độ a + b là:", vec([x + y for x, y in zip(a, b)]), [vec([x - y for x, y in zip(a, b)]), vec([x * y for x, y in zip(a, b)]), vec([x + y + 1 for x, y in zip(a, b)])], 1)
def a2_hieu(rng):
    a, b = _v(rng), _v(rng); d = [x - y for x, y in zip(a, b)]
    return M(f"Cho a = {vec(a)}, b = {vec(b)}. Tọa độ a - b là:", vec(d), [vec([x + y for x, y in zip(a, b)]), vec([y - x for x, y in zip(a, b)]), vec([x - y + 1 for x, y in zip(a, b)])], 1)
def a2_nhan(rng):
    a, k = _v(rng), nz(rng, -4, 4); return M(f"Cho a = {vec(a)}. Tọa độ {k}a là:", vec([k * x for x in a]), [vec([x + k for x in a]), vec([k * a[0], a[1], a[2]]), vec([-k * x for x in a])], 1)
def a2_dai(rng):
    a, b, c = rng.choice([(1, 2, 2), (2, 3, 6), (2, 6, 9), (4, 4, 7), (3, 4, 12)]); d = math.isqrt(a * a + b * b + c * c); return nint(rng, f"Độ dài vectơ u = ({a}; {b}; {c}) là:", d, 2, (1, 2, 3), 0)
def a2_ab(rng):
    A, B = _v(rng), _v(rng); return M(f"Cho A{vec(A)}, B{vec(B)}. Tọa độ vectơ AB là:", vec([y - x for x, y in zip(A, B)]), [vec([x - y for x, y in zip(A, B)]), vec([x + y for x, y in zip(A, B)]), vec([y - x + 1 for x, y in zip(A, B)])], 1)
def a2_tdiem(rng):
    A = [rng.randint(-4, 4) * 2 for _ in range(3)]; B = [rng.randint(-4, 4) * 2 for _ in range(3)]; return M(f"Trung điểm đoạn AB với A{vec(A)}, B{vec(B)} có tọa độ:", vec([(x + y) // 2 for x, y in zip(A, B)]), [vec([x + y for x, y in zip(A, B)]), vec([(y - x) // 2 for x, y in zip(A, B)]), vec([(x + y) // 2 + 1 for x, y in zip(A, B)])], 1)
def a2_trongtam(rng):
    P = [[rng.randint(-4, 4) * 3 for _ in range(3)] for _ in range(3)]; g = [sum(p[i] for p in P) // 3 for i in range(3)]; return M(f"Tam giác ABC có A{vec(P[0])}, B{vec(P[1])}, C{vec(P[2])}. Trọng tâm G có tọa độ:", vec(g), [vec([sum(p[i] for p in P) for i in range(3)]), vec([x + 1 for x in g]), vec([-x for x in g])], 2) if all(sum(p[i] for p in P) % 3 == 0 for i in range(3)) else None
def a2_tichvo(rng):
    a, b = _v(rng), _v(rng); return nint(rng, f"Cho a = {vec(a)}, b = {vec(b)}. Tích vô hướng a·b bằng:", sum(x * y for x, y in zip(a, b)), 2, (1, 2, 3))
def a2_vuong(rng):
    return M("Hai vectơ a, b vuông góc khi:", "a·b = 0", ["a·b = 1", "|a| = |b|", "a = kb"], 1)
def a2_cungphuong(rng):
    a = _v(rng); k = rng.randint(2, 4); return M(f"Hai vectơ a = {vec(a)} và b = {vec([k * x for x in a])} là:", "Cùng phương", ["Vuông góc", "Bằng nhau", "Đối nhau"], 1) if any(a) else None
def a2_oxyz(rng):
    return M("Điểm M(a; b; c) thuộc mặt phẳng (Oxy) khi:", "c = 0", ["a = 0", "b = 0", "a = b = c"], 1)
def a2_hinhchieu(rng):
    a, b, c = _v(rng, 1, 5); return M(f"Hình chiếu vuông góc của M({a}; {b}; {c}) lên mặt phẳng (Oxy) là:", f"({a}; {b}; 0)", [f"({a}; 0; {c})", f"(0; {b}; {c})", f"(0; 0; {c})"], 1)
def a2_dx(rng):
    a, b, c = _v(rng, 1, 5); return M(f"Điểm đối xứng của M({a}; {b}; {c}) qua gốc tọa độ O là:", f"({-a}; {-b}; {-c})", [f"({a}; {b}; {-c})", f"({-a}; {b}; {c})", f"({a}; {-b}; {-c})"], 1)
def a2_goc(rng):
    return M("Tích có hướng của hai vectơ cho ta vectơ:", "Vuông góc với cả hai vectơ đó", ["Song song với cả hai", "Bằng tổng hai vectơ", "Bằng tích vô hướng"], 1)
def a2_hbh(rng):
    A, B, C = _v(rng), _v(rng), _v(rng); D = [A[i] + C[i] - B[i] for i in range(3)]; return M(f"Cho A{vec(A)}, B{vec(B)}, C{vec(C)}. D để ABCD là hình bình hành có tọa độ:", vec(D), [vec([A[i] + B[i] - C[i] for i in range(3)]), vec([B[i] + C[i] - A[i] for i in range(3)]), vec([A[i] + B[i] + C[i] for i in range(3)])], 3)
def b2_toado(rng):
    A, B, C = _v(rng), _v(rng), _v(rng); return T(f"Cho A{vec(A)}, B{vec(B)}, C{vec(C)}. Tìm tọa độ AB, AC, độ dài AB và trọng tâm tam giác ABC.", f"AB = {vec([B[i] - A[i] for i in range(3)])}; AC = {vec([C[i] - A[i] for i in range(3)])}\nAB = √{sum((B[i] - A[i]) ** 2 for i in range(3))}\nG = ({ps(Fraction(sum(p[0] for p in (A, B, C)), 3))}; {ps(Fraction(sum(p[1] for p in (A, B, C)), 3))}; {ps(Fraction(sum(p[2] for p in (A, B, C)), 3))})", 2)
def b2_tichvo(rng):
    a, b = _v(rng), _v(rng); n = sum(x * y for x, y in zip(a, b)); return T(f"Tính a·b và kiểm tra a, b có vuông góc không, với a = {vec(a)}, b = {vec(b)}.", f"a·b = {n}. {'Bằng 0 nên a ⊥ b.' if n == 0 else 'Khác 0 nên a không vuông góc với b.'}", 1)
def b2_hbh(rng):
    A, B, C = _v(rng), _v(rng), _v(rng); D = [A[i] + C[i] - B[i] for i in range(3)]; return T(f"Cho A{vec(A)}, B{vec(B)}, C{vec(C)}. Tìm D để ABCD là hình bình hành.", f"AB = DC ⇒ D = A + C - B = {vec(D)}", 2)
def b2_goc(rng):
    return T("Tính góc giữa hai vectơ a = (1; 0; 1) và b = (0; 1; 1).", "a·b = 1; |a| = |b| = √2 ⇒ cos = 1/2 ⇒ góc = 60°.", 2)
def b2_cm(rng):
    return T("Chứng minh bốn điểm A(0;0;0), B(1;0;0), C(0;1;0), D(0;0;1) không đồng phẳng.", "AB = (1;0;0), AC = (0;1;0), AD = (0;0;1); tích hỗn tạp [AB, AC]·AD = 1 ≠ 0 nên không đồng phẳng.", 2)
def b2_ct(rng):
    return T("Nêu các công thức tọa độ trung điểm, trọng tâm, độ dài và tích vô hướng trong không gian Oxyz.", "M = ((x_A + x_B)/2; ...); G = ((x_A + x_B + x_C)/3; ...); |a| = √(x² + y² + z²); a·b = x₁x₂ + y₁y₂ + z₁z₂.", 1)

# ===== 3. Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm =====
def _nh(rng):
    w = rng.choice([5, 10]); a = rng.randint(0, 3) * w; k = [rng.randint(2, 12) for _ in range(4)]; return w, a, k
def a3_kbt(rng):
    a = rng.randint(0, 5) * 10; b = rng.randint(6, 10) * 10; return nint(rng, f"Khoảng biến thiên của mẫu ghép nhóm có nhóm đầu bắt đầu {a} và nhóm cuối kết thúc {b} là:", b - a, 1, (5, 10), 0)
def a3_dd(rng):
    w, a, k = _nh(rng); return M(f"Giá trị đại diện của nhóm [{a}; {a + w}) là:", tt(a + w / 2), [tt(a), tt(a + w), tt(a + w / 2 + 1)], 1)
def a3_tb(rng):
    w, a, k = _nh(rng); n = sum(k); m = sum((a + i * w + w / 2) * k[i] for i in range(4)) / n; return M(f"Bảng ghép nhóm: [{a};{a + w}): {k[0]}; [{a + w};{a + 2 * w}): {k[1]}; [{a + 2 * w};{a + 3 * w}): {k[2]}; [{a + 3 * w};{a + 4 * w}): {k[3]}. Số trung bình (làm tròn 0,01) là:", f"{m:.2f}".replace(".", ","), [f"{m + 1:.2f}".replace(".", ","), f"{m - 1:.2f}".replace(".", ","), f"{m + w / 2:.2f}".replace(".", ",")], 3)
def a3_pv(rng):
    w, a, k = _nh(rng); n = sum(k); xs = [a + i * w + w / 2 for i in range(4)]; m = sum(xs[i] * k[i] for i in range(4)) / n; v = sum(k[i] * (xs[i] - m) ** 2 for i in range(4)) / n; return M(f"Bảng ghép nhóm: [{a};{a + w}): {k[0]}; [{a + w};{a + 2 * w}): {k[1]}; [{a + 2 * w};{a + 3 * w}): {k[2]}; [{a + 3 * w};{a + 4 * w}): {k[3]}. Phương sai (làm tròn 0,01) là:", f"{v:.2f}".replace(".", ","), [f"{v + 5:.2f}".replace(".", ","), f"{math.sqrt(v):.2f}".replace(".", ","), f"{v * 2:.2f}".replace(".", ",")], 3)
def a3_sd(rng):
    return M("Độ lệch chuẩn của mẫu số liệu ghép nhóm bằng:", "Căn bậc hai của phương sai", ["Bình phương phương sai", "Phương sai chia cho n", "Hiệu hai giá trị đại diện"], 1)
def a3_dq(rng):
    return M("Khoảng tứ phân vị ΔQ của mẫu số liệu ghép nhóm được tính bằng:", "Q₃ - Q₁", ["Q₃ + Q₁", "Q₂ - Q₁", "Q₃ - Q₂"], 1)
def a3_so(rng):
    return M("Phương sai của mẫu càng lớn thì số liệu:", "Càng phân tán", ["Càng tập trung", "Không đổi", "Càng nhỏ"], 1)
def a3_pvx(rng):
    return M("Phương sai có đơn vị là:", "Bình phương đơn vị của số liệu", ["Cùng đơn vị với số liệu", "Không có đơn vị", "Phần trăm"], 1)
def a3_tong(rng):
    w, a, k = _nh(rng); return nint(rng, f"Mẫu ghép nhóm có tần số các nhóm {', '.join(map(str, k))}. Cỡ mẫu là:", sum(k), 1, (1, 2, 5), 0)
def a3_rong(rng):
    w, a, k = _nh(rng); return nint(rng, f"Nhóm [{a}; {a + w}) có độ rộng:", w, 1, (1, 2, 5), 0)
def a3_dcdt(rng):
    return M("So sánh hai mẫu số liệu cùng đơn vị, mẫu có độ lệch chuẩn nhỏ hơn thì:", "Đồng đều hơn", ["Phân tán hơn", "Có trung bình nhỏ hơn", "Có nhiều giá trị hơn"], 1)
def a3_q2(rng):
    return M("Tứ phân vị thứ hai Q₂ của mẫu số liệu chính là:", "Trung vị", ["Số trung bình", "Mốt", "Khoảng biến thiên"], 1)
def b3_pv(rng):
    w, a, k = _nh(rng); n = sum(k); xs = [a + i * w + w / 2 for i in range(4)]; m = sum(xs[i] * k[i] for i in range(4)) / n; v = sum(k[i] * (xs[i] - m) ** 2 for i in range(4)) / n
    return T(f"Bảng ghép nhóm: [{a};{a + w}): {k[0]}; [{a + w};{a + 2 * w}): {k[1]}; [{a + 2 * w};{a + 3 * w}): {k[2]}; [{a + 3 * w};{a + 4 * w}): {k[3]}. Tính số trung bình, phương sai và độ lệch chuẩn.", f"n = {n}; đại diện: {', '.join(tt(x) for x in xs)}\nTrung bình ≈ {m:.2f}; phương sai ≈ {v:.2f}; độ lệch chuẩn ≈ {math.sqrt(v):.2f}".replace(".", ","), 3)
def b3_q(rng):
    w, a, k = _nh(rng); n = sum(k); cum = []; c = 0
    for x in k: c += x; cum.append(c)
    def q(p):
        t = n * p; j = next(i for i in range(4) if cum[i] >= t); prev = cum[j - 1] if j else 0; return a + j * w + (t - prev) / k[j] * w
    return T(f"Bảng ghép nhóm: [{a};{a + w}): {k[0]}; [{a + w};{a + 2 * w}): {k[1]}; [{a + 2 * w};{a + 3 * w}): {k[2]}; [{a + 3 * w};{a + 4 * w}): {k[3]}. Tính Q₁, Q₃ và khoảng tứ phân vị.", f"n = {n}\nQ₁ ≈ {q(0.25):.2f}; Q₃ ≈ {q(0.75):.2f}; ΔQ ≈ {q(0.75) - q(0.25):.2f}".replace(".", ","), 3)
def b3_so(rng):
    return T("Hai lớp có điểm trung bình bằng nhau nhưng độ lệch chuẩn khác nhau. Lớp nào có kết quả đồng đều hơn?", "Lớp có độ lệch chuẩn nhỏ hơn đồng đều hơn vì số liệu ít phân tán quanh trung bình.", 1)
def b3_ct(rng):
    return T("Nêu công thức tính phương sai, độ lệch chuẩn của mẫu số liệu ghép nhóm.", "s² = (1/n)Σ mᵢ(xᵢ - x̄)²; s = √(s²); trong đó xᵢ là giá trị đại diện, mᵢ là tần số, n là cỡ mẫu.", 1)
def b3_kbt(rng):
    a = rng.randint(0, 5) * 10; b = rng.randint(6, 10) * 10; return T(f"Mẫu ghép nhóm bắt đầu từ {a} đến {b}. Tính khoảng biến thiên.", f"R = {b} - {a} = {b - a}.", 1)
def b3_ys(rng):
    return T("Phân biệt ý nghĩa của khoảng biến thiên và khoảng tứ phân vị.", "Khoảng biến thiên đo độ trải rộng toàn bộ mẫu, bị ảnh hưởng bởi giá trị cực đoan; khoảng tứ phân vị đo độ trải của 50% giữa, ổn định hơn.", 1)

# ===== 4. Nguyên hàm và tích phân =====
SUPD = "⁰¹²³⁴⁵⁶⁷⁸⁹"
def sup(n): return "".join(SUPD[int(c)] for c in str(n))
def a4_xn(rng):
    n = rng.randint(2, 6)
    return M(f"Nguyên hàm của f(x) = x{sup(n)} là:", f"x{sup(n + 1)}/{n + 1} + C", [f"x{sup(n - 1)}/{n - 1} + C" if n > 2 else "x + C", f"{n}x{sup(n - 1)} + C" if n > 2 else f"{n}x + C", f"x{sup(n + 1)} + C"], 1)
def a4_hs(rng):
    a, b = rng.randint(1, 5), rng.randint(1, 6); return M(f"Nguyên hàm của f(x) = {2 * a}x + {b} là:", f"{a}x² + {b}x + C", [f"{2 * a}x² + {b}x + C", f"{a}x² + C", f"{2 * a}x + {b}x + C"], 1)
def a4_sin(rng):
    return M("Nguyên hàm của f(x) = cos x là:", "sin x + C", ["-sin x + C", "cos x + C", "-cos x + C"], 1)
def a4_ex(rng):
    return M("Nguyên hàm của f(x) = eˣ là:", "eˣ + C", ["xeˣ + C", "eˣ/x + C", "ln x + C"], 1)
def a4_1x(rng):
    return M("Nguyên hàm của f(x) = 1/x (x > 0) là:", "ln x + C", ["-1/x² + C", "x + C", "eˣ + C"], 1)
def a4_tp(rng):
    a, b = rng.randint(0, 3), rng.randint(4, 7); return nint(rng, f"Tích phân ∫ từ {a} đến {b} của 1 dx bằng:", b - a, 1, (1, 2), 0)
def a4_tp2(rng):
    a = rng.randint(1, 5); return nint(rng, f"Tích phân ∫ từ 0 đến {a} của 2x dx bằng:", a * a, 2, (1, 2, 3), 0)
def a4_tp3(rng):
    a = rng.randint(1, 4); return M(f"Tích phân ∫ từ 0 đến {a} của x² dx bằng:", ps(Fraction(a ** 3, 3)), [ps(Fraction(a ** 2, 2)), ps(Fraction(a ** 3)), ps(Fraction(a ** 3, 2))], 2)
def a4_tp4(rng):
    a, b = rng.randint(1, 4), rng.randint(5, 9); return nint(rng, f"Tích phân ∫ từ {a} đến {b} của 3 dx bằng:", 3 * (b - a), 2, (1, 3, 6), 0)
def a4_tc(rng):
    return M("Tích chất tích phân: ∫ từ a đến b của f(x)dx + ∫ từ b đến c của f(x)dx bằng:", "∫ từ a đến c của f(x)dx", ["∫ từ a đến b của 2f(x)dx", "0", "f(c) - f(a)"], 1)
def a4_doi(rng):
    return M("Khi đổi cận tích phân (đảo a và b) thì giá trị tích phân:", "Đổi dấu", ["Giữ nguyên", "Nhân đôi", "Bằng 0"], 1)
def a4_dt(rng):
    a = rng.randint(1, 4); return M(f"Diện tích hình phẳng giới hạn bởi y = x, trục Ox, x = 0 và x = {a} là:", ps(Fraction(a * a, 2)), [ps(Fraction(a * a)), ps(Fraction(a)), ps(Fraction(a ** 3, 3))], 2)
def a4_thetich(rng):
    return M("Thể tích khối tròn xoay tạo bởi quay hình phẳng quanh trục Ox được tính bằng:", "π∫ f²(x)dx", ["∫ f(x)dx", "π∫ f(x)dx", "2π∫ f(x)dx"], 1)
def a4_dh(rng):
    return M("Nếu F'(x) = f(x) thì F(x) là:", "Một nguyên hàm của f(x)", ["Đạo hàm của f(x)", "Tích phân của f(x)", "Hàm hằng"], 1)
def a4_newton(rng):
    return M("Công thức Newton–Leibniz: ∫ từ a đến b của f(x)dx bằng:", "F(b) - F(a)", ["F(a) - F(b)", "F(a) + F(b)", "f(b) - f(a)"], 1)
def b4_nguyenham(rng):
    a, b, c = rng.randint(1, 5), rng.randint(1, 5), rng.randint(1, 6); return T(f"Tìm nguyên hàm của f(x) = {3 * a}x² + {2 * b}x + {c}.", f"F(x) = {a}x³ + {b}x² + {c}x + C", 1)
def b4_tp(rng):
    a = rng.randint(1, 4); return T(f"Tính ∫ từ 0 đến {a} của (2x + 1) dx.", f"= [x² + x] từ 0 đến {a} = {a * a + a}", 2)
def b4_dt(rng):
    a = rng.randint(1, 4); return T(f"Tính diện tích hình phẳng giới hạn bởi y = x², trục Ox, x = 0 và x = {a}.", f"S = ∫ từ 0 đến {a} của x² dx = {a}³/3 = {ps(Fraction(a ** 3, 3))}", 2)
def b4_thetich(rng):
    a = rng.randint(1, 3); return T(f"Tính thể tích khối tròn xoay do hình phẳng giới hạn bởi y = x, Ox, x = 0, x = {a} quay quanh Ox.", f"V = π∫ từ 0 đến {a} của x² dx = π·{a}³/3 = π·{ps(Fraction(a ** 3, 3))}", 3)
def b4_doibien(rng):
    return T("Tính ∫ từ 0 đến 1 của 2x(x² + 1)³ dx bằng phương pháp đổi biến.", "Đặt t = x² + 1, dt = 2x dx; x: 0→1 ⇒ t: 1→2. I = ∫ từ 1 đến 2 của t³ dt = (2⁴ - 1)/4 = 15/4.", 3)
def b4_pp(rng):
    return T("Nêu các phương pháp tính tích phân thường gặp.", "Dùng định nghĩa/nguyên hàm cơ bản; phương pháp đổi biến số; phương pháp tích phân từng phần: ∫u dv = uv - ∫v du.", 1)
def b4_tptp(rng):
    return T("Tính ∫ từ 0 đến 1 của x·eˣ dx bằng tích phân từng phần.", "Đặt u = x, dv = eˣdx ⇒ du = dx, v = eˣ. I = [x eˣ] - ∫ eˣ dx = e - (e - 1) = 1.", 3)

# ===== 5. Phương pháp tọa độ trong không gian =====
def a5_pt(rng):
    a, b, c, d = nz(rng, -4, 4), nz(rng, -4, 4), nz(rng, -4, 4), rng.randint(-6, 6); return M(f"Vectơ pháp tuyến của mặt phẳng {a}x + {b}y + {c}z + {d} = 0 là:".replace("+ -", "- "), vec([a, b, c]), [vec([a, b, d]), vec([-a, b, c]), vec([d, b, c])], 1)
def a5_qua(rng):
    a, b, c = nz(rng, -3, 3), nz(rng, -3, 3), nz(rng, -3, 3); x, y, z = rng.randint(-3, 3), rng.randint(-3, 3), rng.randint(-3, 3); d = -(a * x + b * y + c * z); return M(f"Mặt phẳng đi qua M({x}; {y}; {z}) nhận n = {vec([a, b, c])} làm vectơ pháp tuyến có phương trình dạng ax + by + cz + d = 0 với d bằng:", d, [-d if d else 1, d + 1, d - 1], 2)
def a5_kc(rng):
    a, b, c, d, x, y, z = rng.choice([(1, 2, 2, 0, 3, 0, 0), (2, 3, 6, 0, 7, 0, 0), (1, 2, 2, -3, 0, 0, 0), (2, 3, 6, 7, 0, 0, 0), (3, 4, 0, 10, 0, 0, 0)]); dd = abs(a * x + b * y + c * z + d) / math.sqrt(a * a + b * b + c * c); return M(f"Khoảng cách từ M({x}; {y}; {z}) đến mặt phẳng {a}x + {b}y + {c}z + {d} = 0 là:".replace("+ -", "- "), tt(round(dd, 4)), [tt(round(dd + 1, 4)), tt(round(dd * 2, 4)), tt(round(dd + 2, 4))], 3)
def a5_cau(rng):
    a, b, c, r = rng.randint(-4, 4), rng.randint(-4, 4), rng.randint(-4, 4), rng.randint(1, 6); return M(f"Mặt cầu tâm I({a}; {b}; {c}), bán kính {r} có phương trình:", f"(x {'-' if a >= 0 else '+'} {abs(a)})² + (y {'-' if b >= 0 else '+'} {abs(b)})² + (z {'-' if c >= 0 else '+'} {abs(c)})² = {r * r}", [f"(x {'+' if a >= 0 else '-'} {abs(a)})² + (y {'+' if b >= 0 else '-'} {abs(b)})² + (z {'+' if c >= 0 else '-'} {abs(c)})² = {r * r}", f"(x {'-' if a >= 0 else '+'} {abs(a)})² + (y {'-' if b >= 0 else '+'} {abs(b)})² + (z {'-' if c >= 0 else '+'} {abs(c)})² = {r}", f"(x {'-' if a >= 0 else '+'} {abs(a)}) + (y {'-' if b >= 0 else '+'} {abs(b)}) + (z {'-' if c >= 0 else '+'} {abs(c)}) = {r * r}"], 2) if a and b and c else None
def a5_ban(rng):
    a, b, c, r = rng.randint(0, 4), rng.randint(0, 4), rng.randint(0, 4), rng.randint(1, 8); return nint(rng, f"Mặt cầu (x - {a})² + (y - {b})² + (z - {c})² = {r * r} có bán kính là:", r, 1, (1, 2, 3), 0)
def a5_vtcp(rng):
    a, b, c = nz(rng, -4, 4), nz(rng, -4, 4), nz(rng, -4, 4); return M(f"Đường thẳng d: x = 1 + {a}t, y = 2 + {b}t, z = 3 + {c}t có vectơ chỉ phương là:".replace("+ -", "- "), vec([a, b, c]), [vec([1, 2, 3]), vec([-a, b, c]), vec([a, b, c + 1])], 1)
def a5_diem(rng):
    x, y, z = rng.randint(-4, 4), rng.randint(-4, 4), rng.randint(-4, 4); a, b, c = nz(rng, -3, 3), nz(rng, -3, 3), nz(rng, -3, 3); return M(f"Đường thẳng đi qua M({x}; {y}; {z}) có vectơ chỉ phương ({a}; {b}; {c}). Điểm nào thuộc đường thẳng ứng với t = 1?", f"({x + a}; {y + b}; {z + c})", [f"({x - a}; {y - b}; {z - c})", f"({x}; {y}; {z})", f"({x + a}; {y + b}; {z - c})"], 2)
def a5_song(rng):
    return M("Hai mặt phẳng song song khi vectơ pháp tuyến của chúng:", "Cùng phương", ["Vuông góc", "Bằng 0", "Có độ dài bằng nhau"], 1)
def a5_vuong(rng):
    return M("Hai mặt phẳng vuông góc khi tích vô hướng hai vectơ pháp tuyến bằng:", 0, [1, -1, 2], 1)
def a5_ptmp(rng):
    return M("Mặt phẳng (Oxy) có phương trình:", "z = 0", ["x = 0", "y = 0", "x + y = 0"], 1)
def a5_goc(rng):
    return M("Góc giữa hai mặt phẳng bằng góc giữa:", "Hai vectơ pháp tuyến (hoặc bù với nó)", ["Hai vectơ chỉ phương", "Hai điểm bất kì", "Hai trục tọa độ"], 1)
def a5_cat(rng):
    r = rng.randint(2, 6); d = rng.choice([r - 1, r, r + 1]); kq = "Cắt mặt cầu" if d < r else "Tiếp xúc mặt cầu" if d == r else "Không cắt mặt cầu"; return M(f"Mặt phẳng cách tâm mặt cầu bán kính {r} một khoảng {d}. Vị trí tương đối là:", kq, [x for x in ["Cắt mặt cầu", "Tiếp xúc mặt cầu", "Không cắt mặt cầu", "Chứa tâm mặt cầu"] if x != kq][:3], 2)
def b5_mp(rng):
    a, b, c = nz(rng, -3, 3), nz(rng, -3, 3), nz(rng, -3, 3); x, y, z = rng.randint(-3, 3), rng.randint(-3, 3), rng.randint(-3, 3); d = -(a * x + b * y + c * z); return T(f"Lập phương trình mặt phẳng đi qua M({x}; {y}; {z}) và có vectơ pháp tuyến n = {vec([a, b, c])}.", f"{a}(x - {x}) + {b}(y - {y}) + {c}(z - {z}) = 0 ⇔ {a}x + {b}y + {c}z + {d} = 0.".replace("- -", "+ ").replace("+ -", "- "), 2)
def b5_duong(rng):
    x, y, z = rng.randint(-3, 3), rng.randint(-3, 3), rng.randint(-3, 3); a, b, c = nz(rng, -3, 3), nz(rng, -3, 3), nz(rng, -3, 3); return T(f"Viết phương trình tham số của đường thẳng đi qua A({x}; {y}; {z}) có vectơ chỉ phương u = {vec([a, b, c])}.", f"x = {x} + {a}t; y = {y} + {b}t; z = {z} + {c}t (t ∈ ℝ).".replace("+ -", "- "), 1)
def b5_cau(rng):
    a, b, c, r = rng.randint(-3, 3), rng.randint(-3, 3), rng.randint(-3, 3), rng.randint(2, 6); return T(f"Viết phương trình mặt cầu tâm I({a}; {b}; {c}), bán kính {r}.", f"(x - ({a}))² + (y - ({b}))² + (z - ({c}))² = {r * r}", 1)
def b5_kc(rng):
    return T("Tính khoảng cách từ M(1; 2; 3) đến mặt phẳng 2x + y - 2z + 1 = 0.", "d = |2·1 + 2 - 2·3 + 1|/√(4 + 1 + 4) = |-1|/3 = 1/3.", 2)
def b5_vtt(rng):
    return T("Xét vị trí tương đối của hai mặt phẳng (P): x + y + z - 1 = 0 và (Q): 2x + 2y + 2z - 5 = 0.", "n_P = (1;1;1), n_Q = (2;2;2) cùng phương, nhưng -1/-5 ≠ 1/2 nên (P) ∥ (Q).", 2)
def b5_goc(rng):
    return T("Tính góc giữa hai mặt phẳng (P): x - y = 0 và (Q): y = 0.", "n_P = (1;-1;0), n_Q = (0;1;0). cos = |−1|/(√2·1) = √2/2 ⇒ góc 45°.", 2)

# ===== 6. Xác suất có điều kiện =====
def a6_dk(rng):
    a, b = rng.randint(2, 5), rng.randint(6, 9); x = Fraction(1, a); y = Fraction(1, b) if False else Fraction(1, a * 2); return M(f"P(B) = {ps(x)}, P(A ∩ B) = {ps(y)}. P(A | B) bằng:", ps(y / x), nh_ps(rng, y / x) if y / x < 1 else [ps(x), ps(y), ps(x + y)], 2)
def a6_dk2(rng):
    a = rng.choice([Fraction(3, 10), Fraction(2, 5), Fraction(1, 4), Fraction(3, 8)]); b = rng.choice([Fraction(3, 5), Fraction(1, 2), Fraction(3, 4)]); 
    inter = a * b * Fraction(1, 2); return M(f"P(A) = {ps(a)}, P(B) = {ps(b)}, P(A ∩ B) = {ps(inter)}. P(A | B) bằng:", ps(inter / b), [ps(inter / a) if inter / a != inter / b else ps(a), ps(inter * b), ps(a * b)], 3) if inter / b < 1 else None
def a6_nhan(rng):
    a, b = rng.choice([(Fraction(1, 2), Fraction(1, 3)), (Fraction(2, 5), Fraction(1, 4)), (Fraction(3, 4), Fraction(2, 3))]); return M(f"P(A) = {ps(a)}, P(B | A) = {ps(b)}. P(A ∩ B) bằng:", ps(a * b), [ps(a + b) if a + b < 1 else ps(a), ps(b / a) if b / a < 1 else ps(a / b), ps(a - b)], 2)
def a6_dl(rng):
    return M("Nếu A, B độc lập thì P(A | B) bằng:", "P(A)", ["P(B)", "P(A)P(B)", "0"], 1)
def a6_tp(rng):
    return M("Công thức xác suất toàn phần với hệ đầy đủ A, Ā: P(B) bằng:", "P(A)P(B|A) + P(Ā)P(B|Ā)", ["P(A)P(B)", "P(A) + P(B)", "P(B|A)·P(A|B)"], 1)
def a6_bayes(rng):
    return M("Công thức Bayes cho P(A | B) bằng:", "P(A)P(B|A)/P(B)", ["P(A)P(B)", "P(B|A)/P(A)", "P(A) + P(B|A)"], 1)
def a6_ban(rng):
    a, b = rng.choice([(0.8, 0.6), (0.7, 0.5), (0.9, 0.6), (0.6, 0.5)]); return M(f"Hai người bắn độc lập, xác suất trúng lần lượt {tt(a)} và {tt(b)}. Xác suất cả hai cùng trúng là:", tt(round(a * b, 4)), [tt(round(a + b - a * b, 4)), tt(round(a + b, 4)) if a + b < 1 else tt(round(abs(a - b), 4)), tt(round(abs(a - b), 4))], 2)
def a6_it(rng):
    a, b = rng.choice([(0.8, 0.6), (0.7, 0.5), (0.9, 0.6), (0.6, 0.5)]); return M(f"Hai người bắn độc lập, xác suất trúng lần lượt {tt(a)} và {tt(b)}. Xác suất có ít nhất một người trúng là:", tt(round(1 - (1 - a) * (1 - b), 4)), [tt(round(a * b, 4)), tt(round(a + b, 4)) if a + b < 1 else tt(round(abs(a - b), 4)), tt(round(abs(a - b), 4))], 2)
def a6_hop(rng):
    n, m = rng.randint(3, 6), rng.randint(3, 6); f = Fraction(n - 1, n + m - 1); return M(f"Hộp có {n} bi đỏ, {m} bi xanh. Lấy lần lượt 2 viên không hoàn lại. Biết viên thứ nhất đỏ, xác suất viên thứ hai đỏ là:", ps(f), nh_ps(rng, f), 3)
def a6_hop2(rng):
    n, m = rng.randint(3, 6), rng.randint(3, 6); f = Fraction(m, n + m - 1); return M(f"Hộp có {n} bi đỏ, {m} bi xanh. Lấy lần lượt 2 viên không hoàn lại. Biết viên thứ nhất đỏ, xác suất viên thứ hai xanh là:", ps(f), nh_ps(rng, f), 3)
def a6_xuc(rng):
    return M("Gieo một con xúc xắc. Biết số chấm là số chẵn, xác suất số chấm là 6 bằng:", "1/3", ["1/6", "1/2", "2/3"], 2)
def a6_dkx(rng):
    return M("Điều kiện để xác suất P(A | B) có nghĩa là:", "P(B) > 0", ["P(A) > 0", "P(A) = P(B)", "A và B xung khắc"], 1)
def a6_cay(rng):
    return M("Trong sơ đồ hình cây, xác suất của một đường đi từ gốc đến lá bằng:", "Tích các xác suất trên các nhánh", ["Tổng các xác suất trên nhánh", "Xác suất nhánh đầu", "Hiệu các xác suất"], 1)
def b6_dk(rng):
    n, m = rng.randint(3, 6), rng.randint(3, 6); f = Fraction(n - 1, n + m - 1); return T(f"Hộp có {n} bi đỏ, {m} bi xanh. Lấy lần lượt hai viên không hoàn lại. Tính xác suất viên thứ hai đỏ biết viên thứ nhất đỏ.", f"Sau khi lấy 1 bi đỏ còn {n - 1} đỏ trong {n + m - 1} bi. P = {ps(f)}", 2)
def b6_tp(rng):
    return T("Có hai hộp: hộp I có 3 bi đỏ, 2 bi xanh; hộp II có 2 bi đỏ, 3 bi xanh. Chọn ngẫu nhiên một hộp rồi lấy một bi. Tính xác suất bi lấy được là đỏ.", "P = (1/2)(3/5) + (1/2)(2/5) = 1/2.", 3)
def b6_bayes(rng):
    return T("Một nhà máy có hai máy A, B sản xuất 60% và 40% sản phẩm; tỉ lệ phế phẩm lần lượt 2% và 3%. Lấy một sản phẩm thấy phế phẩm. Tính xác suất nó do máy A sản xuất.", "P(phế) = 0,6·0,02 + 0,4·0,03 = 0,024; P(A | phế) = 0,012/0,024 = 0,5.", 3)
def b6_dl(rng):
    return T("Chứng minh nếu A và B độc lập thì A và biến cố đối của B cũng độc lập.", "P(A ∩ B̄) = P(A) - P(A ∩ B) = P(A) - P(A)P(B) = P(A)(1 - P(B)) = P(A)P(B̄).", 3)
def b6_xd(rng):
    return T("Phát biểu công thức nhân xác suất và công thức xác suất toàn phần.", "P(A ∩ B) = P(A)·P(B | A); P(B) = P(A)P(B | A) + P(Ā)P(B | Ā).", 1)
def b6_xuc(rng):
    return T("Gieo một con xúc xắc. Tính xác suất được số 5 biết số chấm là số lẻ.", "P(A | B) = P(5)/P(lẻ) = (1/6)/(1/2) = 1/3.", 1)

CHU_DE = [
    ("Chương 1: Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số", [a1_dbien, a1_ct, a1_cd, a1_cubic, a1_cubic_x, a1_gtln, a1_gtnn, a1_doan, a1_tcd, a1_tcn, a1_giao, a1_hsgoc, a1_dau, a1_ct_dk], [b1_khaosat, b1_max, b1_tcn, b1_loi, b1_tt, b1_bbt]),
    ("Chương 2: Vectơ và hệ trục tọa độ trong không gian", [a2_cong, a2_hieu, a2_nhan, a2_dai, a2_ab, a2_tdiem, a2_trongtam, a2_tichvo, a2_vuong, a2_cungphuong, a2_oxyz, a2_hinhchieu, a2_dx, a2_goc, a2_hbh], [b2_toado, b2_tichvo, b2_hbh, b2_goc, b2_cm, b2_ct]),
    ("Chương 3: Các số đặc trưng đo mức độ phân tán của mẫu số liệu ghép nhóm", [a3_kbt, a3_dd, a3_tb, a3_pv, a3_sd, a3_dq, a3_so, a3_pvx, a3_tong, a3_rong, a3_dcdt, a3_q2], [b3_pv, b3_q, b3_so, b3_ct, b3_kbt, b3_ys]),
    ("Chương 4: Nguyên hàm và tích phân", [a4_xn, a4_hs, a4_sin, a4_ex, a4_1x, a4_tp, a4_tp2, a4_tp3, a4_tp4, a4_tc, a4_doi, a4_dt, a4_thetich, a4_dh, a4_newton], [b4_nguyenham, b4_tp, b4_dt, b4_thetich, b4_doibien, b4_pp, b4_tptp]),
    ("Chương 5: Phương pháp tọa độ trong không gian", [a5_pt, a5_qua, a5_kc, a5_cau, a5_ban, a5_vtcp, a5_diem, a5_song, a5_vuong, a5_ptmp, a5_goc, a5_cat], [b5_mp, b5_duong, b5_cau, b5_kc, b5_vtt, b5_goc]),
    ("Chương 6: Xác suất có điều kiện", [a6_dk, a6_dk2, a6_nhan, a6_dl, a6_tp, a6_bayes, a6_ban, a6_it, a6_hop, a6_hop2, a6_xuc, a6_dkx, a6_cay], [b6_dk, b6_tp, b6_bayes, b6_dl, b6_xd, b6_xuc]),
]
def _w(f):
    def g(rng):
        r = f(rng)
        if r is None: raise ValueError
        return r
    g.__name__ = f.__name__
    return g
CHU_DE = [(t, [_w(f) for f in m], [_w(f) for f in l]) for t, m, l in CHU_DE]
