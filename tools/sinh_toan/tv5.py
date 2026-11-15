from tvcore import *
from tvcore import _tron
from tvdata import *
from tvdata2 import *
from tv2 import mc_dung_ss, mc_ss_vat, tl_ss_tim
from tv3 import mc_nhan_hoa, mc_sv_nh, mc_phan_biet, mc_phan_biet2, tl_nh_tim, NHAN_HOA
from tv4 import TL3, H_TL, H_TL_T, N_TL

# ---- đồng âm / nhiều nghĩa: (từ, câu 1, nghĩa 1, câu 2, nghĩa 2, loại) -------------------
DA = [
    ("đá", "Em đá bóng ngoài sân.", "dùng chân đưa bóng đi", "Hòn đá nằm bên đường.", "khối rắn từ lòng đất", "từ đồng âm"),
    ("bàn", "Cả nhà bàn việc đi chơi.", "trao đổi ý kiến", "Quyển sách đặt trên bàn.", "đồ dùng có mặt phẳng để đặt đồ", "từ đồng âm"),
    ("đường", "Con đường làng rợp bóng cây.", "lối đi", "Mẹ cho thêm đường vào cốc chanh.", "chất ngọt dùng để pha chế", "từ đồng âm"),
    ("bay", "Chim bay trên trời.", "di chuyển trên không", "Bác thợ xây dùng cái bay trát tường.", "dụng cụ của thợ nề", "từ đồng âm"),
    ("kho", "Mẹ kho cá với nước màu.", "nấu cho thấm gia vị", "Kho thóc của làng đầy ắp.", "nơi cất giữ", "từ đồng âm"),
    ("sao", "Ngôi sao sáng lấp lánh.", "thiên thể trên bầu trời", "Sao bạn đến muộn thế?", "vì sao (từ để hỏi)", "từ đồng âm"),
    ("mai", "Mai em đi học.", "ngày hôm sau", "Cây hoa mai nở vàng trước sân.", "tên một loài hoa", "từ đồng âm"),
    ("đậu", "Chim đậu trên cành cây.", "dừng lại", "Mẹ nấu chè đậu xanh.", "hạt đậu (một loại cây lương thực)", "từ đồng âm"),
    ("ba", "Nhà em có ba người.", "số 3", "Ba em là kĩ sư.", "bố", "từ đồng âm"),
    ("chín", "Lúa chín vàng cả cánh đồng.", "quả hoặc hạt đã già, có thể ăn hoặc gặt", "Em lên chín tuổi.", "số 9", "từ đồng âm"),
    ("chân", "Chân em bé nhỏ xíu.", "bộ phận cơ thể người", "Chân bàn bị gãy.", "bộ phận đỡ vật", "từ nhiều nghĩa"),
    ("mũi", "Mũi em bé nhỏ xinh.", "bộ phận trên mặt", "Mũi thuyền rẽ sóng.", "phần đầu nhọn của vật", "từ nhiều nghĩa"),
    ("tay", "Tay em cầm bút.", "bộ phận cơ thể", "Tay ghế bằng gỗ.", "bộ phận để tựa của ghế", "từ nhiều nghĩa"),
    ("lưỡi", "Lưỡi em đỏ hồng.", "cơ quan trong miệng", "Lưỡi dao rất sắc.", "phần sắc của dao", "từ nhiều nghĩa"),
    ("đầu", "Đầu em bé tròn xoe.", "phần trên cùng của cơ thể", "Đầu làng có cây đa lớn.", "phần đầu tiên của làng", "từ nhiều nghĩa"),
    ("cánh", "Cánh chim sải rộng.", "bộ phận để bay", "Cánh cửa mở toang.", "bộ phận của cửa", "từ nhiều nghĩa"),
    ("mắt", "Mắt em sáng long lanh.", "cơ quan để nhìn", "Mắt tre đã nảy mầm.", "chỗ lồi ở thân cây", "từ nhiều nghĩa"),
    ("răng", "Răng em trắng đều.", "bộ phận trong miệng", "Răng lược bị gãy.", "phần nhọn của lược", "từ nhiều nghĩa"),
    ("cổ", "Cổ em bé thon dài.", "bộ phận nối đầu với thân", "Cổ chai nhỏ và dài.", "phần thắt lại của chai", "từ nhiều nghĩa"),
    ("chạy", "Em bé chạy quanh sân.", "di chuyển nhanh bằng chân", "Đồng hồ chạy đúng giờ.", "hoạt động bình thường của máy", "từ nhiều nghĩa"),
]
LOAI = ["từ đồng âm", "từ nhiều nghĩa", "từ đồng nghĩa", "từ trái nghĩa"]


