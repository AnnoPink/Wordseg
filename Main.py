# encoding=UTF-8
# Last modified: 2018.12.29

"""
    Wordseg0.0.1 Docstring

    `get_text`          用于将多个txt文本合并为一个文本

    `format_text()`     用于格式化文本，返回字符串

    `cut_word()`        用于分词，返回列表

    `store_word`()      用于存储分词结果，返回输出路径

    `count_word()`      用于词频统计，存储到excel表中，返回输出路径

    `cloud_word_test()` 用于画词云，返回输出路径
"""

from library import in_out,word_maker,word_show


if __name__=='__main__':
    textname = 'all'
    re_textname = textname+'_分词'
    Path = 'input_data/'

    in_out.get_text(Path, textname)

    seg_list=word_maker.cut_word(textname)
    seg_textpath=word_maker.store_cutword(re_textname,'\n',seg_list)

    word_show.count_word(seg_textpath)
    word_show.cloud_word_test(textname,seg_textpath)


