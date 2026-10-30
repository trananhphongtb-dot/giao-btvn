package vn.giaobtvn.tieuhoc.data

import java.text.Normalizer

// ============================================================================
// PHÂN LOẠI TỰ ĐỘNG (GỢI Ý, KHÔNG PHẢI ĐÁP ÁN TUYỆT ĐỐI) — bản sửa 11:17.
// Cô BẮT BUỘC xét lại tag và mức độ ở màn duyệt trước khi câu vào ngân
// hàng; giá trị sau khi cô sửa mới là giá trị được lưu. Độ chính xác phụ
// thuộc vào text gốc (hoặc OCR): text càng rõ, gợi ý càng đúng.
// ============================================================================

/** Kết quả phân loại gợi ý cho 1 câu hỏi. */
data class PhanLoaiGoiY(
    val tags: List<String>,
    /** Mức độ gợi ý 1..3, hoặc null nếu không gợi ý được (cô tự gắn). */
    val doKhoGoiY: Int?,
    /** Giải thích bằng tiếng Việt để cô hiểu vì sao máy gợi ý như vậy. */
    val lyDo: String,
)

/**
 * Chuẩn hóa text về không dấu để so khớp từ khóa cho chắc: "đường tròn"
 * thành "duong tron", "tọa độ" thành "toa do". Text gốc có dấu vẫn được
 * giữ nguyên để hiển thị, hàm này chỉ dùng cho việc so khớp.
 */
fun chuanHoaKhongDau(text: String): String {
    val khongDau = Normalizer.normalize(text, Normalizer.Form.NFD)
        .replace(Regex("\\p{Mn}+"), "")
        .replace('đ', 'd')
        .replace('Đ', 'D')
    // Chỉ giữ chữ, số và khoảng trắng để so khớp từ khóa không bị lệch
    // bởi dấu câu; "x^2" thành "x 2" nên bậc 2 dạng x^2/x² được kiểm tra
    // riêng trên text gốc trước khi chuẩn hóa, xem classifyQuestion.
    return khongDau.lowercase()
        .replace(Regex("[^a-z0-9 ]+"), " ")
        .replace(Regex("\\s+"), " ")
        .trim()
}

private fun coTuKhoa(textChuanHoa: String, tuKhoa: String): Boolean {
    if (tuKhoa.isBlank()) return false
    val padded = " $textChuanHoa "
    // Từ khóa nhiều từ thì so khớp chuỗi có khoảng trắng ở 2 đầu; từ
    // khóa 1 từ thì vẫn khớp đúng từ, không khớp nửa từ khác (ví dụ
    // "tru" không khớp trong "trung" vì có khoảng trắng bao quanh).
    return padded.contains(" $tuKhoa ")
}

/**
 * Bảng từ khóa -> tag, theo thứ tự định nghĩa. Một câu có thể nhận NHIỀU
 * tag, ví dụ "đường tròn + Oxy + bậc 2" hoặc "phương trình bậc 2 + bậc 1".
 * Từ khóa đã chuẩn hóa không dấu, so khớp trên text đã chuẩn hóa.
 */
private val bangTuKhoa: List<Pair<String, List<String>>> = listOf(
    "DUONG_TRON" to listOf("duong tron", "ban kinh", "tiep tuyen"),
    "OXY" to listOf("oxy", "toa do", "he toa do"),
    "PHUONG_TRINH" to listOf("phuong trinh", "giai he"),
    "BAC_2" to listOf("bac 2", "bac hai"),
    "BAC_1" to listOf("bac 1", "bac nhat", "bac mot"),
    "HAM_SO" to listOf("ham so"),
    "HINH_HOC" to listOf("hinh"),
    "DIEN_TICH" to listOf("dien tich"),
    "CHU_VI" to listOf("chu vi"),
    "THE_TICH" to listOf("the tich"),
    "PHAN_SO" to listOf("phan so"),
    "SO_THAP_PHAN" to listOf("so thap phan"),
    "CONG" to listOf("cong", "phep cong", "tong"),
    "TRU" to listOf("tru", "phep tru", "hieu"),
    "NHAN" to listOf("nhan", "phep nhan"),
    "CHIA" to listOf("chia", "phep chia"),
    "DANH_TU" to listOf("danh tu"),
    "DONG_TU" to listOf("dong tu"),
    "TINH_TU" to listOf("tinh tu"),
    "CHINH_TA" to listOf("chinh ta"),
    "TAP_DOC" to listOf("tap doc"),
    "THUC_VAT" to listOf("thuc vat"),
    "DONG_VAT" to listOf("dong vat"),
    "CO_THE_NGUOI" to listOf("co the"),
    "ANH_SANG" to listOf("anh sang"),
    "AM_THANH" to listOf("am thanh"),
    "TRAI_DAT" to listOf("trai dat"),
    "MAT_TROI" to listOf("mat troi"),
)

