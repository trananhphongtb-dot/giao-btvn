from tvcore import *
from tvcore import _tron

# ---------------------------------------------------------------- 1. Âm đầu và vần
VAN = [("bàn", "an"), ("đàn", "an"), ("bạn", "an"), ("cát", "at"), ("hạt", "at"), ("mắt", "ăt"), ("bận", "ân"),
       ("mật", "ât"), ("nón", "on"), ("con", "on"), ("hột", "ot"), ("bốn", "ôn"), ("tốt", "ôt"), ("sen", "en"),
       ("đèn", "en"), ("hết", "êt"), ("tên", "ên"), ("xin", "in"), ("tin", "in"), ("mít", "it"), ("bún", "un"),
       ("mưa", "ưa"), ("lửa", "ưa"), ("cua", "ua"), ("vua", "ua"), ("bia", "ia"), ("kéo", "eo"), ("mèo", "eo"),
       ("sao", "ao"), ("tay", "ay"), ("cây", "ây"), ("mai", "ai"), ("tai", "ai"), ("bầu", "âu"), ("sáu", "au"),
       ("hươu", "ươu"), ("cười", "ươi"), ("mui", "ui"), ("chiều", "iêu"), ("lạnh", "anh"), ("xanh", "anh"),
       ("sách", "ach"), ("gạch", "ach"), ("kem", "em"), ("chim", "im"), ("tim", "im"), ("trăng", "ăng"),
       ("sáng", "ang"), ("vàng", "ang"), ("sông", "ông"), ("học", "oc"), ("hoa", "oa"), ("khoẻ", "oe"),
       ("thúng", "ung"), ("cúc", "uc"), ("rừng", "ưng"), ("đẹp", "ep"), ("hộp", "ôp"), ("cơm", "ơm"), ("ốm", "ôm")]
AM = [("bàn", "b"), ("cá", "c"), ("đi", "đ"), ("gà", "g"), ("ghế", "gh"), ("kẻ", "k"), ("khỉ", "kh"), ("lá", "l"),
      ("mẹ", "m"), ("nhà", "nh"), ("nghe", "ngh"), ("ngã", "ng"), ("phở", "ph"), ("quả", "qu"), ("sáo", "s"),
      ("tôm", "t"), ("thỏ", "th"), ("trâu", "tr"), ("chó", "ch"), ("giỏ", "gi"), ("vịt", "v"), ("xe", "x"),
      ("hoa", "h"), ("dê", "d"), ("rổ", "r")]
_vans = sorted({v for _, v in VAN})
_ams = sorted({a for _, a in AM})


def mc_van_cua(rng):
    t, v = rng.choice(VAN)
    return M(f"Tiếng \"{t}\" có vần gì?", v, _tron(rng, v, _vans), 1)


def mc_tieng_van(rng):
    t, v = rng.choice(VAN)
    khac = [x for x, vv in VAN if vv != v]
    return M(f"Tiếng nào dưới đây có vần \"{v}\"?", t, _tron(rng, t, khac), 1)


def mc_am_cua(rng):
    t, a = rng.choice(AM)
    return M(f"Tiếng \"{t}\" có âm đầu là:", a, _tron(rng, a, _ams), 1)


def mc_tieng_am(rng):
    t, a = rng.choice(AM)
    khac = [x for x, aa in AM if aa != a]
    return M(f"Tiếng nào dưới đây có âm đầu \"{a}\"?", t, _tron(rng, t, khac), 1)


def tl_van(rng):
    v = rng.choice(_vans)
    ds = [t for t, vv in VAN if vv == v]
    if len(ds) < 2: raise ValueError
    return T(f"Tìm ít nhất 2 tiếng có vần \"{v}\".", "Ví dụ: " + ", ".join(ds) + " ...", 1)


def tl_am(rng):
    ch = rng.sample(AM, 4)
    return T("Nêu âm đầu của mỗi tiếng sau: " + ", ".join(t for t, _ in ch), "; ".join(f"{t}: {a}" for t, a in ch), 1)


