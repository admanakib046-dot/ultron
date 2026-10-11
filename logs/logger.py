from datetime import datetime
import os


class Logger:

    def __init__(self):

        os.makedirs("logs", exist_ok=True)

    def log(self, category, message):

        today = datetime.now().strftime("%Y-%m-%d")

        filename = f"logs/{today}.log"

        with open(filename, "a", encoding="utf-8") as file:

            time = datetime.now().strftime("%H:%M:%S")

            file.write(
                f"[{time}] [{category}] {message}\n"
            )