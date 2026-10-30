// Plugin lấy theo mẫu quoc-te-app. google-services BẮT BUỘC phải có thì app
// mới build được, nhưng file google-services.json KHÔNG nằm trong repo này:
// file đó chỉ được thêm vào sau khi tạo Firebase project RIÊNG cho app này.
plugins {
    id("com.android.application") version "8.11.1" apply false
    id("org.jetbrains.kotlin.android") version "2.1.21" apply false
    id("org.jetbrains.kotlin.plugin.compose") version "2.1.21" apply false
    id("com.google.gms.google-services") version "4.4.3" apply false
}
