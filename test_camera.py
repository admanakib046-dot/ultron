import cv2
from vision.camera import Camera

camera = Camera()
camera.open()

print("Camera opened. Press Q to quit.")

while True:
    frame = camera.read()

    if frame is None:
        break

    cv2.imshow("Ultron Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.close()