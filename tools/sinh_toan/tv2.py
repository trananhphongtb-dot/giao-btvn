from tvcore import *
from tvcore import _tron
from tvdata import *
from tvdata2 import *
from tv1 import VIET_HOA, mc_viet_hoa, tl_viet_hoa

SV2 = ["con trâu", "dòng sông", "cánh đồng", "ngôi nhà", "quyển sách", "bông hoa", "cơn mưa", "ngọn núi", "mặt trời", "bầu trời",
       "cây bàng", "chiếc cặp", "cô giáo", "học sinh", "con đường", "ngôi trường", "bác sĩ", "người nông dân"]
HD2 = ["chạy", "nhảy", "đọc", "viết", "hát", "múa", "ngủ", "bơi", "leo", "trồng", "tưới", "gặt", "vẽ", "quét", "nấu", "kể", "giặt", "học"]
DD2 = ["đẹp", "xấu", "cao", "thấp", "xanh", "đỏ", "nhanh", "chậm", "ngoan", "chăm chỉ", "hiền lành", "vui vẻ", "rộng", "hẹp", "sạch sẽ", "thơm", "ngọt", "mềm mại"]
NH3 = {"sự vật": SV2, "hoạt động": HD2, "đặc điểm": DD2}
H3 = {"sự vật": "chỉ sự vật", "hoạt động": "chỉ hoạt động", "đặc điểm": "chỉ đặc điểm"}
N3 = {"sự vật": "chỉ sự vật", "hoạt động": "chỉ hoạt động", "đặc điểm": "chỉ đặc điểm", "khác": "chỉ thời gian"}
H3T = {k: "Từ " + v for k, v in H3.items()}

DS_CT = ["Em quét sân", "Bạn đang đọc sách gì", "Chà, bạn vẽ giỏi thật"]


def mc_dau_cuoi2(rng):
    c, d = rng.choice(DAU_CUOI)
    return M(f"Cuối câu \"{c}\" cần đặt dấu gì?", d, [x for x in [".", "?", "!", ","] if x != d], 1)


def mc_dau_phay(rng):
    c, _ = rng.choice(DAU_PHAY)
    d = c.replace("___", ",")
    sai = [c.replace("___", "."), c.replace("___", "?"), c.replace("___", "!")]
    return M("Câu nào dùng dấu phẩy đúng?", d, sai, 2)


def tl_dau_cuoi(rng):
    ch = rng.sample(DAU_CUOI, 5)
    return T("Điền dấu chấm (.), dấu chấm hỏi (?) hoặc dấu chấm than (!) vào cuối mỗi câu:\n" + "\n".join(c for c, _ in ch), "\n".join(c + d for c, d in ch), 2)


def tl_phay(rng):
    c, _ = rng.choice(DAU_PHAY)
    return T("Điền dấu phẩy vào chỗ trống: " + c.replace("___", " ... "), c.replace("___", ","), 2)


def mc_dung_ss(rng):
    d, _, _ = rng.choice(SO_SANH)
    return M("Câu nào có hình ảnh so sánh?", d, _tron(rng, d, KHONG_SS), 1)


def mc_ss_vat(rng):
    c, a, b = rng.choice(SO_SANH)
    khac = [x for _, _, x in SO_SANH if x != b]
    return M(f"Trong câu \"{c}\", {a} được so sánh với:", b, _tron(rng, b, khac), 2)


def mc_tu_ss(rng):
    c, a, b = rng.choice(SO_SANH)
    tu = "như"
    return M(f"Từ nào được dùng để so sánh trong câu \"{c}\"?", tu, ["và", "của", "nhưng"], 1)


def tl_ss_tim(rng):
    ch = rng.sample(SO_SANH, 3)
    return T("Tìm hình ảnh so sánh trong mỗi câu sau:\n" + "\n".join(f"{i + 1}. {c}" for i, (c, _, _) in enumerate(ch)), "\n".join(f"{i + 1}. {a} được so sánh với {b}" for i, (_, a, b) in enumerate(ch)), 2)


tl_ss_dat = tl_cur([
    ("Đặt một câu có hình ảnh so sánh về bông hoa.", "Ví dụ: Bông hoa đỏ như lửa."), ("Đặt một câu có hình ảnh so sánh về ông mặt trời.", "Ví dụ: Mặt trời tròn như quả bóng."),
    ("Đặt một câu có hình ảnh so sánh về dòng sông.", "Ví dụ: Dòng sông uốn lượn như dải lụa."), ("Đặt một câu có hình ảnh so sánh về mái tóc của bà.", "Ví dụ: Mái tóc bà trắng như bông.")], 2)


