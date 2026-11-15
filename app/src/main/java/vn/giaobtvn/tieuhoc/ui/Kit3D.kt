package vn.giaobtvn.tieuhoc.ui

import androidx.compose.animation.core.animateDpAsState
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.interaction.collectIsPressedAsState
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.offset
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.draw.shadow
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

// ============================================================================
// BỘ THÀNH PHẦN NỔI KHỐI (3D GIẢ): mặt nút có dải sáng ở trên, mép đáy đậm
// hơn và đổ bóng; khi bấm mặt nút lún xuống mép đáy. Chỉ dùng gradient,
// bóng đổ và hình bo tròn của Compose, không dùng ảnh.
// ============================================================================

/** Nút nổi khối: mặt gradient + mép đáy + bóng, lún xuống khi bấm. */
@Composable
fun Nut3D(
    text: String,
    mauTren: Color,
    mauDuoi: Color,
    mauMep: Color,
    mauChu: Color,
    modifier: Modifier = Modifier,
    bat: Boolean = true,
    vien: Color? = null,
    cao: Dp = 54.dp,
    coChu: Int = 17,
    onClick: () -> Unit,
) {
    val nguon = remember { MutableInteractionSource() }
    val dangNhan by nguon.collectIsPressedAsState()
    val mep = 6.dp
    val lun by animateDpAsState(if (dangNhan && bat) mep else 0.dp, label = "lun")
    val hinh = RoundedCornerShape(18.dp)
    val tren = if (bat) mauTren else Color(0xFFD9DEE8)
    val duoi = if (bat) mauDuoi else Color(0xFFC7CEDB)
    val dayNut = if (bat) mauMep else Color(0xFFAEB7C8)
    val chu = if (bat) mauChu else Color(0xFF7B879E)
    Box(
        modifier
            .fillMaxWidth()
            .height(cao + mep)
            .clickable(interactionSource = nguon, indication = null, enabled = bat, onClick = onClick),
    ) {
        Box(
            Modifier
                .fillMaxWidth()
                .height(cao)
                .align(Alignment.BottomCenter)
                .shadow(if (bat) 8.dp else 0.dp, hinh, clip = false, ambientColor = dayNut, spotColor = dayNut)
                .clip(hinh)
                .background(dayNut),
        )
        Box(
            Modifier
                .fillMaxWidth()
                .height(cao)
                .offset(y = lun)
                .clip(hinh)
                .background(Brush.verticalGradient(listOf(tren, duoi)))
                .then(if (vien != null) Modifier.border(BorderStroke(2.dp, vien), hinh) else Modifier),
            contentAlignment = Alignment.Center,
        ) {
            // Dải sáng bóng ở nửa trên mặt nút.
            Box(
                Modifier
                    .fillMaxWidth()
                    .height(cao / 2)
                    .align(Alignment.TopCenter)
                    .background(Brush.verticalGradient(listOf(Color.White.copy(alpha = 0.32f), Color.Transparent))),
            )
            Text(
                text,
                fontSize = coChu.sp,
                fontWeight = FontWeight.Bold,
                color = chu,
                textAlign = TextAlign.Center,
                maxLines = 2,
                modifier = Modifier.padding(horizontal = 12.dp),
            )
        }
    }
}

/** Thẻ nổi khối: nền trắng, bóng đổ mềm màu xanh, viền sáng phía trên. */
@Composable
fun The3D(
    modifier: Modifier = Modifier,
    mauVien: Color = Mau.VienNhat,
    mauBong: Color = Mau.XanhDam,
    nen: Color = Color.White,
    bo: Dp = 24.dp,
    onClick: (() -> Unit)? = null,
    noiDung: @Composable () -> Unit,
) {
    val hinh = RoundedCornerShape(bo)
    Box(
        modifier
            .shadow(10.dp, hinh, clip = false, ambientColor = mauBong.copy(alpha = 0.35f), spotColor = mauBong.copy(alpha = 0.45f))
            .clip(hinh)
            .background(nen)
            .border(1.5.dp, Brush.verticalGradient(listOf(Color.White, mauVien)), hinh)
            .then(if (onClick != null) Modifier.clickable { onClick() } else Modifier),
    ) {
        noiDung()
    }
}

