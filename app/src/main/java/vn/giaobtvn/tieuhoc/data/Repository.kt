package vn.giaobtvn.tieuhoc.data

import android.app.Activity
import android.content.Context
import androidx.credentials.CredentialManager
import androidx.credentials.CustomCredential
import androidx.credentials.GetCredentialRequest
import androidx.credentials.exceptions.GetCredentialCancellationException
import androidx.credentials.exceptions.NoCredentialException
import com.google.android.libraries.identity.googleid.GetGoogleIdOption
import com.google.android.libraries.identity.googleid.GoogleIdTokenCredential
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.GoogleAuthProvider
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.FirebaseDatabase
import java.util.UUID
import vn.giaobtvn.tieuhoc.R
import kotlinx.coroutines.CancellationException
import kotlinx.coroutines.tasks.await

// ============================================================================
// BỘ NHỚ CỤC BỘ — học sinh không cần tài khoản Google.
// ============================================================================

/**
 * Học sinh không đăng nhập Google: mỗi máy tự sinh một hocSinhId và lưu
 * trong SharedPreferences, kèm tên và mã lớp đã tham gia. Hạn chế V1:
 * học sinh đổi máy khác sẽ có id khác, cô sẽ thấy như một học sinh mới.
 */
class LocalPrefs(context: Context) {
    private val sp = context.getSharedPreferences("giao_btvn", Context.MODE_PRIVATE)

    var vaiTro: String
        get() = sp.getString("vai_tro", "") ?: ""
        set(value) { sp.edit().putString("vai_tro", value).apply() }

    var hocSinhId: String
        get() {
            val cu = sp.getString("hoc_sinh_id", "") ?: ""
            if (cu.isNotBlank()) return cu
            val moi = UUID.randomUUID().toString()
            sp.edit().putString("hoc_sinh_id", moi).apply()
            return moi
        }
        set(value) { sp.edit().putString("hoc_sinh_id", value).apply() }

    var tenHocSinh: String
        get() = sp.getString("ten_hoc_sinh", "") ?: ""
        set(value) { sp.edit().putString("ten_hoc_sinh", value).apply() }

    var maLop: String
        get() = sp.getString("ma_lop", "") ?: ""
        set(value) { sp.edit().putString("ma_lop", value).apply() }

    fun roiLop() {
        sp.edit().remove("ma_lop").apply()
    }
}

// ============================================================================
// ĐĂNG NHẬP GOOGLE CHO GIÁO VIÊN — theo mẫu quoc-te-app (Credential Manager).
// ============================================================================

data class GiaoVienDaDangNhap(val uid: String, val ten: String, val email: String)

/**
 * Đăng nhập Google cho giáo viên. Trả về Result: thành công thì có uid,
 * thất bại thì có thông báo tiếng Việt để hiển thị, không ném exception
 * ra màn hình. Chuỗi default_web_client_id do plugin google-services sinh
 * từ google-services.json, nên chưa có file đó thì chưa build được.
 */
object DangNhapGoogle {
    suspend fun dangNhap(activity: Activity): Result<GiaoVienDaDangNhap> {
        return try {
            val option = GetGoogleIdOption.Builder()
                .setFilterByAuthorizedAccounts(false)
                .setServerClientId(activity.getString(R.string.default_web_client_id))
                .build()
            val request = GetCredentialRequest.Builder().addCredentialOption(option).build()
            val result = CredentialManager.create(activity).getCredential(activity, request)
            val cred = result.credential
            if (cred is CustomCredential && cred.type == GoogleIdTokenCredential.TYPE_GOOGLE_ID_TOKEN_CREDENTIAL) {
                val g = GoogleIdTokenCredential.createFrom(cred.data)
                val res = FirebaseAuth.getInstance()
                    .signInWithCredential(GoogleAuthProvider.getCredential(g.idToken, null))
                    .await()
                val user = res.user ?: return Result.failure(Exception("Đăng nhập không thành công"))
                Result.success(
                    GiaoVienDaDangNhap(
                        uid = user.uid,
                        ten = g.displayName?.takeIf { it.isNotBlank() } ?: (user.displayName ?: "Giáo viên"),
                        email = user.email ?: "",
                    )
                )
            } else {
                Result.failure(Exception("Không nhận được tài khoản Google"))
            }
        } catch (e: CancellationException) {
            throw e
        } catch (e: GetCredentialCancellationException) {
            Result.failure(Exception("Bạn đã hủy đăng nhập"))
        } catch (e: NoCredentialException) {
            Result.failure(Exception("Không lấy được tài khoản Google trên máy này. Kiểm tra tài khoản Google trong Cài đặt của điện thoại, hoặc cấu hình Firebase của app, rồi thử lại."))
        } catch (e: Exception) {
            Result.failure(Exception("Đăng nhập không thành công, kiểm tra mạng rồi thử lại"))
        }
    }

