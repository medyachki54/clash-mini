[app]
title = ClashMini
package.name = clashmini
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg

version = 0.1

requirements = python3,kivy

orientation = landscape
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 25b

android.permissions = INTERNET

[python]
python_version = 3
