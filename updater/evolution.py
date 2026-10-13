from updater.sources import Sources
from updater.updater import Updater


class Evolution:

    def __init__(self):
        self.sources = Sources()
        self.updater = Updater()

    def analyze(self):
        return self.sources.find_updates()

    def install(self):

        updates = self.analyze()

        if not updates:
            return False

        print("Installing improvements...\n")

        for update in updates:
            self.updater.install_module(update)

        print("Evolution complete.")
        return True