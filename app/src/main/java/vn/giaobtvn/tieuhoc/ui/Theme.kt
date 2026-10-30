package vn.giaobtvn.tieuhoc.ui

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val XanhChinh = Color(0xFF1565C0)
private val XanhLa = Color(0xFF00897B)
private val DoCanhBao = Color(0xFFD32F2F)
private val VangChoDuyet = Color(0xFFF9A825)
private val Nen = Color(0xFFF5F7FA)

/** Giao diện sáng, đơn giản, chữ lớn vừa đủ cho học sinh tiểu học. */
@Composable
fun GiaoBtvnTheme(noiDung: @Composable () -> Unit) {
    MaterialTheme(
        colorScheme = lightColorScheme(
            primary = XanhChinh,
            secondary = XanhLa,
            error = DoCanhBao,
            background = Nen,
            surface = Color.White,
        ),
        content = noiDung,
    )
}
