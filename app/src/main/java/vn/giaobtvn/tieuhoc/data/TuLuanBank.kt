package vn.giaobtvn.tieuhoc.data

import android.content.Context
import org.json.JSONObject
import kotlin.random.Random

/**
 * Ngân hàng câu TỰ LUẬN Toán lớp 1–5, đọc từ assets/tu_luan_toan.json và tu_luan_tieng_viet.json.
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
    val mon: String = "Toán",
)

class TuLuanBank(val cau: List<CauTuLuan>) {

    companion object {
        private val FILES = listOf("tu_luan_toan.json", "tu_luan_tieng_viet.json", "tu_luan_toan_thcs_thpt.json", "tu_luan_tieng_anh.json", "tu_luan_mon_khac.json")

        /** Đọc từng file riêng; file nào thiếu hoặc lỗi thì bỏ qua, các file còn lại vẫn dùng được. */
        fun load(context: Context): TuLuanBank = TuLuanBank(FILES.flatMap { f ->
            try {
                fromJson(context.assets.open(f).bufferedReader().use { it.readText() }).cau
            } catch (e: Exception) {
                emptyList()
            }
        })

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
                    mon = o.optString("mon").ifBlank { "Toán" },
                )
            }
            return TuLuanBank(list)
        }
    }

    fun cacMon(): List<String> = cau.map { it.mon }.distinct()

    fun cacLop(mon: String): List<Int> = cau.filter { it.mon == mon }.map { it.lop }.distinct().sorted()

    fun cacBai(mon: String, lop: Int): List<String> = cau.filter { it.mon == mon && it.lop == lop }.map { it.bai }.distinct()

    /** Lọc theo môn, lớp và bài; bài rỗng hoặc "Tất cả" = cả lớp. */
    fun loc(mon: String, lop: Int, bai: String = "Tất cả"): List<CauTuLuan> =
        cau.filter { it.mon == mon && it.lop == lop && (bai.isBlank() || bai == "Tất cả" || it.bai == bai) }

    fun layNgauNhien(ds: List<CauTuLuan>, soLuong: Int, random: Random = Random.Default): List<CauTuLuan> =
        if (soLuong <= 0) emptyList() else ds.shuffled(random).take(soLuong)

    /** Giữ đúng thứ tự mã câu cô đã chọn; mã không còn trong ngân hàng thì bỏ qua. */
    fun theoIds(ids: List<String>): List<CauTuLuan> {
        val theoId = cau.associateBy { it.id }
        return ids.mapNotNull { theoId[it] }
    }
}
