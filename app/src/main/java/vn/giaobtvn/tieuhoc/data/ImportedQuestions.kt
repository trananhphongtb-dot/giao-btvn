package vn.giaobtvn.tieuhoc.data

import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.Typeface
import java.util.UUID

// ============================================================================
// CÂU HỎI NHẬP TỪ FILE — NGÂN HÀNG CHUNG (chốt 2026-11-01): câu cô nào
// tạo/up rồi thì giáo viên khác cũng dùng được, không còn ngân hàng
// riêng theo từng cô nữa. Câu cũ lưu riêng vẫn đọc được để dùng nốt,
// nhưng câu mới luôn lưu vào cây nganHangChung. Cách cắt đã chốt:
// CẮT TỰ ĐỘNG + CÔ DUYỆT LẠI, không giao câu nào chưa qua màn duyệt.
// ============================================================================

/** VIET = bài viết làm ra giấy, TRAC_NGHIEM_ANH = trắc nghiệm, đề là ảnh từng câu. */
enum class DangBai { VIET, TRAC_NGHIEM_ANH }

/** NHAP = vừa cắt xong, chưa qua duyệt; DA_DUYET = cô đã chốt, được giao. */
enum class TrangThaiCauNhap { NHAP, DA_DUYET }

data class ImportedQuestion(
    val id: String = "",
    val giaoVienId: String = "",
    val mon: String = "",
    /** Khối lớp, ví dụ "Lớp 4", khác với "lớp học" là nhóm học sinh cụ thể. */
    val khoi: String = "",
    val chuong: String = "",
    /**
     * Bài: TẠM THỜI KHÔNG DÙNG để phân nhánh (bản sửa 11:17). Câu nhập mới
     * chỉ phân nhánh theo Môn/Chương; trường này để nullable cho câu cũ
     * hoặc để trống, không bắt buộc nhập ở UI nhập.
     */
    val bai: String? = null,
    val dang: String = "VIET",
    /** Ảnh câu hỏi, Base64 (JPEG 1024px, chất lượng 70, như ảnh bài giấy ở V1). */
    val anhBase64: String = "",
    /** Text gốc nếu tách từ file có lớp chữ, null/rỗng nếu tách từ ảnh scan. */
    val textGoc: String? = null,
    /** Chỉ số đáp án đúng 0..3, chỉ có ý nghĩa với trắc nghiệm ảnh. */
    val dapAnDung: Int? = null,
    val doKho: Int? = null,
    val trangThai: String = "DA_DUYET",
    val nguonFile: String = "",
    val thuTu: Int = 0,
    val soLanGiao: Int = 0,
    /** Độ tin cậy 0..100, chỉ có ý nghĩa với câu cắt từ OCR, text thì 100. */
    val doTinCay: Int = 100,
    /** Thẻ nội dung sau khi cô sửa ở màn duyệt, ví dụ DUONG_TRON, OXY, BAC_2. */
    val tags: List<String> = emptyList(),
    /**
     * Cờ đóng góp cũ: giữ lại để đọc câu cũ, câu mới trong ngân hàng
     * chung không còn phân biệt riêng/chung bằng cờ này nữa.
     */
    val nguonDongGop: String = "",
    /** Chuyên đề của câu, ví dụ: "Đường tròn", "Phân số" — trục lọc thứ 3 của ngân hàng chung. */
    val chuyenDe: String = "",
    /** Tên người tạo câu, để ngân hàng chung hiện rõ ai tạo, ai sửa được. */
    val giaoVienTen: String = "",
) {
    constructor() : this("", "", "", "", "", null, "VIET", "", null, null, null, "DA_DUYET", "", 0, 0, 100, emptyList(), "", "", "")

    val dangEnum: DangBai
        get() = if (dang == "TRAC_NGHIEM_ANH") DangBai.TRAC_NGHIEM_ANH else DangBai.VIET

    fun toMap(): Map<String, Any?> = mapOf(
        "id" to id,
        "giaoVienId" to giaoVienId,
        "mon" to mon,
        "khoi" to khoi,
        "chuong" to chuong,
        "bai" to bai,
        "dang" to dang,
        "anhBase64" to anhBase64,
        "textGoc" to textGoc,
        "dapAnDung" to dapAnDung,
        "doKho" to doKho,
        "trangThai" to trangThai,
        "nguonFile" to nguonFile,
        "thuTu" to thuTu,
        "soLanGiao" to soLanGiao,
        "doTinCay" to doTinCay,
        "tags" to tags,
        "nguonDongGop" to nguonDongGop,
        "chuyenDe" to chuyenDe,
        "giaoVienTen" to giaoVienTen,
    )

    /**
     * Đổi câu hỏi ảnh thành CauHoi để học sinh làm bài trắc nghiệm bằng
     * chung một luồng chấm điểm với ngân hàng assets: đáp án hiển thị là
     * 4 chữ cái A/B/C/D, đáp án đúng là chỉ số cô đã chọn. laCauAnh = true
     * để hàm trộn không xáo thứ tự A/B/C/D (xáo chữ cái sẽ làm học sinh
     * không biết chọn theo ảnh nữa).
     */
    fun toCauHoi(): CauHoi = CauHoi(
        id = id,
        chuDe = mon,
        bai = bai ?: "",
        chuong = chuong,
        noiDung = textGoc?.takeIf { it.isNotBlank() } ?: "Câu hỏi dạng ảnh — xem ảnh câu hỏi bên dưới",
        cacDapAn = listOf("A", "B", "C", "D"),
        dapAnDung = dapAnDung ?: 0,
        doKho = doKho ?: 1,
        laCauAnh = true,
    )
}

