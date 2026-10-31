package vn.giaobtvn.tieuhoc.ui

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import vn.giaobtvn.tieuhoc.R
import vn.giaobtvn.tieuhoc.data.VaiTro

/**
 * Màn hình đầu tiên của app: chọn Giáo viên hoặc Học sinh.
 * Nền là ảnh lớp học (nen_chon_vai.png), tiêu đề ở vùng trời trống phía
 * trên ảnh, hai thẻ chọn vai ở vùng sáng phía dưới ảnh để chữ luôn đọc
 * được. V1 không có vai phụ huynh, không quảng cáo, không chat tự do.
 */
@Composable
fun RoleScreen(onChon: (VaiTro) -> Unit) {
    Box(Modifier.fillMaxSize()) {
        Image(
            painter = painterResource(R.drawable.nen_chon_vai),
            contentDescription = null,
            contentScale = ContentScale.Crop,
            modifier = Modifier.fillMaxSize(),
        )
        Column(
            Modifier.fillMaxSize().padding(horizontal = 24.dp),
        ) {
            Spacer(Modifier.height(48.dp))
            Text(
                "Giao Bài Tập\nVề Nhà",
                fontSize = 34.sp,
                fontWeight = FontWeight.ExtraBold,
                color = Color(0xFF0D47A1),
                textAlign = TextAlign.Center,
                lineHeight = 40.sp,
                modifier = Modifier.fillMaxWidth(),
            )
            Spacer(Modifier.height(8.dp))
            Text(
                "Học vui • Làm bài đều • Cô chấm nhanh",
                fontSize = 16.sp,
                color = Color(0xFF37474F),
                textAlign = TextAlign.Center,
                modifier = Modifier.fillMaxWidth(),
            )
            Spacer(Modifier.weight(1f))
            TheChonVai(
                bieuTuong = "👩‍🏫",
                mauNenBieuTuong = Color(0xFFE3F2FD),
                tieuDe = "Tôi là giáo viên",
                noiDung = "Đăng nhập Google, tạo lớp, giao bài, chấm bài và xem thống kê của lớp.",
                onClick = { onChon(VaiTro.GIAO_VIEN) },
            )
            Spacer(Modifier.height(14.dp))
            TheChonVai(
                bieuTuong = "🧒",
                mauNenBieuTuong = Color(0xFFE0F2F1),
                tieuDe = "Tôi là học sinh",
                noiDung = "Đăng nhập Google hoặc nhập mã lớp để làm bài cô giao và ôn bài tự do.",
                onClick = { onChon(VaiTro.HOC_SINH) },
            )
            Spacer(Modifier.height(20.dp))
            Text(
                "Dành cho giáo viên và học sinh",
                fontSize = 13.sp,
                color = Color(0xFF607D8B),
                textAlign = TextAlign.Center,
                modifier = Modifier.fillMaxWidth(),
            )
            Spacer(Modifier.height(24.dp))
        }
    }
}

@Composable
private fun TheChonVai(
    bieuTuong: String,
    mauNenBieuTuong: Color,
    tieuDe: String,
    noiDung: String,
    onClick: () -> Unit,
) {
    Card(
        onClick = onClick,
        shape = RoundedCornerShape(24.dp),
        colors = CardDefaults.cardColors(containerColor = Color.White.copy(alpha = 0.94f)),
        elevation = CardDefaults.cardElevation(defaultElevation = 8.dp),
        modifier = Modifier.fillMaxWidth(),
    ) {
        Row(
            Modifier.fillMaxWidth().padding(20.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            Box(
                Modifier.size(64.dp).clip(CircleShape),
                contentAlignment = Alignment.Center,
            ) {
                // Nền tròn màu nhạt phía sau biểu tượng, vẽ bằng Card nhỏ.
                Card(
                    shape = CircleShape,
                    colors = CardDefaults.cardColors(containerColor = mauNenBieuTuong),
                    modifier = Modifier.fillMaxSize(),
                ) {}
                Text(bieuTuong, fontSize = 34.sp)
            }
            Column(Modifier.weight(1f).padding(start = 16.dp)) {
                Text(tieuDe, fontSize = 19.sp, fontWeight = FontWeight.Bold, color = Color(0xFF102027))
                Spacer(Modifier.height(4.dp))
                Text(noiDung, fontSize = 15.sp, color = Color.DarkGray, lineHeight = 20.sp)
            }
            Text("›", fontSize = 28.sp, color = Color(0xFF90A4AE), modifier = Modifier.padding(start = 8.dp))
        }
    }
}
