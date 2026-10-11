class router:

    def route(self, intent):

        routes = {
            "remember": "memory",
            "recall": "memory",

            "calculate": "tool",

            "learn": "knowledge",
            "knowledge_search": "knowledge",
            "knowledge_summary": "knowledge",

            "search": "internet",
            "weather": "weather",
            "news": "news",

            "vision": "vision",
            "voice": "voice",

            "ai": "ai"
        }

        return routes.get(intent.action.lower(), "ai")
         