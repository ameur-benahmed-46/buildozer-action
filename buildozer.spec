[app]

# معلومات التطبيق
title = DiagDiesel Maitre
package.name = diagdieselmaitre
package.domain = org.benahmed

# الملفات المصدرية
source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,json,ttf

# الإصدار
version = 0.1

# المتطلبات
requirements = python3==3.11.1,kivy==2.3.0,kivymd==1.2.0,pillow

# شاشة البداية
orientation = portrait
fullscreen = 1

# الصلاحيات (أضف ما تحتاجه فقط)
android.permissions = INTERNET

# معمارية البناء
android.archs = armeabi-v7a,arm64-v8a

# نسخ احتياطي
android.allow_backup = True

# قبول التراخيص تلقائياً
android.accept_sdk_license = True

# إصدار API
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b

# تحسينات الأداء
android.enable_androidx = True

# إخفاء نافذة Python
android.entrypoint = org.kivy.android.PythonActivity

# تضمين الملفات
source.exclude_dirs = tests,bin,venv,.git,__pycache__
source.exclude_patterns = *.pyc,*.pyo

# تسجيل الأخطاء
log_level = 2

# عدم التحذير عند التشغيل كـ root
warn_on_root = 0

# إعدادات Kivy
osx.python_version = 3
osx.kivy_version = 2.3.0


[buildozer]

log_level = 2
warn_on_root = 0