    fun dangXuat() {
        FirebaseAuth.getInstance().signOut()
    }

    fun giaoVienHienTai(): GiaoVienDaDangNhap? {
        val user = FirebaseAuth.getInstance().currentUser ?: return null
        return GiaoVienDaDangNhap(user.uid, user.displayName ?: "Giáo viên", user.email ?: "")
    }
}

// ============================================================================
// REPOSITORY — mọi thao tác với Realtime Database đều qua interface này,
// trả về Result để màn hình hiển thị lỗi tiếng Việt, không crash khi mất mạng.
// ============================================================================

interface GiaoBtvnRepository {
    suspend fun taoLop(tenLop: String, giaoVien: GiaoVienDaDangNhap): Result<LopHoc>
    suspend fun layLopCuaGiaoVien(giaoVienId: String): Result<List<LopHoc>>
    suspend fun layLopTheoMa(maLop: String): Result<LopHoc>
    suspend fun thamGiaLop(maLop: String, hocSinhId: String, tenHocSinh: String): Result<LopHoc>
    suspend fun taoBaiGiao(maLop: String, baiGiao: BaiGiao): Result<BaiGiao>
    suspend fun layBaiGiaoTheoLop(maLop: String): Result<List<BaiGiao>>
    suspend fun layBaiNopTheoBaiGiao(baiGiaoId: String): Result<Map<String, BaiNop>>
    suspend fun layBaiNopCuaHocSinh(baiGiaoId: String, hocSinhId: String): Result<BaiNop?>
    suspend fun nopBaiGiay(baiGiaoId: String, baiNop: BaiNop): Result<Unit>
    suspend fun nopBaiTracNghiem(baiGiaoId: String, baiNop: BaiNop): Result<Unit>

    /**
     * Cô mở màn chấm thì chạy kiểm tra trùng: so aHash của các bài giấy
     * chưa chấm trong cùng một bài giao, bài nào có ảnh gần giống bài
     * khác thì gắn canhBaoTrung và chuyển sang CHO_DUYET_TRUNG.
     * Trả về danh sách hocSinhId bị gắn cờ.
     */
    suspend fun kiemTraTrung(baiGiaoId: String): Result<List<String>>
    suspend fun duyetTrungOk(baiGiaoId: String, hocSinhId: String): Result<Unit>
    suspend fun yeuCauNopLai(baiGiaoId: String, hocSinhId: String, ghiChu: String): Result<Unit>
    suspend fun chamDiem(baiGiaoId: String, hocSinhId: String, diem: Double, ghiChu: String): Result<Unit>

    /**
     * Ngân hàng câu hỏi riêng của cô, nhập từ file và đã qua duyệt:
     * lưu vào cây teacherQuestions/{giaoVienId}/{questionId}. Chỉ giữ
     * để đọc câu cũ, câu mới không lưu vào đây nữa.
     */
    suspend fun saveTeacherQuestions(giaoVienId: String, questions: List<ImportedQuestion>): Result<Unit>
    suspend fun loadTeacherQuestions(giaoVienId: String): Result<List<ImportedQuestion>>
    suspend fun deleteTeacherQuestion(giaoVienId: String, questionId: String): Result<Unit>

    /**
     * NGÂN HÀNG CHUNG (chốt 2026-11-01): câu cô nào tạo rồi thì giáo
     * viên khác cũng dùng được. Lưu vào cây nganHangChung/{questionId},
     * mỗi câu gắn Môn, Khối lớp, Chương, Bài, Chuyên đề. Chỉ người tạo
     * (giaoVienId trùng người yêu cầu) mới xóa được câu của mình,
     * người khác chỉ dùng nguyên bản để giao bài cho lớp của mình.
     */
    suspend fun saveCommonQuestions(questions: List<ImportedQuestion>): Result<Unit>
    suspend fun loadCommonQuestions(): Result<List<ImportedQuestion>>
    suspend fun deleteCommonQuestion(questionId: String, giaoVienId: String): Result<Unit>
}

