# Giao Bài Tập Về Nhà — V1 (code local, chưa build, chưa push)

App giao bài tập về nhà cho tiểu học, UI tiếng Việt, không quảng cáo,
không chat tự do. V1 chỉ có 2 vai, **không có vai phụ huynh**.

## Luồng dùng đã chốt

1. Mở app, chọn vai: **Giáo viên** hoặc **Học sinh**.
2. **Giáo viên**: đăng nhập Google (Credential Manager, theo mẫu
   quoc-te-app), tạo lớp (mã lớp 6 ký tự chữ + số), quản lý nhiều lớp,
   xem danh sách học sinh từng lớp.
3. **Học sinh**: không cần đăng nhập Google, nhập mã lớp + tên để tham
   gia lớp; xem bài được giao, làm/nộp bài, xem điểm của mình.
4. **Ôn bài tự do** (tách riêng bài giao): học sinh chọn theo chủ đề
   HOẶC theo bài, hệ thống lấy ngẫu nhiên câu hỏi từ ngân hàng trong
   assets, không giới hạn thời gian, không tính vào điểm lớp, làm xong
   mỗi câu hiện đáp án đúng ngay. Vào vai học sinh là ôn được ngay,
   không bắt buộc vào lớp trước.

## 2 loại bài giao

### Loại 1 — Bài giấy chụp ảnh

- Cô giao đề: tiêu đề + nội dung/ảnh đề + hạn nộp.
- Học sinh làm ra giấy, chụp tối đa 3 ảnh nộp. Ảnh nén về tối đa
  1024px, JPEG ~70, lưu dạng Base64 trong Realtime Database ở V1.
  Về sau có thể chuyển sang Firebase Storage thì chỉ cần thay hàm nén
  / tải ảnh, phần còn lại không đổi.
- **Chống trùng ảnh**: khi nộp, máy học sinh tính aHash của mỗi ảnh
  (thu nhỏ 8x8, chuyển xám, so với giá trị trung bình, ra chuỗi 16 ký
  tự hex) và lưu kèm bài nộp. Khi cô mở màn chấm, app so khoảng cách
  Hamming giữa aHash của các bài nộp trong cùng một bài giao; khoảng
  cách <= 12 thì gắn cờ **"nghi trùng"** và hiện 2 ảnh cạnh nhau cho cô
  so sánh. Bài bị gắn cờ chuyển sang trạng thái `CHO_DUYET_TRUNG`,
  chưa được tính điểm; cô bấm **"Xác nhận ok"** mới được nhập điểm,
  hoặc bấm **"Yêu cầu nộp lại"** thì học sinh nộp bài mới.

### Loại 2 — Trắc nghiệm giới hạn thời gian

- Cô chọn bài/chủ đề, rồi 1 trong 2 cách: (a) chọn tay từng câu từ danh
  sách, (b) chọn tự động theo mức độ (nhập số câu dễ/vừa/khó, hệ thống
  lấy ngẫu nhiên không trùng, mức nào thiếu thì không bù bằng mức khác).
- Cô đặt thời gian làm bài (phút) và hạn nộp. Học sinh làm: đếm ngược,
  hết giờ tự nộp, trộn thứ tự câu và đáp án (đáp án nộp lưu theo chỉ số
  gốc để thống kê của cô so sánh đúng), chỉ 1 lượt làm, chấm tự động
  thang điểm 10, hiện điểm ngay sau khi nộp.

## Thống kê (cô xem theo từng bài giao)

Danh sách học sinh trong lớp với trạng thái `DA_NOP` / `CHUA_NOP` /
`QUA_HAN` (dựa vào hạn nộp và thời điểm nộp), điểm từng em, tỉ lệ lớp
đã nộp, điểm trung bình lớp; riêng trắc nghiệm thêm số lần sai của
từng câu để cô thấy câu nào học sinh sai nhiều nhất.

## Cấu trúc Realtime Database

```
classes/{maLop}
  tenLop, giaoVienId, giaoVienTen,
  hocSinh: { hocSinhId: tenHocSinh }
assignments/{maLop}/{baiGiaoId}
  loai, tieuDe, noiDung, anhDeBase64, chuDe, bai, hanNop (millis),
  thoiGianPhut, cauHoiIds, soCauTheoDoKho: { "1": n, "2": n, "3": n }
submissions/{baiGiaoId}/{hocSinhId}
  dapAn: { cauHoiId: chiSoDaChon }, anhBase64: [...tối đa 3...],
  aHash: [...], diem (thang 10, null = chưa chấm), trangThai,
  canhBaoTrung, thoiGianNop (millis), ghiChuGiaoVien
```

