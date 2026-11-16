from thcs import *
import math

# ============ 1. Số hữu tỉ ============
def a1_cong(rng):
    a, b = qr(rng), qr(rng); return M(f"{ps(a)} + ({ps(b)}) = ?", ps(a + b), nq(rng, a + b), 1)
def a1_tru(rng):
    a, b = qr(rng), qr(rng); return M(f"{ps(a)} - ({ps(b)}) = ?", ps(a - b), nq(rng, a - b), 2) if a - b != 0 else (_ for _ in ()).throw(ValueError)
def a1_nhan(rng):
    a, b = qr(rng), qr(rng); return M(f"({ps(a)}) · ({ps(b)}) = ?", ps(a * b), nq(rng, a * b), 2)
def a1_chia(rng):
    a, b = qr(rng), qr(rng); return M(f"({ps(a)}) : ({ps(b)}) = ?", ps(a / b), nq(rng, a / b), 2)
def a1_ss(rng):
    a, b = qr(rng, 12), qr(rng, 12)
    if a == b: raise ValueError
    d = kq_dau(a, b); return M(f"Chọn dấu thích hợp: {ps(a)} ... {ps(b)}", d, sai_dau(d), 2)
def a1_luythua(rng):
    a = qr(rng, 5); n = rng.randint(2, 4); r = a ** n
    return M(f"Giá trị của ({ps(a)}){str(n).translate(SUP)} là:", ps(r), nq(rng, r), 2)
def a1_doi(rng):
    a = qr(rng, 12); return M(f"Số đối của {ps(a)} là:", ps(-a), [ps(a), ps(1 / a), ps(-1 / a)], 1)
def a1_gttd(rng):
    a = qr(rng, 12); return M(f"Giá trị tuyệt đối của {ps(a)} là:", ps(abs(a)), [ps(-abs(a)), ps(1 / abs(a)), ps(abs(a) + 1)], 1)
def a1_x(rng):
    a, b = qr(rng, 8), qr(rng, 8); return M(f"Tìm x biết x + ({ps(a)}) = {ps(a + b)}. Giá trị của x là:", ps(b), nq(rng, b), 2)
def a1_x2(rng):
    a, b = qr(rng, 8), qr(rng, 8); return M(f"Tìm x biết x · ({ps(a)}) = {ps(a * b)}. Giá trị của x là:", ps(b), nq(rng, b), 2)
def a1_tp(rng):
    n = rng.choice([1, 2, 3, 4, 6, 7, 9, 11, 13, 17, 19]); k = rng.choice([4, 5, 8, 10, 20, 25]); f = Fraction(n, k)
    if f.denominator == 1: raise ValueError
    return M(f"Số thập phân {tp(D(f.numerator) / D(f.denominator))} viết dưới dạng phân số tối giản là:", ps(f), nq(rng, f), 2) if (D(f.numerator) / D(f.denominator)).as_tuple().exponent >= -4 else (_ for _ in ()).throw(ValueError)
def a1_bt(rng):
    a, b, c = qr(rng, 6), qr(rng, 6), qr(rng, 6); r = a + b * c
    return M(f"Giá trị của biểu thức {ps(a)} + ({ps(b)}) · ({ps(c)}) là:", ps(r), nq(rng, r), 3)

def b1_tinh(rng):
    a, b, c = qr(rng, 6), qr(rng, 6), qr(rng, 6)
    return T(f"Tính: ({ps(a)}) + ({ps(b)}) · ({ps(c)}).", f"({ps(b)}) · ({ps(c)}) = {ps(b * c)}\n({ps(a)}) + ({ps(b * c)}) = {ps(a + b * c)}", 2)
def b1_x(rng):
    a, b, c = qr(rng, 6), qr(rng, 6), qr(rng, 6)
    return T(f"Tìm x, biết x · ({ps(a)}) + ({ps(b)}) = {ps(c * a + b)}.", f"x · ({ps(a)}) = {ps(c * a)}\nx = {ps(c)}", 2)
def b1_ss(rng):
    ds = []
    while len(ds) < 4:
        f = qr(rng, 10)
        if f not in ds: ds.append(f)
    return T("Sắp xếp các số hữu tỉ sau theo thứ tự tăng dần: " + ", ".join(ps(x) for x in ds) + ".", ", ".join(ps(x) for x in sorted(ds)), 2)
def b1_lt(rng):
    a = qr(rng, 5); n = rng.randint(2, 3); m = rng.randint(1, 3)
    return T(f"Tính: ({ps(a)}){str(n).translate(SUP)} · ({ps(a)}){str(m).translate(SUP)}.", f"= ({ps(a)}){str(n + m).translate(SUP)} = {ps(a ** (n + m))}", 3)
def b1_nhanh(rng):
    a, b, c = qr(rng, 6), qr(rng, 6), rng.randint(2, 9)
    return T(f"Tính hợp lí: ({ps(a)}) · {c} + ({ps(a)}) · ({-c + 1}).", f"= ({ps(a)}) · ({c} + ({-c + 1})) = ({ps(a)}) · 1 = {ps(a)}", 3)
def b1_loi(rng):
    n = rng.randint(2, 6) * 6; a = Fraction(1, 2); b = Fraction(1, 3)
    return T(f"Một người đi từ A đến B dài {n} km. Chặng đầu đi được 1/2 quãng đường, chặng hai đi được 1/3 quãng đường. Hỏi còn lại bao nhiêu km?", f"Đã đi: {n} · (1/2 + 1/3) = {n} · 5/6 = {n * 5 // 6} km\nCòn lại: {n} - {n * 5 // 6} = {n - n * 5 // 6} km", 2)

# ============ 2. Số thực ============
def a2_cbh(rng):
    k = rng.randint(2, 20); return nint(rng, f"Căn bậc hai số học của {k * k} là:", k, 1, (1, 2, 3), 0)
def a2_cbh2(rng):
    k = rng.randint(2, 15); return M(f"Có bao nhiêu số thực x thỏa mãn x² = {k * k}?", 2, [0, 1, 4], 2)
def a2_bt(rng):
    a, b = rng.randint(2, 12), rng.randint(2, 12); d = a + b
    return nint(rng, f"Giá trị của √{a * a} + √{b * b} là:", d, 1, (1, 2, 3), 0)
def a2_bt2(rng):
    a, b = rng.randint(3, 15), rng.randint(2, 9); d = a * a - b * b
    return nint(rng, f"Giá trị của {a}² - ({b})² là:", d, 2, (1, 2, 10), 0)
def a2_vt(rng):
    ds = [x for x in range(2, 40) if math.isqrt(x) ** 2 != x]; k = rng.choice(ds)
    return M("Số nào dưới đây là số vô tỉ?", f"√{k}", [f"√{m * m}" for m in rng.sample(range(2, 12), 3)], 1)
def a2_hh(rng):
    k = rng.randint(2, 12)
    return M("Số nào dưới đây là số hữu tỉ?", f"√{k * k}", [f"√{m}" for m in rng.sample([x for x in range(2, 40) if math.isqrt(x) ** 2 != x], 3)], 1)
def a2_ss(rng):
    a, b = rng.randint(2, 40), rng.randint(2, 40)
    if a == b: raise ValueError
    d = kq_dau(a, b); return M(f"Chọn dấu thích hợp: √{a} ... √{b}", d, sai_dau(d), 1)
def a2_ss2(rng):
    k = rng.randint(2, 12); a = rng.randint(k * k + 1, (k + 1) ** 2 - 1) if (k + 1) ** 2 - k * k > 2 else None
    if a is None: raise ValueError
    return M(f"Số √{a} nằm giữa hai số nguyên liên tiếp nào?", f"{k} và {k + 1}", [f"{k - 1} và {k}", f"{k + 1} và {k + 2}", f"{k + 2} và {k + 3}"], 2)
def a2_x(rng):
    k = rng.randint(2, 12); return M(f"Tìm x biết x² = {k * k}. Giá trị của x là:", f"x = {k} hoặc x = -{k}", [f"x = {k}", f"x = -{k}", f"x = {k * k}"], 2)
def a2_gttd(rng):
    a = rng.randint(2, 12); return M(f"Tìm x biết |x| = {a}. Các giá trị của x là:", f"x = {a} hoặc x = -{a}", [f"x = {a}", f"x = -{a}", f"x = {a * a}"], 1)
def a2_lt(rng):
    x = rd(rng, 1, 30, 3); k = rng.choice([1, 2]); d = tpf(x, k)
    return M(f"Làm tròn số {tp(x)} đến hàng {'phần mười' if k == 1 else 'phần trăm'} ta được:", d, chon3(rng, [tpf(x, 0), tpf(x, 3 - k if k == 1 else 1), tpf(D(d.replace(',', '.')) + D(1).scaleb(-k), k), tpf(D(d.replace(',', '.')) - D(1).scaleb(-k), k)], d), 2)
