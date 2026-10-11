import os
os.environ["QSG_RHI_BACKEND"] = "opengl"
os.environ["QSG_INFO"] = "1"
import sys

from PySide6.QtGui import QGuiApplication, QFontDatabase
from PySide6.QtQml import QQmlApplicationEngine

from ui.backend.system_monitor import SystemMonitor


app = QGuiApplication(sys.argv)

# --------------------------------------------------
# Load Fonts
# --------------------------------------------------

base = os.path.dirname(os.path.dirname(__file__))

font_paths = [
    os.path.join(base, "assets", "fonts", "Orbitron-Regular.ttf"),
    os.path.join(base, "assets", "fonts", "Orbitron-Bold.ttf"),
    os.path.join(base, "assets", "fonts", "Orbitron-Black.ttf"),
]

for path in font_paths:
    print("Loading:", path)

    font_id = QFontDatabase.addApplicationFont(path)

    if font_id == -1:
        print("FAILED:", path)
    else:
        print(
            "Loaded:",
            QFontDatabase.applicationFontFamilies(font_id)
        )

# --------------------------------------------------
# Backend
# --------------------------------------------------

monitor = SystemMonitor()

# --------------------------------------------------
# QML Engine
# --------------------------------------------------

engine = QQmlApplicationEngine()

engine.rootContext().setContextProperty(
    "systemMonitor",
    monitor
)

qml = os.path.join(
    os.path.dirname(__file__),
    "qml",
    "Main.qml"
)

print("Loading QML:", qml)

engine.load(qml)

if not engine.rootObjects():
    print("QML FAILED TO LOAD")
    sys.exit(-1)

sys.exit(app.exec())