/** Huy hiệu tròn bóng (chữ cái đáp án, biểu tượng): gradient + viền sáng. */
@Composable
fun HuyHieuTron(
    chu: String,
    mauTren: Color,
    mauDuoi: Color,
    kichThuoc: Dp = 40.dp,
    coChu: Int = 18,
    mauChu: Color = Color.White,
) {
    Box(
        Modifier
            .size(kichThuoc)
            .shadow(4.dp, CircleShape, clip = false, ambientColor = mauDuoi, spotColor = mauDuoi)
            .clip(CircleShape)
            .background(Brush.verticalGradient(listOf(mauTren, mauDuoi))),
        contentAlignment = Alignment.Center,
    ) {
        Box(
            Modifier
                .fillMaxWidth()
                .height(kichThuoc / 2)
                .align(Alignment.TopCenter)
                .background(Brush.verticalGradient(listOf(Color.White.copy(alpha = 0.35f), Color.Transparent))),
        )
        Text(chu, fontSize = coChu.sp, fontWeight = FontWeight.ExtraBold, color = mauChu)
    }
}

/** Kết quả hiển thị của một đáp án khi đã kiểm tra. */
enum class KetQuaDapAn { CHUA_KIEM_TRA, DUNG, SAI }

/** Thẻ đáp án to, dễ bấm cho học sinh: chữ cái A/B/C/D + nội dung. */
@Composable
fun TheDapAn(
    chuCai: String,
    noiDung: String,
    daChon: Boolean,
    ketQua: KetQuaDapAn = KetQuaDapAn.CHUA_KIEM_TRA,
    bat: Boolean = true,
    onClick: () -> Unit,
) {
    val nen: Color
    val vien: Color
    val mauTren: Color
    val mauDuoi: Color
    when {
        ketQua == KetQuaDapAn.DUNG -> { nen = Mau.LucNhat; vien = Mau.Luc; mauTren = Mau.Luc; mauDuoi = Mau.LucDam }
        ketQua == KetQuaDapAn.SAI -> { nen = Mau.DoNhat; vien = Mau.Do; mauTren = Mau.Do; mauDuoi = Mau.DoDam }
        daChon -> { nen = Mau.XanhNhat; vien = Mau.Xanh; mauTren = Mau.XanhSang; mauDuoi = Mau.XanhDam }
        else -> { nen = Color.White; vien = Mau.VienNhat; mauTren = Color(0xFF9DB0D6); mauDuoi = Color(0xFF6F84B0) }
    }
    val hinh = RoundedCornerShape(18.dp)
    Box(
        Modifier
            .fillMaxWidth()
            .padding(vertical = 5.dp)
            .shadow(if (daChon) 8.dp else 4.dp, hinh, clip = false, ambientColor = vien, spotColor = vien)
            .clip(hinh)
            .background(nen)
            .border(if (daChon || ketQua != KetQuaDapAn.CHUA_KIEM_TRA) 2.5.dp else 1.5.dp, vien, hinh)
            .clickable(enabled = bat, onClick = onClick),
    ) {
        Row(
            Modifier.fillMaxWidth().padding(horizontal = 14.dp, vertical = 12.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            HuyHieuTron(chuCai, mauTren, mauDuoi, kichThuoc = 38.dp, coChu = 17)
            Spacer(Modifier.width(14.dp))
            Text(
                noiDung,
                fontSize = 18.sp,
                fontWeight = if (daChon || ketQua == KetQuaDapAn.DUNG) FontWeight.Bold else FontWeight.Medium,
                color = Mau.Chu,
                modifier = Modifier.weight(1f),
            )
            if (ketQua == KetQuaDapAn.DUNG) Text("✓", fontSize = 22.sp, fontWeight = FontWeight.ExtraBold, color = Mau.LucDam)
            if (ketQua == KetQuaDapAn.SAI) Text("✗", fontSize = 22.sp, fontWeight = FontWeight.ExtraBold, color = Mau.DoDam)
        }
    }
}

/** Thanh tiến độ bo tròn có gradient. tiLe từ 0.0 đến 1.0. */
@Composable
fun ThanhTienDo(tiLe: Float, modifier: Modifier = Modifier) {
    val t = tiLe.coerceIn(0f, 1f)
    Box(
        modifier
            .fillMaxWidth()
            .height(12.dp)
            .clip(RoundedCornerShape(6.dp))
            .background(Color.White.copy(alpha = 0.7f))
            .border(1.dp, Mau.VienNhat, RoundedCornerShape(6.dp)),
    ) {
        if (t > 0f) {
            Box(
                Modifier
                    .fillMaxWidth(t)
                    .height(12.dp)
                    .clip(RoundedCornerShape(6.dp))
                    .background(Brush.horizontalGradient(listOf(Mau.XanhSang, Mau.Xanh))),
            )
        }
    }
}

/** Viên thuốc nhỏ (nhãn trạng thái, điểm): nền nhạt cùng tông, chữ đậm. */
@Composable
fun VienThuoc(text: String, mau: Color, modifier: Modifier = Modifier) {
    Box(
        modifier
            .clip(RoundedCornerShape(50))
            .background(mau.copy(alpha = 0.14f))
            .padding(horizontal = 12.dp, vertical = 5.dp),
    ) {
        Text(text, fontSize = 13.sp, fontWeight = FontWeight.Bold, color = mau)
    }
}

/** Nút chọn dạng viên thuốc, dùng cho bộ lọc: chọn rồi thì nổi màu xanh. */
@Composable
fun ChipChon(text: String, daChon: Boolean, onClick: () -> Unit) {
    val hinh = RoundedCornerShape(50)
    Box(
        Modifier
            .padding(end = 8.dp, bottom = 8.dp)
            .shadow(if (daChon) 6.dp else 2.dp, hinh, clip = false, ambientColor = Mau.XanhDam, spotColor = Mau.XanhDam)
            .clip(hinh)
            .background(if (daChon) Brush.verticalGradient(listOf(Mau.XanhSang, Mau.Xanh)) else Brush.verticalGradient(listOf(Color.White, Color.White)))
            .border(1.5.dp, if (daChon) Mau.XanhDam else Mau.VienNhat, hinh)
            .clickable(onClick = onClick)
            .padding(horizontal = 16.dp, vertical = 9.dp),
    ) {
        Text(
            text,
            fontSize = 15.sp,
            fontWeight = if (daChon) FontWeight.Bold else FontWeight.Medium,
            color = if (daChon) Color.White else Mau.Chu,
        )
    }
}

/** Một nhóm lựa chọn (Môn, Chương, Bài, Số câu): tiêu đề + các chip xuống dòng. */
@OptIn(ExperimentalLayoutApi::class)
@Composable
fun NhomChon(tieuDe: String, cacLuaChon: List<String>, daChon: String, onChon: (String) -> Unit) {
    Column(Modifier.fillMaxWidth().padding(vertical = 4.dp)) {
        Text(tieuDe, fontSize = 15.sp, fontWeight = FontWeight.Bold, color = Mau.ChuPhu)
        Spacer(Modifier.height(6.dp))
        FlowRow(horizontalArrangement = Arrangement.Start) {
            cacLuaChon.forEach { ten -> ChipChon(ten, ten == daChon) { onChon(ten) } }
        }
    }
}

/** Nút nhỏ nổi khối cho hàng nút (không giãn hết chiều ngang). */
@Composable
fun NutNho(text: String, chinh: Boolean = false, onClick: () -> Unit) {
    val nguon = remember { MutableInteractionSource() }
    val dangNhan by nguon.collectIsPressedAsState()
    val mep = 4.dp
    val lun by animateDpAsState(if (dangNhan) mep else 0.dp, label = "lunNho")
    val hinh = RoundedCornerShape(14.dp)
    val tren = if (chinh) Mau.XanhSang else Color.White
    val duoi = if (chinh) Mau.Xanh else Color(0xFFEFF3FC)
    val day = if (chinh) Mau.XanhDam else Color(0xFFB9C6E4)
    val chu = if (chinh) Color.White else Mau.XanhDam
    Box(
        Modifier
            .padding(end = 8.dp, bottom = 4.dp)
            .clickable(interactionSource = nguon, indication = null, onClick = onClick),
    ) {
        Box(Modifier.matchParentSize().padding(top = mep).clip(hinh).background(day))
        Box(
            Modifier
                .padding(bottom = mep)
                .offset(y = lun)
                .height(38.dp)
                .clip(hinh)
                .background(Brush.verticalGradient(listOf(tren, duoi)))
                .then(if (chinh) Modifier else Modifier.border(1.5.dp, Mau.VienNhat, hinh))
                .padding(horizontal = 14.dp),
            contentAlignment = Alignment.Center,
        ) {
            Text(text, fontSize = 14.sp, fontWeight = FontWeight.Bold, color = chu, maxLines = 1)
        }
    }
}
