package vn.giaobtvn.tieuhoc.ui

import android.app.Activity
import android.content.ClipData
import android.content.ClipboardManager
import android.content.Context
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
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Checkbox
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
import java.text.SimpleDateFormat
import java.util.Locale
import kotlinx.coroutines.launch
import vn.giaobtvn.tieuhoc.data.BaiGiao
import vn.giaobtvn.tieuhoc.data.BaiNop
import vn.giaobtvn.tieuhoc.data.CauHoi
import vn.giaobtvn.tieuhoc.data.DangNhapGoogle
import vn.giaobtvn.tieuhoc.data.GiaoBtvnRepository
import vn.giaobtvn.tieuhoc.data.GiaoVienDaDangNhap
import vn.giaobtvn.tieuhoc.data.ImportedQuestion
import vn.giaobtvn.tieuhoc.data.LopHoc
import vn.giaobtvn.tieuhoc.data.QuestionBank
import vn.giaobtvn.tieuhoc.data.TrangThaiNop
import vn.giaobtvn.tieuhoc.data.dinhDangNgayGio
import vn.giaobtvn.tieuhoc.data.khoangCachHamming
import vn.giaobtvn.tieuhoc.data.nenAnhBase64
import vn.giaobtvn.tieuhoc.data.nhanTrangThai
import vn.giaobtvn.tieuhoc.data.timBaiNghiTrung
import vn.giaobtvn.tieuhoc.data.tinhThongKe
import vn.giaobtvn.tieuhoc.data.trangThaiCuaHocSinh

/** Sao chép mã lớp vào bộ nhớ tạm của máy để cô dán cho học sinh. */
fun saoChepMaLop(context: Context, maLop: String) {
    val clipboard = context.getSystemService(Context.CLIPBOARD_SERVICE) as? ClipboardManager
    clipboard?.setPrimaryClip(ClipData.newPlainText("Mã lớp", maLop))
}

/** Nhập ngày dd/MM/yyyy và giờ HH:mm, trả về millis, null nếu sai định dạng. */
fun parseNgayGio(ngay: String, gio: String): Long? {
    return try {
        SimpleDateFormat("dd/MM/yyyy HH:mm", Locale("vi", "VN"))
            .parse("${ngay.trim()} ${gio.trim()}")?.time
    } catch (e: Exception) {
        null
    }
}

/**
 * Kiểm tra hạn nộp: phải sau thời điểm giao ít nhất 30 phút. Trả về
 * thông báo lỗi tiếng Việt, null = hợp lệ. Dùng chung cho bài giấy và
 * bài trắc nghiệm, để cô không giao bài mà hạn nộp đã qua hoặc quá gấp.
 */
fun loiHanNop(hanNop: Long?): String? {
    if (hanNop == null) return "Chưa chọn ngày giờ hạn nộp. Cô bấm chọn ngày và chọn giờ ở dưới."
    val toiThieu = System.currentTimeMillis() + 30L * 60L * 1000L
    if (hanNop < toiThieu) return "Hạn nộp phải sau thời điểm giao ít nhất 30 phút. Cô hãy chọn hạn nộp muộn hơn."
    return null
}

private fun dinhDangNgay(millis: Long): String =
    SimpleDateFormat("dd/MM/yyyy", Locale("vi", "VN")).format(java.util.Date(millis))

private fun dinhDangGio(gio: Int, phut: Int): String =
    String.format(Locale("vi", "VN"), "%02d:%02d", gio, phut)

/**
 * Chọn hạn nộp bằng bảng: 1 nút chọn ngày (lịch) + 1 nút chọn giờ
 * (đồng hồ), thay cho 2 ô gõ tay dd/MM/yyyy và HH:mm trước đây vốn
 * hay sai định dạng. Giá trị chọn được ghi vào ngay/gio để luồng giao
 * bài cũ (parseNgayGio) dùng lại không đổi.
 */
@OptIn(androidx.compose.material3.ExperimentalMaterial3Api::class)
@Composable
fun ChonHanNop(
    ngay: String,
    gio: String,
    onNgay: (String) -> Unit,
    onGio: (String) -> Unit,
) {
    var hienLich by remember { mutableStateOf(false) }
    var hienDongHo by remember { mutableStateOf(false) }
    val homNay = java.util.Calendar.getInstance()
    val trangThaiNgay = androidx.compose.material3.rememberDatePickerState(
        initialSelectedDateMillis = homNay.timeInMillis,
    )
    val gioMacDinh = (homNay.get(java.util.Calendar.HOUR_OF_DAY) + 1) % 24
    val trangThaiGio = androidx.compose.material3.rememberTimePickerState(
        initialHour = gioMacDinh,
        initialMinute = homNay.get(java.util.Calendar.MINUTE),
        is24Hour = true,
    )

    Text("Hạn nộp:", fontWeight = FontWeight.Bold)
    Spacer(Modifier.height(4.dp))
    Text(
        if (ngay.isNotBlank() && gio.isNotBlank()) "Hạn nộp: $ngay lúc $gio" else "Chưa chọn hạn nộp",
        fontSize = 16.sp,
    )
    Spacer(Modifier.height(8.dp))
    Row(verticalAlignment = Alignment.CenterVertically) {
        NutNhoQuanLy("Chọn ngày") { hienLich = true }
        NutNhoQuanLy("Chọn giờ") { hienDongHo = true }
    }
    Text(
        "Hạn nộp phải sau lúc giao ít nhất 30 phút, nếu không app sẽ báo lỗi và không giao bài.",
        fontSize = 14.sp,
        color = Color.Gray,
    )

    if (hienLich) {
        androidx.compose.material3.DatePickerDialog(
            onDismissRequest = { hienLich = false },
            confirmButton = {
                androidx.compose.material3.TextButton(
                    onClick = {
                        trangThaiNgay.selectedDateMillis?.let { onNgay(dinhDangNgay(it)) }
                        hienLich = false
                    },
                ) { Text("Chọn") }
            },
            dismissButton = {
                androidx.compose.material3.TextButton(onClick = { hienLich = false }) { Text("Hủy") }
            },
        ) {
            androidx.compose.material3.DatePicker(state = trangThaiNgay, showModeToggle = false)
        }
    }
    if (hienDongHo) {
        androidx.compose.material3.AlertDialog(
            onDismissRequest = { hienDongHo = false },
            confirmButton = {
                androidx.compose.material3.TextButton(
                    onClick = {
                        onGio(dinhDangGio(trangThaiGio.hour, trangThaiGio.minute))
                        hienDongHo = false
                    },
                ) { Text("Chọn") }
            },
            dismissButton = {
                androidx.compose.material3.TextButton(onClick = { hienDongHo = false }) { Text("Hủy") }
            },
            text = {
                androidx.compose.material3.TimePicker(state = trangThaiGio)
            },
        )
    }
}

