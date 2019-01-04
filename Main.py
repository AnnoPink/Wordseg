# encoding=UTF-8
# Last modified: 2018.12.29

"""
    docstring
    2018.12.29 Copy code from jieba
        明天思考一下如何读取文档，并按照标点符号切割文本，生成test_sent，进行全篇分词
    2018.12.31 Create 'cut_word()'
        - 完成内容：（1）读文件'135.txt'，清洗数据
                  （2）创建新文件'135_分词后.txt'，分词并写入

        - 待完成项：（1）整理出适合教育政策的'userdict.txt'
                  （2）对新创建文件'135_分词后.txt'做词频统计，看统计结果                  √2019.1.1
                  （3）查一些词频可视化的代码或者软件                                    √2019.1.3

    2019.1.1  Create  'count_word()'
        - 完成内容：（1）对新创建文件'135_分词后.txt'做词频统计

        - 待完成项：（1）修改'count_word()'中频数排序部分及写入代码（抄来的，太繁琐）         √2019.1.2
                  （2）修改'cut_word()'\'count_word()'，想办法用string传递读写文件名。
                      分词结果和文件的存储要分开，才三个函数已经要重复分词两遍。
                      jieba分词结果貌似只能join一次seg_list，并不懂为什么？

    2019.1.2  Fix 'count_word()'
        - 完成内容：（1）简化'count_word()'，3行替换7行，开心！
                  （2）搞清楚"序列（列表，元组）和字典"的区别

    2019.1.3  Create  'word_cloud_test()'
        - 完成内容：（1）懵懵地把词云做出来了，基本流程知道。还需要更进一步了解，出来的图很丑。。。。
        - 待完成项：（1）考虑一下如何给词频统计后的词做词云
                  （2）修改一下word_cloud_test()，好乱
"""

import re
import jieba
import matplotlib.pyplot as plt
from scipy.misc import imread
from zhon.hanzi import punctuation
from wordcloud import WordCloud,STOPWORDS

def cut_word():
    jieba.load_userdict('input_data/userdict.txt')

    input_file='input_data/135.txt'
    output_file1='output_data/135_分词后.txt'
    test_text=""

    with open(input_file) as in_f,open(output_file1, mode='a',encoding='utf-8') as out_f1:

        for line_num, line in enumerate(in_f):  #清除中文标点、格式符号
            str=re.sub("[%s]+" %punctuation,"",line.strip())
            test_text=test_text+str

        seg_list = jieba.cut(test_text)     #分词

        out_f1.seek(0)       #清空原文件，将分词结果写入文件
        out_f1.truncate()
        out_f1.write("\n".join(seg_list))


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

        order_dict=sorted(seg_dict.items(),key=lambda x:x[1],reverse=True)  #将字典转化为列表从大到小排序
        for segtup in order_dict:  #在文件中循环输出列表中元组
            out_f.write(segtup[0]+'\t'+str(segtup[1])+'\n')


def cloud_word_test():
    back_color=imread('images/rect.jpg')

    with open('input_data/135.txt') as f:
        text=f.read()
        word_generator=jieba.cut(text,cut_all=False)
        seg_text=' '.join(word_generator)

    wc = WordCloud(background_color='white',
                   max_words=1000,
                   mask=back_color,
                   max_font_size=130,
                   min_font_size=8,
                   stopwords=STOPWORDS,
                   font_path='font/ChangFangSong.ttf',
                   random_state=42).generate(seg_text)

    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    wc.to_file('output_data/135.png')


if __name__=='__main__':
    cut_word()
    count_word()
    cloud_word_test()


