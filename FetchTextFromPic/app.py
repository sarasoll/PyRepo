from PIL import Image

import pytesseract
#I face a problem in installing the "pytesseract" but you can find the solve in the README file 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print(pytesseract.image_to_string(Image.open('PicName.PNG')))