@Composable
fun TeacherHomeScreen(
    activity: Activity,
    repo: GiaoBtvnRepository,
    onTaoLop: () -> Unit,
    onMoLop: (String) -> Unit,
    onDoiVai: () -> Unit,
    onNhapCauHoi: () -> Unit = {},
    // 3 lối vào rõ ràng: tạo BTVN trắc nghiệm (chọn lớp), tự up câu hỏi
    // vào ngân hàng chung, xem ngân hàng BTVN chung.
    onTaoTracNghiemChoLop: (String) -> Unit = {},
    onNganHangChung: () -> Unit = {},
) {
    val scope = rememberCoroutineScope()
    var giaoVien by remember { mutableStateOf(DangNhapGoogle.giaoVienHienTai()) }
    var lopList by remember { mutableStateOf<List<LopHoc>>(emptyList()) }
    var dangTai by remember { mutableStateOf(false) }
    var loi by remember { mutableStateOf("") }
    // Số lần bấm Tải lại: danh sách lớp trước đây chỉ tải 1 lần khi mở
    // màn, nên lớp vừa tạo xong mà quay lại trang chính vẫn có thể
    // thấy danh sách cũ. Bấm Tải lại sẽ tải lại đúng tài khoản đang
    // đăng nhập, không phụ thuộc vào lần tải đầu tiên.
    var lamMoi by remember { mutableStateOf(0) }
    var maTim by remember { mutableStateOf("") }
    var hienTimTheoMa by remember { mutableStateOf(false) }

    fun taiLop(gv: GiaoVienDaDangNhap) {
        dangTai = true
        loi = ""
        scope.launch {
            repo.layLopCuaGiaoVien(gv.uid)
                .onSuccess { lopList = it }
                .onFailure { loi = "Không tải được danh sách lớp, kiểm tra mạng rồi thử lại" }
            dangTai = false
        }
    }
    LaunchedEffect(giaoVien?.uid, lamMoi) {
        giaoVien?.let { taiLop(it) }
    }

    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp)) {
        TieuDeManHinh("Giáo viên", "Tạo lớp, giao bài, chấm bài và xem thống kê")
        val gv = giaoVien
        if (gv == null) {
            Text("Giáo viên cần đăng nhập Google để quản lý lớp của mình.", fontSize = 16.sp)
            Spacer(Modifier.height(16.dp))
            NutLon("Đăng nhập bằng Google") {
                loi = ""
                scope.launch {
                    DangNhapGoogle.dangNhap(activity)
                        .onSuccess { giaoVien = it }
                        .onFailure { loi = it.message ?: "Đăng nhập không thành công" }
                }
            }
        } else {
            Text("Xin chào, ${gv.ten}", fontSize = 18.sp, fontWeight = FontWeight.Bold)
            // Hiện rõ email đang đăng nhập, vì lớp chỉ hiện theo đúng
            // tài khoản đã tạo lớp. Nếu cô vừa đăng nhập vai học sinh
            // bằng Gmail khác rồi quay lại vai giáo viên, tài khoản ở
            // đây sẽ khác tài khoản tạo lớp, và lớp cũ sẽ không hiện.
            if (gv.email.isNotBlank()) {
                Text("Tài khoản: ${gv.email}", fontSize = 15.sp, color = Color.DarkGray)
            }
            if (loi.isNotBlank()) {
                Spacer(Modifier.height(8.dp))
                Text(loi, fontSize = 15.sp, color = Color(0xFFD32F2F), fontWeight = FontWeight.Bold)
            }
            Spacer(Modifier.height(16.dp))
            NutLon("Tạo lớp mới", onClick = onTaoLop)
            Spacer(Modifier.height(8.dp))
            NutLon("Tự up câu hỏi", onClick = onNhapCauHoi)
            Text(
                "Up file ảnh, PDF hoặc DOCX, máy cắt thử thành từng câu, " +
                    "cô duyệt rồi lưu vào ngân hàng chung, giáo viên khác cũng dùng được.",
                fontSize = 14.sp,
                color = Color.Gray,
            )
            Spacer(Modifier.height(8.dp))
            NutLon("Ngân hàng BTVN chung", onClick = onNganHangChung)
            Text(
                "Xem và tìm câu giáo viên khác đã tạo theo Môn, Lớp, Bài, " +
                    "Chuyên đề, rồi dùng để giao bài cho lớp của cô.",
                fontSize = 14.sp,
                color = Color.Gray,
            )
            Spacer(Modifier.height(16.dp))
            Text("Các lớp của tôi — quản lý lớp:", fontSize = 17.sp, fontWeight = FontWeight.Bold)
            Spacer(Modifier.height(8.dp))
            NutNhoQuanLy("Tải lại danh sách lớp") { lamMoi++ }
            Text(
                "Vừa tạo lớp xong mà chưa thấy lớp hiện ra thì bấm nút này, " +
                    "không cần thoát app hay đăng nhập lại.",
                fontSize = 14.sp,
                color = Color.Gray,
            )
            Spacer(Modifier.height(8.dp))
            if (dangTai) {
                Text("Đang tải...")
            } else if (lopList.isEmpty()) {
                Text("Chưa có lớp nào. Hãy tạo lớp đầu tiên rồi chia sẻ mã lớp cho học sinh.")
            } else {
                lopList.forEach { lop ->
                    TheQuanLyLop(
                        lop = lop,
                        onQuanLy = { onMoLop(lop.maLop) },
                        onTaoTracNghiem = { onTaoTracNghiemChoLop(lop.maLop) },
                    )
                }
            }
            Spacer(Modifier.height(16.dp))
            // Đường cứu nhỏ ở cuối, KHÔNG phải bước chính: bình thường
            // cô chỉ cần bấm vào lớp ở danh sách trên là quản lý được.
            // Chỉ khi lớp không hiện thì mới bấm đây để mở theo mã.
            NutPhu("Không thấy lớp? Mở theo mã") { hienTimTheoMa = !hienTimTheoMa }
            if (hienTimTheoMa) {
                Spacer(Modifier.height(8.dp))
                OutlinedTextField(
                    maTim,
                    { maTim = it.uppercase() },
                    label = { Text("Nhập mã lớp, ví dụ: AB12CD") },
                    modifier = Modifier.fillMaxWidth(),
                )
                Spacer(Modifier.height(8.dp))
                NutNhoQuanLy("Mở lớp theo mã") {
                    val ma = maTim.trim()
                    if (ma.isBlank()) {
                        loi = "Cô nhập mã lớp trước đã."
                    } else {
                        scope.launch {
                            repo.layLopTheoMa(ma)
                                .onSuccess { lopTim ->
                                    if (lopTim.giaoVienId.isNotBlank() && lopTim.giaoVienId != gv.uid) {
                                        loi = "Lớp này thuộc tài khoản khác, không phải tài khoản đang đăng nhập (${gv.email}). Cô hãy đăng nhập đúng tài khoản đã tạo lớp rồi mở lại."
                                    } else {
                                        onMoLop(lopTim.maLop)
                                    }
                                }
                                .onFailure { loi = "Không tìm thấy lớp với mã này, cô kiểm tra lại mã lớp." }
                        }
                    }
                }
            }
            Spacer(Modifier.height(16.dp))
            NutPhu("Đăng xuất") {
                DangNhapGoogle.dangXuat()
                giaoVien = null
                lopList = emptyList()
            }
        }
        ThongBaoLoi(loi)
        Spacer(Modifier.height(16.dp))
        NutPhu("Đổi vai", onClick = onDoiVai)
    }
}

