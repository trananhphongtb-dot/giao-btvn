package vn.giaobtvn.tieuhoc.ui

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import vn.giaobtvn.tieuhoc.data.VaiTro

/**
 * Màn hình đầu tiên của app: chỉ chọn Giáo viên hoặc Học sinh.
 * V1 không có vai phụ huynh, không quảng cáo, không chat tự do.
 */
@Composable
fun RoleScreen(onChon: (VaiTro) -> Unit) {
    Column(
        Modifier.fillMaxSize().verticalScroll(rememberScrollState()).padding(24.dp),
    ) {
        Spacer(Modifier.height(32.dp))
        Text(
            "Giao Bài Tập Về Nhà",
            fontSize = 28.sp,
            textAlign = TextAlign.Center,
            modifier = Modifier.fillMaxWidth(),
        )
        Spacer(Modifier.height(8.dp))
        Text(
            "Bạn là ai?",
            fontSize = 18.sp,
            textAlign = TextAlign.Center,
            modifier = Modifier.fillMaxWidth(),
        )
        Spacer(Modifier.height(32.dp))
        TheThongTin(
            tieuDe = "Tôi là giáo viên",
            noiDung = "Đăng nhập Google, tạo lớp, giao bài, chấm bài và xem thống kê của lớp.",
            onClick = { onChon(VaiTro.GIAO_VIEN) },
        )
        Spacer(Modifier.height(12.dp))
        TheThongTin(
            tieuDe = "Tôi là học sinh",
            noiDung = "Nhập mã lớp để tham gia lớp, làm bài cô giao và ôn bài tự do.",
            onClick = { onChon(VaiTro.HOC_SINH) },
        )
    }
}
