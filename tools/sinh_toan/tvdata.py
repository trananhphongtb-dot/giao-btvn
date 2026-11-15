"""Kho từ ngữ dùng chung cho Tiếng Việt lớp 1–5 (soạn tay, đã rà)."""

# ---- từ loại ------------------------------------------------------------------
DT = ["học sinh", "cô giáo", "bác sĩ", "nông dân", "con trâu", "dòng sông", "cánh đồng", "ngôi nhà", "quyển sách", "bông hoa",
      "cơn mưa", "ngọn núi", "mặt trời", "bầu trời", "thành phố", "làng quê", "cây bàng", "chiếc cặp", "ánh nắng", "tiếng hát",
      "niềm vui", "nỗi buồn", "tuổi thơ", "cuộc sống", "tình bạn", "kỉ niệm", "con đường", "ngôi trường", "chú bộ đội", "bầy chim"]
DGT = ["chạy", "nhảy", "đọc", "viết", "hát", "múa", "ngủ", "bơi", "leo", "trồng", "tưới", "gặt", "cấy", "xây", "vẽ", "nghĩ", "nhớ",
       "yêu", "thương", "ngắm", "lắng nghe", "giặt", "quét", "nấu", "kể", "hỏi", "đáp", "ca hát", "vui chơi", "học"]
TT = ["đẹp", "xấu", "cao", "thấp", "xanh", "đỏ", "nhanh", "chậm", "ngoan", "chăm chỉ", "hiền lành", "vui vẻ", "buồn bã", "rộng",
      "hẹp", "sạch sẽ", "thơm", "ngọt", "lạnh", "nóng", "mênh mông", "bát ngát", "dũng cảm", "thông minh", "trong xanh", "rực rỡ",
      "mềm mại", "yên tĩnh", "ồn ào", "xinh xắn"]
TINH_CAM = ["yêu thương", "kính trọng", "biết ơn", "thân thiết", "quý mến", "tự hào", "lo lắng", "vui mừng", "nhớ nhung", "căm ghét",
            "hãnh diện", "xúc động", "ngưỡng mộ", "thương mến"]
SV_COI = {
    "con vật": ["con gà", "con vịt", "con chó", "con mèo", "con trâu", "con bò", "con cá", "con voi", "con khỉ", "con thỏ", "con ngựa", "con hổ"],
    "cây cối": ["cây chuối", "cây dừa", "cây bưởi", "cây cam", "cây xoài", "cây tre", "cây hoa hồng", "cây lúa", "cây mít", "cây ổi"],
    "đồ vật": ["cái bàn", "cái ghế", "quyển vở", "cái bút", "cái cặp", "cái nồi", "cái bát", "cái đèn", "cái quạt", "chiếc xe"],
    "người": ["bố", "mẹ", "ông", "bà", "anh", "chị", "cô giáo", "bác sĩ", "bác nông dân", "chú bộ đội"],
}

# ---- trái nghĩa / đồng nghĩa ---------------------------------------------------
TRAI = [("to", "nhỏ"), ("cao", "thấp"), ("dài", "ngắn"), ("nóng", "lạnh"), ("sáng", "tối"), ("nhanh", "chậm"), ("mới", "cũ"),
        ("đẹp", "xấu"), ("khóc", "cười"), ("vui", "buồn"), ("ngày", "đêm"), ("trên", "dưới"), ("trong", "ngoài"), ("già", "trẻ"),
        ("béo", "gầy"), ("nặng", "nhẹ"), ("mở", "đóng"), ("đúng", "sai"), ("ngoan", "hư"), ("sạch", "bẩn"), ("xa", "gần"),
        ("rộng", "hẹp"), ("tốt", "xấu"), ("hiền", "dữ"), ("siêng năng", "lười biếng"), ("dũng cảm", "hèn nhát"),
        ("trung thực", "gian dối"), ("giàu", "nghèo"), ("mạnh", "yếu"), ("hạnh phúc", "đau khổ"), ("chiến tranh", "hòa bình"),
        ("thắng", "thua"), ("sống", "chết"), ("yêu", "ghét"), ("đoàn kết", "chia rẽ"), ("khiêm tốn", "kiêu ngạo"), ("lên", "xuống"),
        ("trước", "sau"), ("đầu", "cuối"), ("nhiều", "ít"), ("sớm", "muộn"), ("khen", "chê"), ("dày", "mỏng"), ("nông", "sâu"),
        ("cứng", "mềm"), ("khô", "ướt"), ("thẳng", "cong"), ("chua", "ngọt"), ("đắt", "rẻ"), ("thật thà", "dối trá"), ("cho", "nhận")]
