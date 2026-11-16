from thcs import *
import math
def nz(rng, lo=-6, hi=6): return rng.choice([x for x in range(lo, hi + 1) if x])
def tt(x): return f"{x:g}".replace(".", ",")
def xs(a): return f"(x - {a})" if a >= 0 else f"(x + {-a})"

# ===== 1. Hàm số lượng giác và phương trình lượng giác =====
GT = [("0", "0", "1", "0"), ("30°", "1/2", "√3/2", "√3/3"), ("45°", "√2/2", "√2/2", "1"), ("60°", "√3/2", "1/2", "√3"), ("90°", "1", "0", "không xác định")]
def a1_sin(rng):
    g = rng.choice(GT[:4]); return M(f"sin {g[0]} bằng:", g[1], [x for x in ["1/2", "√3/2", "√2/2", "1", "0"] if x != g[1]][:3], 1)
def a1_cos(rng):
    g = rng.choice(GT[:4]); return M(f"cos {g[0]} bằng:", g[2], [x for x in ["1/2", "√3/2", "√2/2", "1", "0"] if x != g[2]][:3], 1)
def a1_tan(rng):
    g = rng.choice(GT[1:4]); return M(f"tan {g[0]} bằng:", g[3], [x for x in ["√3/3", "1", "√3", "1/2", "0"] if x != g[3]][:3], 1)
def a1_rad(rng):
    d = rng.choice([30, 45, 60, 90, 120, 135, 150, 210, 240, 270])
    def f(x):
        x = Fraction(x); n, m = x.numerator, x.denominator
        return "π" if (n, m) == (1, 1) else (f"π/{m}" if n == 1 else f"{n}π/{m}" if m > 1 else f"{n}π")
    f0 = Fraction(d, 180)
    return M(f"Đổi {d}° sang radian:", f(f0), [f(f0 * 2), f(f0 / 2), f(f0 + 1)], 1)
def a1_chuky(rng):
    return M(rng.choice(["Chu kì của hàm số y = sin x là:", "Hàm số y = sin x tuần hoàn với chu kì:"]), "2π", ["π", "π/2", "4π"], 1)
def a1_chuky2(rng):
    return M("Chu kì của hàm số y = tan x là:", "π", ["2π", "π/2", "4π"], 1)
def a1_chan(rng):
    return M("Hàm số nào là hàm số chẵn?", "y = cos x", ["y = sin x", "y = tan x", "y = cot x"], 1)
def a1_le(rng):
    return M("Hàm số nào là hàm số lẻ?", "y = sin x", ["y = cos x", "y = |x|", "y = x²"], 1)
def a1_txd(rng):
    return M("Tập xác định của hàm số y = tan x là:", "ℝ \\ {π/2 + kπ, k ∈ ℤ}", ["ℝ", "ℝ \\ {kπ, k ∈ ℤ}", "[-1; 1]"], 1)
def a1_gtri(rng):
    return M("Tập giá trị của hàm số y = sin x là:", "[-1; 1]", ["ℝ", "[0; 1]", "(-1; 1)"], 1)
def a1_pt1(rng):
    g = rng.choice([("1/2", "π/6"), ("√2/2", "π/4"), ("√3/2", "π/3")]); return M(f"Phương trình sin x = {g[0]} có nghiệm x = ... + k2π, x = π - ... + k2π với ... bằng:", g[1], [x for x in ["π/6", "π/4", "π/3", "π/2"] if x != g[1]][:3], 2)
def a1_pt2(rng):
    g = rng.choice([("1/2", "π/3"), ("√2/2", "π/4"), ("√3/2", "π/6")]); return M(f"Nghiệm của cos x = {g[0]} là x = ±... + k2π với ... bằng:", g[1], [x for x in ["π/6", "π/4", "π/3", "π/2"] if x != g[1]][:3], 2)
def a1_vn(rng):
    k = rng.choice([2, 3, 5, 7]); return M(f"Phương trình sin x = {k} có bao nhiêu nghiệm?", "Vô nghiệm", ["1 nghiệm", "2 nghiệm", "Vô số nghiệm"], 1)
def a1_tan_pt(rng):
    return M("Phương trình tan x = 1 có nghiệm là:", "x = π/4 + kπ", ["x = π/4 + k2π", "x = π/3 + kπ", "x = π/2 + kπ"], 2)
def a1_dk(rng):
    return M("Phương trình sin x = a có nghiệm khi và chỉ khi:", "|a| ≤ 1", ["a > 0", "|a| ≥ 1", "a ≥ 1"], 1)
def a1_dtri(rng):
    k = rng.randint(1, 5); return M(f"Giá trị lớn nhất của hàm số y = {k}sin x + 1 là:", k + 1, [k, k - 1, 2 * k], 2)
def a1_dtri2(rng):
    k = rng.randint(1, 5); return M(f"Giá trị nhỏ nhất của hàm số y = {k}cos x - 1 là:", -k - 1, [-k, -k + 1, k - 1], 2)
def b1_pt(rng):
    g = rng.choice([("1/2", "π/6", "π - π/6 = 5π/6"), ("√2/2", "π/4", "π - π/4 = 3π/4"), ("√3/2", "π/3", "π - π/3 = 2π/3")]); return T(f"Giải phương trình sin x = {g[0]}.", f"x = {g[1]} + k2π hoặc x = {g[2]} + k2π (k ∈ ℤ).", 2)
def b1_cos(rng):
    g = rng.choice([("1/2", "π/3"), ("√2/2", "π/4"), ("√3/2", "π/6")]); return T(f"Giải phương trình cos x = {g[0]}.", f"x = ±{g[1]} + k2π (k ∈ ℤ).", 2)
def b1_tan(rng):
    return T("Giải phương trình tan x = √3.", "x = π/3 + kπ (k ∈ ℤ).", 1)
def b1_bac2(rng):
    return T("Giải phương trình 2sin²x - 3sin x + 1 = 0.", "Đặt t = sin x (|t| ≤ 1): 2t² - 3t + 1 = 0 ⇒ t = 1 hoặc t = 1/2.\nsin x = 1 ⇒ x = π/2 + k2π; sin x = 1/2 ⇒ x = π/6 + k2π hoặc x = 5π/6 + k2π.", 3)
def b1_gtnn(rng):
    k = rng.randint(2, 6); return T(f"Tìm giá trị lớn nhất, nhỏ nhất của y = {k}cos x + 3.", f"-1 ≤ cos x ≤ 1 ⇒ {3 - k} ≤ y ≤ {3 + k}. Max = {3 + k}, Min = {3 - k}.", 2)
def b1_chuky(rng):
    return T("Tìm chu kì và tập xác định của hàm số y = tan 2x.", "Chu kì π/2; tập xác định: 2x ≠ π/2 + kπ ⇒ x ≠ π/4 + kπ/2.", 2)
def b1_cd(rng):
    return T("Nêu tính chẵn, lẻ và chu kì của sin x, cos x, tan x, cot x.", "sin, tan, cot là hàm lẻ; cos là hàm chẵn. sin, cos có chu kì 2π; tan, cot có chu kì π.", 1)

# ===== 2. Dãy số, cấp số cộng, cấp số nhân =====
def a2_un(rng):
    a, b, n = rng.randint(1, 5), rng.randint(-3, 6), rng.randint(3, 10); return nint(rng, f"Dãy số (uₙ) có uₙ = {a}n {'+' if b >= 0 else '-'} {abs(b)}. Số hạng u_{n} là:", a * n + b, 1, (1, 2, 3))
