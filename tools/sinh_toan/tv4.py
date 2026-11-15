from tvcore import *
from tvcore import _tron
from tvdata import *
from tvdata2 import *
from tv3 import mc_chuc_nang, tl_chuc_nang

# (tiếng, âm đầu, vần, thanh)
CAU_TAO = [("nước", "n", "ươc", "sắc"), ("non", "n", "on", "ngang"), ("sông", "s", "ông", "ngang"), ("núi", "n", "ui", "sắc"), ("trăng", "tr", "ăng", "ngang"),
           ("chăm", "ch", "ăm", "ngang"), ("học", "h", "oc", "nặng"), ("sách", "s", "ach", "sắc"), ("hoa", "h", "oa", "ngang"), ("quả", "qu", "a", "hỏi"),
           ("thương", "th", "ương", "ngang"), ("mẹ", "m", "e", "nặng"), ("cá", "c", "a", "sắc"), ("gà", "g", "a", "huyền"), ("nghe", "ngh", "e", "ngang"),
           ("trời", "tr", "ơi", "huyền"), ("đất", "đ", "ât", "sắc"), ("rừng", "r", "ưng", "huyền"), ("mưa", "m", "ưa", "ngang"), ("thuyền", "th", "uyên", "huyền"),
           ("giỏi", "gi", "oi", "hỏi"), ("khoẻ", "kh", "oe", "hỏi"), ("vui", "v", "ui", "ngang"), ("bàn", "b", "an", "huyền"), ("lá", "l", "a", "sắc"), ("chim", "ch", "im", "ngang")]
_AM = sorted({a for _, a, _, _ in CAU_TAO})
_VAN = sorted({v for _, _, v, _ in CAU_TAO})
_TH = ["ngang", "huyền", "sắc", "hỏi", "ngã", "nặng"]


def mc_cau_tao(rng):
    t, a, v, th = rng.choice(CAU_TAO)
    dung = f"âm đầu \"{a}\", vần \"{v}\", thanh {th}"
    sai = [f"âm đầu \"{a}\", vần \"{v}\", thanh {rng.choice([x for x in _TH if x != th])}",
           f"âm đầu \"{a}\", vần \"{rng.choice([x for x in _VAN if x != v])}\", thanh {th}",
           f"âm đầu \"{rng.choice([x for x in _AM if x != a])}\", vần \"{v}\", thanh {th}"]
    return M(f"Tiếng \"{t}\" có cấu tạo gồm:", dung, sai, 2)


def mc_thanh(rng):
    t, _, _, th = rng.choice(CAU_TAO)
    return M(f"Tiếng \"{t}\" có thanh gì?", th, _tron(rng, th, _TH), 1)


def mc_van4(rng):
    t, _, v, _ = rng.choice(CAU_TAO)
    return M(f"Phần vần của tiếng \"{t}\" là:", v, _tron(rng, v, _VAN), 2)


def mc_am4(rng):
    t, a, _, _ = rng.choice(CAU_TAO)
    return M(f"Phần âm đầu của tiếng \"{t}\" là:", a, _tron(rng, a, _AM), 1)


def tl_cau_tao(rng):
    ch = rng.sample(CAU_TAO, 3)
    return T("Phân tích cấu tạo của các tiếng sau (âm đầu, vần, thanh): " + ", ".join(t for t, _, _, _ in ch), "\n".join(f"{t}: âm đầu {a}, vần {v}, thanh {th}" for t, a, v, th in ch), 2)


def tl_khuyet(rng):
    return T("Cho biết tiếng \"yêu\" có những bộ phận nào? Vì sao nói tiếng nào cũng phải có vần và thanh?", "Tiếng \"yêu\" gồm vần \"yêu\" và thanh ngang (không có âm đầu). Mỗi tiếng bắt buộc phải có vần và thanh; âm đầu thì có tiếng không có.", 3)


