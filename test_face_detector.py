import cv2

from vision.face_detector import FaceDetector


camera = cv2.VideoCapture(0)

detector = FaceDetector()

while True:

    ret, frame = camera.read()

    if not ret:
        break

    faces = detector.detect(frame)

    detector.draw(frame, faces)

    cv2.imshow("Ultron Face Detector", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

camera.release()

cv2.destroyAllWindows()