from library import word_maker
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud,STOPWORDS

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