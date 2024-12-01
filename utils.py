import os
import PyPDF2
from pdfminer.high_level import extract_text

def extract_text_to_list_pydf2(parent_path):
    pdf_list = []
    for filename in os.listdir(parent_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(parent_path, filename)

            with open(pdf_path) as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                text = ''

                for page in reader.pages:
                    text += page.extract_text() + "\n"
            pdf_list.append(text.strip())
    return pdf_list

def extract_text_to_list_pdfminer(parent_path):
    pdf_list = []
    for filename in os.listdir(parent_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(parent_path, filename)
            text = extract_text(pdf_path)
            pdf_list.append(text.strip())
    return pdf_list