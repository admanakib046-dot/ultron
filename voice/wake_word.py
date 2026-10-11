class WakeWord:

    def __init__(self):

        self.words = [
            "ultron",
            "hey ultron",
            "ok ultron",
            "okay ultron",
            "hello ultron",
            "hi ultron",
            "arise"
        ]

    def detected(self, text):

        if not text:
            return False

        # Normalize speech
        text = text.lower().strip()

        # Remove duplicate spaces
        text = " ".join(text.split())

        # Check every wake word
        for word in self.words:

            if word.lower() in text:
                return True

        return False

    def remove(self, text):

        if not text:
            return ""

        text = text.lower().strip()

        for word in self.words:

            if word.lower() in text:
                text = text.replace(word.lower(), "", 1)
                break

        return text.strip()