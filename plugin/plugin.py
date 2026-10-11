from abc import ABC, abstractmethod


class Plugin(ABC):

    @abstractmethod
    def name(self):
        pass

    def version(self):
        return "1.0"

    def author(self):
        return "Adman"

    def description(self):
        return "No description."

    def enabled(self):
        return True

    @abstractmethod
    def execute(self, intent):
        pass