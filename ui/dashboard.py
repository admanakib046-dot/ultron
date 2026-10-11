from PySide6.QtWidgets import (
    QWidget,
    QFrame,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QProgressBar
)
from PySide6.QtCore import Qt
import psutil


class Dashboard(QWidget):

    def __init__(self):

        super().__init__()

        root = QHBoxLayout(self)

        # ==========================
        # CENTER
        # ==========================

        center = QVBoxLayout()

        title = QLabel("GOOD EVENING, JAGUER")
        title.setStyleSheet("""
            font-size:34px;
            font-weight:bold;
            color:white;
        """)

        subtitle = QLabel("ULTRON IS ONLINE")
        subtitle.setStyleSheet("""
            color:#bbbbbb;
            font-size:16px;
        """)

        center.addWidget(title)
        center.addWidget(subtitle)

        # --------------------------
        # Hologram Placeholder
        # --------------------------

        core = QFrame()
        core.setMinimumSize(700, 500)

        core.setStyleSheet("""
            QFrame{
                background:#0c1017;
                border:2px solid red;
                border-radius:25px;
            }
        """)

        core_layout = QVBoxLayout(core)

        logo = QLabel("ULTRON CORE")
        logo.setAlignment(Qt.AlignCenter)

        logo.setStyleSheet("""
            font-size:36px;
            font-weight:bold;
            color:red;
        """)

        core_layout.addStretch()
        core_layout.addWidget(logo)
        core_layout.addStretch()

        center.addWidget(core)

        # --------------------------
        # Voice Bar
        # --------------------------

        voice = QFrame()

        voice.setFixedHeight(80)

        voice.setStyleSheet("""
            QFrame{
                background:#10151D;
                border:1px solid red;
                border-radius:40px;
            }
        """)

        voice_layout = QHBoxLayout(voice)

        mic = QLabel("🎤")
        mic.setStyleSheet("font-size:30px;color:red;")

        text = QLabel("How can I help you?")

        text.setStyleSheet("""
            font-size:18px;
            color:white;
        """)

        voice_layout.addWidget(mic)
        voice_layout.addWidget(text)
        voice_layout.addStretch()

        center.addWidget(voice)

        root.addLayout(center, 4)

        # ==========================
        # RIGHT PANEL
        # ==========================

        right = QVBoxLayout()

        def create_card(title):

            card = QFrame()

            card.setStyleSheet("""
                QFrame{
                    background:#10151D;
                    border:1px solid #303030;
                    border-radius:15px;
                }
            """)

            layout = QVBoxLayout(card)

            header = QLabel(title)

            header.setStyleSheet("""
                font-size:18px;
                color:white;
            """)

            layout.addWidget(header)

            return card, layout

        # ---------- System ----------

        card, layout = create_card("SYSTEM OVERVIEW")

        cpu = QProgressBar()
        cpu.setValue(int(psutil.cpu_percent()))

        ram = QProgressBar()
        ram.setValue(int(psutil.virtual_memory().percent))

        disk = QProgressBar()
        disk.setValue(int(psutil.disk_usage("/").percent))

        layout.addWidget(QLabel("CPU"))
        layout.addWidget(cpu)

        layout.addWidget(QLabel("RAM"))
        layout.addWidget(ram)

        layout.addWidget(QLabel("DISK"))
        layout.addWidget(disk)

        right.addWidget(card)

        # ---------- Camera ----------

        card2, layout2 = create_card("VISION")

        camera = QLabel()

        camera.setFixedSize(250, 160)

        camera.setStyleSheet("""
            background:black;
            border:1px solid red;
        """)

        camera.setAlignment(Qt.AlignCenter)
        camera.setText("CAMERA")

        layout2.addWidget(camera)

        right.addWidget(card2)

        # ---------- Memory ----------

        card3, layout3 = create_card("MEMORY")

        memories = QLabel("Stored Memories : 0")

        layout3.addWidget(memories)

        right.addWidget(card3)

        right.addStretch()

        root.addLayout(right, 1)