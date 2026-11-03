package vn.giaobtvn.tieuhoc.ui

import android.Manifest
import android.app.Activity
import android.content.pm.PackageManager
import android.net.Uri
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.Image
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.RadioButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.core.content.ContextCompat
import androidx.core.content.FileProvider
import java.io.File
import kotlinx.coroutines.launch
import vn.giaobtvn.tieuhoc.data.BaiGiao
import vn.giaobtvn.tieuhoc.data.BaiNop
import vn.giaobtvn.tieuhoc.data.DangNhapGoogle
import vn.giaobtvn.tieuhoc.data.CauHoi
import vn.giaobtvn.tieuhoc.data.GiaoBtvnRepository
import vn.giaobtvn.tieuhoc.data.ImportedQuestion
import vn.giaobtvn.tieuhoc.data.LocalPrefs
import vn.giaobtvn.tieuhoc.data.LoaiBaiGiao
import vn.giaobtvn.tieuhoc.data.LopHoc
import vn.giaobtvn.tieuhoc.data.QuestionBank
import vn.giaobtvn.tieuhoc.data.TrangThaiNop
import vn.giaobtvn.tieuhoc.data.chamDiemThang10
import vn.giaobtvn.tieuhoc.data.chuanHoaMaLop
import vn.giaobtvn.tieuhoc.data.dinhDangNgayGio
import vn.giaobtvn.tieuhoc.data.nenAnhBase64
import vn.giaobtvn.tieuhoc.data.nhanTrangThai
import vn.giaobtvn.tieuhoc.data.tinhAHash
import vn.giaobtvn.tieuhoc.data.trangThaiCuaHocSinh
import vn.giaobtvn.tieuhoc.data.tronCauHoiVaDapAn

// ============================================================================
// TRANG CHÍNH HỌC SINH: tham gia lớp + ôn bài tự do.
// Vào vai học sinh là ôn được ngay, không bắt buộc phải vào lớp trước.
// ============================================================================

