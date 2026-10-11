from vision.ocr import OCR

ocr = OCR()

path = input("Image path: ")

text = ocr.read(path)

print("\nDetected Text:\n")
print(text)