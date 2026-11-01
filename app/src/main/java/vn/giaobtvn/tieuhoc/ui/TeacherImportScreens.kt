package vn.giaobtvn.tieuhoc.ui

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
import androidx.compose.material3.Slider
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
import kotlinx.coroutines.launch
import vn.giaobtvn.tieuhoc.data.DangBai
import vn.giaobtvn.tieuhoc.data.GiaoBtvnRepository
import vn.giaobtvn.tieuhoc.data.GiaoVienDaDangNhap
import vn.giaobtvn.tieuhoc.data.ImportedQuestion
import vn.giaobtvn.tieuhoc.data.LoaiFileNhap
import vn.giaobtvn.tieuhoc.data.SplitCandidate
import vn.giaobtvn.tieuhoc.data.gopBitmapDoc
import vn.giaobtvn.tieuhoc.data.nenAnhBase64
import vn.giaobtvn.tieuhoc.data.nhanCanhBao
import vn.giaobtvn.tieuhoc.data.processImport
import vn.giaobtvn.tieuhoc.data.tachBitmapDoc
import vn.giaobtvn.tieuhoc.data.tachBitmapThanhNhieu
import vn.giaobtvn.tieuhoc.data.taoIdCauNhap

private enum class BuocNhap { CHON_FILE, NHANH, CAT_THU, DUYET, CHON_DAP_AN, XONG }

/**
 * Luồng nhập câu hỏi của cô, đúng thiết kế đã chốt:
 * chọn file (ảnh/PDF/DOCX) -> chọn nhánh (Môn/Khối/Chương/Bài/Dạng)
 * -> máy cắt thử tự động -> cô duyệt cắt -> trắc nghiệm thì chọn đáp
 * án đúng từng câu -> lưu vào ngân hàng riêng của cô.
 * Không có câu nào được lưu khi chưa qua màn duyệt.
 */
