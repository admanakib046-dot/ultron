class InternetPlanner:

    def choose_provider(self, query):

        q = query.lower()

        # Weather
        if "weather" in q:
            return "duckduckgo"

        # News
        if "news" in q:
            return "news"

        if "latest" in q:
            return "news"

        # Wikipedia
        if q.startswith("who is"):
            return "wikipedia"

        if q.startswith("what is"):
            return "wikipedia"

        # Default
        return "duckduckgo"