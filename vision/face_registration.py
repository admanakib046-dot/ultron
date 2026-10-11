import os
import pickle
import cv2
from insightface.app import FaceAnalysis


class FaceRegistration:

    def __init__(self):

        self.database = "vision/faces"

        os.makedirs(self.database, exist_ok=True)

        self.app = FaceAnalysis(
            name="buffalo_l",
            providers=["CPUExecutionProvider"]
        )

        self.app.prepare(
            ctx_id=0,
            det_size=(640, 640)
        )

    def register(self, name):

        camera = cv2.VideoCapture(0)

        print("================================")
        print(" Face Registration")
        print("================================")
        print("Press SPACE to capture your face")
        print("Press ESC to cancel")

        while True:

            ret, frame = camera.read()

            if not ret:
                continue

            cv2.imshow("Ultron Face Registration", frame)

            key = cv2.waitKey(1)

            if key == 27:
                camera.release()
                cv2.destroyAllWindows()
                return False

            if key == 32:

                faces = self.app.get(frame)

                if len(faces) == 0:
                    print("No face detected. Try again.")
                    continue

                face = faces[0]

                embedding = face.embedding

                filename = os.path.join(
                    self.database,
                    f"{name}.pkl"
                )

                with open(filename, "wb") as f:
                    pickle.dump(embedding, f)

                camera.release()
                cv2.destroyAllWindows()

                print(f"{name} registered successfully!")

                return True