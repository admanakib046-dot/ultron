import os
import pickle
import cv2
import numpy as np
from insightface.app import FaceAnalysis


class FaceRecognition:

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

    def recognize(self):

        camera = cv2.VideoCapture(0)

        while True:

            ret, frame = camera.read()

            if not ret:
                continue

            faces = self.app.get(frame)

            for face in faces:

                embedding = face.embedding

                best_name = "Unknown"
                best_score = -1

                for file in os.listdir(self.database):

                    if not file.endswith(".pkl"):
                        continue

                    with open(os.path.join(self.database, file), "rb") as f:
                        saved_embedding = pickle.load(f)

                    score = np.dot(saved_embedding, embedding) / (
                        np.linalg.norm(saved_embedding)
                        * np.linalg.norm(embedding)
                    )

                    if score > best_score:
                        best_score = score
                        best_name = file.replace(".pkl", "")

                if best_score < 0.45:
                    best_name = "Unknown"

                box = face.bbox.astype(int)

                x1, y1, x2, y2 = box

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    best_name,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

            cv2.imshow("Ultron Face Recognition", frame)

            if cv2.waitKey(1) == 27:
                break

        camera.release()
        cv2.destroyAllWindows()

    def get_current_user(self):
        """
        Temporary version used by Brain.

        Later this will analyze a live camera frame and
        return the recognized person's name.
        """

        files = []

        for file in os.listdir(self.database):

            if file.endswith(".pkl"):
                files.append(file.replace(".pkl", ""))

        if len(files) == 0:
            return None

        return files[0]