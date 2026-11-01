package vn.giaobtvn.tieuhoc.ui

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
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
import androidx.compose.ui.graphics.Brush
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
 * Màn hình đầu tiên của app: chỉ chọn Giáo viên hoặc Học sinh.
 * Ảnh nền phủ kín toàn màn hình, dạng dọc (nen_chon_vai.png, ảnh dọc),
 * tiêu đề chỉ 1 hàng "Bài tập về nhà", nút chỉ ghi tên vai, không mô tả
 * chi tiết. V1 không có vai phụ huynh, không quảng cáo, không chat tự do.
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
        // Lớp phủ nhạt dần về phía dưới để nút luôn đọc được mà vẫn
        // thấy ảnh nền phủ kín phía sau.
        Box(
            Modifier.fillMaxSize().background(
                Brush.verticalGradient(
                    0.55f to Color.Transparent,
                    1.0f to Color.White.copy(alpha = 0.35f),
                ),
            ),
        )
        Column(
            Modifier.fillMaxSize().padding(horizontal = 24.dp),
        ) {
            Spacer(Modifier.height(48.dp))
            Text(
                "Bài tập về nhà",
                fontSize = 30.sp,
                fontWeight = FontWeight.ExtraBold,
                color = Color(0xFF0D47A1),
                textAlign = TextAlign.Center,
                maxLines = 1,
                modifier = Modifier.fillMaxWidth(),
            )
            Spacer(Modifier.weight(1f))
            TheChonVai(
                bieuTuong = "👩‍🏫",
                mauNenBieuTuong = Color(0xFFE3F2FD),
                tieuDe = "Tôi là giáo viên",
                onClick = { onChon(VaiTro.GIAO_VIEN) },
            )
            Spacer(Modifier.height(14.dp))
            TheChonVai(
                bieuTuong = "🧒",
                mauNenBieuTuong = Color(0xFFE0F2F1),
                tieuDe = "Tôi là học sinh",
                onClick = { onChon(VaiTro.HOC_SINH) },
            )
            Spacer(Modifier.height(32.dp))
        }
    }
}

@Composable
private fun TheChonVai(
    bieuTuong: String,
    mauNenBieuTuong: Color,
    tieuDe: String,
    onClick: () -> Unit,
) {
    Card(
        onClick = onClick,
        shape = RoundedCornerShape(24.dp),
        colors = CardDefaults.cardColors(containerColor = Color.White.copy(alpha = 0.94f)),
        elevation = CardDefaults.cardElevation(defaultElevation = 8.dp),
        modifier = Modifier.fillMaxWidth().height(76.dp),
    ) {
        Row(
            Modifier.fillMaxSize().padding(horizontal = 20.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            Box(
                Modifier.size(52.dp).clip(CircleShape),
                contentAlignment = Alignment.Center,
            ) {
                Card(
                    shape = CircleShape,
                    colors = CardDefaults.cardColors(containerColor = mauNenBieuTuong),
                    modifier = Modifier.fillMaxSize(),
                ) {}
                Text(bieuTuong, fontSize = 30.sp)
            }
            Text(
                tieuDe,
                fontSize = 20.sp,
                fontWeight = FontWeight.Bold,
                color = Color(0xFF102027),
                modifier = Modifier.weight(1f).padding(start = 16.dp),
            )
            Text("›", fontSize = 28.sp, color = Color(0xFF90A4AE))
        }
    }
}