MC_TD = []
MC_TLV_2 = [
    ("Viết 3–4 câu giới thiệu về bản thân em.", "Em tên là Nam, học lớp 2A. Em thích vẽ tranh và đá bóng. Em rất yêu quý bố mẹ và ông bà. Em luôn cố gắng học thật giỏi."),
    ("Viết 3–4 câu giới thiệu về mẹ của em.", "Mẹ em là giáo viên tiểu học. Mẹ có mái tóc dài và nụ cười hiền. Mẹ rất yêu thương em và hay kể chuyện cho em nghe. Em yêu mẹ nhiều lắm."),
    ("Viết 3–4 câu về một con vật nuôi mà em yêu thích.", "Nhà em nuôi một chú mèo tên là Mun. Bộ lông nó đen mượt như nhung. Mun rất thích nằm phơi nắng và bắt chuột. Em rất quý Mun."),
    ("Viết 3–4 câu về cô giáo (hoặc thầy giáo) của em.", "Cô giáo em tên là cô Hoa. Cô dạy em đọc, viết và làm toán. Cô giảng bài rất dễ hiểu và luôn nhẹ nhàng với học sinh. Em rất kính yêu cô."),
    ("Viết 3–4 câu tả một đồ dùng học tập em thích (cái bút, cái cặp, ...).", "Em có một chiếc cặp màu xanh. Cặp có hai ngăn rộng để đựng sách vở. Em luôn giữ cặp sạch sẽ. Chiếc cặp là người bạn đồng hành của em mỗi ngày đến trường."),
    ("Viết 3–4 câu giới thiệu về một người bạn thân của em.", "Bạn thân nhất của em là Minh. Minh học cùng lớp và ngồi cạnh em. Bạn ấy vui tính và hay giúp đỡ mọi người. Em rất quý Minh."),
    ("Viết 3–4 câu kể về một việc em đã làm để giúp đỡ người khác.", "Hôm qua, em thấy bà nhặt rau ngoài sân. Em chạy ra giúp bà nhặt rau. Bà khen em ngoan và xoa đầu em. Em rất vui vì đã giúp được bà."),
    ("Viết 3–4 câu tả một cây mà em thường thấy ở sân trường (hoặc ở nhà).", "Sân trường em có một cây bàng rất to. Thân cây sần sùi, tán lá xòe rộng che mát cả góc sân. Mùa hè, chúng em thường ngồi chơi dưới gốc bàng. Em rất yêu cây bàng ấy."),
    ("Viết 3–4 câu kể về một ngày chủ nhật của em.", "Sáng chủ nhật, em dậy sớm giúp mẹ dọn nhà. Buổi chiều, em làm bài tập rồi đi chơi với các bạn. Tối đến, cả nhà cùng ăn cơm vui vẻ. Em rất thích ngày chủ nhật."),
    ("Viết 3–4 câu cảm ơn cô giáo (hoặc người đã giúp đỡ em).", "Cô Hoa kính mến! Em cảm ơn cô đã dạy em đọc, viết và làm toán. Nhờ có cô, em tiến bộ nhiều. Em hứa sẽ chăm ngoan, học giỏi để cô vui lòng."),
    ("Viết 3–4 câu xin lỗi bạn vì lỡ làm hỏng đồ dùng của bạn.", "Bạn Lan ơi, mình xin lỗi vì đã làm gãy cái bút của bạn. Mình không cố ý đâu. Mình sẽ mua đền bạn cái bút mới nhé. Bạn đừng giận mình nhé!"),
]