@Composable
fun StudentHomeScreen(
    prefs: LocalPrefs,
    repo: GiaoBtvnRepository,
    onXemBai: () -> Unit,
    onOnTuDo: () -> Unit,
    onDoiVai: () -> Unit,
) {
    val scope = rememberCoroutineScope()
    var maLopNhap by remember { mutableStateOf(prefs.maLop) }
    var tenNhap by remember { mutableStateOf(prefs.tenHocSinh) }
    var lop by remember { mutableStateOf<LopHoc?>(null) }
    var loi by remember { mutableStateOf("") }
    var thongBao by remember { mutableStateOf("") }
    // Học sinh KHÔNG cần đăng nhập Google nữa (bỏ từ 2026-11-04):
    // chỉ cần mã lớp + tên, bài nộp tính theo mã máy (hocSinhId).
    var thongBaoList by remember { mutableStateOf<List<vn.giaobtvn.tieuhoc.data.ThongBaoApp>>(emptyList()) }
    val contextThongBao = LocalContext.current
    val xinQuyenThongBao = rememberLauncherForActivityResult(
        ActivityResultContracts.RequestPermission(),
    ) { _ -> }
    LaunchedEffect(prefs.hocSinhId) {
        repo.layThongBao(prefs.hocSinhId).onSuccess { thongBaoList = it }
    }
    fun taiThongBao() {
        scope.launch {
            repo.layThongBao(prefs.hocSinhId).onSuccess { thongBaoList = it }
        }
    }

    LaunchedEffect(prefs.maLop) {
        if (prefs.maLop.isNotBlank()) {
            repo.layLopTheoMa(prefs.maLop).onSuccess { lop = it }
        }
    }

    CanhDoc {
        TieuDeCanh("Học sinh", "Tham gia lớp để làm bài cô giao, hoặc ôn bài tự do")
        // Hộp thông báo: bài mới + nhắc làm bài, kể cả khi app vừa mở lại.
        val chuaDoc = thongBaoList.count { !it.daDoc }
        Khung("🔔 Thông báo", if (chuaDoc > 0) "$chuaDoc thông báo chưa đọc" else "Không có thông báo mới") {
            if (thongBaoList.isEmpty()) {
                Text("Cô chưa gửi thông báo nào cho bạn.", fontSize = 15.sp)
            } else {
                thongBaoList.take(5).forEach { tb ->
                    Column(Modifier.fillMaxWidth().padding(vertical = 6.dp)) {
                        Text(tb.tieuDe, fontSize = 16.sp, fontWeight = FontWeight.Bold)
                        Text(tb.noiDung, fontSize = 14.sp, color = Color.DarkGray)
                        Text(
                            vn.giaobtvn.tieuhoc.data.dinhDangThoiGianThongBao(tb.thoiGian) +
                                if (tb.daDoc) "" else " — Chưa đọc",
                            fontSize = 13.sp, color = Color.Gray,
                        )
                        if (!tb.daDoc) {
                            NutNhoQuanLy("Đánh dấu đã đọc") {
                                scope.launch {
                                    repo.danhDauDaDocThongBao(prefs.hocSinhId, tb.id)
                                    taiThongBao()
                                }
                            }
                        }
                    }
                }
                NutNhoQuanLy("Tải lại thông báo") { taiThongBao() }
            }
            Spacer(Modifier.height(8.dp))
            NutPhu("Bật thông báo đẩy") {
                if (android.os.Build.VERSION.SDK_INT >= 33) {
                    xinQuyenThongBao.launch(android.Manifest.permission.POST_NOTIFICATIONS)
                }
            }
            Text(
                "Bật quyền này thì thông báo mới sẽ hiện cả khi app đã đóng.",
                fontSize = 13.sp, color = Color.Gray,
            )
        }
        val lopHienTai = lop
        if (prefs.maLop.isBlank()) {
            Text("Bạn chưa tham gia lớp nào. Nhập mã lớp cô cho để vào lớp:", fontSize = 16.sp)
            Spacer(Modifier.height(12.dp))
            OutlinedTextField(maLopNhap, { maLopNhap = it }, label = { Text("Mã lớp, ví dụ: K7X2Q9") }, modifier = Modifier.fillMaxWidth())
            Spacer(Modifier.height(8.dp))
            OutlinedTextField(tenNhap, { tenNhap = it }, label = { Text("Tên của bạn") }, modifier = Modifier.fillMaxWidth())
            Spacer(Modifier.height(12.dp))
            NutLon("Tham gia lớp", bat = maLopNhap.isNotBlank() && tenNhap.isNotBlank()) {
                loi = ""
                scope.launch {
                    repo.thamGiaLop(maLopNhap, prefs.hocSinhId, tenNhap)
                        .onSuccess {
                            prefs.maLop = chuanHoaMaLop(maLopNhap)
                            prefs.tenHocSinh = tenNhap.trim()
                            lop = it
                            thongBao = "Đã tham gia lớp ${it.tenLop}"
                        }
                        .onFailure { loi = "Không tìm thấy lớp với mã này, kiểm tra lại mã lớp" }
                }
            }
        } else {
            Text(
                "Lớp của bạn: ${lopHienTai?.tenLop ?: prefs.maLop} (mã ${prefs.maLop})",
                fontSize = 17.sp,
                fontWeight = FontWeight.Bold,
            )
            Text("Tên của bạn: ${prefs.tenHocSinh}", fontSize = 16.sp)
            Spacer(Modifier.height(16.dp))
            NutLon("Xem bài cô giao", onClick = onXemBai)
            Spacer(Modifier.height(8.dp))
            NutPhu("Rời lớp này") {
                prefs.roiLop()
                lop = null
                maLopNhap = ""
            }
        }
        Spacer(Modifier.height(16.dp))
        NutLon("Ôn bài tự do", onClick = onOnTuDo)
        Text(
            "Ôn bài tự do không tính vào điểm lớp, không giới hạn thời gian, " +
                "làm xong mỗi câu sẽ hiện đáp án đúng ngay.",
            fontSize = 14.sp,
            color = Color.Gray,
        )
        ThongBaoLoi(loi)
        ThongBaoTot(thongBao)
        Spacer(Modifier.height(16.dp))
        NutPhu("Đổi vai", onClick = onDoiVai)
    }
}

// ============================================================================
// DANH SÁCH BÀI CÔ GIAO CHO HỌC SINH
// ============================================================================