def mc_loai(rng):
    t, c1, n1, c2, n2, l = rng.choice(DA)
    return M(f"Từ \"{t}\" trong hai câu: \"{c1}\" và \"{c2}\" là:", l, _tron(rng, l, LOAI), 2)


def mc_nghia_cau(rng):
    t, c1, n1, c2, n2, l = rng.choice(DA)
    khac = [x[2] for x in DA if x[0] != t] + [x[4] for x in DA if x[0] != t]
    c, n = (c1, n1) if rng.random() < .5 else (c2, n2)
    return M(f"Từ \"{t}\" trong câu \"{c}\" có nghĩa là:", n, _tron(rng, n, khac), 2)


def tl_phan_biet(rng):
    ch = rng.sample(DA, 1)[0]
    t, c1, n1, c2, n2, l = ch
    return T(f"Từ \"{t}\" trong hai câu sau có nghĩa như thế nào? Đó là từ đồng âm hay từ nhiều nghĩa?\n1. {c1}\n2. {c2}", f"Câu 1: {t} = {n1}\nCâu 2: {t} = {n2}\nĐó là {l}.", 3)


def tl_phan_loai_da(rng):
    ch = rng.sample(DA, 3)
    return T("Cho biết các từ in nghiêng dưới đây là từ đồng âm hay từ nhiều nghĩa:\n" + "\n".join(f"{i + 1}. Từ \"{t}\": \"{c1}\" / \"{c2}\"" for i, (t, c1, _, c2, _, _) in enumerate(ch)), "\n".join(f"{i + 1}. {t}: {l}" for i, (t, _, _, _, _, l) in enumerate(ch)), 2)


tl_dat_da = tl_cur([("Đặt hai câu, mỗi câu dùng một nghĩa khác nhau của từ \"chân\".", "Ví dụ: Chân em bị đau. / Chân bàn làm bằng gỗ."), ("Đặt hai câu để phân biệt nghĩa của hai từ đồng âm \"đá\".", "Ví dụ: Em đá bóng ngoài sân. / Hòn đá nằm bên đường."),
                    ("Đặt hai câu có từ \"bàn\" với nghĩa khác nhau.", "Ví dụ: Cả nhà bàn việc đi chơi. / Em ngồi học ở bàn."), ("Đặt hai câu có từ \"đường\" với nghĩa khác nhau.", "Ví dụ: Con đường làng rất sạch. / Mẹ cho đường vào chè."),
                    ("Đặt hai câu có từ \"cánh\" với nghĩa khác nhau.", "Ví dụ: Cánh chim vỗ nhanh. / Cánh cửa mở rộng."), ("Đặt hai câu có từ \"mắt\" với nghĩa khác nhau.", "Ví dụ: Mắt em bé rất sáng. / Mắt tre đã nảy mầm.")], 3)