/**
 * Thẻ quản lý 1 lớp trên trang chính giáo viên: tên lớp luôn đi kèm mã
 * lớp ở ngay sau tên, mã sao chép được bằng 1 nút, và có nút "Quản lý
 * lớp" rõ ràng để vào màn quản lý (danh sách học sinh, bài đã giao),
 * không phải đoán là bấm vào tên lớp.
 */
@Composable
fun TheQuanLyLop(
    lop: LopHoc,
    onQuanLy: () -> Unit,
    onTaoTracNghiem: () -> Unit,
) {
    val context = LocalContext.current
    var daSaoChep by remember { mutableStateOf(false) }
    androidx.compose.material3.Card(
        colors = androidx.compose.material3.CardDefaults.cardColors(containerColor = Color.White),
        modifier = Modifier.fillMaxWidth().padding(vertical = 4.dp),
    ) {
        Column(Modifier.padding(16.dp)) {
            Text("${lop.tenLop} — Mã: ${lop.maLop}", fontSize = 17.sp, fontWeight = FontWeight.Bold)
            Spacer(Modifier.height(4.dp))
            Text("${lop.hocSinh.size} học sinh đã tham gia", fontSize = 15.sp, color = Color.DarkGray)
            Spacer(Modifier.height(12.dp))
            Row(verticalAlignment = Alignment.CenterVertically) {
                NutNhoQuanLy("Quản lý lớp", onClick = onQuanLy)
                NutNhoQuanLy("Sao chép mã") {
                    saoChepMaLop(context, lop.maLop)
                    daSaoChep = true
                }
            }
            if (daSaoChep) {
                Spacer(Modifier.height(4.dp))
                Text("Đã sao chép mã ${lop.maLop}", fontSize = 14.sp, color = Color(0xFF2E7D32))
            }
            Spacer(Modifier.height(8.dp))
            NutNhoQuanLy("Giao bài trắc nghiệm", onClick = onTaoTracNghiem)
        }
    }
}

@Composable
fun NutNhoQuanLy(text: String, onClick: () -> Unit) {
    androidx.compose.material3.OutlinedButton(
        onClick = onClick,
        modifier = Modifier.padding(end = 8.dp),
    ) {
        Text(text, fontSize = 14.sp)
    }
}

@Composable
fun TaoLopScreen(
    repo: GiaoBtvnRepository,
    giaoVien: GiaoVienDaDangNhap,
    onVaoLop: (String) -> Unit,
    onBack: () -> Unit,
) {
    val scope = rememberCoroutineScope()
    val context = LocalContext.current
    var tenLop by remember { mutableStateOf("") }
    var lopMoi by remember { mutableStateOf<LopHoc?>(null) }
    var loi by remember { mutableStateOf("") }
    var dangTao by remember { mutableStateOf(false) }
    var daSaoChep by remember { mutableStateOf(false) }

    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp)) {
        TieuDeManHinh("Tạo lớp mới")
        OutlinedTextField(
            value = tenLop,
            onValueChange = { tenLop = it },
            label = { Text("Tên lớp, ví dụ: Lớp 4A") },
            modifier = Modifier.fillMaxWidth(),
        )
        Spacer(Modifier.height(16.dp))
        NutLon("Tạo lớp", bat = tenLop.isNotBlank() && !dangTao) {
            loi = ""
            dangTao = true
            scope.launch {
                repo.taoLop(tenLop, giaoVien)
                    .onSuccess { lopMoi = it }
                    .onFailure { loi = "Không tạo được lớp, kiểm tra mạng rồi thử lại" }
                dangTao = false
            }
        }
        val moi = lopMoi
        if (moi != null) {
            Spacer(Modifier.height(16.dp))
            Text("Đã tạo lớp thành công!", fontSize = 17.sp, fontWeight = FontWeight.Bold)
            Text("${moi.tenLop} — Mã: ${moi.maLop}", fontSize = 22.sp, fontWeight = FontWeight.Bold)
            Text("Chia sẻ mã này cho học sinh để các em tham gia lớp.")
            Spacer(Modifier.height(12.dp))
            NutLon("Sao chép mã lớp") {
                saoChepMaLop(context, moi.maLop)
                daSaoChep = true
            }
            if (daSaoChep) {
                Spacer(Modifier.height(4.dp))
                Text("Đã sao chép mã ${moi.maLop}", fontSize = 15.sp, color = Color(0xFF2E7D32))
            }
            Spacer(Modifier.height(8.dp))
            NutLon("Vào lớp này — Quản lý lớp") { onVaoLop(moi.maLop) }
            Spacer(Modifier.height(8.dp))
            NutPhu("Về trang chính — xem lớp vừa tạo") { onBack() }
        }
        ThongBaoLoi(loi)
        Spacer(Modifier.height(16.dp))
        NutPhu("Quay lại", onClick = onBack)
    }
}

