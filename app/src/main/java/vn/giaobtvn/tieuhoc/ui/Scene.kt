package vn.giaobtvn.tieuhoc.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ColumnScope
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

// ============================================================================
// CẢNH DỌC MỖI TRANG — giao diện mới 2026-11-04.
// Mỗi màn hình là một cảnh dọc full màn hình: nền gradient dọc + vài
// hình tròn mờ trang trí ở góc, nội dung nằm trên thẻ trắng bo tròn.
// Không dùng ảnh ngoài, để app nhẹ và không phụ thuộc file ảnh.
// ============================================================================

private val CanhNenTren = Color(0xFFF6F8FC)
private val CanhNenGiua = Color(0xFFF6F8FC)
private val CanhNenDuoi = Color(0xFFF6F8FC)

/** Khung cảnh dọc: bọc toàn bộ nội dung một màn hình. */
@Composable
fun CanhDoc(noiDung: @Composable ColumnScope.() -> Unit) {
    Box(
        Modifier
            .fillMaxSize()
            .background(
                Brush.verticalGradient(
                    listOf(CanhNenTren, CanhNenGiua, CanhNenDuoi)
                )
            )
    ) {
        // Vòng tròn trang trí mờ ở góc trên và góc dưới, tạo cảm giác cảnh.
        Box(
            Modifier
                .size(0.dp)
                .offset((-60).dp, (-60).dp)
                .clip(CircleShape)
                .background(Color(0xFF90CAF9).copy(alpha = 0.35f))
        )
        Box(
            Modifier
                .size(0.dp)
                .align(Alignment.BottomEnd)
                .offset(50.dp, 50.dp)
                .clip(CircleShape)
                .background(Color(0xFF90CAF9).copy(alpha = 0.25f))
        )
        Column(
            Modifier
                .fillMaxSize()
                .verticalScroll(rememberScrollState())
                .padding(horizontal = 16.dp, vertical = 12.dp),
            content = noiDung,
        )
    }
}

/** Tiêu đề trên cảnh dọc: chữ trắng, nổi trên nền gradient. */
@Composable
fun TieuDeCanh(tieuDe: String, phuDe: String = "") {
    Text(tieuDe, fontSize = 23.sp, fontWeight = FontWeight.Bold, color = Color(0xFF0D47A1))
    if (phuDe.isNotBlank()) {
        Spacer(Modifier.height(4.dp))
        Text(phuDe, fontSize = 15.sp, color = Color.DarkGray)
    }
    Spacer(Modifier.height(10.dp))
}

/**
 * Một ô khung đóng khung: dùng cho danh sách học sinh, danh sách bài
 * giao, kết quả bài... Mỗi ô là một thẻ trắng bo tròn, viền nhẹ, các
 * hàng bên trong cân đối, không còn dòng rời rạc ngoài khung.
 */
@Composable
fun Khung(tieuDe: String, phuDe: String = "", noiDung: @Composable ColumnScope.() -> Unit) {
    Card(
        colors = CardDefaults.cardColors(containerColor = Color.White),
        shape = RoundedCornerShape(14.dp),
        elevation = CardDefaults.cardElevation(defaultElevation = 1.dp),
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 4.dp),
    ) {
        Column(Modifier.padding(16.dp)) {
            Text(tieuDe, fontSize = 18.sp, fontWeight = FontWeight.Bold, color = Color(0xFF0D47A1))
            if (phuDe.isNotBlank()) {
                Spacer(Modifier.height(2.dp))
                Text(phuDe, fontSize = 14.sp, color = Color.DarkGray)
            }
            Spacer(Modifier.height(10.dp))
            noiDung()
        }
    }
}

/** Một hàng trong ô khung: nhãn trái, giá trị phải, cân đối 2 đầu. */
@Composable
fun HangKhung(label: String, giaTri: String, onClick: (() -> Unit)? = null) {
    Row(
        Modifier
            .fillMaxWidth()
            .padding(vertical = 6.dp)
            .then(if (onClick != null) Modifier.clickable { onClick() } else Modifier),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Text(label, fontSize = 16.sp, color = Color.DarkGray, modifier = Modifier.weight(1f))
        Text(
            giaTri,
            fontSize = 16.sp,
            fontWeight = FontWeight.Bold,
            color = if (onClick != null) Color(0xFF1565C0) else Color.Black,
        )
    }
}

/** Chip thống kê bấm được: bấm vào số thì ra danh sách tương ứng. */
@Composable
fun ChipThongKe(nhan: String, so: Int, mau: Color, onClick: () -> Unit) {
    Card(
        onClick = onClick,
        colors = CardDefaults.cardColors(containerColor = mau.copy(alpha = 0.14f)),
        shape = RoundedCornerShape(14.dp),
        modifier = Modifier.padding(end = 8.dp, bottom = 8.dp),
    ) {
        Column(Modifier.padding(horizontal = 14.dp, vertical = 10.dp), horizontalAlignment = Alignment.CenterHorizontally) {
            Text("$so", fontSize = 22.sp, fontWeight = FontWeight.Bold, color = mau)
            Text(nhan, fontSize = 13.sp, color = Color.DarkGray)
        }
    }
}

/** Màu trạng thái bài giao cho giáo viên. */
enum class TrangThaiBaiGiao { CAN_KIEM_TRA, DANG_TIEN_TRINH, DA_XONG, QUA_HAN }

fun mauTrangThaiBai(trangThai: TrangThaiBaiGiao): Color = when (trangThai) {
    TrangThaiBaiGiao.CAN_KIEM_TRA -> Color(0xFFE65100)
    TrangThaiBaiGiao.DANG_TIEN_TRINH -> Color(0xFF1565C0)
    TrangThaiBaiGiao.DA_XONG -> Color(0xFF2E7D32)
    TrangThaiBaiGiao.QUA_HAN -> Color(0xFFD32F2F)
}

fun nhanTrangThaiBai(trangThai: TrangThaiBaiGiao): String = when (trangThai) {
    TrangThaiBaiGiao.CAN_KIEM_TRA -> "Cần kiểm tra"
    TrangThaiBaiGiao.DANG_TIEN_TRINH -> "Đang tiến trình"
    TrangThaiBaiGiao.DA_XONG -> "Đã xong"
    TrangThaiBaiGiao.QUA_HAN -> "Quá hạn"
}
