import os

from readers.pdf_reader import PDFReader
from readers.docx_reader import DOCXReader
from readers.txt_reader import TXTReader
from readers.md_reader import MDReader


class DocumentLoader:

    def __init__(self):

        self.readers = {

            ".pdf": PDFReader(),
            ".docx": DOCXReader(),
            ".txt": TXTReader(),
            ".md": MDReader()

        }

    def load(self, path):

        extension = os.path.splitext(path)[1].lower()

        reader = self.readers.get(extension)

        if reader is None:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return reader.read(path)