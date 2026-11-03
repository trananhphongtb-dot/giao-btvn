package vn.giaobtvn.tieuhoc.service

import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.os.Build
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat
import vn.giaobtvn.tieuhoc.MainActivity

// Kênh thông báo hệ thống cho bài mới / nhắc làm bài.
private const val KENH_ID = "btvn_thong_bao"
private const val KENH_TEN = "Bài tập về nhà"

/** Hiện một thông báo hệ thống, bấm vào thì mở app. */
fun hienThongBaoHeThong(context: Context, tieuDe: String, noiDung: String, idThongBao: Int) {
    try {
        val quanLy = context.getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val kenh = NotificationChannel(KENH_ID, KENH_TEN, NotificationManager.IMPORTANCE_DEFAULT)
            quanLy.createNotificationChannel(kenh)
        }
        val intent = Intent(context, MainActivity::class.java).apply {
            flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
        }
        val pending = PendingIntent.getActivity(
            context, 0, intent,
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE,
        )
        val thongBao = NotificationCompat.Builder(context, KENH_ID)
            .setSmallIcon(android.R.drawable.ic_dialog_info)
            .setContentTitle(tieuDe)
            .setContentText(noiDung)
            .setStyle(NotificationCompat.BigTextStyle().bigText(noiDung))
            .setContentIntent(pending)
            .setAutoCancel(true)
            .build()
        NotificationManagerCompat.from(context).notify(idThongBao, thongBao)
    } catch (e: Exception) {
        // Chưa cấp quyền thông báo (Android 13+) thì không crash app.
    }
}
