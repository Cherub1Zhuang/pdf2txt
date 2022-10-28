# 导入工具包
import os
import re
from pdf2docx import parse
import docx2txt


def pdf_to_txt(pdf_name):
    # pdf_file="pdf\\"+pdf_name+".pdf"
    pdf_file=pdf_name+".pdf"
    docx_file="docx\\"+pdf_name+".docx"
    txt_file="txt\\"+pdf_name+".txt"
    parse(pdf_file,docx_file)

    text=docx2txt.process(docx_file)
    word_list=re.findall('[A-Za-z]{2,20}',text)

    with open(txt_file,"w",encoding="utf-8") as f3:
        for word in word_list:
            f3.write(word)
            f3.write(" ")

if __name__ == '__main__':
    if not os.path.exists("docx"):
        os.mkdir("docx")
    if not os.path.exists("txt"):
        os.mkdir("txt")
    path=os.getcwd()
    file_list=os.listdir(path)
    for file in file_list:
        if file.endswith(".pdf"):
            file_name=file[0:-4]
            print(file_name)
            pdf_to_txt(file_name)
    # pdf_to_txt("Attention Is All You Need")