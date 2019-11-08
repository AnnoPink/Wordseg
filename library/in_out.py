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
    book = xlwt.Workbook(encoding='utf-8') # 创建Workbook，相当于创建Excel

    # 创建sheet，Sheet1为表的名字，cell_overwrite_ok为是否覆盖单元格
    sheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)

    # 将数据存入excel中
    sheet1.write(0,0,'Englishname')
    sheet1.write(1,0,'Hellen')
    sheet1.write(0,1,'中文名字')
    sheet1.write(1,1,'海伦')

    # 保存为.xls文件
    book.save('1.xls')
