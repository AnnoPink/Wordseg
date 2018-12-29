# encoding=UTF-8
# Last modified: 2018.12.29

"""
    docstring
    2018.12.29 Copy code from jieba
                明天思考一下如何读取文档，并按照标点符号切割文本，生成test_sent，进行全篇分词
"""
import jieba

jieba.load_userdict("userdict.txt")

test_sent="国家教育事业发展“十三五”规划，“十三五”时期是全面建成小康社会决胜阶段。为加快推进教育现代化，依据《中华人民共和国国民经济和社会发展第十三个五年规划纲要》和《国家中长期教育改革和发展规划纲要（2010—2020年）》（以下简称《教育规划纲要》），制定本规划。"

seg_list=jieba.cut(test_sent,cut_all=True)
print("Full Mode:"+"/".join(seg_list)) #全模式

seg_list=jieba.cut(test_sent,cut_all=False)
print("Default Mode:"+"/".join(seg_list)) #精确模式

seg_list=jieba.cut(test_sent) #默认是精确模式
print(",".join(seg_list))

seg_list=jieba.cut_for_search(test_sent) #搜索引擎模式
print(",".join(seg_list))

