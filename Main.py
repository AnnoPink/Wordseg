# encoding=UTF-8
# Last modified: 2018.12.29

"""
    Wordseg0.0 Docstring

    `format_text()`     用于格式化文本，返回字符串

    `cut_word()`        用于分词，返回列表

    `store_word`()      用于存储分词结果，返回输出路径

    `count_word()`      用于词频统计，返回输出路径

    `cloud_word_test()` 用于画词云，返回输出路径
"""

import re
import jieba
import matplotlib.pyplot as plt
from scipy.misc import imread
from zhon.hanzi import punctuation
from wordcloud import WordCloud,STOPWORDS

def format_text(filestr):
    input_file = 'input_data/' + filestr + '.txt'
    textstr = ""

    with open(input_file) as in_f:
        for line_num, line in enumerate(in_f):  # 清除中文标点、格式符号
            str = re.sub("[%s]+" % punctuation, "", line.strip())
            textstr = textstr + str

    return textstr

def cut_word(filestr):
    jieba.load_userdict('input_data/userdict.txt')   #自定义字典
    text=format_text(filestr)
    seg_list = jieba.cut(text)   #分词

    return seg_list

def store_word(filestr,joinstr,seg_list):
    output_file = 'output_data/' + filestr + '.txt'

    with open(output_file, mode='a',encoding='utf-8') as out_f:
        out_f.seek(0)       #清空原文件，将分词结果写入文件
        out_f.truncate()
        out_f.write(joinstr.join(seg_list))

    return output_file

def count_word(input_file):
    output_file = input_file[:-4]+'_词频统计.txt'
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

    return output_file

def cloud_word_test(filestr,inputfile):
    output_file=inputfile[:-4]+'.png'
    back_color=imread('images/rect.jpg')

    seg_list=cut_word(filestr)
    seg_text=' '.join(seg_list)

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
    wc.to_file(output_file)

    return output_file


if __name__=='__main__':
    textname='15'
    re_textname=textname+'_分词'

    seg_list=cut_word(textname)
    seg_textpath=store_word(re_textname,'\n',seg_list)
    count_word(seg_textpath)
    cloud_word_test(textname,seg_textpath)