# ---- đại từ --------------------------------------------------------------------------------------
DAI_TU = [
    ("Chúng tôi đang học bài.", "Chúng tôi", ["đang", "học", "bài"]), ("Nó chạy rất nhanh.", "Nó", ["chạy", "rất", "nhanh"]),
    ("Cậu có thích đọc sách không?", "Cậu", ["thích", "đọc", "sách"]), ("Họ đang gặt lúa ngoài đồng.", "Họ", ["gặt", "lúa", "đồng"]),
    ("Tớ rất thích hát.", "Tớ", ["rất", "thích", "hát"]), ("Ai cũng yêu quê hương.", "Ai", ["cũng", "yêu", "quê hương"]),
    ("Chúng nó đang chơi đá bóng.", "Chúng nó", ["đang", "chơi", "bóng"]), ("Tôi thích đọc truyện.", "Tôi", ["thích", "đọc", "truyện"]),
    ("Mình thích hoa hồng.", "Mình", ["thích", "hoa", "hồng"]), ("Nó là một chú chó con.", "Nó", ["là", "chú", "con"]),
    ("Họ là những người thợ giỏi.", "Họ", ["là", "thợ", "giỏi"]), ("Tôi sống ở Thái Bình.", "Tôi", ["sống", "ở", "Thái Bình"]),
    ("Chúng ta cùng nhau đi học.", "Chúng ta", ["cùng", "đi", "học"]),
]
KHONG_DT = ["Lan đọc sách.", "Mẹ nấu cơm.", "Trời mưa to.", "Bông hoa rất đẹp.", "Cây bàng xanh tốt.", "Nam chạy nhanh.", "Bố đi làm.", "Cô giáo giảng bài."]


def mc_dt_trong_cau(rng):
    c, d, sai = rng.choice(DAI_TU)
    return M(f"Từ nào là đại từ trong câu \"{c}\"?", d, list(sai), 2)


def mc_cau_dt(rng):
    d, _, _ = rng.choice(DAI_TU)
    return M("Câu nào có dùng đại từ?", d, _tron(rng, d, KHONG_DT), 2)


def tl_dt(rng):
    ch = rng.sample(DAI_TU, 4)
    return T("Tìm đại từ trong mỗi câu sau:\n" + "\n".join(f"{i + 1}. {c}" for i, (c, _, _) in enumerate(ch)), "\n".join(f"{i + 1}. {d}" for i, (_, d, _) in enumerate(ch)), 2)


tl_thay_dt = tl_cur([("Thay các từ in đậm bằng đại từ cho đỡ lặp: \"Lan rất chăm học. Lan luôn đạt điểm cao.\"", "Lan rất chăm học. Bạn ấy (cô bé ấy) luôn đạt điểm cao."),
                     ("Thay các từ lặp lại bằng đại từ thích hợp: \"Con mèo nằm trên ghế. Con mèo ngủ ngon lành.\"", "Con mèo nằm trên ghế. Nó ngủ ngon lành."),
                     ("Thay các từ lặp lại bằng đại từ thích hợp: \"Các bạn nhỏ chơi ở sân. Các bạn nhỏ cười nói vui vẻ.\"", "Các bạn nhỏ chơi ở sân. Họ (Các bạn ấy) cười nói vui vẻ."),
                     ("Viết hai câu có dùng đại từ xưng hô \"chúng tôi\".", "Ví dụ: Chúng tôi cùng nhau học bài. Chúng tôi rất vui."),
                     ("Viết hai câu có dùng đại từ \"nó\" để nói về một con vật.", "Ví dụ: Con chó của em rất ngoan. Nó luôn chờ em ở cổng.")], 2)

