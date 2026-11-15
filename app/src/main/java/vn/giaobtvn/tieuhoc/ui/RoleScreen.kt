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
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.statusBarsPadding
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
            Modifier.fillMaxSize().statusBarsPadding().navigationBarsPadding().padding(horizontal = 24.dp),
        ) {
            Spacer(Modifier.height(36.dp))
            Text(
                "Bài tập về nhà",
                fontSize = 34.sp,
                fontWeight = FontWeight.ExtraBold,
                color = Mau.XanhDam,
                textAlign = TextAlign.Center,
                maxLines = 1,
                style = androidx.compose.ui.text.TextStyle(
                    shadow = androidx.compose.ui.graphics.Shadow(
                        color = Color.White,
                        offset = androidx.compose.ui.geometry.Offset(0f, 4f),
                        blurRadius = 10f,
                    ),
                ),
                modifier = Modifier.fillMaxWidth(),
            )
            Spacer(Modifier.height(6.dp))
            Text(
                "Giao bài · Làm bài · Nhận điểm",
                fontSize = 16.sp,
                fontWeight = FontWeight.Medium,
                color = Mau.ChuPhu,
                textAlign = TextAlign.Center,
                modifier = Modifier.fillMaxWidth(),
            )
            Spacer(Modifier.weight(1f))
            TheChonVai(
                bieuTuong = "👩‍🏫",
                mauTren = Mau.XanhSang,
                mauDuoi = Mau.XanhDam,
                tieuDe = "Tôi là giáo viên",
                phuDe = "Tạo lớp, giao bài, chấm điểm",
                onClick = { onChon(VaiTro.GIAO_VIEN) },
            )
            Spacer(Modifier.height(18.dp))
            TheChonVai(
                bieuTuong = "🧒",
                mauTren = Color(0xFF4CD08B),
                mauDuoi = Mau.LucDam,
                tieuDe = "Tôi là học sinh",
                phuDe = "Làm bài cô giao, ôn bài tự do",
                onClick = { onChon(VaiTro.HOC_SINH) },
            )
            Spacer(Modifier.height(36.dp))
        }
    }
}

@Composable
private fun TheChonVai(
    bieuTuong: String,
    mauTren: Color,
    mauDuoi: Color,
    tieuDe: String,
    phuDe: String,
    onClick: () -> Unit,
) {
    The3D(
        Modifier.fillMaxWidth(),
        mauVien = Color.White,
        mauBong = mauDuoi,
        nen = Color.White.copy(alpha = 0.93f),
        bo = 28.dp,
        onClick = onClick,
    ) {
        Row(
            Modifier.fillMaxWidth().padding(horizontal = 20.dp, vertical = 18.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            HuyHieuTron(bieuTuong, mauTren, mauDuoi, kichThuoc = 62.dp, coChu = 32)
            Column(Modifier.weight(1f).padding(start = 16.dp)) {
                Text(tieuDe, fontSize = 21.sp, fontWeight = FontWeight.ExtraBold, color = Mau.Chu)
                Text(phuDe, fontSize = 14.sp, color = Mau.ChuPhu)
            }
            Text("›", fontSize = 34.sp, fontWeight = FontWeight.Bold, color = mauDuoi)
        }
    }
}
