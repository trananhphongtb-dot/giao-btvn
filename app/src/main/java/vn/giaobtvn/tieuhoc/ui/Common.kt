package vn.giaobtvn.tieuhoc.ui

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.net.Uri
import android.util.Base64
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import kotlinx.coroutines.delay
import vn.giaobtvn.tieuhoc.data.TrangThaiNop
import vn.giaobtvn.tieuhoc.data.dinhDangPhutGiay
import vn.giaobtvn.tieuhoc.data.nhanTrangThai

@Composable
fun TieuDeManHinh(tieuDe: String, phuDe: String = "") {
    Text(tieuDe, fontSize = 22.sp, fontWeight = FontWeight.Bold)
    if (phuDe.isNotBlank()) {
        Spacer(Modifier.height(4.dp))
        Text(phuDe, fontSize = 15.sp, color = Color.Gray)
    }
    Spacer(Modifier.height(16.dp))
}

@Composable
fun NutLon(text: String, bat: Boolean = true, onClick: () -> Unit) {
    Button(
        onClick = onClick,
        enabled = bat,
        modifier = Modifier.fillMaxWidth().height(52.dp),
    ) {
        Text(text, fontSize = 17.sp)
    }
}

@Composable
fun NutPhu(text: String, onClick: () -> Unit) {
    OutlinedButton(
        onClick = onClick,
        modifier = Modifier.fillMaxWidth().height(52.dp),
    ) {
        Text(text, fontSize = 16.sp)
    }
}

@Composable
fun TheThongTin(tieuDe: String, noiDung: String, onClick: (() -> Unit)? = null) {
    Card(
        onClick = onClick ?: {},
        enabled = onClick != null,
        colors = CardDefaults.cardColors(containerColor = Color.White),
        modifier = Modifier.fillMaxWidth().padding(vertical = 4.dp),
    ) {
        Column(Modifier.padding(16.dp)) {
            Text(tieuDe, fontSize = 17.sp, fontWeight = FontWeight.Bold)
            Spacer(Modifier.height(4.dp))
            Text(noiDung, fontSize = 15.sp, color = Color.DarkGray)
        }
    }
}

@Composable
fun ManDangTai() {
    Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        CircularProgressIndicator()
    }
}

@Composable
fun ThongBaoLoi(thongBao: String) {
    if (thongBao.isNotBlank()) {
        Spacer(Modifier.height(8.dp))
        Text(thongBao, color = MaterialTheme.colorScheme.error, fontSize = 15.sp)
    }
}

@Composable
fun ThongBaoTot(thongBao: String) {
    if (thongBao.isNotBlank()) {
        Spacer(Modifier.height(8.dp))
        Text(thongBao, color = Color(0xFF2E7D32), fontSize = 15.sp)
    }
}

@Composable
fun ChipTrangThai(trangThai: TrangThaiNop) {
    val mau = when (trangThai) {
        TrangThaiNop.DA_NOP -> Color(0xFF2E7D32)
        TrangThaiNop.CHUA_NOP -> Color.Gray
        TrangThaiNop.QUA_HAN -> Color(0xFFD32F2F)
        TrangThaiNop.CHO_DUYET_TRUNG -> Color(0xFFF57F17)
        TrangThaiNop.CAN_NOP_LAI -> Color(0xFFD32F2F)
    }
    Text(
        nhanTrangThai(trangThai),
        color = mau,
        fontWeight = FontWeight.Bold,
        fontSize = 14.sp,
    )
}

@Composable
fun HangChu(label: String, giaTri: String) {
    Row(Modifier.fillMaxWidth().padding(vertical = 2.dp), horizontalArrangement = Arrangement.SpaceBetween) {
        Text(label, fontSize = 15.sp, color = Color.DarkGray)
        Spacer(Modifier.width(8.dp))
        Text(giaTri, fontSize = 15.sp, fontWeight = FontWeight.Bold)
    }
}

/**
 * Đọc ảnh từ Uri (thư viện hoặc camera) rồi thu nhỏ về tối đa 1024px ở
 * cạnh dài nhất trước khi nén, để không tốn bộ nhớ với ảnh gốc quá lớn.
 */
fun giaiMaAnhTuUri(context: Context, uri: Uri, canhDaiToiDa: Int = 1024): Bitmap? {
    return try {
        val bounds = BitmapFactory.Options().apply { inJustDecodeBounds = true }
        context.contentResolver.openInputStream(uri)?.use {
            BitmapFactory.decodeStream(it, null, bounds)
        }
        var mau = 1
        while (bounds.outWidth / mau > canhDaiToiDa || bounds.outHeight / mau > canhDaiToiDa) {
            mau *= 2
        }
        val options = BitmapFactory.Options().apply { inSampleSize = mau }
        context.contentResolver.openInputStream(uri)?.use {
            BitmapFactory.decodeStream(it, null, options)
        }
    } catch (e: Exception) {
        null
    }
}

/** Giải mã chuỗi Base64 trong bài nộp thành Bitmap để cô xem ảnh bài làm. */
fun giaiMaBase64ThanhBitmap(base64: String): Bitmap? {
    return try {
        val bytes = Base64.decode(base64, Base64.DEFAULT)
        BitmapFactory.decodeByteArray(bytes, 0, bytes.size)
    } catch (e: Exception) {
        null
    }
}

/**
 * Đồng hồ đếm ngược cho bài trắc nghiệm. Hết giờ thì gọi onHetGio đúng
 * một lần, màn làm bài sẽ tự nộp bài lúc đó.
 */
@Composable
fun DongHoDemNguoc(thoiGianHetMillis: Long, onHetGio: () -> Unit) {
    var conLaiGiay by remember { mutableStateOf(0L) }
    var daBaoHet by remember { mutableStateOf(false) }
    LaunchedEffect(thoiGianHetMillis) {
        while (true) {
            val conLai = (thoiGianHetMillis - System.currentTimeMillis()) / 1000
            conLaiGiay = if (conLai < 0) 0 else conLai
            if (conLai <= 0 && !daBaoHet) {
                daBaoHet = true
                onHetGio()
                break
            }
            delay(1000)
        }
    }
    Text(
        "Còn lại: ${dinhDangPhutGiay(conLaiGiay)}",
        fontSize = 20.sp,
        fontWeight = FontWeight.Bold,
        color = if (conLaiGiay <= 60) Color(0xFFD32F2F) else Color(0xFF1565C0),
    )
}
