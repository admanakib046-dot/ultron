import cv2
import os
from datetime import datetime


class ImageCapture:

    def __init__(self):

        self.folder = "captures"

        os.makedirs(self.folder, exist_ok=True)

    def save(self, frame):

        filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")

        path = os.path.join(self.folder, filename)

        cv2.imwrite(path, frame)

        return path