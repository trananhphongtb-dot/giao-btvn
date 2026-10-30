package vn.giaobtvn.tieuhoc.data

import android.graphics.Bitmap
import android.util.Base64
import java.io.ByteArrayOutputStream
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale
import kotlin.math.roundToInt
import kotlin.random.Random

// ============================================================================
// VAI TRÒ VÀ LOẠI BÀI GIAO — V1 chỉ có 2 vai, KHÔNG có vai phụ huynh.
// ============================================================================

enum class VaiTro { GIAO_VIEN, HOC_SINH }

/** GIAY = bài giấy chụp ảnh nộp, TRAC_NGHIEM = trắc nghiệm giới hạn thời gian. */
enum class LoaiBaiGiao { GIAY, TRAC_NGHIEM }

/**
 * Trạng thái bài nộp, dùng để hiển thị trong thống kê của cô:
 * - DA_NOP: đã nộp (bài giấy đã nộp và không bị gắn cờ, hoặc trắc nghiệm đã nộp).
 * - CHUA_NOP: chưa nộp và vẫn còn hạn.
 * - QUA_HAN: chưa nộp và đã quá hạn nộp.
 * - CHO_DUYET_TRUNG: bài giấy bị gắn cờ nghi trùng, chưa được tính điểm.
 * - CAN_NOP_LAI: cô đã yêu cầu nộp lại, học sinh cần nộp bài mới.
 * CHUA_NOP và QUA_HAN không lưu trong Database mà được tính từ hạn nộp và
 * thời điểm hiện tại, xem hàm trangThaiCuaHocSinh.
 */
enum class TrangThaiNop { DA_NOP, CHUA_NOP, QUA_HAN, CHO_DUYET_TRUNG, CAN_NOP_LAI }

// ============================================================================
// CÂU HỎI — nằm trong assets/cau_hoi.json, KHÔNG nằm trong Realtime Database
// ở V1, để app ôn tự do và cô tạo bài trắc nghiệm không cần tải từ mạng.
// ============================================================================

data class CauHoi(
    val id: String = "",
    val chuDe: String = "",
    val bai: String = "",
    val noiDung: String = "",
    val cacDapAn: List<String> = emptyList(),
    /** Chỉ số đáp án đúng trong cacDapAn, từ 0 đến 3. */
    val dapAnDung: Int = 0,
    /** 1 = dễ, 2 = vừa, 3 = khó (theo kiểu tư duy, không chia theo lớp). */
    val doKho: Int = 1,
    /**
     * True = câu hỏi ảnh do cô nhập từ file (đáp án hiển thị là A/B/C/D).
     * Hàm trộn sẽ KHÔNG xáo thứ tự đáp án của câu này, vì xáo chữ cái
     * sẽ làm học sinh không biết chọn theo ảnh nữa.
     */
    val laCauAnh: Boolean = false,
    /** Chương của câu hỏi (câu nhập mới); câu assets cũ để rỗng. */
    val chuong: String = "",
    /** Môn và lớp của câu hỏi, dùng cho nhánh pilot (ví dụ Toán, lớp 10).
     *  Câu assets V1 cũ không có 2 trường này nên mặc định rỗng / 0. */
    val mon: String = "",
    val lop: Int = 0,
    /** Thẻ nội dung của câu hỏi, ví dụ OXY, DUONG_TRON, BAC_2.
     *  Câu assets V1 cũ để rỗng; cô vẫn duyệt/sửa thẻ ở màn duyệt. */
    val the: List<String> = emptyList(),
)

/**
 * Câu hỏi sau khi đã trộn thứ tự đáp án để hiển thị cho học sinh làm bài.
 * dapAnDung ở đây là chỉ số đúng TRONG DANH SÁCH ĐÃ TRỘN, không phải chỉ
 * số gốc, nên chấm điểm phải dùng danh sách này, không dùng CauHoi gốc.
 */
