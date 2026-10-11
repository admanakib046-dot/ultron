import os
import json


class ConversationMemory:

    def __init__(self):
        self.file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "conversations.json"
        )

        self.messages = []
        self.load()

    # -------------------------
    # Load Conversation
    # -------------------------

    def load(self):

        if os.path.exists(self.file):

            try:

                with open(self.file, "r", encoding="utf-8") as f:
                    self.messages = json.load(f)

            except Exception:

                self.messages = []

        else:

            self.messages = []

    # -------------------------
    # Save Conversation
    # -------------------------

    def save(self):

        os.makedirs(os.path.dirname(self.file), exist_ok=True)

        with open(self.file, "w", encoding="utf-8") as f:

            json.dump(
                self.messages,
                f,
                indent=4,
                ensure_ascii=False
            )

    # -------------------------
    # Add Message
    # -------------------------

    def add(self, role, message):

        self.messages.append({

            "role": role,
            "message": message

        })

        self.save()

    # -------------------------
    # Get Conversation
    # -------------------------

    def get(self):

        return self.messages

    # -------------------------
    # Last N Messages
    # -------------------------

    def last(self, count=10):

        return self.messages[-count:]

    # -------------------------
    # Clear Conversation
    # -------------------------

    def clear(self):

        self.messages = []

        self.save()