@Composable
fun LopDetailScreen(
    repo: GiaoBtvnRepository,
    maLop: String,
    onTaoBaiGiay: () -> Unit,
    onTaoTracNghiem: () -> Unit,
    onMoCham: (BaiGiao) -> Unit,
    onBack: () -> Unit,
) {
    val scope = rememberCoroutineScope()
    val context = LocalContext.current
    var lop by remember { mutableStateOf<LopHoc?>(null) }
    var baiList by remember { mutableStateOf<List<BaiGiao>>(emptyList()) }
    var loi by remember { mutableStateOf("") }
    var daSaoChep by remember { mutableStateOf(false) }

    fun taiLai() {
        scope.launch {
            repo.layLopTheoMa(maLop)
                .onSuccess { lop = it }
                .onFailure { loi = "Không tải được lớp này" }
            repo.layBaiGiaoTheoLop(maLop)
                .onSuccess { baiList = it }
                .onFailure { loi = "Không tải được danh sách bài giao" }
        }
    }

    LaunchedEffect(maLop) {
        taiLai()
    }

    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp)) {
        val lopHienTai = lop
        TieuDeManHinh(
            lopHienTai?.tenLop ?: "Lớp $maLop",
            if (lopHienTai != null) "Mã lớp: ${lopHienTai.maLop}" else "",
        )
        // Mã lớp luôn hiện ngay sau tên lớp và sao chép được, để cô
        // không phải quay lại trang chính mới thấy mã.
        Row(verticalAlignment = Alignment.CenterVertically) {
            Text(
                "Mã lớp: $maLop",
                fontSize = 18.sp,
                fontWeight = FontWeight.Bold,
            )
            Spacer(Modifier.width(12.dp))
            NutNhoQuanLy("Sao chép mã") {
                saoChepMaLop(context, maLop)
                daSaoChep = true
            }
        }
        if (daSaoChep) {
            Spacer(Modifier.height(4.dp))
            Text("Đã sao chép mã $maLop", fontSize = 15.sp, color = Color(0xFF2E7D32))
        }
        Spacer(Modifier.height(12.dp))
        NutLon("Giao bài giấy (chụp ảnh)", onClick = onTaoBaiGiay)
        Spacer(Modifier.height(8.dp))
        NutLon("Giao bài trắc nghiệm", onClick = onTaoTracNghiem)
        Spacer(Modifier.height(20.dp))
        Text("Học sinh trong lớp (${lopHienTai?.hocSinh?.size ?: 0}):", fontSize = 17.sp, fontWeight = FontWeight.Bold)
        Spacer(Modifier.height(8.dp))
        NutNhoQuanLy("Tải lại danh sách học sinh") { taiLai() }
        Text(
            "Học sinh vào lớp sau khi cô mở màn này thì bấm nút trên để " +
                "danh sách cập nhật, không cần thoát ra vào lại.",
            fontSize = 14.sp,
            color = Color.Gray,
        )
        Spacer(Modifier.height(8.dp))
        if (lopHienTai?.hocSinh.isNullOrEmpty()) {
            Text("Chưa có học sinh nào tham gia. Chia sẻ mã lớp cho các em.")
        } else {
            lopHienTai?.hocSinh?.values?.forEach { ten ->
                Text("• $ten", fontSize = 16.sp)
            }
        }
        Spacer(Modifier.height(20.dp))
        Text("Bài đã giao:", fontSize = 17.sp, fontWeight = FontWeight.Bold)
        Spacer(Modifier.height(8.dp))
        if (baiList.isEmpty()) {
            Text("Chưa giao bài nào.")
        } else {
            baiList.forEach { bai ->
                TheThongTin(
                    tieuDe = bai.tieuDe,
                    noiDung = (if (bai.loaiEnum == vn.giaobtvn.tieuhoc.data.LoaiBaiGiao.GIAY) "Bài giấy" else "Trắc nghiệm") +
                        " — Hạn nộp: ${dinhDangNgayGio(bai.hanNop)}",
                    onClick = { onMoCham(bai) },
                )
            }
        }
        ThongBaoLoi(loi)
        Spacer(Modifier.height(16.dp))
        NutPhu("Quay lại", onClick = onBack)
    }
}

@Composable
fun TaoBaiGiayScreen(
    repo: GiaoBtvnRepository,
    maLop: String,
    onXong: () -> Unit,
    onBack: () -> Unit,
) {
    val context = LocalContext.current
    val scope = rememberCoroutineScope()
    var tieuDe by remember { mutableStateOf("") }
    var noiDung by remember { mutableStateOf("") }
    var ngay by remember { mutableStateOf("") }
    var gio by remember { mutableStateOf("") }
    var anhDeBase64 by remember { mutableStateOf("") }
    var loi by remember { mutableStateOf("") }
    var thongBao by remember { mutableStateOf("") }

    val chonAnh = rememberLauncherForActivityResult(ActivityResultContracts.GetContent()) { uri ->
        if (uri == null) return@rememberLauncherForActivityResult
        val bitmap = giaiMaAnhTuUri(context, uri)
        if (bitmap == null) {
            loi = "Không đọc được ảnh này"
        } else {
            anhDeBase64 = nenAnhBase64(bitmap)
            thongBao = "Đã chọn ảnh đề"
        }
    }

    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp)) {
        TieuDeManHinh("Giao bài giấy", "Học sinh làm ra giấy rồi chụp ảnh nộp, tối đa 3 ảnh")
        OutlinedTextField(tieuDe, { tieuDe = it }, label = { Text("Tiêu đề bài") }, modifier = Modifier.fillMaxWidth())
        Spacer(Modifier.height(8.dp))
        OutlinedTextField(noiDung, { noiDung = it }, label = { Text("Nội dung đề bài") }, modifier = Modifier.fillMaxWidth(), minLines = 3)
        Spacer(Modifier.height(8.dp))
        ChonHanNop(ngay = ngay, gio = gio, onNgay = { ngay = it }, onGio = { gio = it })
        Spacer(Modifier.height(12.dp))
        NutPhu(if (anhDeBase64.isBlank()) "Chọn ảnh đề (không bắt buộc)" else "Đổi ảnh đề") {
            chonAnh.launch("image/*")
        }
        Spacer(Modifier.height(16.dp))
        NutLon("Giao bài", bat = tieuDe.isNotBlank()) {
            val hanNop = parseNgayGio(ngay, gio)
            val loiHan = loiHanNop(hanNop)
            if (loiHan != null) {
                loi = loiHan
                return@NutLon
            }
            // loiHanNop đã chặn hanNop null, nhưng compiler vẫn thấy hanNop là Long?
            // nên cần chặn null tường minh ở đây thì BaiGiao(hanNop: Long) mới build được.
            if (hanNop == null) {
                loi = "Chưa chọn ngày giờ hạn nộp."
                return@NutLon
            }
            loi = ""
            scope.launch {
                repo.taoBaiGiao(
                    maLop,
                    BaiGiao(loai = "GIAY", tieuDe = tieuDe.trim(), noiDung = noiDung.trim(), anhDeBase64 = anhDeBase64, hanNop = hanNop),
                ).onSuccess { onXong() }
                    .onFailure { loi = "Không giao được bài, kiểm tra mạng rồi thử lại" }
            }
        }
        ThongBaoLoi(loi)
        ThongBaoTot(thongBao)
        Spacer(Modifier.height(16.dp))
        NutPhu("Quay lại", onClick = onBack)
    }
}

