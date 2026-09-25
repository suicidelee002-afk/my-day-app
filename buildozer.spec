[app]

title = My Day
package.name = myday
package.domain = org.myday

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1


[app:android]

android.api = 35
android.minapi = 21
android.ndk = 27c