Câu hỏi nằm trong `app/src/main/assets/cau_hoi.json`, không nằm trong
Realtime Database ở V1. File mẫu V1 có 64 câu thật: Toán 24, Tiếng Việt
20, Khoa học 20, chia theo bài, mỗi câu 4 đáp án, độ khó 1–3.

## Cấu trúc code

```
settings.gradle.kts, build.gradle.kts, gradle.properties
app/build.gradle.kts        (namespace/applicationId TẠM vn.giaobtvn.tieuhoc)
app/src/main/AndroidManifest.xml
app/src/main/res/values/    (strings, themes, colors)
app/src/main/res/xml/file_paths.xml   (FileProvider cho ảnh camera)
app/src/main/java/vn/giaobtvn/tieuhoc/
  MainActivity.kt           (điều hướng bằng state, không dùng Navigation)
  data/Models.kt            (data class, enum, cấu trúc RTDB, aHash/Hamming,
                             trộn câu/đáp án, chấm điểm thang 10)
  data/QuestionBank.kt      (đọc assets, lọc, lấy ngẫu nhiên, chọn theo mức độ)
  data/Repository.kt        (FirebaseRepository, đăng nhập Google, LocalPrefs)
  ui/Theme.kt, ui/Common.kt (nút, thẻ, chip trạng thái, đồng hồ đếm ngược,
                             đọc ảnh từ Uri/Base64)
  ui/RoleScreen.kt
  ui/TeacherScreens.kt      (tạo lớp, danh sách lớp, tạo 2 loại bài,
                             chấm + duyệt trùng + thống kê, chọn câu đã nhập)
  ui/StudentScreens.kt      (tham gia lớp, danh sách bài, làm trắc nghiệm
                             tính giờ (gồm câu ảnh đã nhập), nộp bài giấy
                             camera/thư viện, ôn tự do)
  data/ImportedQuestions.kt (câu hỏi nhập, tách text theo đầu câu, render
                             text thành ảnh, gộp/tách ảnh)
  data/QuestionImport.kt    (đọc DOCX/PDF/ảnh, OCR ML Kit, cắt trang theo
                             header, luồng nhập tổng)
  data/QuestionClassify.kt  (gợi ý thẻ nội dung + mức độ bằng từ khóa
                             tiếng Việt, cô xét lại ở màn duyệt mới lưu)
  ui/TeacherImportScreens.kt (chọn file -> nhánh -> cắt thử -> duyệt ->
                             chọn đáp án đúng -> lưu ngân hàng của cô)
```

## Nhập câu hỏi từ file — đã code ngày 2026-10-30, chưa build thật, chưa push

Cách cắt đã chốt: **cắt tự động + cô duyệt lại**. Luồng của cô: trang giáo
viên bấm "Up bài tập / Nhập câu hỏi" -> chọn file ảnh, PDF hoặc DOCX ->
chọn nhánh Môn / Khối / Chương / Bài / Dạng (Viết hay Trắc nghiệm ảnh) ->
máy cắt thử -> cô duyệt (Giữ / Gộp với câu sau / Tách theo thanh trượt /
Xóa / Lên / Xuống) -> trắc nghiệm thì chọn đáp án đúng A/B/C/D cho từng
câu -> lưu vào ngân hàng riêng của cô (`teacherQuestions/{giaoVienId}`).

- DOCX có chữ: đọc text bằng ZipInputStream + XmlPullParser (không thêm
  dependency nặng), tách theo đầu dòng `Câu N.` / `Câu N)`, đoạn mở đầu
  trước câu đầu tiên thành 1 ứng viên để cô xóa chứ không tự bỏ, rồi
  render mỗi câu thành ảnh.
- PDF / ảnh scan: render trang thành ảnh, OCR bằng ML Kit Text Recognition
  (dependency `com.google.mlkit:text-recognition:16.0.0`, cần kiểm tra lại
  phiên bản ở lần build Gradle thật đầu tiên), cắt theo tọa độ dòng
  `Câu N`. Trang không tìm thấy đầu câu thì cả trang thành 1 ứng viên
  để cô tách tay, không bỏ trang.
- Khi tạo bài trắc nghiệm, cô có thể chọn thêm câu đã nhập (lọc theo
  Môn/Khối/Chương/Bài); ảnh và đáp án đúng của câu nhập được gắn kèm
  vào bài giao để học sinh làm được (xem ảnh, chọn A/B/C/D, không xáo
  thứ tự chữ cái) và thống kê câu sai gồm cả câu nhập.