def tl_van_cua(rng):
    ch = rng.sample(VAN, 4)
    return T("Nêu vần của mỗi tiếng sau: " + ", ".join(t for t, _ in ch), "; ".join(f"{t}: {v}" for t, v in ch), 1)


def tl_tach(rng):
    # tách tiếng thành âm đầu + vần (chỉ lấy tiếng có trong cả hai bảng)
    am = dict(AM); van = dict(VAN)
    chung = [t for t in am if t in van]
    if len(chung) < 3: raise ValueError
    ch = rng.sample(chung, 3)
    return T("Tách mỗi tiếng sau thành âm đầu và vần: " + ", ".join(ch), "; ".join(f"{t} = {am[t]} + {van[t]}" for t in ch), 2)

# ---------------------------------------------------------------- 2. Dấu thanh
TONE = ["không dấu", "dấu huyền", "dấu sắc", "dấu hỏi", "dấu ngã", "dấu nặng"]
CO_SO = ["ba", "ma", "la", "ca", "ta", "ha", "xa", "ga", "ve", "me", "be", "co", "bo", "to", "ho", "mo"]
DANH = {"a": "aàáảãạ", "e": "eèéẻẽẹ", "o": "oòóỏõọ"}
FORM = {b: [b[:-1] + DANH[b[-1]][i] for i in range(6)] for b in CO_SO}


def mc_them_dau(rng):
    b = rng.choice(CO_SO); i = rng.randint(1, 5)
    f = FORM[b]
    return M(f"Thêm {TONE[i]} vào tiếng \"{b}\" được tiếng:", f[i], _tron(rng, f[i], f), 1)


def mc_dau_cua(rng):
    b = rng.choice(CO_SO); i = rng.randint(0, 5)
    t = FORM[b][i]
    return M(f"Tiếng \"{t}\" có dấu thanh nào?", TONE[i], _tron(rng, TONE[i], TONE), 1)


def mc_tieng_dau(rng):
    b = rng.choice(CO_SO); i = rng.randint(1, 5)
    ten = TONE[i]
    khac = [FORM[bb][j] for bb in CO_SO for j in range(6) if j != i]
    return M(f"Tiếng nào dưới đây có {ten}?", FORM[b][i], _tron(rng, FORM[b][i], khac), 1)


def tl_nam_dau(rng):
    b = rng.choice(CO_SO)
    return T(f"Thêm các dấu thanh vào tiếng \"{b}\" để được các tiếng khác nhau.", ", ".join(FORM[b]), 1)


def tl_dau_ten(rng):
    cs = rng.sample(CO_SO, 3)
    ch = [(FORM[b][i := rng.randint(1, 5)], TONE[i]) for b in cs]
    return T("Nêu dấu thanh của các tiếng: " + ", ".join(t for t, _ in ch), "; ".join(f"{t}: {d}" for t, d in ch), 1)


def tl_viet_dau(rng):
    cs = rng.sample(CO_SO, 3)
    ch = [(b, rng.randint(1, 5)) for b in cs]
    return T("Thêm dấu thanh cho đúng: " + "; ".join(f"{b} + {TONE[i]}" for b, i in ch), "; ".join(FORM[b][i] for b, i in ch), 1)