class FirebaseRepository : GiaoBtvnRepository {
    private val root = FirebaseDatabase.getInstance().reference
    private val classesRef get() = root.child("classes")
    private val assignmentsRef get() = root.child("assignments")
    private val submissionsRef get() = root.child("submissions")
    private val teacherQuestionsRef get() = root.child("teacherQuestions")
    private val commonQuestionsRef get() = root.child("nganHangChung")
    // Danh sách lớp theo tài khoản: teacherClasses/{uid}/{maLop} = true.
    // Trang chính đọc thẳng danh sách này, không phụ thuộc vào truy vấn
    // tìm kiếm theo giaoVienId vốn là chỗ dễ làm lớp vừa tạo không hiện.
    private val teacherClassesRef get() = root.child("teacherClasses")

    /** Gói try/catch chung: lỗi mạng hay lỗi Firebase đều thành Result.failure. */
    private suspend fun <T> anToan(block: suspend () -> T): Result<T> {
        return try {
            Result.success(block())
        } catch (e: CancellationException) {
            throw e
        } catch (e: Exception) {
            Result.failure(e)
        }
    }

    override suspend fun taoLop(tenLop: String, giaoVien: GiaoVienDaDangNhap): Result<LopHoc> =
        anToan {
            var maLop = taoMaLop()
            var lanThu = 0
            // Mã lớp phải duy nhất: trùng thì sinh mã khác, tối đa 10 lần.
            while (lanThu < 10) {
                val daCo = classesRef.child(maLop).get().await().exists()
                if (!daCo) break
                maLop = taoMaLop()
                lanThu++
            }
            val lop = LopHoc(maLop, tenLop.trim(), giaoVien.uid, giaoVien.ten, emptyMap())
            classesRef.child(maLop).setValue(lop.toMap()).await()
            // Ghi thêm vào danh sách lớp của tài khoản này, để trang chính
            // đọc thẳng danh sách này mà không cần tìm kiếm.
            teacherClassesRef.child(giaoVien.uid).child(maLop).setValue(true).await()
            lop
        }

    override suspend fun layLopCuaGiaoVien(giaoVienId: String): Result<List<LopHoc>> =
        anToan {
            // Cách 1 (chính): đọc thẳng danh sách mã lớp của tài khoản,
            // rồi tải từng lớp theo mã. Không dùng truy vấn tìm kiếm.
            val maList = try {
                val snap = teacherClassesRef.child(giaoVienId).get().await()
                snap.children.mapNotNull { it.key }
            } catch (e: Exception) {
                emptyList()
            }
            val tuDanhSach = maList.mapNotNull { ma ->
                try {
                    val snap = classesRef.child(ma).get().await()
                    docLop(snap)
                } catch (e: Exception) {
                    null
                }
            }
            // Cách 2 (dự phòng + tự sửa): vẫn thử truy vấn cũ để bắt lớp
            // tạo từ bản cũ chưa có trong danh sách theo tài khoản, rồi
            // ghi bù những lớp đó vào danh sách để lần sau đọc thẳng.
            val tuTruyVan = try {
                val snap = classesRef.orderByChild("giaoVienId").equalTo(giaoVienId).get().await()
                snap.children.mapNotNull { docLop(it) }
            } catch (e: Exception) {
                emptyList()
            }
            val gop = (tuDanhSach + tuTruyVan).distinctBy { it.maLop }
            for (lop in gop) {
                if (lop.maLop !in maList) {
                    try {
                        teacherClassesRef.child(giaoVienId).child(lop.maLop).setValue(true).await()
                    } catch (e: Exception) {
                        // Ghi bù thất bại thì lần sau vẫn đọc được bằng truy vấn, không lỗi.
                    }
                }
            }
            gop
        }

    override suspend fun layLopTheoMa(maLop: String): Result<LopHoc> =
        anToan {
            val snap = classesRef.child(chuanHoaMaLop(maLop)).get().await()
            docLop(snap) ?: throw Exception("Không tìm thấy lớp với mã này")
        }

    override suspend fun thamGiaLop(maLop: String, hocSinhId: String, tenHocSinh: String): Result<LopHoc> =
        anToan {
            val ma = chuanHoaMaLop(maLop)
            val snap = classesRef.child(ma).get().await()
            val lop = docLop(snap) ?: throw Exception("Không tìm thấy lớp với mã này")
            classesRef.child(ma).child("hocSinh").child(hocSinhId).setValue(tenHocSinh.trim()).await()
            lop.copy(hocSinh = lop.hocSinh + (hocSinhId to tenHocSinh.trim()))
        }