@Composable
fun TaoTracNghiemScreen(
    repo: GiaoBtvnRepository,
    bank: QuestionBank,
    maLop: String,
    onXong: () -> Unit,
    onBack: () -> Unit,
    giaoVienId: String = "",
) {
    val scope = rememberCoroutineScope()
    var tieuDe by remember { mutableStateOf("") }
    var chuDe by remember { mutableStateOf(bank.cacChuDe().firstOrNull() ?: "") }
    var bai by remember { mutableStateOf("Tất cả") }
    var cheDoTuDong by remember { mutableStateOf(true) }
    var soDe by remember { mutableStateOf("3") }
    var soVua by remember { mutableStateOf("3") }
    var soKho by remember { mutableStateOf("2") }
    var cauDaChon by remember { mutableStateOf<Set<String>>(emptySet()) }
    // Câu trắc nghiệm ảnh từ NGÂN HÀNG CHUNG (cộng thêm câu riêng cũ
    // nếu còn, tránh trùng id), lọc theo Môn/Lớp/Chương/Bài/Chuyên đề/
    // tag/mức độ.
    var cauNhap by remember { mutableStateOf<List<ImportedQuestion>>(emptyList()) }
    var locMonNhap by remember { mutableStateOf("") }
    var locLopNhap by remember { mutableStateOf("") }
    var locChuongNhap by remember { mutableStateOf("") }
    var locBaiNhap by remember { mutableStateOf("") }
    var locChuyenDeNhap by remember { mutableStateOf("") }
    var locTagNhap by remember { mutableStateOf("") }
    var locDoKhoNhap by remember { mutableStateOf<Int?>(null) }
    var cauNhapDaChon by remember { mutableStateOf<Set<String>>(emptySet()) }

    LaunchedEffect(giaoVienId) {
        val chung = repo.loadCommonQuestions().getOrNull() ?: emptyList()
        val riengCu = if (giaoVienId.isNotBlank()) {
            repo.loadTeacherQuestions(giaoVienId).getOrNull() ?: emptyList()
        } else {
            emptyList()
        }
        val gop = (chung + riengCu).distinctBy { it.id }
        cauNhap = gop.filter { cau -> cau.dang == "TRAC_NGHIEM_ANH" }
    }
    var thoiGianPhut by remember { mutableStateOf("15") }
    var ngay by remember { mutableStateOf("") }
    var gio by remember { mutableStateOf("") }
    var loi by remember { mutableStateOf("") }

    val cacBai = listOf("Tất cả") + bank.cacBaiTheoChuDe(chuDe)
    val cauLoc = bank.loc(chuDe, bai)
    val cauTuDong = remember(chuDe, bai, soDe, soVua, soKho) {
        bank.chonTuDongTheoDoKho(
            mapOf(1 to (soDe.toIntOrNull() ?: 0), 2 to (soVua.toIntOrNull() ?: 0), 3 to (soKho.toIntOrNull() ?: 0)),
            chuDe, bai,
        )
    }

    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp)) {
        TieuDeManHinh("Giao bài trắc nghiệm", "Cô chọn tay từng câu hoặc chọn tự động theo mức độ")
        OutlinedTextField(tieuDe, { tieuDe = it }, label = { Text("Tiêu đề bài") }, modifier = Modifier.fillMaxWidth())
        Spacer(Modifier.height(12.dp))
        Text("Chủ đề:", fontWeight = FontWeight.Bold)
        bank.cacChuDe().forEach { ten ->
            Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable {
                chuDe = ten
                bai = "Tất cả"
                cauDaChon = emptySet()
            }) {
                RadioButton(selected = chuDe == ten, onClick = {
                    chuDe = ten
                    bai = "Tất cả"
                    cauDaChon = emptySet()
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
        Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable { cheDoTuDong = true }) {
            RadioButton(selected = cheDoTuDong, onClick = { cheDoTuDong = true })
            Text("Chọn tự động theo mức độ", fontSize = 16.sp)
        }
        Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable { cheDoTuDong = false }) {
            RadioButton(selected = !cheDoTuDong, onClick = { cheDoTuDong = false })
            Text("Chọn tay từng câu", fontSize = 16.sp)
        }
        Spacer(Modifier.height(8.dp))
        if (cheDoTuDong) {
            OutlinedTextField(soDe, { soDe = it }, label = { Text("Số câu dễ") }, modifier = Modifier.fillMaxWidth())
            Spacer(Modifier.height(8.dp))
            OutlinedTextField(soVua, { soVua = it }, label = { Text("Số câu vừa") }, modifier = Modifier.fillMaxWidth())
            Spacer(Modifier.height(8.dp))
            OutlinedTextField(soKho, { soKho = it }, label = { Text("Số câu khó") }, modifier = Modifier.fillMaxWidth())
            Spacer(Modifier.height(8.dp))
            val tongYeuCau = (soDe.toIntOrNull() ?: 0) + (soVua.toIntOrNull() ?: 0) + (soKho.toIntOrNull() ?: 0)
            Text("Hệ thống sẽ lấy ${cauTuDong.size} câu trong tổng số $tongYeuCau câu yêu cầu.")
            if (cauTuDong.size < tongYeuCau) {
                Text("Ngân hàng không đủ câu ở mức độ đã chọn, cô hãy giảm số câu hoặc chọn bài khác.", color = Color(0xFFD32F2F))
            }
        } else {
            Text("Chọn câu hỏi (${cauDaChon.size} câu đã chọn, trong ${cauLoc.size} câu):", fontWeight = FontWeight.Bold)
            cauLoc.forEach { cau ->
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Checkbox(
                        checked = cau.id in cauDaChon,
                        onCheckedChange = { chon ->
                            cauDaChon = if (chon) cauDaChon + cau.id else cauDaChon - cau.id
                        },
                    )
                    Text(cau.noiDung, fontSize = 15.sp, modifier = Modifier.weight(1f))
                    Spacer(Modifier.width(8.dp))
                    Text(if (cau.doKho == 1) "Dễ" else if (cau.doKho == 2) "Vừa" else "Khó", fontSize = 13.sp, color = Color.Gray)
                }
            }
        }
        Spacer(Modifier.height(12.dp))
        Text("Câu hỏi từ ngân hàng BTVN chung (trắc nghiệm ảnh):", fontWeight = FontWeight.Bold)
        if (cauNhap.isEmpty()) {
            Text(
                "Ngân hàng chung chưa có câu trắc nghiệm nào. Về trang giáo viên, bấm " +
                    "\"Tự up câu hỏi\" để nhập file, hoặc bấm \"Ngân hàng BTVN chung\" để xem câu giáo viên khác đã tạo.",
                fontSize = 15.sp,
                color = Color.Gray,
            )
        } else {
            OutlinedTextField(locMonNhap, { locMonNhap = it }, label = { Text("Lọc theo Môn (để trống = tất cả)") }, modifier = Modifier.fillMaxWidth())
            Spacer(Modifier.height(8.dp))
            OutlinedTextField(locLopNhap, { locLopNhap = it }, label = { Text("Lọc theo Lớp, ví dụ: Lớp 10 (để trống = tất cả)") }, modifier = Modifier.fillMaxWidth())
            Spacer(Modifier.height(8.dp))
            OutlinedTextField(locChuongNhap, { locChuongNhap = it }, label = { Text("Lọc theo Chương (để trống = tất cả)") }, modifier = Modifier.fillMaxWidth())
            Spacer(Modifier.height(8.dp))
            OutlinedTextField(locBaiNhap, { locBaiNhap = it }, label = { Text("Lọc theo Bài (để trống = tất cả)") }, modifier = Modifier.fillMaxWidth())
            Spacer(Modifier.height(8.dp))
            OutlinedTextField(locChuyenDeNhap, { locChuyenDeNhap = it }, label = { Text("Lọc theo Chuyên đề (để trống = tất cả)") }, modifier = Modifier.fillMaxWidth())
            Spacer(Modifier.height(8.dp))
            OutlinedTextField(locTagNhap, { locTagNhap = it }, label = { Text("Lọc theo thẻ, ví dụ: OXY (để trống = tất cả)") }, modifier = Modifier.fillMaxWidth())
            Spacer(Modifier.height(8.dp))
            Text("Lọc theo mức độ:", fontWeight = FontWeight.Bold)
            Row(verticalAlignment = Alignment.CenterVertically) {
                Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable { locDoKhoNhap = null }) {
                    RadioButton(selected = locDoKhoNhap == null, onClick = { locDoKhoNhap = null })
                    Text("Tất cả", fontSize = 15.sp)
                }
                listOf(1, 2, 3).forEach { muc ->
                    Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable { locDoKhoNhap = muc }) {
                        RadioButton(selected = locDoKhoNhap == muc, onClick = { locDoKhoNhap = muc })
                        Text("$muc", fontSize = 15.sp)
                    }
                }
            }
            Spacer(Modifier.height(8.dp))
            val cauNhapLoc = cauNhap.filter { cau ->
                (locMonNhap.isBlank() || cau.mon.contains(locMonNhap, ignoreCase = true)) &&
                    (locLopNhap.isBlank() || cau.khoi.contains(locLopNhap, ignoreCase = true)) &&
                    (locChuongNhap.isBlank() || cau.chuong.contains(locChuongNhap, ignoreCase = true)) &&
                    (locBaiNhap.isBlank() || (cau.bai ?: "").contains(locBaiNhap, ignoreCase = true)) &&
                    (locChuyenDeNhap.isBlank() || cau.chuyenDe.contains(locChuyenDeNhap, ignoreCase = true)) &&
                    (locTagNhap.isBlank() || cau.tags.any { tag -> tag.contains(locTagNhap, ignoreCase = true) }) &&
                    (locDoKhoNhap == null || cau.doKho == locDoKhoNhap)
            }
            Text("Đã chọn ${cauNhapDaChon.size} câu ngân hàng chung, trong ${cauNhapLoc.size} câu khớp bộ lọc:", fontWeight = FontWeight.Bold)
            cauNhapLoc.forEach { cau ->
                Column(Modifier.fillMaxWidth().padding(vertical = 6.dp)) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Checkbox(
                            checked = cau.id in cauNhapDaChon,
                            onCheckedChange = { chon ->
                                cauNhapDaChon = if (chon) cauNhapDaChon + cau.id else cauNhapDaChon - cau.id
                            },
                        )
                        Text(
                            "${cau.mon} • ${cau.khoi}" +
                                (if (cau.chuong.isNotBlank()) " • ${cau.chuong}" else "") +
                                (if (!cau.bai.isNullOrBlank()) " • Bài: ${cau.bai}" else "") +
                                (if (cau.chuyenDe.isNotBlank()) " • Chuyên đề: ${cau.chuyenDe}" else "") +
                                (if (cau.giaoVienTen.isNotBlank()) " • Tạo bởi: ${cau.giaoVienTen}" else "") +
                                (if (cau.tags.isNotEmpty()) " • Thẻ: ${cau.tags.joinToString(", ")}" else "") +
                                (if (cau.doKho != null) " • Mức độ: ${cau.doKho}" else ""),
                            fontSize = 15.sp,
                            modifier = Modifier.weight(1f),
                        )
                        Spacer(Modifier.width(8.dp))
                        Text(
                            "Đáp án: " + when (cau.dapAnDung) {
                                0 -> "A"
                                1 -> "B"
                                2 -> "C"
                                3 -> "D"
                                else -> "?"
                            },
                            fontSize = 13.sp,
                            color = Color.Gray,
                        )
                    }
                    val anhNhap = remember(cau.anhBase64) { giaiMaBase64ThanhBitmap(cau.anhBase64) }
                    if (anhNhap != null) {
                        Image(
                            anhNhap.asImageBitmap(),
                            contentDescription = "Ảnh câu hỏi đã nhập",
                            modifier = Modifier.fillMaxWidth().height(160.dp).padding(vertical = 4.dp),
                        )
                    }
                    if (!cau.textGoc.isNullOrBlank()) {
                        Text(cau.textGoc, fontSize = 14.sp, color = Color.DarkGray)
                    }
                }
            }
        }
        Spacer(Modifier.height(12.dp))
        OutlinedTextField(thoiGianPhut, { thoiGianPhut = it }, label = { Text("Thời gian làm bài (phút)") }, modifier = Modifier.fillMaxWidth())
        Spacer(Modifier.height(8.dp))
        ChonHanNop(ngay = ngay, gio = gio, onNgay = { ngay = it }, onGio = { gio = it })
        Spacer(Modifier.height(16.dp))
        val cauIdsCuoi = if (cheDoTuDong) cauTuDong.map { it.id } else cauDaChon.toList()
        // Câu đã nhập được giao kèm ảnh và đáp án đúng trong chính bài giao,
        // để học sinh làm được mà không cần truy cập ngân hàng riêng của cô.
        val cauNhapDuocChon = cauNhap.filter { it.id in cauNhapDaChon }
        val cauIdsDayDu = (cauIdsCuoi + cauNhapDuocChon.map { it.id }).distinct()
        NutLon("Giao bài", bat = tieuDe.isNotBlank() && cauIdsDayDu.isNotEmpty()) {
            val hanNop = parseNgayGio(ngay, gio)
            val phut = thoiGianPhut.toIntOrNull()
            val loiHan = loiHanNop(hanNop)
            if (loiHan != null) {
                loi = loiHan
                return@NutLon
            }
            // loiHanNop đã chặn hanNop null, nhưng compiler vẫn thấy hanNop là Long?
            // nên cần chặn null tường minh ở đây thì BaiGiao(hanNop: Long) mới build được.
            if (hanNop == null) {
                loi = "Chưa chọn ngày giờ hạn nộp."
                return@NutLon
            }
            if (phut == null || phut <= 0) {
                loi = "Thời gian làm bài phải là số phút lớn hơn 0."
                return@NutLon
            }
            loi = ""
            scope.launch {
                val theoDoKho = if (cheDoTuDong) {
                    mapOf(
                        "1" to (soDe.toIntOrNull() ?: 0),
                        "2" to (soVua.toIntOrNull() ?: 0),
                        "3" to (soKho.toIntOrNull() ?: 0),
                    )
                } else {
                    emptyMap()
                }
                repo.taoBaiGiao(
                    maLop,
                    BaiGiao(
                        loai = "TRAC_NGHIEM",
                        tieuDe = tieuDe.trim(),
                        chuDe = chuDe,
                        bai = bai,
                        hanNop = hanNop,
                        thoiGianPhut = phut,
                        cauHoiIds = cauIdsDayDu,
                        soCauTheoDoKho = theoDoKho,
                        cauHoiAnh = cauNhapDuocChon.associate { it.id to it.anhBase64 },
                        dapAnCauAnh = cauNhapDuocChon.mapNotNull { cau ->
                            val dap = cau.dapAnDung ?: return@mapNotNull null
                            cau.id to dap
                        }.toMap(),
                    ),
                ).onSuccess { onXong() }
                    .onFailure { loi = "Không giao được bài, kiểm tra mạng rồi thử lại" }
            }
        }
        ThongBaoLoi(loi)
        Spacer(Modifier.height(16.dp))
        NutPhu("Quay lại", onClick = onBack)
    }
}