CHU_DE = [
    ("Từ chỉ sự vật, hoạt động, đặc điểm",
     [mc_nhom(NH3, H3), mc_nhan(NH3, N3)],
     [tl_nhom(NH3, H3T, "Xếp các từ sau vào nhóm thích hợp:", 3, 2, 1), tl_nhom(NH3, H3T, "Gạch chân và phân loại các từ sau:", 2, 3, 1), tl_nhom(NH3, H3T, "Chọn từ thích hợp xếp vào mỗi nhóm:", 3, 3, 2)]),
    ("Từ cùng nghĩa, từ trái nghĩa",
     [mc_cap(TRAI, "Từ trái nghĩa với \"{}\" là:"), mc_cap(DONG, "Từ nào cùng nghĩa với \"{}\"?")],
     [tl_cap(TRAI, "Tìm từ trái nghĩa với các từ:", 3, 1), tl_cap(DONG, "Tìm từ cùng nghĩa với các từ:", 3, 2)]),
    ("Chính tả: ch/tr, s/x, l/n",
     [mc_cs_nhom(CH_TR, ("ch", "tr")), mc_cs_nhom(S_X, ("s", "x")), mc_cs_nhom(L_N, ("l", "n")),
      mc_cs_dien(CH_TR, ("ch", "tr"), ["ch", "tr", "kh", "nh"]), mc_cs_dien(S_X, ("s", "x"), ["s", "x", "ch", "tr"])],
     [tl_cs_dien(CH_TR, ("ch", "tr"), "Điền ch hoặc tr vào chỗ trống:", 4, 1), tl_cs_dien(S_X, ("s", "x"), "Điền s hoặc x vào chỗ trống:", 4, 1),
      tl_cs_dien(L_N, ("l", "n"), "Điền l hoặc n vào chỗ trống:", 4, 1), tl_cs_sua(CH_TR, ("ch", "tr"), "Viết lại cho đúng chính tả:", 4, 2), tl_cs_sua(S_X, ("s", "x"), "Viết lại cho đúng chính tả:", 4, 2)]),
    ("Câu: Ai là gì? Ai làm gì? Ai thế nào?",
     [mc_cau_nhan(CAU3, LABEL3, "Câu \"{c}\" thuộc kiểu câu nào?"),
      mc_cau_chon(CAU3, "Ai làm gì?", "Câu nào thuộc kiểu câu Ai làm gì?", 1), mc_cau_chon(CAU3, "Ai thế nào?", "Câu nào thuộc kiểu câu Ai thế nào?", 1),
      mc_cau_chon(CAU3, "Ai là gì?", "Câu nào thuộc kiểu câu Ai là gì?", 1)],
     [tl_cau_nhan(CAU3, "Xác định kiểu câu (Ai là gì?, Ai làm gì?, Ai thế nào?) của mỗi câu sau:", 4, 2),
      tl_cur([("Đặt một câu theo mẫu Ai làm gì? nói về mẹ em.", "Ví dụ: Mẹ em nấu cơm."), ("Đặt một câu theo mẫu Ai làm gì? nói về bạn em.", "Ví dụ: Bạn Lan đang đọc sách."),
              ("Đặt một câu theo mẫu Ai thế nào? nói về con mèo.", "Ví dụ: Con mèo rất lười."), ("Đặt một câu theo mẫu Ai thế nào? nói về bầu trời.", "Ví dụ: Bầu trời hôm nay trong xanh."),
              ("Đặt một câu theo mẫu Ai là gì? nói về em.", "Ví dụ: Em là học sinh lớp 2."), ("Đặt một câu theo mẫu Ai là gì? nói về bố em.", "Ví dụ: Bố em là bác sĩ."),
              ("Đặt một câu theo mẫu Ai làm gì? nói về cô giáo.", "Ví dụ: Cô giáo giảng bài."), ("Đặt một câu theo mẫu Ai thế nào? nói về bông hoa.", "Ví dụ: Bông hoa rất thơm.")], 2)]),
    ("Dấu câu và viết hoa tên riêng",
     [mc_dau_cuoi2, mc_dau_phay, mc_viet_hoa],
     [tl_dau_cuoi, tl_phay, tl_viet_hoa]),
    ("Hình ảnh so sánh",
     [mc_dung_ss, mc_ss_vat, mc_tu_ss],
     [tl_ss_tim, tl_ss_dat]),
    ("Thành ngữ, tục ngữ",
     [mc_dien_tu(TN_DIEN, "Chọn từ thích hợp điền vào chỗ trống:", 1), mc_nghia(TUC_NGU[:8], "Câu tục ngữ \"{x}\" khuyên chúng ta điều gì?", 2, TUC_NHOM)],
     [tl_dien_tu(TN_DIEN, "Điền từ thích hợp vào chỗ trống:", 4, 1), tl_cur([(f"Em hiểu câu \"{x}\" như thế nào?", n) for x, n in TUC_NGU[:8]], 2)]),
    ("Tập làm văn: viết đoạn văn ngắn", [], [tl_cur(MC_TLV_2, 2)], {"n_mc": 0}),
]
