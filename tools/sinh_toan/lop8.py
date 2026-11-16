from thcs import *
import math

def nz(rng, lo=-6, hi=6):
    return rng.choice([x for x in range(lo, hi + 1) if x])

# ============ 1. Đa thức nhiều biến ============
def p2(rng, n=3, lo=-5, hi=5):
    ks = rng.sample([(2, 0), (1, 1), (0, 2), (1, 0), (0, 1), (0, 0), (2, 1), (1, 2)], n)
    return {k: nz(rng, lo, hi) for k in ks}
def a1_bac(rng):
    p = p2(rng, 3); b = max(i + j for i, j in p); return nint(rng, f"Bậc của đa thức {da2(p)} là:", b, 1, (1, 2), 0)
def a1_gt(rng):
    p = p2(rng, 3); x, y = rng.randint(-3, 3), rng.randint(-3, 3); v = sum(c * x ** i * y ** j for (i, j), c in p.items())
    return nint(rng, f"Giá trị của đa thức {da2(p)} tại x = {x}, y = {y} là:", v, 2, (1, 2, 5))
def a1_cong(rng):
    p, q = p2(rng, 3), p2(rng, 3); r = padd2(p, q)
    if not r: raise ValueError
    return M(f"({da2(p)}) + ({da2(q)}) = ?", da2(r), sai_da2(rng, r), 2)
def a1_tru(rng):
    p, q = p2(rng, 3), p2(rng, 3); r = padd2(p, q, -1)
    if not r: raise ValueError
    return M(f"({da2(p)}) - ({da2(q)}) = ?", da2(r), sai_da2(rng, r), 2)
def a1_don(rng):
    a, b = nz(rng, -5, 5), nz(rng, -5, 5); i, j, k, l = rng.randint(1, 3), rng.randint(0, 2), rng.randint(0, 2), rng.randint(1, 3)
    r = {(i + k, j + l): a * b}
    return M(f"({mono(a, i, j)}) · ({mono(b, k, l)}) = ?", da2(r), sai_da2(rng, r) if len(r) else [], 2) if False else M(f"({'-' if a < 0 else ''}{mono(a, i, j)}) · ({'-' if b < 0 else ''}{mono(b, k, l)}) = ?", da2(r), [da2({(i + k, j + l): a * b + d}) for d in (1, -1, 2) if a * b + d] + [da2({(i + k + 1, j + l): a * b})], 2)
def a1_chia_don(rng):
    a, k = nz(rng, -5, 5), rng.randint(2, 5); i, j = rng.randint(2, 4), rng.randint(1, 3); b = rng.randint(1, i); c = rng.randint(0, j)
    num = {(i, j): a * k}; den = {(b, c): k}
    r = {(i - b, j - c): a}
    return M(f"({da2(num)}) : ({da2(den)}) = ?", da2(r), [da2({(i - b, j - c): a + d}) for d in (1, -1, 2) if a + d] + [da2({(i - b + 1, j - c): a})], 2)
def a1_nhan_dt(rng):
    a = rng.randint(2, 5); p = p2(rng, 2, -4, 4); q = {(1, 0): a}; r = pmul2(q, p)
    return M(f"{a}x·({da2(p)}) = ?", da2(r), sai_da2(rng, r), 2)
def a1_nhan(rng):
    p = {(1, 0): rng.randint(1, 3), (0, 0): nz(rng, -4, 4)}; q = {(1, 0): rng.randint(1, 3), (0, 1): nz(rng, -4, 4)}; r = pmul2(p, q)
    return M(f"({da2(p)})({da2(q)}) = ?", da2(r), sai_da2(rng, r), 3)
def a1_chia_dt(rng):
    a, b = nz(rng, -5, 5), nz(rng, -5, 5); c = rng.randint(2, 5)
    num = {(2, 0): a * c, (1, 0): b * c}; r = {(1, 0): a, (0, 0): b}
    return M(f"({da2(num)}) : {c}x = ?", da2(r), sai_da2(rng, r), 2)
def a1_dong_dang(rng):
    i, j = rng.randint(1, 3), rng.randint(1, 3); a, b = rng.randint(2, 6), rng.randint(2, 6); x = f"{mono(a, i, j)}"
    return M(f"Tổng của hai đơn thức đồng dạng {mono(a, i, j)} và {mono(b, i, j)} là:", mono(a + b, i, j), [mono(a * b, i, j), mono(a + b, i + 1, j), mono(a + b, i, j + 1)], 2)
def a1_he_so(rng):
    a = nz(rng, -9, 9); i, j = rng.randint(1, 3), rng.randint(1, 3)
    return M(f"Hệ số của đơn thức {'-' if a < 0 else ''}{mono(a, i, j)} là:", a, [-a, i, j], 1)
def a1_bac_don(rng):
    i, j, k = rng.randint(1, 4), rng.randint(1, 4), rng.randint(1, 3); a = rng.randint(2, 7)
    return nint(rng, f"Bậc của đơn thức {a}x{str(i).translate(SUP)}y{str(j).translate(SUP)}z{str(k).translate(SUP)} là:", i + j + k, 1, (1, 2), 0)
def b1_cong(rng):
    p, q = p2(rng, 3), p2(rng, 3)
    return T(f"Cho A = {da2(p)} và B = {da2(q)}. Tính A + B và A - B.", f"A + B = {da2(padd2(p, q))}\nA - B = {da2(padd2(p, q, -1))}", 2)
def b1_nhan(rng):
    p = {(1, 0): rng.randint(1, 3), (0, 0): nz(rng, -4, 4)}; q = {(1, 0): rng.randint(1, 3), (0, 1): nz(rng, -4, 4)}
    return T(f"Nhân hai đa thức ({da2(p)}) và ({da2(q)}).", da2(pmul2(p, q)), 3)
def b1_gt(rng):
    p = p2(rng, 3); x, y = rng.randint(-3, 3), rng.randint(-3, 3)
    return T(f"Tính giá trị của biểu thức A = {da2(p)} tại x = {x}, y = {y}.", f"A = {sum(c * x ** i * y ** j for (i, j), c in p.items())}", 1)
def b1_chia(rng):
    a, b = nz(rng, -5, 5), nz(rng, -5, 5); c = rng.randint(2, 5)
    return T(f"Thực hiện phép chia ({da2({(2, 0): a * c, (1, 0): b * c})}) : {c}x.", da2({(1, 0): a, (0, 0): b}), 2)
def b1_bac(rng):
    p = p2(rng, 4); return T(f"Xác định bậc của đa thức {da2(p)} và thu gọn (nếu có hạng tử đồng dạng).", f"Bậc: {max(i + j for i, j in p)}", 1)
def b1_loi(rng):
    a, b = rng.randint(3, 9), rng.randint(2, 6)
    return T(f"Hình chữ nhật có chiều dài x + {a} (m) và chiều rộng x - {b} (m). Viết biểu thức diện tích và rút gọn.", f"S = (x + {a})(x - {b}) = x² + {a - b}x - {a * b}", 2) if a - b != 0 else (_ for _ in ()).throw(ValueError)

# ============ 2. Hằng đẳng thức đáng nhớ ============
def lin(a, b, v="x"): return da([a, b], v)
def a2_tong(rng):
    a, b = rng.randint(1, 4), rng.randint(1, 6); r = [a * a, 2 * a * b, b * b]
    return M(f"({lin(a, b)})² = ?", da(r), lay_sai_da(rng, r), 2)
def a2_hieu(rng):
    a, b = rng.randint(1, 4), rng.randint(1, 6); r = [a * a, -2 * a * b, b * b]
    return M(f"({lin(a, -b)})² = ?", da(r), lay_sai_da(rng, r), 2)
def a2_hh2(rng):
    a, b = rng.randint(1, 4), rng.randint(1, 8); r = [a * a, 0, -b * b]
    return M(f"({lin(a, b)})({lin(a, -b)}) = ?", da(r), lay_sai_da(rng, r), 2)
def a2_lp_tong(rng):
    b = rng.randint(1, 5); r = [1, 3 * b, 3 * b * b, b ** 3]
    return M(f"(x + {b})³ = ?", da(r), lay_sai_da(rng, r), 3)
def a2_lp_hieu(rng):
    b = rng.randint(1, 5); r = [1, -3 * b, 3 * b * b, -b ** 3]
    return M(f"(x - {b})³ = ?", da(r), lay_sai_da(rng, r), 3)
def a2_tong_lp(rng):
    b = rng.randint(1, 5); return M(f"x³ + {b ** 3} = ?", f"(x + {b})(x² - {b}x + {b * b})", [f"(x + {b})(x² + {b}x + {b * b})", f"(x + {b})³", f"(x - {b})(x² + {b}x + {b * b})"], 3)
