import os
import shutil


class FileManager:

    def exists(self, path):

        return os.path.exists(path)

    def delete(self, path):

        if os.path.exists(path):
            os.remove(path)

    def copy(self, src, dst):

        shutil.copy(src, dst)

    def move(self, src, dst):

        shutil.move(src, dst)

    def list_files(self, folder="."):

        return os.listdir(folder)