# ---------------------------------------------------------------- 3. Chính tả c/k, g/gh, ng/ngh
DUNGSAI = [
    ("ghế", ["gế", "ngế", "nghế"]), ("nghỉ", ["ngỉ", "ghỉ", "cỉ"]), ("nghĩ", ["ngĩ", "ghĩ", "cĩ"]),
    ("kính", ["cính", "ghính", "nghính"]), ("kéo", ["céo", "ghéo", "nghéo"]), ("kem", ["cem", "ghem", "nghem"]),
    ("kể", ["cể", "ghể", "nghể"]), ("gà", ["ghà", "nghà", "kà"]), ("gỗ", ["ghỗ", "nghỗ", "kỗ"]),
    ("gạo", ["ghạo", "nghạo", "kạo"]), ("ngô", ["nghô", "ghô", "kô"]), ("ngủ", ["nghủ", "ghủ", "kủ"]),
    ("ngựa", ["nghựa", "ghựa", "kựa"]), ("cá", ["ká", "ghá", "nghá"]), ("cổ", ["kổ", "ghổ", "nghổ"]),
    ("cờ", ["kờ", "ghờ", "nghờ"]), ("cây", ["kây", "ghây", "nghây"]), ("cua", ["kua", "ghua", "nghua"]),
    ("cơm", ["kơm", "ghơm", "nghơm"]), ("cửa", ["kửa", "ghửa", "nghửa"]), ("kết", ["cết", "ghết", "nghết"]),
    ("kiểm", ["ciểm", "ghiểm", "nghiểm"]), ("nghe", ["nge", "ngge", "ngghe"])
]
DIEN = [
    ("_á", "c", ["k", "gh", "ngh"]), ("_ổ", "c", ["k", "gh", "ngh"]), ("_ờ", "c", ["k", "gh", "ngh"]),
    ("_ây", "c", ["k", "gh", "ngh"]), ("_ua", "c", ["k", "gh", "ngh"]), ("_ơm", "c", ["k", "gh", "ngh"]),
    ("_ửa", "c", ["k", "gh", "ngh"]), ("_ầu", "c", ["k", "gh", "ngh"]),
    ("_éo", "k", ["c", "gh", "ngh"]), ("_em", "k", ["c", "gh", "ngh"]), ("_ính", "k", ["c", "gh", "ngh"]),
    ("_ể", "k", ["c", "gh", "ngh"]), ("_ết", "k", ["c", "gh", "ngh"]), ("_ẹp", "k", ["c", "gh", "ngh"]),
    ("_iểm", "k", ["c", "gh", "ngh"]),
    ("_ế", "gh", ["g", "ng", "ngh"]), ("_ép", "gh", ["g", "ng", "ngh"]), ("_ét", "gh", ["g", "ng", "ngh"]),
    ("_im", "gh", ["g", "ng", "ngh"]),
    ("_à", "g", ["gh", "ngh", "k"]), ("_ỗ", "g", ["gh", "ngh", "k"]), ("_ạo", "g", ["gh", "ngh", "k"]),
    ("_ạch", "g", ["gh", "ngh", "k"]), ("_ấu", "g", ["gh", "ngh", "k"]), ("_ối", "g", ["gh", "ngh", "k"]),
    ("_ió", "g", ["gh", "ngh", "k"]), ("_ửi", "g", ["gh", "ngh", "k"]),
    ("_ã", "ng", ["ngh", "gh", "k"]), ("_ô", "ng", ["ngh", "gh", "k"]), ("_ủ", "ng", ["ngh", "gh", "k"]),
    ("_ọt", "ng", ["ngh", "gh", "k"]), ("_ón", "ng", ["ngh", "gh", "k"]), ("_ỗng", "ng", ["ngh", "gh", "k"]),
    ("_ựa", "ng", ["ngh", "gh", "k"]), ("_ày", "ng", ["ngh", "gh", "k"]),
    ("_e", "ngh", ["ng", "c", "p"]), ("_ỉ", "ngh", ["ng", "c", "p"]), ("_ĩ", "ngh", ["ng", "c", "p"]),
    ("_ề", "ngh", ["ng", "c", "p"]), ("_ệ", "ngh", ["ng", "c", "p"]), ("_ìn", "ngh", ["ng", "c", "p"]),
    ("_ịch", "ngh", ["ng", "c", "p"]),
]


def tl_dien_ck(rng):
    ch = rng.sample(DIEN, 5)
    return T("Điền c, k, g, gh, ng hoặc ngh vào chỗ trống:\n" + "; ".join(k for k, _, _ in ch), "; ".join(k.replace("_", d) for k, d, _ in ch), 1)


