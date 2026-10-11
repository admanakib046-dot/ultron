class FileEditor:

    def append(self, path, text):

        with open(path, "a", encoding="utf-8") as f:

            f.write(text)

        return True