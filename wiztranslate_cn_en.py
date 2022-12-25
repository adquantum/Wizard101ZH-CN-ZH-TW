def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False
file_list="D:/Downloads/file2.txt"
fl=open(file_list,encoding='utf-16 le')
fl = fl.read().splitlines()
for lang in fl[1::]:
  file_name=lang
  file_path="D:/wizproject/backup/Locale/English/"
  file_path2="D:/wizproject/wiz汉化文件/Wizard101ZH-CN-ZH-TW/Debug-Full-CN/Locale/English/"
  file=file_path + file_name
  file2=file_path2 +file_name
  f=open(file,encoding='utf-16 le')
  f2=open(file2,encoding='utf-16 le')
  f = f.read().splitlines()
  f2 = f2.read().splitlines()
  key=f2[1::3]
  value=f2[::3][1::]
  d =dict(zip(key,value))
#  for s_key in list(d.keys()):
 #  if not is_contains_chinese(d[s_key]):
  #   d.pop(s_key)
  for i in range(1,len(f),3):
    if f[i] in d:
      if i+2 <len(f):
        if d[f[i]].find('·') != -1:
          t = f[i+1]
          f[i+1]= f[i+2]
          f[i+2]= d[f[i]]+"/n"+f[i+2]
        else:
          t = f[i+1]
          f[i+1]= f[i+2]
          f[i+2]= d[f[i]]
      if f[i+1]==f[i+2]:
        f[i+1]=t
  with open(file2,'w',encoding='utf-16 le') as f1:
    for line in f:
      f1.write(line+'\n')
  print(file_name)

