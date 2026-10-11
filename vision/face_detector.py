import cv2
from insightface.app import FaceAnalysis


class FaceDetector:

    def __init__(self):

        self.app = FaceAnalysis(
            name="buffalo_l",
            providers=["CPUExecutionProvider"]
        )

        self.app.prepare(
            ctx_id=0,
            det_size=(640, 640)
        )

    def detect(self, frame):

        faces = self.app.get(frame)

        return faces

    def draw(self, frame, faces):

        for face in faces:

            box = face.bbox.astype(int)

            x1, y1, x2, y2 = box

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0,255,0),
                2
            )

            score = face.det_score

            cv2.putText(
                frame,
                f"{score:.2f}",
                (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0,255,0),
                2
            )

        return frame