QUY_TAC = [
    ("Khi nào viết \"k\", khi nào viết \"c\"? Cho ví dụ.", "Viết \"k\" trước các chữ e, ê, i (kẻ, kể, kì). Viết \"c\" trước các chữ còn lại (cá, cổ, cờ)."),
    ("Khi nào viết \"gh\", khi nào viết \"g\"? Cho ví dụ.", "Viết \"gh\" trước các chữ e, ê, i (ghế, ghi, ghé). Viết \"g\" trước các chữ còn lại (gà, gỗ, gạo)."),
    ("Khi nào viết \"ngh\", khi nào viết \"ng\"? Cho ví dụ.", "Viết \"ngh\" trước các chữ e, ê, i (nghe, nghề, nghỉ). Viết \"ng\" trước các chữ còn lại (ngã, ngô, ngủ)."),
]
tl_quy_tac = tl_cur(QUY_TAC, 2)

# ---------------------------------------------------------------- 4. Từ chỉ sự vật
SV = {
    "con vật": ["con gà", "con vịt", "con chó", "con mèo", "con trâu", "con bò", "con cá", "con voi", "con khỉ", "con thỏ", "con ngựa", "con hổ", "con dê", "con ong", "con ếch"],
    "cây cối": ["cây chuối", "cây dừa", "cây bưởi", "cây cam", "cây xoài", "cây tre", "cây hoa hồng", "cây rau", "cây lúa", "cây na", "cây mít", "cây ổi"],
    "đồ vật": ["cái bàn", "cái ghế", "quyển vở", "cái bút", "cái cặp", "cái nồi", "cái bát", "cái đèn", "cái quạt", "cái gương", "chiếc xe", "cái tủ"],
    "người": ["bố", "mẹ", "ông", "bà", "anh", "chị", "em", "cô giáo", "bạn", "bác sĩ", "bác nông dân", "chú bộ đội"],
}
SV_HOI = {"con vật": "chỉ con vật", "cây cối": "chỉ cây cối", "đồ vật": "chỉ đồ vật", "người": "chỉ người"}
SV_NHAN = {"con vật": "chỉ con vật", "cây cối": "chỉ cây cối", "đồ vật": "chỉ đồ vật", "người": "chỉ người"}
SV_NHOM = {k: v for k, v in SV.items()}

# ---------------------------------------------------------------- 5. Từ chỉ hoạt động, đặc điểm
HD = {
    "hoạt động": ["chạy", "nhảy", "đọc", "viết", "hát", "múa", "ăn", "uống", "ngủ", "tưới cây", "quét nhà", "vẽ", "bơi", "leo", "học"],
    "đặc điểm": ["đỏ", "xanh", "cao", "thấp", "to", "nhỏ", "đẹp", "ngoan", "chăm chỉ", "thơm", "ngọt", "nhanh", "chậm", "sạch", "mềm"],
    "sự vật": ["quyển vở", "con mèo", "cái bàn", "cây cam", "bông hoa", "cái cặp", "chiếc xe", "con gà", "ngôi nhà", "dòng sông"],
}
HD_HOI = {"hoạt động": "chỉ hoạt động", "đặc điểm": "chỉ đặc điểm", "sự vật": "chỉ sự vật"}
HD_NHAN = {"hoạt động": "chỉ hoạt động", "đặc điểm": "chỉ đặc điểm", "sự vật": "chỉ sự vật", "khác": "chỉ tình cảm"}

# ---------------------------------------------------------------- 6. Trái nghĩa, đồng nghĩa đơn giản
TN = [("to", "nhỏ"), ("cao", "thấp"), ("dài", "ngắn"), ("nóng", "lạnh"), ("sáng", "tối"), ("nhanh", "chậm"), ("mới", "cũ"),
      ("đẹp", "xấu"), ("khóc", "cười"), ("vui", "buồn"), ("ngày", "đêm"), ("trên", "dưới"), ("trong", "ngoài"), ("già", "trẻ"),
      ("béo", "gầy"), ("nặng", "nhẹ"), ("mở", "đóng"), ("đúng", "sai"), ("ngoan", "hư"), ("sạch", "bẩn"), ("xa", "gần"), ("rộng", "hẹp")]
