# -*- coding:utf-8*-
#python 合并同一个文件夹下所有PDF文件
#参考：https://blog.csdn.net/u013421629/article/details/77703582
#修改为在 3.6版本下可用

import os
from PyPDF2 import PdfFileReader,PdfFileWriter
import time
time1=time.time()


# 使用os模块walk函数，搜索出某目录下的全部pdf文件
######################获取同一个文件夹下的所有PDF文件名#######################
def getFileName(filepath):
    file_list = []
    for root,dirs,files in os.walk(filepath):
        for filespath in files:
            # print(os.path.join(root,filespath))
            file_list.append(os.path.join(root,filespath))

    return file_list



##########################合并同一个文件夹下所有PDF文件########################
def MergePDF(filepath,outfile):
    output=PdfFileWriter()
    outputPages=0
    pdf_fileName=getFileName(filepath)
    for each in pdf_fileName:
        print(each)
        # 读取源pdf文件
        input = PdfFileReader(each)

        # 如果pdf文件已经加密，必须首先解密才能使用pyPdf
        if input.isEncrypted == True:
            input.decrypt("map")

        # 获得源pdf文件中页面总数
        pageCount = input.getNumPages()
        outputPages += pageCount
        print(pageCount)

        # 分别将page添加到输出output中
        for iPage in range(0, pageCount):
            output.addPage(input.getPage(iPage))


    print("All Pages Number:"+str(outputPages))
    # 最后写pdf文件
    outputStream=file(filepath+outfile,"wb")
    output.write(outputStream)
    outputStream.close()
    print("finished")



if __name__ == '__main__':
    file_dir = r'D:/2/'
    out="合并文件.pdf"
    MergePDF(file_dir,out)
    time2 = time.time()
    print('总共耗时：' + str(time2 - time1) + 's')