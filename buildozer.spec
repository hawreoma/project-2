[app]

title = Vehicle Expert AI
package.name = vehicleexpertai
package.domain = org.hawrestack

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,npz

version = 1.0

requirements = python3,kivy==2.3.1,numpy==1.23.5,kivymd==1.2.0

presplash.filename = %(source.dir)s/data/presplash.png
icon.filename = %(source.dir)s/data/icon.png

orientation = portrait

osx.kivy_version = 2.2.0

fullscreen = 0

android.permissions = INTERNET
android.api = 34
android.minapi = 24
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.copy_libs = 1

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2

ios.codesign.allowed = false

[buildozer]

log_level = 2
warn_on_root = 1
