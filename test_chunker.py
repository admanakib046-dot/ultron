from knowledge.document_loader import DocumentLoader
from knowledge.chunkers import Chunker

loader = DocumentLoader()

text = loader.load("test.txt")

chunker = Chunker(chunk_size=10)

chunks = chunker.split(text)

for i, chunk in enumerate(chunks):

    print(f"\nChunk {i+1}")
    print(chunk)