import os
import pickle


class FaceDatabase:

    def __init__(self):

        self.database = "vision/faces"

        os.makedirs(self.database, exist_ok=True)

    def get_people(self):

        people = []

        for file in os.listdir(self.database):

            if file.endswith(".pkl"):
                people.append(file.replace(".pkl", ""))

        return people

    def exists(self, name):

        return os.path.exists(
            os.path.join(self.database, f"{name}.pkl")
        )

    def delete(self, name):

        file = os.path.join(
            self.database,
            f"{name}.pkl"
        )

        if os.path.exists(file):
            os.remove(file)
            return True

        return False

    def load_embedding(self, name):

        file = os.path.join(
            self.database,
            f"{name}.pkl"
        )

        if not os.path.exists(file):
            return None

        with open(file, "rb") as f:
            return pickle.load(f)