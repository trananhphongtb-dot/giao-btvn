"""Kho câu, biện pháp tu từ, thành ngữ – tục ngữ cho Tiếng Việt lớp 2–5 (soạn tay)."""

# ---- so sánh: (câu, sự vật 1, sự vật 2) ---------------------------------------------
SO_SANH = [
    ("Mặt trời đỏ như quả cầu lửa.", "mặt trời", "quả cầu lửa"),
    ("Đôi mắt em bé trong như hạt nhãn.", "đôi mắt em bé", "hạt nhãn"),
    ("Trăng tròn như chiếc đĩa bạc.", "trăng", "chiếc đĩa bạc"),
    ("Cánh đồng lúa chín vàng như tấm thảm khổng lồ.", "cánh đồng lúa", "tấm thảm khổng lồ"),
    ("Mái tóc bà trắng như cước.", "mái tóc bà", "cước"),
    ("Dòng sông mềm mại như dải lụa.", "dòng sông", "dải lụa"),
    ("Những đám mây trắng như bông.", "những đám mây", "bông"),
    ("Con đường quanh co như con rắn.", "con đường", "con rắn"),
    ("Má em bé hồng như quả đào chín.", "má em bé", "quả đào chín"),
    ("Tiếng suối chảy róc rách như tiếng đàn.", "tiếng suối", "tiếng đàn"),
    ("Bàn tay mẹ ấm như ngọn lửa hồng.", "bàn tay mẹ", "ngọn lửa hồng"),
    ("Những ngôi sao lấp lánh như những viên kim cương.", "những ngôi sao", "những viên kim cương"),
    ("Chú bé chạy nhanh như sóc.", "chú bé", "sóc"),
    ("Ông em khỏe như voi.", "ông em", "voi"),
]
KHONG_SS = [
    "Mặt trời mọc ở đằng đông.", "Em đi học bằng xe đạp.", "Cánh đồng lúa chín vàng.", "Trăng sáng vằng vặc.", "Dòng sông chảy qua làng.",
    "Bầu trời hôm nay trong xanh.", "Lá cây rơi đầy sân.", "Em bé đang ngủ ngon lành.", "Hoa hồng nở đỏ thắm.", "Chim sâu hót líu lo.",
    "Mẹ nấu cơm cho cả nhà.", "Trên cành, những chú chim đang hót.", "Gió thổi nhè nhẹ qua cánh đồng.",
]
NHAN_HOA = [
    "Chú gà trống cất tiếng gáy chào buổi sáng.", "Cây bàng đứng lặng lẽ giữa sân trường.", "Bác gió rì rào kể chuyện cho lá nghe.",
    "Mặt trời mỉm cười chào ngày mới.", "Chị gió đưa chiếc diều bay cao.", "Cô mưa tắm mát cho cây cối.", "Ông mặt trời thức dậy từ sớm.",
    "Dòng sông thủ thỉ kể chuyện với bờ cát.", "Chú mèo lười biếng nằm phơi nắng.", "Những chú ong chăm chỉ đi tìm mật hoa.",
    "Bác bếp lửa đang thức suốt đêm.", "Cây tre bảo vệ làng xóm như người lính canh.",
]
KHONG_NH = [
    "Gà trống gáy sáng.", "Gió thổi xào xạc.", "Cây bàng có nhiều lá.", "Mưa rơi tí tách.", "Ong bay đi tìm mật.", "Sông chảy qua làng.",
    "Mặt trời mọc ở đằng đông.", "Mèo bắt chuột trong bếp.", "Trời nắng to.", "Em tưới cây ngoài vườn.",
]
# ---- Ai là gì? Ai làm gì? Ai thế nào? --------------------------------------------------
CAU3 = [
    ("Bố em đang sửa xe.", "Ai làm gì?"), ("Chị Lan quét nhà.", "Ai làm gì?"), ("Bà em kể chuyện cổ tích.", "Ai làm gì?"),
    ("Các bạn nhỏ chơi đá cầu.", "Ai làm gì?"), ("Mẹ nấu bữa cơm chiều.", "Ai làm gì?"), ("Nam tưới cây ngoài vườn.", "Ai làm gì?"),
    ("Cô giáo giảng bài.", "Ai làm gì?"), ("Con mèo bắt chuột.", "Ai làm gì?"),
    ("Bạn Hoa rất chăm chỉ.", "Ai thế nào?"), ("Cánh đồng rộng mênh mông.", "Ai thế nào?"), ("Con voi to lớn.", "Ai thế nào?"),
    ("Mái tóc bà bạc trắng.", "Ai thế nào?"), ("Chú mèo rất lười.", "Ai thế nào?"), ("Bầu trời hôm nay trong xanh.", "Ai thế nào?"),
    ("Lớp em đoàn kết.", "Ai thế nào?"), ("Bông hoa thơm ngát.", "Ai thế nào?"),
    ("Bố em là bác sĩ.", "Ai là gì?"), ("Hà Nội là thủ đô của nước ta.", "Ai là gì?"), ("Lan là học sinh giỏi.", "Ai là gì?"),
    ("Cô Hoa là giáo viên.", "Ai là gì?"), ("Cá voi là loài động vật biển lớn nhất.", "Ai là gì?"), ("Con trâu là bạn của nhà nông.", "Ai là gì?"),
    ("Hà là lớp trưởng của lớp em.", "Ai là gì?"), ("Sông Hồng là dòng sông lớn của miền Bắc.", "Ai là gì?"),
]
LABEL3 = ["Ai là gì?", "Ai làm gì?", "Ai thế nào?", "Câu hỏi"]
# (câu, bộ phận hỏi, câu hỏi)
HOI_BP = [
    ("Bố em đang sửa xe.", "Bố em", "Ai đang sửa xe?"), ("Bố em đang sửa xe.", "đang sửa xe", "Bố em đang làm gì?"),
    ("Chị Lan quét nhà.", "Chị Lan", "Ai quét nhà?"), ("Chị Lan quét nhà.", "quét nhà", "Chị Lan làm gì?"),
    ("Bà em kể chuyện cổ tích.", "Bà em", "Ai kể chuyện cổ tích?"), ("Bà em kể chuyện cổ tích.", "kể chuyện cổ tích", "Bà em làm gì?"),
    ("Con mèo bắt chuột.", "Con mèo", "Con gì bắt chuột?"), ("Con mèo bắt chuột.", "bắt chuột", "Con mèo làm gì?"),
    ("Bạn Hoa rất chăm chỉ.", "Bạn Hoa", "Ai rất chăm chỉ?"), ("Bạn Hoa rất chăm chỉ.", "rất chăm chỉ", "Bạn Hoa thế nào?"),
    ("Cánh đồng rộng mênh mông.", "Cánh đồng", "Cái gì rộng mênh mông?"), ("Cánh đồng rộng mênh mông.", "rộng mênh mông", "Cánh đồng thế nào?"),
    ("Bông hoa thơm ngát.", "Bông hoa", "Cái gì thơm ngát?"), ("Bông hoa thơm ngát.", "thơm ngát", "Bông hoa thế nào?"),
    ("Hà Nội là thủ đô của nước ta.", "Hà Nội", "Cái gì là thủ đô của nước ta?"), ("Hà Nội là thủ đô của nước ta.", "thủ đô của nước ta", "Hà Nội là gì?"),
    ("Bố em là bác sĩ.", "Bố em", "Ai là bác sĩ?"), ("Bố em là bác sĩ.", "bác sĩ", "Bố em là gì?"),
    ("Lan là học sinh giỏi.", "Lan", "Ai là học sinh giỏi?"), ("Lan là học sinh giỏi.", "học sinh giỏi", "Lan là gì?"),
]
# ---- câu kể/hỏi/cảm/khiến ----------------------------------------------------------------
KIEU4 = [
    ("Hôm nay trời nắng đẹp.", "Câu kể"), ("Em đang làm bài tập.", "Câu kể"), ("Mẹ đi làm về.", "Câu kể"), ("Cả nhà ăn cơm tối.", "Câu kể"),
    ("Lan là học sinh giỏi.", "Câu kể"), ("Bạn đã làm xong bài tập chưa?", "Câu hỏi"), ("Ai đã hái hoa trong vườn?", "Câu hỏi"),
    ("Vì sao bạn đến muộn?", "Câu hỏi"), ("Mẹ đang làm gì đấy?", "Câu hỏi"), ("Bao giờ lớp mình đi dã ngoại?", "Câu hỏi"),
    ("Ôi, bông hoa đẹp quá!", "Câu cảm"), ("Chà, bạn vẽ đẹp thật!", "Câu cảm"), ("Trời ơi, mưa to quá!", "Câu cảm"),
    ("Cảnh đẹp biết bao!", "Câu cảm"), ("Hoan hô, đội mình thắng rồi!", "Câu cảm"),
    ("Hãy giữ yên lặng!", "Câu khiến"), ("Con đi ngủ sớm đi!", "Câu khiến"), ("Bạn cho mình mượn cây bút nhé!", "Câu khiến"),
    ("Đề nghị các bạn trật tự.", "Câu khiến"), ("Xin mời bác ngồi.", "Câu khiến"),
]
LABEL4 = ["Câu kể", "Câu hỏi", "Câu cảm", "Câu khiến"]
# ---- chủ ngữ / vị ngữ -----------------------------------------------------------------------
CN_VN = [
    ("Bạn Lan chăm chỉ học bài.", "Bạn Lan", "chăm chỉ học bài"), ("Những chú chim hót líu lo.", "Những chú chim", "hót líu lo"),
    ("Mẹ em đang nấu cơm.", "Mẹ em", "đang nấu cơm"), ("Dòng sông chảy hiền hòa.", "Dòng sông", "chảy hiền hòa"),
    ("Cô giáo giảng bài rất hay.", "Cô giáo", "giảng bài rất hay"), ("Bố em là kĩ sư.", "Bố em", "là kĩ sư"),
    ("Cánh đồng lúa chín vàng rực.", "Cánh đồng lúa", "chín vàng rực"), ("Em bé ngủ ngon lành.", "Em bé", "ngủ ngon lành"),
    ("Ông em trồng rất nhiều cây.", "Ông em", "trồng rất nhiều cây"), ("Các bạn học sinh đang chơi đá cầu.", "Các bạn học sinh", "đang chơi đá cầu"),
    ("Mặt trời đỏ ối như quả cầu lửa.", "Mặt trời", "đỏ ối như quả cầu lửa"), ("Con mèo nằm phơi nắng.", "Con mèo", "nằm phơi nắng"),
    ("Chiếc cặp của em màu xanh.", "Chiếc cặp của em", "màu xanh"), ("Trường em có nhiều cây xanh.", "Trường em", "có nhiều cây xanh"),
]
# ---- danh từ riêng / chung ------------------------------------------------------------------
DT_RIENG = ["Hà Nội", "Sông Hồng", "Việt Nam", "Nguyễn Du", "Trần Hưng Đạo", "Thái Bình", "Hồ Chí Minh", "Hải Phòng", "Đà Nẵng",
            "Cửu Long", "Trường Sơn", "Hồ Gươm", "Vịnh Hạ Long", "Cà Mau", "Phú Quốc", "Lê Lợi", "Cần Thơ", "Sa Pa"]