@Composable
fun ChamVaThongKeScreen(
    repo: GiaoBtvnRepository,
    bank: QuestionBank,
    maLop: String,
    baiGiao: BaiGiao,
    onBack: () -> Unit,
) {
    val scope = rememberCoroutineScope()
    var lop by remember { mutableStateOf<LopHoc?>(null) }
    var baiNopMap by remember { mutableStateOf<Map<String, BaiNop>>(emptyMap()) }
    var loi by remember { mutableStateOf("") }
    var thongBao by remember { mutableStateOf("") }

    fun taiLai() {
        scope.launch {
            repo.layLopTheoMa(maLop).onSuccess { lop = it }
            if (baiGiao.loaiEnum == vn.giaobtvn.tieuhoc.data.LoaiBaiGiao.GIAY) {
                repo.kiemTraTrung(baiGiao.id)
            }
            repo.layBaiNopTheoBaiGiao(baiGiao.id)
                .onSuccess { baiNopMap = it }
                .onFailure { loi = "Không tải được bài nộp" }
        }
    }
    LaunchedEffect(baiGiao.id) { taiLai() }

    val hocSinh = lop?.hocSinh ?: emptyMap()
    // Đáp án đúng gồm cả ngân hàng assets và câu hỏi ảnh do cô nhập
    // (gắn kèm trong bài giao), để thống kê câu sai không bỏ sót câu nhập.
    val dapAnDung = bank.cauHoiTheoIds(baiGiao.cauHoiIds).associate { it.id to it.dapAnDung } + baiGiao.dapAnCauAnh
    val thongKe = tinhThongKe(baiGiao, hocSinh, baiNopMap, dapAnDung, System.currentTimeMillis())
    val capTrung = timBaiNghiTrung(baiNopMap)

    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp)) {
        TieuDeManHinh(
            "Chấm và thống kê",
            "${baiGiao.tieuDe} — Hạn nộp: ${dinhDangNgayGio(baiGiao.hanNop)}",
        )
        Text("Thống kê lớp:", fontSize = 17.sp, fontWeight = FontWeight.Bold)
        HangChu("Tổng số học sinh", "${thongKe.tongHocSinh}")
        HangChu("Đã nộp", "${thongKe.daNop}")
        HangChu("Chưa nộp", "${thongKe.chuaNop}")
        HangChu("Quá hạn", "${thongKe.quaHan}")
        if (thongKe.choDuyetTrung > 0) HangChu("Chờ duyệt trùng", "${thongKe.choDuyetTrung}")
        if (thongKe.canNopLai > 0) HangChu("Cần nộp lại", "${thongKe.canNopLai}")
        HangChu("Tỉ lệ lớp đã nộp", "${(thongKe.tiLeDaNop * 100).toInt()}%")
        HangChu("Điểm trung bình lớp", thongKe.diemTrungBinh?.toString() ?: "Chưa có điểm")
        if (baiGiao.loaiEnum == vn.giaobtvn.tieuhoc.data.LoaiBaiGiao.TRAC_NGHIEM && thongKe.soLanSaiTheoCau.isNotEmpty()) {
            Spacer(Modifier.height(12.dp))
            Text("Câu học sinh sai nhiều nhất:", fontSize = 17.sp, fontWeight = FontWeight.Bold)
            val cauTheoId = bank.cauHoiTheoIds(baiGiao.cauHoiIds).associateBy { it.id } +
                baiGiao.cauHoiAnh.keys.associateWith { id ->
                    CauHoi(id = id, noiDung = "Câu hỏi dạng ảnh do cô nhập")
                }
            thongKe.soLanSaiTheoCau.entries.sortedByDescending { it.value }.take(5).forEach { (cauId, soLan) ->
                Text("• ${cauTheoId[cauId]?.noiDung ?: cauId}: sai $soLan lần", fontSize = 15.sp)
            }
        }
        Spacer(Modifier.height(20.dp))
        Text("Bài nộp từng học sinh:", fontSize = 17.sp, fontWeight = FontWeight.Bold)
        Spacer(Modifier.height(8.dp))
        if (hocSinh.isEmpty()) {
            Text("Lớp chưa có học sinh nào.")
        } else {
            hocSinh.forEach { (hocSinhId, ten) ->
                val nop = baiNopMap[hocSinhId]
                val trangThai = trangThaiCuaHocSinh(nop, baiGiao.hanNop, System.currentTimeMillis())
                Column(Modifier.fillMaxWidth().padding(vertical = 8.dp)) {
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text(ten, fontSize = 17.sp, fontWeight = FontWeight.Bold, modifier = Modifier.weight(1f))
                        ChipTrangThai(trangThai)
                    }
                    if (nop != null) {
                        if (nop.diem != null) {
                            Text("Điểm: ${nop.diem} / 10", fontSize = 16.sp)
                        } else {
                            Text("Chưa có điểm", fontSize = 15.sp, color = Color.Gray)
                        }
                        if (nop.ghiChuGiaoVien.isNotBlank()) {
                            Text("Nhận xét của cô: ${nop.ghiChuGiaoVien}", fontSize = 15.sp)
                        }
                        if (baiGiao.loaiEnum == vn.giaobtvn.tieuhoc.data.LoaiBaiGiao.GIAY) {
                            nop.anhBase64.forEach { anh ->
                                val bitmap = remember(anh) { giaiMaBase64ThanhBitmap(anh) }
                                if (bitmap != null) {
                                    Image(
                                        bitmap.asImageBitmap(),
                                        contentDescription = "Ảnh bài làm của $ten",
                                        modifier = Modifier.fillMaxWidth().height(200.dp).padding(vertical = 4.dp),
                                    )
                                }
                            }
                            if (nop.canhBaoTrung || trangThai == TrangThaiNop.CHO_DUYET_TRUNG) {
                                Text(
                                    "NGHI TRÙNG: ảnh bài này gần giống ảnh của học sinh khác. " +
                                        "Cô cần xác nhận ok thì mới được chấm điểm.",
                                    color = Color(0xFFD32F2F),
                                    fontWeight = FontWeight.Bold,
                                    fontSize = 15.sp,
                                )
                                val doiChieu = capTrung[hocSinhId] ?: emptyList()
                                doiChieu.forEach { idKhac ->
                                    val tenKhac = hocSinh[idKhac] ?: idKhac
                                    Text("Ảnh đối chiếu với bài của $tenKhac:", fontSize = 15.sp)
                                    baiNopMap[idKhac]?.anhBase64?.forEach { anhKhac ->
                                        val bitmapKhac = remember(anhKhac) { giaiMaBase64ThanhBitmap(anhKhac) }
                                        if (bitmapKhac != null) {
                                            Image(
                                                bitmapKhac.asImageBitmap(),
                                                contentDescription = "Ảnh bài làm của $tenKhac",
                                                modifier = Modifier.fillMaxWidth().height(200.dp).padding(vertical = 4.dp),
                                            )
                                        }
                                    }
                                }
                            }
                        }
                        // Trắc nghiệm đã chấm tự động nên cô không chấm tay
                        // lại ở đây, chỉ bài giấy mới có hàng chấm điểm.
                        if (baiGiao.loaiEnum == vn.giaobtvn.tieuhoc.data.LoaiBaiGiao.GIAY) HangChamDiem(
                            baiNop = nop,
                            choPhepCham = trangThai != TrangThaiNop.CHO_DUYET_TRUNG,
                            onDuyetOk = {
                                scope.launch {
                                    repo.duyetTrungOk(baiGiao.id, hocSinhId)
                                        .onSuccess { thongBao = "Đã xác nhận, cô có thể nhập điểm cho $ten"; taiLai() }
                                        .onFailure { loi = "Không xác nhận được, thử lại" }
                                }
                            },
                            onYeuCauLai = { ghiChu ->
                                scope.launch {
                                    repo.yeuCauNopLai(baiGiao.id, hocSinhId, ghiChu)
                                        .onSuccess { thongBao = "Đã yêu cầu $ten nộp lại"; taiLai() }
                                        .onFailure { loi = "Không gửi được yêu cầu, thử lại" }
                                }
                            },
                            onCham = { diem, ghiChu ->
                                scope.launch {
                                    repo.chamDiem(baiGiao.id, hocSinhId, diem, ghiChu)
                                        .onSuccess { thongBao = "Đã lưu điểm cho $ten"; taiLai() }
                                        .onFailure { loi = "Điểm phải từ 0 đến 10" }
                                }
                            },
                        )
                    } else {
                        Text(nhanTrangThai(trangThai), fontSize = 15.sp, color = Color.Gray)
                    }
                }
            }
        }
        ThongBaoLoi(loi)
        ThongBaoTot(thongBao)
        Spacer(Modifier.height(16.dp))
        NutPhu("Quay lại", onClick = onBack)
    }
}

