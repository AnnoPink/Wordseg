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
                  （2）对新创建文件'135_分词后.txt'做词频统计，看统计结果  √2019.1.1
                  （3）查一些词频可视化的代码或者软件
    2019.1.1  Create  'count_word()'
        - 完成内容：（1）对新创建文件'135_分词后.txt'做词频统计
        - 待完成项：（1）修改'count_word()'中频数排序部分及写入代码（抄来的，太繁琐https://blog.csdn.net/u014070086/article/details/73201590）
                  （2）看《十三五教育规划》，整理出一版'userdict.text'
                  （3）修改'cut_word()'\'count_word()'，想办法用string传递读写文件名
"""

import re
import jieba
from zhon.hanzi import punctuation

def cut_word():
    jieba.load_userdict("userdict.txt")

    input_file='input_data/135.txt'
    output_file='output_data/135_分词后.txt'
    test_text=""
    words=[]

    with open(input_file) as in_f,open(output_file, mode='a',encoding='utf-8') as out_f:

        for line_num, line in enumerate(in_f):  #清除中文标点、格式符号
            str=re.sub("[%s]+" %punctuation,"",line.strip())
            test_text=test_text+str

        seg_list = jieba.cut(test_text)     #分词

        out_f.seek(0)       #清空原文件，将分词结果写入文件
        out_f.truncate()
        out_f.write("\n".join(seg_list))


def count_word():
    input_file = 'output_data/135_分词后.txt'
    output_file = 'output_data/135_分词后_词频统计.txt'
    seg_dict={}
    with open(input_file) as in_f, open(output_file, mode='a', encoding='utf-8') as out_f:
        out_f.seek(0)
        out_f.truncate()

        for line in in_f.readlines():  #读词seg，去除单个字，放入词典seg_dict中，统计词频
            seg=line.strip()
            if len(seg)<=1:
                continue
            if seg not in seg_dict:
                seg_dict[seg]=1
            else:
                seg_dict[seg]+=1

        order_dict=list(seg_dict.values())  #按频数从大到小排序，写入135_分词后_词频统计.txt中
        order_dict.sort(reverse=True)

        for i in range(len(order_dict)):
            for keyseg in seg_dict:
                if seg_dict[keyseg]==order_dict[i]:
                    out_f.write(keyseg + '   ' + str(seg_dict[keyseg]) + '\n')
                    seg_dict[keyseg]=0



if __name__=='__main__':
    cut_word()
    count_word()