DONG = [("chăm chỉ", "siêng năng"), ("to lớn", "khổng lồ"), ("đẹp", "xinh"), ("nhanh", "mau"), ("bao la", "mênh mông"),
        ("dũng cảm", "gan dạ"), ("học sinh", "học trò"), ("ba", "bố"), ("mẹ", "má"), ("quê hương", "quê nhà"), ("tổ quốc", "đất nước"),
        ("siêng năng", "cần cù"), ("thông minh", "sáng dạ"), ("trung thực", "thật thà"), ("hiền lành", "hiền hậu"), ("lười biếng", "lười nhác"),
        ("vui mừng", "phấn khởi"), ("buồn bã", "u sầu"), ("yên lặng", "im lặng"), ("rộng lớn", "bao la"), ("xinh xắn", "xinh đẹp"),
        ("bé", "nhỏ"), ("ngôi nhà", "căn nhà"), ("nhìn", "xem"), ("nói", "bảo"), ("cha", "bố"), ("tặng", "biếu"),
        ("giúp", "giúp đỡ")]

# ---- chính tả ------------------------------------------------------------------
CH_TR = ["chăm chỉ", "chậm chạp", "trong trẻo", "chói chang", "chen chúc", "chắc chắn", "trắng trẻo", "chuyện trò", "trầm trồ",
         "chùng chình", "chông chênh", "trơn tru", "trắc trở", "trăn trở", "chăm chút", "trung trực", "trống trải", "trập trùng"]
S_X = ["xinh xắn", "sạch sẽ", "sáng suốt", "xanh xao", "xôn xao", "xào xạc", "sôi sục", "xa xôi", "sắp xếp", "sần sùi", "sâu sắc",
       "sung sướng", "xum xuê", "san sẻ", "sáng sủa", "xấu xa", "xúm xít", "sâu xa"]
L_N = ["lung linh", "nô nức", "long lanh", "lấp lánh", "nõn nà", "lả lướt", "nao núng", "lo lắng", "nặng nề", "lơ lửng", "nung nấu",
       "lanh lợi", "lên lớp", "lạnh lẽo", "lặng lẽ", "nỗ lực", "no nê", "nảy nở", "nồng nàn"]
D_GI_R = ["giữ gìn", "rì rào", "dịu dàng", "rộn ràng", "giản dị", "rực rỡ", "dập dờn", "giặt giũ", "rung rinh", "dè dặt", "gieo giống",
          "rạng rỡ", "dạy dỗ", "rảnh rỗi", "giận dữ", "rón rén", "giành giật", "dành dụm", "rộng rãi", "giục giã"]
THANH = ["sửa chữa", "ngẫm nghĩ", "dễ dãi", "rảnh rỗi", "thỉnh thoảng", "nhõng nhẽo", "lủng củng", "ủ rũ", "lả tả", "hể hả",
         "lẩn thẩn", "rủ rỉ", "kể lể", "nhổ cỏ"]
# ---- từ ghép / từ láy -----------------------------------------------------------
GHEP = ["bàn ghế", "quần áo", "sách vở", "cha mẹ", "anh em", "đất nước", "trường học", "nhà cửa", "giày dép", "ruộng đồng", "sông núi",
        "cây cối", "ăn uống", "học hành", "nhà máy", "xe đạp", "bút chì", "hoa hồng", "cá chép", "tàu hỏa", "áo dài", "nước mắm",
        "bánh chưng", "xe máy", "hoa sen", "nhà sàn"]
LAY = ["lung linh", "long lanh", "xinh xắn", "lấp lánh", "rì rào", "thì thầm", "lao xao", "xào xạc", "bập bềnh", "mênh mông", "thăm thẳm",
       "đo đỏ", "nhỏ nhắn", "ngoan ngoãn", "nhè nhẹ", "róc rách", "thập thò", "khấp khểnh", "lom khom", "chói chang", "lấm tấm", "tí tách",
       "lả tả", "rì rầm", "thoang thoảng", "lác đác"]
