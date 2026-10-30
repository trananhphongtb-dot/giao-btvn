package vn.giaobtvn.tieuhoc.data

import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.pdf.PdfRenderer
import android.net.Uri
import android.os.ParcelFileDescriptor
import com.google.mlkit.vision.common.InputImage
import com.google.mlkit.vision.text.TextRecognition
import com.google.mlkit.vision.text.TextRecognizerOptions
import java.io.InputStream
import java.util.zip.ZipInputStream
import kotlinx.coroutines.tasks.await
import org.xmlpull.v1.XmlPullParser
import org.xmlpull.v1.XmlPullParserFactory

// ============================================================================
// ĐỌC FILE NHẬP: DOCX (text) / PDF (trang) / ẢNH — không thêm dependency
// nặng cho DOCX, chỉ dùng ZipInputStream + XmlPullParser có sẵn.
// ============================================================================

/** Loại file nhập, dùng để lưu vào nguonFile và chọn đường xử lý. */
enum class LoaiFileNhap { DOCX, PDF, ANH, KHONG_BIET }

data class KetQuaNhap(
    val candidates: List<SplitCandidate>,
    val loaiFile: LoaiFileNhap,
)

/** Đầu câu OCR tìm được trên 1 trang ảnh: số câu, tọa độ Y trên cùng, độ tin cậy. */
data class OcrHeader(val soCau: Int, val topY: Int, val doTinCay: Int)

/** Interface OCR để dễ thay bộ máy khác về sau mà không sửa màn duyệt. */
interface OcrEngine {
    suspend fun findQuestionHeaders(bitmap: Bitmap): List<OcrHeader>
}

/**
 * OCR bằng ML Kit Text Recognition (bộ máy Latin, đọc được tiếng Việt có
 * dấu vì tiếng Việt dùng bảng chữ Latin mở rộng). ML Kit không công bố
 * độ tin cậy từng dòng nên header tìm được gán 80 điểm, để màn duyệt
 * vẫn biết đây là câu cắt từ OCR chứ không phải từ text chuẩn.
 * Lỗi ML Kit thì trả về danh sách rỗng, phía gọi sẽ fallback thành 1 ứng
 * viên cho cả trang để cô tách tay, không được bỏ trang.
 */
class MlKitOcrEngine : OcrEngine {
    // Cùng lý do như regexDauCau: [âÂaA] để nhận cả "Câu" có dấu và
    // "Cau" mất dấu do OCR, không dùng (?i) đơn thuần.
    private val regexOcr = Regex("""^\s*[Cc][âÂaA][uU]\s*(\d+)\s*[.\)]""")

    override suspend fun findQuestionHeaders(bitmap: Bitmap): List<OcrHeader> {
        return try {
            val recognizer = TextRecognition.getClient(TextRecognizerOptions.DEFAULT_OPTIONS)
            val ketQua = recognizer.process(InputImage.fromBitmap(bitmap, 0)).await()
            val headers = mutableListOf<OcrHeader>()
            for (block in ketQua.textBlocks) {
                for (line in block.lines) {
                    val match = regexOcr.find(line.text.trim()) ?: continue
                    val so = match.groupValues.getOrNull(1)?.toIntOrNull() ?: continue
                    val top = line.boundingBox?.top ?: continue
                    headers.add(OcrHeader(soCau = so, topY = top, doTinCay = 80))
                }
            }
            headers.sortedBy { it.topY }.distinctBy { it.soCau }
        } catch (e: Exception) {
            emptyList()
        }
    }
}

/**
 * Đọc text từ file DOCX: DOCX là file zip, text nằm trong word/document.xml,
 * mỗi đoạn <w:t> là một mảnh text, hết đoạn văn <w:p> thì xuống dòng.
 * Trả Result để màn hình hiển thị lỗi tiếng Việt, không crash khi file
 * không phải DOCX thật hoặc bị hỏng.
 */