/**
 * Một ứng viên câu hỏi sau bước cắt thử, chưa qua duyệt. Các trường
 * mon/chuong/tags/doKhoGoiY là giá trị GỢI Ý hoặc giá trị cô đang sửa
 * ở màn duyệt; chỉ khi cô bấm Chốt thì giá trị này mới được lưu vào
 * ngân hàng, không câu nào vào ngân hàng khi chưa qua duyệt.
 */
data class SplitCandidate(
    val anhBase64: String = "",
    val textGoc: String? = null,
    /** Số câu máy đoán được từ đầu câu ("Câu N"), 0 = đoạn mở đầu/tiêu đề. */
    val soCauDuDoan: Int = 0,
    /** Các cờ cảnh báo, ví dụ: DOAN_MO_DAU, TRAN_TRANG, OCR_THAP, CAN_KIEM_TRA. */
    val canhBao: List<String> = emptyList(),
    val doTinCay: Int = 100,
    /** Môn/Chương gợi ý (mặc định lấy từ nhánh cô chọn trước khi cắt). */
    val mon: String = "",
    val chuong: String = "",
    /** Bài và Chuyên đề gợi ý, cô sửa được ở màn duyệt. */
    val bai: String = "",
    val chuyenDe: String = "",
    /** Thẻ nội dung gợi ý từ classifyQuestion, cô sửa được ở màn duyệt. */
    val tags: List<String> = emptyList(),
    /** Mức độ gợi ý 1..3, null = chưa gợi ý được, cô tự gắn. */
    val doKhoGoiY: Int? = null,
)

fun nhanCanhBao(canhBao: String): String = when (canhBao) {
    "DOAN_MO_DAU" -> "Đoạn mở đầu (tiêu đề/hướng dẫn)"
    "TRAN_TRANG" -> "Nghi tràn trang, cần gộp tay"
    "OCR_THAP" -> "Nhận diện chữ chưa chắc, cần kiểm tra"
    "CAN_KIEM_TRA" -> "Không tìm thấy đầu câu, cần tách tay"
    else -> canhBao
}

fun taoIdCauNhap(): String = "NHAP-" + UUID.randomUUID().toString().take(8).uppercase()

// ============================================================================
// TÁCH TEXT THEO ĐẦU CÂU — dùng cho file DOCX và PDF có lớp chữ.
// ============================================================================

/** Một câu đã tách từ text, kèm số câu đoán được từ đầu câu. */
data class CauDaTach(val soCau: Int, val text: String)

/** Kết quả tách: đoạn mở đầu (tiêu đề/hướng dẫn) + danh sách câu hỏi. */
data class KetQuaTachText(val doanMoDau: String, val cau: List<CauDaTach>)

