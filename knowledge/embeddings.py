import re


class Embeddings:

    def preprocess(self, text):

        text = text.lower()

        text = re.sub(r"[^a-z0-9 ]", "", text)

        return text.split()

    def embed(self, text):

        return set(
            self.preprocess(text)
        )

    def similarity(self, text1, text2):

        v1 = self.embed(text1)
        v2 = self.embed(text2)

        if not v1 or not v2:
            return 0

        score = len(v1 & v2) / len(v1 | v2)

        return score