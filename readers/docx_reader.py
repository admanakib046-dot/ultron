from docx import Document


class DOCXReader:

    def read(self, path):

        document = Document(path)

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text