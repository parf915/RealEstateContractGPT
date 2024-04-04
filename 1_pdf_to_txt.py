import os
import fitz  # PyMuPDF for handling PDF files
import pytesseract  # OCR library
from PIL import Image  # Python Imaging Library for image processing
import re  # Regular expressions library

# Path to the tesseract executable. This needs to be set for pytesseract.
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

def contiene_palabra(texto, palabra):
    """
    Check if a specific word exists in the text, ignoring case sensitivity.
    :param texto: The text to search within.
    :param palabra: The word to search for.
    :return: True if the word exists in the text; False otherwise.
    """
    return re.search(r'\b' + re.escape(palabra) + r'\b', texto, re.IGNORECASE) is not None

def extraer_texto_de_pagina(pagina):
    """
    Extracts text from a PDF page. If no text is extractable, attempts OCR on the page's images.
    :param pagina: The PDF page from which to extract text.
    :return: Extracted text as a string.
    """
    texto_pagina = pagina.get_text()
    if texto_pagina.strip() != "":
        return texto_pagina
    else:
        texto_imagen = ""
        for img_index in range(len(pagina.get_images(full=True))):
            xref = pagina.get_images(full=True)[img_index][0]
            pix = fitz.Pixmap(pagina.parent, xref)
            if pix.n < 5:  # Exclude CMYK images and images with transparency
                pix = fitz.Pixmap(fitz.csRGB, pix)
            imagen = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            texto_imagen += pytesseract.image_to_string(imagen)
            pix = None  # Free resources
        return texto_imagen

def procesar_pdfs_en_carpeta(carpeta_pdf, carpeta_destino, palabra_clave):
    """
    Processes all PDF files in a specified directory, extracting text and saving it to new text files.
    :param carpeta_pdf: Directory containing PDF files to process.
    :param carpeta_destino: Destination directory for the extracted text files.
    :param palabra_clave: A keyword to search for in the PDFs (currently not used in the script).
    """
    for archivo in os.listdir(carpeta_pdf):
        if archivo.lower().endswith(".pdf"):
            ruta_pdf = os.path.join(carpeta_pdf, archivo)
            texto_acumulado = ""

            with fitz.open(ruta_pdf) as doc:
                for pagina in doc:
                    texto_pagina = extraer_texto_de_pagina(pagina)
                    texto_acumulado += texto_pagina

            nombre_archivo_texto = f"{os.path.splitext(archivo)[0]}.txt"
            ruta_archivo_texto = os.path.join(carpeta_destino, nombre_archivo_texto)
            
            with open(ruta_archivo_texto, 'w', encoding='utf-8') as archivo_texto:
                archivo_texto.write(texto_acumulado)
            print(f"Complete text saved in {ruta_archivo_texto}")

# Specify the directory containing your PDF files
carpeta_pdf = '/Users/renzo/Downloads/divorcios'

# Specify the destination directory for the extracted text files
carpeta_destino = '/Users/renzo/Downloads/divorcios_txt'

# Process the PDFs in the specified directory
procesar_pdfs_en_carpeta(carpeta_pdf, carpeta_destino, palabra_clave)
