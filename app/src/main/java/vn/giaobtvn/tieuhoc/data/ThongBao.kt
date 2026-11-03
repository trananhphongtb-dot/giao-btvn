package vn.giaobtvn.tieuhoc.data

// ============================================================================
// THÔNG BÁO — hộp thư trong Realtime Database + FCM.
// Cây dữ liệu:
//   thongBao/{hocSinhId}/{thongBaoId}
//     tieuDe, noiDung, loai (BAI_MOI / NHAC_LAM_BAI), maLop, baiGiaoId,
//     baiTieuDe, thoiGian (millis), daDoc (true/false)
//   fcmTokens/{nguoiDungId} = token
// Hộp thư này là nơi học sinh xem lại thông báo trong app, kể cả khi
// thông báo đẩy FCM chưa tới hoặc máy chưa cấp quyền thông báo.
// ============================================================================

enum class LoaiThongBao { BAI_MOI, NHAC_LAM_BAI }

data class ThongBaoApp(
    val id: String = "",
    val tieuDe: String = "",
    val noiDung: String = "",
    val loai: String = "BAI_MOI",
    val maLop: String = "",
    val baiGiaoId: String = "",
    val baiTieuDe: String = "",
    val thoiGian: Long = 0L,
    val daDoc: Boolean = false,
) {
    constructor() : this("", "", "", "BAI_MOI", "", "", "", 0L, false)
    val loaiEnum: LoaiThongBao
        get() = if (loai == "NHAC_LAM_BAI") LoaiThongBao.NHAC_LAM_BAI else LoaiThongBao.BAI_MOI
    fun toMap(): Map<String, Any?> = mapOf(
        "tieuDe" to tieuDe,
        "noiDung" to noiDung,
        "loai" to loai,
        "maLop" to maLop,
        "baiGiaoId" to baiGiaoId,
        "baiTieuDe" to baiTieuDe,
        "thoiGian" to thoiGian,
        "daDoc" to daDoc,
    )
}

fun dinhDangThoiGianThongBao(millis: Long): String {
    if (millis <= 0L) return ""
    return dinhDangNgayGio(millis)
}