DT_CHUNG = ["thành phố", "dòng sông", "đất nước", "nhà thơ", "tỉnh", "anh hùng", "ngọn núi", "hồ nước", "vịnh", "thủ đô", "nhà văn",
            "con sông", "quận", "làng", "cô giáo", "học sinh", "thị xã", "dãy núi"]
# ---- dấu câu ----------------------------------------------------------------------------------
DAU_CUOI = [("Ôi, bông hoa đẹp quá", "!"), ("Bạn đang đọc sách gì", "?"), ("Em quét sân", "."), ("Chà, bạn vẽ giỏi thật", "!"),
            ("Mẹ đi chợ từ sáng sớm", "."), ("Hôm nay bạn có đi học không", "?"), ("Trời ơi, mưa to quá", "!"),
            ("Vì sao lá cây có màu xanh", "?"), ("Cả nhà ngồi ăn cơm", "."), ("Thỏ đang ăn cà rốt ngoài vườn", "."),
            ("Ai đã làm đổ mực ra bàn", "?"), ("Hoan hô, đội ta thắng rồi", "!"), ("Em học bài xong rồi", "."), ("Bao giờ cả nhà đi chơi", "?")]
DAU_PHAY = [("Trong vườn có hoa hồng___ hoa cúc___ hoa huệ.", "dấu phẩy"), ("Em mua vở___ bút___ thước kẻ.", "dấu phẩy"),
            ("Mùa xuân___ cây cối đâm chồi nảy lộc.", "dấu phẩy"), ("Mẹ em đi chợ___ nấu cơm___ giặt quần áo.", "dấu phẩy")]