def a2_csc(rng):
    u, d, n = rng.randint(-5, 9), rng.randint(1, 6), rng.randint(5, 20); return nint(rng, f"Cấp số cộng có u₁ = {u}, công sai d = {d}. Số hạng u_{n} là:", u + (n - 1) * d, 2, (d, 2, 3))
def a2_d(rng):
    u, d = rng.randint(-5, 9), rng.randint(2, 7); return nint(rng, f"Cấp số cộng có u₁ = {u}, u₂ = {u + d}. Công sai d bằng:", d, 1, (1, 2, 3))
def a2_s(rng):
    u, d, n = rng.randint(1, 5), rng.randint(1, 5), rng.randint(5, 12); return nint(rng, f"Cấp số cộng có u₁ = {u}, d = {d}. Tổng {n} số hạng đầu là:", n * (2 * u + (n - 1) * d) // 2, 3, (3, 5, 10), 0) if (n * (2 * u + (n - 1) * d)) % 2 == 0 else None
def a2_csn(rng):
    u, q, n = rng.randint(1, 4), rng.randint(2, 3), rng.randint(3, 6); return nint(rng, f"Cấp số nhân có u₁ = {u}, công bội q = {q}. Số hạng u_{n} là:", u * q ** (n - 1), 3, (q, 2, 5), 0)
def a2_q(rng):
    u, q = rng.randint(1, 4), rng.randint(2, 5); return nint(rng, f"Cấp số nhân có u₁ = {u}, u₂ = {u * q}. Công bội q bằng:", q, 1, (1, 2), 0)
def a2_sn(rng):
    u, q, n = rng.randint(1, 3), rng.randint(2, 3), rng.randint(3, 6); return nint(rng, f"Cấp số nhân u₁ = {u}, q = {q}. Tổng {n} số hạng đầu là:", u * (q ** n - 1) // (q - 1), 3, (3, 5, 10), 0)
def a2_tang(rng):
    a = rng.randint(1, 5); return M(f"Dãy số uₙ = {a}n + 2 là dãy số:", "Tăng", ["Giảm", "Không đổi", "Không tăng, không giảm"], 1)
def a2_giam(rng):
    a = rng.randint(1, 5); return M(f"Dãy số uₙ = -{a}n + 10 là dãy số:", "Giảm", ["Tăng", "Không đổi", "Không tăng, không giảm"], 1)
def a2_bi(rng):
    return M("Dãy số uₙ = 1/n bị chặn trong khoảng nào?", "0 < uₙ ≤ 1", ["uₙ ≥ 1", "uₙ < 0", "uₙ > 1"], 2)
def a2_csc_tc(rng):
    a, c = rng.randint(1, 10), rng.randint(11, 20) ; 
    if (a + c) % 2: raise ValueError
    return nint(rng, f"Ba số {a}, x, {c} theo thứ tự lập thành cấp số cộng. Giá trị x là:", (a + c) // 2, 1, (1, 2), 0)
def a2_csn_tc(rng):
    a, k = rng.randint(1, 4), rng.randint(2, 4); return nint(rng, f"Ba số {a}, x, {a * k * k} (x > 0) theo thứ tự lập thành cấp số nhân. Giá trị x là:", a * k, 2, (1, 2), 0)
def a2_tong_nho(rng):
    n = rng.randint(5, 30); return nint(rng, f"Tổng 1 + 2 + 3 + ... + {n} bằng:", n * (n + 1) // 2, 2, (n, 10, 1), 0)
def b2_csc(rng):
    u, d, n = rng.randint(-3, 6), rng.randint(2, 5), rng.randint(8, 20); return T(f"Cấp số cộng có u₁ = {u}, d = {d}. Tính u_{n} và tổng {n} số hạng đầu.", f"u_{n} = {u} + {n - 1}·{d} = {u + (n - 1) * d}\nS = {n}·({u} + {u + (n - 1) * d})/2 = {n * (2 * u + (n - 1) * d) // 2 if (n * (2 * u + (n - 1) * d)) % 2 == 0 else tt(n * (2 * u + (n - 1) * d) / 2)}", 2)
def b2_csn(rng):
    u, q, n = rng.randint(1, 3), rng.randint(2, 3), rng.randint(4, 7); return T(f"Cấp số nhân có u₁ = {u}, q = {q}. Tính u_{n} và tổng {n} số hạng đầu.", f"u_{n} = {u}·{q}^{n - 1} = {u * q ** (n - 1)}\nS = {u}({q}^{n} - 1)/({q} - 1) = {u * (q ** n - 1) // (q - 1)}", 2)
def b2_tim(rng):
    u, d = rng.randint(1, 6), rng.randint(2, 5); return T(f"Cấp số cộng có u₃ = {u + 2 * d}, u₅ = {u + 4 * d}. Tìm u₁ và d.", f"2d = {2 * d} ⇒ d = {d}; u₁ = u₃ - 2d = {u}.", 2)
def b2_loi(rng):
    return T("Một người gửi tiết kiệm 100 triệu, lãi 6%/năm (lãi kép). Số tiền sau n năm có dạng cấp số gì? Viết công thức.", "Đây là cấp số nhân với u₁ = 106, công bội 1,06: số tiền sau n năm là 100·(1,06)ⁿ triệu đồng.", 2)
def b2_cm(rng):
    return T("Chứng minh dãy (uₙ) với uₙ = 3n + 2 là cấp số cộng.", "uₙ₊₁ - uₙ = 3(n + 1) + 2 - 3n - 2 = 3 không đổi nên là cấp số cộng với d = 3.", 2)
def b2_pt(rng):
    return T("Nêu công thức số hạng tổng quát và tổng n số hạng đầu của cấp số cộng và cấp số nhân.", "CSC: uₙ = u₁ + (n - 1)d; Sₙ = n(u₁ + uₙ)/2.\nCSN: uₙ = u₁qⁿ⁻¹; Sₙ = u₁(qⁿ - 1)/(q - 1) (q ≠ 1).", 1)

# ===== 3. Các số đặc trưng đo xu thế trung tâm (số liệu ghép nhóm) =====
def _nh(rng):
    w = rng.choice([5, 10]); a = rng.randint(0, 3) * w; k = [rng.randint(2, 12) for _ in range(4)]; return w, a, k
def a3_tong(rng):
    w, a, k = _nh(rng); return nint(rng, f"Mẫu ghép nhóm có tần số các nhóm lần lượt là {', '.join(map(str, k))}. Cỡ mẫu n là:", sum(k), 1, (1, 2, 5), 0)
def a3_rong(rng):
    w, a, k = _nh(rng); return nint(rng, f"Nhóm [{a}; {a + w}) có độ rộng là:", w, 1, (1, 2, 5), 0)
def a3_dd(rng):
    w, a, k = _nh(rng)
    return M(f"Giá trị đại diện của nhóm [{a}; {a + w}) là:", tt(a + w / 2), [tt(a), tt(a + w), tt(a + w / 2 + 1)], 1)
def a3_tb(rng):
    w, a, k = _nh(rng); n = sum(k); m = sum((a + i * w + w / 2) * k[i] for i in range(4)) / n; return M(f"Bảng ghép nhóm: [{a};{a + w}): {k[0]}; [{a + w};{a + 2 * w}): {k[1]}; [{a + 2 * w};{a + 3 * w}): {k[2]}; [{a + 3 * w};{a + 4 * w}): {k[3]}. Số trung bình (làm tròn 0,01) là:", f"{m:.2f}".replace(".", ","), [f"{m + 1:.2f}".replace(".", ","), f"{m - 1:.2f}".replace(".", ","), f"{m + w / 2:.2f}".replace(".", ",")], 3)
def a3_nhom_med(rng):
    w, a, k = _nh(rng); n = sum(k); c = 0
    for i in range(4):
        c += k[i]
        if c >= n / 2: j = i; break
    return M(f"Mẫu ghép nhóm có các nhóm [{a};{a + w}), [{a + w};{a + 2 * w}), [{a + 2 * w};{a + 3 * w}), [{a + 3 * w};{a + 4 * w}) với tần số {', '.join(map(str, k))}. Nhóm chứa trung vị là:", f"[{a + j * w}; {a + (j + 1) * w})", [f"[{a + i * w}; {a + (i + 1) * w})" for i in range(4) if i != j][:3], 3)
def a3_mot(rng):
    w, a, k = _nh(rng)
    if k.count(max(k)) > 1: raise ValueError
    j = k.index(max(k)); return M(f"Mẫu ghép nhóm có các nhóm [{a};{a + w}), [{a + w};{a + 2 * w}), [{a + 2 * w};{a + 3 * w}), [{a + 3 * w};{a + 4 * w}) với tần số {', '.join(map(str, k))}. Nhóm chứa mốt là:", f"[{a + j * w}; {a + (j + 1) * w})", [f"[{a + i * w}; {a + (i + 1) * w})" for i in range(4) if i != j][:3], 2)
def a3_tl(rng):
    w, a, k = _nh(rng); n = sum(k); f = Fraction(k[0], n); return M(f"Mẫu có tần số các nhóm {', '.join(map(str, k))}. Tần số tương đối của nhóm đầu là:", ps(f), nh_ps(rng, f), 2)
def a3_cong(rng):
    w, a, k = _nh(rng); return nint(rng, f"Tần số tích lũy của hai nhóm đầu, với tần số {', '.join(map(str, k))}, là:", k[0] + k[1], 1, (1, 2, 3), 0)
def a3_mauso(rng):
    return M("Số trung bình của mẫu số liệu ghép nhóm được tính dựa trên:", "Giá trị đại diện của mỗi nhóm", ["Giá trị lớn nhất của nhóm", "Giá trị nhỏ nhất của nhóm", "Số nhóm"], 1)
def a3_do(rng):
    return M("Trung vị của mẫu số liệu ghép nhóm là giá trị chia mẫu thành hai phần có:", "Số phần tử bằng nhau", ["Độ rộng bằng nhau", "Tổng bằng nhau", "Số nhóm bằng nhau"], 1)
def a3_ghep(rng):
    return M("Khi nào nên ghép nhóm số liệu?", "Khi số liệu có nhiều giá trị khác nhau", ["Khi số liệu ít", "Khi mọi giá trị bằng nhau", "Không bao giờ"], 1)
def a3_tuphan(rng):
    w, a, k = _nh(rng); return nint(rng, f"Mẫu có {sum(k)} số liệu. Tứ phân vị thứ hai nằm ở vị trí số liệu thứ (n/2, làm tròn) khoảng:", sum(k) // 2, 1, (1, 2, 3), 0)
def b3_tb(rng):
    w, a, k = _nh(rng); n = sum(k); m = sum((a + i * w + w / 2) * k[i] for i in range(4)) / n
    return T(f"Bảng ghép nhóm: [{a};{a + w}): {k[0]}; [{a + w};{a + 2 * w}): {k[1]}; [{a + 2 * w};{a + 3 * w}): {k[2]}; [{a + 3 * w};{a + 4 * w}): {k[3]}. Tính số trung bình.", f"n = {n}; giá trị đại diện: {', '.join(tt(a + i * w + w / 2) for i in range(4))}\nTrung bình ≈ {m:.2f}".replace(".", ","), 2)
def b3_med(rng):
    w, a, k = _nh(rng); n = sum(k); c = 0; cum = []
    for x in k: c += x; cum.append(c)
    j = next(i for i in range(4) if cum[i] >= n / 2); prev = cum[j - 1] if j else 0; me = a + j * w + (n / 2 - prev) / k[j] * w
    return T(f"Bảng ghép nhóm: [{a};{a + w}): {k[0]}; [{a + w};{a + 2 * w}): {k[1]}; [{a + 2 * w};{a + 3 * w}): {k[2]}; [{a + 3 * w};{a + 4 * w}): {k[3]}. Tính trung vị.", f"n = {n}, n/2 = {tt(n / 2)}; nhóm chứa trung vị [{a + j * w}; {a + (j + 1) * w}).\nMe = {a + j * w} + ({tt(n / 2)} - {prev})/{k[j]}·{w} ≈ {me:.2f}".replace(".", ","), 3)
def b3_mot(rng):
    w, a, k = _nh(rng)
    if k.count(max(k)) > 1: raise ValueError
    j = k.index(max(k)); k0 = k[j - 1] if j else 0; k2 = k[j + 1] if j < 3 else 0; mo = a + j * w + (k[j] - k0) / ((k[j] - k0) + (k[j] - k2)) * w
    return T(f"Bảng ghép nhóm: [{a};{a + w}): {k[0]}; [{a + w};{a + 2 * w}): {k[1]}; [{a + 2 * w};{a + 3 * w}): {k[2]}; [{a + 3 * w};{a + 4 * w}): {k[3]}. Tính mốt.", f"Nhóm chứa mốt: [{a + j * w}; {a + (j + 1) * w}).\nMo = {a + j * w} + ({k[j]} - {k0})/(({k[j]} - {k0}) + ({k[j]} - {k2}))·{w} ≈ {mo:.2f}".replace(".", ","), 3)
def b3_lap(rng):
    return T("Giải thích cách lập bảng tần số ghép nhóm từ một mẫu số liệu rời rạc.", "Chọn các nhóm cùng độ rộng dạng [a; b), phủ hết khoảng giá trị; đếm số giá trị rơi vào mỗi nhóm để có tần số.", 1)
def b3_pq(rng):
    return T("So sánh ưu, nhược điểm của số trung bình, trung vị và mốt trong mẫu ghép nhóm.", "Trung bình dùng mọi dữ liệu nhưng bị ảnh hưởng bởi giá trị cực đoan; trung vị ổn định; mốt cho giá trị thường gặp nhất.", 1)

# ===== 4. Quan hệ song song trong không gian =====
def a4_dd(rng):
    return M("Hai đường thẳng không có điểm chung và không cùng nằm trong một mặt phẳng gọi là:", "Chéo nhau", ["Song song", "Cắt nhau", "Trùng nhau"], 1)
def a4_mp(rng):
    return M("Qua ba điểm không thẳng hàng có bao nhiêu mặt phẳng?", "Duy nhất một", ["Hai", "Vô số", "Không có"], 1)
def a4_dt(rng):
    return M("Qua hai đường thẳng cắt nhau xác định:", "Một mặt phẳng duy nhất", ["Hai mặt phẳng", "Vô số mặt phẳng", "Không mặt phẳng nào"], 1)
def a4_ss1(rng):
    return M("Nếu đường thẳng a không nằm trong mặt phẳng (P) và a ∥ b với b ⊂ (P) thì:", "a ∥ (P)", ["a cắt (P)", "a ⊂ (P)", "a ⊥ (P)"], 1)
def a4_ss2(rng):
    return M("Hai mặt phẳng song song khi:", "Mặt phẳng này chứa hai đường thẳng cắt nhau cùng song song với mặt phẳng kia", ["Hai mặt phẳng có một điểm chung", "Hai mặt phẳng có một đường thẳng chung", "Có một đường thẳng nằm trong cả hai"], 1)
def a4_giaotuyen(rng):
    return M("Giao tuyến của hai mặt phẳng phân biệt có điểm chung là:", "Một đường thẳng", ["Một điểm", "Một mặt phẳng", "Rỗng"], 1)
def a4_chop(rng):
    n = rng.randint(3, 8); return nint(rng, f"Hình chóp có đáy là đa giác {n} cạnh. Số mặt của hình chóp là:", n + 1, 1, (1, 2), 0)
def a4_chop_canh(rng):
    n = rng.randint(3, 8); return nint(rng, f"Hình chóp có đáy là đa giác {n} cạnh. Số cạnh của hình chóp là:", 2 * n, 1, (1, 2), 0)
def a4_lang(rng):
    n = rng.randint(3, 8); return nint(rng, f"Hình lăng trụ có đáy là đa giác {n} cạnh. Số mặt là:", n + 2, 1, (1, 2), 0)
def a4_lang_d(rng):
    n = rng.randint(3, 8); return nint(rng, f"Hình lăng trụ có đáy là đa giác {n} cạnh. Số đỉnh là:", 2 * n, 1, (1, 2), 0)
def a4_tt(rng):
    return M("Phép chiếu song song giữ nguyên tính chất nào?", "Tính song song của hai đường thẳng", ["Độ dài đoạn thẳng", "Góc giữa hai đường", "Diện tích hình"], 1)
def a4_tl(rng):
    k = rng.choice([2, 3, 4]); a = rng.randint(2, 6); return M(f"Đường thẳng d ∥ (P). Qua phép chiếu song song lên (P) theo phương l, đoạn AB ∥ (P) có độ dài {a}. Hình chiếu A'B' có độ dài:", a, [a * k, a + k, a - 1], 2)
def a4_tales(rng):
    a, b, c = rng.randint(2, 6), rng.randint(2, 6), rng.randint(2, 6); x = Fraction(b * c, a); return M(f"Ba mặt phẳng song song chắn hai cát tuyến các đoạn tương ứng AB = {a}, BC = {b}; A'B' = {c}. Độ dài B'C' (theo Thalès) là:", ps(x), [ps(x + 1), ps(Fraction(a * c, b)), ps(Fraction(a * b, c))], 3)
def b4_giao(rng):
    return T("Cho hình chóp S.ABCD đáy là hình bình hành. Tìm giao tuyến của hai mặt phẳng (SAB) và (SCD).", "S là điểm chung. AB ∥ CD nên giao tuyến là đường thẳng đi qua S song song với AB, CD.", 3)
def b4_ss(rng):
    return T("Cho hình chóp S.ABCD, M, N lần lượt là trung điểm SA, SC. Chứng minh MN ∥ (ABCD).", "MN là đường trung bình của tam giác SAC nên MN ∥ AC. AC ⊂ (ABCD) và MN ⊄ (ABCD) ⇒ MN ∥ (ABCD).", 2)
def b4_tl(rng):
    return T("Phát biểu định lí Thalès trong không gian cho ba mặt phẳng song song.", "Ba mặt phẳng song song chắn trên hai cát tuyến bất kì những đoạn thẳng tương ứng tỉ lệ.", 1)
def b4_hlt(rng):
    return T("Nêu các tính chất của hình lăng trụ và hình hộp.", "Lăng trụ: hai đáy là hai đa giác bằng nhau nằm trong hai mặt phẳng song song, các mặt bên là hình bình hành. Hình hộp là lăng trụ có đáy là hình bình hành.", 1)
def b4_hv(rng):
    return T("Cho hình hộp ABCD.A'B'C'D'. Chứng minh (A'BD) ∥ (CB'D').", "A'B ∥ D'C và BD ∥ B'D' ⇒ hai đường cắt nhau trong (A'BD) song song với hai đường trong (CB'D') nên hai mặt phẳng song song.", 3)
def b4_mp(rng):
    return T("Nêu ba cách xác định một mặt phẳng.", "Qua ba điểm không thẳng hàng; qua một đường thẳng và một điểm không thuộc nó; qua hai đường thẳng cắt nhau (hoặc song song).", 1)

def b4_t1(rng):
    return T("Cho tứ diện ABCD, M, N lần lượt là trung điểm AB, AC. Chứng minh MN ∥ (BCD).", "MN là đường trung bình của tam giác ABC nên MN ∥ BC; BC ⊂ (BCD), MN ⊄ (BCD) ⇒ MN ∥ (BCD).", 2)
def b4_t2(rng):
    return T("Cho hình chóp S.ABCD đáy là hình bình hành. Tìm giao tuyến của (SAD) và (SBC).", "S là điểm chung; AD ∥ BC nên giao tuyến là đường thẳng qua S song song với AD, BC.", 3)
def b4_t3(rng):
    return T("Cho hình chóp S.ABCD, đáy ABCD là hình thang đáy lớn AD. Tìm giao điểm của SD với mặt phẳng (MBC), M ∈ SA.", "Gọi E = AD ∩ BC (nếu cắt); trong (SAD) nối ME cắt SD tại N; N là giao điểm cần tìm.", 3)
def b4_t4(rng):
    return T("Nêu điều kiện để hai đường thẳng trong không gian chéo nhau và cho ví dụ trên hình hộp.", "Hai đường chéo nhau khi không có điểm chung và không đồng phẳng. Ví dụ: AB và CC' trong hình hộp ABCD.A'B'C'D'.", 2)
def b4_t5(rng):
    return T("Phát biểu hai tính chất về hai mặt phẳng song song.", "Qua một điểm nằm ngoài mặt phẳng (P) có duy nhất một mặt phẳng song song với (P). Nếu mặt phẳng cắt hai mặt phẳng song song thì hai giao tuyến song song.", 1)
def b4_t6(rng):
    return T("Cho hình hộp ABCD.A'B'C'D'. Chứng minh AC ∥ A'C'.", "ACC'A' là hình bình hành (AA' ∥ CC', AA' = CC') nên AC ∥ A'C'.", 1)

# ===== 5. Giới hạn, hàm số liên tục =====
def a5_gh(rng):
    k = rng.randint(1, 6); return nint(rng, f"lim 1/n bằng ... nên lim ({k} + 1/n) bằng:", k, 1, (1, 2, 3), 0)
def a5_ps(rng):
    a, b, c, d = rng.randint(1, 5), rng.randint(1, 5), rng.randint(1, 5), rng.randint(1, 5); f = Fraction(a, c); return M(f"lim ({a}n + {b})/({c}n + {d}) bằng:", ps(f), nh_ps(rng, f) if f < 1 else [ps(Fraction(a, d)), ps(Fraction(b, d)), ps(f + 1)], 2)
def a5_gh_hs(rng):
    a, b = rng.randint(-5, 5), rng.randint(1, 5); x0 = rng.randint(-3, 4); return nint(rng, f"lim (x → {x0}) ({da([b, a])}) bằng:", b * x0 + a, 1, (1, 2, 3))
def a5_gh2(rng):
    a = rng.randint(1, 6); return nint(rng, f"lim (x → {a}) (x² - {a * a})/(x - {a}) bằng:", 2 * a, 2, (1, 2, 3), 0)
def a5_gh3(rng):
    a = rng.randint(1, 6); return nint(rng, f"lim (x → {a}) (x² - {2 * a}x + {a * a})/(x - {a}) bằng:", 0, 2, (1, 2), 0)
def a5_cap(rng):
    return M("lim (x → +∞) 1/x bằng:", 0, [1, "+∞", "-∞"], 1)
def a5_vc(rng):
    return M("lim (x → +∞) x² bằng:", "+∞", [0, 1, "-∞"], 1)
def a5_lt(rng):
    a = rng.randint(1, 5); return M(f"Hàm số f(x) = x² + {a} liên tục trên:", "ℝ", ["(0; +∞)", "ℝ \\ {0}", "[0; +∞)"], 1)
def a5_ltk(rng):
    a = rng.randint(1, 5); return M(f"Hàm số f(x) = 1/(x - {a}) liên tục trên:", f"ℝ \\ {{{a}}}", ["ℝ", f"[{a}; +∞)", f"(-∞; {a}]"], 1)
def a5_tong(rng):
    a = rng.randint(2, 6); b = Fraction(1, a); return M(f"Tổng của cấp số nhân lùi vô hạn có u₁ = 1, q = 1/{a} là:", ps(Fraction(a, a - 1)), [ps(Fraction(a - 1, a)), ps(Fraction(1, a)), ps(Fraction(a + 1, a))], 2)
def a5_vo(rng):
    return M("lim qⁿ = 0 khi:", "|q| < 1", ["|q| > 1", "q > 1", "q = 1"], 1)
def a5_dkh(rng):
    return M("Hàm số f liên tục tại x₀ khi:", "lim (x → x₀) f(x) = f(x₀)", ["lim f(x) = 0", "f(x₀) = 0", "lim f(x) = +∞"], 1)
def a5_nghiem(rng):
    return M("Nếu f liên tục trên [a; b] và f(a)·f(b) < 0 thì phương trình f(x) = 0:", "Có ít nhất một nghiệm trong (a; b)", ["Vô nghiệm", "Có đúng hai nghiệm", "Có nghiệm tại a hoặc b"], 1)
def b5_gh(rng):
    a, b, c, d = rng.randint(1, 5), rng.randint(1, 5), rng.randint(2, 5), rng.randint(1, 5); return T(f"Tính lim ({a}n² + {b}n)/({c}n² + {d}).", f"Chia tử và mẫu cho n²: lim = {ps(Fraction(a, c))}.", 2)
def b5_hs(rng):
    a = rng.randint(2, 7); return T(f"Tính lim (x → {a}) (x² - {a * a})/(x - {a}).", f"= lim (x + {a}) = {2 * a}.", 2)
def b5_lt(rng):
    a = rng.randint(1, 5); return T(f"Xét tính liên tục của hàm số f(x) = x² (x ≠ {a}), f({a}) = {a * a} tại x = {a}.", f"lim x² = {a * a} = f({a}) nên f liên tục tại x = {a}.", 1)
def b5_nghiem(rng):
    return T("Chứng minh phương trình x³ - 3x + 1 = 0 có ít nhất một nghiệm trong khoảng (0; 1).", "f(0) = 1 > 0; f(1) = -1 < 0; f liên tục ⇒ tồn tại c ∈ (0; 1): f(c) = 0.", 2)
def b5_cap(rng):
    return T("Tính tổng S = 1 + 1/2 + 1/4 + ... + 1/2ⁿ + ...", "Cấp số nhân lùi vô hạn: u₁ = 1, q = 1/2 ⇒ S = 1/(1 - 1/2) = 2.", 2)
def b5_so(rng):
    return T("Nêu các quy tắc tính giới hạn của tổng, hiệu, tích, thương.", "Nếu lim u = a, lim v = b thì lim(u ± v) = a ± b; lim(u·v) = ab; lim(u/v) = a/b (b ≠ 0).", 1)

# ===== 6. Hàm số mũ và logarit =====
def a6_luythua(rng):
    a, n = rng.randint(2, 5), rng.randint(2, 5); return nint(rng, f"Giá trị của {a}^{n} là:", a ** n, 2, (a, 2, 5), 0)
def a6_am(rng):
    a, n = rng.randint(2, 4), rng.randint(1, 3); return M(f"{a}^(-{n}) bằng:", f"1/{a ** n}", [f"-{a ** n}", f"{a ** n}", f"-1/{a ** n}"], 1)
def a6_can(rng):
    a, n = rng.randint(2, 6), rng.choice([2, 3]); return nint(rng, f"Giá trị của {a ** n}^(1/{n}) là:", a, 2, (1, 2), 0)
def a6_log(rng):
    a, n = rng.randint(2, 5), rng.randint(2, 5); return nint(rng, f"log_{a} {a ** n} bằng:", n, 1, (1, 2), 0)
def a6_log10(rng):
    n = rng.randint(1, 5); return nint(rng, f"lg {10 ** n} bằng:", n, 1, (1, 2), 0)
def a6_tich(rng):
    a, m, n = rng.randint(2, 4), rng.randint(1, 4), rng.randint(1, 4); return nint(rng, f"log_{a} {a ** m} + log_{a} {a ** n} bằng:", m + n, 1, (1, 2), 0)
def a6_thuong(rng):
    a, m, n = rng.randint(2, 4), rng.randint(3, 6), rng.randint(1, 2); return nint(rng, f"log_{a} {a ** m} - log_{a} {a ** n} bằng:", m - n, 1, (1, 2), 0)
def a6_pt(rng):
    a, n = rng.randint(2, 5), rng.randint(1, 5); return nint(rng, f"Nghiệm của phương trình {a}^x = {a ** n} là:", n, 1, (1, 2), 0)
def a6_ptlog(rng):
    a, n = rng.randint(2, 5), rng.randint(1, 4); return nint(rng, f"Nghiệm của phương trình log_{a} x = {n} là:", a ** n, 2, (a, 2, 5), 0)
def a6_dongbien(rng):
    a = rng.choice([2, 3, 5, 10]); return M(f"Hàm số y = {a}^x là hàm:", "Đồng biến trên ℝ", ["Nghịch biến trên ℝ", "Chẵn", "Không đơn điệu"], 1)
def a6_nghich(rng):
    a = rng.choice([2, 3, 4, 5]); return M(f"Hàm số y = (1/{a})^x là hàm:", "Nghịch biến trên ℝ", ["Đồng biến trên ℝ", "Chẵn", "Hàm hằng"], 1)
def a6_dk(rng):
    return M("Điều kiện xác định của log_a x (a > 0, a ≠ 1) là:", "x > 0", ["x ≥ 0", "x ≠ 0", "x < 0"], 1)
def a6_txd(rng):
    return M("Tập giá trị của hàm số y = aˣ (a > 0, a ≠ 1) là:", "(0; +∞)", ["ℝ", "[0; +∞)", "(1; +∞)"], 1)
def a6_bpt(rng):
    n = rng.randint(2, 6); return nint(rng, f"Số nghiệm nguyên dương của bất phương trình 2^x < {2 ** n} là:", n - 1, 2, (1, 2), 0)
def b6_pt(rng):
    a, n = rng.randint(2, 4), rng.randint(2, 5); return T(f"Giải phương trình {a}^(x + 1) = {a ** n}.", f"x + 1 = {n} ⇒ x = {n - 1}.", 1)
def b6_log(rng):
    a, m, n = rng.randint(2, 4), rng.randint(2, 4), rng.randint(1, 3); return T(f"Tính log_{a} {a ** m} + log_{a} {a ** n} - log_{a} {a}.", f"= {m} + {n} - 1 = {m + n - 1}", 1)
def b6_ptlog(rng):
    a = rng.randint(2, 4); n = rng.randint(2, 4); return T(f"Giải phương trình log_{a}(x - 1) = {n}.", f"Điều kiện x > 1; x - 1 = {a ** n} ⇒ x = {a ** n + 1}.", 2)
def b6_bpt(rng):
    n = rng.randint(2, 6); return T(f"Giải bất phương trình 2^x > {2 ** n}.", f"Cơ số 2 > 1 nên x > {n}.", 1)
def b6_loi(rng):
    return T("Dân số một thành phố là 1 triệu người, tăng 2%/năm. Sau n năm dân số là? Tìm n để dân số vượt 1,5 triệu.", "P(n) = 1,02ⁿ triệu. 1,02ⁿ > 1,5 ⇒ n > log₁,₀₂ 1,5 ≈ 20,5 nên n ≥ 21 năm.", 3)
def b6_tc(rng):
    return T("Nêu các tính chất của lôgarit.", "log_a(MN) = log_a M + log_a N; log_a(M/N) = log_a M - log_a N; log_a Mᵏ = k·log_a M; đổi cơ số: log_a b = log_c b/log_c a.", 1)

# ===== 7. Đạo hàm =====
def a7_xn(rng):
    n = rng.randint(2, 8); return M(f"Đạo hàm của y = x^{n} là:", f"{n}x^{n - 1}" if n > 2 else "2x", [f"x^{n - 1}", f"{n}x^{n}", f"{n - 1}x^{n - 1}"], 1)
def a7_hs(rng):
    a, b, c = nz(rng, -4, 4), nz(rng, -5, 5), rng.randint(-5, 5); return M(f"Đạo hàm của y = {da([a, b, c])} là:", da([2 * a, b]), [da([a, b]), da([2 * a, b, c]), da([a, 2 * b])], 1)
def a7_diem(rng):
    a, b, x = nz(rng, -3, 3), rng.randint(-4, 4), rng.randint(-3, 4); return nint(rng, f"Cho f(x) = {da([a, b, 1])}. f'({x}) bằng:", 2 * a * x + b, 1, (1, 2, 3))
def a7_sin(rng):
    return M("Đạo hàm của y = sin x là:", "cos x", ["-cos x", "-sin x", "tan x"], 1)
def a7_cos(rng):
    return M("Đạo hàm của y = cos x là:", "-sin x", ["sin x", "cos x", "-cos x"], 1)
def a7_ex(rng):
    return M("Đạo hàm của y = eˣ là:", "eˣ", ["xeˣ⁻¹", "eˣ/x", "1/x"], 1)
def a7_ln(rng):
    return M("Đạo hàm của y = ln x là:", "1/x", ["x", "eˣ", "ln x"], 1)
def a7_tich(rng):
    a = rng.randint(2, 6); return M(f"Đạo hàm của y = x·eˣ là:", "(x + 1)eˣ", ["eˣ", "xeˣ", "(x - 1)eˣ"], 2)
def a7_thuong(rng):
    return M("Đạo hàm của y = 1/x là:", "-1/x²", ["1/x²", "-1/x", "ln x"], 1)
def a7_can(rng):
    return M("Đạo hàm của y = √x (x > 0) là:", "1/(2√x)", ["1/√x", "2√x", "-1/(2√x)"], 1)
def a7_tt(rng):
    a, x = rng.randint(1, 3), rng.randint(1, 3); k = 2 * a * x; y = a * x * x; return M(f"Hệ số góc của tiếp tuyến của y = {a}x² tại điểm có hoành độ {x} là:", k, [k + 1, k - 1, y], 2)
def a7_tt_pt(rng):
    x = rng.randint(1, 3); k = 2 * x; y = x * x; b = y - k * x; return M(f"Tiếp tuyến của y = x² tại điểm có hoành độ {x} có phương trình:", f"y = {k}x {'+' if b >= 0 else '-'} {abs(b)}" if b else f"y = {k}x", [f"y = {k + 1}x {'+' if b >= 0 else '-'} {abs(b)}", f"y = {k}x {'-' if b >= 0 else '+'} {abs(b)}" if b else f"y = {k + 1}x", f"y = {y}x"], 3)
def a7_chuoi(rng):
    n = rng.randint(3, 6); return M(f"Đạo hàm của y = (x + 1)^{n} là:", f"{n}(x + 1)^{n - 1}", [f"(x + 1)^{n - 1}", f"{n}(x + 1)^{n}", f"{n}x^{n - 1}"], 2)
def a7_vt(rng):
    a, b = rng.randint(2, 5), rng.randint(1, 5); t = rng.randint(1, 5); return nint(rng, f"Một vật chuyển động theo s(t) = {a}t² + {b}t. Vận tốc tại t = {t} là:", 2 * a * t + b, 2, (1, 2, 3), 0)
def b7_dh(rng):
    a, b, c = nz(rng, -4, 4), nz(rng, -5, 5), rng.randint(-5, 5); return T(f"Tính đạo hàm của y = {da([a, b, c, 1])}.", f"y' = {da([3 * a, 2 * b, c])}", 2)
def b7_tt(rng):
    x = rng.randint(1, 3); return T(f"Viết phương trình tiếp tuyến của đồ thị y = x³ tại điểm có hoành độ {x}.", f"y' = 3x² ⇒ hệ số góc {3 * x * x}; y({x}) = {x ** 3}.\nTiếp tuyến: y = {3 * x * x}(x - {x}) + {x ** 3}.", 3)
def b7_tich(rng):
    return T("Tính đạo hàm của y = x²·sin x.", "y' = 2x·sin x + x²·cos x.", 2)
def b7_thuong(rng):
    return T("Tính đạo hàm của y = (x + 1)/(x - 1).", "y' = [(x - 1) - (x + 1)]/(x - 1)² = -2/(x - 1)².", 2)
def b7_vt(rng):
    a = rng.randint(2, 6); return T(f"Vật chuyển động theo s(t) = t³ - {3 * a}t² + 5 (t: giây, s: mét). Tính vận tốc và gia tốc tại t = {a} s.", f"v = s' = 3t² - {6 * a}t ⇒ v({a}) = {3 * a * a - 6 * a * a} m/s\na = v' = 6t - {6 * a} ⇒ a({a}) = 0 m/s².", 3)
def b7_ct(rng):
    return T("Nêu công thức đạo hàm của tổng, tích, thương và hàm hợp.", "(u ± v)' = u' ± v'; (uv)' = u'v + uv'; (u/v)' = (u'v - uv')/v²; [f(u)]' = f'(u)·u'.", 1)

# ===== 8. Quan hệ vuông góc trong không gian =====
def a8_vg(rng):
    return M("Đường thẳng a vuông góc với mặt phẳng (P) khi:", "a vuông góc với hai đường thẳng cắt nhau nằm trong (P)", ["a song song với (P)", "a vuông góc với một đường nằm trong (P)", "a cắt (P)"], 1)
def a8_goc(rng):
    return M("Góc giữa hai đường thẳng a, b trong không gian có số đo nằm trong khoảng:", "[0°; 90°]", ["[0°; 180°]", "(90°; 180°)", "[0°; 360°)"], 1)
def a8_chop(rng):
    a = rng.randint(2, 9); return M(f"Hình chóp S.ABCD đáy là hình vuông cạnh {a}, SA ⊥ (ABCD), SA = {a}. Góc giữa SA và (ABCD) bằng:", "90°", ["45°", "60°", "30°"], 1)
def a8_goc2(rng):
    return M("Hình chóp S.ABCD có SA ⊥ (ABCD) và SA = AB (đáy hình vuông). Góc giữa SB và (ABCD) bằng:", "45°", ["30°", "60°", "90°"], 1)
def a8_dai(rng):
    a = rng.randint(2, 9); return M(f"Hình lập phương cạnh {a}. Độ dài đường chéo là:", f"{a}√3", [f"{a}√2", f"{3 * a}", f"{a * a}"], 1)
def a8_chephon(rng):
    a = rng.randint(2, 9); return M(f"Hình lập phương cạnh {a}. Độ dài đường chéo của một mặt là:", f"{a}√2", [f"{a}√3", f"{2 * a}", f"{a}"], 1)
def a8_dtc(rng):
    a, b, c = rng.choice([(1, 2, 2), (2, 3, 6), (3, 4, 12), (2, 6, 9), (4, 4, 7)]); d = math.isqrt(a * a + b * b + c * c); return nint(rng, f"Hình hộp chữ nhật có ba kích thước {a}, {b}, {c}. Độ dài đường chéo là:", d, 2, (1, 2, 3), 0)
def a8_vgmp(rng):
    return M("Hai mặt phẳng vuông góc khi:", "Mặt phẳng này chứa một đường thẳng vuông góc với mặt phẳng kia", ["Hai mặt phẳng song song", "Chúng có một điểm chung", "Góc giữa chúng bằng 45°"], 1)
def a8_vt(rng):
    a, h = rng.randint(2, 8), rng.randint(3, 10); return nint(rng, f"Thể tích hình hộp chữ nhật đáy hình vuông cạnh {a}, chiều cao {h} là:", a * a * h, 2, (a, h, 10), 0)
def a8_chop_v(rng):
    a, h = rng.randint(2, 8), rng.randint(3, 4) * 3; return nint(rng, f"Thể tích hình chóp có diện tích đáy {a * a} và chiều cao {h} là:", a * a * h // 3, 2, (a, 3, 10), 0)
def a8_lt(rng):
    a, h = rng.randint(2, 8), rng.randint(3, 10); return nint(rng, f"Thể tích lăng trụ có diện tích đáy {a * 2} và chiều cao {h} là:", a * 2 * h, 2, (a, h, 10), 0)
def a8_kc(rng):
    return M("Khoảng cách từ một điểm đến mặt phẳng là:", "Độ dài đoạn vuông góc hạ từ điểm đó xuống mặt phẳng", ["Độ dài đoạn nối đến một điểm bất kì", "Độ dài đường chéo", "Bán kính mặt cầu"], 1)
def b8_chop(rng):
    a = rng.randint(2, 9); return T(f"Hình chóp S.ABCD đáy là hình vuông cạnh {a}, SA ⊥ (ABCD), SA = {a}. Tính thể tích chóp và góc giữa SC và đáy.", f"V = (1/3)·{a}²·{a} = {ps(Fraction(a ** 3, 3))}\nAC = {a}√2; tan(SC, ABCD) = SA/AC = 1/√2 ⇒ góc ≈ 35,26°", 3)
def b8_vg(rng):
    return T("Cho hình chóp S.ABC có SA ⊥ (ABC), tam giác ABC vuông tại B. Chứng minh BC ⊥ (SAB).", "BC ⊥ AB (gt), BC ⊥ SA (SA ⊥ (ABC)) ⇒ BC ⊥ (SAB).", 2)
def b8_hop(rng):
    a, b, c = rng.randint(2, 7), rng.randint(2, 7), rng.randint(2, 7); return T(f"Hình hộp chữ nhật có ba kích thước {a}, {b}, {c}. Tính thể tích và độ dài đường chéo.", f"V = {a}·{b}·{c} = {a * b * c}\nd = √({a * a} + {b * b} + {c * c}) = √{a * a + b * b + c * c}", 2)
def b8_kc(rng):
    a = rng.randint(2, 8); return T(f"Hình lập phương ABCD.A'B'C'D' cạnh {a}. Tính khoảng cách từ A đến mặt phẳng (A'BD)? (nêu hướng).", "Dùng thể tích: d(A, (A'BD)) = 3V/S với V là thể tích tứ diện A.A'BD.", 3)
def b8_phat(rng):
    return T("Phát biểu định lí ba đường vuông góc.", "Cho a ⊂ (P), b là hình chiếu vuông góc của đường thẳng d lên (P). Khi đó a ⊥ d ⇔ a ⊥ b.", 1)
def b8_goc(rng):
    return T("Nêu cách xác định góc giữa đường thẳng và mặt phẳng, giữa hai mặt phẳng.", "Góc giữa đường thẳng và mặt phẳng là góc giữa đường thẳng và hình chiếu của nó lên mặt phẳng. Góc giữa hai mặt phẳng là góc giữa hai đường thẳng lần lượt vuông góc với giao tuyến trong mỗi mặt phẳng.", 1)

# ===== 9. Xác suất =====
def a9_hop(rng):
    n, m = rng.randint(4, 8), rng.randint(3, 6); f = Fraction(math.comb(n, 2), math.comb(n + m, 2)); return M(f"Hộp có {n} bi đỏ và {m} bi xanh. Lấy 2 viên. Xác suất cả hai đỏ là:", ps(f), nh_ps(rng, f), 3)
def a9_hop2(rng):
    n, m = rng.randint(4, 8), rng.randint(3, 6); f = Fraction(n * m, math.comb(n + m, 2)); return M(f"Hộp có {n} bi đỏ và {m} bi xanh. Lấy 2 viên. Xác suất được 1 đỏ 1 xanh là:", ps(f), nh_ps(rng, f), 3)
def a9_giao(rng):
    a, b = Fraction(1, rng.randint(2, 4)), Fraction(1, rng.randint(2, 5)); return M(f"A, B độc lập, P(A) = {ps(a)}, P(B) = {ps(b)}. P(A ∩ B) là:", ps(a * b), [ps(a + b) if a + b < 1 else ps(a), ps(abs(a - b)) if a != b else ps(a * 2), ps(a / b) if a / b < 1 else ps(b / a)], 2)
def a9_hop_(rng):
    a, b = Fraction(1, rng.randint(3, 5)), Fraction(1, rng.randint(6, 9)); return M(f"A, B xung khắc, P(A) = {ps(a)}, P(B) = {ps(b)}. P(A ∪ B) là:", ps(a + b), [ps(a * b), ps(abs(a - b)), ps(a)], 2)
def a9_doi(rng):
    p = Fraction(rng.randint(1, 4), rng.randint(5, 9)); return M(f"P(A) = {ps(p)}. P(biến cố đối của A) là:", ps(1 - p), nh_ps(rng, 1 - p), 1)
def a9_hop2_cong(rng):
    a, b, c = Fraction(1, 2), Fraction(1, 3), Fraction(1, 6); return M("P(A) = 1/2, P(B) = 1/3, P(A ∩ B) = 1/6. P(A ∪ B) bằng:", "2/3", ["5/6", "1/6", "1/2"], 2)
def a9_dk(rng):
    a, b = rng.randint(2, 5), rng.randint(2, 5); return M(f"Công thức xác suất có điều kiện P(A|B) bằng (P(B) > 0):", "P(A ∩ B)/P(B)", ["P(A)·P(B)", "P(A) + P(B)", "P(B)/P(A)"], 1)
def a9_dg(rng):
    n = rng.randint(6, 12); return nint(rng, f"Số cách chọn 2 học sinh từ {n} học sinh là:", n * (n - 1) // 2, 3, (1, 2, n), 0)
def a9_xuc(rng):
    s = rng.randint(2, 12); c = 6 - abs(s - 7); f = Fraction(c, 36); return M(f"Gieo hai con xúc xắc. Xác suất tổng hai mặt bằng {s} là:", ps(f), nh_ps(rng, f), 2)
def a9_ba(rng):
    return M("Tung ba đồng xu. Xác suất cả ba cùng sấp là:", "1/8", ["1/3", "1/4", "3/8"], 2)
def a9_chiahet(rng):
    n, k = rng.randint(20, 60), rng.choice([3, 4, 5]); f = Fraction(n // k, n); return M(f"Chọn ngẫu nhiên một số từ 1 đến {n}. Xác suất số đó chia hết cho {k} là:", ps(f), nh_ps(rng, f), 2)
def a9_bayes(rng):
    return M("Hai biến cố A, B độc lập khi:", "P(A ∩ B) = P(A)·P(B)", ["P(A ∩ B) = 0", "P(A ∪ B) = 1", "P(A) = P(B)"], 1)
def b9_hop(rng):
    n, m = rng.randint(4, 7), rng.randint(3, 6); f = Fraction(math.comb(n, 3), math.comb(n + m, 3)); return T(f"Hộp có {n} bi đỏ, {m} bi xanh. Lấy ngẫu nhiên 3 viên. Tính xác suất cả 3 viên đỏ.", f"|Ω| = C({n + m},3) = {math.comb(n + m, 3)}; thuận lợi C({n},3) = {math.comb(n, 3)}. P = {ps(f)}", 3)
def b9_cong(rng):
    return T("Tung hai con xúc xắc. Tính xác suất để tổng số chấm là số chia hết cho 5.", "Tổng 5: 4 cách; tổng 10: 3 cách ⇒ 7 cách. P = 7/36.", 2)
def b9_nhan(rng):
    return T("Hai xạ thủ bắn độc lập, xác suất trúng của mỗi người lần lượt 0,8 và 0,7. Tính xác suất cả hai cùng trúng.", "P = 0,8·0,7 = 0,56.", 1)
def b9_it(rng):
    return T("Hai xạ thủ bắn độc lập, xác suất trúng của mỗi người 0,8 và 0,7. Tính xác suất có ít nhất một người trúng.", "P = 1 - (1 - 0,8)(1 - 0,7) = 1 - 0,06 = 0,94.", 2)
def b9_dk(rng):
    return T("Một lớp có 25 học sinh, 15 em thích Toán, 10 em thích Văn, 5 em thích cả hai. Chọn một em ngẫu nhiên. Tính xác suất em đó thích Toán hoặc Văn.", "P = (15 + 10 - 5)/25 = 20/25 = 4/5.", 2)
def b9_ct(rng):
    return T("Nêu quy tắc cộng và quy tắc nhân xác suất.", "Cộng: P(A ∪ B) = P(A) + P(B) - P(A ∩ B). Nhân (độc lập): P(A ∩ B) = P(A)·P(B).", 1)

CHU_DE = [
    ("Chương 1: Hàm số lượng giác và phương trình lượng giác", [a1_sin, a1_cos, a1_tan, a1_rad, a1_chuky, a1_chuky2, a1_chan, a1_le, a1_txd, a1_gtri, a1_pt1, a1_pt2, a1_vn, a1_tan_pt, a1_dk, a1_dtri, a1_dtri2], [b1_pt, b1_cos, b1_tan, b1_bac2, b1_gtnn, b1_chuky, b1_cd]),
    ("Chương 2: Dãy số, cấp số cộng và cấp số nhân", [a2_un, a2_csc, a2_d, a2_s, a2_csn, a2_q, a2_sn, a2_tang, a2_giam, a2_bi, a2_csc_tc, a2_csn_tc, a2_tong_nho], [b2_csc, b2_csn, b2_tim, b2_loi, b2_cm, b2_pt]),
    ("Chương 3: Các số đặc trưng đo xu thế trung tâm của mẫu số liệu ghép nhóm", [a3_tong, a3_rong, a3_dd, a3_tb, a3_nhom_med, a3_mot, a3_tl, a3_cong, a3_mauso, a3_do, a3_ghep, a3_tuphan], [b3_tb, b3_med, b3_mot, b3_lap, b3_pq]),
    ("Chương 4: Quan hệ song song trong không gian", [a4_dd, a4_mp, a4_dt, a4_ss1, a4_ss2, a4_giaotuyen, a4_chop, a4_chop_canh, a4_lang, a4_lang_d, a4_tt, a4_tl, a4_tales], [b4_giao, b4_ss, b4_tl, b4_hlt, b4_hv, b4_mp, b4_t1, b4_t2, b4_t3, b4_t4, b4_t5, b4_t6]),
    ("Chương 5: Giới hạn, hàm số liên tục", [a5_gh, a5_ps, a5_gh_hs, a5_gh2, a5_gh3, a5_cap, a5_vc, a5_lt, a5_ltk, a5_tong, a5_vo, a5_dkh, a5_nghiem], [b5_gh, b5_hs, b5_lt, b5_nghiem, b5_cap, b5_so]),
    ("Chương 6: Hàm số mũ và hàm số lôgarit", [a6_luythua, a6_am, a6_can, a6_log, a6_log10, a6_tich, a6_thuong, a6_pt, a6_ptlog, a6_dongbien, a6_nghich, a6_dk, a6_txd, a6_bpt], [b6_pt, b6_log, b6_ptlog, b6_bpt, b6_loi, b6_tc]),
    ("Chương 7: Đạo hàm", [a7_xn, a7_hs, a7_diem, a7_sin, a7_cos, a7_ex, a7_ln, a7_tich, a7_thuong, a7_can, a7_tt, a7_tt_pt, a7_chuoi, a7_vt], [b7_dh, b7_tt, b7_tich, b7_thuong, b7_vt, b7_ct]),
    ("Chương 8: Quan hệ vuông góc trong không gian", [a8_vg, a8_goc, a8_chop, a8_goc2, a8_dai, a8_chephon, a8_dtc, a8_vgmp, a8_vt, a8_chop_v, a8_lt, a8_kc], [b8_chop, b8_vg, b8_hop, b8_kc, b8_phat, b8_goc]),
    ("Chương 9: Xác suất", [a9_hop, a9_hop2, a9_giao, a9_hop_, a9_doi, a9_hop2_cong, a9_dk, a9_dg, a9_xuc, a9_ba, a9_chiahet, a9_bayes], [b9_hop, b9_cong, b9_nhan, b9_it, b9_dk, b9_ct]),
]
def _w(f):
    def g(rng):
        r = f(rng)
        if r is None: raise ValueError
        return r
    g.__name__ = f.__name__
    return g
CHU_DE = [(t, [_w(f) for f in m], [_w(f) for f in l]) for t, m, l in CHU_DE]