Giới hạn: OCR và PdfRenderer chưa được build thật để kiểm chứng; câu tràn
trang chưa tự gộp liên trang hoàn hảo (cô gộp tay ở màn duyệt); kéo chỉnh
pixel chính xác chưa làm, chỉ có thanh trượt vị trí tách.

## Bản sửa 11:17 ngày 2026-10-30 (đã code, chưa build thật, chưa push)

- **Nhánh tạm thời chỉ Môn/Chương, không chia đến Bài.** Luồng nhập chỉ
  bắt buộc Môn + Chương (Khối lớp không bắt buộc). Trường bai của câu
  nhập để nullable; ngân hàng câu nhập lọc theo Môn/Chương (kèm
  tag/mức độ). Ngân hàng assets cũ giữ trường bai cho câu cũ.
- **Phân loại tự động là gợi ý, cô xét lại mới vào ngân hàng.**
  `data/QuestionClassify.kt` gợi ý thẻ nội dung bằng từ khóa tiếng Việt
  (chuẩn hóa không dấu để so khớp, giữ text gốc có dấu để hiển thị) và
  mức độ theo heuristic (1 thẻ + câu ngắn = 1, 2 thẻ hoặc câu dài hoặc
  có "chứng minh" = 2, từ 3 thẻ trở lên = 3). Một câu có thể có nhiều
  thẻ, ví dụ DUONG_TRON + OXY + BAC_2. Màn duyệt cho cô sửa Môn/Chương,
  tag và mức độ từng câu; giá trị sau khi sửa mới được lưu. Câu cắt từ
  ảnh scan không có text thì không gợi ý được, cô tự gắn.
- **Giáo viên có 3 lối vào rõ ràng:** (a) "Tạo BTVN trắc nghiệm" (chọn
  lớp, chọn câu từ ngân hàng lọc Môn/Chương/tag/mức độ hoặc câu assets),
  (b) "Tự up câu hỏi" (luồng import, dùng ngay để tạo bài),
  (c) "Đóng góp cho ngân hàng BTVN" (cùng luồng import + duyệt, câu chốt
  có cờ nguonDongGop = giaoVienId). Ở bản này ngân hàng vẫn lưu riêng
  theo từng cô, chưa chia sẻ chéo thật.
- **Học sinh ôn tập từ ngân hàng này:** màn Ôn tập lấy thêm câu trắc
  nghiệm ảnh đã duyệt của cô dạy lớp các em đang tham gia (lọc
  Môn/Chương), vẫn không giới hạn thời gian, không tính điểm lớp, hiện
  đáp án đúng ngay sau mỗi câu (câu ảnh hiện đáp án đúng A/B/C/D).

Giới hạn thêm: phân loại từ khóa chỉ là gợi ý, độ chính xác phụ thuộc
text gốc hoặc OCR, và bắt buộc cô duyệt — không câu nào tự vào ngân
hàng khi chưa qua duyệt.

## 3 thứ còn thiếu để build (chưa làm)

1. **google-services.json** từ Firebase project **RIÊNG** cho app này
   (không dùng chung project với app khác, không commit file này vào
   repo). Chưa có file này thì chưa build được vì plugin google-services
   cần nó để sinh `default_web_client_id` cho đăng nhập Google.
2. **Tên app + package chính thức** do user chốt (hiện tại chỉ là tạm:
   tên hiển thị "Giao Bài Tập Về Nhà", namespace/applicationId
   `vn.giaobtvn.tieuhoc`).
3. **Repo GitHub chính thức** do user chốt (chưa tạo repo, chưa push
   code này lên đâu cả).

Ngoài ra, V1 chưa chạy build Gradle thật trên máy này (chưa xác nhận có
Android SDK), nên code mới chỉ được kiểm tra bằng script: đếm file,
package, cân bằng ngoặc, JSON ngân hàng hợp lệ.

## Hạn chế đã biết ở V1 (không phải lỗi, cần user biết)

- Học sinh đổi máy khác sẽ có id mới, cô sẽ thấy như một học sinh mới,
  vì học sinh không đăng nhập tài khoản.
- Đồng hồ trắc nghiệm chạy trên máy học sinh: thoát app giữa chừng rồi
  vào lại thì đồng hồ tính lại từ đầu, nhưng bài đã nộp thì không làm
  lại được.
- Ảnh Base64 trong Realtime Database chỉ hợp cho V1 với ít ảnh; khi lớp
  đông hoặc bài nhiều ảnh thì nên chuyển sang Firebase Storage.
