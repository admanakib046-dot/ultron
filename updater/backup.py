import shutil
import datetime


class Backup:

    def create(self):

        name = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        shutil.make_archive(
            "backups/" + name,
            "zip",
            "."
        )