# encoding=UTF-8
# Last modified: 2018.12.29

"""
    docstring
    2018.12.29 Copy code from jieba
        明天思考一下如何读取文档，并按照标点符号切割文本，生成test_sent，进行全篇分词
    2018.12.31 Create 'cut_word()'
        - 完成内容：（1）读文件'135.txt'，清洗数据
                  （2）创建新文件'135_分词后.txt'，分词并写入
        - 待完成项：（1）整理出适合教育政策的'userdict.text'
                  （2）对新创建文件'135_分词后.txt'做词频统计，看统计结果
                  （3）查一些词频可视化的代码或者软件
"""

import re
import jieba
from zhon.hanzi import punctuation

def cut_word():
    jieba.load_userdict("userdict.txt")

    input_file='input_data/135.txt'
    output_file='output_data/135_分词后.txt'
    test_text=""

    with open(input_file) as in_f,open(output_file, mode='a',encoding='utf-8') as out_f:

        for line_num, line in enumerate(in_f):  #清除中文标点、格式符号
            str=re.sub("[%s]+" %punctuation,"",line.strip())
            test_text=test_text+str

        seg_list = jieba.cut(test_text)     #分词

        out_f.seek(0)       #清空原文件，将分词结果写入文件
        out_f.truncate()
        out_f.write("\n".join(seg_list))

if __name__=='__main__':
    cut_word()


