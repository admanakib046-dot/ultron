from filesystem.file_writer import FileWriter
from filesystem.file_reader import FileReader

writer = FileWriter()
reader = FileReader()

writer.write("hello.txt", "Hello Ultron!")

print(reader.read("hello.txt"))