fun readDocxText(context: Context, uri: Uri): Result<String> {
    return try {
        val stream: InputStream = context.contentResolver.openInputStream(uri)
            ?: return Result.failure(Exception("Không mở được file này"))
        var textTimDuoc: String? = null
        stream.use { input ->
            val zip = ZipInputStream(input)
            var entry = zip.nextEntry
            while (entry != null) {
                if (entry.name == "word/document.xml") {
                    textTimDuoc = docTextTuDocumentXml(zip)
                    break
                }
                entry = zip.nextEntry
            }
        }
        val text = textTimDuoc
        if (text.isNullOrBlank()) {
            Result.failure(Exception("File này không có chữ để đọc, có thể là file ảnh scan"))
        } else {
            Result.success(text)
        }
    } catch (e: Exception) {
        Result.failure(Exception("Không đọc được file DOCX này"))
    }
}

private fun docTextTuDocumentXml(stream: InputStream): String {
    val factory = XmlPullParserFactory.newInstance().apply { isNamespaceAware = true }
    val parser = factory.newPullParser()
    parser.setInput(stream, "UTF-8")
    val ketQua = StringBuilder()
    var trongText = false
    var event = parser.eventType
    while (event != XmlPullParser.END_DOCUMENT) {
        when (event) {
            XmlPullParser.START_TAG -> {
                if (parser.name == "t") trongText = true
            }
            XmlPullParser.TEXT -> {
                if (trongText) ketQua.append(parser.text)
            }
            XmlPullParser.END_TAG -> {
                if (parser.name == "t") {
                    trongText = false
                } else if (parser.name == "p") {
                    ketQua.append("\n")
                }
            }
        }
        event = parser.next()
    }
    return ketQua.toString()
}

/**
 * Render mỗi trang PDF thành 1 Bitmap bằng PdfRenderer có sẵn của Android.
 * Kích thước trang gốc của PdfRenderer đủ đọc trên điện thoại, bản này
 * không phóng to thêm để tránh tốn bộ nhớ với đề nhiều trang.
 */
fun renderPdfPagesToBitmaps(context: Context, uri: Uri): Result<List<Bitmap>> {
    return try {
        val pfd: ParcelFileDescriptor = context.contentResolver.openFileDescriptor(uri, "r")
            ?: return Result.failure(Exception("Không mở được file PDF này"))
        val pages = mutableListOf<Bitmap>()
        pfd.use { fd ->
            val renderer = PdfRenderer(fd)
            try {
                for (i in 0 until renderer.pageCount) {
                    val page = renderer.openPage(i)
                    try {
                        val bitmap = Bitmap.createBitmap(page.width, page.height, Bitmap.Config.ARGB_8888)
                        page.render(bitmap, null, null, PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY)
                        pages.add(bitmap)
                    } finally {
                        page.close()
                    }
                }
            } finally {
                renderer.close()
            }
        }
        if (pages.isEmpty()) {
            Result.failure(Exception("File PDF này không có trang nào"))
        } else {
            Result.success(pages)
        }
    } catch (e: Exception) {
        Result.failure(Exception("Không đọc được file PDF này"))
    }
}

