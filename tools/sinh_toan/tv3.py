from tvcore import *
from tvcore import _tron
from tvdata import *
from tvdata2 import *
from tv2 import mc_dung_ss, mc_ss_vat, mc_tu_ss, tl_ss_tim, mc_dau_cuoi2, tl_dau_cuoi, MC_TLV_2

NH4 = {"sự vật": ["con trâu", "dòng sông", "cánh đồng", "ngôi nhà", "quyển sách", "bông hoa", "ngọn núi", "bầu trời", "cây bàng", "ngôi trường", "chiếc cặp", "con đường"],
       "hoạt động": ["gặt lúa", "tưới cây", "nấu cơm", "kể chuyện", "chạy", "bơi", "nhảy dây", "quét nhà", "vẽ tranh", "đọc sách", "tập hát", "trồng cây"],
       "đặc điểm": ["xanh biếc", "rộng mênh mông", "thơm ngát", "chăm chỉ", "hiền lành", "nhanh nhẹn", "sạch sẽ", "rực rỡ", "mềm mại", "cao vút", "ngọt lịm", "yên tĩnh"],
       "tình cảm": ["yêu thương", "kính trọng", "biết ơn", "thân thiết", "quý mến", "tự hào", "lo lắng", "vui mừng", "nhớ nhung", "xúc động"]}
H4 = {"sự vật": "chỉ sự vật", "hoạt động": "chỉ hoạt động", "đặc điểm": "chỉ đặc điểm", "tình cảm": "chỉ tình cảm"}
H4T = {k: "Từ " + v for k, v in H4.items()}

NH_SV = {"Chú gà trống cất tiếng gáy chào buổi sáng.": "gà trống", "Cây bàng đứng lặng lẽ giữa sân trường.": "cây bàng",
         "Bác gió rì rào kể chuyện cho lá nghe.": "gió", "Mặt trời mỉm cười chào ngày mới.": "mặt trời", "Chị gió đưa chiếc diều bay cao.": "gió",
         "Cô mưa tắm mát cho cây cối.": "mưa", "Ông mặt trời thức dậy từ sớm.": "mặt trời", "Dòng sông thủ thỉ kể chuyện với bờ cát.": "dòng sông",
         "Chú mèo lười biếng nằm phơi nắng.": "con mèo", "Những chú ong chăm chỉ đi tìm mật hoa.": "những chú ong",
         "Bác bếp lửa đang thức suốt đêm.": "bếp lửa", "Cây tre bảo vệ làng xóm như người lính canh.": "cây tre"}


def mc_nhan_hoa(rng):
    d = rng.choice(NHAN_HOA)
    return M("Câu nào có hình ảnh nhân hóa?", d, _tron(rng, d, KHONG_NH), 1)


def mc_sv_nh(rng):
    c, sv = rng.choice(list(NH_SV.items()))
    khac = list(dict.fromkeys(NH_SV.values()))
    return M(f"Trong câu \"{c}\", sự vật nào được nhân hóa?", sv, _tron(rng, sv, [x for x in khac if x != sv]), 2)


def mc_phan_biet(rng):
    c = rng.choice(NHAN_HOA)
    return M(f"Câu \"{c}\" sử dụng biện pháp nghệ thuật nào?", "Nhân hóa", ["So sánh", "Liệt kê", "Điệp từ"], 2)


def mc_phan_biet2(rng):
    c, _, _ = rng.choice(SO_SANH)
    return M(f"Câu \"{c}\" sử dụng biện pháp nghệ thuật nào?", "So sánh", ["Nhân hóa", "Liệt kê", "Điệp từ"], 2)


def tl_nh_tim(rng):
    ch = rng.sample(NHAN_HOA, 3)
    return T("Tìm sự vật được nhân hóa trong mỗi câu sau:\n" + "\n".join(f"{i + 1}. {c}" for i, c in enumerate(ch)), "\n".join(f"{i + 1}. {NH_SV[c]}" for i, c in enumerate(ch)), 2)


def mc_hoi_bp(rng):
    c, bp, q = rng.choice(HOI_BP)
    khac = [x[2] for x in HOI_BP if x[0] != c]
    return M(f"Đặt câu hỏi cho bộ phận «{bp}» trong câu \"{c}\":", q, _tron(rng, q, khac), 2)


def tl_hoi_bp(rng):
    ch = rng.sample(HOI_BP, 3)
    return T("Đặt câu hỏi cho bộ phận được in đậm trong mỗi câu (bộ phận để trong dấu «»):\n" + "\n".join(f"{i + 1}. {c.replace(bp, '«' + bp + '»')}" for i, (c, bp, _) in enumerate(ch)), "\n".join(f"{i + 1}. {q}" for i, (_, _, q) in enumerate(ch)), 2)


