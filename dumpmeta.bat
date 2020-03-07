@echo off
setlocal enabledelayedexpansion

for /r %%f in (*.apk) do (
	(aapt dump badging "%%f") > %%f.yml
)