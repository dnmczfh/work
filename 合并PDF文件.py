# -*- coding:utf-8 -*-

from PyPDF2 import PdfFileReader, PdfFileWriter,PdfFileMerger
import os
#如果不能合并，原因是PDF文件的编码格式不是utf-8

REPORT_PDF_PATH = r'D:\2\doc'
os.chdir(REPORT_PDF_PATH)

def mergePdf(inFileList, outFile):
    '''
    合并文档
    :param inFileList: 要合并的文档的 list
    :param outFile:    合并后的输出文件
    :return:
    '''
    pdf_merger = PdfFileMerger()
    for inFile in inFileList:
        # 依次追加到合并文件
        pdf_merger.append(PdfFileReader(inFile, strict=True))
    # 最后,统一写入到输出文件中
    pdf_merger.write(outFile)


filenames = ['2.pdf', '2.pdf', '3.pdf']
mergePdf(filenames,'4.pdf')