    override suspend fun taoBaiGiao(maLop: String, baiGiao: BaiGiao): Result<BaiGiao> =
        anToan {
            val id = assignmentsRef.child(maLop).push().key ?: throw Exception("Không tạo được mã bài giao")
            val bai = baiGiao.copy(id = id)
            assignmentsRef.child(maLop).child(id).setValue(bai.toMap()).await()
            bai
        }

    override suspend fun layBaiGiaoTheoLop(maLop: String): Result<List<BaiGiao>> =
        anToan {
            val snap = assignmentsRef.child(maLop).get().await()
            snap.children.mapNotNull { docBaiGiao(it) }.sortedByDescending { it.hanNop }
        }

    override suspend fun layBaiNopTheoBaiGiao(baiGiaoId: String): Result<Map<String, BaiNop>> =
        anToan {
            val snap = submissionsRef.child(baiGiaoId).get().await()
            snap.children.mapNotNull { child ->
                val key = child.key ?: return@mapNotNull null
                val nop = docBaiNop(child) ?: return@mapNotNull null
                key to nop
            }.toMap()
        }

    override suspend fun layBaiNopCuaHocSinh(baiGiaoId: String, hocSinhId: String): Result<BaiNop?> =
        anToan {
            val snap = submissionsRef.child(baiGiaoId).child(hocSinhId).get().await()
            if (!snap.exists()) null else docBaiNop(snap)
        }

    override suspend fun nopBaiGiay(baiGiaoId: String, baiNop: BaiNop): Result<Unit> =
        anToan {
            // Nộp lại sau khi cô yêu cầu nộp lại thì ghi đè bài cũ, điểm cũ
            // bị xóa vì bài mới chưa được chấm.
            val moi = baiNop.copy(trangThai = "DA_NOP", canhBaoTrung = false, diem = null)
            submissionsRef.child(baiGiaoId).child(baiNop.hocSinhId).setValue(moi.toMap()).await()
        }

    override suspend fun nopBaiTracNghiem(baiGiaoId: String, baiNop: BaiNop): Result<Unit> =
        anToan {
            // Trắc nghiệm chỉ 1 lượt: đã có bài nộp thì không ghi đè.
            val cu = submissionsRef.child(baiGiaoId).child(baiNop.hocSinhId).get().await()
            if (cu.exists()) throw Exception("Bạn đã làm bài này rồi, mỗi bài chỉ được làm 1 lượt")
            submissionsRef.child(baiGiaoId).child(baiNop.hocSinhId)
                .setValue(baiNop.copy(trangThai = "DA_NOP").toMap()).await()
        }

    override suspend fun kiemTraTrung(baiGiaoId: String): Result<List<String>> =
        anToan {
            val tatCa = layBaiNopTheoBaiGiao(baiGiaoId).getOrThrow()
            val nghiTrung = timBaiNghiTrung(tatCa)
            val biGanCo = mutableListOf<String>()
            for ((hocSinhId, _) in nghiTrung) {
                val hienTai = tatCa[hocSinhId] ?: continue
                if (hienTai.trangThai == "CHO_DUYET_TRUNG") {
                    biGanCo.add(hocSinhId)
                    continue
                }
                submissionsRef.child(baiGiaoId).child(hocSinhId).updateChildren(
                    mapOf<String, Any>("canhBaoTrung" to true, "trangThai" to "CHO_DUYET_TRUNG")
                ).await()
                biGanCo.add(hocSinhId)
            }
            biGanCo
        }

    override suspend fun duyetTrungOk(baiGiaoId: String, hocSinhId: String): Result<Unit> =
        anToan {
            // Cô xác nhận ảnh không có vấn đề thì bài trở lại DA_NOP và
            // cô mới được nhập điểm, đúng quy trình đã chốt.
            submissionsRef.child(baiGiaoId).child(hocSinhId).updateChildren(
                mapOf<String, Any>("canhBaoTrung" to false, "trangThai" to "DA_NOP")
            ).await()
        }

