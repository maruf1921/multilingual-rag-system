import pytesseract
from pdf2image import convert_from_path
import os


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

def pdf_to_text_ocr(pdf_path, output_txt_path, dpi=300):
    print("Converting PDF pages to images...")
    pages = convert_from_path(pdf_path, dpi=dpi)
    print(f"Total pages: {len(pages)}")

    full_text = ""
    for i, page in enumerate(pages):
        print(f"Performing OCR on page {i+1}...")
        text = pytesseract.image_to_string(page, lang='ben+eng')  # Bengali + English
        full_text += text + "\n"

    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"OCR completed. Extracted text saved to {output_txt_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    pdf_file = os.path.join(base_dir, "data", "hsc26_bangla1.pdf")
    output_file = os.path.join(base_dir, "data", "raw_text.txt")

    pdf_to_text_ocr(pdf_file, output_file)
