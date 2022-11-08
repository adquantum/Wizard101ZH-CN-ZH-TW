del .\Locale_English-Root.wad
del ..\Locale_English-Root.wad
wizwad pack Locale_English-Root.wad .\local
cd ..\

wizwad pack Locale_English-Root.wad .\Wizard101ZH-CN-ZH-TW\local_test

@Echo Off

Echo open 101.43.174.221 21 >ftp.up

Echo blaze>>ftp.up

Echo Lyuu0226@>>ftp.up


Echo binary>>ftp.up

Echo put "D:\wizproject\wiz汉化文件\Wizard101ZH-CN-ZH-TW\Locale_English-Root.wad">>ftp.up

Echo bye>>ftp.up

FTP -s:ftp.up

del ftp.up /q