    override suspend fun yeuCauNopLai(baiGiaoId: String, hocSinhId: String, ghiChu: String): Result<Unit> =
        anToan {
            // Ghi đè toàn bộ bài nộp vì điểm phải về null khi yêu cầu nộp
            // lại; updateChildren không xóa được giá trị bằng null.
            val snap = submissionsRef.child(baiGiaoId).child(hocSinhId).get().await()
            val cu = docBaiNop(snap)
                ?: throw Exception("Không tìm thấy bài nộp này")
            submissionsRef.child(baiGiaoId).child(hocSinhId)
                .setValue(cu.copy(diem = null, trangThai = "YEU_CAU_NOP_LAI", canhBaoTrung = false, ghiChuGiaoVien = ghiChu).toMap()).await()
        }

    override suspend fun chamDiem(baiGiaoId: String, hocSinhId: String, diem: Double, ghiChu: String): Result<Unit> =
        anToan {
            require(diem in 0.0..10.0) { "Điểm phải từ 0 đến 10" }
            submissionsRef.child(baiGiaoId).child(hocSinhId).updateChildren(
                mapOf<String, Any>(
                    "diem" to diem,
                    "trangThai" to "DA_NOP",
                    "canhBaoTrung" to false,
                    "ghiChuGiaoVien" to ghiChu,
                )
            ).await()
        }

    override suspend fun saveTeacherQuestions(giaoVienId: String, questions: List<ImportedQuestion>): Result<Unit> =
        anToan {
            for (cau in questions) {
                teacherQuestionsRef.child(giaoVienId).child(cau.id).setValue(cau.toMap()).await()
            }
        }

    override suspend fun loadTeacherQuestions(giaoVienId: String): Result<List<ImportedQuestion>> =
        anToan {
            val snap = teacherQuestionsRef.child(giaoVienId).get().await()
            snap.children.mapNotNull { docCauNhap(it) }.sortedBy { it.thuTu }
        }

    override suspend fun deleteTeacherQuestion(giaoVienId: String, questionId: String): Result<Unit> =
        anToan {
            teacherQuestionsRef.child(giaoVienId).child(questionId).removeValue().await()
        }

    override suspend fun saveCommonQuestions(questions: List<ImportedQuestion>): Result<Unit> =
        anToan {
            for (cau in questions) {
                commonQuestionsRef.child(cau.id).setValue(cau.toMap()).await()
            }
        }

    override suspend fun loadCommonQuestions(): Result<List<ImportedQuestion>> =
        anToan {
            val snap = commonQuestionsRef.get().await()
            snap.children.mapNotNull { docCauNhap(it) }.sortedBy { it.thuTu }
        }

    override suspend fun deleteCommonQuestion(questionId: String, giaoVienId: String): Result<Unit> =
        anToan {
            val snap = commonQuestionsRef.child(questionId).get().await()
            val cau = docCauNhap(snap) ?: throw Exception("Không tìm thấy câu này trong ngân hàng chung")
            if (cau.giaoVienId.isNotBlank() && cau.giaoVienId != giaoVienId) {
                throw Exception("Chỉ người tạo mới xóa được câu này")
            }
            commonQuestionsRef.child(questionId).removeValue().await()
        }
}

// ============================================================================
// ĐỌC SNAPSHOT THỦ CÔNG — tránh lỗi chuyển kiểu số của Firebase khi dùng
// getValue(data class), vì Firebase trả số về dạng Long còn code cần Int.
// ============================================================================

private fun snapString(snap: DataSnapshot, key: String): String =
    snap.child(key).getValue(String::class.java) ?: ""

private fun snapLong(snap: DataSnapshot, key: String): Long =
    (snap.child(key).value as? Number)?.toLong() ?: 0L

private fun snapInt(snap: DataSnapshot, key: String): Int =
    (snap.child(key).value as? Number)?.toInt() ?: 0

private fun snapBool(snap: DataSnapshot, key: String): Boolean =
    snap.child(key).getValue(Boolean::class.java) ?: false

private fun snapStringList(snap: DataSnapshot, key: String): List<String> =
    snap.child(key).children.mapNotNull { it.getValue(String::class.java) }

private fun docLop(snap: DataSnapshot): LopHoc? {
    if (!snap.exists()) return null
    val hocSinh = snap.child("hocSinh").children.mapNotNull { child ->
        val ten = child.getValue(String::class.java) ?: return@mapNotNull null
        (child.key ?: return@mapNotNull null) to ten
    }.toMap()
    return LopHoc(
        maLop = snap.key ?: snapString(snap, "maLop"),
        tenLop = snapString(snap, "tenLop"),
        giaoVienId = snapString(snap, "giaoVienId"),
        giaoVienTen = snapString(snap, "giaoVienTen"),
        hocSinh = hocSinh,
    )
}

