import tkinter as tk 
import PyPDF2
import os


pdf_files = []
output_filename = 'merge.pdf'

for filename in os.listdir('.'):
    if filename.endswith(""):
        pdf_files.append(filename)
pdf_files.sort()
pdf_writer = PyPDF2.PdfWriter()

for filename in pdf_files:
    pdf_reader = PyPDF2.PdfReader(open(filename, 'rb'))
    for i in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(i))
with open(output_filename, 'wb') as f:
    pdf_writer.write(f)
