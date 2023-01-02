del .\Patch-Debug\Locale_English-Root.wad
del .\Patch-Release\Locale_English-Root.wad
@echo off
rem 读取半汉化需要的文件列表
setlocal enabledelayedexpansion
set file_list=release_file_quick.txt
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
rem 复制打包好的全汉化到我的steam wiz游戏目录直接测试 此行可修改
copy .\Locale_English-Root.wad "D:\steam\steamapps\common\Wizard101\Data\GameData\"
