from internet.internet import Internet
class Google(Internet):
    def search(self, query):
         return f"[google]\nSearching for: {query}"