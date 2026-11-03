package vn.giaobtvn.tieuhoc.service

import android.Manifest
import android.content.Context
import android.content.pm.PackageManager
import android.os.Build
import androidx.core.content.ContextCompat
import androidx.work.CoroutineWorker
import androidx.work.WorkerParameters
import com.google.firebase.database.FirebaseDatabase
import kotlinx.coroutines.tasks.await

// ============================================================================
// Kiểm tra hộp thư định kỳ khi app đã đóng.
// WorkManager chạy tối đa khoảng 15 phút một lần (giới hạn của Android),
// nên thông báo khi đóng app có thể tới chậm hơn FCM tức thì, nhưng vẫn
// tới mà không cần máy chủ gửi riêng. Đây là cầu nối cho tới khi có
// Cloud Function gửi FCM tự động từ hộp thư.
// ============================================================================

class ThongBaoWorker(appContext: Context, params: WorkerParameters) : CoroutineWorker(appContext, params) {
    override suspend fun doWork(): Result {
        try {
            if (Build.VERSION.SDK_INT >= 33 &&
                ContextCompat.checkSelfPermission(applicationContext, Manifest.permission.POST_NOTIFICATIONS) != PackageManager.PERMISSION_GRANTED
            ) {
                return Result.success()
            }
            val prefs = applicationContext.getSharedPreferences("giao_btvn", Context.MODE_PRIVATE)
            val hocSinhId = prefs.getString("hoc_sinh_id", "") ?: ""
            if (hocSinhId.isBlank()) return Result.success()
            val snap = FirebaseDatabase.getInstance().reference
                .child("thongBao").child(hocSinhId).get().await()
            var dem = 0
            snap.children.forEach { child ->
                val daDoc = child.child("daDoc").getValue(Boolean::class.java) ?: false
                if (!daDoc) {
                    val tieuDe = child.child("tieuDe").getValue(String::class.java) ?: "Bài tập về nhà mới"
                    val noiDung = child.child("noiDung").getValue(String::class.java) ?: "Mở app để xem bài cô giao."
                    hienThongBaoHeThong(
                        applicationContext, tieuDe, noiDung,
                        (child.key?.hashCode() ?: dem),
                    )
                    dem++
                }
            }
            return Result.success()
        } catch (e: Exception) {
            return Result.success()
        }
    }
}
