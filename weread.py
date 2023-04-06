import tkinter as tk
from tkinter import filedialog
import PyPDF2
import os

class PDFMerge:
    def __init__(self):
        self.pdf_files = []

        self.root = tk.Tk()
        self.root.title('WeRead')

        self.add_button = tk.Button(self.root, text='Add files', command=self.add_button)
        self.add_button.pack(pady=10)


        self.merge_button = tk.Button(self.root, text='Merge files', command=self.merge_pdf)
        self.merge_button.pack(pady=10)

        self.status_label = tk.Label(self.root, text='No PDFs added')
        self.status_label.pack()

        self.root.mainloop()
    def add_button(self):
        pdf_files = filedialog.askopenfilenames(filetypes=[('PDF files', '*.pdf')])
        if pdf_files:
            self.pdf_files.extend(pdf_files)
            self.status_label.config(text=f'{len(self.pdf_files)} PDFs added')
    def merge_pdf(self):
        if not self.pdf_files:
            self.status_label.config(text='No PDFs added')
            return
        self.pdf_files.sort()
        pdf_writer = PyPDF2.PdfFileWriter()

        for filename in self.pdf_files:
            pdf_reader = PyPDF2.PdfReader(open(filename,'rb'))
            for i in range(pdf_reader.gerNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(i))

        output_filename = 'merged.pdf'
        with open(output_filename, 'wb') as f:
            pdf_writer(f)
        self.status_label.config(text=f'{len(self.pdf_files)} PDFs merged to {output_filename}')
if __name__ == "__main__":
    PDFMerge()