data class CauHoiTron(
    val id: String,
    val noiDung: String,
    val cacDapAn: List<String>,
    val dapAnDung: Int,
    /**
     * Ánh xạ ngược từ vị trí đã trộn về vị trí gốc: vị trí đã trộn i
     * tương ứng với đáp án gốc thuTuGoc[i]. Nhờ đó bài nộp lưu đáp án
     * theo chỉ số GỐC, để thống kê sai của cô so sánh đúng với đáp án gốc.
     */
    val thuTuGoc: List<Int> = emptyList(),
)

// ============================================================================
// LỚP, BÀI GIAO, BÀI NỘP — lưu trong Firebase Realtime Database.
// ============================================================================

/**
 * Cấu trúc cây Realtime Database ở V1:
 * classes/{maLop}
 *   tenLop, giaoVienId, giaoVienTen,
 *   hocSinh: { hocSinhId: tenHocSinh }
 * assignments/{maLop}/{baiGiaoId}
 *   loai, tieuDe, noiDung, anhDeBase64, chuDe, bai, hanNop (millis),
 *   thoiGianPhut (chỉ trắc nghiệm, 0 = bài giấy),
 *   cauHoiIds: [id, ...],
 *   soCauTheoDoKho: { "1": n, "2": n, "3": n } (chỉ khi chọn tự động)
 * submissions/{baiGiaoId}/{hocSinhId}
 *   dapAn: { cauHoiId: chiSoDaChon } (chỉ trắc nghiệm),
 *   anhBase64: [chuỗi Base64, tối đa 3 ảnh] (chỉ bài giấy),
 *   aHash: [hash 16 ký tự hex, song song với anhBase64] (chỉ bài giấy),
 *   diem (thang 10, null = chưa chấm), trangThai, canhBaoTrung,
 *   thoiGianNop (millis), ghiChuGiaoVien
 *
 * Lưu ý: lopId trong assignments chính là maLop, không có id lớp riêng.
 */
data class LopHoc(
    val maLop: String = "",
    val tenLop: String = "",
    val giaoVienId: String = "",
    val giaoVienTen: String = "",
    val hocSinh: Map<String, String> = emptyMap(),
) {
    constructor() : this("", "", "", "", emptyMap())
    fun toMap(): Map<String, Any?> = mapOf(
        "maLop" to maLop,
        "tenLop" to tenLop,
        "giaoVienId" to giaoVienId,
        "giaoVienTen" to giaoVienTen,
        "hocSinh" to hocSinh,
    )
}

data class BaiGiao(
    val id: String = "",
    val loai: String = "GIAY",
    val tieuDe: String = "",
    val noiDung: String = "",
    /** Ảnh đề của cô, dạng Base64, chuỗi rỗng = không có ảnh đề. */
    val anhDeBase64: String = "",
    val chuDe: String = "",
    val bai: String = "",
    /** Hạn nộp, tính bằng millis từ epoch. */
    val hanNop: Long = 0L,
    /** Thời gian làm bài tính bằng phút, chỉ có ý nghĩa với trắc nghiệm. */
    val thoiGianPhut: Int = 0,
    val cauHoiIds: List<String> = emptyList(),
    /** Khóa là "1", "2", "3" vì Firebase không cho khóa số nguyên trong Map. */
    val soCauTheoDoKho: Map<String, Int> = emptyMap(),
    /**
     * Câu hỏi ảnh do cô nhập, gắn kèm vào bài giao để học sinh làm được
     * mà không cần truy cập ngân hàng riêng của cô: cauHoiId -> ảnh Base64.
     * Chỉ có ý nghĩa với trắc nghiệm có câu đã nhập, bài khác để rỗng.
     */
    val cauHoiAnh: Map<String, String> = emptyMap(),
    /** Đáp án đúng của câu hỏi ảnh: cauHoiId -> chỉ số đúng 0..3. */
    val dapAnCauAnh: Map<String, Int> = emptyMap(),
) {
    constructor() : this("", "GIAY", "", "", "", "", "", 0L, 0, emptyList(), emptyMap())
    val loaiEnum: LoaiBaiGiao
        get() = if (loai == "TRAC_NGHIEM") LoaiBaiGiao.TRAC_NGHIEM else LoaiBaiGiao.GIAY
    fun toMap(): Map<String, Any?> = mapOf(
        "id" to id,
        "loai" to loai,
        "tieuDe" to tieuDe,
        "noiDung" to noiDung,
        "anhDeBase64" to anhDeBase64,
        "chuDe" to chuDe,
        "bai" to bai,
        "hanNop" to hanNop,
        "thoiGianPhut" to thoiGianPhut,
        "cauHoiIds" to cauHoiIds,
        "soCauTheoDoKho" to soCauTheoDoKho,
        "cauHoiAnh" to cauHoiAnh,
        "dapAnCauAnh" to dapAnCauAnh,
    )
}