@Composable
fun NhapCauHoiScreen(
    repo: GiaoBtvnRepository,
    giaoVien: GiaoVienDaDangNhap,
    onXong: () -> Unit,
    onBack: () -> Unit,
    // Tham số cũ giữ lại để không vỡ lời gọi cũ: từ bản ngân hàng chung,
    // mọi câu chốt đều vào ngân hàng chung, không còn riêng/chung theo cờ.
    dongGop: Boolean = false,
) {
    val context = LocalContext.current
    val scope = rememberCoroutineScope()
    var buoc by remember { mutableStateOf(BuocNhap.CHON_FILE) }
    var uriNhap by remember { mutableStateOf<Uri?>(null) }
    var loaiFile by remember { mutableStateOf(LoaiFileNhap.KHONG_BIET) }
    var mon by remember { mutableStateOf("") }
    var khoi by remember { mutableStateOf("") }
    var chuong by remember { mutableStateOf("") }
    var baiChung by remember { mutableStateOf("") }
    var chuyenDeChung by remember { mutableStateOf("") }
    var dang by remember { mutableStateOf(DangBai.TRAC_NGHIEM_ANH) }
    var monDaCo by remember { mutableStateOf<List<String>>(emptyList()) }
    var candidates by remember { mutableStateOf<List<SplitCandidate>>(emptyList()) }
    var daCat by remember { mutableStateOf(false) }
    var dapAnChon by remember { mutableStateOf<Map<Int, Int>>(emptyMap()) }
    var loi by remember { mutableStateOf("") }
    var thongBao by remember { mutableStateOf("") }
    var dangLuu by remember { mutableStateOf(false) }

    LaunchedEffect(giaoVien.uid) {
        repo.loadCommonQuestions()
            .onSuccess { monDaCo = it.map { cau -> cau.mon }.filter { m -> m.isNotBlank() }.distinct() }
    }

    val chonFile = rememberLauncherForActivityResult(ActivityResultContracts.GetContent()) { uri ->
        if (uri == null) return@rememberLauncherForActivityResult
        uriNhap = uri
        val mime = try {
            context.contentResolver.getType(uri) ?: ""
        } catch (e: Exception) {
            ""
        }
        loaiFile = when {
            mime == "application/pdf" -> LoaiFileNhap.PDF
            mime == "application/vnd.openxmlformats-officedocument.wordprocessingml.document" -> LoaiFileNhap.DOCX
            mime.startsWith("image/") -> LoaiFileNhap.ANH
            else -> LoaiFileNhap.KHONG_BIET
        }
        buoc = BuocNhap.NHANH
    }

    // Bước cắt thử: chạy đúng 1 lần cho 1 file, lỗi thì quay về chọn file.
    LaunchedEffect(buoc, uriNhap) {
        if (buoc == BuocNhap.CAT_THU && uriNhap != null && !daCat) {
            daCat = true
            processImport(context, uriNhap!!, loaiFile)
                .onSuccess { ketQua ->
                    loaiFile = ketQua.loaiFile
                    // Nhánh Môn/Chương cô chọn ở bước trước làm giá trị
                    // mặc định cho mọi câu; cô sửa từng câu ở màn duyệt.
                    candidates = ketQua.candidates.map { ungVien ->
                        ungVien.copy(
                            mon = mon.trim(),
                            chuong = chuong.trim(),
                            bai = baiChung.trim(),
                            chuyenDe = chuyenDeChung.trim(),
                        )
                    }
                    buoc = BuocNhap.DUYET
                }
                .onFailure { e ->
                    loi = e.message ?: "Không đọc được file này"
                    buoc = BuocNhap.CHON_FILE
                }
        }
    }

    fun luuVaoNganHang() {
        dangLuu = true
        loi = ""
        scope.launch {
            // Giá trị lưu là giá trị SAU KHI cô sửa ở màn duyệt (Môn,
            // Chương, Bài, Chuyên đề, tag, mức độ của từng câu), không
            // phải gợi ý thô. Câu lưu vào NGÂN HÀNG CHUNG, giáo viên
            // khác cũng dùng được, người tạo ghi rõ tên để phân quyền xóa.
            val questions = candidates.mapIndexed { index, ungVien ->
                ImportedQuestion(
                    id = taoIdCauNhap(),
                    giaoVienId = giaoVien.uid,
                    mon = ungVien.mon.ifBlank { mon.trim() },
                    khoi = khoi.trim(),
                    chuong = ungVien.chuong.ifBlank { chuong.trim() },
                    bai = ungVien.bai.ifBlank { baiChung.trim() }.takeIf { it.isNotBlank() },
                    dang = dang.name,
                    anhBase64 = ungVien.anhBase64,
                    textGoc = ungVien.textGoc,
                    dapAnDung = if (dang == DangBai.TRAC_NGHIEM_ANH) dapAnChon[index] else null,
                    doKho = ungVien.doKhoGoiY,
                    trangThai = "DA_DUYET",
                    nguonFile = loaiFile.name,
                    thuTu = index,
                    soLanGiao = 0,
                    doTinCay = ungVien.doTinCay,
                    tags = ungVien.tags,
                    nguonDongGop = giaoVien.uid,
                    chuyenDe = ungVien.chuyenDe.ifBlank { chuyenDeChung.trim() },
                    giaoVienTen = giaoVien.ten,
                )
            }
            repo.saveCommonQuestions(questions)
                .onSuccess {
                    thongBao = "Đã lưu ${questions.size} câu vào ngân hàng BTVN chung, giáo viên khác cũng dùng được"
                    buoc = BuocNhap.XONG
                }
                .onFailure { loi = "Không lưu được, kiểm tra mạng rồi thử lại" }
            dangLuu = false
        }
    }

    Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(20.dp)) {
        when (buoc) {
            BuocNhap.CHON_FILE -> {
                TieuDeManHinh(
                    if (dongGop) "Đóng góp cho ngân hàng BTVN" else "Tự up câu hỏi",
                    "Chọn file ảnh, PDF hoặc DOCX. Máy sẽ cắt thử thành từng câu, " +
                        "cô duyệt (sửa Môn/Chương/Bài/Chuyên đề, tag, mức độ) rồi mới lưu.",
                )
                NutLon("Chọn file ảnh, PDF hoặc DOCX") { chonFile.launch("*/*") }
                Text(
                    "Mẹo: file PDF hoặc DOCX có chữ sẵn thì máy cắt chính xác nhất. " +
                        "Ảnh chụp đề hoặc PDF scan thì máy dùng nhận diện chữ để cắt, " +
                        "cô cần kiểm tra lại ở màn duyệt. Máy không cắt được thì " +
                        "cô vẫn tách tay ở màn duyệt: nhập số câu trong ảnh, máy " +
                        "chia đều thành từng câu.",
                    fontSize = 14.sp,
                    color = Color.Gray,
                )
            }
            BuocNhap.NHANH -> {
                TieuDeManHinh(
                    "Chọn nhánh cho bài này",
                    "Ngân hàng chung phân theo Môn, Lớp, Chương, Bài và Chuyên đề. " +
                        "Nhánh này làm giá trị mặc định cho mọi câu, cô sửa từng câu ở màn duyệt.",
                )
                OutlinedTextField(mon, { mon = it }, label = { Text("Môn, ví dụ: Toán") }, modifier = Modifier.fillMaxWidth())
                if (monDaCo.isNotEmpty()) {
                    Spacer(Modifier.height(8.dp))
                    Text("Môn cô đã dùng trước đây, bấm để chọn nhanh:", fontSize = 14.sp, color = Color.Gray)
                    monDaCo.forEach { ten ->
                        Text(
                            "• $ten",
                            fontSize = 16.sp,
                            color = Color(0xFF1565C0),
                            modifier = Modifier.clickable { mon = ten }.padding(vertical = 2.dp),
                        )
                    }
                }
                Spacer(Modifier.height(8.dp))
                OutlinedTextField(chuong, { chuong = it }, label = { Text("Chương, ví dụ: Chương Đường tròn") }, modifier = Modifier.fillMaxWidth())
                Spacer(Modifier.height(8.dp))
                OutlinedTextField(baiChung, { baiChung = it }, label = { Text("Bài, không bắt buộc, ví dụ: Đường tròn trong mặt phẳng tọa độ") }, modifier = Modifier.fillMaxWidth())
                Spacer(Modifier.height(8.dp))
                OutlinedTextField(chuyenDeChung, { chuyenDeChung = it }, label = { Text("Chuyên đề, không bắt buộc, ví dụ: Đường tròn") }, modifier = Modifier.fillMaxWidth())
                Spacer(Modifier.height(8.dp))
                OutlinedTextField(khoi, { khoi = it }, label = { Text("Khối lớp, không bắt buộc, ví dụ: Lớp 4") }, modifier = Modifier.fillMaxWidth())
                Spacer(Modifier.height(12.dp))
                Text("Dạng bài:", fontWeight = FontWeight.Bold)
                Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable { dang = DangBai.TRAC_NGHIEM_ANH }) {
                    RadioButton(selected = dang == DangBai.TRAC_NGHIEM_ANH, onClick = { dang = DangBai.TRAC_NGHIEM_ANH })
                    Text("Trắc nghiệm dạng ảnh (cô sẽ chọn đáp án đúng từng câu)", fontSize = 16.sp)
                }
                Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable { dang = DangBai.VIET }) {
                    RadioButton(selected = dang == DangBai.VIET, onClick = { dang = DangBai.VIET })
                    Text("Bài viết (học sinh làm ra giấy rồi chụp ảnh nộp)", fontSize = 16.sp)
                }
                Spacer(Modifier.height(16.dp))
                NutLon(
                    "Cắt thử thành từng câu",
                    bat = mon.isNotBlank() && chuong.isNotBlank(),
                ) {
                    daCat = false
                    buoc = BuocNhap.CAT_THU
                }
                Text("Cần nhập Môn và Chương mới cắt được. Bài và Chuyên đề không bắt buộc, nhưng càng ghi đủ thì giáo viên khác càng dễ tìm trong ngân hàng chung.", fontSize = 14.sp, color = Color.Gray)
            }
            BuocNhap.CAT_THU -> {
                TieuDeManHinh("Đang cắt thử...", "Máy đang tách file thành từng câu, cô chờ một chút")
                Text("Nếu file dài hoặc ảnh mờ thì bước này có thể lâu hơn bình thường.")
            }
            BuocNhap.DUYET -> {
                DuyetCauScreen(
                    candidates = candidates,
                    onDoiCandidates = { candidates = it },
                    onChot = {
                        if (dang == DangBai.TRAC_NGHIEM_ANH) {
                            buoc = BuocNhap.CHON_DAP_AN
                        } else {
                            luuVaoNganHang()
                        }
                    },
                )
            }
            BuocNhap.CHON_DAP_AN -> {
                TieuDeManHinh("Chọn đáp án đúng", "Bắt buộc chọn đủ đáp án cho mọi câu mới lưu được")
                candidates.forEachIndexed { index, ungVien ->
                    Column(Modifier.fillMaxWidth().padding(vertical = 8.dp)) {
                        Text("Câu ${index + 1}:", fontSize = 17.sp, fontWeight = FontWeight.Bold)
                        val bitmap = remember(ungVien.anhBase64) { giaiMaBase64ThanhBitmap(ungVien.anhBase64) }
                        if (bitmap != null) {
                            Image(
                                bitmap.asImageBitmap(),
                                contentDescription = "Ảnh câu hỏi ${index + 1}",
                                modifier = Modifier.fillMaxWidth().height(200.dp).padding(vertical = 4.dp),
                            )
                        }
                        if (ungVien.textGoc != null) {
                            Text(ungVien.textGoc, fontSize = 14.sp, color = Color.DarkGray)
                        }
                        Row(verticalAlignment = Alignment.CenterVertically) {
                            listOf("A", "B", "C", "D").forEachIndexed { dapAnIndex, chu ->
                                Row(
                                    verticalAlignment = Alignment.CenterVertically,
                                    modifier = Modifier.clickable { dapAnChon = dapAnChon + (index to dapAnIndex) },
                                ) {
                                    RadioButton(
                                        selected = dapAnChon[index] == dapAnIndex,
                                        onClick = { dapAnChon = dapAnChon + (index to dapAnIndex) },
                                    )
                                    Text(chu, fontSize = 17.sp)
                                }
                            }
                        }
                    }
                }
                Spacer(Modifier.height(16.dp))
                NutLon(
                    "Lưu vào ngân hàng",
                    bat = !dangLuu && candidates.indices.all { dapAnChon.containsKey(it) },
                ) { luuVaoNganHang() }
                Spacer(Modifier.height(8.dp))
                NutPhu("Quay lại màn duyệt") { buoc = BuocNhap.DUYET }
            }
            BuocNhap.XONG -> {
                TieuDeManHinh("Đã lưu xong!", thongBao)
                Text(
                    if (dongGop) {
                        "Các câu này đã vào ngân hàng BTVN với cờ đóng góp của cô, " +
                            "học sinh lớp của cô có thể ôn tập từ các câu này."
                    } else {
                        "Các câu này đã vào ngân hàng riêng của cô. Về trang giáo viên, " +
                            "bấm \"Tạo BTVN trắc nghiệm\" để dùng ngay các câu vừa nhập."
                    },
                )
                Spacer(Modifier.height(16.dp))
                NutLon("Xong", onClick = onXong)
            }
        }
        ThongBaoLoi(loi)
        ThongBaoTot(thongBao)
        if (buoc != BuocNhap.XONG) {
            Spacer(Modifier.height(16.dp))
            NutPhu("Quay lại", onClick = onBack)
        }
    }
}