# ---- quan hệ từ ---------------------------------------------------------------------------------------
QHT_DON = [
    ("Quyển sách của em đặt trên bàn.", "của", ["quyển", "sách", "đặt"]), ("Em học chăm chỉ để đạt điểm cao.", "để", ["học", "chăm chỉ", "điểm"]),
    ("Mẹ và em đi chợ.", "và", ["Mẹ", "em", "chợ"]), ("Em thích đá bóng hoặc chơi cờ vua.", "hoặc", ["thích", "đá", "cờ"]),
    ("Bạn Lan học giỏi nhưng rất khiêm tốn.", "nhưng", ["học", "giỏi", "khiêm tốn"]), ("Trời rét mà em vẫn dậy sớm.", "mà", ["rét", "vẫn", "dậy"]),
    ("Mai và Hoa là đôi bạn thân.", "và", ["Mai", "Hoa", "bạn"]), ("Cuốn truyện của bạn Nam rất hay.", "của", ["Cuốn", "truyện", "hay"]),
    ("Hoa cười vì được điểm mười.", "vì", ["cười", "được", "điểm"]),
    ("Hôm nay em đến trường bằng xe đạp.", "bằng", ["em", "trường", "xe đạp"]), ("Chiếc áo của mẹ màu xanh.", "của", ["Chiếc", "áo", "màu"]),
]
QHT_CAP = [
    ("Vì trời rét nên em mặc áo ấm.", "Vì – nên"), ("Nếu trời nắng thì lớp em đi cắm trại.", "Nếu – thì"), ("Tuy nhà nghèo nhưng Nam học rất giỏi.", "Tuy – nhưng"),
    ("Không những Lan học giỏi mà bạn còn hát hay.", "Không những – mà còn"), ("Hễ trời mưa thì đường làng lại lầy lội.", "Hễ – thì"),
    ("Vì Hoa chăm chỉ nên bạn đạt điểm cao.", "Vì – nên"), ("Nếu em cố gắng thì em sẽ thành công.", "Nếu – thì"),
    ("Tuy trời mưa to nhưng các bạn vẫn đến lớp đúng giờ.", "Tuy – nhưng"), ("Hễ có thời gian rảnh thì em lại đọc sách.", "Hễ – thì"), ("Vì mải chơi nên Nam quên làm bài.", "Vì – nên"),
]
CAP_LC = ["Vì – nên", "Nếu – thì", "Tuy – nhưng", "Không những – mà còn", "Hễ – thì"]


def mc_qht(rng):
    c, d, sai = rng.choice(QHT_DON)
    return M(f"Từ nào là quan hệ từ trong câu \"{c}\"?", d, list(sai), 2)


tl_qht = tl_cur([("Gạch chân quan hệ từ trong các câu: (1) Mẹ và em đi chợ. (2) Em học chăm chỉ để đạt điểm cao.", "(1) và; (2) để"), ("Gạch chân quan hệ từ trong các câu: (1) Quyển sách của em đặt trên bàn. (2) Trời rét mà em vẫn dậy sớm.", "(1) của; (2) mà"),
                 ("Điền quan hệ từ thích hợp vào chỗ trống: Trời mưa to ... em vẫn đi học.", "nhưng (Tuy trời mưa to nhưng em vẫn đi học)"), ("Điền cặp quan hệ từ thích hợp: ... trời mưa ... đường trơn.", "Vì ... nên ... / Nếu ... thì ..."),
                 ("Điền cặp quan hệ từ thích hợp: ... Nam học giỏi ... bạn ấy còn hát hay.", "Không những ... mà ... còn ..."), ("Điền quan hệ từ thích hợp: Em muốn làm bài thật tốt ... được cô khen.", "để"),
                 ("Đặt một câu có cặp quan hệ từ \"vì ... nên ...\".", "Ví dụ: Vì trời mưa nên em ở nhà đọc sách."), ("Đặt một câu có cặp quan hệ từ \"tuy ... nhưng ...\".", "Ví dụ: Tuy bài khó nhưng Nam vẫn làm được."),
                 ("Đặt một câu có cặp quan hệ từ \"nếu ... thì ...\".", "Ví dụ: Nếu em chăm chỉ thì em sẽ tiến bộ."), ("Đặt một câu có quan hệ từ \"và\" nối hai từ chỉ người.", "Ví dụ: Bố và mẹ đi làm.")], 2)


def mc_cap_qht(rng):
    c, d = rng.choice(QHT_CAP)
    return M(f"Cặp quan hệ từ trong câu \"{c}\" là:", d, _tron(rng, d, CAP_LC), 2)


