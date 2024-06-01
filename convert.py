from pdf2image import convert_from_path
import pytesseract
from docx import Document
import os

# Função para converter PDF para imagens
def pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    return images

# Função para extrair texto de imagens usando pytesseract
def extract_text_from_images(images):
    text = ""
    for i, image in enumerate(images):
        image_text = pytesseract.image_to_string(image, lang='por')  # Usando 'por' para português
        text += f"--- Página {i + 1} ---\n"
        text += image_text + "\n"
    return text

# Função para salvar texto em um arquivo Word
def save_text_to_word(text, output_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)

def main(pdf_path, output_path):
    images = pdf_to_images(pdf_path)
    text = extract_text_from_images(images)
    save_text_to_word(text, output_path)
    print(f"Texto extraído e salvo em {output_path}")

# Caminho do PDF de entrada e do arquivo Word de saída
pdf_path = '31-05 Visitação de Nossa Senhora.pdf.pdf'
output_path = 'texto_extraido.docx'

# Executar o processo
main(pdf_path, output_path)