data class BaiNop(
    val hocSinhId: String = "",
    val dapAn: Map<String, Int> = emptyMap(),
    val anhBase64: List<String> = emptyList(),
    val aHash: List<String> = emptyList(),
    /** Thang điểm 10, null = chưa chấm (bài giấy mới nộp hoặc đang chờ duyệt). */
    val diem: Double? = null,
    val trangThai: String = "DA_NOP",
    val canhBaoTrung: Boolean = false,
    val thoiGianNop: Long = 0L,
    val ghiChuGiaoVien: String = "",
) {
    constructor() : this("", emptyMap(), emptyList(), emptyList(), null, "DA_NOP", false, 0L, "")
    val trangThaiEnum: TrangThaiNop
        get() = when (trangThai) {
            "CHO_DUYET_TRUNG" -> TrangThaiNop.CHO_DUYET_TRUNG
            "YEU_CAU_NOP_LAI" -> TrangThaiNop.CAN_NOP_LAI
            else -> TrangThaiNop.DA_NOP
        }
    fun toMap(): Map<String, Any?> = mapOf(
        "hocSinhId" to hocSinhId,
        "dapAn" to dapAn,
        "anhBase64" to anhBase64,
        "aHash" to aHash,
        "diem" to diem,
        "trangThai" to trangThai,
        "canhBaoTrung" to canhBaoTrung,
        "thoiGianNop" to thoiGianNop,
        "ghiChuGiaoVien" to ghiChuGiaoVien,
    )
}

// ============================================================================
// THỐNG KÊ — chỉ tính toán lúc hiển thị, không lưu trong Database.
// ============================================================================

data class ThongKeBai(
    val tongHocSinh: Int = 0,
    val daNop: Int = 0,
    val chuaNop: Int = 0,
    val quaHan: Int = 0,
    val choDuyetTrung: Int = 0,
    val canNopLai: Int = 0,
    /** Tỉ lệ đã nộp trên tổng số học sinh, từ 0.0 đến 1.0. */
    val tiLeDaNop: Double = 0.0,
    /** Điểm trung bình của những bài đã có điểm, null = chưa có bài nào có điểm. */
    val diemTrungBinh: Double? = null,
    /** Điểm từng học sinh, chỉ những em đã có điểm. */
    val diemTheoHocSinh: Map<String, Double> = emptyMap(),
    /** Trắc nghiệm: mỗi câu hỏi đã bị chọn sai bao nhiêu lần, để cô thấy
     *  câu nào học sinh sai nhiều nhất. */
    val soLanSaiTheoCau: Map<String, Int> = emptyMap(),
)

// ============================================================================
// MÃ LỚP, TRẠNG THÁI, THỐNG KÊ
// ============================================================================

/** Mã lớp 6 ký tự chữ và số, bỏ các ký tự dễ nhầm là I, O, 0, 1. */
fun taoMaLop(random: Random = Random.Default): String {
    val bangChu = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    return (1..6).map { bangChu[random.nextInt(bangChu.length)] }.joinToString("")
}

fun chuanHoaMaLop(maTho: String): String = maTho.trim().uppercase()

/**
 * Trạng thái hiển thị của một học sinh trong một bài giao.
 * Học sinh chưa nộp: quá hạn hay chưa nộp tùy thời điểm hiện tại so với hạn.
 * Học sinh đã nộp: giữ nguyên trạng thái lưu trong bài nộp.
 */
