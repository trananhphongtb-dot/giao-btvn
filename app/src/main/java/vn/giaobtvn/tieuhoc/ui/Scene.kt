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
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.layout.imePadding
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.statusBarsPadding
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
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.compositeOver
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

/**
 * Khung cảnh dọc: nền gradient xanh nhạt + vài quả cầu bóng trang trí, nội
 * dung cuộn bên trên. Chừa chỗ cho thanh trạng thái, thanh điều hướng và
 * bàn phím (app vẽ tràn màn hình).
 */
@Composable
fun CanhDoc(noiDung: @Composable ColumnScope.() -> Unit) {
    Box(
        Modifier
            .fillMaxSize()
            .background(Brush.verticalGradient(listOf(Mau.NenTren, Mau.NenGiua, Mau.NenDuoi)))
    ) {
        QuaCauBong(Modifier.size(260.dp).offset((-90).dp, (-80).dp), Mau.XanhSang, 0.30f)
        QuaCauBong(Modifier.size(200.dp).align(Alignment.CenterEnd).offset(90.dp, (-40).dp), Mau.Vang, 0.22f)
        QuaCauBong(Modifier.size(240.dp).align(Alignment.BottomStart).offset((-100).dp, 90.dp), Mau.XanhSang, 0.22f)
        Column(
            Modifier
                .fillMaxSize()
                .statusBarsPadding()
                .navigationBarsPadding()
                .imePadding()
                .verticalScroll(rememberScrollState())
                .padding(horizontal = 18.dp, vertical = 14.dp),
            content = noiDung,
        )
    }
}

/** Quả cầu bóng mờ làm nền: gradient tỏa tròn, sáng lệch về góc trên trái. */
@Composable
fun QuaCauBong(modifier: Modifier, mau: Color, doDam: Float) {
    Box(
        modifier
            .clip(CircleShape)
            .background(
                Brush.radialGradient(
                    colors = listOf(Color.White.copy(alpha = doDam + 0.15f), mau.copy(alpha = doDam), mau.copy(alpha = 0.04f)),
                    center = androidx.compose.ui.geometry.Offset(150f, 130f),
                    radius = 520f,
                )
            )
    )
}

/**
 * Banner tiêu đề nổi khối ở đầu mỗi màn hình: gradient xanh, quả cầu bóng
 * ở góc, dải sáng phía trên, chữ trắng.
 */
@Composable
fun TieuDeCanh(tieuDe: String, phuDe: String = "") {
    val hinh = RoundedCornerShape(26.dp)
    Box(
        Modifier
            .fillMaxWidth()
            .shadow(14.dp, hinh, clip = false, ambientColor = Mau.XanhDam, spotColor = Mau.XanhDam)
            .clip(hinh)
            .background(
                Brush.linearGradient(
                    listOf(Mau.XanhDam, Mau.Xanh, Mau.XanhSang),
                    start = androidx.compose.ui.geometry.Offset(0f, 0f),
                    end = androidx.compose.ui.geometry.Offset(900f, 500f),
                )
            ),
    ) {
        // Lớp trang trí khớp đúng kích thước banner, không làm banner cao thêm.
        Box(Modifier.matchParentSize()) {
            QuaCauBong(Modifier.size(150.dp).align(Alignment.TopEnd).offset(40.dp, (-50).dp), Color.White, 0.30f)
            QuaCauBong(Modifier.size(90.dp).align(Alignment.BottomEnd).offset((-30).dp, 30.dp), Mau.Vang, 0.45f)
            Box(
                Modifier
                    .fillMaxWidth()
                    .height(44.dp)
                    .background(Brush.verticalGradient(listOf(Color.White.copy(alpha = 0.22f), Color.Transparent)))
            )
        }
        Column(Modifier.padding(horizontal = 22.dp, vertical = 20.dp)) {
            Text(tieuDe, fontSize = 26.sp, fontWeight = FontWeight.ExtraBold, color = Color.White)
            if (phuDe.isNotBlank()) {
                Spacer(Modifier.height(4.dp))
                Text(phuDe, fontSize = 15.sp, color = Color.White.copy(alpha = 0.88f))
            }
        }
    }
    Spacer(Modifier.height(18.dp))
}

/**
 * Một ô khung nổi khối: dùng cho danh sách học sinh, bài giao, kết quả...
 * Thẻ trắng bo tròn, bóng đổ mềm, tiêu đề có thanh nhấn màu bên trái.
 */
@Composable
fun Khung(tieuDe: String, phuDe: String = "", noiDung: @Composable ColumnScope.() -> Unit) {
    The3D(Modifier.fillMaxWidth().padding(vertical = 7.dp)) {
        Column(Modifier.padding(horizontal = 18.dp, vertical = 16.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Box(
                    Modifier
                        .width(6.dp)
                        .height(if (phuDe.isNotBlank()) 40.dp else 24.dp)
                        .clip(RoundedCornerShape(3.dp))
                        .background(Brush.verticalGradient(listOf(Mau.XanhSang, Mau.Vang)))
                )
                Spacer(Modifier.width(12.dp))
                Column {
                    Text(tieuDe, fontSize = 18.sp, fontWeight = FontWeight.ExtraBold, color = Mau.Chu)
                    if (phuDe.isNotBlank()) {
                        Text(phuDe, fontSize = 14.sp, color = Mau.ChuPhu)
                    }
                }
            }
            Spacer(Modifier.height(12.dp))
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
        Text(label, fontSize = 16.sp, color = Mau.ChuPhu, modifier = Modifier.weight(1f))
        Text(
            giaTri,
            fontSize = 16.sp,
            fontWeight = FontWeight.Bold,
            color = if (onClick != null) Mau.Xanh else Mau.Chu,
        )
    }
}

/** Chip thống kê bấm được: bấm vào số thì ra danh sách tương ứng. */
@Composable
fun ChipThongKe(nhan: String, so: Int, mau: Color, onClick: () -> Unit) {
    The3D(
        Modifier.padding(end = 8.dp, bottom = 10.dp),
        mauVien = mau.copy(alpha = 0.5f),
        mauBong = mau,
        nen = mau.copy(alpha = 0.10f).compositeOver(Color.White),
        bo = 16.dp,
        onClick = onClick,
    ) {
        Column(Modifier.padding(horizontal = 16.dp, vertical = 10.dp), horizontalAlignment = Alignment.CenterHorizontally) {
            Text("$so", fontSize = 24.sp, fontWeight = FontWeight.ExtraBold, color = mau)
            Text(nhan, fontSize = 13.sp, color = Mau.ChuPhu)
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
