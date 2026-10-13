import json

from updater.github_checker import GithubChecker
from updater.updater import Updater
from updater.backup import Backup
from updater.tester import Tester
from updater.rollback import Rollback
from updater.module_updater import ModuleUpdater


class UpdateManager:

    def __init__(self):

        self.github = GithubChecker()
        self.backup = Backup()
        self.updater = Updater()
        self.tester = Tester()
        self.rollback = Rollback()
        self.module_updater = ModuleUpdater()

    # =====================================
    # Check GitHub for updates
    # =====================================
    def check(self):

        remote = self.github.check()

        if not remote:
            return None

        # Read local version
        try:
            with open("version.json", "r") as f:
                local = json.load(f)
        except FileNotFoundError:
            local = {
                "version": "0.0.0",
                "build": 0,
                "release_date": ""
            }

        local_version = local["version"]
        remote_version = remote["version"]["version"]

        if local_version == remote_version:
            return {
                "update": False,
                "current": local_version,
                "latest": remote_version,
                "modules": remote["modules"],
                "notes": remote["notes"]
            }

        return {
            "update": True,
            "current": local_version,
            "latest": remote_version,
            "modules": remote["modules"],
            "notes": remote["notes"]
        }

    # =====================================
    # Install update
    # =====================================
    def install(self):

     print("Creating backup...")
     self.backup.create()

     remote = self.github.check()

     if not remote:
        print("Unable to contact GitHub.")
        return False

     modules = remote["modules"]

     print("\nUpdating modules...\n")

     for module in modules:

        print(f"Updating {module}...")

        ok = self.module_updater.update_module(module)

        if not ok:
            print(f"Failed updating {module}")
            self.rollback.restore()
            return False

        print("\nRunning tests...")

     if not self.tester.run():
        print("Tests failed.")
        self.rollback.restore()
        return False

     with open("version.json", "w") as f:
        json.dump(remote["version"], f, indent=4)

     print("Version updated.")
     print("Update completed successfully.")

     return True
    