CONFLICT = {"A": "CE", "C": "AE", "E": "AC"}


def mc_chuc_nang(rng):
    c, dau, k = rng.choice(DAU_CN)
    khac = [v for kk, v in CN_CHUC.items() if kk != k and kk not in CONFLICT.get(k, "")]
    return M(f"Dấu \"{dau.replace('dấu ', '')}\" trong câu \"{c}\" dùng để làm gì?", CN_CHUC[k], _tron(rng, CN_CHUC[k], khac), 2)


def tl_chuc_nang(rng):
    ch = rng.sample(DAU_CN, 3)
    return T("Nêu tác dụng của dấu câu trong mỗi câu sau:\n" + "\n".join(f"{i + 1}. {c}" for i, (c, _, _) in enumerate(ch)), "\n".join(f"{i + 1}. {d.capitalize()}: {CN_CHUC[k]}" for i, (_, d, k) in enumerate(ch)), 2)


def tl_dien_dau(rng):
    return T("Điền dấu câu thích hợp (dấu phẩy, dấu chấm, dấu chấm hỏi, dấu chấm than) vào chỗ trống:\n" + rng.choice([
        "Mùa xuân ... cây cối đâm chồi nảy lộc ...", "Bạn có thích đọc truyện không ...", "Ôi ... cảnh đẹp quá ...", "Bố ... mẹ và em đi chơi công viên ..."]),
        "Ví dụ: Mùa xuân, cây cối đâm chồi nảy lộc. / Bạn có thích đọc truyện không? / Ôi, cảnh đẹp quá! / Bố, mẹ và em đi chơi công viên.", 2)


TLV3 = [
    ("Viết đoạn văn (5–7 câu) kể về ông (hoặc bà) của em.", "Gợi ý: giới thiệu ông/bà (tên, tuổi); ngoại hình; việc ông/bà hay làm; tình cảm của em.\nVí dụ: Bà nội em năm nay đã hơn bảy mươi tuổi. Mái tóc bà bạc trắng như cước. Mỗi buổi chiều, bà thường kể chuyện cổ tích cho em nghe. Em rất yêu quý bà."),
    ("Viết đoạn văn (5–7 câu) tả một đồ vật mà em yêu thích.", "Gợi ý: đồ vật gì, ai tặng; hình dáng, màu sắc, các bộ phận; công dụng; em giữ gìn thế nào.\nVí dụ: Em có một chiếc cặp màu xanh do mẹ mua tặng. Cặp có hai ngăn lớn và một ngăn nhỏ. Mỗi ngày, em cẩn thận xếp sách vở vào cặp rồi đến trường."),
    ("Viết đoạn văn (5–7 câu) tả một cây mà em thích.", "Gợi ý: cây gì, trồng ở đâu; thân, cành, lá, hoa, quả; ích lợi; tình cảm của em.\nVí dụ: Trước sân nhà em có một cây ổi. Thân cây nhỏ, vỏ nhẵn. Mùa quả chín, cây thơm lừng và rất sai quả."),
    ("Viết đoạn văn (5–7 câu) tả một con vật nuôi trong nhà.", "Gợi ý: tên, loài; hình dáng, bộ lông, đôi mắt; hoạt động hằng ngày; tình cảm.\nVí dụ: Nhà em nuôi một chú chó tên là Vàng. Bộ lông nó vàng óng. Mỗi khi em đi học về, Vàng chạy ra mừng rối rít."),
    ("Viết đoạn văn (5–7 câu) kể về một việc tốt em đã làm.", "Gợi ý: việc gì, ở đâu, khi nào; em làm thế nào; kết quả, cảm nghĩ.\nVí dụ: Hôm qua, em nhặt được chiếc ví của một bác trên đường. Em đem đến công an phường nhờ trả lại. Bác ấy cảm ơn em rối rít. Em thấy rất vui."),
    ("Viết đoạn văn (5–7 câu) kể về một buổi lao động (hoặc văn nghệ) ở trường em.", "Gợi ý: ở đâu, khi nào; các bạn làm gì; không khí; cảm nghĩ.\nVí dụ: Sáng thứ bảy, lớp em lao động dọn vệ sinh sân trường. Bạn quét lá, bạn nhổ cỏ, ai cũng hăng hái. Chỉ một lúc sau, sân trường đã sạch bong."),
    ("Viết đoạn văn (5–7 câu) tả cảnh đẹp ở quê hương em.", "Gợi ý: cảnh gì (cánh đồng, dòng sông, ...); màu sắc, âm thanh; con người; tình cảm.\nVí dụ: Quê em có cánh đồng lúa rộng mênh mông. Mùa gặt, lúa chín vàng óng như tấm thảm khổng lồ. Gió thổi, sóng lúa rập rờn."),
    ("Viết một bức thư ngắn (khoảng 5 câu) thăm hỏi ông bà.", "Gợi ý: đầu thư (nơi viết, ngày tháng, lời xưng hô); nội dung (hỏi thăm sức khỏe, kể về học tập, gia đình); cuối thư (lời chúc, chữ kí).\nVí dụ: Ông bà kính mến! Cháu viết thư thăm ông bà. Dạo này ông bà có khỏe không ạ? Cháu học tập chăm chỉ và rất nhớ ông bà. Cháu chúc ông bà luôn mạnh khỏe."),
    ("Viết đoạn văn (5–7 câu) kể về một ngày Tết (hoặc lễ hội) mà em biết.", "Gợi ý: ngày lễ gì; mọi người chuẩn bị gì; hoạt động; cảm nghĩ.\nVí dụ: Tết Nguyên đán là ngày lễ lớn nhất trong năm. Cả nhà em dọn dẹp, gói bánh chưng và trang trí hoa đào. Sáng mùng một, em mặc áo mới đi chúc Tết ông bà."),
    ("Viết đoạn văn (5–7 câu) nêu cảm nghĩ của em về một người bạn.", "Gợi ý: bạn tên gì; bạn có điểm gì tốt; kỉ niệm với bạn; tình cảm của em.\nVí dụ: Người bạn thân nhất của em là Hoa. Hoa học giỏi và hay giúp đỡ mọi người. Có lần em quên bút, Hoa đã cho em mượn. Em rất quý bạn."),
]

