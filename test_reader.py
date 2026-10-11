from readers.txt_reader import TXTReader

reader = TXTReader()

text = reader.read("test.txt")

print(text)