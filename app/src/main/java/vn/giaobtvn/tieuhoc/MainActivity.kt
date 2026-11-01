package vn.giaobtvn.tieuhoc

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.BackHandler
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import vn.giaobtvn.tieuhoc.data.BaiGiao
import vn.giaobtvn.tieuhoc.data.DangNhapGoogle
import vn.giaobtvn.tieuhoc.data.FirebaseRepository
import vn.giaobtvn.tieuhoc.data.LocalPrefs
import vn.giaobtvn.tieuhoc.data.QuestionBank
import vn.giaobtvn.tieuhoc.data.VaiTro
import vn.giaobtvn.tieuhoc.ui.ChamVaThongKeScreen
import vn.giaobtvn.tieuhoc.ui.DanhSachBaiGiaoScreen
import vn.giaobtvn.tieuhoc.ui.GiaoBtvnTheme
import vn.giaobtvn.tieuhoc.ui.LamTracNghiemScreen
import vn.giaobtvn.tieuhoc.ui.LopDetailScreen
import vn.giaobtvn.tieuhoc.ui.ManDangTai
import vn.giaobtvn.tieuhoc.ui.NganHangChungScreen
import vn.giaobtvn.tieuhoc.ui.NhapCauHoiScreen
import vn.giaobtvn.tieuhoc.ui.NopBaiGiayScreen
import vn.giaobtvn.tieuhoc.ui.OnTuDoScreen
import vn.giaobtvn.tieuhoc.ui.RoleScreen
import vn.giaobtvn.tieuhoc.ui.StudentHomeScreen
import vn.giaobtvn.tieuhoc.ui.TaoBaiGiayScreen
import vn.giaobtvn.tieuhoc.ui.TaoLopScreen
import vn.giaobtvn.tieuhoc.ui.TaoTracNghiemScreen
import vn.giaobtvn.tieuhoc.ui.TeacherHomeScreen

/**
 * Điều hướng bằng state đơn giản, KHÔNG dùng Navigation library để tránh
 * thêm dependency cho V1. Mỗi vai có một route riêng, nút Back của hệ
 * thống luôn quay về màn trước đó trong cùng vai.
 */
private sealed class GiaoVienRoute {
    data object Home : GiaoVienRoute()
    data object TaoLop : GiaoVienRoute()
    data object NganHangChung : GiaoVienRoute()
    // Luồng nhập chung: mọi câu chốt đều vào ngân hàng chung.
    data class NhapCauHoi(val dongGop: Boolean = false) : GiaoVienRoute()
    data class LopDetail(val maLop: String) : GiaoVienRoute()
    data class TaoBaiGiay(val maLop: String) : GiaoVienRoute()
    data class TaoTracNghiem(val maLop: String) : GiaoVienRoute()
    data class Cham(val maLop: String, val baiGiao: BaiGiao) : GiaoVienRoute()
}