fun trangThaiCuaHocSinh(baiNop: BaiNop?, hanNop: Long, bayGio: Long): TrangThaiNop {
    if (baiNop == null) return if (bayGio > hanNop) TrangThaiNop.QUA_HAN else TrangThaiNop.CHUA_NOP
    return baiNop.trangThaiEnum
}

fun nhanTrangThai(trangThai: TrangThaiNop): String = when (trangThai) {
    TrangThaiNop.DA_NOP -> "Đã nộp"
    TrangThaiNop.CHUA_NOP -> "Chưa nộp"
    TrangThaiNop.QUA_HAN -> "Quá hạn"
    TrangThaiNop.CHO_DUYET_TRUNG -> "Chờ duyệt trùng"
    TrangThaiNop.CAN_NOP_LAI -> "Cần nộp lại"
}

/**
 * Thống kê một bài giao cho cô xem. dapAnDung là map cauHoiId -> chỉ số
 * đúng GỐC (chưa trộn), chỉ dùng để đếm số lần sai của trắc nghiệm; nếu
 * bài là bài giấy thì map này rỗng và soLanSaiTheoCau sẽ rỗng.
 */
fun tinhThongKe(
    baiGiao: BaiGiao,
    hocSinh: Map<String, String>,
    baiNopTheoHocSinh: Map<String, BaiNop>,
    dapAnDung: Map<String, Int>,
    bayGio: Long,
): ThongKeBai {
    var daNop = 0
    var chuaNop = 0
    var quaHan = 0
    var choDuyet = 0
    var canNopLai = 0
    val diemMap = mutableMapOf<String, Double>()
    val saiMap = mutableMapOf<String, Int>()
    for ((hocSinhId, _) in hocSinh) {
        val nop = baiNopTheoHocSinh[hocSinhId]
        when (trangThaiCuaHocSinh(nop, baiGiao.hanNop, bayGio)) {
            TrangThaiNop.DA_NOP -> daNop++
            TrangThaiNop.CHUA_NOP -> chuaNop++
            TrangThaiNop.QUA_HAN -> quaHan++
            TrangThaiNop.CHO_DUYET_TRUNG -> {
                choDuyet++
                daNop++
            }
            TrangThaiNop.CAN_NOP_LAI -> {
                canNopLai++
                if (bayGio > baiGiao.hanNop) quaHan++ else chuaNop++
            }
        }
        nop?.diem?.let { diemMap[hocSinhId] = it }
        if (nop != null && dapAnDung.isNotEmpty()) {
            for ((cauId, dapAnDungCuaCau) in dapAnDung) {
                val daChon = nop.dapAn[cauId]
                if (daChon != null && daChon != dapAnDungCuaCau) {
                    saiMap[cauId] = (saiMap[cauId] ?: 0) + 1
                }
            }
        }
    }
    val tong = hocSinh.size
    val diemTb = if (diemMap.isEmpty()) null
        else (diemMap.values.sum() / diemMap.size * 10.0).roundToInt() / 10.0
    return ThongKeBai(
        tongHocSinh = tong,
        daNop = daNop,
        chuaNop = chuaNop,
        quaHan = quaHan,
        choDuyetTrung = choDuyet,
        canNopLai = canNopLai,
        tiLeDaNop = if (tong == 0) 0.0 else daNop.toDouble() / tong,
        diemTrungBinh = diemTb,
        diemTheoHocSinh = diemMap,
        soLanSaiTheoCau = saiMap,
    )
}

// ============================================================================
// TRỘN CÂU HỎI / ĐÁP ÁN VÀ CHẤM ĐIỂM THANG 10
// ============================================================================

/**
 * Trộn thứ tự câu hỏi và, trong mỗi câu, trộn thứ tự đáp án, đồng thời
 * tính lại chỉ số đáp án đúng theo danh sách đã trộn. Học sinh khác nhau
 * làm cùng một bài sẽ thấy thứ tự khác nhau, hạn chế nhìn bài nhau.
 */
