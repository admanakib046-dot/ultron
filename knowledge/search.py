from knowledge.embeddings import Embeddings
from knowledge.database import KnowledgeDatabase

class KnowledgeSearch:

    def __init__(self,database=None):

        self.database = database or KnowledgeDatabase()
        self.embedding = Embeddings()

    def search(self, query):

        results = []
        print("DATABASE:", self.database.documents)
        for filename, chunks in self.database.documents.items():

            for index, chunk in enumerate(chunks):

                score = self.embedding.similarity(
                    query,
                    chunk
                )

                if score > 0:

                    results.append({

                        "file": filename,
                        "chunk": index,
                        "text": chunk,
                        "score": score

                    })

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results