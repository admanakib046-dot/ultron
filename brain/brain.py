from memory.memory import Memory
from memory.memory_detector import MemoryDetector
from brain.planner import planner
from vision.face_recognition import FaceRecognition


class Brain:

    def __init__(self):

        self.memory = Memory()
        self.detector = MemoryDetector()
        self.planner = planner()
        self.face = FaceRecognition()

    def identify_user(self):

        try:
            return self.face.get_current_user()
        except:
            return None

    def process(self, text):

        lower = text.lower()

        # -------------------------
        # Face Recognition
        # -------------------------

        user = self.identify_user()

        if user:
            print(f"Welcome back {user}!")

        # -------------------------
        # Remember
        # -------------------------

        if self.detector.should_remember(text):

            if "my name is" in lower:

                name = text.split("is", 1)[1].strip()

                self.memory.remember(
                    "name",
                    name,
                    "profile",
                    10
                )

                return f"I'll remember your name is {name}."

        # -------------------------
        # Recall
        # -------------------------

        if "what is my name" in lower or "who am i" in lower:

            name = self.memory.recall("name")

            if name:
                return f"Your name is {name}"

            return "I don't know your name yet."

        # -------------------------
        # Planner
        # -------------------------

        task = self.planner.plan(text)

        if task != "ai":
            return f"Planner selected: {task}"

        return "I don't understand yet."