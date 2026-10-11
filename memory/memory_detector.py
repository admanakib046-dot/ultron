import re


class MemoryDetector:

    def should_remember(self, text):

        text = text.lower()

        keywords = [
            "my name is",
            "i am",
            "i'm",
            "my birthday",
            "my favorite",
            "i like",
            "i live",
            "my email",
            "my phone"
        ]

        return any(k in text for k in keywords)