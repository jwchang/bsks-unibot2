import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

data_folder = 'data'
output_file = 'output.txt'

all_text = ''

for filename in os.listdir(data_folder):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(data_folder, filename)cd 
        text = extract_text_from_pdf(pdf_path)
        all_text += f'===== {filename} =====\n{text}\n'

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(all_text)

print(f'Text extracted from PDFs and saved to {output_file}')

