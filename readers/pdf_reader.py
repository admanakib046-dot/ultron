import fitz


class PDFReader:

    def read(self, path):

        document = fitz.open(path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text