def a2_cbh_tp(rng):
    k = rng.randint(2, 15); return M(f"√{tp(D(k * k) / 100)} bằng:", tp(D(k) / 10), [tp(D(k)), tp(D(k) / 100), tp(D(k * k) / 10)], 2)
def a2_taphop(rng):
    return M(rng.choice(["Kí hiệu ℝ là tập hợp nào?", "Tập hợp ℝ gồm:"]), "Các số thực (số hữu tỉ và số vô tỉ)", ["Chỉ các số hữu tỉ", "Chỉ các số tự nhiên", "Chỉ các số vô tỉ"], 1)

def b2_cbh(rng):
    a, b, c = rng.randint(2, 12), rng.randint(2, 9), rng.randint(2, 6)
    return T(f"Tính: √{a * a} - {c}·√{b * b} + {c}².", f"{a} - {c}·{b} + {c * c} = {a - c * b + c * c}", 2)
def b2_x(rng):
    a, b = rng.randint(2, 10), rng.randint(2, 9)
    return T(f"Tìm x, biết (x - {b})² = {a * a}.", f"x - {b} = {a} hoặc x - {b} = -{a}\nx = {a + b} hoặc x = {b - a}", 3)
def b2_ss(rng):
    ds = rng.sample([x for x in range(2, 30)], 4)
    return T("Sắp xếp các số sau theo thứ tự tăng dần: " + ", ".join(f"√{x}" for x in ds) + ".", ", ".join(f"√{x}" for x in sorted(ds)), 1)
def b2_phan(rng):
    h = rng.randint(2, 9) ** 2; v = rng.choice([x for x in range(2, 30) if math.isqrt(x) ** 2 != x])
    return T(f"Trong các số √{h}, √{v}, {rng.randint(2, 9)}, 0,5, số nào là số vô tỉ? Vì sao?", f"√{v} là số vô tỉ vì {v} không phải là bình phương của số tự nhiên (căn không là số hữu tỉ). Các số còn lại là số hữu tỉ.", 2)
def b2_lt(rng):
    x = rd(rng, 1, 90, 3)
    return T(f"Làm tròn số {tp(x)} đến hàng phần mười và đến hàng phần trăm.", f"Phần mười: {tpf(x, 1)}\nPhần trăm: {tpf(x, 2)}", 1)
def b2_dtich(rng):
    k = rng.randint(3, 15)
    return T(f"Một mảnh đất hình vuông có diện tích {k * k} m². Tính chu vi mảnh đất.", f"Cạnh = √{k * k} = {k} m\nChu vi = 4 · {k} = {4 * k} m", 2)

# ============ 3. Góc và đường thẳng song song ============
def a3_doi_dinh(rng):
    x = rng.randint(20, 160); return nint(rng, f"Hai đường thẳng cắt nhau tạo thành hai góc đối đỉnh. Một góc có số đo {x}° thì góc đối đỉnh với nó có số đo (độ):", x, 1, (10, 20, 30), 0)
def a3_ke_bu(rng):
    x = rng.randint(20, 160); return nint(rng, f"Hai góc kề bù, một góc có số đo {x}°. Góc kia có số đo (độ):", 180 - x, 1, (10, 20, 30), 0)
