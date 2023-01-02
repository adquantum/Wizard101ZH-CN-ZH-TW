import os
# 读取版本号
with open('latest-version.txt', 'r') as f:
    version = f.read().strip()

# 分离版本号的各个部分
major, minor, patch = version.split('.')

# 将 patch 加 1
patch = str(int(patch) + 1)

# 满 15 进 1
if patch == '15':
    patch = '1'
    minor = str(int(minor) + 1)

# 更新版本号
new_version = '.'.join([major, minor, patch])

# 覆盖 latest-version.txt 文件
with open('latest-version.txt', 'w') as f:
    f.write(new_version)
# 读取输入的内容
input_text = input('请输入要写入的内容: ')
# 构建目标路径
dest_path = '/usr/local/toolWiz/public/file/debug/xx/'
dest_path = dest_path.replace('xx', new_version)
# 构建mark文件的路径
mark_path = '/usr/local/toolWiz/public/file/debug/xx/mark'
mark_path = mark_path.replace('xx', new_version)
# 创建目录
os.makedirs(dest_path, exist_ok=True)
# 写入输入的内容到mark文件中
with open(mark_path, 'w') as f:
    f.write(input_text)
# 复制文件
src_path = './Patch-Debug/Locale_English-Root.wad'
os.system(f'cp {src_path} {dest_path}')
# 构建目标路径
dest_path = '/usr/local/toolWiz/public/file/release/xx/'
dest_path = dest_path.replace('xx', new_version)
# 构建mark文件的路径
mark_path = '/usr/local/toolWiz/public/file/release/xx/mark'
mark_path = mark_path.replace('xx', new_version)
# 创建目录
os.makedirs(dest_path, exist_ok=True)
# 写入输入的内容到mark文件中
with open(mark_path, 'w') as f:
    f.write(input_text)
# 创建目录
os.makedirs(dest_path, exist_ok=True)
# 复制文件
src_path = './Patch-Release/Locale_English-Root.wad'
os.system(f'cp {src_path} {dest_path}')