@Composable
fun DanhSachBaiGiaoScreen(
    repo: GiaoBtvnRepository,
    prefs: LocalPrefs,
    onMoBai: (BaiGiao) -> Unit,
    onBack: () -> Unit,
) {
    var baiList by remember { mutableStateOf<List<BaiGiao>>(emptyList()) }
    var baiNopMap by remember { mutableStateOf<Map<String, BaiNop>>(emptyMap()) }
    var loi by remember { mutableStateOf("") }

    LaunchedEffect(prefs.maLop) {
        repo.layBaiGiaoTheoLop(prefs.maLop)
            .onSuccess { list ->
                baiList = list
                list.forEach { bai ->
                    repo.layBaiNopCuaHocSinh(bai.id, prefs.hocSinhId)
                        .onSuccess { nop ->
                            if (nop != null) baiNopMap = baiNopMap + (bai.id to nop)
                        }
                }
            }
            .onFailure { loi = "Không tải được bài giao, kiểm tra mạng rồi thử lại" }
    }

    CanhDoc {
        TieuDeCanh("Bài cô giao")
        if (baiList.isEmpty()) {
            Text("Cô chưa giao bài nào cho lớp của bạn.")
        } else {
            baiList.forEach { bai ->
                val nop = baiNopMap[bai.id]
                val trangThai = trangThaiCuaHocSinh(nop, bai.hanNop, System.currentTimeMillis())
                TheThongTin(
                    tieuDe = bai.tieuDe,
                    noiDung = (if (bai.loaiEnum == LoaiBaiGiao.GIAY) "Bài giấy" else "Trắc nghiệm") +
                        " — Hạn nộp: ${dinhDangNgayGio(bai.hanNop)}" +
                        " — ${nhanTrangThai(trangThai)}" +
                        (if (nop?.diem != null) " — Điểm: ${nop.diem} / 10" else ""),
                    onClick = { onMoBai(bai) },
                )
            }
        }
        ThongBaoLoi(loi)
        Spacer(Modifier.height(16.dp))
        NutPhu("Quay lại", onClick = onBack)
    }
}

// ============================================================================
// LÀM BÀI TRẮC NGHIỆM: đếm ngược, hết giờ tự nộp, 1 lượt, chấm thang 10.
// Hạn chế V1: đồng hồ chạy trên máy học sinh, nếu thoát app giữa chừng
// rồi vào lại thì đồng hồ tính lại từ đầu, nhưng bài đã nộp thì không
// được làm lại vì máy chủ đã có bài nộp.
// ============================================================================

