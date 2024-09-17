import PyPDF2
import os

merger = PyPDF2.PdfMerger()

files_list = os.listdir('files')
files_list.sort()
print(files_list)

for pdf_file in files_list:
    if '.pdf' in pdf_file:
        merger.append(f'files/{pdf_file}')

merger.write('Final PDF.pdf')