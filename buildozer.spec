[app]
title = FaceApp
package.name = faceapp
package.domain = org.example
source.dir = .
source.include_exts = py,html,png,jpg,kv,json,ttf,xml,csv
version = 1.0
requirements = flask==2.3.2,kivy==2.3.0,kivymd==1.1.1,requests==2.31.0,opencv-python==4.9.0.80,pandas==2.2.2,fpdf==1.7.2,apscheduler==3.10.4,pygame==2.5.2,edge-tts==6.1.8,numpy==1.26.4,android_webview==0.1.0
orientation = portrait
osx.python_version = 3
android.api = 33
android.minapi = 23
android.ndk = 23b
android.arch = armeabi-v7a,arm64-v8a
# Correct permissions for networking and camera
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, RECORD_AUDIO
# Add this line if your app needs to keep running in the background:
android.foreground = True
# Exclude unnecessary files
exclude_patterns = *.pyc,*.pyo,tmp*,.git,.github,*.md
# Icons (optional)
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[python]
# (empty, use the requirements above)
