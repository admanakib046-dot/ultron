from vision.camera import Camera
from vision.image_capture import ImageCapture
from vision.ocr import OCR

from brain.vision_reader import VisionReader


class VisionManager:

    def __init__(self):

        self.camera = Camera()
        self.capture = ImageCapture()
        self.ocr = OCR()

        self.reader = VisionReader()

    def capture_image(self):

        self.camera.open()

        frame = self.camera.read()

        filename = self.capture.save(frame)

        self.camera.close()

        return filename

    def read_text(self):

        image = self.capture_image()

        return self.ocr.read(image)
    def understand_text(self):

        text = self.read_text()

        return self.reader.understand(text)