# (câu, dấu, chức năng)
CN_CHUC = {
    "A": "Báo hiệu lời nói trực tiếp của nhân vật",
    "B": "Báo hiệu phần liệt kê hoặc giải thích",
    "C": "Đánh dấu lời nói trực tiếp hoặc lời trích dẫn",
    "D": "Đánh dấu tên tác phẩm hoặc từ ngữ dùng với nghĩa đặc biệt",
    "E": "Đánh dấu chỗ bắt đầu lời nói của nhân vật trong đối thoại",
    "F": "Nối các từ ngữ trong một liên danh",
}
DAU_CN = [
    ("Mẹ dặn: “Con nhớ đóng cửa nhé!”", "dấu hai chấm", "A"),
    ("Cô giáo hỏi: “Ai làm xong bài rồi?”", "dấu hai chấm", "A"),
    ("Trong vườn có nhiều loại hoa: hồng, cúc, huệ, lan.", "dấu hai chấm", "B"),
    ("Nhà em có ba người: bố, mẹ và em.", "dấu hai chấm", "B"),
    ("Bố khen: “Con tiến bộ nhiều lắm!”", "dấu ngoặc kép", "C"),
    ("Cô giáo nói: “Các em hãy giữ gìn lớp học sạch đẹp.”", "dấu ngoặc kép", "C"),
    ("Em rất thích bài thơ “Tre Việt Nam”.", "dấu ngoặc kép", "D"),
    ("Cả lớp gọi bạn Nam là “nhà bác học nhỏ”.", "dấu ngoặc kép", "D"),
    ("— Hôm nay cậu đi học à? — Nam hỏi.", "dấu gạch ngang", "E"),
    ("— Con đã làm xong bài chưa? — mẹ hỏi.", "dấu gạch ngang", "E"),
]
# ---- thành ngữ, tục ngữ ------------------------------------------------------------------------
TUC_NGU = [
    ("Có công mài sắt, có ngày nên kim.", "Kiên trì, nhẫn nại thì việc khó cũng thành công."),
    ("Uống nước nhớ nguồn.", "Phải biết ơn những người đã tạo ra thành quả cho mình hưởng."),
    ("Ăn quả nhớ kẻ trồng cây.", "Phải biết ơn những người đã giúp đỡ mình."),
    ("Lá lành đùm lá rách.", "Người có điều kiện phải giúp đỡ, đùm bọc người gặp khó khăn."),
    ("Một cây làm chẳng nên non, ba cây chụm lại nên hòn núi cao.", "Đoàn kết lại thì có sức mạnh lớn."),
    ("Có chí thì nên.", "Có ý chí, quyết tâm thì sẽ thành công."),
    ("Học thầy không tày học bạn.", "Học hỏi ở bạn bè cũng rất quan trọng."),
    ("Tốt gỗ hơn tốt nước sơn.", "Phẩm chất bên trong quan trọng hơn vẻ đẹp bề ngoài."),
    ("Thương người như thể thương thân.", "Yêu thương người khác như yêu chính bản thân mình."),
    ("Đi một ngày đàng, học một sàng khôn.", "Đi nhiều nơi sẽ học hỏi, hiểu biết được nhiều điều."),
    ("Gần mực thì đen, gần đèn thì sáng.", "Môi trường, bạn bè có ảnh hưởng lớn đến con người."),
    ("Nước chảy đá mòn.", "Kiên trì, bền bỉ thì việc gì cũng làm được."),
    ("Kính trên nhường dưới.", "Kính trọng người trên, nhường nhịn người dưới."),
    ("Thất bại là mẹ thành công.", "Từ thất bại rút ra bài học thì sẽ thành công."),
]
# (khung có ___, từ đúng)
TN_DIEN = [
    ("Có công mài sắt, có ngày nên ___.", "kim"), ("Uống nước nhớ ___.", "nguồn"), ("Ăn quả nhớ kẻ trồng ___.", "cây"),
    ("Lá lành đùm lá ___.", "rách"), ("Có chí thì ___.", "nên"), ("Học thầy không tày học ___.", "bạn"),
    ("Thương người như thể thương ___.", "thân"), ("Đi một ngày đàng, học một sàng ___.", "khôn"),
    ("Gần mực thì đen, gần đèn thì ___.", "sáng"), ("Nước chảy đá ___.", "mòn"), ("Tốt gỗ hơn tốt nước ___.", "sơn"),
    ("Kính trên nhường ___.", "dưới"), ("Chậm như ___.", "rùa"), ("Nhanh như ___.", "chớp"), ("Khỏe như ___.", "voi"),
    ("Đẹp như ___.", "tiên", ["rùa", "kiến", "chì"]), ("Hiền như ___.", "bụt"), ("Lạnh như ___.", "tiền", ["rùa", "kiến", "son"]), ("Trắng như ___.", "tuyết", ["tiền", "rùa", "chớp"]),
    ("Đỏ như ___.", "son"), ("Nhẹ như ___.", "bấc", ["voi", "chì", "kiến"]), ("Nặng như ___.", "chì", ["tiên", "bụt", "son"]), ("Cứng như ___.", "đá", ["tuyết", "bụt", "kiến"]), ("Đông như ___.", "kiến"),
]
THANH_NGU_NGHIA = [
    ("Chậm như rùa", "Rất chậm chạp."), ("Nhanh như chớp", "Rất nhanh."), ("Khỏe như voi", "Rất khỏe."),
    ("Đẹp như tiên", "Rất đẹp."), ("Hiền như bụt", "Rất hiền lành."), ("Lạnh như tiền", "Rất lạnh (hoặc thờ ơ, lạnh nhạt)."),
    ("Nhường cơm sẻ áo", "Chia sẻ, giúp đỡ nhau lúc khó khăn."), ("Chung lưng đấu cật", "Đoàn kết, cùng nhau làm việc."),
    ("Ăn ngay nói thẳng", "Thật thà, nói đúng sự thật."), ("Đồng tâm hiệp lực", "Cùng một lòng, cùng góp sức làm việc."),
    ("Nhẹ như bấc", "Rất nhẹ."), ("Nặng như chì", "Rất nặng."),
]

TUC_NHOM = {
    "Có công mài sắt, có ngày nên kim.": "kiên trì", "Nước chảy đá mòn.": "kiên trì", "Có chí thì nên.": "kiên trì", "Thất bại là mẹ thành công.": "kiên trì",
    "Uống nước nhớ nguồn.": "biết ơn", "Ăn quả nhớ kẻ trồng cây.": "biết ơn",
    "Lá lành đùm lá rách.": "đoàn kết", "Thương người như thể thương thân.": "đoàn kết", "Một cây làm chẳng nên non, ba cây chụm lại nên hòn núi cao.": "đoàn kết",
    "Học thầy không tày học bạn.": "học hỏi", "Đi một ngày đàng, học một sàng khôn.": "học hỏi", "Gần mực thì đen, gần đèn thì sáng.": "học hỏi",
    "Tốt gỗ hơn tốt nước sơn.": "phẩm chất", "Kính trên nhường dưới.": "lễ phép",
}
