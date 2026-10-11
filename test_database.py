from knowledge.document_loader import DocumentLoader
from knowledge.chunkers import Chunker
from knowledge.database import KnowledgeDatabase

loader = DocumentLoader()

text = loader.load("test.txt")

chunker = Chunker(10)

chunks = chunker.split(text)

db = KnowledgeDatabase()

db.add_document("test.txt", chunks)

print(db.all())