@Composable
fun LamTracNghiemScreen(
    repo: GiaoBtvnRepository,
    bank: QuestionBank,
    baiGiao: BaiGiao,
    prefs: LocalPrefs,
    onXong: () -> Unit,
    onBack: () -> Unit,
) {
    val scope = rememberCoroutineScope()
    var baiCu by remember { mutableStateOf<BaiNop?>(null) }
    var daKiemTraCu by remember { mutableStateOf(false) }
    var loi by remember { mutableStateOf("") }
    var ketQua by remember { mutableStateOf<Double?>(null) }

    // Câu hỏi theo đúng thứ tự trong bài giao: câu assets lấy từ ngân hàng,
    // câu ảnh do cô nhập được tái tạo từ ảnh + đáp án đúng gắn kèm trong
    // bài giao (đáp án hiển thị là A/B/C/D, không xáo thứ tự chữ cái).
    val cauGoc = remember(baiGiao.cauHoiIds) {
        val theoId = bank.cauHoiTheoIds(baiGiao.cauHoiIds).associateBy { it.id }
        baiGiao.cauHoiIds.mapNotNull { id ->
            theoId[id] ?: run {
                val dap = baiGiao.dapAnCauAnh[id] ?: return@run null
                if (id !in baiGiao.cauHoiAnh) return@run null
                CauHoi(
                    id = id,
                    chuDe = baiGiao.chuDe,
                    bai = baiGiao.bai,
                    noiDung = "Câu hỏi dạng ảnh — xem ảnh câu hỏi bên dưới",
                    cacDapAn = listOf("A", "B", "C", "D"),
                    dapAnDung = dap,
                    doKho = 1,
                    laCauAnh = true,
                )
            }
        }
    }
    val cauTron = remember(cauGoc) { tronCauHoiVaDapAn(cauGoc) }
    val thoiGianHet = remember(baiGiao.id) {
        System.currentTimeMillis() + baiGiao.thoiGianPhut * 60L * 1000L
    }
    var chiSoHienTai by remember { mutableStateOf(0) }
    var dapAnTron by remember { mutableStateOf<Map<String, Int>>(emptyMap()) }
    var daNop by remember { mutableStateOf(false) }

    LaunchedEffect(baiGiao.id) {
        repo.layBaiNopCuaHocSinh(baiGiao.id, prefs.hocSinhId)
            .onSuccess { baiCu = it }
        daKiemTraCu = true
    }

    fun nopBai() {
        if (daNop) return
        daNop = true
        // Đổi đáp án đã chọn (theo vị trí đã trộn) về chỉ số gốc rồi mới
        // lưu, để thống kê sai của cô so sánh đúng với đáp án gốc.
        val dapAnGoc = mutableMapOf<String, Int>()
        for (cau in cauTron) {
            val daChonTron = dapAnTron[cau.id] ?: continue
            val goc = cau.thuTuGoc.getOrNull(daChonTron) ?: continue
            dapAnGoc[cau.id] = goc
        }
        val diem = chamDiemThang10(dapAnGoc, cauGoc)
        scope.launch {
            repo.nopBaiTracNghiem(
                baiGiao.id,
                BaiNop(
                    hocSinhId = prefs.hocSinhId,
                    dapAn = dapAnGoc,
                    diem = diem,
                    trangThai = "DA_NOP",
                    thoiGianNop = System.currentTimeMillis(),
                ),
            ).onSuccess { ketQua = diem }
                .onFailure { loi = it.message ?: "Không nộp được bài"; daNop = false }
        }
    }

    CanhDoc {
        TieuDeCanh(baiGiao.tieuDe, "Trắc nghiệm — ${baiGiao.thoiGianPhut} phút — chỉ làm 1 lượt")
        val cu = baiCu
        val diemKetQua = ketQua
        when {
            !daKiemTraCu -> Text("Đang tải bài...")
            cu != null -> {
                Text("Bạn đã làm bài này rồi.", fontSize = 18.sp, fontWeight = FontWeight.Bold)
                if (cu.diem != null) Text("Điểm của bạn: ${cu.diem} / 10", fontSize = 20.sp)
                Spacer(Modifier.height(16.dp))
                NutPhu("Quay lại", onClick = onBack)
            }
            diemKetQua != null -> {
                Text("Bạn đã nộp bài!", fontSize = 18.sp, fontWeight = FontWeight.Bold)
                Text("Điểm của bạn: $diemKetQua / 10", fontSize = 22.sp)
                Text("Số câu đúng: ${(diemKetQua * cauGoc.size / 10).toInt()} / ${cauGoc.size}")
                Spacer(Modifier.height(16.dp))
                NutLon("Về danh sách bài", onClick = onXong)
            }
            cauTron.isEmpty() -> {
                Text("Bài này không còn câu hỏi nào, hãy báo cô kiểm tra lại.")
                Spacer(Modifier.height(16.dp))
                NutPhu("Quay lại", onClick = onBack)
            }
            else -> {
                DongHoDemNguoc(thoiGianHet) { nopBai() }
                Spacer(Modifier.height(16.dp))
                val cau = cauTron[chiSoHienTai]
                Text("Câu ${chiSoHienTai + 1} / ${cauTron.size}", fontSize = 17.sp, fontWeight = FontWeight.Bold)
                Spacer(Modifier.height(8.dp))
                Text(cau.noiDung, fontSize = 18.sp)
                val anhCau = baiGiao.cauHoiAnh[cau.id]
                if (anhCau != null) {
                    val bitmapCau = remember(anhCau) { giaiMaBase64ThanhBitmap(anhCau) }
                    if (bitmapCau != null) {
                        Spacer(Modifier.height(8.dp))
                        Image(
                            bitmapCau.asImageBitmap(),
                            contentDescription = "Ảnh câu hỏi",
                            modifier = Modifier.fillMaxWidth().height(240.dp),
                        )
                        Text("Chọn đáp án A, B, C hoặc D theo ảnh câu hỏi.", fontSize = 14.sp, color = Color.Gray)
                    }
                }
                Spacer(Modifier.height(12.dp))
                cau.cacDapAn.forEachIndexed { index, dapAn ->
                    Row(
                        verticalAlignment = Alignment.CenterVertically,
                        modifier = Modifier.clickable {
                            dapAnTron = dapAnTron + (cau.id to index)
                        }.padding(vertical = 4.dp),
                    ) {
                        RadioButton(
                            selected = dapAnTron[cau.id] == index,
                            onClick = { dapAnTron = dapAnTron + (cau.id to index) },
                        )
                        Text(dapAn, fontSize = 17.sp)
                    }
                }
                Spacer(Modifier.height(16.dp))
                NutPhu("Câu trước") {
                    if (chiSoHienTai > 0) chiSoHienTai--
                }
                Spacer(Modifier.height(8.dp))
                NutPhu("Câu sau") {
                    if (chiSoHienTai < cauTron.size - 1) chiSoHienTai++
                }
                Spacer(Modifier.height(16.dp))
                NutLon("Nộp bài") { nopBai() }
                Text("Bạn đã trả lời ${dapAnTron.size} / ${cauTron.size} câu.", fontSize = 14.sp, color = Color.Gray)
            }
        }
        ThongBaoLoi(loi)
        if (cu == null && diemKetQua == null) {
            Spacer(Modifier.height(16.dp))
            NutPhu("Quay lại", onClick = onBack)
        }
    }
}

