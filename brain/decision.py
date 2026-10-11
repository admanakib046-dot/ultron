class DecisionEngine:

    def __init__(self):

        self.modules = [
            "ai",
            "internet",
            "memory",
            "vision",
            "document",
            "task"
        ]

    def decide(self, action, command):

        text = command.lower()

        scores = {
            "ai": 0,
            "internet": 0,
            "memory": 0,
            "vision": 0,
            "document": 0,
            "task": 0
        }

        # -------------------------
        # NLP Action
        # -------------------------

        if action == "search":
            scores["internet"] += 90

        elif action == "remember":
            scores["memory"] += 100

        elif action == "recall":
            scores["memory"] += 90

        elif action == "calculate":
            scores["ai"] += 80

        # -------------------------
        # Vision
        # -------------------------

        vision_words = [
            "camera",
            "photo",
            "picture",
            "image",
            "scan",
            "detect",
            "recognize",
            "vision"
        ]

        if any(word in text for word in vision_words):
            scores["vision"] += 100

        # -------------------------
        # Documents
        # -------------------------

        document_words = [
            "pdf",
            "document",
            "docx",
            "ppt",
            "excel",
            "file"
        ]

        if any(word in text for word in document_words):
            scores["document"] += 100

        # -------------------------
        # Tasks
        # -------------------------

        task_words = [
            "build",
            "create",
            "develop",
            "project",
            "plan"
        ]

        if any(word in text for word in task_words):
            scores["task"] += 90

        # -------------------------
        # Internet keywords
        # -------------------------

        internet_words = [
            "latest",
            "today",
            "news",
            "weather",
            "google",
            "search",
            "find"
        ]

        if any(word in text for word in internet_words):
            scores["internet"] += 80

        # -------------------------
        # Default AI
        # -------------------------

        if max(scores.values()) == 0:
            scores["ai"] = 100

        destination = max(scores, key=scores.get)

        reasons = {
            "ai": "Using AI.",
            "internet": "Searching the internet.",
            "memory": "Using memory.",
            "vision": "Using vision.",
            "document": "Reading documents.",
            "task": "Planning tasks."
        }

        return {
            "destination": destination,
            "reason": reasons[destination],
            "confidence": scores[destination],
            "scores": sorted(
                scores.items(),
                key=lambda x: x[1],
                reverse=True
            )
        }