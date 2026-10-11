class FileWriter:

    def write(self, path, text):

        with open(path, "w", encoding="utf-8") as f:

            f.write(text)

        return True