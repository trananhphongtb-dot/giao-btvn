package vn.giaobtvn.tieuhoc.ui

import androidx.compose.foundation.Image
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
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlinx.coroutines.launch
import vn.giaobtvn.tieuhoc.data.GiaoBtvnRepository
import vn.giaobtvn.tieuhoc.data.GiaoVienDaDangNhap
import vn.giaobtvn.tieuhoc.data.ImportedQuestion

/**
 * Ngân hàng BTVN chung: mọi câu giáo viên nào tạo rồi đều hiện ở đây
 * cho giáo viên khác tìm theo Môn, Lớp, Bài, Chuyên đề rồi dùng để
 * giao bài cho lớp của mình. Bài đã giao thì vẫn chỉ thuộc về lớp đó,
 * học sinh không tự lục ngân hàng này. Chỉ người tạo mới xóa được
 * câu của mình, người khác chỉ dùng nguyên bản.
 */
@Composable
fun NganHangChungScreen(
    repo: GiaoBtvnRepository,
    giaoVien: GiaoVienDaDangNhap,
    onBack: () -> Unit,
) {
    val scope = rememberCoroutineScope()
    var tatCa by remember { mutableStateOf<List<ImportedQuestion>>(emptyList()) }
    var dangTai by remember { mutableStateOf(true) }
    var loi by remember { mutableStateOf("") }
    var locMon by remember { mutableStateOf("") }
    var locLop by remember { mutableStateOf("") }
    var locBai by remember { mutableStateOf("") }
    var locChuyenDe by remember { mutableStateOf("") }
    var tuKhoa by remember { mutableStateOf("") }

    fun taiLai() {
        dangTai = true
        loi = ""
        scope.launch {
            repo.loadCommonQuestions()
                .onSuccess { tatCa = it }
                .onFailure { loi = "Không tải được ngân hàng chung, kiểm tra mạng rồi thử lại" }
            dangTai = false
        }
    }

    LaunchedEffect(Unit) { taiLai() }

    val cauLoc = tatCa.filter { cau ->
        (locMon.isBlank() || cau.mon.contains(locMon, ignoreCase = true)) &&
            (locLop.isBlank() || cau.khoi.contains(locLop, ignoreCase = true)) &&
            (locBai.isBlank() || (cau.bai ?: "").contains(locBai, ignoreCase = true)) &&
            (locChuyenDe.isBlank() || cau.chuyenDe.contains(locChuyenDe, ignoreCase = true)) &&
            (tuKhoa.isBlank() ||
                (cau.textGoc ?: "").contains(tuKhoa, ignoreCase = true) ||
                cau.tags.any { tag -> tag.contains(tuKhoa, ignoreCase = true) })
    }

    CanhDoc {
        TieuDeCanh(
            "Ngân hàng BTVN chung",
            "Câu giáo viên nào tạo rồi thì giáo viên khác cũng dùng được. " +
                "Tìm theo Môn, Lớp, Bài, Chuyên đề, rồi về màn giao bài để chọn câu.",
        )
        if (dangTai) {
            Text("Đang tải...")
        } else if (loi.isNotBlank()) {
            Text(loi, fontSize = 15.sp, color = Color(0xFFD32F2F), fontWeight = FontWeight.Bold)
        } else {
            Text("Đang có ${tatCa.size} câu trong ngân hàng chung.", fontSize = 16.sp, fontWeight = FontWeight.Bold)
        }
        Spacer(Modifier.height(12.dp))
        NutNhoQuanLy("Tải lại ngân hàng chung") { taiLai() }
        Spacer(Modifier.height(12.dp))
        OutlinedTextField(locMon, { locMon = it }, label = { Text("Lọc theo Môn (để trống = tất cả)") }, modifier = Modifier.fillMaxWidth())
        Spacer(Modifier.height(8.dp))
        OutlinedTextField(locLop, { locLop = it }, label = { Text("Lọc theo Lớp, ví dụ: Lớp 10 (để trống = tất cả)") }, modifier = Modifier.fillMaxWidth())
        Spacer(Modifier.height(8.dp))
        OutlinedTextField(locBai, { locBai = it }, label = { Text("Lọc theo Bài (để trống = tất cả)") }, modifier = Modifier.fillMaxWidth())
        Spacer(Modifier.height(8.dp))
        OutlinedTextField(locChuyenDe, { locChuyenDe = it }, label = { Text("Lọc theo Chuyên đề (để trống = tất cả)") }, modifier = Modifier.fillMaxWidth())
        Spacer(Modifier.height(8.dp))
        OutlinedTextField(tuKhoa, { tuKhoa = it }, label = { Text("Tìm trong nội dung câu hoặc thẻ") }, modifier = Modifier.fillMaxWidth())
        Spacer(Modifier.height(16.dp))
        Text("Khớp bộ lọc: ${cauLoc.size} câu", fontSize = 17.sp, fontWeight = FontWeight.Bold)
        if (cauLoc.isEmpty() && !dangTai) {
            Text("Chưa có câu nào khớp. Cô hãy thử nới bộ lọc, hoặc up câu mới vào ngân hàng chung.")
        }
        cauLoc.forEach { cau ->
            Column(Modifier.fillMaxWidth().padding(vertical = 8.dp)) {
                Text(
                    "${cau.mon} • ${cau.khoi}" +
                        (if (!cau.chuong.isNullOrBlank()) " • ${cau.chuong}" else "") +
                        (if (!cau.bai.isNullOrBlank()) " • Bài: ${cau.bai}" else "") +
                        (if (cau.chuyenDe.isNotBlank()) " • Chuyên đề: ${cau.chuyenDe}" else ""),
                    fontSize = 15.sp,
                    fontWeight = FontWeight.Bold,
                )
                Text(
                    "Người tạo: " + (cau.giaoVienTen.ifBlank { "Giáo viên khác" }) +
                        (if (cau.doKho != null) " • Mức độ: ${cau.doKho}" else "") +
                        (if (cau.tags.isNotEmpty()) " • Thẻ: ${cau.tags.joinToString(", ")}" else ""),
                    fontSize = 14.sp,
                    color = Color.DarkGray,
                )
                val anh = remember(cau.anhBase64) { giaiMaBase64ThanhBitmap(cau.anhBase64) }
                if (anh != null) {
                    Image(
                        anh.asImageBitmap(),
                        contentDescription = "Ảnh câu hỏi ngân hàng chung",
                        modifier = Modifier.fillMaxWidth().height(160.dp).padding(vertical = 4.dp),
                    )
                }
                if (!cau.textGoc.isNullOrBlank()) {
                    Text(cau.textGoc, fontSize = 14.sp, color = Color.DarkGray)
                }
                if (cau.giaoVienId == giaoVien.uid) {
                    Spacer(Modifier.height(4.dp))
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Text("Câu của cô, ", fontSize = 14.sp, color = Color(0xFF2E7D32))
                        NutNhoQuanLy("Xóa câu này") {
                            scope.launch {
                                repo.deleteCommonQuestion(cau.id, giaoVien.uid)
                                    .onSuccess { tatCa = tatCa.filter { it.id != cau.id } }
                                    .onFailure { loi = it.message ?: "Không xóa được câu này" }
                            }
                        }
                    }
                }
            }
        }
        ThongBaoLoi(loi)
        Spacer(Modifier.height(16.dp))
        NutPhu("Quay lại", onClick = onBack)
    }
}
