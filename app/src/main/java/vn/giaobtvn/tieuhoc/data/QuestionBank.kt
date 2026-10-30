package vn.giaobtvn.tieuhoc.data

import android.content.Context
import org.json.JSONArray
import org.json.JSONObject
import kotlin.random.Random

/**
 * Ngân hàng câu hỏi đọc từ assets/cau_hoi.json, dùng chung cho 2 việc:
 * - Cô tạo bài trắc nghiệm: chọn tay từng câu, hoặc chọn tự động theo mức độ.
 * - Học sinh ôn bài tự do: chọn theo chủ đề hoặc theo bài, lấy ngẫu nhiên.
 *
 * Định dạng file assets (khác với file câu hỏi tiểu học gốc dùng A/B/C/D):
 * { "cau_hoi": [ { "id", "chu_de", "bai", "noi_dung",
 *                  "cac_dap_an": [4 chuỗi], "dap_an_dung": 0..3,
 *                  "do_kho": 1..3 } ] }
 * Ôn tự do không ghi điểm vào lớp, không giới hạn thời gian.
 */
class QuestionBank(val cauHoi: List<CauHoi>) {

    companion object {
        fun load(context: Context): QuestionBank {
            val text = context.assets.open("cau_hoi.json").bufferedReader().use { it.readText() }
            return fromJson(text)
        }

        /**
         * Nhánh pilot Toán 10 Chương VII, đọc từ assets/cau_hoi_toan10.json.
         * Tách riêng khỏi cau_hoi.json (ngân hàng tiểu học V1) để 2 ngân
         * hàng không trộn vào nhau trong lúc thử nghiệm.
         */
        fun loadPilotToan10(context: Context): QuestionBank {
            val text = context.assets.open("cau_hoi_toan10.json").bufferedReader().use { it.readText() }
            return fromJson(text)
        }

        /** Đọc từ chuỗi JSON, tách riêng để logic đọc không phụ thuộc Android. */
        fun fromJson(text: String): QuestionBank {
            val root = JSONObject(text)
            val arr: JSONArray = root.optJSONArray("cau_hoi") ?: JSONArray()
            val list = mutableListOf<CauHoi>()
            for (i in 0 until arr.length()) {
                val o = arr.getJSONObject(i)
                val dapAnArr = o.optJSONArray("cac_dap_an") ?: JSONArray()
                val dapAn = (0 until dapAnArr.length()).map { dapAnArr.getString(it) }
                if (dapAn.size != 4) continue
                val dapAnDung = o.optInt("dap_an_dung", 0)
                if (dapAnDung !in 0..3) continue
                val theArr = o.optJSONArray("the") ?: JSONArray()
                val the = (0 until theArr.length()).map { theArr.getString(it) }
                list.add(
                    CauHoi(
                        id = o.optString("id"),
                        chuDe = o.optString("chu_de"),
                        bai = o.optString("bai"),
                        noiDung = o.optString("noi_dung"),
                        cacDapAn = dapAn,
                        dapAnDung = dapAnDung,
                        doKho = o.optInt("do_kho", 1).coerceIn(1, 3),
                        chuong = o.optString("chuong"),
                        mon = o.optString("mon"),
                        lop = o.optInt("lop", 0),
                        the = the,
                    )
                )
            }
            return QuestionBank(list)
        }
    }

    /** Các chủ đề có trong ngân hàng, theo thứ tự xuất hiện. */
    fun cacChuDe(): List<String> = cauHoi.map { it.chuDe }.distinct()

    /** Các bài thuộc một chủ đề, theo thứ tự xuất hiện. */
    fun cacBaiTheoChuDe(chuDe: String): List<String> =
        cauHoi.filter { it.chuDe == chuDe }.map { it.bai }.distinct()

    /** Lọc câu hỏi, bỏ qua tiêu chí nào để trống hoặc bằng "Tất cả". */
    fun loc(chuDe: String? = null, bai: String? = null, doKho: Int? = null): List<CauHoi> {
        return cauHoi.filter { cau ->
            (chuDe.isNullOrBlank() || chuDe == "Tất cả" || cau.chuDe == chuDe) &&
                (bai.isNullOrBlank() || bai == "Tất cả" || cau.bai == bai) &&
                (doKho == null || cau.doKho == doKho)
        }
    }

    /**
     * Lọc theo nhánh pilot: môn, lớp, chương, thẻ. Tiêu chí nào để trống
     * hoặc bằng "Tất cả" thì bỏ qua. Dùng cho nhánh Toán 10 Chương VII,
     * không ảnh hưởng hàm loc() cũ của ngân hàng V1.
     */
    fun locTheoNhanh(
        mon: String? = null,
        lop: Int? = null,
        chuong: String? = null,
        the: String? = null,
        bai: String? = null,
        doKho: Int? = null,
    ): List<CauHoi> {
        return cauHoi.filter { cau ->
            (mon.isNullOrBlank() || mon == "Tất cả" || cau.mon == mon) &&
                (lop == null || lop == 0 || cau.lop == lop) &&
                (chuong.isNullOrBlank() || chuong == "Tất cả" || cau.chuong == chuong) &&
                (the.isNullOrBlank() || the == "Tất cả" || the in cau.the) &&
                (bai.isNullOrBlank() || bai == "Tất cả" || cau.bai == bai) &&
                (doKho == null || cau.doKho == doKho)
        }
    }

    fun cauHoiTheoIds(ids: List<String>): List<CauHoi> {
        val theoId = cauHoi.associateBy { it.id }
        return ids.mapNotNull { theoId[it] }
    }

    /**
     * Lấy ngẫu nhiên không trùng từ một danh sách. Nếu danh sách ít hơn
     * số lượng yêu cầu thì trả về toàn bộ danh sách đã trộn, không lặp câu.
     */
    fun layNgauNhien(danhSach: List<CauHoi>, soLuong: Int, random: Random = Random.Default): List<CauHoi> {
        if (soLuong <= 0) return emptyList()
        return danhSach.shuffled(random).take(soLuong)
    }

    /**
     * Chọn tự động theo mức độ cho bài trắc nghiệm của cô.
     * soCauTheoDoKho: map mức độ (1, 2, 3) -> số câu cần lấy.
     * Mỗi mức độ lấy ngẫu nhiên không trùng, các mức độ không lấy trùng
     * nhau. Mức nào trong ngân hàng không đủ câu thì lấy hết số câu có,
     * phần thiếu không bù bằng mức khác để cô thấy rõ và tự bổ sung.
     */
    fun chonTuDongTheoDoKho(
        soCauTheoDoKho: Map<Int, Int>,
        chuDe: String? = null,
        bai: String? = null,
        random: Random = Random.Default,
    ): List<CauHoi> {
        val daChon = mutableSetOf<String>()
        val ketQua = mutableListOf<CauHoi>()
        for (doKho in 1..3) {
            val canLay = soCauTheoDoKho[doKho] ?: 0
            if (canLay <= 0) continue
            val ungVien = loc(chuDe, bai, doKho).filter { it.id !in daChon }
            val lay = layNgauNhien(ungVien, canLay, random)
            ketQua.addAll(lay)
            daChon.addAll(lay.map { it.id })
        }
        return ketQua
    }
}
