import re
import jieba
from zhon.hanzi import punctuation



def format_text(filestr):
    input_file = 'output_data/' + filestr + '.txt'
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

def store_cutword(filestr,joinstr,seg_list):
    output_file = 'output_data/' + filestr + '.txt'


    with open(output_file, mode='a',encoding='utf-8') as out_f:
        out_f.seek(0)       #清空原文件，将分词结果写入文件
        out_f.truncate()
        out_f.write(joinstr.join(seg_list))

    return output_file