def a2_hieu_lp(rng):
    b = rng.randint(1, 5); return M(f"x³ - {b ** 3} = ?", f"(x - {b})(x² + {b}x + {b * b})", [f"(x - {b})(x² - {b}x + {b * b})", f"(x - {b})³", f"(x + {b})(x² - {b}x + {b * b})"], 3)
def a2_hh2_nhan(rng):
    b = rng.randint(2, 12); return M(f"x² - {b * b} phân tích thành nhân tử là:", f"(x - {b})(x + {b})", [f"(x - {b})²", f"(x + {b})²", f"(x - {b * b})(x + {b * b})"], 2)
def a2_binhphuong_nt(rng):
    b = rng.randint(2, 9); return M(f"x² + {2 * b}x + {b * b} phân tích thành nhân tử là:", f"(x + {b})²", [f"(x - {b})²", f"(x + {b})(x - {b})", f"(x + {2 * b})²"], 2)
def a2_gt(rng):
    a = rng.randint(51, 99); return nint(rng, f"Tính nhanh {a}² - {a - 1}²... ".replace(f"{a}² - {a - 1}²... ", f"{a}² - {a - 1}²") + " ta được:", 2 * a - 1, 2, (1, 2, 10), 0)
def a2_gt2(rng):
    a = rng.randint(2, 9) * 10 + rng.choice([1, -1]); return nint(rng, f"Tính nhanh {a}² bằng cách dùng hằng đẳng thức:", a * a, 2, (10, 20, 2 * a), 0)
def a2_bt(rng):
    a = rng.randint(2, 8); x = rng.randint(-3, 4); return nint(rng, f"Giá trị của biểu thức (x + {a})² - (x - {a})² tại x = {x} là:", 4 * a * x, 3, (a, 2, 4))
def b2_khai(rng):
    a, b = rng.randint(1, 4), rng.randint(1, 6)
    return T(f"Khai triển: ({lin(a, b)})², ({lin(a, -b)})², ({lin(a, b)})({lin(a, -b)}).", f"({lin(a, b)})² = {da([a * a, 2 * a * b, b * b])}\n({lin(a, -b)})² = {da([a * a, -2 * a * b, b * b])}\n({lin(a, b)})({lin(a, -b)}) = {da([a * a, 0, -b * b])}", 1)
def b2_pt(rng):
    a, b = rng.randint(2, 8), rng.randint(2, 6)
    return T(f"Phân tích đa thức thành nhân tử: x² - {a * a}; x² + {2 * b}x + {b * b}; x³ - {b ** 3}.", f"x² - {a * a} = (x - {a})(x + {a})\nx² + {2 * b}x + {b * b} = (x + {b})²\nx³ - {b ** 3} = (x - {b})(x² + {b}x + {b * b})", 2)
def b2_tinh(rng):
    a = rng.randint(2, 9) * 10 + rng.choice([1, 2, -1, -2]); b = abs(a - round(a, -1))
    return T(f"Tính nhanh: {a}².", f"{a}² = ({round(a, -1)} {'+' if a > round(a, -1) else '-'} {b})² = {a * a}", 1)
def b2_x(rng):
    a = rng.randint(2, 9)
    return T(f"Tìm x, biết x² - {a * a} = 0.", f"(x - {a})(x + {a}) = 0 ⇒ x = {a} hoặc x = -{a}", 2)
def b2_cm(rng):
    return T("Chứng minh rằng (a + b)² - (a - b)² = 4ab với mọi a, b.", "(a + b)² - (a - b)² = (a² + 2ab + b²) - (a² - 2ab + b²) = 4ab.", 2)
def b2_min(rng):
    a = rng.randint(1, 6); c = rng.randint(1, 9)
    return T(f"Tìm giá trị nhỏ nhất của biểu thức A = x² + {2 * a}x + {a * a + c}.", f"A = (x + {a})² + {c} ≥ {c}. Giá trị nhỏ nhất là {c}, đạt khi x = -{a}.", 3)

# ============ 3. Tứ giác ============
def a3_tong(rng):
    a, b, c = rng.randint(60, 120), rng.randint(60, 110), rng.randint(60, 110); d = 360 - a - b - c
    if d <= 0 or d >= 180: raise ValueError
    return nint(rng, f"Tứ giác ABCD có góc A = {a}°, B = {b}°, C = {c}°. Số đo góc D là (độ):", d, 1, (10, 20, 5), 0)
def a3_hbh(rng):
    a = rng.randint(50, 120); return nint(rng, f"Hình bình hành ABCD có góc A = {a}°. Số đo góc C là (độ):", a, 1, (10, 20, 30), 0)
def a3_hbh2(rng):
    a = rng.randint(50, 120); return nint(rng, f"Hình bình hành ABCD có góc A = {a}°. Số đo góc B là (độ):", 180 - a, 1, (10, 20, 30), 0)
def a3_thang(rng):
    a = rng.randint(50, 120); return nint(rng, f"Hình thang ABCD (AB // CD) có góc A = {a}°. Số đo góc D là (độ):", 180 - a, 2, (10, 20, 30), 0)
def a3_thang_can(rng):
    a = rng.randint(50, 85); return nint(rng, f"Hình thang cân ABCD (AB // CD) có góc D = {a}°. Số đo góc C là (độ):", a, 2, (10, 20, 30), 0)
def a3_hcn(rng):
    a, b = rng.randint(3, 9), rng.randint(4, 12); d = math.isqrt(a * a + b * b)
    if d * d != a * a + b * b: raise ValueError
    return nint(rng, f"Hình chữ nhật ABCD có AB = {a} cm, BC = {b} cm. Độ dài đường chéo AC là (cm):", d, 3, (1, 2, 3), 0)
def a3_hcn2(rng):
    a, b = rng.choice([(3, 4), (5, 12), (6, 8), (8, 15), (9, 12), (12, 16), (7, 24), (15, 20)]); return nint(rng, f"Hình chữ nhật có hai cạnh {a} cm và {b} cm. Đường chéo dài (cm):", math.isqrt(a * a + b * b), 3, (1, 2, 3), 0)