DN = [("mẹ", "má"), ("bố", "ba"), ("ngôi nhà", "căn nhà"), ("chăm chỉ", "siêng năng"), ("to lớn", "to"), ("xinh", "đẹp"),
      ("bé", "nhỏ"), ("nhìn", "xem"), ("nói", "bảo"), ("học sinh", "học trò")]
TN_NHAN = None

# ---------------------------------------------------------------- 7. Câu và dấu câu
CAU = [
    ("Em đi học.", "câu kể"), ("Mẹ nấu cơm.", "câu kể"), ("Bé chơi với mèo.", "câu kể"), ("Trời mưa to.", "câu kể"),
    ("Ông em trồng cây.", "câu kể"), ("Bạn tên là gì?", "câu hỏi"), ("Con đang làm gì đấy?", "câu hỏi"), ("Mẹ đi đâu rồi?", "câu hỏi"),
    ("Hôm nay là thứ mấy?", "câu hỏi"), ("Bạn có khoẻ không?", "câu hỏi"),
]
HOI_DAU = [("Bé đang ăn cơm", "."), ("Mẹ đi chợ", "."), ("Bạn tên là gì", "?"), ("Con đi đâu đấy", "?"), ("Trời nắng to", "."),
           ("Em học bài", "."), ("Bố làm việc ở đâu", "?"), ("Chim hót líu lo", "."), ("Hôm nay bạn có đi học không", "?"), ("Bà em kể chuyện", "."),
           ("Con mèo ở đâu", "?"), ("Em tưới cây", ".")]
SAP_XEP = [("em / đi / học", "Em đi học."), ("mẹ / nấu / cơm", "Mẹ nấu cơm."), ("bé / chơi / bóng", "Bé chơi bóng."), ("gà / ăn / thóc", "Gà ăn thóc."),
           ("bà / kể / chuyện", "Bà kể chuyện."), ("cô giáo / dạy / em", "Cô giáo dạy em."), ("chim / hót / líu lo", "Chim hót líu lo."),
           ("hoa / nở / đỏ rực", "Hoa nở đỏ rực."), ("bố / đọc / báo", "Bố đọc báo."), ("em / quét / nhà", "Em quét nhà.")]
VIET_HOA = [("hà nội", "Hà Nội"), ("việt nam", "Việt Nam"), ("lan", "Lan"), ("thái bình", "Thái Bình"), ("nam", "Nam"), ("hồ chí minh", "Hồ Chí Minh"),
            ("huế", "Huế"), ("đà nẵng", "Đà Nẵng"), ("minh", "Minh"), ("hải phòng", "Hải Phòng")]


def mc_dau_cuoi(rng):
    c, d = rng.choice(HOI_DAU)
    return M(f"Cuối câu \"{c}\" cần đặt dấu gì?", d, ["." if d == "?" else "?", ",", "!"], 1)


def mc_kieu(rng):
    c, k = rng.choice(CAU)
    return M(f"Câu \"{c}\" là câu gì?", k, ["câu hỏi" if k == "câu kể" else "câu kể", "câu cảm", "câu khiến"], 1)


def mc_sap(rng):
    from itertools import permutations
    x, d = rng.choice(SAP_XEP)
    ts = x.split(" / ")
    sai = []
    for p in permutations(ts):
        c = " ".join(p)
        c = c[0].upper() + c[1:] + "."
        if c != d:
            sai.append(c)
    if len(sai) < 3: raise ValueError
    return M("Sắp xếp các từ \"" + " - ".join(ts) + "\" thành câu đúng:", d, rng.sample(sai, 3), 2)