private sealed class HocSinhRoute {
    data object Home : HocSinhRoute()
    data object DanhSachBai : HocSinhRoute()
    data class LamBai(val baiGiao: BaiGiao) : HocSinhRoute()
    data object OnTuDo : HocSinhRoute()
}

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge()
        super.onCreate(savedInstanceState)
        val prefs = LocalPrefs(this)
        val repo = FirebaseRepository()

        setContent {
            GiaoBtvnTheme {
                var vaiTro by remember {
                    mutableStateOf(
                        when (prefs.vaiTro) {
                            "GIAO_VIEN" -> VaiTro.GIAO_VIEN
                            "HOC_SINH" -> VaiTro.HOC_SINH
                            else -> null
                        }
                    )
                }
                var giaoVienRoute by remember { mutableStateOf<GiaoVienRoute>(GiaoVienRoute.Home) }
                var hocSinhRoute by remember { mutableStateOf<HocSinhRoute>(HocSinhRoute.Home) }
                var bank by remember { mutableStateOf<QuestionBank?>(null) }
                var loiBank by remember { mutableStateOf("") }

                LaunchedEffect(Unit) {
                    try {
                        val bankV1 = QuestionBank.load(this@MainActivity)
                        // Pilot Toán 10 Chương VII: tải riêng từ file pilot
                        // rồi gộp vào ngân hàng dùng chung trong app, để
                        // màn hình cô/học sinh hiện có (lọc theo chủ đề/bài)
                        // thấy được bài "Đường tròn trong mặt phẳng tọa độ"
                        // mà không cần sửa màn hình. File pilot lỗi/thiếu
                        // thì vẫn giữ ngân hàng V1, app không crash.
                        val bankPilot = try {
                            QuestionBank.loadPilotToan10(this@MainActivity)
                        } catch (e: Exception) {
                            QuestionBank(emptyList())
                        }
                        bank = QuestionBank(bankV1.cauHoi + bankPilot.cauHoi)
                    } catch (e: Exception) {
                        loiBank = "Không tải được ngân hàng câu hỏi trong app"
                    }
                }

                fun chonVai(vai: VaiTro) {
                    prefs.vaiTro = vai.name
                    vaiTro = vai
                    giaoVienRoute = GiaoVienRoute.Home
                    hocSinhRoute = HocSinhRoute.Home
                }

                fun doiVai() {
                    prefs.vaiTro = ""
                    vaiTro = null
                }

                val bankHienTai = bank
                when (val vai = vaiTro) {
                    null -> RoleScreen(onChon = { chonVai(it) })
                    VaiTro.GIAO_VIEN -> {
                        // Ngân hàng lỗi thì vẫn cho giáo viên dùng app với
                        // ngân hàng rỗng, vì tạo lớp và chấm bài giấy
                        // không cần ngân hàng câu hỏi.
                        if (bankHienTai == null && loiBank.isBlank()) {
                            ManDangTai()
                        } else {
                            val bankDung = bankHienTai ?: QuestionBank(emptyList())
                            when (val route = giaoVienRoute) {
                                GiaoVienRoute.Home -> {
                                    TeacherHomeScreen(
                                        activity = this@MainActivity,
                                        repo = repo,
                                        onTaoLop = { giaoVienRoute = GiaoVienRoute.TaoLop },
                                        onMoLop = { giaoVienRoute = GiaoVienRoute.LopDetail(it) },
                                        onDoiVai = { doiVai() },
                                        onNhapCauHoi = { giaoVienRoute = GiaoVienRoute.NhapCauHoi(dongGop = false) },
                                        onTaoTracNghiemChoLop = { giaoVienRoute = GiaoVienRoute.TaoTracNghiem(it) },
                                        onNganHangChung = { giaoVienRoute = GiaoVienRoute.NganHangChung },
                                    )
                                }
                                is GiaoVienRoute.NhapCauHoi -> {
                                    val gv = DangNhapGoogle.giaoVienHienTai()
                                    if (gv == null) {
                                        TeacherHomeScreen(
                                            activity = this@MainActivity,
                                            repo = repo,
                                            onTaoLop = { giaoVienRoute = GiaoVienRoute.TaoLop },
                                            onMoLop = { giaoVienRoute = GiaoVienRoute.LopDetail(it) },
                                            onDoiVai = { doiVai() },
                                            onNhapCauHoi = { giaoVienRoute = GiaoVienRoute.NhapCauHoi(dongGop = false) },
                                            onTaoTracNghiemChoLop = { giaoVienRoute = GiaoVienRoute.TaoTracNghiem(it) },
                                            onNganHangChung = { giaoVienRoute = GiaoVienRoute.NganHangChung },
                                        )
                                    } else {
                                        BackHandler { giaoVienRoute = GiaoVienRoute.Home }
                                        NhapCauHoiScreen(
                                            repo = repo,
                                            giaoVien = gv,
                                            onXong = { giaoVienRoute = GiaoVienRoute.Home },
                                            onBack = { giaoVienRoute = GiaoVienRoute.Home },
                                            dongGop = route.dongGop,
                                        )
                                    }
                                }
                                GiaoVienRoute.NganHangChung -> {
                                    val gv = DangNhapGoogle.giaoVienHienTai()
                                    if (gv == null) {
                                        TeacherHomeScreen(
                                            activity = this@MainActivity,
                                            repo = repo,
                                            onTaoLop = { giaoVienRoute = GiaoVienRoute.TaoLop },
                                            onMoLop = { giaoVienRoute = GiaoVienRoute.LopDetail(it) },
                                            onDoiVai = { doiVai() },
                                            onNhapCauHoi = { giaoVienRoute = GiaoVienRoute.NhapCauHoi(dongGop = false) },
                                            onTaoTracNghiemChoLop = { giaoVienRoute = GiaoVienRoute.TaoTracNghiem(it) },
                                            onNganHangChung = { giaoVienRoute = GiaoVienRoute.NganHangChung },
                                        )
                                    } else {
                                        BackHandler { giaoVienRoute = GiaoVienRoute.Home }
                                        NganHangChungScreen(
                                            repo = repo,
                                            giaoVien = gv,
                                            onBack = { giaoVienRoute = GiaoVienRoute.Home },
                                        )
                                    }
                                }
                                GiaoVienRoute.TaoLop -> {
                                    val gv = DangNhapGoogle.giaoVienHienTai()
                                    if (gv == null) {
                                        // Chưa đăng nhập thì quay về trang
                                        // chính để đăng nhập, không đổi
                                        // state trong lúc đang vẽ màn hình.
                                        TeacherHomeScreen(
                                            activity = this@MainActivity,
                                            repo = repo,
                                            onTaoLop = { giaoVienRoute = GiaoVienRoute.TaoLop },
                                            onMoLop = { giaoVienRoute = GiaoVienRoute.LopDetail(it) },
                                            onDoiVai = { doiVai() },
                                            onNhapCauHoi = { giaoVienRoute = GiaoVienRoute.NhapCauHoi(dongGop = false) },
                                            onTaoTracNghiemChoLop = { giaoVienRoute = GiaoVienRoute.TaoTracNghiem(it) },
                                            onNganHangChung = { giaoVienRoute = GiaoVienRoute.NganHangChung },
                                        )
                                    } else {
                                        BackHandler { giaoVienRoute = GiaoVienRoute.Home }
                                        TaoLopScreen(
                                            repo = repo,
                                            giaoVien = gv,
                                            onVaoLop = { giaoVienRoute = GiaoVienRoute.LopDetail(it) },
                                            onBack = { giaoVienRoute = GiaoVienRoute.Home },
                                        )
                                    }
                                }
                                is GiaoVienRoute.LopDetail -> {
                                    BackHandler { giaoVienRoute = GiaoVienRoute.Home }
                                    LopDetailScreen(
                                        repo = repo,
                                        maLop = route.maLop,
                                        onTaoBaiGiay = { giaoVienRoute = GiaoVienRoute.TaoBaiGiay(route.maLop) },
                                        onTaoTracNghiem = { giaoVienRoute = GiaoVienRoute.TaoTracNghiem(route.maLop) },
                                        onMoCham = { giaoVienRoute = GiaoVienRoute.Cham(route.maLop, it) },
                                        onBack = { giaoVienRoute = GiaoVienRoute.Home },
                                    )
                                }
                                is GiaoVienRoute.TaoBaiGiay -> {
                                    BackHandler { giaoVienRoute = GiaoVienRoute.LopDetail(route.maLop) }
                                    TaoBaiGiayScreen(
                                        repo = repo,
                                        maLop = route.maLop,
                                        onXong = { giaoVienRoute = GiaoVienRoute.LopDetail(route.maLop) },
                                        onBack = { giaoVienRoute = GiaoVienRoute.LopDetail(route.maLop) },
                                    )
                                }
                                is GiaoVienRoute.TaoTracNghiem -> {
                                    BackHandler { giaoVienRoute = GiaoVienRoute.LopDetail(route.maLop) }
                                    TaoTracNghiemScreen(
                                        repo = repo,
                                        bank = bankDung,
                                        maLop = route.maLop,
                                        onXong = { giaoVienRoute = GiaoVienRoute.LopDetail(route.maLop) },
                                        onBack = { giaoVienRoute = GiaoVienRoute.LopDetail(route.maLop) },
                                        giaoVienId = DangNhapGoogle.giaoVienHienTai()?.uid ?: "",
                                    )
                                }
                                is GiaoVienRoute.Cham -> {
                                    BackHandler { giaoVienRoute = GiaoVienRoute.LopDetail(route.maLop) }
                                    ChamVaThongKeScreen(
                                        repo = repo,
                                        bank = bankDung,
                                        maLop = route.maLop,
                                        baiGiao = route.baiGiao,
                                        onBack = { giaoVienRoute = GiaoVienRoute.LopDetail(route.maLop) },
                                    )
                                }
                            }
                        }
                    }
                    VaiTro.HOC_SINH -> {
                        if (bankHienTai == null && loiBank.isBlank()) {
                            ManDangTai()
                        } else {
                            val bankDung = bankHienTai ?: QuestionBank(emptyList())
                            when (val route = hocSinhRoute) {
                                HocSinhRoute.Home -> {
                                    StudentHomeScreen(
                                        activity = this@MainActivity,
                                        prefs = prefs,
                                        repo = repo,
                                        onXemBai = { hocSinhRoute = HocSinhRoute.DanhSachBai },
                                        onOnTuDo = { hocSinhRoute = HocSinhRoute.OnTuDo },
                                        onDoiVai = { doiVai() },
                                    )
                                }
                                HocSinhRoute.DanhSachBai -> {
                                    BackHandler { hocSinhRoute = HocSinhRoute.Home }
                                    DanhSachBaiGiaoScreen(
                                        repo = repo,
                                        prefs = prefs,
                                        onMoBai = { hocSinhRoute = HocSinhRoute.LamBai(it) },
                                        onBack = { hocSinhRoute = HocSinhRoute.Home },
                                    )
                                }
                                is HocSinhRoute.LamBai -> {
                                    BackHandler { hocSinhRoute = HocSinhRoute.DanhSachBai }
                                    if (route.baiGiao.loaiEnum == vn.giaobtvn.tieuhoc.data.LoaiBaiGiao.GIAY) {
                                        NopBaiGiayScreen(
                                            repo = repo,
                                            baiGiao = route.baiGiao,
                                            prefs = prefs,
                                            onXong = { hocSinhRoute = HocSinhRoute.DanhSachBai },
                                            onBack = { hocSinhRoute = HocSinhRoute.DanhSachBai },
                                        )
                                    } else {
                                        LamTracNghiemScreen(
                                            repo = repo,
                                            bank = bankDung,
                                            baiGiao = route.baiGiao,
                                            prefs = prefs,
                                            onXong = { hocSinhRoute = HocSinhRoute.DanhSachBai },
                                            onBack = { hocSinhRoute = HocSinhRoute.DanhSachBai },
                                        )
                                    }
                                }
                                HocSinhRoute.OnTuDo -> {
                                    BackHandler { hocSinhRoute = HocSinhRoute.Home }
                                    OnTuDoScreen(
                                        bank = bankDung,
                                        repo = repo,
                                        prefs = prefs,
                                        onBack = { hocSinhRoute = HocSinhRoute.Home },
                                    )
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