# ---- câu đơn, câu ghép -----------------------------------------------------------------------------------
GHEP = [
    ("Trời mưa to, đường phố ngập nước.", "Câu ghép"), ("Mặt trời mọc, sương tan dần.", "Câu ghép"), ("Tuy nhà nghèo nhưng Nam học rất giỏi.", "Câu ghép"),
    ("Vì trời mưa nên chúng em nghỉ đá bóng.", "Câu ghép"), ("Mẹ nấu cơm còn bố đọc báo.", "Câu ghép"), ("Chim hót líu lo, hoa nở rực rỡ.", "Câu ghép"),
    ("Nếu em chăm chỉ thì em sẽ tiến bộ.", "Câu ghép"), ("Gió thổi mạnh, cây cối nghiêng ngả.", "Câu ghép"), ("Em làm bài tập còn anh em đọc truyện.", "Câu ghép"),
    ("Tuy trời rét nhưng em vẫn dậy sớm tập thể dục.", "Câu ghép"),
    ("Em đi học.", "Câu đơn"), ("Mẹ nấu cơm rất ngon.", "Câu đơn"), ("Những chú chim đang hót trên cành.", "Câu đơn"), ("Bố em là kĩ sư.", "Câu đơn"),
    ("Cả lớp lắng nghe cô giáo giảng bài.", "Câu đơn"), ("Chiếc cặp của em màu xanh.", "Câu đơn"), ("Chúng em đang tưới cây ngoài vườn.", "Câu đơn"),
    ("Bà em kể chuyện cổ tích cho em nghe.", "Câu đơn"), ("Con mèo nằm phơi nắng trên thềm.", "Câu đơn"), ("Lan là học sinh giỏi.", "Câu đơn"),
]
LABEL_G = ["Câu đơn", "Câu ghép", "Câu cảm", "Câu khiến"]
VE = [("Trời mưa to, đường phố ngập nước.", "Trời mưa to", "đường phố ngập nước"), ("Mặt trời mọc, sương tan dần.", "Mặt trời mọc", "sương tan dần"),
      ("Tuy nhà nghèo nhưng Nam học rất giỏi.", "Tuy nhà nghèo", "nhưng Nam học rất giỏi"), ("Vì trời mưa nên chúng em nghỉ đá bóng.", "Vì trời mưa", "nên chúng em nghỉ đá bóng"),
      ("Mẹ nấu cơm, bố đọc báo.", "Mẹ nấu cơm", "bố đọc báo"), ("Chim hót líu lo, hoa nở rực rỡ.", "Chim hót líu lo", "hoa nở rực rỡ"),
      ("Nếu em chăm chỉ thì em sẽ tiến bộ.", "Nếu em chăm chỉ", "thì em sẽ tiến bộ"), ("Gió thổi mạnh, cây cối nghiêng ngả.", "Gió thổi mạnh", "cây cối nghiêng ngả")]


def mc_so_ve(rng):
    c, v1, v2 = rng.choice(VE)
    ws = c.rstrip(".").replace(",", "").split()
    dung = f"{v1} / {v2}"
    sai = [f"{' '.join(ws[:i])} / {' '.join(ws[i:])}" for i in range(1, len(ws))]
    sai = [x for x in sai if x != dung]
    return M(f"Câu ghép \"{c}\" có hai vế câu là:", dung, _tron(rng, dung, sai), 3)


def tl_ve(rng):
    ch = rng.sample(VE, 3)
    return T("Tách các vế trong mỗi câu ghép sau:\n" + "\n".join(f"{i + 1}. {c}" for i, (c, _, _) in enumerate(ch)), "\n".join(f"{i + 1}. Vế 1: {a} | Vế 2: {b}" for i, (_, a, b) in enumerate(ch)), 3)


tl_dat_ghep = tl_cur([("Đặt một câu ghép nói về thời tiết.", "Ví dụ: Trời nắng gắt, đường phố vắng người."), ("Đặt một câu ghép có cặp quan hệ từ \"vì ... nên ...\".", "Ví dụ: Vì Nam chăm chỉ nên bạn học rất giỏi."),
                      ("Đặt một câu ghép nói về việc học của em.", "Ví dụ: Em làm bài tập, còn em trai em vẽ tranh."), ("Nối hai câu đơn thành một câu ghép: \"Trời mưa. Em vẫn đi học.\"", "Tuy trời mưa nhưng em vẫn đi học."),
                      ("Nối hai câu đơn thành một câu ghép: \"Gió thổi. Cây lá rung rinh.\"", "Gió thổi, cây lá rung rinh."), ("Đặt một câu ghép có cặp quan hệ từ \"nếu ... thì ...\".", "Ví dụ: Nếu trời đẹp thì cả nhà đi dã ngoại.")], 3)