/**
 * Gợi ý tag nội dung + mức độ cho 1 câu hỏi từ text gốc (text tách từ
 * file có chữ). Text null hoặc rỗng (câu cắt từ ảnh scan, chưa có OCR
 * toàn văn) thì không gợi ý được gì, trả về tags rỗng và doKho null để
 * cô tự gắn ở màn duyệt, không đoán mò.
 *
 * Heuristic mức độ, GHI RÕ là gợi ý:
 * - 3 nếu từ 3 tag trở lên (ví dụ đường tròn + Oxy + bậc 2), hoặc có
 *   "chứng minh" kèm từ 2 tag trở lên.
 * - 2 nếu đúng 2 tag, hoặc 1 tag nhưng câu dài trên 200 ký tự, hoặc có
 *   "chứng minh".
 * - 1 nếu 1 tag và câu ngắn, hoặc không nhận ra tag nào (lúc này mức độ
 *   1 cũng chỉ là giá trị mặc định để cô sửa, không phải kết luận).
 */
fun classifyQuestion(textGoc: String?): PhanLoaiGoiY {
    if (textGoc.isNullOrBlank()) {
        return PhanLoaiGoiY(
            tags = emptyList(),
            doKhoGoiY = null,
            lyDo = "Không có text để gợi ý (câu cắt từ ảnh), cô tự gắn tag và mức độ.",
        )
    }
    val textThap = textGoc.lowercase()
    val chuanHoa = chuanHoaKhongDau(textGoc)
    val tags = mutableListOf<String>()
    for ((tag, tuKhoas) in bangTuKhoa) {
        if (tuKhoas.any { coTuKhoa(chuanHoa, it) }) {
            tags.add(tag)
        }
    }
    // Bậc 2 dạng ký hiệu: "x^2" hoặc "x²" bị chuẩn hóa thành "x 2" nên
    // phải kiểm tra trên text gốc trước khi chuẩn hóa.
    if (("x^2" in textThap || "x²" in textThap) && "BAC_2" !in tags) {
        // Chèn BAC_2 ngay sau PHUONG_TRINH nếu có, để thứ tự tag dễ đọc.
        val viTri = tags.indexOf("PHUONG_TRINH").let { if (it >= 0) it + 1 else tags.size }
        tags.add(viTri, "BAC_2")
    }
    val coChungMinh = coTuKhoa(chuanHoa, "chung minh")
    val doKho = when {
        tags.size >= 3 -> 3
        coChungMinh && tags.size >= 2 -> 3
        tags.size == 2 -> 2
        coChungMinh -> 2
        tags.size == 1 && textGoc.length > 200 -> 2
        else -> 1
    }
    val lyDo = if (tags.isEmpty()) {
        "Máy chưa nhận ra thẻ nội dung nào từ câu này, mức độ 1 chỉ là " +
            "giá trị mặc định, cô tự gắn lại ở màn duyệt."
    } else {
        "Gợi ý từ ${tags.size} thẻ: ${tags.joinToString(", ")}" +
            if (coChungMinh) " (có yêu cầu chứng minh nên tăng mức độ)" else ""
    }
    return PhanLoaiGoiY(tags = tags, doKhoGoiY = doKho, lyDo = lyDo)
}