fun tronCauHoiVaDapAn(cauHoi: List<CauHoi>, random: Random = Random.Default): List<CauHoiTron> {
    return cauHoi.shuffled(random).map { cau ->
        // Câu hỏi ảnh: giữ nguyên thứ tự A/B/C/D, không xáo chữ cái.
        val thuTu = if (cau.laCauAnh) {
            cau.cacDapAn.indices.toList()
        } else {
            cau.cacDapAn.indices.shuffled(random)
        }
        val dapAnTron = thuTu.map { cau.cacDapAn[it] }
        val dapAnDungMoi = thuTu.indexOf(cau.dapAnDung)
        CauHoiTron(cau.id, cau.noiDung, dapAnTron, dapAnDungMoi, thuTu)
    }
}

/**
 * Chấm điểm thang 10, làm tròn 1 chữ số thập phân. Câu chưa chọn thì
 * tính là sai. Danh sách rỗng thì điểm 0, không chia cho 0.
 */
fun chamDiemThang10(dapAn: Map<String, Int>, cauHoi: List<CauHoi>): Double {
    if (cauHoi.isEmpty()) return 0.0
    val soDung = cauHoi.count { dapAn[it.id] == it.dapAnDung }
    return (soDung * 10.0 / cauHoi.size * 10.0).roundToInt() / 10.0
}

/**
 * Chấm điểm cho bài đã trộn đáp án: so sánh đáp án đã chọn với chỉ số
 * đúng trong danh sách đã trộn. Dùng hàm này khi chấm bài trắc nghiệm
 * trên máy học sinh, vì đáp án hiển thị đã bị trộn.
 */
fun chamDiemBaiTron(dapAn: Map<String, Int>, cauTron: List<CauHoiTron>): Double {
    if (cauTron.isEmpty()) return 0.0
    val soDung = cauTron.count { dapAn[it.id] == it.dapAnDung }
    return (soDung * 10.0 / cauTron.size * 10.0).roundToInt() / 10.0
}

// ============================================================================
// ẢNH: NÉN, AHASH, KHOẢNG CÁCH HAMMING — CHỐNG TRÙNG ẢNH BÀI GIẤY
// ============================================================================

/**
 * Nén ảnh về tối đa 1024px ở cạnh dài nhất, lưu JPEG chất lượng 70 rồi
 * mã hóa Base64 để lưu trong Realtime Database ở V1.
 * Về sau có thể chuyển sang Firebase Storage thì chỉ cần thay hàm này
 * bằng hàm tải ảnh lên Storage và lưu URL, phần còn lại không đổi.
 */
fun nenAnhBase64(bitmapGoc: Bitmap, canhDaiToiDa: Int = 1024, chatLuongJpeg: Int = 70): String {
    val tiLe = if (bitmapGoc.width <= canhDaiToiDa && bitmapGoc.height <= canhDaiToiDa) {
        1.0f
    } else if (bitmapGoc.width >= bitmapGoc.height) {
        canhDaiToiDa.toFloat() / bitmapGoc.width
    } else {
        canhDaiToiDa.toFloat() / bitmapGoc.height
    }
    val bitmap = if (tiLe >= 1.0f) {
        bitmapGoc
    } else {
        Bitmap.createScaledBitmap(
            bitmapGoc,
            (bitmapGoc.width * tiLe).roundToInt().coerceAtLeast(1),
            (bitmapGoc.height * tiLe).roundToInt().coerceAtLeast(1),
            true,
        )
    }
    val out = ByteArrayOutputStream()
    bitmap.compress(Bitmap.CompressFormat.JPEG, chatLuongJpeg, out)
    if (bitmap !== bitmapGoc) bitmap.recycle()
    return Base64.encodeToString(out.toByteArray(), Base64.NO_WRAP)
}

/**
 * Tính aHash của ảnh: thu nhỏ về 8x8, chuyển xám, lấy giá trị trung bình,
 * mỗi điểm ảnh cho 1 bit (sáng hơn trung bình = 1). Kết quả là chuỗi
 * 16 ký tự hex, tương đương 64 bit, đủ nhỏ để lưu kèm mỗi bài nộp.
 */
