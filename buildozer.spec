[app]

# (str) Title of your application
title = DiagDiesel Maitre

# (str) Package name
package.name = diagdieselmaitre

# (str) Package domain (needed for android packaging)
package.domain = org.benahmed

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,ttf

# (list) Application requirements
# تم ضبط الإصدارات هنا بدقة لتتوافق مع تصميم واجهتك الحديثة والمستقرة
requirements = python3, kivy==2.3.0, kivymd==2.0.0, pillow

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# =============================================================================
# Android specific configuration
# =============================================================================

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data directory for storing app files
android.private_storage = True

# (str) Bootstrap to use for android outputs
android.bootstrap = sdl2

# (bool) Copy library instead of making a symlink
# مهم جداً لمنع مشاكل الصلاحيات أثناء البناء على سيرفرات GitHub
android.copy_libs = 1

# (bool) Accept SDK license without operator input
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