def a3_thoi(rng):
    a, b = rng.randint(3, 10) * 2, rng.randint(2, 9) * 2; return nint(rng, f"Hình thoi có hai đường chéo dài {a} cm và {b} cm. Diện tích là (cm²):", a * b // 2, 2, (a, b, 10), 0)
def a3_vuong(rng):
    a = rng.randint(2, 12); return nint(rng, f"Hình vuông có cạnh {a} cm. Độ dài đường chéo bình phương (d²) bằng:", 2 * a * a, 3, (a, 2, 10), 0)
def a3_dau(rng):
    return M(rng.choice(["Tứ giác có hai đường chéo cắt nhau tại trung điểm của mỗi đường là:", "Tứ giác nào có hai đường chéo cắt nhau tại trung điểm mỗi đường?"]), "Hình bình hành", ["Hình thang", "Hình thang cân (không là hcn)", "Tứ giác bất kì"], 2)
def a3_dau2(rng):
    return M("Hình bình hành có một góc vuông là:", "Hình chữ nhật", ["Hình thoi", "Hình thang cân", "Hình thang vuông"], 1)
def a3_dau3(rng):
    return M("Hình chữ nhật có hai cạnh kề bằng nhau là:", "Hình vuông", ["Hình thoi (không vuông)", "Hình thang cân", "Hình bình hành (không đặc biệt)"], 1)
def a3_tc(rng):
    return M("Trong hình thoi, hai đường chéo:", "Vuông góc với nhau và cắt nhau tại trung điểm mỗi đường", ["Bằng nhau", "Song song với nhau", "Chỉ vuông góc, không cắt tại trung điểm"], 2)
def b3_goc(rng):
    a, b, c = rng.randint(60, 120), rng.randint(60, 110), rng.randint(60, 110); d = 360 - a - b - c
    if not 0 < d < 180: raise ValueError
    return T(f"Tứ giác ABCD có A = {a}°, B = {b}°, C = {c}°. Tính D và các góc ngoài tại mỗi đỉnh.", f"D = 360° - {a}° - {b}° - {c}° = {d}°\nGóc ngoài: {180 - a}°, {180 - b}°, {180 - c}°, {180 - d}°", 2)
def b3_hbh(rng):
    return T("Cho hình bình hành ABCD. Chứng minh AB = CD và AD = BC.", "Kẻ đường chéo AC. Vì AB // CD, AD // BC nên ABC = CDA (g.c.g) (cùng chung AC, các góc so le trong bằng nhau).\nSuy ra AB = CD và AD = BC.", 2)
def b3_hcn(rng):
    a, b = rng.choice([(3, 4), (5, 12), (6, 8), (8, 15), (9, 12)])
    return T(f"Hình chữ nhật có hai cạnh {a} cm và {b} cm. Tính đường chéo và diện tích.", f"Đường chéo: √({a}² + {b}²) = √{a * a + b * b} = {math.isqrt(a * a + b * b)} cm\nDiện tích: {a}·{b} = {a * b} cm²", 2)
def b3_thoi(rng):
    a, b = rng.randint(3, 10) * 2, rng.randint(2, 9) * 2
    return T(f"Hình thoi ABCD có AC = {a} cm, BD = {b} cm. Tính diện tích và cạnh của hình thoi (làm tròn nếu cần).", f"S = {a}·{b}:2 = {a * b // 2} cm²\nCạnh = √(({a}/2)² + ({b}/2)²) = √{(a // 2) ** 2 + (b // 2) ** 2}", 3)
def b3_dh(rng):
    return T("Nêu dấu hiệu nhận biết hình chữ nhật, hình thoi, hình vuông.", "Hình chữ nhật: tứ giác có ba góc vuông; hình bình hành có một góc vuông; hình bình hành có hai đường chéo bằng nhau.\nHình thoi: tứ giác có bốn cạnh bằng nhau; hình bình hành có hai cạnh kề bằng nhau; hai đường chéo vuông góc.\nHình vuông: hình chữ nhật có hai cạnh kề bằng nhau, hoặc hình thoi có một góc vuông.", 1)
def b3_thang(rng):
    a = rng.randint(50, 85)
    return T(f"Hình thang cân ABCD (AB // CD) có góc D = {a}°. Tính các góc còn lại.", f"C = D = {a}°; A = B = 180° - {a}° = {180 - a}°.", 2)

# ============ 4. Định lí Thalès ============
def a4_tile(rng):
    a, b, k = rng.randint(2, 8), rng.randint(2, 8), rng.randint(2, 5); return M(f"Tỉ số của hai đoạn thẳng AB = {a * k} cm và CD = {b * k} cm là:", ps(Fraction(a, b)), nh_ps(rng, Fraction(a, b)) if Fraction(a, b) < 1 else [ps(Fraction(b, a)), ps(Fraction(a + 1, b)), ps(Fraction(a, b + 1))], 1)
def a4_thales(rng):
    a, b, k = rng.randint(2, 6), rng.randint(2, 6), rng.randint(2, 5); return nint(rng, f"Tam giác ABC, MN // BC (M ∈ AB, N ∈ AC). Biết AM = {a} cm, MB = {b} cm, AN = {a * k} cm. Độ dài NC là (cm):", b * k, 3, (1, 2, 3), 0)
def a4_thales2(rng):
    a, b, k = rng.randint(2, 6), rng.randint(2, 6), rng.randint(2, 5); return nint(rng, f"Tam giác ABC, MN // BC, M ∈ AB, N ∈ AC, AM = {a} cm, AB = {a + b} cm, AN = {a * k} cm. Độ dài AC là (cm):", (a + b) * k, 3, (1, 2, 3), 0)
def a4_tb(rng):
    a = rng.randint(3, 15); return nint(rng, f"M, N lần lượt là trung điểm của AB, AC. Biết BC = {2 * a} cm. Độ dài MN là (cm):", a, 1, (1, 2, 3), 0)
def a4_tb2(rng):
    a = rng.randint(3, 15); return nint(rng, f"M, N lần lượt là trung điểm của AB, AC. Biết MN = {a} cm. Độ dài BC là (cm):", 2 * a, 1, (a, 2, 3), 0)
def a4_pg(rng):
    a, b, k = rng.randint(2, 6), rng.randint(2, 6), rng.randint(2, 4)
    if a == b: raise ValueError
    return nint(rng, f"Tam giác ABC có AD là phân giác (D ∈ BC), AB = {a} cm, AC = {b} cm, BD = {a * k} cm. Độ dài DC là (cm):", b * k, 3, (1, 2, 3), 0)
def a4_dao(rng):
    return M("Nếu một đường thẳng cắt hai cạnh của tam giác và định ra trên hai cạnh đó những đoạn thẳng tương ứng tỉ lệ thì đường thẳng đó:", "Song song với cạnh còn lại", ["Vuông góc với cạnh còn lại", "Trùng với cạnh còn lại", "Đi qua trọng tâm"], 2)
def a4_tl_xy(rng):
    a, b, c = rng.randint(2, 8), rng.randint(2, 8), rng.randint(2, 6); return nint(rng, f"Biết AB/CD = {a}/{b} và CD = {b * c} cm. Độ dài AB là (cm):", a * c, 2, (c, 2, 3), 0)
def a4_ten(rng):
    return M("Đường trung bình của tam giác có tính chất nào sau đây?", "Song song với cạnh thứ ba và bằng nửa cạnh đó", ["Vuông góc với cạnh thứ ba", "Bằng cạnh thứ ba", "Song song với cạnh thứ ba và dài gấp đôi cạnh đó"], 1)
def a4_tb3(rng):
    a, b = rng.randint(3, 12), rng.randint(3, 12); return nint(rng, f"Hình thang ABCD (AB // CD), M, N là trung điểm AD, BC. AB = {a * 2} cm, CD = {b * 2} cm. Độ dài đường trung bình MN là (cm):", a + b, 2, (1, 2, 3), 0)
def a4_gt(rng):
    a, b = rng.randint(2, 5), rng.randint(2, 5); k = rng.randint(2, 4); return nint(rng, f"Trong hình thang ABCD, AB // CD, hai đường chéo cắt nhau tại O. Biết OA = {a} cm, OC = {a * k} cm, OB = {b} cm. Độ dài OD là (cm):", b * k, 3, (1, 2, 3), 0)
def b4_thales(rng):
    a, b, k = rng.randint(2, 6), rng.randint(2, 6), rng.randint(2, 5)
    return T(f"Tam giác ABC có MN // BC (M ∈ AB, N ∈ AC). AM = {a} cm, MB = {b} cm, AN = {a * k} cm. Tính NC và AC.", f"AM/MB = AN/NC ⇒ NC = {b}·{a * k}/{a} = {b * k} cm\nAC = {a * k} + {b * k} = {(a + b) * k} cm", 2)
def b4_tb(rng):
    a = rng.randint(3, 12)
    return T(f"Cho tam giác ABC, M, N là trung điểm của AB, AC. Biết BC = {2 * a} cm. Tính MN và chứng minh MN // BC.", f"MN là đường trung bình của ΔABC nên MN // BC và MN = BC : 2 = {a} cm.", 2)
def b4_pg(rng):
    a, b, k = rng.randint(2, 6), rng.randint(2, 6), rng.randint(2, 4)
    if a == b: raise ValueError
    return T(f"Tam giác ABC có AB = {a * k} cm, AC = {b * k} cm, AD là phân giác (D ∈ BC), BC = {(a + b) * k} cm. Tính BD và DC.", f"BD/DC = AB/AC = {a}/{b}\nBD = {(a + b) * k}·{a}/{a + b} = {a * k} cm; DC = {b * k} cm", 3)
def b4_cm(rng):
    return T("Phát biểu định lí Thalès và định lí đảo của nó trong tam giác.", "Thalès: Nếu một đường thẳng song song với một cạnh của tam giác và cắt hai cạnh còn lại thì nó định ra trên hai cạnh đó những đoạn thẳng tương ứng tỉ lệ.\nĐịnh lí đảo: Nếu một đường thẳng cắt hai cạnh của tam giác và định ra trên hai cạnh đó những đoạn thẳng tương ứng tỉ lệ thì đường thẳng đó song song với cạnh còn lại.", 1)
def b4_tl(rng):
    a, b = rng.randint(2, 9), rng.randint(2, 9); k = rng.randint(2, 5)
    return T(f"Cho AB = {a * k} cm, CD = {b * k} cm. Tính tỉ số AB/CD, rồi suy ra AB nếu CD = {b * k + b} cm giữ tỉ số không đổi.", f"AB/CD = {a}/{b}\nAB mới = {b * k + b}·{a}/{b} = {a * (k + 1)} cm", 2)
def b4_gt(rng):
    a, b = rng.randint(3, 12), rng.randint(3, 12)
    return T(f"Hình thang ABCD (AB // CD) có AB = {a * 2} cm, CD = {b * 2} cm. Gọi M, N là trung điểm của AD, BC. Tính MN.", f"MN là đường trung bình: MN = ({a * 2} + {b * 2}) : 2 = {a + b} cm", 2)

# ============ 5. Dữ liệu và biểu đồ ============
def a5_loai(rng):
    ds = [("Chiều cao của một nhóm học sinh", "Số liệu liên tục"), ("Số bàn thắng mỗi trận", "Số liệu rời rạc"), ("Màu sắc yêu thích", "Dữ liệu định tính"), ("Xếp loại học lực", "Dữ liệu định tính"), ("Số điện thoại của khách", "Không phải số liệu để tính toán"), ("Cân nặng của học sinh", "Số liệu liên tục")]
    x, d = rng.choice(ds); return M(f"\"{x}\" là:", d, chon3(rng, ["Số liệu liên tục", "Số liệu rời rạc", "Dữ liệu định tính", "Không phải số liệu để tính toán"], d), 2)
def a5_tong(rng):
    ds = [rng.randint(5, 40) for _ in range(5)]; return nint(rng, f"Số học sinh 5 lớp khối 8 lần lượt là {', '.join(map(str, ds))}. Tổng số học sinh là:", sum(ds), 1, (1, 2, 5), 0)
def a5_tb(rng):
    n = rng.randint(4, 6); ds = [rng.randint(4, 10) for _ in range(n)]
    if sum(ds) % n: raise ValueError
    return nint(rng, f"Điểm của {n} bài kiểm tra: {', '.join(map(str, ds))}. Điểm trung bình là:", sum(ds) // n, 2, (1, 2), 0)
def a5_pt(rng):
    a, b = rng.randint(5, 30), rng.randint(5, 30); n = a + b
    if a * 100 % n: raise ValueError
    return M(f"Khảo sát {n} học sinh, {a} bạn đi xe đạp, còn lại đi bộ. Tỉ lệ phần trăm số bạn đi xe đạp là:", f"{a * 100 // n}%", chon3(rng, [f"{a * 100 // n + 5}%", f"{a * 100 // n - 5}%", f"{b * 100 // n}%", f"{a}%"], f"{a * 100 // n}%"), 2)
def a5_goc(rng):
    p = rng.choice([10, 15, 20, 25, 30, 40, 45, 50]); return nint(rng, f"Trong biểu đồ hình quạt tròn, phần chiếm {p}% có góc ở tâm là (độ):", p * 360 // 100, 2, (10, 18, 36), 0)
def a5_cot(rng):
    ds = rng.sample(range(5, 50), 4); t = ["A", "B", "C", "D"]; i = ds.index(min(ds)); return M(f"Biểu đồ cột cho giá trị của A, B, C, D lần lượt là {', '.join(map(str, ds))}. Cột thấp nhất là:", t[i], [x for x in t if x != t[i]], 1)
def a5_tang(rng):
    a, b = rng.randint(20, 60), rng.randint(10, 40)
    if a <= b: raise ValueError
    return M(f"Doanh thu tháng 1 là {b} triệu đồng, tháng 2 là {a} triệu đồng. Tháng 2 tăng so với tháng 1 là:", f"{a - b} triệu đồng", chon3(rng, [f"{a + b} triệu đồng", f"{a} triệu đồng", f"{b} triệu đồng", f"{a - b + 5} triệu đồng"], f"{a - b} triệu đồng"), 1)
def a5_chon(rng):
    return M("Để biểu diễn sự thay đổi của nhiệt độ trong một ngày, nên dùng biểu đồ nào?", "Biểu đồ đoạn thẳng", ["Biểu đồ hình quạt tròn", "Biểu đồ tranh", "Bảng tần số ghép nhóm"], 2)
def a5_ss(rng):
    return M("Để so sánh trực quan số lượng giữa các nhóm rời rạc, nên dùng biểu đồ nào?", "Biểu đồ cột", ["Biểu đồ đoạn thẳng", "Biểu đồ hình quạt tròn", "Biểu đồ phân tán"], 1)
def a5_tilepc(rng):
    p = rng.choice([20, 25, 40, 50]); n = rng.randint(2, 9) * 20; return nint(rng, f"Biểu đồ hình quạt cho thấy {p}% trong tổng {n} học sinh thích bóng rổ. Số học sinh thích bóng rổ là:", n * p // 100, 2, (2, 5, 10), 0)
def a5_dl(rng):
    return M("Nguồn dữ liệu nào sau đây là nguồn đáng tin cậy để thống kê số học sinh của trường?", "Sổ quản lí học sinh của nhà trường", ["Lời đồn của học sinh", "Bài đăng ẩn danh trên mạng", "Phỏng đoán của một bạn"], 1)
def a5_bat_thuong(rng):
    ds = [rng.randint(6, 9) for _ in range(5)] + [rng.randint(1, 2)]; rng.shuffle(ds)
    return M(f"Cho dãy dữ liệu: {', '.join(map(str, ds))}. Giá trị nào dưới đây có thể là giá trị bất thường?", min(ds), [x for x in ds if x != min(ds)][:3] if len(set(x for x in ds if x != min(ds))) >= 3 else (_ for _ in ()).throw(ValueError), 3)
def b5_loai(rng):
    return T("Phân loại dữ liệu: (a) tên các bạn trong lớp; (b) số điểm 10 của mỗi bạn; (c) chiều cao của học sinh.", "(a) Dữ liệu định tính; (b) Số liệu rời rạc; (c) Số liệu liên tục.", 1)
def b5_tb(rng):
    ds = [rng.randint(4, 10) for _ in range(6)]
    return T(f"Điểm 6 bài kiểm tra của Hùng: {', '.join(map(str, ds))}. Tính điểm trung bình và cho biết điểm cao nhất, thấp nhất.", f"TB = {sum(ds)}/6 ≈ {sum(ds) / 6:.2f}\nCao nhất: {max(ds)}; thấp nhất: {min(ds)}".replace(".", ","), 1)
def b5_quat(rng):
    n = rng.randint(2, 6) * 20
    return T(f"Biểu đồ hình quạt biểu diễn học lực của {n} học sinh: Giỏi 30%, Khá 45%, Trung bình 25%. Tính số học sinh mỗi loại và góc ở tâm tương ứng.", f"Giỏi: {n * 30 // 100} HS, {108}°\nKhá: {n * 45 // 100} HS, {162}°\nTrung bình: {n * 25 // 100} HS, {90}°", 2)
def b5_chon(rng):
    return T("Nêu cách chọn biểu đồ: biểu diễn (a) tỉ lệ các loại hoạt động ngoại khóa; (b) lượng mưa theo tháng trong năm; (c) số học sinh mỗi lớp.", "(a) hình quạt tròn; (b) đoạn thẳng (hoặc cột); (c) biểu đồ cột.", 1)
def b5_pt(rng):
    a, b = rng.randint(10, 40), rng.randint(10, 40)
    return T(f"Năm trước trường có {a} học sinh giỏi, năm nay có {b} học sinh giỏi. Tính tỉ lệ phần trăm tăng (hoặc giảm) so với năm trước, làm tròn đến hàng phần mười.", f"({b} - {a})/{a} = {(b - a) / a * 100:.1f}%".replace(".", ","), 2)
def b5_lap(rng):
    return T("Lập bảng thống kê số lần xuất hiện của các số trong dãy: 3, 5, 3, 4, 5, 3, 4, 3. Số nào xuất hiện nhiều nhất?", "Số 3: 4 lần; số 4: 2 lần; số 5: 2 lần. Số 3 xuất hiện nhiều nhất.", 1)

# ============ 6. Phân thức đại số ============
def a6_dkxd(rng):
    a = rng.randint(1, 9); return M(f"Điều kiện xác định của phân thức 1/(x - {a}) là:", f"x ≠ {a}", [f"x ≠ -{a}", f"x ≠ 0", f"x > {a}"], 1)
def a6_dkxd2(rng):
    a, b = rng.randint(2, 6), rng.randint(1, 9); return M(f"Điều kiện xác định của phân thức x/({a}x + {a * b}) là:", f"x ≠ -{b}", [f"x ≠ {b}", f"x ≠ -{a}", f"x ≠ {a * b}"], 2)
def a6_dkxd3(rng):
    a = rng.randint(2, 9); return M(f"Điều kiện xác định của phân thức 2/(x² - {a * a}) là:", f"x ≠ ±{a}", [f"x ≠ {a}", f"x ≠ -{a}", f"x ≠ {a * a}"], 2)
def a6_rutgon(rng):
    a, k = rng.randint(2, 9), rng.randint(2, 5); return M(f"Rút gọn phân thức ({k}x² - {k * a * a})/({k}x - {k * a}) ta được:", f"x + {a}", [f"x - {a}", f"{k}(x + {a})", f"x² + {a}"], 2)
def a6_rutgon2(rng):
    a, b = rng.randint(2, 9), rng.randint(2, 6); return M(f"Rút gọn phân thức ({a * b}x²y)/({a}xy²) ta được:", f"{b}x/y", [f"{b}y/x", f"{a * b}x/y", f"{b}xy"], 2)
def a6_cong(rng):
    a, b = rng.randint(2, 9), rng.randint(2, 9); return M(f"Tính: {a}/x + {b}/x (với x ≠ 0).", f"{a + b}/x", [f"{a * b}/x", f"{a + b}/(2x)", f"{a + b}/x²"], 1)
def a6_tru(rng):
    a, b = rng.randint(6, 12), rng.randint(2, 5); return M(f"Tính: {a}/(x + 1) - {b}/(x + 1) (với x ≠ -1).", f"{a - b}/(x + 1)", [f"{a + b}/(x + 1)", f"{a - b}/(x - 1)", f"{a - b}"], 2)
def a6_nhan(rng):
    a, b = rng.randint(2, 6), rng.randint(2, 6); return M(f"Tính: ({a}/x)·(x/{b}) (với x ≠ 0).", ps(Fraction(a, b)), [ps(Fraction(b, a)), f"{a * b}", f"{a}x²/{b}"], 2)
def a6_chia(rng):
    a, b = rng.randint(2, 6), rng.randint(2, 6); return M(f"Tính: ({a}x/{b}) : (x/{a}) (với x ≠ 0).", ps(Fraction(a * a, b)), [ps(Fraction(b, a * a)), ps(Fraction(a, b)), f"{a}x²"], 3)
def a6_doi(rng):
    a = rng.randint(2, 9); return M(f"Phân thức đối của phân thức ({a}x)/(x + 1) là:", f"-({a}x)/(x + 1)", [f"({a}x)/(x - 1)", f"(x + 1)/({a}x)", f"{a}x/(x + 1)"], 1)
def a6_bang(rng):
    a, b, k = rng.randint(2, 6), rng.randint(2, 6), rng.randint(2, 5); return M(f"Hai phân thức {a}/x và {a * k}/({k}x) có bằng nhau không (x ≠ 0)?", "Có", ["Không", "Chỉ khi x > 0", "Chỉ khi x = 1"], 2)
def a6_gt(rng):
    a, x = rng.randint(2, 8), rng.randint(2, 9); return M(f"Giá trị của phân thức (x² - {a * a})/(x - {a}) tại x = {x} (x ≠ {a}) là:", x + a, [x - a, x * a, a * a + x][:3] if len({x + a, x - a, x * a, a * a + x}) == 4 else (_ for _ in ()).throw(ValueError), 3) if x != a else (_ for _ in ()).throw(ValueError)
def b6_rutgon(rng):
    a, k = rng.randint(2, 9), rng.randint(2, 5)
    return T(f"Rút gọn phân thức ({k}x² - {k * a * a})/({k}x + {k * a}) và nêu điều kiện xác định.", f"= {k}(x - {a})(x + {a})/({k}(x + {a})) = x - {a}\nĐKXĐ: x ≠ -{a}", 2)
def b6_cong(rng):
    a, b = rng.randint(2, 6), rng.randint(2, 6); return T(f"Thực hiện phép tính: {a}/(x + {b}) + x/(x + {b}).", f"= ({a} + x)/(x + {b}) = (x + {a})/(x + {b})", 2)
def b6_tru(rng):
    a, b = rng.randint(3, 8), rng.randint(2, 5)
    return T(f"Thực hiện phép tính: ({a}x + {b})/(x - 1) - ({b}x + 1)/(x - 1).", f"= ({a}x + {b} - {b}x - 1)/(x - 1) = ({a - b}x + {b - 1})/(x - 1)", 2)
def b6_nhan(rng):
    a, b = rng.randint(2, 7), rng.randint(2, 7)
    return T(f"Thực hiện phép tính: (x² - {a * a})/(x + {b}) · ({b}x + {b * b})/(x - {a}).", f"= (x - {a})(x + {a})/(x + {b}) · {b}(x + {b})/(x - {a}) = {b}(x + {a})", 3)
def b6_dkxd(rng):
    a, b = rng.randint(2, 9), rng.randint(2, 9)
    return T(f"Tìm điều kiện xác định của các phân thức: 1/(x - {a}); x/(x² - {b * b}).", f"x ≠ {a}; x ≠ {b} và x ≠ -{b}.", 1)
def b6_gt(rng):
    a, x = rng.randint(2, 6), rng.randint(2, 8)
    if x == a: raise ValueError
    return T(f"Rút gọn rồi tính giá trị của biểu thức (x² - {a * a})/(x - {a}) tại x = {x}.", f"(x² - {a * a})/(x - {a}) = x + {a}\nTại x = {x}: {x} + {a} = {x + a}", 2)

# ============ 7. Phương trình bậc nhất và hàm số bậc nhất ============
def a7_pt(rng):
    a, b, x = nz(rng, -7, 7), nz(rng, -9, 9), nz(rng, -6, 8); return nint(rng, f"Nghiệm của phương trình {da([a, b]).replace('x','x')} = {a * x + b} là:", x, 1, (1, 2, 3))
def a7_pt2(rng):
    a, b, c, x = rng.randint(2, 6), rng.randint(1, 8), rng.randint(1, 5), rng.randint(-5, 8)
    if a == c: raise ValueError
    return nint(rng, f"Nghiệm của phương trình {a}x + {b} = {c}x + {c * x + b - (a - c) * x + 0 if False else c * x - (a * x) + (a * x + b)} là:", x, 2, (1, 2, 3)) if False else nint(rng, f"Nghiệm của phương trình {a}x + {b} = {c}x + {a * x + b - c * x} là:", x, 2, (1, 2, 3))
def a7_pt3(rng):
    a, b, x = rng.randint(2, 6), rng.randint(1, 5), rng.randint(-4, 6); return nint(rng, f"Nghiệm của phương trình {a}(x - {b}) = {a * (x - b)} là:", x, 2, (1, 2, 3))
def a7_pt4(rng):
    k, x = rng.randint(2, 6), rng.randint(-6, 8); a, b = rng.randint(1, 5), rng.randint(1, 7)
    return M(f"Tập nghiệm của phương trình (x - {a})(x + {b}) = 0 là:", f"{{{a}; -{b}}}", [f"{{-{a}; {b}}}", f"{{{a}; {b}}}", f"{{-{a}; -{b}}}"], 2)
def a7_ham(rng):
    a, b, x = nz(rng, -5, 5), rng.randint(-6, 6), rng.randint(-4, 5); return nint(rng, f"Cho hàm số y = {da([a, b])}. Giá trị của y khi x = {x} là:", a * x + b, 1, (1, 2, 5))
def a7_bac(rng):
    a = nz(rng, -5, 5); b = rng.randint(-5, 5); return M(f"Hàm số y = {da([a, b])} đồng biến khi:", "a > 0" if a > 0 else "a < 0 (không), vì a < 0 hàm nghịch biến", [], 2) if False else M(f"Hàm số y = {da([a, b])} là hàm số:", "đồng biến" if a > 0 else "nghịch biến", ["nghịch biến" if a > 0 else "đồng biến", "hàm hằng", "không là hàm số bậc nhất"], 2)
def a7_hsg(rng):
    a = nz(rng, -6, 6); b = rng.randint(-6, 6); return nint(rng, f"Hệ số góc của đường thẳng y = {da([a, b])} là:", a, 1, (1, 2, 3))
def a7_song(rng):
    a = nz(rng, -5, 5); b, c = rng.randint(-5, 5), rng.randint(-5, 5)
    if b == c: raise ValueError
    return M(f"Đường thẳng y = {da([a, b])} song song với đường thẳng nào dưới đây?", f"y = {da([a, c])}", [f"y = {da([a + 1, c])}", f"y = {da([-a, c])}", f"y = {da([a + 2, b])}"], 2)
def a7_cat_oy(rng):
    a, b = nz(rng, -5, 5), nz(rng, -7, 7); return nint(rng, f"Đồ thị hàm số y = {da([a, b])} cắt trục tung tại điểm có tung độ:", b, 1, (1, 2, 3))
def a7_cat_ox(rng):
    a, x = rng.randint(2, 5), rng.randint(-5, 6); b = -a * x; return nint(rng, f"Đồ thị hàm số y = {da([a, b])} cắt trục hoành tại điểm có hoành độ:", x, 2, (1, 2, 3))
def a7_thuoc(rng):
    a, b, x = nz(rng, -4, 4), rng.randint(-5, 5), rng.randint(-3, 4); y = a * x + b
    return M(f"Điểm nào thuộc đồ thị hàm số y = {da([a, b])}?", f"({x}; {y})", [f"({x}; {y + 1})", f"({x + 1}; {y})", f"({-x}; {y + 2})"], 2)
def a7_giao(rng):
    a, b = rng.randint(1, 4), rng.randint(1, 4)
    if a == b: raise ValueError
    x = rng.randint(-3, 4); c = (a - b) * x; return M(f"Hai đường thẳng y = {da([a, 0])} + {c if c >= 0 else f'({c})'} và y = {da([b, 0])} cắt nhau tại điểm có hoành độ:", -c // (a - b) if c % (a - b) == 0 else x, [x + 1, x - 1, -x + 2], 3) if False else nint(rng, f"Hoành độ giao điểm của hai đường thẳng y = {da([a, c])} và y = {da([b, 0])} là:", -c // (a - b) if c % (a - b) == 0 else 0, 3, (1, 2, 3)) if c % (a - b) == 0 else (_ for _ in ()).throw(ValueError)
def a7_bai(rng):
    a, b, x = rng.randint(2, 9), rng.randint(5, 30), rng.randint(2, 10); return nint(rng, f"Một xe taxi tính phí mở cửa {b} nghìn đồng và {a} nghìn đồng mỗi km. Đi {x} km phải trả (nghìn đồng):", b + a * x, 2, (a, 2, 5), 0)
def b7_pt(rng):
    a, b, c, x = rng.randint(2, 6), rng.randint(1, 8), rng.randint(1, 5), rng.randint(-5, 8)
    if a == c: raise ValueError
    return T(f"Giải phương trình {a}x + {b} = {c}x + {a * x + b - c * x}.", f"{a}x - {c}x = {a * x + b - c * x} - {b}\n{a - c}x = {(a - c) * x}\nx = {x}", 2)
def b7_tich(rng):
    a, b = rng.randint(1, 6), rng.randint(1, 6)
    return T(f"Giải phương trình (x - {a})(x + {b}) = 0.", f"x - {a} = 0 hoặc x + {b} = 0\nx = {a} hoặc x = -{b}", 1)
def b7_ham(rng):
    a, b = nz(rng, -4, 4), nz(rng, -5, 5)
    return T(f"Cho hàm số y = {da([a, b])}. Xác định hệ số góc, tung độ gốc và tìm giao điểm với hai trục toạ độ.", f"Hệ số góc: {a}; tung độ gốc: {b}\nGiao Oy: (0; {b})\nGiao Ox: y = 0 ⇒ x = {Fraction(-b, a)} ⇒ ({ps(Fraction(-b, a))}; 0)", 2)
def b7_song(rng):
    a, b, m = nz(rng, -4, 4), rng.randint(-5, 5), rng.randint(1, 7)
    return T(f"Tìm m để đồ thị hàm số y = ({m} + 2)x + 3 song song với đồ thị y = {m + 2}x - 1... ".replace(" song song với đồ thị y = {m + 2}x - 1... ", "") if False else f"Viết phương trình đường thẳng có hệ số góc {a} và đi qua điểm (0; {b}).", f"y = {da([a, b])}", 1)
def b7_loi(rng):
    v, t = rng.randint(2, 6) * 10, rng.randint(2, 5)
    return T(f"Một ô tô đi từ A đến B với vận tốc {v} km/h. Lập hàm số S theo thời gian t (giờ) và tính quãng đường sau {t} giờ.", f"S = {v}t\nKhi t = {t}: S = {v * t} km", 1)
def b7_bai(rng):
    a, b, x = rng.randint(2, 9), rng.randint(10, 40), rng.randint(2, 10)
    return T(f"Một người thuê xe: phí cố định {b} nghìn đồng, phí {a} nghìn đồng mỗi giờ. Viết hàm số tính tổng chi phí y theo số giờ x và tính chi phí khi x = {x}.", f"y = {a}x + {b}\nKhi x = {x}: y = {a * x + b} nghìn đồng", 2)

# ============ 8. Mở đầu về tính xác suất của biến cố ============
def a8_xs_cb(rng):
    n = rng.randint(2, 9) * 10; k = rng.randint(1, n // 5); f = Fraction(k, n); return M(f"Một hộp có {n} thẻ, trong đó {k} thẻ ghi số 1. Lấy ngẫu nhiên một thẻ. Xác suất lấy được thẻ ghi số 1 là:", ps(f), nh_ps(rng, f), 2)
def a8_kg(rng):
    n = rng.randint(2, 6); return nint(rng, f"Tung một đồng xu {n} lần liên tiếp. Số kết quả có thể xảy ra là:", 2 ** n, 3, (2, 4, 8), 0)
def a8_xuc(rng):
    return M("Gieo hai con xúc xắc. Số kết quả có thể xảy ra là:", 36, [12, 24, 6], 2)
def a8_tong(rng):
    s = rng.randint(2, 12); c = 6 - abs(s - 7); return M(f"Gieo hai con xúc xắc. Xác suất tổng số chấm bằng {s} là:", ps(Fraction(c, 36)), nh_ps(rng, Fraction(c, 36)), 3)
def a8_boi(rng):
    n = rng.choice([20, 30, 40, 50, 60, 100]); k = rng.choice([3, 4, 5, 7]); f = Fraction(n // k, n)
    return M(f"Chọn ngẫu nhiên một số từ 1 đến {n}. Xác suất chọn được số chia hết cho {k} là:", ps(f), nh_ps(rng, f), 3)
def a8_nto(rng):
    n = rng.choice([10, 20, 30]); c = len([x for x in range(2, n + 1) if nguyen_to(x)]); f = Fraction(c, n)
    return M(f"Chọn ngẫu nhiên một số từ 1 đến {n}. Xác suất chọn được số nguyên tố là:", ps(f), nh_ps(rng, f), 3)
def a8_dong(rng):
    return M("Tung hai đồng xu. Xác suất cả hai đồng đều ngửa là:", "1/4", ["1/2", "1/3", "1/8"], 2)
def a8_it_nhat(rng):
    return M("Tung hai đồng xu. Xác suất có ít nhất một đồng sấp là:", "3/4", ["1/4", "1/2", "2/3"], 3)
def a8_doi(rng):
    p = rng.choice([Fraction(1, 5), Fraction(1, 4), Fraction(2, 5), Fraction(3, 8), Fraction(1, 3)]); return M(f"Biết xác suất của biến cố A là {ps(p)}. Xác suất của biến cố đối của A là:", ps(1 - p), nh_ps(rng, 1 - p), 2)
def a8_xx(rng):
    return M("Hai kết quả được gọi là đồng khả năng khi:", "Chúng có cùng khả năng xảy ra", ["Chúng luôn xảy ra cùng nhau", "Chúng không thể xảy ra", "Chúng có xác suất bằng 1"], 1)
def a8_the(rng):
    n = rng.randint(10, 40); k = rng.randint(2, 8); f = Fraction(k, n); return M(f"Có {n} học sinh, {k} bạn thuận tay trái. Chọn ngẫu nhiên một bạn. Xác suất chọn được bạn thuận tay trái là:", ps(f), nh_ps(rng, f), 2)
def a8_lon(rng):
    k = rng.randint(2, 5); return M(f"Gieo một con xúc xắc. Xác suất mặt xuất hiện có số chấm lớn hơn {k} là:", ps(Fraction(6 - k, 6)), nh_ps(rng, Fraction(6 - k, 6)), 2)
def b8_xs(rng):
    n = rng.randint(2, 9) * 10; k = rng.randint(1, n // 5); return T(f"Một hộp có {n} thẻ, trong đó {k} thẻ ghi số 1. Lấy ngẫu nhiên một thẻ. Tính xác suất lấy được thẻ khác số 1.", f"Số thẻ khác số 1: {n - k}\nXác suất: {pf(n - k, n)}", 2)
def b8_xuc(rng):
    s = rng.randint(3, 11); c = 6 - abs(s - 7)
    return T(f"Gieo hai con xúc xắc cân đối. Tính xác suất để tổng số chấm bằng {s}.", f"Có 36 kết quả đồng khả năng; số kết quả thuận lợi: {c}\nXác suất: {pf(c, 36)}", 3)
def b8_boi(rng):
    n = rng.choice([30, 40, 50, 60]); k = rng.choice([3, 4, 5, 6])
    return T(f"Chọn ngẫu nhiên một số từ 1 đến {n}. Tính xác suất chọn được số chia hết cho {k}.", f"Số kết quả thuận lợi: {n // k}\nXác suất: {pf(n // k, n)}", 2)
def b8_dong(rng):
    return T("Tung đồng thời hai đồng xu. Liệt kê các kết quả có thể và tính xác suất để có đúng một đồng sấp.", "Kết quả: SS, SN, NS, NN. Có 2 kết quả thuận lợi (SN, NS).\nXác suất = 2/4 = 1/2.", 2)
def b8_doi(rng):
    p = rng.choice([Fraction(1, 5), Fraction(1, 4), Fraction(2, 5), Fraction(3, 8)])
    return T(f"Biết xác suất của biến cố A là {ps(p)}. Tính xác suất của biến cố \"không xảy ra A\".", f"P(không A) = 1 - {ps(p)} = {ps(1 - p)}", 1)
def b8_bc(rng):
    return T("Khi gieo một con xúc xắc, hãy nêu các kết quả thuận lợi cho biến cố \"mặt xuất hiện có số chấm là số chẵn\" và tính xác suất.", "Kết quả thuận lợi: 2, 4, 6 (3 kết quả)\nXác suất = 3/6 = 1/2.", 1)

# ============ 9. Tam giác đồng dạng ============
def a9_tile(rng):
    a, b, k = rng.randint(2, 6), rng.randint(2, 6), rng.randint(2, 4); return M(f"ΔABC ∽ ΔDEF, AB = {a} cm, DE = {a * k} cm. Tỉ số đồng dạng k = AB/DE là:", ps(Fraction(1, k)), nh_ps(rng, Fraction(1, k)), 1)
def a9_canh(rng):
    a, k = rng.randint(2, 6), rng.randint(2, 4); return nint(rng, f"ΔABC ∽ ΔDEF theo tỉ số {k} (DE/AB = {k}). Biết AB = {a} cm. Độ dài DE là (cm):", a * k, 2, (1, 2, 3), 0)
def a9_cv(rng):
    c, k = rng.randint(6, 20), rng.randint(2, 4); return nint(rng, f"ΔABC ∽ ΔA'B'C' theo tỉ số k = {k} (A'B'/AB = {k}). Chu vi ΔABC bằng {c} cm. Chu vi ΔA'B'C' là (cm):", c * k, 2, (c, 2, 5), 0)
def a9_dt(rng):
    s, k = rng.randint(2, 8), rng.randint(2, 4); return nint(rng, f"ΔABC ∽ ΔA'B'C' theo tỉ số k = {k} (A'B'/AB = {k}). Diện tích ΔABC bằng {s} cm². Diện tích ΔA'B'C' là (cm²):", s * k * k, 3, (s, 2, 5), 0)
def a9_cgc(rng):
    return M("Hai tam giác có hai cặp cạnh tương ứng tỉ lệ và góc xen giữa bằng nhau thì:", "Đồng dạng (c.g.c)", ["Bằng nhau", "Không đồng dạng", "Đồng dạng (g.g)"], 2)
def a9_ccc(rng):
    return M("Hai tam giác có ba cặp cạnh tương ứng tỉ lệ thì:", "Đồng dạng (c.c.c)", ["Bằng nhau", "Đồng dạng (g.g)", "Chưa kết luận được"], 1)
def a9_gg(rng):
    return M("Hai tam giác có hai cặp góc tương ứng bằng nhau thì:", "Đồng dạng (g.g)", ["Bằng nhau", "Đồng dạng (c.c.c)", "Chưa kết luận được"], 1)
def a9_gg2(rng):
    a, b = rng.randint(40, 80), rng.randint(40, 80); return M(f"ΔABC có A = {a}°, B = {b}°; ΔDEF có D = {a}°, E = {b}°. Hai tam giác đó:", "Đồng dạng (g.g)", ["Bằng nhau", "Không đồng dạng", "Chưa kết luận được"], 2)
def a9_huyen(rng):
    return M("Hai tam giác vuông đồng dạng với nhau nếu có:", "Một cặp góc nhọn bằng nhau", ["Một cặp cạnh góc vuông bằng nhau", "Cạnh huyền bằng nhau", "Hai cạnh góc vuông bằng nhau"], 2)
def a9_py(rng):
    a, b = rng.choice([(3, 4), (5, 12), (8, 15), (6, 8), (9, 12), (7, 24)]); return nint(rng, f"Tam giác ABC vuông tại A, AB = {a} cm, AC = {b} cm. Độ dài BC là (cm):", math.isqrt(a * a + b * b), 2, (1, 2, 3), 0)
def a9_hl(rng):
    a, b = rng.choice([(3, 4), (6, 8), (5, 12)]); c = math.isqrt(a * a + b * b); return M(f"Tam giác ABC vuông tại A, AB = {a}, AC = {b}, BC = {c}. Đường cao AH có độ dài (cm):", ps(Fraction(a * b, c)) if (a * b) % c else str(a * b // c), [ps(Fraction(a * b, c) + Fraction(1, 2)), ps(Fraction(a + b, 2)), ps(Fraction(a * b, c * 2))] if True else [], 3) if a * b % c else M(f"Tam giác ABC vuông tại A, AB = {a}, AC = {b}, BC = {c}. Đường cao AH có độ dài (cm):", a * b // c, [a * b // c + 1, a * b // c - 1 if a * b // c > 1 else 5, a * b // c + 2], 3)
def a9_ti_cao(rng):
    a, b = rng.randint(2, 6), rng.randint(2, 6)
    return M("Tỉ số hai đường cao tương ứng của hai tam giác đồng dạng bằng:", "Tỉ số đồng dạng", ["Bình phương tỉ số đồng dạng", "Tỉ số chu vi chia 2", "1"], 2)
def a9_ti_dt(rng):
    return M("Tỉ số diện tích của hai tam giác đồng dạng bằng:", "Bình phương tỉ số đồng dạng", ["Tỉ số đồng dạng", "Hai lần tỉ số đồng dạng", "Lập phương tỉ số đồng dạng"], 2)
def a9_bong(rng):
    h, b, B = rng.randint(2, 4), rng.randint(2, 6), rng.randint(10, 30)
    return nint(rng, f"Một cây cao có bóng dài {B * b} m, cùng lúc đó cột cao {h} m có bóng dài {b} m. Chiều cao cây là (m):", B * h, 3, (1, 2, 5), 0)
def b9_dd(rng):
    a, b = rng.randint(40, 80), rng.randint(40, 80)
    return T(f"Cho ΔABC có A = {a}°, B = {b}° và ΔDEF có D = {a}°, E = {b}°. Chứng minh hai tam giác đồng dạng và viết tỉ số đồng dạng nếu AB = 6 cm, DE = 9 cm.", f"Vì A = D, B = E nên ΔABC ∽ ΔDEF (g.g).\nTỉ số đồng dạng: AB/DE = 6/9 = 2/3.", 2)
def b9_cv(rng):
    c, k = rng.randint(6, 24), rng.randint(2, 4)
    return T(f"ΔABC ∽ ΔA'B'C' với tỉ số k = {k}. Chu vi ΔABC là {c} cm, diện tích {c // 2 or 1} cm². Tính chu vi và diện tích ΔA'B'C'.", f"Chu vi: {c}·{k} = {c * k} cm\nDiện tích: {c // 2 or 1}·{k}² = {(c // 2 or 1) * k * k} cm²", 2)
def b9_py(rng):
    a, b = rng.choice([(3, 4), (5, 12), (8, 15), (6, 8), (9, 12)])
    return T(f"Tam giác ABC vuông tại A, AB = {a} cm, AC = {b} cm. Tính BC và đường cao AH.", f"BC = √({a}² + {b}²) = {math.isqrt(a * a + b * b)} cm\nAH = AB·AC/BC = {a}·{b}/{math.isqrt(a * a + b * b)} = {ps(Fraction(a * b, math.isqrt(a * a + b * b)))} cm", 3)
def b9_cm(rng):
    return T("Cho tam giác ABC vuông tại A, đường cao AH. Chứng minh ΔHBA ∽ ΔABC.", "Xét ΔHBA và ΔABC: góc H = góc A = 90°; góc B chung. Vậy ΔHBA ∽ ΔABC (g.g).", 2)
def b9_bong(rng):
    h, b, B = rng.randint(2, 4), rng.randint(2, 6), rng.randint(10, 30)
    return T(f"Cùng một lúc, cột cờ có bóng dài {B * b} m, một cây cột cao {h} m có bóng dài {b} m. Tính chiều cao cột cờ.", f"Tỉ số: {B * b}/{b} = {B}\nChiều cao cột cờ: {h}·{B} = {h * B} m", 2)
def b9_ps(rng):
    return T("Nêu ba trường hợp đồng dạng của hai tam giác.", "Cạnh - cạnh - cạnh (c.c.c); cạnh - góc - cạnh (c.g.c); góc - góc (g.g).", 1)

# ============ 10. Hình khối trong thực tiễn ============
def a10_chop_v(rng):
    s, h = rng.randint(3, 10) ** 2, rng.randint(3, 12) * 3; return nint(rng, f"Hình chóp tứ giác đều có diện tích đáy {s} cm² và chiều cao {h} cm. Thể tích là (cm³):", s * h // 3, 2, (s, h, 5), 0)
def a10_chop_t(rng):
    s, h = rng.randint(2, 9) * 3, rng.randint(2, 10) * 3; return nint(rng, f"Hình chóp tam giác đều có diện tích đáy {s} cm² và chiều cao {h} cm. Thể tích là (cm³):", s * h // 3, 2, (s, h, 5), 0)
def a10_sxq(rng):
    c, d = rng.randint(2, 9) * 2, rng.randint(3, 12); return nint(rng, f"Hình chóp tứ giác đều có chu vi đáy {c * 2} cm và chiều cao mặt bên (trung đoạn) {d} cm. Diện tích xung quanh là (cm²):", c * d, 3, (d, 2, 10), 0)
def a10_dem_mat(rng):
    return M("Hình chóp tam giác đều có bao nhiêu mặt?", 4, [3, 5, 6], 1)
def a10_dem_canh(rng):
    return M("Hình chóp tam giác đều có bao nhiêu cạnh?", 6, [4, 5, 8], 1)
def a10_dem_mat2(rng):
    return M("Hình chóp tứ giác đều có bao nhiêu mặt?", 5, [4, 6, 8], 1)
def a10_dem_canh2(rng):
    return M("Hình chóp tứ giác đều có bao nhiêu cạnh?", 8, [4, 5, 6], 1)
def a10_mb(rng):
    return M("Các mặt bên của hình chóp tứ giác đều là:", "Những tam giác cân bằng nhau", ["Những hình vuông bằng nhau", "Những tam giác đều", "Những hình chữ nhật"], 2)
def a10_day(rng):
    return M("Đáy của hình chóp tứ giác đều là:", "Hình vuông", ["Hình chữ nhật", "Tam giác đều", "Hình thoi"], 1)
def a10_stp(rng):
    sd, sxq = rng.randint(5, 30), rng.randint(20, 90); return nint(rng, f"Hình chóp có diện tích xung quanh {sxq} cm² và diện tích đáy {sd} cm². Diện tích toàn phần là (cm²):", sd + sxq, 2, (sd, 2, 10), 0)
def a10_cao(rng):
    s, h = rng.randint(3, 10) ** 2, rng.randint(2, 8); return nint(rng, f"Hình chóp có thể tích {s * h} cm³ và diện tích đáy {3 * s} cm². Chiều cao là (cm):", h, 3, (1, 2, 3), 0)
def a10_the(rng):
    c = rng.randint(2, 9); return nint(rng, f"Hình chóp tứ giác đều có cạnh đáy {c} cm. Diện tích đáy là (cm²):", c * c, 1, (c, 2, 10), 0)
def b10_v(rng):
    c, h = rng.randint(3, 10), rng.randint(3, 12) * 3
    return T(f"Hình chóp tứ giác đều có cạnh đáy {c} cm, chiều cao {h} cm. Tính thể tích.", f"Diện tích đáy: {c}² = {c * c} cm²\nV = (1/3)·{c * c}·{h} = {c * c * h // 3} cm³", 2)
def b10_sxq(rng):
    c, d = rng.randint(3, 10), rng.randint(3, 12)
    return T(f"Hình chóp tứ giác đều có cạnh đáy {c} cm, trung đoạn {d} cm. Tính diện tích xung quanh và diện tích toàn phần.", f"Sxq = (1/2)·4·{c}·{d} = {2 * c * d} cm²\nStp = Sxq + Sđáy = {2 * c * d} + {c * c} = {2 * c * d + c * c} cm²", 3)
def b10_loi(rng):
    c, h = rng.randint(3, 8) * 2, rng.randint(3, 9) * 3
    return T(f"Một mái lều hình chóp tứ giác đều có đáy là hình vuông cạnh {c} m, chiều cao {h} m. Tính thể tích không khí bên trong lều.", f"V = (1/3)·{c}²·{h} = {c * c * h // 3} m³", 2)
def b10_cao(rng):
    s, h = rng.randint(3, 10) ** 2, rng.randint(2, 8)
    return T(f"Hình chóp có thể tích {s * h} cm³ và diện tích đáy {3 * s} cm². Tính chiều cao.", f"V = (1/3)Sh ⇒ h = 3V/S = 3·{s * h}/{3 * s} = {h} cm", 2)
def b10_hh(rng):
    return T("Nêu số mặt, số cạnh, số đỉnh của hình chóp tam giác đều và hình chóp tứ giác đều.", "Hình chóp tam giác đều: 4 mặt, 6 cạnh, 4 đỉnh.\nHình chóp tứ giác đều: 5 mặt, 8 cạnh, 5 đỉnh.", 1)
def b10_cm(rng):
    return T("Nêu công thức tính diện tích xung quanh, thể tích hình chóp đều và giải thích các kí hiệu.", "Sxq = p·d (p: nửa chu vi đáy, d: trung đoạn).\nV = (1/3)·S·h (S: diện tích đáy, h: chiều cao).", 1)

CHU_DE = [
    ("Chương 1: Đa thức nhiều biến", [a1_bac, a1_gt, a1_cong, a1_tru, a1_don, a1_chia_don, a1_nhan_dt, a1_nhan, a1_chia_dt, a1_dong_dang, a1_he_so, a1_bac_don], [b1_cong, b1_nhan, b1_gt, b1_chia, b1_bac, b1_loi]),
    ("Chương 2: Hằng đẳng thức đáng nhớ", [a2_tong, a2_hieu, a2_hh2, a2_lp_tong, a2_lp_hieu, a2_tong_lp, a2_hieu_lp, a2_hh2_nhan, a2_binhphuong_nt, a2_gt, a2_gt2, a2_bt], [b2_khai, b2_pt, b2_tinh, b2_x, b2_cm, b2_min]),
    ("Chương 3: Tứ giác", [a3_tong, a3_hbh, a3_hbh2, a3_thang, a3_thang_can, a3_hcn, a3_hcn2, a3_thoi, a3_vuong, a3_dau, a3_dau2, a3_dau3, a3_tc], [b3_goc, b3_hbh, b3_hcn, b3_thoi, b3_dh, b3_thang]),
    ("Chương 4: Định lí Thalès", [a4_tile, a4_thales, a4_thales2, a4_tb, a4_tb2, a4_pg, a4_dao, a4_tl_xy, a4_ten, a4_tb3, a4_gt], [b4_thales, b4_tb, b4_pg, b4_cm, b4_tl, b4_gt]),
    ("Chương 5: Dữ liệu và biểu đồ", [a5_loai, a5_tong, a5_tb, a5_pt, a5_goc, a5_cot, a5_tang, a5_chon, a5_ss, a5_tilepc, a5_dl, a5_bat_thuong], [b5_loai, b5_tb, b5_quat, b5_chon, b5_pt, b5_lap]),
    ("Chương 6: Phân thức đại số", [a6_dkxd, a6_dkxd2, a6_dkxd3, a6_rutgon, a6_rutgon2, a6_cong, a6_tru, a6_nhan, a6_chia, a6_doi, a6_bang, a6_gt], [b6_rutgon, b6_cong, b6_tru, b6_nhan, b6_dkxd, b6_gt]),
    ("Chương 7: Phương trình bậc nhất và hàm số bậc nhất", [a7_pt, a7_pt2, a7_pt3, a7_pt4, a7_ham, a7_bac, a7_hsg, a7_song, a7_cat_oy, a7_cat_ox, a7_thuoc, a7_bai], [b7_pt, b7_tich, b7_ham, b7_song, b7_loi, b7_bai]),
    ("Chương 8: Mở đầu về tính xác suất của biến cố", [a8_xs_cb, a8_kg, a8_xuc, a8_tong, a8_boi, a8_nto, a8_dong, a8_it_nhat, a8_doi, a8_xx, a8_the, a8_lon], [b8_xs, b8_xuc, b8_boi, b8_dong, b8_doi, b8_bc]),
    ("Chương 9: Tam giác đồng dạng", [a9_tile, a9_canh, a9_cv, a9_dt, a9_cgc, a9_ccc, a9_gg, a9_gg2, a9_huyen, a9_py, a9_ti_cao, a9_ti_dt, a9_bong], [b9_dd, b9_cv, b9_py, b9_cm, b9_bong, b9_ps]),
    ("Chương 10: Một số hình khối trong thực tiễn", [a10_chop_v, a10_chop_t, a10_sxq, a10_dem_mat, a10_dem_canh, a10_dem_mat2, a10_dem_canh2, a10_mb, a10_day, a10_stp, a10_cao, a10_the], [b10_v, b10_sxq, b10_loi, b10_cao, b10_hh, b10_cm]),
]
