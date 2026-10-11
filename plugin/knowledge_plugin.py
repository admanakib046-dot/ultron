from plugin.plugin import Plugin

from knowledge.document_loader import DocumentLoader
from knowledge.chunkers import Chunker
from knowledge.database import KnowledgeDatabase
from knowledge.search import KnowledgeSearch


class KnowledgePlugin(Plugin):

    def __init__(self, services):

        self.services = services

        self.loader = DocumentLoader()
        self.chunker = Chunker()

        # Shared database
        self.database = KnowledgeDatabase()

        # Search engine uses the SAME database
        self.search_engine = KnowledgeSearch(self.database)

    def name(self):
        return "knowledge"

    def version(self):
        return "1.0"

    def author(self):
        return "Ultron"

    def description(self):
        return "Knowledge Engine"

    def enabled(self):
        return True

    def execute(self, intent):

        # ==========================
        # Learn Document
        # ==========================

        if intent.action == "learn":

            file = intent.data["file"]

            print("\nLEARNING:", file)

            text = self.loader.load(file)

            print("\nDOCUMENT:")
            print(text)

            chunks = self.chunker.split(text)

            print("\nCHUNKS:")
            for i, chunk in enumerate(chunks):
                print(f"{i}: {chunk}")

            self.database.add_document(file, chunks)

            print("\nDATABASE AFTER SAVE:")
            print(self.database.documents)

            return f"Learned {file}"

        # ==========================
        # Search Knowledge
        # ==========================

        elif intent.action == "knowledge_search":

            query = intent.data["query"]

            print("\nQUERY:", query)

            print("\nDATABASE BEFORE SEARCH:")
            print(self.database.documents)

            # Ensure both use the same database
            self.search_engine.database = self.database

            results = self.search_engine.search(query)

            print("\nRESULTS:")
            print(results)

            if not results:
                return "Nothing found."

            answer = ""

            for item in results[:5]:

                answer += (
                    f"\n[{item['file']} - Chunk {item['chunk']}]\n"
                    f"{item['text']}\n"
                )

            return answer

        return "Unknown knowledge command."