/**
 * Regex đầu câu, áp dụng ở đầu dòng (multiline):
 * "Câu 1.", "Câu 1)", "Câu 1:", "Bài 1.", "CÂU 12.", "Cau 1." (OCR mất
 * dấu) đều nhận. Lớp ký tự [âÂaA] là bắt buộc vì [Aa] KHÔNG khớp chữ
 * "â" trong "Câu" — lỗi này đã được script kiểm tra bắt được, không dùng
 * (?i) đơn thuần vì Java/Kotlin không gấp chữ â/Â khi thiếu UNICODE_CASE.
 * Dấu ":" được nhận từ bản này vì nhiều đề Toán viết "Câu 1:"; chỉ nhận
 * ở đầu dòng nên vẫn tránh nhầm với câu văn thường có chữ "Câu" ở giữa.
 */
private val regexDauCau = Regex(
    """(?m)^\s*(?:[Cc][âÂaA][uU]|[Bb][àÀaA][iI])\s*(\d+)\s*[.\)\:]\s*""",
)

/**
 * Regex dự phòng cho đề chỉ đánh số trần: "1.", "1)", "1:" ở đầu dòng
 * mà không có chữ Câu/Bài. Chỉ dùng khi regex chính không tìm được đầu
 * câu nào, và chỉ tin khi có từ 2 đầu số trở lên, để tránh nhầm với
 * danh sách con (đáp án, ý nhỏ) bên trong 1 câu hỏi.
 */
private val regexSoTran = Regex(
    """(?m)^\s*(\d{1,2})\s*[.\)\:]\s+""",
)

/**
 * Tách text thành từng câu hỏi theo đầu câu. Chỉ trả về các câu hỏi,
 * đoạn mở đầu trước câu đầu tiên không nằm trong danh sách này.
 * Không tìm thấy đầu câu nào thì trả về danh sách rỗng để phía gọi xử
 * lý fallback (cả trang thành 1 ứng viên, cô tách tay ở màn duyệt).
 */
fun splitTextQuestions(text: String): List<String> {
    return tachTextCoMoDau(text).cau.map { it.text }
}

/**
 * Tách text kèm đoạn mở đầu: đoạn trước "Câu 1" (thường là tiêu đề đề,
 * hướng dẫn chung) được trả riêng để màn duyệt hiện cho cô xóa, KHÔNG
 * tự ý bỏ, vì có đề viết hướng dẫn quan trọng ở phần này.
 */
fun tachTextCoMoDau(text: String): KetQuaTachText {
    var matches = regexDauCau.findAll(text).toList()
    if (matches.isEmpty()) {
        // Đề chỉ đánh số trần: chỉ tin khi có từ 2 đầu số trở lên.
        val soTran = regexSoTran.findAll(text).toList()
        if (soTran.size >= 2) matches = soTran
    }
    if (matches.isEmpty()) return KetQuaTachText(doanMoDau = text.trim(), cau = emptyList())
    val moDau = text.substring(0, matches.first().range.first).trim()
    val cau = matches.mapIndexed { index, match ->
        val batDau = match.range.first
        val ketThuc = if (index + 1 < matches.size) matches[index + 1].range.first else text.length
        val so = match.groupValues.getOrNull(1)?.toIntOrNull() ?: (index + 1)
        CauDaTach(soCau = so, text = text.substring(batDau, ketThuc).trim())
    }
    return KetQuaTachText(doanMoDau = moDau, cau = cau)
}

// ============================================================================
// RENDER TEXT THÀNH ẢNH — để câu tách từ file có chữ hiển thị thống nhất
// với câu cắt từ ảnh scan, học sinh chỉ nhìn 1 dạng ảnh câu hỏi.
// ============================================================================

/**
 * Vẽ text tiếng Việt lên Bitmap nền trắng chữ đen, tự ngắt dòng theo
 * chiều rộng. Cỡ chữ 46px ở chiều rộng 1080px đủ đọc trên điện thoại
 * tiểu học, không cần quá nét ở bản này vì ảnh sẽ được nén lại về
 * tối đa 1024px khi lưu Base64.
 */
