from vision.image_capture import ImageCapture

capture = ImageCapture()

path = capture.capture()

print("Saved:", path)