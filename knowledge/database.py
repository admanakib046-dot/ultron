class KnowledgeDatabase:

    _documents = {}

    def add_document(self, filename, chunks):

        self.__class__._documents[filename] = chunks

    @property
    def documents(self):

        return self.__class__._documents

    def search(self, query):

        query = query.lower()

        results = []

        for filename, chunks in self.documents.items():

            for i, chunk in enumerate(chunks):

                if query in chunk.lower():

                    results.append({

                        "file": filename,
                        "chunk": i,
                        "text": chunk

                    })

        return results