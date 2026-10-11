from plugin.plugin import Plugin


class WeatherPlugin(Plugin):

    def __init__(self, services):
        self.services = services

    def name(self):
        return "weather"

    def version(self):
        return "1.0"

    def author(self):
        return "Adman"

    def description(self):
        return "Gets live weather information."

    def execute(self, intent):

        internet = self.services.get("internet")

        city = intent.data["query"]

        return internet.search(
            f"weather {city}"
        )