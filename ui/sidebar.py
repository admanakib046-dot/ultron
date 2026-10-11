from PySide6.QtWidgets import QFrame,QVBoxLayout,QPushButton


class Sidebar(QFrame):

    def __init__(self):

        super().__init__()

        self.setFixedWidth(220)

        layout=QVBoxLayout(self)

        buttons=[
            "HOME",
            "VISION",
            "VOICE",
            "SYSTEM",
            "MEMORY",
            "INTERNET",
            "AUTOMATION",
            "SETTINGS"
        ]

        for b in buttons:

            layout.addWidget(QPushButton(b))

        layout.addStretch()