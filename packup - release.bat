del .\Patch-Debug\Locale_English-Root.wad
del .\Patch-Release\Locale_English-Root.wad
cd .\Patch-Release\
wizwad pack Locale_English-Root.wad ..\local
cd ..\
cd .\Patch-Debug\ 
wizwad pack Locale_English-Root.wad ..\local_test

copy .\Locale_English-Root.wad "D:\steam\steamapps\common\Wizard101\Data\GameData\"
@Echo Off

Echo open 101.43.174.221 21 >ftp.up

Echo blaze>>ftp.up

Echo Lyuu0226@>>ftp.up


Echo binary>>ftp.up

Echo put "D:\wizproject\wiz汉化文件\Wizard101ZH-CN-ZH-TW\\Patch-Release\Locale_English-Root.wad">>ftp.up

Echo bye>>ftp.up

FTP -s:ftp.up

del ftp.up /q
