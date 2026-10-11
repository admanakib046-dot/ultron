import cv2
import pytesseract
from PIL import Image


class OCR:

    def __init__(self):

        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )

    def read(self, image_path):

        img = cv2.imread(image_path)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        gray = cv2.GaussianBlur(gray, (3,3), 0)

        thresh = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        cv2.imwrite("temp_ocr.jpg", thresh)

        image = Image.open("temp_ocr.jpg")

        text = pytesseract.image_to_string(
            image,
            config="--psm 6"
        )

        return text.strip()