DON = ["bàn", "ghế", "đi", "chạy", "nhà", "hoa", "mưa", "xanh", "cao", "học", "vở", "sách", "sông", "núi", "trời", "đất"]
TU3 = {"từ ghép": GHEP, "từ láy": LAY, "từ đơn": DON}
H_TU3 = {"từ ghép": "là từ ghép", "từ láy": "là từ láy", "từ đơn": "là từ đơn"}
N_TU3 = {"từ ghép": "từ ghép", "từ láy": "từ láy", "từ đơn": "từ đơn", "khác": "thành ngữ"}
H_TU3_T = {"từ ghép": "Từ ghép", "từ láy": "Từ láy", "từ đơn": "Từ đơn"}


def mc_tu_nhan(rng):
    k = rng.choice(["từ ghép", "từ láy", "từ đơn"])
    w = rng.choice(TU3[k])
    return M(f"Từ \"{w}\" thuộc loại từ nào?", N_TU3[k], _tron(rng, N_TU3[k], list(N_TU3.values())), 2)


def tl_tim_lay(rng):
    return T(rng.choice(["Tìm 5 từ láy tả tiếng mưa hoặc tiếng gió.", "Tìm 5 từ láy tả dáng đi của người.", "Tìm 5 từ láy tả màu sắc."]),
             "Ví dụ: rì rào, lao xao, xào xạc, tí tách, thì thầm / lom khom, thập thò, khấp khểnh, lững thững, thoăn thoắt / đo đỏ, xanh xanh, vàng vàng, tim tím, hồng hồng", 2)


def tl_ghep_lay(rng):
    ch = rng.sample(GHEP, 3) + rng.sample(LAY, 3)
    rng.shuffle(ch)
    return T("Xếp các từ sau vào hai nhóm: từ ghép, từ láy.\n" + ", ".join(ch), f"Từ ghép: {', '.join(w for w in ch if w in GHEP)}\nTừ láy: {', '.join(w for w in ch if w in LAY)}", 2)


# ---- từ loại ---------------------------------------------------------------------
TL3 = {"danh từ": DT, "động từ": DGT, "tính từ": TT}
H_TL = {"danh từ": "là danh từ", "động từ": "là động từ", "tính từ": "là tính từ"}
H_TL_T = {"danh từ": "Danh từ", "động từ": "Động từ", "tính từ": "Tính từ"}
N_TL = {"danh từ": "danh từ", "động từ": "động từ", "tính từ": "tính từ", "khác": "quan hệ từ"}

# ---- danh từ riêng/chung ----------------------------------------------------------
TL_RC = {"danh từ riêng": DT_RIENG, "danh từ chung": DT_CHUNG}
H_RC = {"danh từ riêng": "là danh từ riêng", "danh từ chung": "là danh từ chung"}
N_RC = {"danh từ riêng": "danh từ riêng", "danh từ chung": "danh từ chung", "a": "động từ", "b": "tính từ"}


def mc_rc_nhan(rng):
    k = rng.choice(list(TL_RC))
    w = rng.choice(TL_RC[k])
    return M(f"Từ \"{w}\" là:", N_RC[k], _tron(rng, N_RC[k], list(N_RC.values())), 1)


def mc_viet_hoa4(rng):
    w = rng.choice(DT_RIENG)
    ts = w.split()
    sai = [w.lower(), " ".join(t if i == 0 else t.lower() for i, t in enumerate(ts)), w.upper()]
    sai = [x for x in dict.fromkeys(sai) if x != w]
    if len(sai) < 3:
        raise ValueError
    return M("Cách viết tên riêng nào đúng quy tắc viết hoa?", w, sai, 1)


def tl_viet_hoa4(rng):
    ch = rng.sample(DT_RIENG, 5)
    return T("Viết hoa lại cho đúng các danh từ riêng sau: " + ", ".join(w.lower() for w in ch), "; ".join(ch), 1)


def tl_tim_dt(rng):
    return T(rng.choice(["Tìm 3 danh từ riêng chỉ tên tỉnh, thành phố ở nước ta.", "Tìm 3 danh từ riêng chỉ tên sông, núi.", "Tìm 3 danh từ riêng chỉ tên người."]),
             "Ví dụ: Hà Nội, Đà Nẵng, Thái Bình / sông Hồng, sông Cửu Long, núi Trường Sơn / Nguyễn Du, Trần Hưng Đạo, Lê Lợi", 1)