# ---- biện pháp tu từ -----------------------------------------------------------------------------------------
tl_viet_bptt = tl_cur([("Viết một đoạn văn 3 câu tả buổi sáng, trong đó có dùng một hình ảnh so sánh.", "Ví dụ: Buổi sáng, mặt trời đỏ như quả cầu lửa nhô lên sau lũy tre. Sương mai đọng trên lá lấp lánh. Cả làng quê bừng tỉnh trong tiếng chim hót."),
                       ("Viết một đoạn văn 3 câu tả cơn gió, trong đó có dùng một hình ảnh nhân hóa.", "Ví dụ: Bác gió rủ cây cối nhảy múa trong sân trường. Lá bay xào xạc như hát. Chiều xuống, bác gió lặng lẽ ra về."),
                       ("Chuyển câu \"Chim hót trên cành\" thành câu có hình ảnh nhân hóa.", "Ví dụ: Chú chim sâu cất tiếng hát chào buổi sáng trên cành cây."),
                       ("Chuyển câu \"Mặt trăng sáng\" thành câu có hình ảnh so sánh.", "Ví dụ: Mặt trăng sáng như chiếc đĩa bạc."),
                       ("Nêu tác dụng của biện pháp nhân hóa trong văn miêu tả.", "Nhân hóa làm cho sự vật, con vật, cây cối trở nên gần gũi, sinh động, có tâm hồn như con người."),
                       ("Nêu tác dụng của biện pháp so sánh trong văn miêu tả.", "So sánh giúp người đọc hình dung sự vật rõ ràng, sinh động hơn nhờ liên tưởng đến một sự vật khác tương đồng.")], 3)