def mc_viet_hoa(rng):
    s, d = rng.choice(VIET_HOA)
    ts = s.split()
    sai = [" ".join(t.capitalize() if i == 0 else t for i, t in enumerate(ts)), s, " ".join(t.upper() for t in ts),
           " ".join(t if i == 0 else t.capitalize() for i, t in enumerate(ts))]
    sai = [x for x in dict.fromkeys(sai) if x != d]
    if len(sai) < 3: raise ValueError
    return M("Cách viết tên riêng nào đúng?", d, sai[:3], 1)


def tl_dau(rng):
    ch = rng.sample(HOI_DAU, 4)
    return T("Điền dấu chấm (.) hoặc dấu chấm hỏi (?) vào cuối câu:\n" + "\n".join(c for c, _ in ch), "\n".join(c + d for c, d in ch), 1)


def tl_sap(rng):
    ch = rng.sample(SAP_XEP, 3)
    return T("Sắp xếp các từ thành câu:\n" + "\n".join(f"{i + 1}. {x}" for i, (x, _) in enumerate(ch)), "\n".join(f"{i + 1}. {d}" for i, (_, d) in enumerate(ch)), 2)


def tl_viet_hoa(rng):
    ch = rng.sample(VIET_HOA, 4)
    return T("Viết hoa tên riêng cho đúng: " + ", ".join(s for s, _ in ch), "; ".join(f"{s} → {d}" for s, d in ch), 1)


CHU_DE = [
    ("Âm đầu, vần và tiếng", [mc_van_cua, mc_tieng_van, mc_am_cua, mc_tieng_am], [tl_van, tl_am, tl_van_cua, tl_tach]),
    ("Dấu thanh", [mc_them_dau, mc_dau_cua, mc_tieng_dau], [tl_nam_dau, tl_dau_ten, tl_viet_dau]),
    ("Chính tả: c/k, g/gh, ng/ngh",
     [mc_dungsai(DUNGSAI, ["Chữ nào viết đúng chính tả?", "Tiếng nào viết đúng chính tả?"]), mc_dien_am(DIEN, "Điền chữ thích hợp vào chỗ trống:")],
     [tl_dien_ck, tl_quy_tac, tl_dungsai(DUNGSAI, "Các chữ sau viết sai chính tả, hãy sửa lại:", 4, 1)]),
    ("Từ chỉ sự vật",
     [mc_nhom(SV_NHOM, SV_HOI), mc_nhan(SV_NHOM, SV_NHAN)],
     [tl_nhom(SV_NHOM, {k: "Từ " + v for k, v in SV_HOI.items()}, "Xếp các từ sau vào nhóm thích hợp:", 2, 3, 1), tl_nhom(SV_NHOM, {k: "Từ " + v for k, v in SV_HOI.items()}, "Gạch chân các từ chỉ con vật, cây cối, đồ vật, người trong các từ sau:", 3, 2, 1)]),
    ("Từ chỉ hoạt động, đặc điểm",
     [mc_nhom(HD, HD_HOI), mc_nhan(HD, HD_NHAN)],
     [tl_nhom(HD, {k: "Từ " + v for k, v in HD_HOI.items()}, "Xếp các từ sau vào nhóm thích hợp:", 3, 2, 1)]),
    ("Từ trái nghĩa, đồng nghĩa đơn giản",
     [mc_cap(TN, "Từ trái nghĩa với \"{}\" là:"), mc_cap(DN, "Từ nào cùng nghĩa với \"{}\"?")],
     [tl_cap(TN, "Tìm từ trái nghĩa với các từ:", 3, 1), tl_cap(DN, "Tìm từ cùng nghĩa với các từ:", 3, 2)]),
    ("Câu và dấu câu",
     [mc_dau_cuoi, mc_kieu, mc_sap, mc_viet_hoa],
     [tl_dau, tl_sap, tl_viet_hoa]),
]
