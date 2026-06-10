[app]
title = DiagDiesel Maitre
package.name = diagdieselmaitre
package.domain = org.benahmed
source.dir = .
source.include_exts = py,kv,png,jpg

# الإصدار الذي تم إصلاحه
version = 0.1

# المتطلبات المستقرة 100% مع البناء السحابي (أضفنا pillow لمعالجة أيقونات تطبيقك)
requirements = python3==3.11.1, kivy==2.3.0, kivymd==1.2.0, pillow

# إعدادات الأندرويد الأساسية والسريعة
orientation = portrait
fullscreen = 1
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True

# قبول التراخيص تلقائياً لتفادي توقف السيرفر
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
