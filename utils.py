import os
import PyPDF2

def extract_text_from_pdf(parent_path):
    pdf_list = []
    for filename in os.listdir(parent_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(parent_path, filename)

            with open(pdf_path) as pdf_file:
                reader = PyPDF2.PdfReader(pdf_path)
                text = ''

                for page in reader.pages:
                    text += page.extract_text + "\n"
            pdf_list.append(text.strip())
    return pdf_list