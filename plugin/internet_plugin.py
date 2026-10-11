from plugin.plugin import Plugin


class InternetPlugin(Plugin):

    def __init__(self, services):
        self.services = services

    def name(self):
        return "search"
    def version(self):
        return "1.0"

    def author(self):
        return "Adman"

    def description(self):
        return "Performs mathematical calculations."

    def execute(self, intent):

        internet = self.services.get("internet")

        query = intent.data["query"]

        return internet.search(query)