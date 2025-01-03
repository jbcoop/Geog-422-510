#version 1
"""from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("My First MainWindow App")

button = QPushButton()
button.setText("Press Me!")

window.setCentralWidget(button)

window.show()
app.exec()
"""
#version 2
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press Me")

        #set the button as the central widget of the window
        self.setCentralWidget(button)
        

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()
"""

#version 3
import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder   

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()