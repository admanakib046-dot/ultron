from PySide6.QtWidgets import QLabel,QHBoxLayout,QFrame


class TopBar(QFrame):

    def __init__(self):

        super().__init__()

        layout=QHBoxLayout(self)

        title=QLabel("ULTRON V1")

        layout.addWidget(title)

        layout.addStretch()