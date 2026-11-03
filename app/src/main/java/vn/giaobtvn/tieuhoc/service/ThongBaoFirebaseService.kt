package vn.giaobtvn.tieuhoc.service

import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.database.FirebaseDatabase
import com.google.firebase.messaging.FirebaseMessagingService
import com.google.firebase.messaging.RemoteMessage

// ============================================================================
// FCM — nhận thông báo đẩy, kể cả khi app đã đóng.
// Tin FCM gửi tới (từ Firebase Console hoặc Cloud Function gửi tới token
// đã lưu ở fcmTokens/) sẽ hiện thành thông báo hệ thống, bấm vào mở app.
// Token mới được lưu theo cả hocSinhId (học sinh) và uid (giáo viên),
// để phía gửi biết gửi cho đúng người.
// ============================================================================

class ThongBaoFirebaseService : FirebaseMessagingService() {
    override fun onMessageReceived(message: RemoteMessage) {
        val tieuDe = message.notification?.title
            ?: message.data["tieuDe"]
            ?: "Bài tập về nhà mới"
        val noiDung = message.notification?.body
            ?: message.data["noiDung"]
            ?: "Cô vừa giao bài mới, mở app để xem."
        hienThongBaoHeThong(
            this, tieuDe, noiDung,
            (message.messageId?.hashCode() ?: System.currentTimeMillis().toInt()),
        )
    }

    override fun onNewToken(token: String) {
        luuToken(token)
    }

    private fun luuToken(token: String) {
        try {
            val root = FirebaseDatabase.getInstance().reference
            val prefs = getSharedPreferences("giao_btvn", MODE_PRIVATE)
            val hocSinhId = prefs.getString("hoc_sinh_id", "") ?: ""
            if (hocSinhId.isNotBlank()) {
                root.child("fcmTokens").child(hocSinhId).setValue(token)
            }
            val uid = FirebaseAuth.getInstance().currentUser?.uid
            if (!uid.isNullOrBlank()) {
                root.child("fcmTokens").child(uid).setValue(token)
            }
        } catch (e: Exception) {
            // Lưu token thất bại thì lần mở app sau sẽ lưu lại, không crash.
        }
    }
}