# ---- tập làm văn lớp 5 ------------------------------------------------------------------------------------------
TLV5 = [
    ("Lập dàn ý bài văn tả người thân (mẹ, bà, ...) của em.", "Dàn ý: Mở bài: giới thiệu người định tả (là ai, quan hệ với em). Thân bài: tả ngoại hình (tuổi, dáng người, khuôn mặt, mái tóc, đôi mắt, nụ cười), tả tính tình, hoạt động tiêu biểu (việc làm hằng ngày, cử chỉ, lời nói), tình cảm dành cho em. Kết bài: tình cảm và mong ước của em."),
    ("Lập dàn ý bài văn tả một cơn mưa.", "Dàn ý: Mở bài: giới thiệu cơn mưa (thời điểm, địa điểm). Thân bài: tả trước cơn mưa (bầu trời, gió, mây), tả cơn mưa (hạt mưa, âm thanh, cảnh vật, con người), tả sau cơn mưa (không khí, cây cối, ánh nắng). Kết bài: cảm nghĩ về cơn mưa."),
    ("Lập dàn ý bài văn tả cảnh dòng sông (hoặc cánh đồng) ở quê em.", "Dàn ý: Mở bài: giới thiệu cảnh (ở đâu, vào thời điểm nào). Thân bài: tả bao quát, tả chi tiết (màu sắc, âm thanh, hình ảnh, hoạt động của con người) theo trình tự thời gian hoặc không gian. Kết bài: tình cảm với quê hương."),
    ("Lập dàn ý bài văn tả một cây ăn quả mà em yêu thích.", "Dàn ý: Mở bài: giới thiệu cây (loại cây, trồng ở đâu). Thân bài: tả bao quát (chiều cao, tán lá), tả chi tiết (rễ, thân, cành, lá, hoa, quả), ích lợi và sự chăm sóc. Kết bài: tình cảm của em với cây."),
    ("Lập dàn ý bài văn tả một con vật nuôi trong nhà.", "Dàn ý: Mở bài: giới thiệu con vật (loài, tên, được nuôi từ bao giờ). Thân bài: tả hình dáng (kích thước, bộ lông, đầu, mắt, chân, đuôi), tả hoạt động và thói quen, tính nết. Kết bài: tình cảm của em với con vật."),
    ("Lập dàn ý bài văn tả một đồ vật gắn bó với em (chiếc cặp, chiếc xe đạp, ...).", "Dàn ý: Mở bài: giới thiệu đồ vật, hoàn cảnh có được. Thân bài: tả hình dáng, màu sắc, chất liệu, các bộ phận, công dụng, kỉ niệm, cách giữ gìn. Kết bài: tình cảm của em với đồ vật."),
    ("Lập dàn ý bài văn kể về một việc làm tốt (hoặc việc mà em chứng kiến) khiến em xúc động.", "Dàn ý: Mở bài: nêu việc định kể (khi nào, ở đâu, ai tham gia). Thân bài: diễn biến theo trình tự (nguyên nhân, việc làm, lời nói, thái độ các nhân vật), cảm xúc của em. Kết bài: kết quả, bài học rút ra."),
    ("Viết một bức thư (khoảng 10 câu) cảm ơn thầy (cô) giáo cũ của em.", "Gợi ý: đầu thư (địa điểm, ngày tháng, lời xưng hô kính trọng); nội dung (hỏi thăm, kể về việc học hiện nay, nhớ kỉ niệm, lời cảm ơn); cuối thư (lời chúc, lời hứa, kí tên).\nVí dụ: Thưa cô, em là ... học trò cũ của cô. Nhân dịp ... em viết thư thăm cô."),
    ("Lập dàn ý bài văn tả một người lao động mà em kính trọng (bác nông dân, chú công nhân, ...).", "Dàn ý: Mở bài: giới thiệu người em định tả (là ai, em gặp ở đâu). Thân bài: tả ngoại hình (dáng người, gương mặt, đôi bàn tay), tả công việc và thái độ làm việc, tả phẩm chất đáng quý. Kết bài: tình cảm của em."),
    ("Nêu cảm nghĩ của em về một người thầy (cô) mà em kính yêu (khoảng 8–10 câu).", "Gợi ý: giới thiệu người thầy (cô); những điều em kính phục (dạy dỗ tận tâm, tình thương); một kỉ niệm đáng nhớ; điều em muốn nói với thầy (cô).\nVí dụ mở đầu: Trong suốt những năm tiểu học, người để lại cho em nhiều ấn tượng nhất là cô giáo chủ nhiệm."),
]

TOANC = {"danh từ": DT, "động từ": DGT, "tính từ": TT}

