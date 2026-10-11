from knowledge.search import KnowledgeSearch

search = KnowledgeSearch()

results = search.search("Ultron")

for result in results:

    print("=" * 50)
    print("File :", result["file"])
    print("Chunk:", result["chunk"])
    print(result["text"])