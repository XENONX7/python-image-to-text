import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"   #PAY SPECIAL ATTENTION ON THIS.THIS SHOULD BE RIGHT.

img = cv2.imread('yourimage.png')

print(pytesseract.image_to_string(img))