def a3_pg(rng):
    x = rng.randint(2, 8) * 20; return nint(rng, f"Tia Oz là phân giác của góc xOy = {x}°. Số đo góc xOz là (độ):", x // 2, 1, (10, 20, 5), 0)
def a3_so_le(rng):
    x = rng.randint(30, 150); return nint(rng, f"Đường thẳng c cắt hai đường thẳng song song a, b. Góc A₁ = {x}° và A₁ so le trong với B₁. Số đo B₁ là (độ):", x, 2, (10, 20, 30), 0)
def a3_dong_vi(rng):
    x = rng.randint(30, 150); return nint(rng, f"Đường thẳng c cắt hai đường thẳng song song a, b. Góc A₂ = {x}° và A₂, B₂ là hai góc đồng vị. Số đo B₂ là (độ):", x, 2, (10, 20, 30), 0)
def a3_trong_cung(rng):
    x = rng.randint(40, 140); return nint(rng, f"Đường thẳng c cắt hai đường thẳng song song a, b. Hai góc trong cùng phía là A₁ và B₂, biết A₁ = {x}°. Số đo B₂ là (độ):", 180 - x, 2, (10, 20, 30), 0)
def a3_ss(rng):
    return M(rng.choice(["Qua một điểm nằm ngoài đường thẳng a, có bao nhiêu đường thẳng song song với a?", "Theo tiên đề Euclid, qua một điểm M nằm ngoài đường thẳng a, số đường thẳng đi qua M và song song với a là:"]), "Một và chỉ một", ["Hai", "Vô số", "Không có"], 1)
def a3_vuong(rng):
    return M("Hai đường thẳng cùng vuông góc với một đường thẳng thứ ba thì chúng:", "Song song với nhau", ["Cắt nhau", "Trùng nhau", "Vuông góc với nhau"], 2)
def a3_tc(rng):
    x = rng.randint(30, 150); return nint(rng, f"Cho a // b, c cắt a tại A, cắt b tại B. Góc xAB (đồng vị với góc yBC) = {x}°, góc yBC bằng (độ):", x, 2, (10, 20, 30), 0)
def a3_goc_tt(rng):
    a, b = rng.randint(20, 80), rng.randint(20, 80); return nint(rng, f"Tia Oy nằm giữa hai tia Ox, Oz, xOy = {a}°, yOz = {b}°. Tính xOz (độ):", a + b, 1, (10, 20, 5), 0)
def a3_ngoai(rng):
    a, b = rng.randint(30, 90), rng.randint(20, 70); return nint(rng, f"Hai đường thẳng song song bị cắt bởi một cát tuyến, góc A₁ = {a}° và góc A₃ đối đỉnh với A₁. Số đo A₃ là (độ):", a, 2, (10, 20, 5), 0)
def a3_kiem_tra(rng):
    a = rng.randint(40, 120); return M(f"Hai đường thẳng a, b bị cắt bởi đường thẳng c, có một cặp góc so le trong bằng {a}° và {a}°. Kết luận nào đúng?", "a // b", ["a ⊥ b", "a cắt b", "a trùng b"], 2)

def b3_tinh(rng):
    x = rng.randint(30, 150)
    return T(f"Hai đường thẳng xx' và yy' cắt nhau tại O, biết xOy = {x}°. Tính x'Oy, xOy', x'Oy'.", f"x'Oy = 180° - {x}° = {180 - x}°\nxOy' = x'Oy = {180 - x}° (đối đỉnh)\nx'Oy' = xOy = {x}° (đối đỉnh)", 2)
def b3_ss(rng):
    x = rng.randint(40, 130)
    return T(f"Cho a // b, đường thẳng c cắt a, b tại A, B. Biết một góc ở A bằng {x}°. Tính hai góc đồng vị và hai góc trong cùng phía tương ứng ở B.", f"Góc đồng vị ở B bằng góc ở A = {x}°.\nGóc trong cùng phía = 180° - {x}° = {180 - x}°.", 3)
def b3_pg(rng):
    x = rng.randint(2, 8) * 20
    return T(f"Vẽ góc xOy = {x}°. Vẽ tia phân giác Oz. Tính xOz và vẽ tia Ot là tia đối của tia Ox. Tính tOy.", f"xOz = {x // 2}°\ntOy = 180° - {x}° = {180 - x}° (kề bù với xOy)", 2)
def b3_cm(rng):
    a = rng.randint(40, 120)
    return T(f"Cho hai đường thẳng a, b cùng cắt đường thẳng c, có cặp góc đồng vị bằng nhau và bằng {a}°. Chứng minh a // b.", "Hai đường thẳng a, b cắt c tạo ra một cặp góc đồng vị bằng nhau nên theo dấu hiệu nhận biết hai đường thẳng song song, a // b.", 2)
def b3_euclid(rng):
    return T("Phát biểu tiên đề Euclid về đường thẳng song song và nêu hai tính chất của hai đường thẳng song song.", "Tiên đề Euclid: Qua một điểm ở ngoài một đường thẳng chỉ có một đường thẳng song song với đường thẳng đó.\nTính chất: hai đường thẳng song song bị cắt bởi một cát tuyến thì hai góc so le trong bằng nhau, hai góc đồng vị bằng nhau, hai góc trong cùng phía bù nhau.", 1)
def b3_tong(rng):
    a = rng.randint(30, 80); b = rng.randint(30, 80)
    return T(f"Tia Oy nằm giữa hai tia Ox, Oz, xOy = {a}°, yOz = {b}°. Tính xOz. Tia nào là phân giác nếu a = b?", f"xOz = {a} + {b} = {a + b}°. Nếu xOy = yOz thì Oy là tia phân giác của xOz.", 1)

# ============ 4. Tam giác bằng nhau ============
def a4_tong(rng):
    a, b = rng.randint(30, 80), rng.randint(30, 80); return nint(rng, f"Tam giác ABC có góc A = {a}°, góc B = {b}°. Số đo góc C là (độ):", 180 - a - b, 1, (10, 20, 5), 0)
def a4_vuong(rng):
    b = rng.randint(20, 70); return nint(rng, f"Tam giác ABC vuông tại A, góc B = {b}°. Số đo góc C là (độ):", 90 - b, 1, (10, 20, 5), 0)
def a4_ngoai(rng):
    a, b = rng.randint(30, 80), rng.randint(30, 80); return nint(rng, f"Tam giác ABC có góc A = {a}°, góc B = {b}°. Góc ngoài tại đỉnh C có số đo (độ):", a + b, 2, (10, 20, 5), 0)
def a4_can(rng):
    a = rng.randint(2, 8) * 10 + 20; return nint(rng, f"Tam giác ABC cân tại A, góc A = {a}°. Số đo góc B là (độ):", (180 - a) // 2, 2, (10, 20, 5), 0) if (180 - a) % 2 == 0 else (_ for _ in ()).throw(ValueError)
def a4_can2(rng):
    b = rng.randint(30, 80); return nint(rng, f"Tam giác ABC cân tại A, góc B = {b}°. Số đo góc A là (độ):", 180 - 2 * b, 2, (10, 20, 5), 0)
def a4_deu(rng):
    return M("Mỗi góc của tam giác đều có số đo là:", "60°", ["45°", "90°", "30°"], 1)
def a4_truong_hop(rng):
    return M(rng.choice(["Hai tam giác có ba cặp cạnh tương ứng bằng nhau thì bằng nhau theo trường hợp nào?", "Trường hợp bằng nhau cạnh - cạnh - cạnh được viết tắt là:"]), "c.c.c", ["c.g.c", "g.c.g", "góc - góc - góc"], 1)
def a4_cgc(rng):
    return M("Hai tam giác có hai cặp cạnh bằng nhau và góc xen giữa bằng nhau thì bằng nhau theo trường hợp:", "c.g.c", ["c.c.c", "g.c.g", "cạnh - cạnh - góc"], 1)
def a4_gcg(rng):
    return M("Hai tam giác có một cặp cạnh bằng nhau và hai góc kề cạnh đó tương ứng bằng nhau thì bằng nhau theo trường hợp:", "g.c.g", ["c.c.c", "c.g.c", "góc - góc - góc"], 1)
def a4_huyen(rng):
    return M("Hai tam giác vuông bằng nhau nếu có cạnh huyền và một góc nhọn tương ứng bằng nhau. Đây là trường hợp:", "cạnh huyền - góc nhọn", ["cạnh huyền - cạnh góc vuông (sai)", "góc - góc - góc", "cạnh - góc - cạnh (không xen giữa)"], 2)
def a4_tuong_ung(rng):
    a, b, c = rng.randint(3, 12), rng.randint(3, 12), rng.randint(3, 12); return nint(rng, f"Biết ΔABC = ΔDEF, AB = {a} cm, BC = {b} cm, CA = {c} cm. Độ dài DE là (cm):", a, 1, (1, 2, 3), 0)
def a4_goc_tu(rng):
    a = rng.randint(20, 80); return nint(rng, f"Biết ΔABC = ΔDEF, góc A = {a}°. Số đo góc D là (độ):", a, 1, (10, 20, 5), 0)
def a4_chuvi(rng):
    a, b, c = rng.randint(3, 12), rng.randint(3, 12), rng.randint(3, 12); return nint(rng, f"ΔABC = ΔMNP có AB = {a} cm, BC = {b} cm, CA = {c} cm. Chu vi tam giác MNP là (cm):", a + b + c, 1, (1, 2, 3), 0)

def b4_goc(rng):
    a, b = rng.randint(30, 80), rng.randint(30, 80)
    return T(f"Tam giác ABC có góc A = {a}°, góc B = {b}°. Tính góc C và góc ngoài tại đỉnh C.", f"C = 180° - {a}° - {b}° = {180 - a - b}°\nGóc ngoài tại C = 180° - {180 - a - b}° = {a + b}°", 2)
def b4_can(rng):
    a = rng.randint(3, 8) * 10
    return T(f"Tam giác ABC cân tại A có góc A = {a}°. Tính góc B và góc C.", f"B = C = (180° - {a}°) : 2 = {(180 - a) // 2}° (vì ΔABC cân tại A).", 2)
def b4_cm(rng):
    return T("Cho tam giác ABC có AB = AC. Gọi M là trung điểm của BC. Chứng minh ΔABM = ΔACM.", "Xét ΔABM và ΔACM có: AB = AC (gt); MB = MC (M là trung điểm của BC); AM chung.\nVậy ΔABM = ΔACM (c.c.c).", 2)
def b4_cm2(rng):
    return T("Cho góc xOy, tia phân giác Oz. Lấy A ∈ Ox, B ∈ Oy sao cho OA = OB. Chứng minh ΔOAM = ΔOBM, với M là điểm bất kì trên Oz.", "Xét ΔOAM và ΔOBM có: OA = OB (gt); AOM = BOM (Oz là phân giác); OM chung.\nVậy ΔOAM = ΔOBM (c.g.c).", 3)
def b4_chuvi(rng):
    a, b, c = rng.randint(3, 12), rng.randint(3, 12), rng.randint(3, 12)
    return T(f"Cho ΔABC = ΔDEF. Biết AB = {a} cm, BC = {b} cm, CA = {c} cm. Tính các cạnh của ΔDEF và chu vi.", f"DE = {a} cm; EF = {b} cm; FD = {c} cm. Chu vi = {a + b + c} cm.", 1)
def b4_deu(rng):
    c = rng.randint(3, 15)
    return T(f"Tam giác đều ABC có chu vi {3 * c} cm. Tính độ dài mỗi cạnh và số đo mỗi góc.", f"Cạnh = {3 * c} : 3 = {c} cm. Mỗi góc bằng 180° : 3 = 60°.", 1)

# ============ 5. Thu thập và biểu diễn dữ liệu ============
DL = [("Số học sinh trong lớp", "Số liệu rời rạc (định lượng)"), ("Màu sắc yêu thích", "Dữ liệu định tính"), ("Chiều cao của học sinh", "Số liệu liên tục (định lượng)"),
      ("Tên môn học yêu thích", "Dữ liệu định tính"), ("Số điểm 10 của mỗi bạn", "Số liệu rời rạc (định lượng)"), ("Cân nặng của học sinh", "Số liệu liên tục (định lượng)"),
      ("Nơi sinh của học sinh", "Dữ liệu định tính"), ("Số anh chị em ruột của mỗi bạn", "Số liệu rời rạc (định lượng)"), ("Nhiệt độ trung bình các ngày", "Số liệu liên tục (định lượng)"),
      ("Loại phương tiện đến trường", "Dữ liệu định tính")]
LOAI_DL = ["Dữ liệu định tính", "Số liệu rời rạc (định lượng)", "Số liệu liên tục (định lượng)", "Không phải dữ liệu"]
def a5_loai(rng):
    x, d = rng.choice(DL); return M(f"\"{x}\" thuộc loại dữ liệu nào?", d, [y for y in LOAI_DL if y != d], 2)
def a5_phan_tram(rng):
    n = rng.randint(2, 9) * 20; a = rng.randint(2, 6) * 10; return nint(rng, f"Khảo sát {n} học sinh, có {a}% chọn môn Toán. Số học sinh chọn môn Toán là:", n * a // 100, 2, (2, 5, 10), 0)
def a5_quat(rng):
    p = rng.choice([10, 20, 25, 30, 40, 50]); return nint(rng, f"Trong biểu đồ hình quạt tròn, một phần chiếm {p}% thì góc ở tâm của hình quạt đó là (độ):", p * 360 // 100, 3, (10, 20, 36), 0)
def a5_tong(rng):
    ds = [rng.randint(5, 30) for _ in range(4)]; return nint(rng, f"Biểu đồ cột cho số học sinh 4 tổ lần lượt là {', '.join(map(str, ds))}. Tổng số học sinh là:", sum(ds), 1, (1, 2, 5), 0)
def a5_max(rng):
    ds = rng.sample(range(5, 40), 4); t = ["Tổ 1", "Tổ 2", "Tổ 3", "Tổ 4"]; i = ds.index(max(ds))
    return M(f"Số học sinh của bốn tổ lần lượt là {', '.join(map(str, ds))} (Tổ 1 đến Tổ 4). Tổ có nhiều học sinh nhất là:", t[i], [x for x in t if x != t[i]], 1)
def a5_tb(rng):
    n = rng.randint(3, 6); ds = [rng.randint(5, 10) for _ in range(n)]
    if sum(ds) % n: raise ValueError
    return nint(rng, f"Điểm kiểm tra của {n} bạn là {', '.join(map(str, ds))}. Điểm trung bình của {n} bạn là:", sum(ds) // n, 2, (1, 2), 0)
def a5_tile(rng):
    a, b = rng.randint(3, 15), rng.randint(3, 15); p = a * 100 // (a + b)
    if a * 100 % (a + b): raise ValueError
    return M(f"Lớp có {a} bạn nam và {b} bạn nữ. Tỉ lệ phần trăm số bạn nam so với cả lớp là:", f"{p}%", chon3(rng, [f"{p + 5}%", f"{p - 5}%", f"{100 - p}%", f"{p * 2}%"], f"{p}%"), 2)
def a5_vuot(rng):
    return M("Loại biểu đồ nào thích hợp để biểu diễn sự thay đổi của một đại lượng theo thời gian?", "Biểu đồ đoạn thẳng", ["Biểu đồ hình quạt tròn", "Biểu đồ cột kép", "Bảng tần số"], 2)
def a5_quat2(rng):
    return M("Loại biểu đồ nào thích hợp để biểu diễn tỉ lệ phần trăm của các phần so với tổng thể?", "Biểu đồ hình quạt tròn", ["Biểu đồ đoạn thẳng", "Biểu đồ tranh", "Biểu đồ cột"], 1)
def a5_goc_pt(rng):
    g = rng.choice([36, 72, 90, 108, 144, 180]); return M(f"Trong biểu đồ hình quạt tròn, hình quạt có góc ở tâm {g}° chiếm tỉ lệ phần trăm là:", f"{g * 100 // 360}%", chon3(rng, [f"{g * 100 // 360 + 10}%", f"{g * 100 // 360 + 5}%", f"{max(g * 100 // 360 - 5, 1)}%", f"{g}%"], f"{g * 100 // 360}%"), 3)
def a5_hieu(rng):
    a, b = rng.randint(10, 50), rng.randint(5, 40)
    if a == b: raise ValueError
    return nint(rng, f"Số học sinh thích bóng đá là {a}, thích cầu lông là {b}. Số học sinh thích bóng đá nhiều hơn cầu lông là:", a - b, 1, (1, 2, 5))

def b5_loai(rng):
    ds = rng.sample(DL, 4); return T("Phân loại các dữ liệu sau (định tính hay định lượng; rời rạc hay liên tục): " + "; ".join(x for x, _ in ds) + ".", "\n".join(f"{x}: {d}" for x, d in ds), 1)
def b5_quat(rng):
    ps_ = [("Toán", 40), ("Văn", 30), ("Anh", 20), ("Khác", 10)]; n = rng.randint(2, 6) * 10
    return T(f"Biểu đồ hình quạt biểu diễn môn học yêu thích của {n * 10} học sinh: Toán 40%, Văn 30%, Anh 20%, Khác 10%. Tính số học sinh của mỗi nhóm và góc ở tâm tương ứng.", "\n".join(f"{t}: {n * 10 * p // 100} học sinh, góc {p * 360 // 100}°" for t, p in ps_), 2)
def b5_tb(rng):
    ds = [rng.randint(5, 10) for _ in range(5)]
    return T(f"Điểm 5 bài kiểm tra của Lan là {', '.join(map(str, ds))}. Tính điểm trung bình cộng và cho biết điểm nào cao nhất.", f"TB = ({' + '.join(map(str, ds))}) : 5 = {sum(ds) / 5:g}\nĐiểm cao nhất: {max(ds)}", 1)
def b5_bang(rng):
    a, b, c = rng.randint(5, 20), rng.randint(5, 20), rng.randint(5, 20); n = a + b + c
    return T(f"Khảo sát phương tiện đến trường của {n} học sinh: đi bộ {a}, xe đạp {b}, xe máy {c}. Tính tỉ lệ phần trăm mỗi loại (làm tròn đến hàng phần mười).", f"Đi bộ: {a * 100 / n:.1f}%\nXe đạp: {b * 100 / n:.1f}%\nXe máy: {c * 100 / n:.1f}%".replace(".", ","), 2)
def b5_chon(rng):
    return T("Nêu cách chọn biểu đồ phù hợp: biểu diễn (1) tỉ lệ các loại học lực của lớp; (2) nhiệt độ trung bình từng tháng trong năm.", "(1) Biểu đồ hình quạt tròn (so sánh các phần trong tổng thể). (2) Biểu đồ đoạn thẳng (thể hiện sự thay đổi theo thời gian).", 1)
def b5_hon(rng):
    a, b = rng.randint(10, 50), rng.randint(5, 40)
    if a == b: raise ValueError
    return T(f"Lớp 7A thu được {a} kg giấy vụn, lớp 7B thu được {b} kg. Lớp nào thu được nhiều hơn và nhiều hơn bao nhiêu phần trăm so với lớp còn lại (làm tròn đến hàng đơn vị)?", f"Chênh lệch: |{a} - {b}| = {abs(a - b)} kg\nTỉ lệ so với lớp ít hơn: {abs(a - b) * 100 / min(a, b):.0f}%", 3)

# ============ 6. Tỉ lệ thức và đại lượng tỉ lệ ============
def a6_tlt(rng):
    a, b = rng.randint(2, 9), rng.randint(2, 9); k = rng.randint(2, 6); c = a * k; x = b * k
    return nint(rng, f"Tìm x biết {a}/{b} = {c}/x. Giá trị x là:", x, 2, (1, 2, 5), 0)
def a6_tlt2(rng):
    a, b = rng.randint(2, 9), rng.randint(2, 9); k = rng.randint(2, 6)
    return nint(rng, f"Tìm x biết x/{a} = {b * k}/{b}. Giá trị x là:", a * k, 2, (1, 2, 5), 0)
def a6_dtsbn(rng):
    a, b = rng.randint(2, 7), rng.randint(2, 7); s = (a + b) * rng.randint(2, 6); k = s // (a + b)
    return nint(rng, f"Biết x/{a} = y/{b} và x + y = {s}. Giá trị của x là:", a * k, 3, (a, 2, 5), 0)
def a6_dtsbn2(rng):
    a, b = rng.randint(2, 7), rng.randint(2, 7); d = abs(a - b) * rng.randint(2, 6)
    if a == b: raise ValueError
    k = d // abs(a - b); x, y = a * k, b * k
    return nint(rng, f"Biết x/{a} = y/{b} và |x - y| = {d}. Với x, y là các số dương, tổng x + y bằng:", x + y, 3, (a, 2, 5), 0)
def a6_thuan(rng):
    k = rng.randint(2, 9); x = rng.randint(2, 9)
    return nint(rng, f"Hai đại lượng x và y tỉ lệ thuận, khi x = {x} thì y = {k * x}. Hệ số tỉ lệ k là:", k, 2, (1, 2), 0)
def a6_thuan2(rng):
    k = rng.randint(2, 9); x1, x2 = rng.randint(2, 6), rng.randint(7, 15)
    return nint(rng, f"Biết y tỉ lệ thuận với x theo hệ số {k}. Khi x = {x2} thì y bằng:", k * x2, 2, (k, 2, 5), 0)
def a6_nghich(rng):
    a = rng.randint(2, 6) * rng.randint(2, 6) * 2; x = rng.choice([d for d in uoc(a) if 1 < d < a])
    return nint(rng, f"Hai đại lượng x, y tỉ lệ nghịch, khi x = {x} thì y = {a // x}. Hệ số tỉ lệ a bằng:", a, 2, (a // x, 2, 5), 0)
def a6_nghich2(rng):
    a = rng.randint(2, 6) * rng.randint(2, 6) * 2; d = [x for x in uoc(a) if 1 < x < a]; x1, x2 = rng.sample(d, 2)
    return nint(rng, f"Biết x, y tỉ lệ nghịch. Khi x = {x1} thì y = {a // x1}. Khi x = {x2} thì y bằng:", a // x2, 3, (1, 2, 5), 0)
def a6_cv(rng):
    a, b, m = rng.randint(3, 8), rng.randint(2, 6), rng.randint(2, 6); n = rng.randint(a + 2, 15)
    return nint(rng, f"{a} người làm xong một công việc trong {b * m} giờ. Hỏi {a * 2} người (năng suất như nhau) làm xong việc đó trong bao nhiêu giờ?", b * m // 2 if (b * m) % 2 == 0 else b * m, 3, (1, 2), 0) if (b * m) % 2 == 0 else (_ for _ in ()).throw(ValueError)
def a6_chia(rng):
    a, b = rng.randint(2, 6), rng.randint(2, 6); k = rng.randint(2, 6)
    return nint(rng, f"Chia số 100 thành hai phần tỉ lệ thuận với {a} và {b}. Chênh lệch... ".replace("Chênh lệch... ", "Phần lớn hơn (làm tròn đến số nguyên gần nhất nếu cần) bằng:") if False else f"Chia số {(a + b) * k} thành hai phần tỉ lệ với {a} và {b}. Phần lớn hơn bằng:", max(a, b) * k, 3, (k, 2, 5), 0)
def a6_tile_ban(rng):
    k = rng.randint(2, 9); return M(f"Nếu y = {k}x thì y và x là hai đại lượng:", "tỉ lệ thuận", ["tỉ lệ nghịch", "không có quan hệ gì", "luôn bằng nhau"], 1)

def b6_dtsbn(rng):
    a, b = rng.randint(2, 7), rng.randint(2, 7); k = rng.randint(2, 6); x, y = a * k, b * k
    return T(f"Tìm x, y biết x/{a} = y/{b} và x + y = {x + y}.", f"Theo tính chất dãy tỉ số bằng nhau: x/{a} = y/{b} = (x + y)/({a} + {b}) = {x + y}/{a + b} = {k}\nx = {a}·{k} = {x}; y = {b}·{k} = {y}", 2)
def b6_chia(rng):
    a, b, c = rng.randint(2, 5), rng.randint(2, 5), rng.randint(2, 5); k = rng.randint(2, 6)
    return T(f"Ba bạn góp vốn kinh doanh theo tỉ lệ {a} : {b} : {c}, tổng số vốn {(a + b + c) * k} triệu đồng. Tính vốn của mỗi bạn.", f"Mỗi phần: {(a + b + c) * k} : {a + b + c} = {k} triệu\nVốn: {a * k}; {b * k}; {c * k} (triệu đồng)", 2)
def b6_tt(rng):
    a = rng.randint(2, 9); k = rng.randint(2, 9)
    return T(f"Cứ {a} m vải giá {a * k} nghìn đồng. Hỏi {a * 3 + 1} m vải cùng loại giá bao nhiêu tiền?", f"Giá 1 m: {a * k} : {a} = {k} nghìn đồng\n{a * 3 + 1} m: {k} · {a * 3 + 1} = {k * (a * 3 + 1)} nghìn đồng", 2)
def b6_nghich(rng):
    a, v = rng.randint(2, 6), rng.randint(2, 6) * 10
    return T(f"Một ô tô đi từ A đến B với vận tốc {v} km/h hết {a * 2} giờ. Nếu đi với vận tốc {v * 2} km/h thì hết mấy giờ?", f"Quãng đường: {v} · {a * 2} = {v * a * 2} km\nThời gian: {v * a * 2} : {v * 2} = {a} giờ (vận tốc và thời gian tỉ lệ nghịch).", 2)
def b6_tlt(rng):
    a, b = rng.randint(2, 9), rng.randint(2, 9); k = rng.randint(2, 6)
    return T(f"Tìm x trong tỉ lệ thức {a}/{b} = {a * k}/x và kiểm tra lại bằng tính chất tích chéo.", f"x = {b} · {a * k} : {a} = {b * k}\nKiểm tra: {a} · {b * k} = {b} · {a * k} = {a * b * k}.", 2)
def b6_dayhh(rng):
    a, b, c = rng.randint(2, 6), rng.randint(2, 6), rng.randint(2, 6); k = rng.randint(2, 5)
    return T(f"Tìm ba số x, y, z biết x/{a} = y/{b} = z/{c} và x + y + z = {(a + b + c) * k}.", f"Mỗi phần: {(a + b + c) * k} : {a + b + c} = {k}\nx = {a * k}; y = {b * k}; z = {c * k}", 3)

# ============ 7. Biểu thức đại số, đa thức một biến ============
def a7_gt(rng):
    a, b, x = rng.randint(2, 6), rng.randint(-8, 8), rng.randint(-4, 5); d = a * x + b
    return nint(rng, f"Giá trị của biểu thức {da([a, b])} tại x = {x} là:", d, 1, (1, 2, 5))
def a7_gt2(rng):
    cs = rpoly(rng, 2, -5, 5); x = rng.randint(-3, 4); d = dval(cs, x)
    return nint(rng, f"Giá trị của đa thức {da(cs)} tại x = {x} là:", d, 2, (1, 2, 5))
def a7_bac(rng):
    n = rng.randint(2, 6); cs = [rng.randint(1, 5)] + [rng.randint(-5, 5) for _ in range(n)]; return nint(rng, f"Bậc của đa thức {da(cs)} là:", n, 1, (1, 2), 0)
def a7_hscao(rng):
    cs = rpoly(rng, rng.randint(2, 4), -7, 7); return nint(rng, f"Hệ số cao nhất của đa thức {da(cs)} là:", cs[0], 1, (1, 2, 3))
def a7_tdt(rng):
    cs = rpoly(rng, 3, -6, 6); cs[-1] = rng.choice([x for x in range(-8, 9) if x]); return nint(rng, f"Hệ số tự do của đa thức {da(cs)} là:", cs[-1], 1, (1, 2, 3))
def a7_cong(rng):
    a, b = rpoly(rng, 2, -5, 5), rpoly(rng, 2, -5, 5); r = dadd(a, b)
    if r[0] == 0 and len(set(r)) == 1: raise ValueError
    s = da(r); return M(f"({da(a)}) + ({da(b)}) = ?", s, lay_sai_da(rng, r), 2)
def a7_tru(rng):
    a, b = rpoly(rng, 2, -5, 5), rpoly(rng, 2, -5, 5); r = dadd(a, b, -1)
    if all(c == 0 for c in r): raise ValueError
    return M(f"({da(a)}) - ({da(b)}) = ?", da(r), lay_sai_da(rng, r), 2)
def a7_nhan_dt(rng):
    a = rng.randint(2, 6); b = rpoly(rng, 2, -4, 4); r = dmul([a], b)
    return M(f"{a}·({da(b)}) = ?", da(r), lay_sai_da(rng, r), 2)
def a7_nhan(rng):
    a, b = rpoly(rng, 1, -4, 4), rpoly(rng, 1, -4, 4); r = dmul(a, b)
    return M(f"({da(a)})({da(b)}) = ?", da(r), lay_sai_da(rng, r), 3)
def a7_chia(rng):
    q = rpoly(rng, 1, -5, 5); d = rng.randint(2, 5); r = dmul(q, [d, 0]) if False else dmul(q, [d])
    return M(f"({da(r)}) : {d} = ?", da(q) if False else da([c // d for c in r]) if all(c % d == 0 for c in r) else (_ for _ in ()).throw(ValueError), lay_sai_da(rng, [c // d for c in r] if all(c % d == 0 for c in r) else [1, 1]), 2) if all(c % d == 0 for c in r) else (_ for _ in ()).throw(ValueError)
def a7_nghiem(rng):
    r = rng.randint(-6, 6); a = rng.randint(2, 5); cs = [a, -a * r]
    return M(f"Nghiệm của đa thức {da(cs)} là:", r, [x for x in [r + 1, r - 1, -r if r else 1, a][:4] if x != r][:3] if len({r + 1, r - 1, a * r, -r, a}) > 3 else [r + 1, r - 1, r + 2], 2)
def a7_nghiem2(rng):
    r = rng.randint(1, 6); cs = [1, -r - 1, r]; x0 = rng.choice([r, 1])
    return M(f"Giá trị x = {x0} có phải là nghiệm của đa thức {da(cs)} không?", "Có", ["Không", "Chỉ khi x > 0", "Không xác định"], 3)
def a7_dongdang(rng):
    a, b, c = rng.randint(2, 6), rng.randint(2, 6), rng.randint(1, 5); n = rng.randint(2, 3)
    return M(f"Cộng hai đơn thức đồng dạng {a}x{str(n).translate(SUP)} và {b}x{str(n).translate(SUP)} ta được:", f"{a + b}x{str(n).translate(SUP)}", [f"{a * b}x{str(n).translate(SUP)}", f"{a + b}x{str(2 * n).translate(SUP)}", f"{a + b}x"], 2)

def b7_gt(rng):
    cs = rpoly(rng, 2, -5, 5); x = rng.randint(-3, 3)
    return T(f"Tính giá trị của đa thức P(x) = {da(cs)} tại x = {x}.", f"P({x}) = {da(cs).replace('x', f'({x})')} = {dval(cs, x)}", 1)
def b7_cong(rng):
    a, b = rpoly(rng, 2, -5, 5), rpoly(rng, 2, -5, 5)
    return T(f"Cho P(x) = {da(a)} và Q(x) = {da(b)}. Tính P(x) + Q(x) và P(x) - Q(x).", f"P + Q = {da(dadd(a, b))}\nP - Q = {da(dadd(a, b, -1))}", 2)
def b7_nhan(rng):
    a, b = rpoly(rng, 1, -4, 4), rpoly(rng, 2, -3, 3)
    return T(f"Nhân hai đa thức: ({da(a)})({da(b)}).", f"= {da(dmul(a, b))}", 3)
def b7_nghiem(rng):
    r = rng.randint(-5, 5); a = rng.randint(2, 6)
    return T(f"Tìm nghiệm của đa thức {da([a, -a * r])}.", f"{da([a, -a * r])} = 0 ⇒ x = {r}", 1)
def b7_bac(rng):
    cs = rpoly(rng, rng.randint(3, 4), -6, 6)
    return T(f"Cho đa thức P(x) = {da(cs)}. Xác định bậc, hệ số cao nhất và hệ số tự do của P(x).", f"Bậc: {len(cs) - 1}\nHệ số cao nhất: {cs[0]}\nHệ số tự do: {cs[-1]}", 1)
def b7_loi(rng):
    a, b = rng.randint(5, 20), rng.randint(2, 9); x = rng.randint(3, 10)
    return T(f"Một người mua x quyển vở giá {a} nghìn đồng một quyển và 1 chiếc bút giá {b} nghìn đồng. Viết biểu thức biểu thị tổng số tiền và tính tổng số tiền khi x = {x}.", f"Tổng tiền: {a}x + {b} (nghìn đồng)\nKhi x = {x}: {a}·{x} + {b} = {a * x + b} nghìn đồng", 1)

# ============ 8. Biến cố và xác suất ============
def a8_bc(rng):
    return M(rng.choice(["Tung một đồng xu, biến cố \"xuất hiện mặt sấp hoặc mặt ngửa\" là biến cố:", "Biến cố \"mặt xuất hiện là mặt sấp hoặc ngửa\" khi tung đồng xu là:"]), "Biến cố chắc chắn", ["Biến cố không thể", "Biến cố ngẫu nhiên", "Không phải biến cố"], 1)
def a8_kt(rng):
    return M("Gieo một con xúc xắc 6 mặt, biến cố \"xuất hiện mặt 7 chấm\" là biến cố:", "Biến cố không thể", ["Biến cố chắc chắn", "Biến cố ngẫu nhiên", "Xác suất bằng 1"], 1)
def a8_ngau_nhien(rng):
    return M("Gieo một con xúc xắc, biến cố \"xuất hiện mặt 6 chấm\" là biến cố:", "Biến cố ngẫu nhiên", ["Biến cố chắc chắn", "Biến cố không thể", "Biến cố có xác suất 0"], 1)
def a8_xs_xx(rng):
    k = rng.randint(1, 5); return M(f"Gieo một con xúc xắc cân đối. Xác suất xuất hiện mặt {k} chấm là:", "1/6", ["1/3", "1/2", "1/5"], 1)
def a8_chan(rng):
    return M("Gieo một con xúc xắc cân đối. Xác suất của biến cố \"số chấm xuất hiện là số chẵn\" là:", "1/2", ["1/3", "1/6", "2/3"], 2)
def a8_nguyento(rng):
    return M("Gieo một con xúc xắc cân đối. Xác suất của biến cố \"mặt xuất hiện có số chấm là số nguyên tố\" là:", "1/2", ["1/3", "2/3", "1/6"], 3)
def a8_bong(rng):
    d, x, v = rng.randint(2, 8), rng.randint(2, 8), rng.randint(1, 6); n = d + x + v; f = Fraction(d, n)
    return M(f"Một hộp có {d} bóng đỏ, {x} bóng xanh, {v} bóng vàng cùng kích thước. Lấy ngẫu nhiên một bóng. Xác suất lấy được bóng đỏ là:", ps(f), nh_ps(rng, f), 2)
def a8_the(rng):
    n = rng.randint(10, 30); k = rng.randint(2, n // 2); f = Fraction(k, n)
    return M(f"Có {n} tấm thẻ ghi số từ 1 đến {n}. Rút ngẫu nhiên một thẻ. Xác suất rút được thẻ có số nhỏ hơn hoặc bằng {k} là:", ps(f), nh_ps(rng, f), 2)
def a8_boi(rng):
    n = rng.choice([20, 30, 40, 50]); k = rng.choice([2, 5, 10]); c = n // k; f = Fraction(c, n)
    return M(f"Rút ngẫu nhiên một tấm thẻ từ {n} thẻ đánh số 1 đến {n}. Xác suất để số ghi trên thẻ chia hết cho {k} là:", ps(f), nh_ps(rng, f), 3)
def a8_xs0(rng):
    return M("Xác suất của biến cố không thể bằng:", "0", ["1", "1/2", "Không xác định"], 1)
def a8_xs1(rng):
    return M("Xác suất của biến cố chắc chắn bằng:", "1", ["0", "1/2", "100"], 1)
def a8_dong(rng):
    return M("Tung đồng xu cân đối. Xác suất xuất hiện mặt sấp là:", "1/2", ["1", "1/4", "0"], 1)
def a8_khong_dung(rng):
    k = rng.randint(2, 6); n = rng.randint(7, 12); f = Fraction(n - k, n)
    return M(f"Trong hộp có {n} viên bi, trong đó {k} bi đỏ, còn lại là bi xanh. Lấy ngẫu nhiên một viên. Xác suất lấy được bi xanh là:", ps(f), nh_ps(rng, f), 2)

def b8_bc(rng):
    return T("Gieo một con xúc xắc. Hãy cho ví dụ về một biến cố chắc chắn, một biến cố không thể và một biến cố ngẫu nhiên.", "Chắc chắn: số chấm nhỏ hơn 7. Không thể: số chấm bằng 0 (hoặc bằng 7). Ngẫu nhiên: xuất hiện mặt 6 chấm.", 1)
def b8_xs(rng):
    d, x, v = rng.randint(2, 8), rng.randint(2, 8), rng.randint(1, 6); n = d + x + v
    return T(f"Một hộp có {d} bóng đỏ, {x} bóng xanh, {v} bóng vàng. Lấy ngẫu nhiên một bóng. Tính xác suất lấy được mỗi loại bóng.", f"Đỏ: {pf(d, n)}\nXanh: {pf(x, n)}\nVàng: {pf(v, n)}", 2)
def b8_the(rng):
    n = rng.randint(2, 5) * 10; k = rng.choice([2, 3, 5])
    return T(f"Rút ngẫu nhiên một thẻ từ {n} thẻ đánh số từ 1 đến {n}. Tính xác suất của biến cố \"thẻ ghi số chia hết cho {k}\".", f"Số kết quả thuận lợi: {n // k}\nXác suất: {pf(n // k, n)}", 2)
def b8_xuc_xac(rng):
    return T("Gieo một con xúc xắc cân đối. Tính xác suất của các biến cố: A: \"số chấm lớn hơn 4\"; B: \"số chấm là số lẻ\".", "A: các kết quả thuận lợi 5, 6 ⇒ P(A) = 2/6 = 1/3\nB: các kết quả 1, 3, 5 ⇒ P(B) = 3/6 = 1/2", 2)
def b8_hien_nhien(rng):
    k = rng.randint(3, 9)
    return T(f"Trong một túi chỉ có {k} viên bi đỏ. Lấy ngẫu nhiên một viên. Biến cố \"lấy được bi đỏ\" là biến cố gì? Xác suất bằng bao nhiêu?", "Là biến cố chắc chắn, xác suất bằng 1.", 1)
def b8_kb(rng):
    return T("Khi tung hai đồng xu, em có thể nhận được những kết quả nào? Tính xác suất để cả hai đồng đều sấp.", "Kết quả: SS, SN, NS, NN (4 kết quả đồng khả năng).\nP(cả hai sấp) = 1/4.", 2)

# ============ 9. Quan hệ giữa các yếu tố trong một tam giác ============
def a9_bdt(rng):
    a, b = rng.randint(3, 10), rng.randint(3, 10); c = rng.randint(abs(a - b) + 1, a + b - 1) if abs(a - b) + 1 <= a + b - 1 else None
    if c is None: raise ValueError
    ok = [a, b, c]; ng = [a, b, a + b + rng.randint(0, 3)]
    d = f"{ok[0]} cm, {ok[1]} cm, {ok[2]} cm"
    return M("Bộ ba độ dài nào có thể là ba cạnh của một tam giác?", d, [f"{ng[0]} cm, {ng[1]} cm, {ng[2]} cm", f"{a} cm, {a} cm, {a * 2 + 1} cm", f"{b} cm, {b + 1} cm, {2 * b + 3} cm"], 2)
def a9_khoang(rng):
    a, b = rng.randint(3, 10), rng.randint(3, 10)
    if a == b: raise ValueError
    lo, hi = abs(a - b), a + b
    return M(f"Tam giác có hai cạnh dài {a} cm và {b} cm. Độ dài cạnh thứ ba (số nguyên cm) có thể là:", min(hi - 1, lo + 1), [lo, hi, hi + 1], 3)
def a9_cg(rng):
    return M("Trong một tam giác, cạnh đối diện với góc lớn hơn thì:", "lớn hơn", ["nhỏ hơn", "bằng nhau", "không so sánh được"], 1)
def a9_gc(rng):
    return M("Trong một tam giác, góc đối diện với cạnh lớn nhất là:", "góc lớn nhất", ["góc nhỏ nhất", "góc vuông", "góc bằng 60°"], 1)
def a9_tronglg(rng):
    m = rng.randint(2, 8) * 3; return nint(rng, f"G là trọng tâm tam giác ABC, AM là trung tuyến, AM = {m} cm. Độ dài AG là (cm):", 2 * m // 3, 2, (1, 2, 3), 0)
def a9_trong2(rng):
    g = rng.randint(2, 8) * 2; return nint(rng, f"G là trọng tâm tam giác ABC, AM là trung tuyến, AG = {g} cm. Độ dài GM là (cm):", g // 2, 2, (1, 2, 3), 0)
def a9_dongquy(rng):
    return M("Ba đường trung tuyến của một tam giác cùng đi qua một điểm. Điểm đó gọi là:", "trọng tâm", ["trực tâm", "tâm đường tròn nội tiếp", "tâm đường tròn ngoại tiếp"], 1)
def a9_pg(rng):
    return M("Giao điểm ba đường phân giác của tam giác cách đều:", "ba cạnh của tam giác", ["ba đỉnh của tam giác", "hai cạnh bất kì", "ba trung điểm của ba cạnh"], 2)
def a9_trungtruc(rng):
    return M("Giao điểm ba đường trung trực của tam giác cách đều:", "ba đỉnh của tam giác", ["ba cạnh của tam giác", "hai đỉnh bất kì", "ba chân đường cao"], 2)
def a9_duong_cao(rng):
    return M("Giao điểm của ba đường cao trong một tam giác gọi là:", "trực tâm", ["trọng tâm", "tâm đường tròn nội tiếp", "tâm đường tròn ngoại tiếp"], 1)
def a9_xien(rng):
    return M("Cho điểm A nằm ngoài đường thẳng d, AH ⊥ d (H ∈ d), B là điểm bất kì thuộc d (B ≠ H). So sánh AH và AB:", "AH < AB", ["AH > AB", "AH = AB", "Không so sánh được"], 2)
def a9_chuvi(rng):
    a = rng.randint(4, 12); b = rng.randint(4, 12); return nint(rng, f"Tam giác ABC cân tại A có AB = {a} cm, BC = {b} cm. Chu vi tam giác là (cm):", 2 * a + b, 1, (a, 2, 5), 0) if abs(a - a) < b < 2 * a else (_ for _ in ()).throw(ValueError)
def a9_goc_nho(rng):
    a, b = rng.randint(40, 80), rng.randint(40, 80); return M(f"Tam giác ABC có góc A = {a}°, góc B = {b}°. Cạnh nào ngắn nhất (góc C = {180 - a - b}°)?", ["BC", "AC", "AB"][[a, b, 180 - a - b].index(min(a, b, 180 - a - b))], [x for x in ["BC", "AC", "AB"] if x != ["BC", "AC", "AB"][[a, b, 180 - a - b].index(min(a, b, 180 - a - b))]] + ["Không xác định"], 3) if len({a, b, 180 - a - b}) == 3 else (_ for _ in ()).throw(ValueError)

def b9_bdt(rng):
    a, b = rng.randint(3, 9), rng.randint(3, 9); c = a + b + rng.randint(0, 3)
    return T(f"Có thể dựng được tam giác có ba cạnh {a} cm, {b} cm, {c} cm không? Vì sao?", f"Không, vì {a} + {b} = {a + b} ≤ {c} (tổng hai cạnh phải lớn hơn cạnh còn lại).", 1)
def b9_tg(rng):
    g = rng.randint(2, 8) * 3
    return T(f"G là trọng tâm tam giác ABC, trung tuyến AM = {g} cm. Tính AG và GM.", f"AG = (2/3)·AM = {2 * g // 3} cm; GM = (1/3)·AM = {g // 3} cm.", 2)
def b9_so_sanh(rng):
    a, b = rng.randint(50, 80), rng.randint(40, 70); c = 180 - a - b
    if len({a, b, c}) < 3: raise ValueError
    return T(f"Tam giác ABC có góc A = {a}°, góc B = {b}°. Tính góc C và sắp xếp ba cạnh theo thứ tự tăng dần.", f"C = {c}°\nCạnh đối diện góc nhỏ hơn thì nhỏ hơn: " + ", ".join(n for n, _ in sorted([("BC", a), ("AC", b), ("AB", c)], key=lambda x: x[1])), 2)
def b9_cm(rng):
    return T("Cho tam giác ABC cân tại A. Gọi M là trung điểm của BC. Chứng minh AM vuông góc với BC.", "ΔABM = ΔACM (c.c.c) nên AMB = AMC. Mà AMB + AMC = 180° nên AMB = AMC = 90°. Vậy AM ⊥ BC.", 3)
def b9_dongquy(rng):
    return T("Nêu tên ba điểm đồng quy đặc biệt trong tam giác tương ứng với trung tuyến, phân giác, trung trực, đường cao.", "Trung tuyến: trọng tâm. Phân giác: tâm đường tròn nội tiếp (cách đều ba cạnh). Trung trực: tâm đường tròn ngoại tiếp (cách đều ba đỉnh). Đường cao: trực tâm.", 1)
def b9_khoang(rng):
    a, b = rng.randint(3, 10), rng.randint(3, 10)
    if a == b: raise ValueError
    return T(f"Tam giác có hai cạnh {a} cm và {b} cm. Hỏi cạnh thứ ba nằm trong khoảng nào?", f"{abs(a - b)} cm < cạnh thứ ba < {a + b} cm", 2)

# ============ 10. Một số hình khối trong thực tiễn ============
def a10_hhcn(rng):
    a, b, c = rng.randint(3, 15), rng.randint(2, 12), rng.randint(2, 10); return nint(rng, f"Hình hộp chữ nhật có ba kích thước {a} cm, {b} cm, {c} cm. Thể tích là (cm³):", a * b * c, 1, (a, b, c), 0)
def a10_lapphuong(rng):
    a = rng.randint(2, 12); return nint(rng, f"Hình lập phương có cạnh {a} cm. Thể tích là (cm³):", a ** 3, 1, (a, a * a, 6), 0)
def a10_sxq_hop(rng):
    a, b, c = rng.randint(3, 15), rng.randint(2, 12), rng.randint(2, 10); return nint(rng, f"Hình hộp chữ nhật có đáy {a} cm × {b} cm, chiều cao {c} cm. Diện tích xung quanh là (cm²):", 2 * (a + b) * c, 2, (c, 2, 10), 0)
def a10_lt(rng):
    a, b = rng.randint(3, 12), rng.randint(3, 12); h = rng.randint(3, 15); t = a * b // 2 if (a * b) % 2 == 0 else None
    if t is None: raise ValueError
    return nint(rng, f"Lăng trụ đứng có đáy là tam giác vuông hai cạnh góc vuông {a} cm, {b} cm, chiều cao {h} cm. Thể tích là (cm³):", t * h, 2, (h, a, b), 0)
def a10_sxq_lt(rng):
    a, b, c = rng.randint(3, 8), rng.randint(3, 8), rng.randint(3, 8); h = rng.randint(3, 12); return nint(rng, f"Lăng trụ đứng tam giác có đáy là tam giác ba cạnh {a} cm, {b} cm, {c} cm, chiều cao {h} cm. Diện tích xung quanh là (cm²):", (a + b + c) * h, 2, (h, 2, 10), 0)
def a10_dem(rng):
    return M(rng.choice(["Hình hộp chữ nhật có bao nhiêu mặt?", "Số mặt của hình hộp chữ nhật là:"]), 6, [4, 8, 12], 1)
def a10_canh(rng):
    return M("Hình hộp chữ nhật có bao nhiêu cạnh?", 12, [6, 8, 10], 1)
def a10_dinh(rng):
    return M("Hình lập phương có bao nhiêu đỉnh?", 8, [6, 12, 4], 1)
def a10_lt_mat(rng):
    return M("Lăng trụ đứng tam giác có bao nhiêu mặt?", 5, [4, 6, 3], 2)
def a10_lt_canh(rng):
    return M("Lăng trụ đứng tam giác có bao nhiêu cạnh?", 9, [6, 12, 8], 2)
def a10_chieu_cao(rng):
    a, b = rng.randint(3, 12), rng.randint(3, 12); h = rng.randint(3, 10); return nint(rng, f"Một bể hình hộp chữ nhật đáy {a} m × {b} m chứa được {a * b * h} m³ nước. Chiều cao của bể là (m):", h, 3, (1, 2, 3), 0)
def a10_lit(rng):
    a, b, c = rng.randint(2, 8) * 10, rng.randint(2, 8) * 10, rng.randint(2, 8) * 10; return nint(rng, f"Một thùng hình hộp chữ nhật có ba kích thước {a} cm, {b} cm, {c} cm. Thể tích của thùng là (lít, biết 1 lít = 1000 cm³):", a * b * c // 1000, 3, (1, 2, 5), 0) if (a * b * c) % 1000 == 0 else (_ for _ in ()).throw(ValueError)
def a10_stp_lapphuong(rng):
    a = rng.randint(2, 12); return nint(rng, f"Hình lập phương cạnh {a} cm. Diện tích toàn phần là (cm²):", 6 * a * a, 2, (a, 2 * a, 12), 0)

def b10_hop(rng):
    a, b, c = rng.randint(3, 15), rng.randint(2, 12), rng.randint(2, 10)
    return T(f"Một hình hộp chữ nhật có ba kích thước {a} cm, {b} cm, {c} cm. Tính thể tích và diện tích xung quanh.", f"V = {a} · {b} · {c} = {a * b * c} cm³\nSxq = 2·({a} + {b})·{c} = {2 * (a + b) * c} cm²", 1)
def b10_lt(rng):
    a, b = rng.randint(2, 6) * 2, rng.randint(3, 9); h = rng.randint(3, 12)
    return T(f"Lăng trụ đứng có đáy là tam giác vuông với hai cạnh góc vuông {a} cm và {b} cm, chiều cao {h} cm. Tính thể tích.", f"Diện tích đáy: {a}·{b}:2 = {a * b // 2} cm²\nV = {a * b // 2} · {h} = {a * b // 2 * h} cm³", 2)
def b10_be(rng):
    a, b = rng.randint(3, 8), rng.randint(3, 8); h = rng.randint(2, 4)
    return T(f"Một bể nước hình hộp chữ nhật đáy {a} m × {b} m, cao {h} m. Bể chứa tối đa bao nhiêu lít nước (1 m³ = 1000 lít)?", f"V = {a}·{b}·{h} = {a * b * h} m³ = {a * b * h * 1000} lít", 2)
def b10_son(rng):
    a = rng.randint(2, 8)
    return T(f"Người ta sơn tất cả các mặt ngoài của một hình lập phương cạnh {a} dm. Tính diện tích cần sơn và thể tích hình lập phương.", f"S = 6·{a}² = {6 * a * a} dm²\nV = {a}³ = {a ** 3} dm³", 1)
def b10_cao(rng):
    a, b = rng.randint(3, 10), rng.randint(3, 10); h = rng.randint(3, 8)
    return T(f"Hình hộp chữ nhật có thể tích {a * b * h} cm³, đáy {a} cm × {b} cm. Tính chiều cao.", f"h = {a * b * h} : ({a}·{b}) = {h} cm", 2)
def b10_hh(rng):
    return T("Nêu số mặt, số cạnh, số đỉnh của hình hộp chữ nhật và lăng trụ đứng tam giác.", "Hình hộp chữ nhật: 6 mặt, 12 cạnh, 8 đỉnh.\nLăng trụ đứng tam giác: 5 mặt, 9 cạnh, 6 đỉnh.", 1)

CHU_DE = [
    ("Chương 1: Số hữu tỉ", [a1_cong, a1_tru, a1_nhan, a1_chia, a1_ss, a1_luythua, a1_doi, a1_gttd, a1_x, a1_x2, a1_tp, a1_bt], [b1_tinh, b1_x, b1_ss, b1_lt, b1_nhanh, b1_loi]),
    ("Chương 2: Số thực", [a2_cbh, a2_cbh2, a2_bt, a2_bt2, a2_vt, a2_hh, a2_ss, a2_ss2, a2_x, a2_gttd, a2_lt, a2_cbh_tp, a2_taphop], [b2_cbh, b2_x, b2_ss, b2_phan, b2_lt, b2_dtich]),
    ("Chương 3: Góc và đường thẳng song song", [a3_doi_dinh, a3_ke_bu, a3_pg, a3_so_le, a3_dong_vi, a3_trong_cung, a3_ss, a3_vuong, a3_tc, a3_goc_tt, a3_ngoai, a3_kiem_tra], [b3_tinh, b3_ss, b3_pg, b3_cm, b3_euclid, b3_tong]),
    ("Chương 4: Tam giác bằng nhau", [a4_tong, a4_vuong, a4_ngoai, a4_can, a4_can2, a4_deu, a4_truong_hop, a4_cgc, a4_gcg, a4_huyen, a4_tuong_ung, a4_goc_tu, a4_chuvi], [b4_goc, b4_can, b4_cm, b4_cm2, b4_chuvi, b4_deu]),
    ("Chương 5: Thu thập và biểu diễn dữ liệu", [a5_loai, a5_phan_tram, a5_quat, a5_tong, a5_max, a5_tb, a5_tile, a5_vuot, a5_quat2, a5_goc_pt, a5_hieu], [b5_loai, b5_quat, b5_tb, b5_bang, b5_chon, b5_hon]),
    ("Chương 6: Tỉ lệ thức và đại lượng tỉ lệ", [a6_tlt, a6_tlt2, a6_dtsbn, a6_dtsbn2, a6_thuan, a6_thuan2, a6_nghich, a6_nghich2, a6_cv, a6_chia, a6_tile_ban], [b6_dtsbn, b6_chia, b6_tt, b6_nghich, b6_tlt, b6_dayhh]),
    ("Chương 7: Biểu thức đại số và đa thức một biến", [a7_gt, a7_gt2, a7_bac, a7_hscao, a7_tdt, a7_cong, a7_tru, a7_nhan_dt, a7_nhan, a7_chia, a7_nghiem, a7_dongdang], [b7_gt, b7_cong, b7_nhan, b7_nghiem, b7_bac, b7_loi]),
    ("Chương 8: Làm quen với biến cố và xác suất của biến cố", [a8_bc, a8_kt, a8_ngau_nhien, a8_xs_xx, a8_chan, a8_nguyento, a8_bong, a8_the, a8_boi, a8_xs0, a8_xs1, a8_khong_dung], [b8_bc, b8_xs, b8_the, b8_xuc_xac, b8_hien_nhien, b8_kb]),
    ("Chương 9: Quan hệ giữa các yếu tố trong một tam giác", [a9_bdt, a9_khoang, a9_cg, a9_gc, a9_tronglg, a9_trong2, a9_dongquy, a9_pg, a9_trungtruc, a9_duong_cao, a9_xien, a9_goc_nho], [b9_bdt, b9_tg, b9_so_sanh, b9_cm, b9_dongquy, b9_khoang]),
    ("Chương 10: Một số hình khối trong thực tiễn", [a10_hhcn, a10_lapphuong, a10_sxq_hop, a10_lt, a10_sxq_lt, a10_dem, a10_canh, a10_dinh, a10_lt_mat, a10_lt_canh, a10_chieu_cao, a10_stp_lapphuong], [b10_hop, b10_lt, b10_be, b10_son, b10_cao, b10_hh]),
]
