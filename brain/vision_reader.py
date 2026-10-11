class VisionReader:

    def understand(self, text):

        text = text.strip()

        if text == "":
            return "I couldn't detect any readable text."

        return f"I found the following text:\n\n{text}"