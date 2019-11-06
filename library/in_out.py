import os
import xlwt

def get_text(in_Path,filestr):
    out_txt = 'output_data/' + filestr + '.txt'
    txtLists = os.listdir(in_Path)  # 列出文件夹下所有的目录与文件

    with open(out_txt, mode='a', encoding='utf-8') as out_f:
        out_f.seek(0)  # 清空原文件，将分词结果写入文件
        for txt in txtLists:
            print(txt)
            with open(in_Path+txt) as in_f:
                out_f.write(in_f.read())

def write_file():
    book = xlwt.Workbook(encoding='utf-8')