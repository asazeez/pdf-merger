from PyPDF2 import PdfWriter
import os
import sys

files = []

def pdf_merger():
    merger = PdfWriter()
    for pdf in files:
        try:
            merger.append(pdf)
        except:
            print ("file not found")
    merger.write("merged-pdf.pdf")
    print ("files merged!")
    merger.close()

def get_files ():
    ans = input("Enter file name ")
    while (ans!='exit'):
        files.append(ans)
        print(files)
        ans = input("Enter file name ")
    return files

def get_direct ():
    answer = input(" ")
    try:
        os.chdir(answer)
        print(os.getcwd())
    except:
        print("Directory does not exist")

def rename_file():
    answer = input ("Rename file ")
    if (answer=='yes'):
        ans = input ("Enter file name ")
        try:
            os.rename('merged-pdf.pdf',ans)
        except:
            print("invalid file name")


get_direct()
get_files()
pdf_merger()
rename_file()