CHU_DE = [
    ("Từ chỉ sự vật, hoạt động, đặc điểm, tình cảm",
     [mc_nhom(NH4, H4), mc_nhan(NH4, {**H4, "khác": "chỉ thời gian"})],
     [tl_nhom(NH4, H4T, "Xếp các từ sau vào nhóm thích hợp:", 3, 2, 2), tl_nhom(NH4, H4T, "Phân loại các từ sau:", 4, 2, 2)]),
    ("Từ trái nghĩa, từ đồng nghĩa",
     [mc_cap(TRAI, ["Từ trái nghĩa với \"{}\" là:", "Chọn từ có nghĩa trái ngược với \"{}\":"]), mc_cap(DONG, ["Từ nào cùng nghĩa với \"{}\"?", "Chọn từ đồng nghĩa với \"{}\":"])],
     [tl_cap(TRAI, "Tìm từ trái nghĩa với các từ:", 4, 2), tl_cap(DONG, "Tìm từ đồng nghĩa với các từ:", 3, 2)]),
    ("Biện pháp so sánh",
     [mc_dung_ss, mc_ss_vat, mc_tu_ss, mc_phan_biet2],
     [tl_ss_tim, tl_cur([("Đặt một câu có hình ảnh so sánh nói về bông hoa.", "Ví dụ: Bông hoa đỏ như ngọn lửa."), ("Đặt một câu có hình ảnh so sánh nói về bầu trời.", "Ví dụ: Bầu trời xanh như tấm gương khổng lồ."),
                         ("Đặt một câu có hình ảnh so sánh nói về dòng sông.", "Ví dụ: Dòng sông mềm mại như dải lụa."), ("Đặt một câu có hình ảnh so sánh nói về mẹ.", "Ví dụ: Tình yêu của mẹ ấm áp như ánh mặt trời."),
                         ("Đặt một câu có hình ảnh so sánh nói về em bé.", "Ví dụ: Đôi mắt em bé tròn như hạt nhãn.")], 2)]),
    ("Biện pháp nhân hóa",
     [mc_nhan_hoa, mc_sv_nh, mc_phan_biet],
     [tl_nh_tim, tl_cur([("Viết lại câu \"Gió thổi nhè nhẹ.\" thành câu có hình ảnh nhân hóa.", "Ví dụ: Bác gió nhè nhẹ vuốt ve cánh đồng."),
                         ("Viết lại câu \"Mặt trời mọc.\" thành câu có hình ảnh nhân hóa.", "Ví dụ: Ông mặt trời thức dậy, tươi cười chào mọi người."),
                         ("Viết lại câu \"Cây bàng có nhiều lá.\" thành câu có hình ảnh nhân hóa.", "Ví dụ: Cây bàng khoác lên mình chiếc áo xanh mướt."),
                         ("Viết lại câu \"Mưa rơi trên mái nhà.\" thành câu có hình ảnh nhân hóa.", "Ví dụ: Cô mưa gõ nhịp tí tách trên mái nhà."),
                         ("Viết lại câu \"Con mèo ngủ trên ghế.\" thành câu có hình ảnh nhân hóa.", "Ví dụ: Chú mèo ngủ say sưa trên ghế, mơ về những chú chuột.")], 2)]),
    ("Chính tả: ch/tr, s/x, l/n, d/gi/r, hỏi/ngã",
     [mc_cs_nhom(CH_TR, ("ch", "tr")), mc_cs_nhom(S_X, ("s", "x")), mc_cs_nhom(L_N, ("l", "n")), mc_cs_nhom(D_GI_R, ("d", "gi", "r")), mc_cs_thanh(THANH),
      mc_cs_dien(D_GI_R, ("d", "gi", "r"), ["d", "gi", "r", "v"])],
     [tl_cs_dien(CH_TR, ("ch", "tr"), "Điền ch hoặc tr vào chỗ trống:", 4, 1), tl_cs_dien(S_X, ("s", "x"), "Điền s hoặc x vào chỗ trống:", 4, 1),
      tl_cs_dien(D_GI_R, ("d", "gi", "r"), "Điền d, gi hoặc r vào chỗ trống:", 4, 2), tl_cs_sua(L_N, ("l", "n"), "Viết lại cho đúng chính tả:", 4, 2),
      tl_cs_thanh(THANH, "Sửa lỗi dấu hỏi/dấu ngã trong các từ sau:", 4, 2)]),
    ("Câu Ai là gì? Ai làm gì? Ai thế nào?",
     [mc_cau_nhan(CAU3, LABEL3, "Câu \"{c}\" thuộc kiểu câu nào?"), mc_hoi_bp, mc_cau_chon(CAU3, "Ai làm gì?", "Câu nào thuộc kiểu câu Ai làm gì?", 1),
      mc_cau_chon(CAU3, "Ai thế nào?", "Câu nào thuộc kiểu câu Ai thế nào?", 1), mc_cau_chon(CAU3, "Ai là gì?", "Câu nào thuộc kiểu câu Ai là gì?", 1)],
     [tl_cau_nhan(CAU3, "Xác định kiểu câu (Ai là gì?, Ai làm gì?, Ai thế nào?) của mỗi câu sau:", 4, 2), tl_hoi_bp,
      tl_cur([("Đặt câu theo mẫu Ai làm gì? nói về các bạn nhỏ ở sân trường.", "Ví dụ: Các bạn nhỏ chơi nhảy dây ngoài sân trường."), ("Đặt câu theo mẫu Ai thế nào? tả con đường làng.", "Ví dụ: Con đường làng thẳng tắp và sạch sẽ."),
              ("Đặt câu theo mẫu Ai là gì? giới thiệu về cô giáo của em.", "Ví dụ: Cô Lan là giáo viên chủ nhiệm lớp em."), ("Đặt câu theo mẫu Ai làm gì? nói về bác nông dân.", "Ví dụ: Bác nông dân cày ruộng từ sáng sớm.")], 2)]),
    ("Dấu câu: dấu phẩy, dấu hai chấm, ngoặc kép, gạch ngang",
     [mc_dau_cuoi2, mc_chuc_nang],
     [tl_dau_cuoi, tl_chuc_nang, tl_dien_dau]),
    ("Thành ngữ, tục ngữ",
     [mc_dien_tu(TN_DIEN, "Chọn từ thích hợp điền vào chỗ trống:", 1), mc_nghia(TUC_NGU, "Câu tục ngữ \"{x}\" khuyên chúng ta điều gì?", 2, TUC_NHOM), mc_nghia(THANH_NGU_NGHIA, "Thành ngữ \"{x}\" có nghĩa là gì?", 2)],
     [tl_dien_tu(TN_DIEN, "Điền từ thích hợp vào chỗ trống:", 4, 1), tl_cur([(f"Em hiểu câu \"{x}\" như thế nào?", n) for x, n in TUC_NGU], 2), tl_cur([(f"Giải thích thành ngữ \"{x}\".", n) for x, n in THANH_NGU_NGHIA], 2)]),
    ("Tập làm văn: viết đoạn văn", [], [tl_cur(TLV3, 3)], {"n_mc": 0}),
]
