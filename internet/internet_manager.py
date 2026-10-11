from internet.duckduckgo import DuckDuckGo
from internet.wikipedia import Wikipedia
from internet.news import News
from internet.internet_planner import InternetPlanner
from internet.internet_ai import InternetAI


class InternetManager:

    def __init__(self):
        self.duckduckgo = DuckDuckGo()
        self.wikipedia = Wikipedia()
        self.news = News()

        self.ai = InternetAI()
        self.planner = InternetPlanner()

    def search(self, query):

        provider = self.planner.choose_provider(query)

        if provider == "duckduckgo":
            results = self.duckduckgo.search(query)

        elif provider == "wikipedia":
            results = self.wikipedia.search(query)

        elif provider == "news":
            results = self.news.search(query)

        else:
            results = self.duckduckgo.search(query)

        print("\n=== RAW SEARCH RESULTS ===")
        print(results)

        if results.startswith("No"):
            return results

        return self.ai.summarize(results, query)

    