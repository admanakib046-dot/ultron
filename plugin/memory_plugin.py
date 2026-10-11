from plugin.plugin import Plugin


class MemoryPlugin(Plugin):

    def __init__(self, services):
        self.services = services

    def name(self):
        return "memory"
    def version(self):
        return "1.0"

    def author(self):
        return "Adman"

    def description(self):
        return "Performs mathematical calculations."

    def execute(self, intent):

        memory = self.services.get("memory")

        if intent.action == "remember":

            key = intent.data["key"]
            value = intent.data["value"]

            memory.remember(key, value)

            return f"I'll remember that {key}."

        elif intent.action == "recall":

            key = intent.data["key"]

            value = memory.recall(key)

            if value:
                return f"{key} = {value}"

            return "I don't remember that."