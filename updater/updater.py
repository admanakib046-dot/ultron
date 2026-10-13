import os
import shutil
import zipfile
import tempfile
import requests


class Updater:

    REPO = "admanakib046-dot/ultron"

    def install(self):

        url = f"https://github.com/{self.REPO}/archive/refs/heads/main.zip"

        print("Downloading latest version...")

        temp = tempfile.mkdtemp()
        zip_path = os.path.join(temp, "update.zip")

        r = requests.get(url, timeout=30)

        if r.status_code != 200:
            print("Download failed.")
            return False

        with open(zip_path, "wb") as f:
            f.write(r.content)

        print("Extracting...")

        with zipfile.ZipFile(zip_path) as z:
            z.extractall(temp)

        extracted = os.path.join(temp, "ultron-main")
        current = os.getcwd()

        print("Replacing files...")

        for root, dirs, files in os.walk(extracted):

            rel = os.path.relpath(root, extracted)
            target = os.path.join(current, rel)

            os.makedirs(target, exist_ok=True)

            for file in files:

                src = os.path.join(root, file)
                dst = os.path.join(target, file)

                shutil.copy2(src, dst)

        print("Update installed.")

        return True

    # ===========================================
    # Evolution Module Installer
    # ===========================================

    def install_module(self, update):

        module = update["module"]

        print(f"Installing {module}...")

        # Placeholder for now.
        # Later this can download only the changed module from GitHub.

        return True