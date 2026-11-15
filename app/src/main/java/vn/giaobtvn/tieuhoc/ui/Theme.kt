package vn.giaobtvn.tieuhoc.ui

import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Shapes
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp

/** Bảng màu dùng chung cho toàn app (giao diện mới 2026-11-16). */
object Mau {
    val Xanh = Color(0xFF2F5BEA)
    val XanhDam = Color(0xFF1F3FB8)
    val XanhSang = Color(0xFF6A93FF)
    val XanhNhat = Color(0xFFE4ECFF)
    val Vang = Color(0xFFFFB300)
    val VangDam = Color(0xFFD98E00)
    val Luc = Color(0xFF2EAD6A)
    val LucDam = Color(0xFF1B7F4B)
    val LucNhat = Color(0xFFDDF5E8)
    val Do = Color(0xFFE5484D)
    val DoDam = Color(0xFFB02A30)
    val DoNhat = Color(0xFFFFE3E4)
    val Cam = Color(0xFFF08A24)
    val Chu = Color(0xFF14213D)
    val ChuPhu = Color(0xFF5B6B8C)
    val VienNhat = Color(0xFFD5DEF2)
    val NenTren = Color(0xFFD6E4FF)
    val NenGiua = Color(0xFFEAF1FF)
    val NenDuoi = Color(0xFFFFFFFF)
}

/** Giao diện sáng, bo tròn nhiều, màu tươi, nút và thẻ nổi khối. */
@Composable
fun GiaoBtvnTheme(noiDung: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = lightColorScheme(
            primary = Mau.Xanh,
            onPrimary = Color.White,
            primaryContainer = Mau.XanhNhat,
            onPrimaryContainer = Mau.XanhDam,
            secondary = Mau.Luc,
            tertiary = Mau.Vang,
            error = Mau.Do,
            background = Mau.NenGiua,
            onBackground = Mau.Chu,
            surface = Color.White,
            onSurface = Mau.Chu,
            surfaceVariant = Mau.XanhNhat,
            onSurfaceVariant = Mau.ChuPhu,
            outline = Mau.VienNhat,
        ),
        shapes = Shapes(
            extraSmall = RoundedCornerShape(12.dp),
            small = RoundedCornerShape(14.dp),
            medium = RoundedCornerShape(18.dp),
            large = RoundedCornerShape(24.dp),
            extraLarge = RoundedCornerShape(28.dp),
        ),
        content = noiDung,
    )
}
