import os
import shutil
import tempfile
import zipfile
import requests


class ModuleUpdater:

    REPO = "admanakib046-dot/ultron"

    def update_module(self, module):

        print(f"Updating {module}...")

        url = f"https://github.com/{self.REPO}/archive/refs/heads/main.zip"

        temp = tempfile.mkdtemp()

        zip_path = os.path.join(temp, "update.zip")

        r = requests.get(url)

        if r.status_code != 200:
            return False

        with open(zip_path, "wb") as f:
            f.write(r.content)

        with zipfile.ZipFile(zip_path) as z:
            z.extractall(temp)

        source = os.path.join(
            temp,
            "ultron-main",
            module
        )

        destination = os.path.join(
            os.getcwd(),
            module
        )

        if not os.path.exists(source):
            return False

        if os.path.exists(destination):
            shutil.rmtree(destination)

        shutil.copytree(source, destination)

        return True