/**
 * Màn duyệt cắt: mỗi câu ảnh có nút Giữ (mặc định, không cần bấm),
 * Gộp với câu sau, Tách theo thanh trượt, Xóa, Lên/Xuống đổi thứ tự.
 * Nút Chốt chỉ bật khi còn ít nhất 1 câu, và chỉ câu đã chốt mới được lưu.
 */
@Composable
private fun DuyetCauScreen(
    candidates: List<SplitCandidate>,
    onDoiCandidates: (List<SplitCandidate>) -> Unit,
    onChot: () -> Unit,
) {
    var viTriCat by remember { mutableStateOf<Map<Int, Float>>(emptyMap()) }
    var soCauTay by remember { mutableStateOf<Map<Int, String>>(emptyMap()) }

    // Sửa từng câu trực tiếp trên ứng viên: cập nhật là đổi luôn danh
    // sách, nên thao tác Gộp/Tách về sau vẫn giữ đúng giá trị cô đã sửa.
    val capNhat: (Int, SplitCandidate) -> Unit = { chiSo, moi ->
        val danhSach = candidates.toMutableList()
        danhSach[chiSo] = moi
        onDoiCandidates(danhSach)
    }
    TieuDeManHinh(
        "Duyệt câu đã cắt",
        "Máy cắt thử được ${candidates.size} câu. Cô kiểm tra, sửa Môn/Chương/Bài/Chuyên đề, " +
            "tag và mức độ từng câu, gộp/tách/xóa rồi bấm Chốt. Không câu nào " +
            "vào ngân hàng khi chưa qua màn này.",
    )
    if (candidates.isEmpty()) {
        Text("Máy không cắt được câu nào từ file này. Cô hãy chọn file khác rõ hơn.")
    } else {
        candidates.forEachIndexed { index, ungVien ->
            Column(Modifier.fillMaxWidth().padding(vertical = 8.dp)) {
                Text(
                    "Câu ${index + 1}" + if (ungVien.soCauDuDoan > 0) " (máy đoán Câu ${ungVien.soCauDuDoan})" else "",
                    fontSize = 17.sp,
                    fontWeight = FontWeight.Bold,
                )
                if (ungVien.canhBao.isNotEmpty()) {
                    Text(
                        ungVien.canhBao.joinToString(", ") { nhanCanhBao(it) },
                        fontSize = 14.sp,
                        color = Color(0xFFD32F2F),
                        fontWeight = FontWeight.Bold,
                    )
                }
                val bitmap = remember(ungVien.anhBase64) { giaiMaBase64ThanhBitmap(ungVien.anhBase64) }
                if (bitmap != null) {
                    Image(
                        bitmap.asImageBitmap(),
                        contentDescription = "Ảnh câu hỏi ${index + 1}",
                        modifier = Modifier.fillMaxWidth().height(200.dp).padding(vertical = 4.dp),
                    )
                }
                if (ungVien.textGoc != null) {
                    Text(ungVien.textGoc, fontSize = 14.sp, color = Color.DarkGray)
                }
                // Cô sửa Môn/Chương/Bài/Chuyên đề, tag và mức độ của từng câu ngay tại đây.
                // Tag và mức độ ban đầu là gợi ý từ máy (câu có text mới có
                // gợi ý, câu cắt từ ảnh thì cô tự gắn), giá trị sau khi sửa
                // mới là giá trị lưu vào ngân hàng khi bấm Chốt.
                Spacer(Modifier.height(8.dp))
                OutlinedTextField(
                    ungVien.mon,
                    { capNhat(index, ungVien.copy(mon = it)) },
                    label = { Text("Môn của câu này") },
                    modifier = Modifier.fillMaxWidth(),
                )
                Spacer(Modifier.height(8.dp))
                OutlinedTextField(
                    ungVien.chuong,
                    { capNhat(index, ungVien.copy(chuong = it)) },
                    label = { Text("Chương của câu này") },
                    modifier = Modifier.fillMaxWidth(),
                )
                Spacer(Modifier.height(8.dp))
                OutlinedTextField(
                    ungVien.bai,
                    { capNhat(index, ungVien.copy(bai = it)) },
                    label = { Text("Bài của câu này") },
                    modifier = Modifier.fillMaxWidth(),
                )
                Spacer(Modifier.height(8.dp))
                OutlinedTextField(
                    ungVien.chuyenDe,
                    { capNhat(index, ungVien.copy(chuyenDe = it)) },
                    label = { Text("Chuyên đề của câu này") },
                    modifier = Modifier.fillMaxWidth(),
                )
                Spacer(Modifier.height(8.dp))
                OutlinedTextField(
                    ungVien.tags.joinToString(", "),
                    { textMoi ->
                        val tagsMoi = textMoi.split(",")
                            .map { tag -> tag.trim().uppercase() }
                            .filter { tag -> tag.isNotBlank() }
                        capNhat(index, ungVien.copy(tags = tagsMoi))
                    },
                    label = { Text("Thẻ nội dung, cách nhau bằng dấu phẩy, ví dụ: DUONG_TRON, OXY") },
                    modifier = Modifier.fillMaxWidth(),
                )
                Spacer(Modifier.height(8.dp))
                Text("Mức độ của câu này:", fontWeight = FontWeight.Bold)
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable { capNhat(index, ungVien.copy(doKhoGoiY = null)) }) {
                        RadioButton(selected = ungVien.doKhoGoiY == null, onClick = { capNhat(index, ungVien.copy(doKhoGoiY = null)) })
                        Text("Chưa gắn", fontSize = 15.sp)
                    }
                    listOf(1, 2, 3).forEach { muc ->
                        Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.clickable { capNhat(index, ungVien.copy(doKhoGoiY = muc)) }) {
                            RadioButton(selected = ungVien.doKhoGoiY == muc, onClick = { capNhat(index, ungVien.copy(doKhoGoiY = muc)) })
                            Text("$muc", fontSize = 15.sp)
                        }
                    }
                }
                // Tách: thanh trượt chọn vị trí cắt theo chiều cao ảnh.
                val tyLe = viTriCat[index] ?: 0.5f
                Text("Vị trí tách (nếu bấm Tách): ${(tyLe * 100).toInt()}% chiều cao ảnh", fontSize = 14.sp)
                Slider(
                    value = tyLe,
                    onValueChange = { viTriCat = viTriCat + (index to it) },
                    valueRange = 0.1f..0.9f,
                    modifier = Modifier.fillMaxWidth(),
                )
                // Tách tay khi máy không cắt được: cô đếm số câu trong
                // ảnh này rồi nhập N, máy chia đều ảnh thành N mảnh.
                // Dùng cho ảnh chụp nghiêng, đề chỉ đánh số, công thức
                // toán mà OCR đọc kém — không cần kéo pixel chính xác.
                Text(
                    "Máy không cắt được ảnh này? Nhập số câu trong ảnh rồi bấm Tách tay.",
                    fontSize = 14.sp,
                    color = Color.DarkGray,
                )
                Row(verticalAlignment = Alignment.CenterVertically) {
                    OutlinedTextField(
                        soCauTay[index] ?: "",
                        { soCauTay = soCauTay + (index to it.filter { c -> c.isDigit() }) },
                        label = { Text("Số câu trong ảnh") },
                        modifier = Modifier.weight(1f),
                    )
                    NutNho("Tách tay") {
                        val n = (soCauTay[index] ?: "").toIntOrNull() ?: return@NutNho
                        if (n < 2) return@NutNho
                        val goc = giaiMaBase64ThanhBitmap(ungVien.anhBase64) ?: return@NutNho
                        val manh = tachBitmapThanhNhieu(goc, n)
                        if (manh.size < 2) return@NutNho
                        val moi = candidates.toMutableList()
                        moi[index] = ungVien.copy(anhBase64 = nenAnhBase64(manh[0]))
                        for (i in 1 until manh.size) {
                            moi.add(
                                index + i,
                                ungVien.copy(
                                    anhBase64 = nenAnhBase64(manh[i]),
                                    textGoc = null,
                                    soCauDuDoan = 0,
                                    canhBao = listOf("CAN_KIEM_TRA"),
                                    tags = emptyList(),
                                    doKhoGoiY = null,
                                ),
                            )
                        }
                        onDoiCandidates(moi)
                    }
                }
                Row(verticalAlignment = Alignment.CenterVertically) {
                    NutNho("Gộp sau", bat = index < candidates.size - 1) {
                        val tren = giaiMaBase64ThanhBitmap(ungVien.anhBase64) ?: return@NutNho
                        val duoi = giaiMaBase64ThanhBitmap(candidates[index + 1].anhBase64) ?: return@NutNho
                        val gop = gopBitmapDoc(tren, duoi)
                        val textGop = listOfNotNull(ungVien.textGoc, candidates[index + 1].textGoc)
                            .joinToString("\n").takeIf { it.isNotBlank() }
                        val moi = candidates.toMutableList()
                        moi[index] = ungVien.copy(
                            anhBase64 = nenAnhBase64(gop),
                            textGoc = textGop,
                            canhBao = (ungVien.canhBao + candidates[index + 1].canhBao).distinct(),
                            doTinCay = minOf(ungVien.doTinCay, candidates[index + 1].doTinCay),
                            // Gộp: Môn/Chương lấy của câu trên, tag hợp 2 câu,
                            // mức độ lấy mức cao hơn trong 2 câu (nếu có).
                            tags = (ungVien.tags + candidates[index + 1].tags).distinct(),
                            doKhoGoiY = listOfNotNull(ungVien.doKhoGoiY, candidates[index + 1].doKhoGoiY).maxOrNull(),
                        )
                        moi.removeAt(index + 1)
                        onDoiCandidates(moi)
                    }
                    NutNho("Tách") {
                        val goc = giaiMaBase64ThanhBitmap(ungVien.anhBase64) ?: return@NutNho
                        val (tren, duoi) = tachBitmapDoc(goc, tyLe)
                        val text = ungVien.textGoc
                        val textTren: String?
                        val textDuoi: String?
                        if (text != null) {
                            val cat = (text.length * tyLe).toInt().coerceIn(0, text.length)
                            textTren = text.substring(0, cat).takeIf { it.isNotBlank() }
                            textDuoi = text.substring(cat).takeIf { it.isNotBlank() }
                        } else {
                            textTren = null
                            textDuoi = null
                        }
                        val moi = candidates.toMutableList()
                        moi[index] = ungVien.copy(anhBase64 = nenAnhBase64(tren), textGoc = textTren)
                        moi.add(
                            index + 1,
                            ungVien.copy(
                                anhBase64 = nenAnhBase64(duoi),
                                textGoc = textDuoi,
                                soCauDuDoan = 0,
                                canhBao = listOf("CAN_KIEM_TRA"),
                                // Câu tách ra chưa có tag/mức độ riêng, cô gắn
                                // lại ở chính màn duyệt này.
                                tags = emptyList(),
                                doKhoGoiY = null,
                            ),
                        )
                        onDoiCandidates(moi)
                    }
                    NutNho("Xóa") {
                        onDoiCandidates(candidates.filterIndexed { i, _ -> i != index })
                    }
                }
                Row(verticalAlignment = Alignment.CenterVertically) {
                    NutNho("Lên", bat = index > 0) {
                        val moi = candidates.toMutableList()
                        val tam = moi[index - 1]
                        moi[index - 1] = moi[index]
                        moi[index] = tam
                        onDoiCandidates(moi)
                    }
                    NutNho("Xuống", bat = index < candidates.size - 1) {
                        val moi = candidates.toMutableList()
                        val tam = moi[index + 1]
                        moi[index + 1] = moi[index]
                        moi[index] = tam
                        onDoiCandidates(moi)
                    }
                }
            }
        }
        Spacer(Modifier.height(16.dp))
        NutLon("Chốt ${candidates.size} câu này", bat = candidates.isNotEmpty(), onClick = onChot)
        Text(
            "Lưu ý: câu tràn sang trang sau ở bản này chưa tự gộp hoàn hảo, " +
                "cô dùng nút Gộp với câu sau để gộp tay. Nếu máy không nhận " +
                "được đầu câu nào, cô dùng Tách tay ở từng ảnh: nhập số câu " +
                "trong ảnh, máy chia đều thành từng câu. Câu lưu dạng ảnh " +
                "nên công thức toán trong ảnh vẫn hiển thị đúng như bản gốc " +
                "cho học sinh, dù máy không đọc được công thức thành chữ.",
            fontSize = 14.sp,
            color = Color.Gray,
        )
    }
}

@Composable
private fun NutNho(text: String, bat: Boolean = true, onClick: () -> Unit) {
    androidx.compose.material3.OutlinedButton(
        onClick = onClick,
        enabled = bat,
        modifier = Modifier.padding(end = 8.dp),
    ) {
        Text(text, fontSize = 14.sp)
    }
}