CHU_DE = [
    ("Từ đồng nghĩa, từ trái nghĩa",
     [mc_cap(TRAI, ["Từ trái nghĩa với \"{}\" là:", "Chọn từ có nghĩa trái ngược với \"{}\":"]), mc_cap(DONG, ["Từ nào đồng nghĩa với \"{}\"?", "Chọn từ cùng nghĩa với \"{}\":"])],
     [tl_cap(TRAI, "Tìm từ trái nghĩa với các từ:", 4, 2), tl_cap(DONG, "Tìm từ đồng nghĩa với các từ:", 4, 2),
      tl_cur([("Đặt câu có cặp từ trái nghĩa \"to – nhỏ\".", "Ví dụ: Quả bưởi to còn quả chanh nhỏ."), ("Đặt câu có cặp từ trái nghĩa \"sáng – tối\".", "Ví dụ: Trời sáng thì sân trường vui, trời tối thì vắng lặng."),
              ("Thay từ in đậm bằng từ đồng nghĩa: \"Bạn Lan rất chăm chỉ.\"", "Bạn Lan rất siêng năng (cần cù)."), ("Đặt câu có cặp từ trái nghĩa \"cao – thấp\".", "Ví dụ: Cây tre cao còn bụi cỏ thấp."), ("Đặt câu có cặp từ trái nghĩa \"nhanh – chậm\".", "Ví dụ: Thỏ chạy nhanh còn rùa bò chậm."),
              ("Thay từ in đậm bằng từ đồng nghĩa: \"Cánh đồng rộng lớn.\"", "Cánh đồng bao la (mênh mông).")], 3)]),
    ("Từ đồng âm và từ nhiều nghĩa",
     [mc_loai, mc_nghia_cau],
     [tl_phan_biet, tl_phan_loai_da, tl_dat_da]),
    ("Đại từ",
     [mc_dt_trong_cau, mc_cau_dt],
     [tl_dt, tl_thay_dt]),
    ("Quan hệ từ",
     [mc_qht, mc_cap_qht],
     [tl_qht]),
    ("Câu đơn và câu ghép",
     [mc_cau_nhan(GHEP, LABEL_G, "Câu \"{c}\" là:", 2), mc_cau_chon(GHEP, "Câu ghép", "Câu nào là câu ghép?", 2), mc_cau_chon(GHEP, "Câu đơn", "Câu nào là câu đơn?", 1), mc_so_ve],
     [tl_cau_nhan(GHEP, "Xác định câu đơn hay câu ghép của mỗi câu sau:", 4, 2), tl_ve, tl_dat_ghep]),
    ("Biện pháp tu từ: so sánh, nhân hóa",
     [mc_dung_ss, mc_nhan_hoa, mc_ss_vat, mc_sv_nh, mc_phan_biet, mc_phan_biet2],
     [tl_ss_tim, tl_nh_tim, tl_viet_bptt]),
    ("Ôn tập từ loại: danh từ, động từ, tính từ",
     [mc_nhom(TL3, H_TL), mc_nhan(TL3, N_TL)],
     [tl_nhom(TL3, H_TL_T, "Xếp các từ sau vào các nhóm danh từ, động từ, tính từ:", 3, 3, 2), tl_nhom(TL3, H_TL_T, "Tìm danh từ, động từ, tính từ trong các từ sau:", 3, 2, 2)]),
    ("Chính tả: ch/tr, s/x, l/n, d/gi/r, hỏi/ngã",
     [mc_cs_nhom(CH_TR, ("ch", "tr")), mc_cs_nhom(S_X, ("s", "x")), mc_cs_nhom(L_N, ("l", "n")), mc_cs_nhom(D_GI_R, ("d", "gi", "r")), mc_cs_thanh(THANH)],
     [tl_cs_sua(CH_TR, ("ch", "tr"), "Phát hiện và sửa lỗi chính tả:", 5, 2), tl_cs_sua(S_X, ("s", "x"), "Phát hiện và sửa lỗi chính tả:", 5, 2), tl_cs_sua(L_N, ("l", "n"), "Phát hiện và sửa lỗi chính tả:", 5, 2),
      tl_cs_sua(D_GI_R, ("d", "gi", "r"), "Phát hiện và sửa lỗi chính tả:", 5, 2), tl_cs_thanh(THANH, "Sửa lỗi dấu hỏi/dấu ngã:", 5, 2)]),
    ("Thành ngữ, tục ngữ",
     [mc_dien_tu(TN_DIEN, "Chọn từ thích hợp điền vào chỗ trống:", 1), mc_nghia(TUC_NGU, "Câu tục ngữ \"{x}\" khuyên chúng ta điều gì?", 2, TUC_NHOM), mc_nghia(THANH_NGU_NGHIA, "Thành ngữ \"{x}\" có nghĩa là gì?", 2)],
     [tl_dien_tu(TN_DIEN, "Điền từ thích hợp vào chỗ trống:", 4, 1), tl_cur([(f"Em hiểu câu \"{x}\" như thế nào? Hãy nêu một việc làm thể hiện đúng lời khuyên đó.", n) for x, n in TUC_NGU], 3),
      tl_cur([(f"Giải thích thành ngữ \"{x}\" và đặt một câu có dùng thành ngữ này.", n) for x, n in THANH_NGU_NGHIA], 3)]),
    ("Tập làm văn: dàn ý và bài viết", [], [tl_cur(TLV5, 3)], {"n_mc": 0}),
]
