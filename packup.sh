# 删除旧的打包文件
export PATH=$PATH:/www/server/python_manager/versions/3.10.0/bin
rm ./Patch-Debug/Locale_English-Root.wad
rm ./Patch-Release/Locale_English-Root.wad 
# 读取半汉化需要的文件列表
file_list="release_file_quick.txt"
sed -i 's/\r//' "${file_list}"
# 循环遍历文件列表
while read -r file; do
  # 执行覆盖操作
  cp "./Debug-Full-CN/Locale/English/${file}" "./Release-Half-CN/Locale/English/${file}"
done < "${file_list}"
# 进入Patch-Release目录
cd ./Patch-Release/ || exit
# 打包半汉化文件
wizwad pack Locale_English-Root.wad ../Release-Half-CN
# 返回上一级目录
cd ..
# 进入Patch-Debug目录
cd ./Patch-Debug/ || exit
# 打包半汉化文件
wizwad pack Locale_English-Root.wad ../Debug-Full-CN
