from vision.face_database import FaceDatabase

db = FaceDatabase()

print("People:", db.get_people())

print("Jaguer Exists:", db.exists("Jaguer"))

print("John Exists:", db.exists("John"))