from PySide6.QtGui import QFontDatabase
import os

font_path = os.path.join(
    os.path.dirname(__file__),
    "fonts",
    "Orbitron-Regular.ttf"
)

print("Loading:", font_path)

font_id = QFontDatabase.addApplicationFont(font_path)

print("Font ID:", font_id)

if font_id == -1:
    print("❌ Failed to load Orbitron")
else:
    print("✅ Loaded:", QFontDatabase.applicationFontFamilies(font_id))