# ---- kiểu câu ---------------------------------------------------------------------
# ---- chủ ngữ, vị ngữ --------------------------------------------------------------
def mc_cn(rng):
    c, cn, vn = rng.choice(CN_VN)
    khac = [x[1] for x in CN_VN if x[0] != c] + [vn]
    return M(f"Chủ ngữ của câu \"{c}\" là:", cn, _tron(rng, cn, khac), 2)


def mc_vn(rng):
    c, cn, vn = rng.choice(CN_VN)
    khac = [x[2] for x in CN_VN if x[0] != c] + [cn]
    return M(f"Vị ngữ của câu \"{c}\" là:", vn, _tron(rng, vn, khac), 2)


def tl_cn_vn(rng):
    ch = rng.sample(CN_VN, 3)
    return T("Xác định chủ ngữ và vị ngữ của mỗi câu sau:\n" + "\n".join(f"{i + 1}. {c}" for i, (c, _, _) in enumerate(ch)), "\n".join(f"{i + 1}. CN: {cn} | VN: {vn}" for i, (_, cn, vn) in enumerate(ch)), 2)


tl_dat_cau = tl_cur([
    ("Đặt một câu có chủ ngữ là \"Chú mèo\".", "Ví dụ: Chú mèo nằm phơi nắng."), ("Đặt một câu có vị ngữ là \"đang đọc sách\".", "Ví dụ: Bạn Nam đang đọc sách."),
    ("Đặt một câu có chủ ngữ là \"Những bông hoa\".", "Ví dụ: Những bông hoa nở rực rỡ trong vườn."), ("Đặt một câu có vị ngữ là \"chạy rất nhanh\".", "Ví dụ: Con ngựa chạy rất nhanh."),
    ("Đặt một câu có chủ ngữ là \"Bố em\".", "Ví dụ: Bố em làm việc ở nhà máy."), ("Đặt một câu có vị ngữ là \"hót líu lo trên cành cây\".", "Ví dụ: Những chú chim hót líu lo trên cành cây.")], 2)


def tl_kieu(rng):
    ch = rng.sample(KIEU4, 4)
    return T("Xác định kiểu câu (câu kể, câu hỏi, câu cảm, câu khiến) của mỗi câu sau:\n" + "\n".join(f"{i + 1}. {c}" for i, (c, _) in enumerate(ch)), "\n".join(f"{i + 1}. {l}" for i, (_, l) in enumerate(ch)), 2)


tl_dat_kieu = tl_cur([
    ("Đặt một câu hỏi để hỏi bạn về bài tập về nhà.", "Ví dụ: Bạn đã làm xong bài tập về nhà chưa?"), ("Đặt một câu cảm để bày tỏ cảm xúc trước cảnh đẹp.", "Ví dụ: Cảnh đẹp quá!"),
    ("Đặt một câu khiến để nhờ bạn cho mượn cái bút.", "Ví dụ: Bạn cho mình mượn cái bút nhé!"), ("Đặt một câu kể nói về việc em làm vào buổi sáng.", "Ví dụ: Sáng nay em dậy sớm tập thể dục."),
    ("Đặt một câu hỏi để hỏi thăm sức khỏe của bà.", "Ví dụ: Bà có khỏe không ạ?"), ("Đặt một câu cảm để khen bạn vẽ đẹp.", "Ví dụ: Bạn vẽ đẹp quá!"),
    ("Đặt một câu khiến để nhắc các bạn giữ trật tự.", "Ví dụ: Các bạn hãy giữ trật tự nhé!")], 2)


