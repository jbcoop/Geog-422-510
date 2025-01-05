from PySide6.QtWidgets import QWidget

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("background-color: #000000; color: #ffffff;")

        self.show()