// ============================================================================
// NỘP BÀI GIẤY: chụp ảnh bằng camera hoặc chọn từ thư viện, tối đa 3 ảnh.
// Ảnh được nén 1024px JPEG 70 và tính aHash ngay trên máy học sinh trước
// khi nộp, để phía cô so sánh trùng sau.
// ============================================================================

@Composable
fun NopBaiGiayScreen(
    repo: GiaoBtvnRepository,
    baiGiao: BaiGiao,
    prefs: LocalPrefs,
    onXong: () -> Unit,
    onBack: () -> Unit,
) {
    val context = LocalContext.current
    val scope = rememberCoroutineScope()
    var baiCu by remember { mutableStateOf<BaiNop?>(null) }
    var daKiemTraCu by remember { mutableStateOf(false) }
    var anhUris by remember { mutableStateOf<List<Uri>>(emptyList()) }
    var anhChupUri by remember { mutableStateOf<Uri?>(null) }
    var loi by remember { mutableStateOf("") }
    var thongBao by remember { mutableStateOf("") }
    var dangNop by remember { mutableStateOf(false) }

    val chonTuThuVien = rememberLauncherForActivityResult(ActivityResultContracts.GetMultipleContents()) { uris ->
        anhUris = (anhUris + uris).take(3)
        if (uris.size + anhUris.size > 3) loi = "Mỗi bài chỉ nộp tối đa 3 ảnh"
    }
    val chupAnh = rememberLauncherForActivityResult(ActivityResultContracts.TakePicture()) { thanhCong ->
        val uri = anhChupUri
        if (thanhCong && uri != null) {
            anhUris = (anhUris + uri).take(3)
        }
    }
    val xinQuyenCamera = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { duocCap ->
        if (duocCap) {
            val file = taoFileAnhTam(context)
            val uri = FileProvider.getUriForFile(context, "${context.packageName}.fileprovider", file)
            anhChupUri = uri
            chupAnh.launch(uri)
        } else {
            loi = "Bạn chưa cấp quyền camera, hãy chọn ảnh từ thư viện"
        }
    }

    LaunchedEffect(baiGiao.id) {
        repo.layBaiNopCuaHocSinh(baiGiao.id, prefs.hocSinhId)
            .onSuccess { baiCu = it }
        daKiemTraCu = true
    }

    val cu = baiCu
    val duocNopLai = cu == null || cu.trangThai == "YEU_CAU_NOP_LAI"

    CanhDoc {
        TieuDeCanh(baiGiao.tieuDe, "Bài giấy — Hạn nộp: ${dinhDangNgayGio(baiGiao.hanNop)}")
        if (baiGiao.noiDung.isNotBlank()) {
            Text(baiGiao.noiDung, fontSize = 17.sp)
            Spacer(Modifier.height(8.dp))
        }
        if (baiGiao.anhDeBase64.isNotBlank()) {
            val anhDe = remember(baiGiao.anhDeBase64) { giaiMaBase64ThanhBitmap(baiGiao.anhDeBase64) }
            if (anhDe != null) {
                Image(anhDe.asImageBitmap(), contentDescription = "Ảnh đề của cô", modifier = Modifier.fillMaxWidth().height(200.dp))
            }
        }
        if (!daKiemTraCu) {
            Text("Đang tải...")
        } else if (!duocNopLai) {
            if (cu?.trangThai == "CHO_DUYET_TRUNG") {
                Text("Bài của bạn đang chờ cô kiểm tra vì ảnh gần giống bài của bạn khác. Cô xác nhận xong mới được chấm điểm.", fontSize = 16.sp)
            } else if (cu?.diem != null) {
                Text("Bạn đã nộp bài này rồi.", fontSize = 17.sp, fontWeight = FontWeight.Bold)
                Text("Điểm của bạn: ${cu.diem} / 10", fontSize = 20.sp)
                if (cu.ghiChuGiaoVien.isNotBlank()) Text("Nhận xét của cô: ${cu.ghiChuGiaoVien}")
            } else {
                Text("Bạn đã nộp bài này rồi, đang chờ cô chấm điểm.", fontSize = 17.sp)
            }
            Spacer(Modifier.height(16.dp))
            NutPhu("Quay lại", onClick = onBack)
        } else {
            if (cu?.trangThai == "YEU_CAU_NOP_LAI") {
                Text("Cô đã yêu cầu bạn nộp lại bài này.", fontSize = 16.sp, fontWeight = FontWeight.Bold, color = Color(0xFFD32F2F))
                if (cu.ghiChuGiaoVien.isNotBlank()) Text("Nhận xét của cô: ${cu.ghiChuGiaoVien}")
                Spacer(Modifier.height(8.dp))
            }
            Text("Chụp hoặc chọn tối đa 3 ảnh bài làm ra giấy của bạn:", fontSize = 16.sp)
            Spacer(Modifier.height(12.dp))
            NutLon("Chụp ảnh") {
                if (ContextCompat.checkSelfPermission(context, Manifest.permission.CAMERA) == PackageManager.PERMISSION_GRANTED) {
                    val file = taoFileAnhTam(context)
                    val uri = FileProvider.getUriForFile(context, "${context.packageName}.fileprovider", file)
                    anhChupUri = uri
                    chupAnh.launch(uri)
                } else {
                    xinQuyenCamera.launch(Manifest.permission.CAMERA)
                }
            }
            Spacer(Modifier.height(8.dp))
            NutPhu("Chọn ảnh từ thư viện") { chonTuThuVien.launch("image/*") }
            Spacer(Modifier.height(8.dp))
            Text("Đã chọn ${anhUris.size} / 3 ảnh", fontSize = 15.sp)
            anhUris.forEach { uri ->
                val bitmap = remember(uri) { giaiMaAnhTuUri(context, uri) }
                if (bitmap != null) {
                    Image(bitmap.asImageBitmap(), contentDescription = "Ảnh bài làm đã chọn", modifier = Modifier.fillMaxWidth().height(180.dp).padding(vertical = 4.dp))
                }
            }
            if (anhUris.isNotEmpty()) {
                NutPhu("Xóa ảnh đã chọn") { anhUris = emptyList() }
                Spacer(Modifier.height(8.dp))
            }
            Spacer(Modifier.height(12.dp))
            NutLon("Nộp bài", bat = anhUris.isNotEmpty() && !dangNop) {
                dangNop = true
                loi = ""
                scope.launch {
                    val anhBase64 = mutableListOf<String>()
                    val hashList = mutableListOf<String>()
                    var loiDocAnh = false
                    for (uri in anhUris) {
                        val bitmap = giaiMaAnhTuUri(context, uri)
                        if (bitmap == null) {
                            loiDocAnh = true
                            break
                        }
                        anhBase64.add(nenAnhBase64(bitmap))
                        hashList.add(tinhAHash(bitmap))
                    }
                    if (loiDocAnh) {
                        loi = "Có ảnh không đọc được, hãy chọn lại ảnh khác"
                        dangNop = false
                    } else {
                        repo.nopBaiGiay(
                            baiGiao.id,
                            BaiNop(
                                hocSinhId = prefs.hocSinhId,
                                anhBase64 = anhBase64,
                                aHash = hashList,
                                trangThai = "DA_NOP",
                                thoiGianNop = System.currentTimeMillis(),
                            ),
                        ).onSuccess { onXong() }
                            .onFailure { loi = "Không nộp được bài, kiểm tra mạng rồi thử lại" }
                        dangNop = false
                    }
                }
            }
        }
        ThongBaoLoi(loi)
        ThongBaoTot(thongBao)
        if (duocNopLai) {
            Spacer(Modifier.height(16.dp))
            NutPhu("Quay lại", onClick = onBack)
        }
    }
}