/**
 * Hàng chấm điểm cho một bài nộp giấy. Khi bài đang chờ duyệt trùng thì
 * nút Lưu điểm bị khóa, cô phải bấm Xác nhận ok hoặc Yêu cầu nộp lại trước.
 */
@Composable
private fun HangChamDiem(
    baiNop: BaiNop,
    choPhepCham: Boolean,
    onDuyetOk: () -> Unit,
    onYeuCauLai: (String) -> Unit,
    onCham: (Double, String) -> Unit,
) {
    var diemText by remember { mutableStateOf(baiNop.diem?.toString() ?: "") }
    var ghiChu by remember { mutableStateOf(baiNop.ghiChuGiaoVien) }
    var loiCham by remember { mutableStateOf("") }

    Column {
        if (!choPhepCham) {
            Spacer(Modifier.height(8.dp))
            NutLon("Xác nhận ok, cho chấm điểm", onClick = onDuyetOk)
            Spacer(Modifier.height(8.dp))
            NutPhu("Yêu cầu nộp lại") { onYeuCauLai(ghiChu) }
        }
        Spacer(Modifier.height(8.dp))
        OutlinedTextField(diemText, { diemText = it }, label = { Text("Điểm (0 - 10)") }, modifier = Modifier.fillMaxWidth())
        Spacer(Modifier.height(8.dp))
        OutlinedTextField(ghiChu, { ghiChu = it }, label = { Text("Nhận xét của cô") }, modifier = Modifier.fillMaxWidth())
        Spacer(Modifier.height(8.dp))
        NutLon(
            "Lưu điểm",
            bat = choPhepCham,
        ) {
            val diem = diemText.toDoubleOrNull()
            if (diem == null || diem < 0.0 || diem > 10.0) {
                loiCham = "Điểm phải là số từ 0 đến 10"
            } else {
                loiCham = ""
                onCham(diem, ghiChu)
            }
        }
        ThongBaoLoi(loiCham)
    }
}