/** Giải mã ảnh từ Uri, thu nhỏ về tối đa 1600px để OCR và cắt không tốn bộ nhớ. */
fun giaiMaBitmapNhap(context: Context, uri: Uri, canhDaiToiDa: Int = 1600): Bitmap? {
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

// ============================================================================
// CẮT ẢNH THEO HEADER OCR
// ============================================================================

/**
 * Cắt 1 trang ảnh thành các ứng viên câu hỏi theo tọa độ Y của header:
 * câu N lấy từ đầu header Câu N đến ngay trước header Câu N+1, câu cuối
 * lấy đến hết trang. Vùng trước header đầu tiên (thường là tiêu đề đề)
 * nếu cao từ 60px trở lên cũng thành 1 ứng viên đoạn mở đầu để cô xóa,
 * không tự ý bỏ. Câu tràn trang ở bản này CHƯA tự gộp liên trang hoàn
 * hảo: cô dùng nút Gộp ở màn duyệt, đã ghi rõ trong README.
 */
fun splitPageBitmapByHeaders(bitmap: Bitmap, headers: List<OcrHeader>): List<SplitCandidate> {
    if (headers.isEmpty()) {
        return listOf(
            SplitCandidate(
                anhBase64 = nenAnhBase64(bitmap),
                textGoc = null,
                soCauDuDoan = 0,
                canhBao = listOf("CAN_KIEM_TRA"),
                doTinCay = 0,
            )
        )
    }
    val sapXep = headers.sortedBy { it.topY }
    val ketQua = mutableListOf<SplitCandidate>()
    val topDau = sapXep.first().topY.coerceIn(0, bitmap.height - 1)
    if (topDau >= 60) {
        val moDau = Bitmap.createBitmap(bitmap, 0, 0, bitmap.width, topDau)
        ketQua.add(
            SplitCandidate(
                anhBase64 = nenAnhBase64(moDau),
                textGoc = null,
                soCauDuDoan = 0,
                canhBao = listOf("DOAN_MO_DAU"),
                doTinCay = 100,
            )
        )
    }
    for (i in sapXep.indices) {
        val top = sapXep[i].topY.coerceIn(0, bitmap.height - 1)
        val bottom = if (i + 1 < sapXep.size) {
            sapXep[i + 1].topY.coerceIn(top + 1, bitmap.height)
        } else {
            bitmap.height
        }
        if (bottom - top < 10) continue
        val cat = Bitmap.createBitmap(bitmap, 0, top, bitmap.width, bottom - top)
        val tinCay = sapXep[i].doTinCay
        ketQua.add(
            SplitCandidate(
                anhBase64 = nenAnhBase64(cat),
                textGoc = null,
                soCauDuDoan = sapXep[i].soCau,
                canhBao = if (tinCay < 50) listOf("OCR_THAP") else emptyList(),
                doTinCay = tinCay,
            )
        )
    }
    return ketQua
}

// ============================================================================
// LUỒNG NHẬP TỔNG: chọn đường xử lý theo loại file, luôn trả về ứng viên
// để cô duyệt, không bao giờ trả về rỗng mà không có lý do.
// ============================================================================

/**
 * Xử lý 1 file nhập thành danh sách ứng viên câu hỏi:
 * - DOCX: đọc text, tách theo đầu câu, render mỗi câu thành ảnh. Đoạn mở
 *   đầu (nếu có) thành ứng viên đầu tiên để cô xóa.
 * - PDF: render từng trang, OCR tìm header, cắt theo header. Trang nào
 *   không tìm thấy header thì cả trang thành 1 ứng viên CAN_KIEM_TRA.
 * - Ảnh: giải mã rồi xử lý như 1 trang PDF scan.
 * - Không xác định được loại: thử đọc DOCX trước, rồi thử PDF, cuối cùng
 *   thử giải mã ảnh; tất cả thất bại thì trả lỗi rõ ràng.
 */
suspend fun processImport(
    context: Context,
    uri: Uri,
    loaiFileGoiY: LoaiFileNhap = LoaiFileNhap.KHONG_BIET,
    ocr: OcrEngine = MlKitOcrEngine(),
): Result<KetQuaNhap> {
    // Đường DOCX: đọc text trước, tách câu, render ảnh từng câu.
    if (loaiFileGoiY == LoaiFileNhap.DOCX) {
        val textResult = readDocxText(context, uri)
        if (textResult.isSuccess) {
            val text = textResult.getOrThrow()
            return Result.success(KetQuaNhap(candidatesTuText(text), LoaiFileNhap.DOCX))
        }
        // DOCX không đọc được chữ (có thể là ảnh scan đóng trong DOCX)
        // thì rơi xuống đường ảnh ở cuối hàm, không báo lỗi ngay.
    }
    // Đường PDF: render trang rồi OCR từng trang.
    if (loaiFileGoiY == LoaiFileNhap.PDF) {
        val pdfResult = renderPdfPagesToBitmaps(context, uri)
        if (pdfResult.isSuccess) {
            val tatCa = mutableListOf<SplitCandidate>()
            for (trang in pdfResult.getOrThrow()) {
                val headers = ocr.findQuestionHeaders(trang)
                tatCa.addAll(splitPageBitmapByHeaders(trang, headers))
            }
            return Result.success(KetQuaNhap(tatCa, LoaiFileNhap.PDF))
        }
        return Result.failure(Exception("Không đọc được file PDF này"))
    }
    // Đường ảnh (và fallback cuối cho mọi loại không xác định).
    val bitmap = giaiMaBitmapNhap(context, uri)
    if (bitmap != null) {
        val headers = ocr.findQuestionHeaders(bitmap)
        return Result.success(KetQuaNhap(splitPageBitmapByHeaders(bitmap, headers), LoaiFileNhap.ANH))
    }
    // Thử lần cuối theo từng loại, để báo lỗi đúng nguyên nhân nhất.
    val docxThu = readDocxText(context, uri)
    if (docxThu.isSuccess) {
        return Result.success(KetQuaNhap(candidatesTuText(docxThu.getOrThrow()), LoaiFileNhap.DOCX))
    }
    val pdfThu = renderPdfPagesToBitmaps(context, uri)
    if (pdfThu.isSuccess) {
        val tatCa = mutableListOf<SplitCandidate>()
        for (trang in pdfThu.getOrThrow()) {
            val headers = ocr.findQuestionHeaders(trang)
            tatCa.addAll(splitPageBitmapByHeaders(trang, headers))
        }
        return Result.success(KetQuaNhap(tatCa, LoaiFileNhap.PDF))
    }
    return Result.failure(Exception("Không đọc được file này. Hãy chọn file ảnh, PDF hoặc DOCX khác."))
}

private fun candidatesTuText(text: String): List<SplitCandidate> {
    val tach = tachTextCoMoDau(text)
    val ketQua = mutableListOf<SplitCandidate>()
    if (tach.doanMoDau.isNotBlank()) {
        val anhMoDau = renderTextQuestionToBitmap(tach.doanMoDau)
        ketQua.add(
            SplitCandidate(
                anhBase64 = nenAnhBase64(anhMoDau),
                textGoc = tach.doanMoDau,
                soCauDuDoan = 0,
                canhBao = listOf("DOAN_MO_DAU"),
                doTinCay = 100,
            )
        )
    }
    for (cau in tach.cau) {
        val anh = renderTextQuestionToBitmap(cau.text)
        // Phân loại gợi ý ngay lúc cắt (chỉ làm được vì có text); cô sẽ
        // xét lại tag và mức độ ở màn duyệt trước khi chốt, giá trị sau
        // khi sửa mới được lưu vào ngân hàng.
        val phanLoai = classifyQuestion(cau.text)
        ketQua.add(
            SplitCandidate(
                anhBase64 = nenAnhBase64(anh),
                textGoc = cau.text,
                soCauDuDoan = cau.soCau,
                canhBao = emptyList(),
                doTinCay = 100,
                tags = phanLoai.tags,
                doKhoGoiY = phanLoai.doKhoGoiY,
            )
        )
    }
    if (ketQua.isEmpty()) {
        // Text có nhưng không có đầu câu nào: cả text thành 1 ứng viên
        // để cô tách tay ở màn duyệt, không tự ý bỏ nội dung.
        val anh = renderTextQuestionToBitmap(text)
        ketQua.add(
            SplitCandidate(
                anhBase64 = nenAnhBase64(anh),
                textGoc = text,
                soCauDuDoan = 0,
                canhBao = listOf("CAN_KIEM_TRA"),
                doTinCay = 0,
            )
        )
    }
    return ketQua
}
