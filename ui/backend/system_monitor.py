from PySide6.QtCore import QObject, Signal, QTimer
import psutil

try:
    import GPUtil
except ImportError:
    GPUtil = None


class SystemMonitor(QObject):

    updated = Signal()

    def __init__(self):
        super().__init__()

        self.cpu = 0
        self.ram = 0
        self.disk = 0
        self.gpu = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

    def update_stats(self):

        self.cpu = int(psutil.cpu_percent())

        self.ram = int(psutil.virtual_memory().percent)

        self.disk = int(psutil.disk_usage("/").percent)

        if GPUtil:

            gpus = GPUtil.getGPUs()

            if gpus:
                self.gpu = int(gpus[0].load * 100)

        self.updated.emit()