TLV4 = [
    ("Lập dàn ý và viết mở bài, kết bài cho bài văn tả một cây bóng mát ở sân trường em.", "Dàn ý: Mở bài: giới thiệu cây (cây gì, ở đâu). Thân bài: tả bao quát (cao, tán lá), tả chi tiết (gốc, thân, cành, lá, hoa, quả), hoạt động của người và vật quanh cây theo mùa. Kết bài: tình cảm của em với cây.\nVí dụ mở bài: Giữa sân trường em có một cây phượng vĩ rất lớn."),
    ("Lập dàn ý cho bài văn tả một con vật nuôi mà em yêu thích.", "Dàn ý: Mở bài: giới thiệu con vật (tên, nuôi từ khi nào). Thân bài: tả hình dáng (bộ lông, đầu, mắt, chân, đuôi), hoạt động (ăn, chơi, quen người), tính nết. Kết bài: tình cảm của em với con vật."),
    ("Lập dàn ý cho bài văn tả một đồ dùng học tập (hoặc một đồ vật) em yêu thích.", "Dàn ý: Mở bài: giới thiệu đồ vật, ai tặng, dùng từ bao giờ. Thân bài: tả hình dáng, màu sắc, chất liệu, các bộ phận, công dụng, cách em giữ gìn. Kết bài: tình cảm của em với đồ vật."),
    ("Lập dàn ý cho bài văn tả cảnh buổi sáng ở sân trường (hoặc ở quê em).", "Dàn ý: Mở bài: giới thiệu thời gian, địa điểm. Thân bài: tả bầu trời, ánh nắng, cây cối, âm thanh, hoạt động của mọi người theo trình tự thời gian. Kết bài: cảm nghĩ của em về cảnh buổi sáng."),
    ("Lập dàn ý cho bài văn kể về một việc làm tốt của em.", "Dàn ý: Mở bài: giới thiệu việc tốt (ở đâu, khi nào). Thân bài: diễn biến (nguyên nhân, em đã làm gì, lời nói, việc làm của những người liên quan). Kết bài: kết quả và bài học em rút ra."),
    ("Lập dàn ý cho bài văn kể về một kỉ niệm đáng nhớ của em với bạn bè (hoặc người thân).", "Dàn ý: Mở bài: nêu kỉ niệm định kể. Thân bài: hoàn cảnh, diễn biến theo thứ tự thời gian, cảm xúc của em. Kết bài: ý nghĩa của kỉ niệm đó."),
    ("Lập dàn ý cho bài văn tả cô giáo (hoặc thầy giáo) của em.", "Dàn ý: Mở bài: giới thiệu cô giáo (tên, dạy lớp mấy). Thân bài: tả ngoại hình (dáng người, khuôn mặt, mái tóc, giọng nói), tính tình, việc làm khi dạy học và quan tâm học sinh. Kết bài: tình cảm của em với cô."),
    ("Viết thư (khoảng 8 câu) gửi một người bạn ở xa để hỏi thăm và kể về lớp em.", "Gợi ý: đầu thư (địa điểm, ngày tháng, lời xưng hô); nội dung (hỏi thăm bạn, kể việc học tập, vui chơi ở lớp, mời bạn về chơi); cuối thư (lời chúc, hẹn gặp lại, kí tên).\nVí dụ: Thái Bình, ngày ... tháng ... năm ... Hoa thân mến! Lâu rồi mình không gặp bạn..."),
    ("Kể lại ngắn gọn một câu chuyện cổ tích mà em thích bằng lời của em.", "Gợi ý: nêu tên truyện; kể theo ba phần: mở đầu (nhân vật, hoàn cảnh), diễn biến chính (sự việc nối tiếp nhau), kết thúc (kết quả, bài học). Dùng lời văn của mình, không chép nguyên văn."),
    ("Lập dàn ý cho bài văn tả một đồ chơi (hoặc món quà) em được tặng.", "Dàn ý: Mở bài: ai tặng, vào dịp nào. Thân bài: tả hình dáng, màu sắc, các bộ phận, cách chơi, điều em thích. Kết bài: tình cảm và cách em giữ gìn món quà."),
]


