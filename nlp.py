import re
import jieba
from jieba import posseg

# 读取原文和译文文件
with open('Debug-Full-CN/Locale/English/WizQst13D4F.lang',encoding='utf-16 le') as f:
# 将文件中的内容按行分割
    f=f.read().splitlines()
    lines_en = f[2::3]
    lines_zh = f[::3][1::]

# 创建专有名词字典
noun_dict = {}
# 遍历每一行
for line_en, line_zh in zip(lines_en, lines_zh):
    # 使用正则表达式匹配英文专有名词
    noun_phrase = re.findall(r'[A-Z][a-z]+', line_en)
    # 如果匹配到了专有名词
    if noun_phrase:
        # 对中文进行分词和词性标注
        words_zh = posseg.lcut(line_zh)
        # 遍历每一个词
        for word, pos in words_zh:
            # 判断词性是否为专有名词
            if pos == 'nz':
                # 将专有名词添加到字典中，对应的值为对应的译文
                noun_dict[noun_phrase[0]] = word
                break
# 打印字典
print(noun_dict)
