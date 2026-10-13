import os
import shutil
import datetime


class Backup:

    def create(self):

        # Create backups folder
        os.makedirs("backups", exist_ok=True)

        # Backup name
        name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        destination = os.path.join("backups", name)

        # Ignore unnecessary folders
        ignore = shutil.ignore_patterns(
            ".git",
            ".venv",
            "__pycache__",
            "backups",
            ".vscode"
        )

        print("Copying project files...")

        shutil.copytree(
            ".",
            destination,
            ignore=ignore,
            dirs_exist_ok=True
        )

        print("Backup created:", destination)