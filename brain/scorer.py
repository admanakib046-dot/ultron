class ConfidenceScorer:

    def score(self, intent):

        scores = {
            "memory": 0,
            "knowledge": 0,
            "internet": 0,
            "tool": 0,
            "weather": 0,
            "news": 0,
            "ai": 10
        }

        action = intent.action.lower()

        if action in ["remember", "recall"]:
            scores["memory"] = 100

        elif action in [
            "learn",
            "knowledge_search",
            "knowledge_summary"
        ]:
            scores["knowledge"] = 100

        elif action == "calculate":
            scores["tool"] = 100

        elif action == "weather":
            scores["weather"] = 100

        elif action == "news":
            scores["news"] = 100

        elif action == "search":
            scores["internet"] = 100

        else:
            scores["ai"] = 90

        return scores