import os
import textwrap
import subprocess
subprocess.run(["bash", "packup.sh"])
def get_multi_line_input():
    lines = []
    print("请输入版本更新的内容，输入完成后按两次回车结束输入:")
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return "\n".join(lines)

def get_dest_path(base_path, version):
    return base_path.replace('xx', version)

def write_mark_file(mark_path, input_text):
    with open(mark_path, 'w') as f:
        f.write(input_text)

def copy_and_write(src_path, dest_path, mark_path, input_text):
    # 复制文件
    os.system(f'cp {src_path} {dest_path}')
    # 写入输入的内容到mark文件中
    write_mark_file(mark_path, input_text)
def patch_push(mode):
    # 构建目标路径
    if mode == 'debug':
        base_path = '/usr/local/toolWiz/public/file/debug/xx/'
        src_path = './Patch-Debug/Locale_English-Root.wad'
    elif mode == 'release':
        base_path = '/usr/local/toolWiz/public/file/release/xx/'
        src_path = './Patch-Release/Locale_English-Root.wad'
    else:
        raise ValueError('Invalid mode')
    dest_path = get_dest_path(base_path, new_version)
    # 创建目录
    os.makedirs(dest_path, exist_ok=True)
    # 构建 mark 文件的路径
    mark_path = base_path.replace('xx', new_version) + 'mark'
    # 复制文件并写入内容到 mark 文件
    copy_and_write(src_path, dest_path, mark_path, input_text)


# 读取版本号
with open('latest-version.txt', 'r') as f:
    version = f.read().strip()

# 分离版本号的各个部分
major, minor, patch = version.split('.')

# 将 patch 加 1
patch = str(int(patch) + 1)

# 满 11 进 1
if patch == '11':
    patch = '1'
    minor = str(int(minor) + 1)

# 更新版本号
new_version = '.'.join([major, minor, patch])

# 覆盖 latest-version.txt 文件
with open('latest-version.txt', 'w') as f:
    f.write(new_version)

#读取输入的内容
input_text = get_multi_line_input()
# 调用 patch_push 函数发布补丁
patch_push('debug')
patch_push('release')