private fun taoFileAnhTam(context: android.content.Context): File {
    val thuMuc = File(context.cacheDir, "anh_bai").apply { mkdirs() }
    return File(thuMuc, "bai_${System.currentTimeMillis()}.jpg")
}

// ============================================================================
// ÔN BÀI TỰ DO: chọn theo chủ đề hoặc theo bài, lấy ngẫu nhiên, không
// giới hạn thời gian, không tính điểm lớp, làm xong mỗi câu hiện đáp án
// đúng ngay. Toàn bộ phần này chạy trên máy, không ghi gì lên Database.
// ============================================================================

@Composable
fun OnTuDoScreen(
    bank: QuestionBank,
    repo: GiaoBtvnRepository,
    prefs: LocalPrefs,
    onBack: () -> Unit,
) {
    // Ôn tập lấy câu từ 3 nguồn: ngân hàng trong app + ngân hàng chung
    // (ôn ngẫu nhiên theo chủ đề, không phải lục ngân hàng) + câu riêng
    // cũ của cô dạy lớp học sinh đang tham gia. Học sinh vẫn chỉ làm
    // bài được giao cho lớp mình, ôn tập này không tính điểm lớp.
    var cauNhap by remember { mutableStateOf<List<ImportedQuestion>>(emptyList()) }
    var anhTheoCau by remember { mutableStateOf<Map<String, String>>(emptyMap()) }
    LaunchedEffect(prefs.maLop) {
        val chung = repo.loadCommonQuestions().getOrNull() ?: emptyList()
        val riengCu = if (prefs.maLop.isNotBlank()) {
            val giaoVienId = repo.layLopTheoMa(prefs.maLop).getOrNull()?.giaoVienId ?: ""
            if (giaoVienId.isNotBlank()) repo.loadTeacherQuestions(giaoVienId).getOrNull() ?: emptyList() else emptyList()
        } else {
            emptyList()
        }
        val loc = (chung + riengCu).distinctBy { it.id }.filter { cau ->
            cau.dang == "TRAC_NGHIEM_ANH" && cau.trangThai == "DA_DUYET" && cau.dapAnDung != null
        }
        cauNhap = loc
        anhTheoCau = loc.associate { it.id to it.anhBase64 }
    }
    val tatCaCau = remember(bank, cauNhap) { bank.cauHoi + cauNhap.map { it.toCauHoi() } }
    var chuDe by remember { mutableStateOf("Tất cả") }
    var chuong by remember { mutableStateOf("Tất cả") }
    var bai by remember { mutableStateOf("Tất cả") }
    var soCau by remember { mutableStateOf(10) }
    var cauLuyen by remember { mutableStateOf<List<CauHoi>?>(null) }

    val cauDangLuyen = cauLuyen
    if (cauDangLuyen != null) {
        OnTuDoLamScreen(
            cauHoi = cauDangLuyen,
            anhTheoCau = anhTheoCau,
            onLuyenLai = { cauLuyen = null },
            onBack = onBack,
        )
        return
    }

    // Lọc ôn tập theo Môn/Chương (câu nhập mới) + Bài (câu assets cũ vẫn
    // giữ trường bài, câu nhập mới có bài rỗng nên chỉ khớp "Tất cả").
    val cacMon = listOf("Tất cả") + tatCaCau.map { it.chuDe }.filter { it.isNotBlank() }.distinct()
    val cacChuong = listOf("Tất cả") + tatCaCau
        .filter { chuDe == "Tất cả" || it.chuDe == chuDe }
        .map { it.chuong }.filter { it.isNotBlank() }.distinct()
    val cacBai = listOf("Tất cả") + tatCaCau
        .filter { (chuDe == "Tất cả" || it.chuDe == chuDe) && (chuong == "Tất cả" || it.chuong == chuong) }
        .map { it.bai }.filter { it.isNotBlank() }.distinct()
    val cauLoc = tatCaCau.filter { cau ->
        (chuDe == "Tất cả" || cau.chuDe == chuDe) &&
            (chuong == "Tất cả" || cau.chuong == chuong) &&
            (bai == "Tất cả" || cau.bai == bai)
    }
    CanhDoc {
        TieuDeCanh(
            "Ôn bài tự do",
            "Chọn Môn/Chương, hệ thống lấy ngẫu nhiên câu hỏi trong app và " +
                "câu đã duyệt của cô (nếu bạn đã tham gia lớp).",
        )
        Text("Môn:", fontWeight = FontWeight.Bold)
        cacMon.forEach { ten ->
            Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable {
                chuDe = ten
                chuong = "Tất cả"
                bai = "Tất cả"
            }) {
                RadioButton(selected = chuDe == ten, onClick = {
                    chuDe = ten
                    chuong = "Tất cả"
                    bai = "Tất cả"
                })
                Text(ten, fontSize = 16.sp)
            }
        }
        Spacer(Modifier.height(8.dp))
        Text("Chương:", fontWeight = FontWeight.Bold)
        cacChuong.forEach { ten ->
            Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable {
                chuong = ten
                bai = "Tất cả"
            }) {
                RadioButton(selected = chuong == ten, onClick = {
                    chuong = ten
                    bai = "Tất cả"
                })
                Text(ten, fontSize = 16.sp)
            }
        }
        Spacer(Modifier.height(8.dp))
        Text("Bài:", fontWeight = FontWeight.Bold)
        cacBai.forEach { ten ->
            Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable { bai = ten }) {
                RadioButton(selected = bai == ten, onClick = { bai = ten })
                Text(ten, fontSize = 16.sp)
            }
        }
        Spacer(Modifier.height(12.dp))
        Text("Số câu mỗi lượt ôn:", fontWeight = FontWeight.Bold)
        listOf(5, 10, 15).forEach { n ->
            Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable { soCau = n }) {
                RadioButton(selected = soCau == n, onClick = { soCau = n })
                Text("$n câu", fontSize = 16.sp)
            }
        }
        Spacer(Modifier.height(16.dp))
        val soCauCoSan = cauLoc.size
        Text("Ngân hàng có $soCauCoSan câu cho lựa chọn này (gồm câu trong app và câu đã duyệt của cô).")
        Spacer(Modifier.height(8.dp))
        NutLon("Bắt đầu luyện", bat = soCauCoSan > 0) {
            cauLuyen = QuestionBank(cauLoc).layNgauNhien(cauLoc, soCau)
        }
        Spacer(Modifier.height(16.dp))
        NutPhu("Quay lại", onClick = onBack)
    }
}

