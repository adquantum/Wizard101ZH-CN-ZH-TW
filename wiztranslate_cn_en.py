# is_contains_chinese 函数用于判断给定字符串中是否包含中文字符
def is_contains_chinese(strs):
    # 遍历字符串中的每一个字符
    for _char in strs:
        # 如果字符的 Unicode 编码在中文字符的范围内，则返回 True
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    # 如果字符串中没有中文字符，则返回 False
    return False
def fix_italics(line):
  if "<ITALICS>" in line and "</ITALICS>" not in line:
      fixed_line = line + "</ITALICS>"
  elif "</ITALICS>" in line and "<ITALICS>" not in line:
      fixed_line = "<ITALICS>" + line            
  else:
      fixed_line = line
  return fixed_line

# 读取文件列表
file_list = "./file.txt"
fl = open(file_list, encoding='utf-16 le')
fl = fl.read().splitlines()

# 循环遍历文件列表
for lang in fl[1::]:
    # 获取文件名
    file_name = lang

    # 定义文件路径
    file_path = "./Original-English/Locale/English/"
    file_path2 = "./Debug-Full-CN/Locale/English/"

    # 拼接文件路径
    file = file_path + file_name
    file2 = file_path2 + file_name

    # 读取文件内容
    f = open(file, encoding='utf-16 le')
    f2 = open(file2, encoding='utf-16 le')
    f = f.read().splitlines()
    f2 = f2.read().splitlines()

    # 获取文件中的键和值
    key = f2[1::3]
    value = fix_italics(f2[::3][1::])
    for i, line in enumerate(value):
        value[i] = fix_italics(line)

    # 将键值对组成字典
    d = dict(zip(key, value))

    # 遍历字典的键
    for s_key in list(d.keys()):
        # 如果字典中的值不包含中文字符或 "$All_Enemies_Wide_image$"，则将该键从字典中删除
        if not is_contains_chinese(d[s_key]) and "$All_Enemies_Wide_image$" not in d[s_key]:
            d.pop(s_key)


    # 遍历第一个文件的列表

    for i in range(1,len(f),3):
      if f[i] in d:
        if i+2 <len(f):
          t = f[i+1]
          f[i+1]= f[i+2]
          f[i+2]= d[f[i]]
        if f[i+1]==f[i+2]:
          f[i+1]=t
    with open(file2, 'w', encoding='utf-16 le', newline='\r\n') as f1:
        for line in f:
            f1.write(line+'\n')

    print(file_name)

