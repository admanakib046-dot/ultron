from plugin.plugin import Plugin


class CalculatorPlugin(Plugin):

    def __init__(self, services):
        self.services = services

    def name(self):
        return "calculate"
    def version(self):
        return "1.0"

    def author(self):
        return "Adman"

    def description(self):
        return "Performs mathematical calculations."

    def execute(self, intent):

        tools = self.services.get("tools")

        expression = intent.data["expression"]

        return tools.use(
            "calculator",
            expression
        )