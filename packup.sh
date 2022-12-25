rm ./Patch-Debug/Locale_English-Root.wad
rm ./Patch-Release/Locale_English-Root.wad
cd ./Patch-Release/
wizwad pack Locale_English-Root.wad ../Release-Half-CN
cd ..
cd ./Patch-Debug/ 
wizwad pack Locale_English-Root.wad ../Debug-Full-CN
