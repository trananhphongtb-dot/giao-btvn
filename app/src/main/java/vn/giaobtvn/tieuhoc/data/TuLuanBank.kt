package vn.giaobtvn.tieuhoc.data

import android.content.Context
import org.json.JSONObject
import kotlin.random.Random

/**
 * Ngân hàng câu TỰ LUẬN Toán lớp 1–5, đọc từ assets/tu_luan_toan.json.
 * Mỗi chủ đề (bài) có 10 câu, mỗi câu có đề và lời giải gợi ý. Cô chọn
 * ngẫu nhiên hoặc theo chủ đề khi giao bài giấy; lời giải gợi ý chỉ hiện
 * cho cô lúc chấm bài, KHÔNG gửi cho học sinh (bài giao chỉ lưu mã câu).
 */
data class CauTuLuan(
    val id: String,
    val lop: Int,
    val bai: String,
    val de: String,
    val goiY: String,
    val doKho: Int,
)

class TuLuanBank(val cau: List<CauTuLuan>) {

    companion object {
        fun load(context: Context): TuLuanBank = try {
            fromJson(context.assets.open("tu_luan_toan.json").bufferedReader().use { it.readText() })
        } catch (e: Exception) {
            TuLuanBank(emptyList())
        }

        fun fromJson(text: String): TuLuanBank {
            val arr = JSONObject(text).optJSONArray("tu_luan") ?: return TuLuanBank(emptyList())
            val list = (0 until arr.length()).mapNotNull { i ->
                val o = arr.getJSONObject(i)
                val de = o.optString("de")
                if (de.isBlank()) null else CauTuLuan(
                    id = o.optString("id"),
                    lop = o.optInt("lop"),
                    bai = o.optString("bai"),
                    de = de,
                    goiY = o.optString("goi_y"),
                    doKho = o.optInt("do_kho", 1).coerceIn(1, 3),
                )
            }
            return TuLuanBank(list)
        }
    }

    fun cacLop(): List<Int> = cau.map { it.lop }.distinct().sorted()

    fun cacBai(lop: Int): List<String> = cau.filter { it.lop == lop }.map { it.bai }.distinct()

    /** Lọc theo lớp và bài; bài rỗng hoặc "Tất cả" = cả lớp. */
    fun loc(lop: Int, bai: String = "Tất cả"): List<CauTuLuan> =
        cau.filter { it.lop == lop && (bai.isBlank() || bai == "Tất cả" || it.bai == bai) }

    fun layNgauNhien(ds: List<CauTuLuan>, soLuong: Int, random: Random = Random.Default): List<CauTuLuan> =
        if (soLuong <= 0) emptyList() else ds.shuffled(random).take(soLuong)

    /** Giữ đúng thứ tự mã câu cô đã chọn; mã không còn trong ngân hàng thì bỏ qua. */
    fun theoIds(ids: List<String>): List<CauTuLuan> {
        val theoId = cau.associateBy { it.id }
        return ids.mapNotNull { theoId[it] }
    }
}
