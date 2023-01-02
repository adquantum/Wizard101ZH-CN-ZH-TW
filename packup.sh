rm ./Patch-Debug/Locale_English-Root.wad
rm ./Patch-Release/Locale_English-Root.wad
# 读取半汉化需要的文件列表
file_list="release_file_quick.txt"

# 循环遍历文件列表
while read -r file; do
  # 执行覆盖操作
  cp "./Debug-Full-CN/Locale/English/${file}" "./Release-Half-CN/Locale/English/${file}"
done < "${file_list}"
cd ./Patch-Release/
#打包半汉化文件
wizwad pack Locale_English-Root.wad ../Release-Half-CN
cd ..
cd ./Patch-Debug/ 
wizwad pack Locale_English-Root.wad ../Debug-Full-CN
