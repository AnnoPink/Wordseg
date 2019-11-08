from library import word_maker
import xlwt
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud,STOPWORDS

def count_word(input_file):
    output_file = input_file[:-4]+'_词频统计.xls'
    seg_dict={}
    book = xlwt.Workbook(encoding='utf-8')  # 创建Workbook，相当于创建Excel
    i = 0

    # 创建sheet，Sheet1为表的名字，cell_overwrite_ok为是否覆盖单元格
    sheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)

    with open(input_file) as in_f:

        for line in in_f.readlines():  # 读词seg，去除单个字，放入词典seg_dict中，统计词频
            seg=line.strip()
            if len(seg)<=1:
                continue
            if seg not in seg_dict:
                seg_dict[seg]=1
            else:
                seg_dict[seg]+=1

    order_dict=sorted(seg_dict.items(),key=lambda x:x[1],reverse=True)  # 将字典转化为列表从大到小排序


    for segtup in order_dict:  # 在文件中循环输出列表中元组
        sheet1.write(i,0,segtup[0])
        sheet1.write(i,1,str(segtup[1]))
        i = i+1

    # 保存为.xls文件
    book.save(output_file)

    return output_file

def cloud_word_test(filestr,inputfile):
    output_file=inputfile[:-4]+'.png'
    back_color=imread('images/rect.jpg')

    seg_list=word_maker.cut_word(filestr)
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