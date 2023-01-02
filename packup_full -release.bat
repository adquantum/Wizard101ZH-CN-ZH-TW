rem 删除旧版本的全汉化和半汉化
del .\Patch-Debug\Locale_English-Root.wad
del .\Patch-Release\Locale_English-Root.wad
@echo off
rem 读取半汉化需要的文件列表
setlocal enabledelayedexpansion
set file_list=release_file.txt
for /f "tokens=*" %%f in (%file_list%) do (
set file=%%f
rem 执行覆盖操作
xcopy .\Debug-Full-CN\Locale\English\!file! .\Release-Half-CN\Locale\English\!file! /Y
)

cd .\Patch-Release\
rem 打包半汉化
wizwad pack Locale_English-Root.wad ..\Release-Half-CN
cd ..\
cd .\Patch-Debug\ 
rem 打包全汉化
wizwad pack Locale_English-Root.wad ..\Debug-Full-CN

copy .\Locale_English-Root.wad "D:\steam\steamapps\common\Wizard101\Data\GameData\"