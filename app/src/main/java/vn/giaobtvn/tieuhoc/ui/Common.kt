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
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.draw.clip
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
    Text(tieuDe, fontSize = 22.sp, fontWeight = FontWeight.ExtraBold, color = Mau.Chu)
    if (phuDe.isNotBlank()) {
        Spacer(Modifier.height(4.dp))
        Text(phuDe, fontSize = 15.sp, color = Mau.ChuPhu)
    }
    Spacer(Modifier.height(16.dp))
}

@Composable
fun NutLon(text: String, bat: Boolean = true, onClick: () -> Unit) {
    Nut3D(
        text = text,
        mauTren = Mau.XanhSang,
        mauDuoi = Mau.Xanh,
        mauMep = Mau.XanhDam,
        mauChu = Color.White,
        modifier = Modifier.padding(vertical = 3.dp),
        bat = bat,
        onClick = onClick,
    )
}

@Composable
fun NutPhu(text: String, onClick: () -> Unit) {
    Nut3D(
        text = text,
        mauTren = Color.White,
        mauDuoi = Color(0xFFEFF3FC),
        mauMep = Color(0xFFB9C6E4),
        mauChu = Mau.XanhDam,
        modifier = Modifier.padding(vertical = 3.dp),
        vien = Mau.VienNhat,
        cao = 50.dp,
        coChu = 16,
        onClick = onClick,
    )
}

@Composable
fun TheThongTin(tieuDe: String, noiDung: String, onClick: (() -> Unit)? = null) {
    The3D(Modifier.fillMaxWidth().padding(vertical = 6.dp), onClick = onClick) {
        Column(Modifier.padding(horizontal = 18.dp, vertical = 14.dp)) {
            Text(tieuDe, fontSize = 17.sp, fontWeight = FontWeight.ExtraBold, color = Mau.Chu)
            Spacer(Modifier.height(4.dp))
            Text(noiDung, fontSize = 15.sp, color = Mau.ChuPhu)
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
        Spacer(Modifier.height(10.dp))
        Box(
            Modifier
                .fillMaxWidth()
                .clip(androidx.compose.foundation.shape.RoundedCornerShape(14.dp))
                .background(Mau.DoNhat)
                .padding(horizontal = 14.dp, vertical = 10.dp),
        ) {
            Text(thongBao, color = Mau.DoDam, fontSize = 15.sp, fontWeight = FontWeight.Medium)
        }
    }
}

@Composable
fun ThongBaoTot(thongBao: String) {
    if (thongBao.isNotBlank()) {
        Spacer(Modifier.height(10.dp))
        Box(
            Modifier
                .fillMaxWidth()
                .clip(androidx.compose.foundation.shape.RoundedCornerShape(14.dp))
                .background(Mau.LucNhat)
                .padding(horizontal = 14.dp, vertical = 10.dp),
        ) {
            Text(thongBao, color = Mau.LucDam, fontSize = 15.sp, fontWeight = FontWeight.Medium)
        }
    }
}

@Composable
fun ChipTrangThai(trangThai: TrangThaiNop) {
    val mau = when (trangThai) {
        TrangThaiNop.DA_NOP -> Mau.LucDam
        TrangThaiNop.CHUA_NOP -> Mau.ChuPhu
        TrangThaiNop.QUA_HAN -> Mau.DoDam
        TrangThaiNop.CHO_DUYET_TRUNG -> Mau.VangDam
        TrangThaiNop.CAN_NOP_LAI -> Mau.DoDam
    }
    VienThuoc(nhanTrangThai(trangThai), mau)
}

@Composable
fun HangChu(label: String, giaTri: String) {
    Row(Modifier.fillMaxWidth().padding(vertical = 2.dp), horizontalArrangement = Arrangement.SpaceBetween) {
        Text(label, fontSize = 15.sp, color = Mau.ChuPhu)
        Spacer(Modifier.width(8.dp))
        Text(giaTri, fontSize = 15.sp, fontWeight = FontWeight.Bold, color = Mau.Chu)
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
    val gapRut = conLaiGiay <= 60
    Box(
        Modifier
            .clip(androidx.compose.foundation.shape.RoundedCornerShape(50))
            .background(
                Brush.verticalGradient(
                    if (gapRut) listOf(Mau.Do, Mau.DoDam) else listOf(Mau.XanhSang, Mau.XanhDam)
                )
            )
            .padding(horizontal = 18.dp, vertical = 8.dp),
    ) {
        Text(
            "⏱ ${dinhDangPhutGiay(conLaiGiay)}",
            fontSize = 20.sp,
            fontWeight = FontWeight.ExtraBold,
            color = Color.White,
        )
    }
}