@Composable
private fun OnTuDoLamScreen(
    cauHoi: List<CauHoi>,
    anhTheoCau: Map<String, String> = emptyMap(),
    onLuyenLai: () -> Unit,
    onBack: () -> Unit,
) {
    var chiSo by remember { mutableStateOf(0) }
    var daChon by remember { mutableStateOf<Int?>(null) }
    var daKiemTra by remember { mutableStateOf(false) }
    var soDung by remember { mutableStateOf(0) }
    var daXong by remember { mutableStateOf(false) }

    if (daXong) {
        CanhDoc {
            TieuDeCanh("Luyện xong!", "Bạn làm đúng $soDung / ${cauHoi.size} câu")
            Spacer(Modifier.height(16.dp))
            NutLon("Luyện lại lượt khác", onClick = onLuyenLai)
            Spacer(Modifier.height(8.dp))
            NutPhu("Về trang chính", onClick = onBack)
        }
        return
    }
    CanhDoc {
        val cau = cauHoi[chiSo]
        TieuDeCanh("Ôn bài tự do", "Câu ${chiSo + 1} / ${cauHoi.size}")
        Text(cau.noiDung, fontSize = 18.sp)
        val anhCau = anhTheoCau[cau.id]
        if (anhCau != null) {
            val bitmapCau = remember(anhCau) { giaiMaBase64ThanhBitmap(anhCau) }
            if (bitmapCau != null) {
                Spacer(Modifier.height(8.dp))
                Image(
                    bitmapCau.asImageBitmap(),
                    contentDescription = "Ảnh câu hỏi",
                    modifier = Modifier.fillMaxWidth().height(240.dp),
                )
                Text("Chọn đáp án A, B, C hoặc D theo ảnh câu hỏi.", fontSize = 14.sp, color = Color.Gray)
            }
        }
        Spacer(Modifier.height(12.dp))
        cau.cacDapAn.forEachIndexed { index, dapAn ->
            val mau = when {
                !daKiemTra -> Color.DarkGray
                index == cau.dapAnDung -> Color(0xFF2E7D32)
                index == daChon -> Color(0xFFD32F2F)
                else -> Color.DarkGray
            }
            Row(
                verticalAlignment = Alignment.CenterVertically,
                modifier = Modifier.clickable {
                    if (!daKiemTra) daChon = index
                }.padding(vertical = 4.dp),
            ) {
                RadioButton(selected = daChon == index, onClick = { if (!daKiemTra) daChon = index })
                Text(
                    dapAn,
                    fontSize = 17.sp,
                    color = mau,
                    fontWeight = if (daKiemTra && index == cau.dapAnDung) FontWeight.Bold else FontWeight.Normal,
                )
            }
        }
        Spacer(Modifier.height(16.dp))
        if (!daKiemTra) {
            NutLon("Kiểm tra", bat = daChon != null) {
                daKiemTra = true
                if (daChon == cau.dapAnDung) soDung++
            }
        } else {
            Text(
                if (daChon == cau.dapAnDung) "Đúng rồi! Giỏi lắm." else "Chưa đúng. Đáp án đúng là: ${cau.cacDapAn[cau.dapAnDung]}",
                fontSize = 17.sp,
                fontWeight = FontWeight.Bold,
                color = if (daChon == cau.dapAnDung) Color(0xFF2E7D32) else Color(0xFFD32F2F),
            )
            Spacer(Modifier.height(16.dp))
            NutLon(if (chiSo < cauHoi.size - 1) "Câu tiếp theo" else "Xem kết quả") {
                if (chiSo < cauHoi.size - 1) {
                    chiSo++
                    daChon = null
                    daKiemTra = false
                } else {
                    daXong = true
                }
            }
        }
    }
}
