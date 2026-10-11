import cv2


class Camera:

    def __init__(self):

        self.camera = None

    def open(self):

        self.camera = cv2.VideoCapture(0)

        if not self.camera.isOpened():
            raise Exception("Unable to open camera.")

    def read(self):

        if self.camera is None:
            return None

        success, frame = self.camera.read()

        if not success:
            return None

        return frame

    def close(self):

        if self.camera is not None:
            self.camera.release()

        cv2.destroyAllWindows()