fun renderTextQuestionToBitmap(text: String, widthPx: Int = 1080): Bitmap {
    val rong = if (widthPx > 0) widthPx else 1080
    val le = 48
    val paint = Paint().apply {
        isAntiAlias = true
        color = Color.BLACK
        textSize = 46f
        typeface = Typeface.DEFAULT
    }
    val chieuRongChu = (rong - le * 2).toFloat()
    val dong = mutableListOf<String>()
    for (dongTho in text.split("\n")) {
        var conLai = dongTho
        if (conLai.isBlank()) {
            dong.add("")
            continue
        }
        while (conLai.isNotEmpty()) {
            val soKyTu = paint.breakText(conLai, true, chieuRongChu, null)
            if (soKyTu <= 0) {
                dong.add(conLai)
                break
            }
            var cat = soKyTu
            // Ngắt ở khoảng trắng gần nhất để không cắt đôi từ, nếu có.
            if (cat < conLai.length) {
                val khoangTrang = conLai.substring(0, cat).lastIndexOf(' ')
                if (khoangTrang > 0) cat = khoangTrang + 1
            }
            dong.add(conLai.substring(0, cat).trimEnd())
            conLai = conLai.substring(cat).trimStart()
        }
    }
    val caoDong = (paint.fontMetrics.bottom - paint.fontMetrics.top).toInt() + 10
    val cao = le * 2 + dong.size.coerceAtLeast(1) * caoDong
    val bitmap = Bitmap.createBitmap(rong, cao, Bitmap.Config.ARGB_8888)
    val canvas = Canvas(bitmap)
    canvas.drawColor(Color.WHITE)
    var y = le - paint.fontMetrics.top
    for (dongText in dong) {
        canvas.drawText(dongText, le.toFloat(), y, paint)
        y += caoDong
    }
    return bitmap
}

/**
 * Gộp 2 ảnh câu hỏi theo chiều dọc (ảnh trên + ảnh dưới), dùng cho nút
 * "Gộp với câu sau" ở màn duyệt khi máy cắt nhầm 1 câu thành 2. Ảnh kết
 * quả có chiều rộng bằng ảnh rộng hơn, phần hẹp hơn căn trái.
 */
fun gopBitmapDoc(tren: Bitmap, duoi: Bitmap): Bitmap {
    val rong = maxOf(tren.width, duoi.width)
    val cao = tren.height + duoi.height
    val ketQua = Bitmap.createBitmap(rong, cao, Bitmap.Config.ARGB_8888)
    val canvas = Canvas(ketQua)
    canvas.drawColor(Color.WHITE)
    canvas.drawBitmap(tren, 0f, 0f, null)
    canvas.drawBitmap(duoi, 0f, tren.height.toFloat(), null)
    return ketQua
}

/**
 * Tách 1 ảnh câu hỏi thành 2 ảnh theo tỉ lệ chiều cao (0.0..1.0), dùng
 * cho nút "Tách" ở màn duyệt kèm thanh trượt vị trí cắt. Đây là bản tách
 * theo tỉ lệ, chưa phải kéo pixel chính xác, đã ghi rõ trong README.
 */
fun tachBitmapDoc(bitmap: Bitmap, tiLe: Float): Pair<Bitmap, Bitmap> {
    val tyLe = tiLe.coerceIn(0.1f, 0.9f)
    val yCat = (bitmap.height * tyLe).toInt().coerceIn(1, bitmap.height - 1)
    val tren = Bitmap.createBitmap(bitmap, 0, 0, bitmap.width, yCat)
    val duoi = Bitmap.createBitmap(bitmap, 0, yCat, bitmap.width, bitmap.height - yCat)
    return tren to duoi
}

/**
 * Tách tay 1 ảnh thành N mảnh đều nhau theo chiều cao, dùng cho nút
 * "Tách tay thành N câu" ở màn duyệt khi máy không nhận được đầu câu
 * nào (ảnh chụp nghiêng, đề chỉ đánh số, công thức toán OCR kém).
 * Cô tự đếm số câu trong ảnh rồi nhập N, không cần kéo pixel chính xác.
 */
fun tachBitmapThanhNhieu(bitmap: Bitmap, soManh: Int): List<Bitmap> {
    val n = soManh.coerceIn(1, 20)
    if (n == 1) return listOf(bitmap)
    val ketQua = mutableListOf<Bitmap>()
    for (i in 0 until n) {
        val y0 = (bitmap.height * i / n)
        val y1 = if (i == n - 1) bitmap.height else (bitmap.height * (i + 1) / n)
        if (y1 - y0 >= 10) {
            ketQua.add(Bitmap.createBitmap(bitmap, 0, y0, bitmap.width, y1 - y0))
        }
    }
    return ketQua
}