DAU_KT = [
    ("Điền dấu thích hợp vào chỗ trống: Mẹ dặn em ___ “Con nhớ khóa cửa nhé!”", ":", [",", "…", "?"]),
    ("Điền dấu thích hợp vào chỗ trống: Nhà em nuôi nhiều con vật ___ gà, vịt, lợn, chó.", ":", [",", ".", "!"]),
    ("Điền dấu thích hợp vào chỗ trống: Lan hỏi bạn ___ “Bạn đã ăn sáng chưa?”", ":", [",", ".", "!"]),
    ("Điền dấu thích hợp vào chỗ trống: Cô giáo nói với cả lớp ___ “Các em hãy trật tự nào!”", ":", [",", "?", "…"]),
    ("Để dẫn lời nói trực tiếp của nhân vật, sau dấu hai chấm ta thường đặt lời nói trong dấu nào?", "dấu ngoặc kép", ["dấu ngoặc đơn", "dấu chấm lửng", "dấu chấm phẩy"]),
    ("Dấu gạch ngang đặt ở đầu dòng trong đoạn đối thoại dùng để làm gì?", "Đánh dấu chỗ bắt đầu lời nói của nhân vật", ["Kết thúc câu hỏi", "Ngăn cách các từ cùng loại", "Báo hiệu phần liệt kê"]),
    ("Dấu ngoặc kép được dùng trong trường hợp nào sau đây?", "Dẫn lời nói trực tiếp của người khác", ["Kết thúc câu kể", "Ngăn cách các bộ phận cùng loại", "Kết thúc câu hỏi"]),
    ("Dấu hai chấm được dùng trong trường hợp nào sau đây?", "Báo hiệu phần liệt kê, giải thích hoặc lời nói trực tiếp", ["Kết thúc câu hỏi", "Kết thúc câu cảm", "Đánh dấu tên người"]),
    ("Dấu nào dùng để đánh dấu tên bài thơ, tên truyện khi nhắc lại trong câu?", "dấu ngoặc kép", ["dấu hai chấm", "dấu phẩy", "dấu chấm hỏi"]),
    ("Từ \"nhà thơ nhỏ\" trong câu \"Cả lớp gọi Nam là nhà thơ nhỏ\" được dùng với nghĩa đặc biệt, cần đặt trong dấu nào?", "dấu ngoặc kép", ["dấu gạch ngang", "dấu hai chấm", "dấu chấm hỏi"]),
    ("Khi viết lời nói của hai người trong đối thoại, mỗi lời nói được viết ở đầu dòng và bắt đầu bằng dấu gì?", "dấu gạch ngang", ["dấu ngoặc kép", "dấu hai chấm", "dấu chấm phẩy"]),
    ("Trong câu \"Mẹ hỏi: “Con đã làm bài xong chưa?”\", dấu hai chấm đứng trước phần nào?", "Lời nói trực tiếp của mẹ", ["Phần liệt kê", "Phần chú thích", "Tên tác phẩm"]),
]

