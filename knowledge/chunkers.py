class Chunker:

    def __init__(self, chunk_size=500):
        self.chunk_size = chunk_size

    def split(self, text):

        words = text.split()

        chunks = []

        current = []
        current_size = 0

        for word in words:

            current.append(word)
            current_size += len(word) + 1

            if current_size >= self.chunk_size:

                chunks.append(" ".join(current))

                current = []
                current_size = 0

        if current:
            chunks.append(" ".join(current))

        return chunks