plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("org.jetbrains.kotlin.plugin.compose")
    id("com.google.gms.google-services")
}

android {
    // Namespace và applicationId TẠM, chưa chốt tên app / package / repo chính thức.
    // Khi user chốt, đổi 2 dòng dưới và đổi tên thư mục package Kotlin cho khớp.
    namespace = "vn.giaobtvn.tieuhoc"
    compileSdk = 36

    defaultConfig {
        applicationId = "vn.giaobtvn.tieuhoc"
        minSdk = 24
        targetSdk = 36
        versionCode = 1
        versionName = "0.1.0"
    }

    // Khóa ký lấy từ biến môi trường khi build (theo mẫu cũ); không có thì
    // dùng khóa debug mặc định. KHÔNG hard-code mật khẩu trong file này.
    val ksFile = System.getenv("KEYSTORE_FILE")?.let { file(it) }?.takeIf { it.exists() }
    signingConfigs {
        if (ksFile != null) {
            create("upload") {
                storeFile = ksFile
                storePassword = System.getenv("KEYSTORE_PASSWORD")
                keyAlias = System.getenv("KEY_ALIAS")
                keyPassword = System.getenv("KEY_PASSWORD")
            }
        }
    }

    buildTypes {
        debug {
            if (ksFile != null) signingConfig = signingConfigs.getByName("upload")
        }
        release {
            isMinifyEnabled = false
            if (ksFile != null) signingConfig = signingConfigs.getByName("upload")
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = "17"
    }
    buildFeatures {
        compose = true
    }
}

dependencies {
    implementation(platform("androidx.compose:compose-bom:2025.06.00"))
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.foundation:foundation")
    implementation("androidx.compose.material3:material3")
    implementation("androidx.activity:activity-compose:1.10.1")
    implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.9.1")
    implementation("androidx.core:core-ktx:1.16.0")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.10.2")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-play-services:1.10.2")

    // Firebase: đăng nhập giáo viên + Realtime Database cho lớp / bài giao / bài nộp.
    // Theo mẫu quoc-te-app, dùng Firebase BOM 34.0.0.
    implementation(platform("com.google.firebase:firebase-bom:34.0.0"))
    implementation("com.google.firebase:firebase-auth")
    implementation("com.google.firebase:firebase-database")

    // Đăng nhập Google qua Credential Manager, theo mẫu quoc-te-app.
    implementation("androidx.credentials:credentials:1.5.0")
    implementation("androidx.credentials:credentials-play-services-auth:1.5.0")
    implementation("com.google.android.libraries.identity.googleid:googleid:1.1.1")

    // Nhận diện chữ tiếng Việt (bảng chữ Latin) để cắt ảnh đề thành từng
    // câu theo đầu câu "Câu N". Phiên bản 16.0.0 lấy theo hệ sinh thái
    // ML Kit 2025, cần kiểm tra lại ở lần build Gradle thật đầu tiên.
    implementation("com.google.mlkit:text-recognition:16.0.0")
}
