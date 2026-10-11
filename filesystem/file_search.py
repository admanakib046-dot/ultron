import os


class FileSearch:

    def find(self, filename, folder="."):

        matches = []

        for root, dirs, files in os.walk(folder):

            if filename in files:

                matches.append(
                    os.path.join(root, filename)
                )

        return matches