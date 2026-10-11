class planner:

    def __init__(self):

        self.memory_words = {
            "remember",
            "recall",
            "forget",
            "memorize"
        }

        self.tool_words = {
            "calculate",
            "solve",
            "convert"
        }

        self.weather_words = {
            "weather",
            "temperature",
            "forecast",
            "humidity",
            "wind",
            "rain",
            "snow"
        }

        self.news_words = {
            "news",
            "latest",
            "breaking",
            "headline"
        }

        self.internet_prefix = (
            "who is",
            "what is",
            "where is",
            "when is",
            "why is",
            "how to",
            "search",
            "find",
            "look up"
        )

    def plan(self, command):

        text = command.lower().strip()

        # Memory
        if any(word in text for word in self.memory_words):
            return "memory"

        # Calculator / Tools
        if any(text.startswith(word) for word in self.tool_words):
            return "tool"

        # Weather
        if any(word in text for word in self.weather_words):
            return "weather"

        # News
        if any(word in text for word in self.news_words):
            return "news"

        # Internet Search
        if text.startswith(self.internet_prefix):
            return "internet"

        # AI Conversation
        return "ai"