from updater.github_checker import GithubChecker
from updater.updater import Updater
from updater.backup import Backup
from updater.tester import Tester
from updater.rollback import Rollback


class UpdateManager:

    def __init__(self):
        self.github = GithubChecker()
        self.backup = Backup()
        self.updater = Updater()
        self.tester = Tester()
        self.rollback = Rollback()

    def check(self):
        return self.github.check()

    def install(self):
        print("Creating backup...")
        self.backup.create()

        print("Downloading update...")
        self.updater.install()

        print("Testing...")

        if self.tester.run():
            print("Update successful.")
            return True

        print("Rolling back...")
        self.rollback.restore()
        return False
    