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
            // Quy tắc Database chỉ cho đọc hộp thư khi đúng uid ẩn danh của em này.
            if (com.google.firebase.auth.FirebaseAuth.getInstance().currentUser?.uid != hocSinhId) {
                return Result.success()
            }
            // Mỗi thông báo chỉ hiện 1 lần, nhớ id những thông báo đã hiện.
            val daBao = prefs.getStringSet("da_bao_thong_bao", emptySet())?.toMutableSet() ?: mutableSetOf()
            val snap = FirebaseDatabase.getInstance().reference
                .child("thongBao").child(hocSinhId).get().await()
            var dem = 0
            snap.children.forEach { child ->
                val daDoc = child.child("daDoc").getValue(Boolean::class.java) ?: false
                val key = child.key ?: ""
                if (!daDoc && key.isNotBlank() && key !in daBao) {
                    daBao.add(key)
                    val tieuDe = child.child("tieuDe").getValue(String::class.java) ?: "Bài tập về nhà mới"
                    val noiDung = child.child("noiDung").getValue(String::class.java) ?: "Mở app để xem bài cô giao."
                    hienThongBaoHeThong(
                        applicationContext, tieuDe, noiDung,
                        (child.key?.hashCode() ?: dem),
                    )
                    dem++
                }
            }
            // Giữ tối đa 200 id gần nhất để không phình dữ liệu.
            prefs.edit().putStringSet("da_bao_thong_bao", daBao.toList().takeLast(200).toSet()).apply()
            return Result.success()
        } catch (e: Exception) {
            return Result.success()
        }
    }
}