private fun docBaiGiao(snap: DataSnapshot): BaiGiao? {
    if (!snap.exists()) return null
    val cauIds = snapStringList(snap, "cauHoiIds")
    val theoDoKho = snap.child("soCauTheoDoKho").children.mapNotNull { child ->
        val so = (child.value as? Number)?.toInt() ?: return@mapNotNull null
        (child.key ?: return@mapNotNull null) to so
    }.toMap()
    val cauAnh = snap.child("cauHoiAnh").children.mapNotNull { child ->
        val anh = child.getValue(String::class.java) ?: return@mapNotNull null
        (child.key ?: return@mapNotNull null) to anh
    }.toMap()
    val dapAnAnh = snap.child("dapAnCauAnh").children.mapNotNull { child ->
        val dap = (child.value as? Number)?.toInt() ?: return@mapNotNull null
        (child.key ?: return@mapNotNull null) to dap
    }.toMap()
    return BaiGiao(
        id = snap.key ?: snapString(snap, "id"),
        loai = snapString(snap, "loai").ifBlank { "GIAY" },
        tieuDe = snapString(snap, "tieuDe"),
        noiDung = snapString(snap, "noiDung"),
        anhDeBase64 = snapString(snap, "anhDeBase64"),
        chuDe = snapString(snap, "chuDe"),
        bai = snapString(snap, "bai"),
        hanNop = snapLong(snap, "hanNop"),
        thoiGianPhut = snapInt(snap, "thoiGianPhut"),
        cauHoiIds = cauIds,
        soCauTheoDoKho = theoDoKho,
        cauHoiAnh = cauAnh,
        dapAnCauAnh = dapAnAnh,
    )
}

private fun snapIntOrNull(snap: DataSnapshot, key: String): Int? =
    (snap.child(key).value as? Number)?.toInt()

private fun docCauNhap(snap: DataSnapshot): ImportedQuestion? {
    if (!snap.exists()) return null
    return ImportedQuestion(
        id = snap.key ?: snapString(snap, "id"),
        giaoVienId = snapString(snap, "giaoVienId"),
        mon = snapString(snap, "mon"),
        khoi = snapString(snap, "khoi"),
        chuong = snapString(snap, "chuong"),
        bai = snap.child("bai").getValue(String::class.java),
        dang = snapString(snap, "dang").ifBlank { "VIET" },
        anhBase64 = snapString(snap, "anhBase64"),
        textGoc = snap.child("textGoc").getValue(String::class.java),
        dapAnDung = snapIntOrNull(snap, "dapAnDung"),
        doKho = snapIntOrNull(snap, "doKho"),
        trangThai = snapString(snap, "trangThai").ifBlank { "DA_DUYET" },
        nguonFile = snapString(snap, "nguonFile"),
        thuTu = snapInt(snap, "thuTu"),
        soLanGiao = snapInt(snap, "soLanGiao"),
        doTinCay = snapInt(snap, "doTinCay"),
        tags = snapStringList(snap, "tags"),
        nguonDongGop = snapString(snap, "nguonDongGop"),
        chuyenDe = snapString(snap, "chuyenDe"),
        giaoVienTen = snapString(snap, "giaoVienTen"),
    )
}

private fun docBaiNop(snap: DataSnapshot): BaiNop? {
    if (!snap.exists()) return null
    val dapAn = snap.child("dapAn").children.mapNotNull { child ->
        val chon = (child.value as? Number)?.toInt() ?: return@mapNotNull null
        (child.key ?: return@mapNotNull null) to chon
    }.toMap()
    val diemRaw = snap.child("diem").value as? Number
    return BaiNop(
        hocSinhId = snap.key ?: snapString(snap, "hocSinhId"),
        dapAn = dapAn,
        anhBase64 = snapStringList(snap, "anhBase64"),
        aHash = snapStringList(snap, "aHash"),
        diem = diemRaw?.toDouble(),
        trangThai = snapString(snap, "trangThai").ifBlank { "DA_NOP" },
        canhBaoTrung = snapBool(snap, "canhBaoTrung"),
        thoiGianNop = snapLong(snap, "thoiGianNop"),
        ghiChuGiaoVien = snapString(snap, "ghiChuGiaoVien"),
    )
}
