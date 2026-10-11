from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout
)

from ui.sidebar import Sidebar
from ui.topbar import TopBar
from ui.dashboard import Dashboard
from ui.styles import MAIN_STYLE

import sys


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.resize(1600,900)

        self.setWindowTitle("ULTRON")

        self.setStyleSheet(MAIN_STYLE)

        root=QHBoxLayout(self)

        root.addWidget(Sidebar())

        right=QVBoxLayout()

        right.addWidget(TopBar())

        right.addWidget(Dashboard())

        root.addLayout(right)


if __name__=="__main__":

    app=QApplication(sys.argv)

    window=MainWindow()

    window.show()

    sys.exit(app.exec())