CHU_DE = [
    ("Cấu tạo của tiếng", [mc_cau_tao, mc_thanh, mc_van4, mc_am4], [tl_cau_tao, tl_khuyet]),
    ("Từ đơn, từ phức; từ ghép, từ láy",
     [mc_nhom(TU3, H_TU3), mc_tu_nhan],
     [tl_ghep_lay, tl_nhom(TU3, H_TU3_T, "Xếp các từ sau vào các nhóm thích hợp:", 3, 2, 2), tl_tim_lay]),
    ("Danh từ, động từ, tính từ",
     [mc_nhom(TL3, H_TL), mc_nhan(TL3, N_TL)],
     [tl_nhom(TL3, H_TL_T, "Xếp các từ sau vào các nhóm danh từ, động từ, tính từ:", 3, 3, 2), tl_nhom(TL3, H_TL_T, "Tìm danh từ, động từ, tính từ trong các từ sau:", 3, 2, 2)]),
    ("Danh từ chung, danh từ riêng và quy tắc viết hoa",
     [mc_nhom(TL_RC, H_RC), mc_rc_nhan, mc_viet_hoa4],
     [tl_nhom(TL_RC, {"danh từ riêng": "Danh từ riêng", "danh từ chung": "Danh từ chung"}, "Xếp các từ sau vào hai nhóm: danh từ chung, danh từ riêng:", 2, 4, 2), tl_viet_hoa4, tl_tim_dt]),
    ("Các kiểu câu: câu kể, câu hỏi, câu cảm, câu khiến",
     [mc_cau_nhan(KIEU4, LABEL4, "Câu \"{c}\" là kiểu câu nào?"), mc_cau_chon(KIEU4, "Câu kể", "Câu nào là câu kể?", 1), mc_cau_chon(KIEU4, "Câu hỏi", "Câu nào là câu hỏi?", 1),
      mc_cau_chon(KIEU4, "Câu cảm", "Câu nào là câu cảm?", 1), mc_cau_chon(KIEU4, "Câu khiến", "Câu nào là câu khiến?", 1)],
     [tl_kieu, tl_dat_kieu]),
    ("Chủ ngữ và vị ngữ", [mc_cn, mc_vn], [tl_cn_vn, tl_dat_cau]),
    ("Dấu hai chấm, ngoặc kép, gạch ngang", [mc_chuc_nang, mc_ktra(DAU_KT, 2)], [tl_chuc_nang, tl_cur([("Điền dấu câu thích hợp vào chỗ trống: Cô giáo hỏi ... \"Ai làm xong bài rồi?\"", "Cô giáo hỏi: “Ai làm xong bài rồi?”"), ("Điền dấu câu thích hợp: Nhà em có bốn người ... bố, mẹ, anh trai và em.", "Nhà em có bốn người: bố, mẹ, anh trai và em."), ("Viết lại câu sau có dùng dấu ngoặc kép để dẫn lời nói: Mẹ bảo em phải giữ gìn sức khỏe.", "Mẹ bảo em: “Con phải giữ gìn sức khỏe.”"), ("Viết một đoạn đối thoại ngắn (2 lượt lời) giữa hai bạn có dùng dấu gạch ngang.", "— Chiều nay cậu có đi đá bóng không? — Nam hỏi.\n— Có, mình đi cùng cậu nhé! — Hùng đáp."), ("Cho ví dụ về câu có dùng dấu hai chấm để liệt kê.", "Ví dụ: Trong cặp có đủ đồ dùng: sách, vở, bút và thước kẻ.")], 2)]),
    ("Chính tả: ch/tr, s/x, l/n, d/gi/r, hỏi/ngã",
     [mc_cs_nhom(CH_TR, ("ch", "tr")), mc_cs_nhom(S_X, ("s", "x")), mc_cs_nhom(L_N, ("l", "n")), mc_cs_nhom(D_GI_R, ("d", "gi", "r")), mc_cs_thanh(THANH)],
     [tl_cs_sua(CH_TR, ("ch", "tr"), "Viết lại cho đúng chính tả:", 5, 2), tl_cs_sua(S_X, ("s", "x"), "Viết lại cho đúng chính tả:", 5, 2), tl_cs_sua(L_N, ("l", "n"), "Viết lại cho đúng chính tả:", 5, 2),
      tl_cs_sua(D_GI_R, ("d", "gi", "r"), "Viết lại cho đúng chính tả:", 5, 2), tl_cs_thanh(THANH, "Sửa lỗi dấu hỏi/dấu ngã trong các từ sau:", 5, 2)]),
    ("Thành ngữ, tục ngữ",
     [mc_dien_tu(TN_DIEN, "Chọn từ thích hợp điền vào chỗ trống:", 1), mc_nghia(TUC_NGU, "Câu tục ngữ \"{x}\" khuyên chúng ta điều gì?", 2, TUC_NHOM), mc_nghia(THANH_NGU_NGHIA, "Thành ngữ \"{x}\" có nghĩa là gì?", 2)],
     [tl_dien_tu(TN_DIEN, "Điền từ thích hợp vào chỗ trống:", 4, 1), tl_cur([(f"Em hiểu câu \"{x}\" như thế nào? Cho một ví dụ về việc vận dụng.", n) for x, n in TUC_NGU], 2), tl_cur([(f"Giải thích thành ngữ \"{x}\" và đặt một câu có dùng thành ngữ này.", n) for x, n in THANH_NGU_NGHIA], 2)]),
    ("Tập làm văn: dàn ý và đoạn văn", [], [tl_cur(TLV4, 3)], {"n_mc": 0}),
]