fun tinhAHash(bitmap: Bitmap): String {
    val nho = Bitmap.createScaledBitmap(bitmap, 8, 8, true)
    val pixels = IntArray(64)
    nho.getPixels(pixels, 0, 8, 0, 0, 8, 8)
    nho.recycle()
    val doXam = IntArray(64) { i ->
        val p = pixels[i]
        val r = (p shr 16) and 0xFF
        val g = (p shr 8) and 0xFF
        val b = p and 0xFF
        (r * 299 + g * 587 + b * 114) / 1000
    }
    return aHashTuDoXam(doXam)
}

/** Phần thuần logic của aHash, tách riêng để dễ kiểm tra: 64 giá trị xám. */
fun aHashTuDoXam(doXam: IntArray): String {
    require(doXam.size == 64) { "aHash cần đúng 64 giá trị xám 8x8" }
    val trungBinh = doXam.average()
    // Dùng ULong vì bit cao nhất (bit 63) làm Long bị âm và in hex bị sai.
    var giaTri = 0UL
    for (i in 0 until 64) {
        if (doXam[i] > trungBinh) giaTri = giaTri or (1UL shl (63 - i))
    }
    return giaTri.toString(16).padStart(16, '0')
}

/**
 * Khoảng cách Hamming giữa 2 aHash: số bit khác nhau. Hai ảnh giống hệt
 * nhau thì khoảng cách 0; ảnh chụp lại cùng một tờ giấy, hơi lệch sáng
 * hoặc lệch góc, thường vẫn dưới ngưỡng. Hash sai định dạng thì trả về
 * giá trị rất lớn để không bao giờ bị coi là trùng.
 */
fun khoangCachHamming(hashA: String, hashB: String): Int {
    val a = hashA.toULongOrNull(16) ?: return Int.MAX_VALUE
    val b = hashB.toULongOrNull(16) ?: return Int.MAX_VALUE
    return (a xor b).countOneBits()
}

/** Ngưỡng V1: khoảng cách Hamming <= 12 thì gắn cờ "nghi trùng". */
const val NGUONG_TRUNG_AHASH = 12

/**
 * Tìm các cặp bài nộp nghi trùng trong cùng một bài giao: với mỗi học
 * sinh, trả về danh sách học sinh khác mà có ít nhất một ảnh gần giống
 * ảnh của mình. Chỉ so sánh các bài chưa có điểm, bài đã chấm thì không
 * gắn cờ lại.
 */
fun timBaiNghiTrung(baiNopTheoHocSinh: Map<String, BaiNop>): Map<String, List<String>> {
    val ketQua = mutableMapOf<String, MutableList<String>>()
    val danhSach = baiNopTheoHocSinh.entries
        .filter { it.value.diem == null && it.value.aHash.isNotEmpty() }
    for (i in danhSach.indices) {
        for (j in i + 1 until danhSach.size) {
            val (idA, nopA) = danhSach[i]
            val (idB, nopB) = danhSach[j]
            val trung = nopA.aHash.any { ha ->
                nopB.aHash.any { hb -> khoangCachHamming(ha, hb) <= NGUONG_TRUNG_AHASH }
            }
            if (trung) {
                ketQua.getOrPut(idA) { mutableListOf() }.add(idB)
                ketQua.getOrPut(idB) { mutableListOf() }.add(idA)
            }
        }
    }
    return ketQua
}

// ============================================================================
// ĐỊNH DẠNG THỜI GIAN HIỂN THỊ
// ============================================================================

fun dinhDangNgayGio(millis: Long): String {
    if (millis <= 0L) return "Chưa đặt"
    return SimpleDateFormat("HH:mm dd/MM/yyyy", Locale("vi", "VN")).format(Date(millis))
}

fun dinhDangPhutGiay(tongGiay: Long): String {
    val phut = tongGiay / 60
    val giay = tongGiay % 60
    return "%02d:%02d".format(Locale.US, phut, giay)
}
