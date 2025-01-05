#Version 1
"""
from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked():
    print("You clicked the button!")

app = QApplication()
button = QPushButton("Press Me")

button.clicked.connect(button_clicked)

button.show()
app.exec()
"""
#Version 2
"""
from PySide6.QtWidgets import QApplication, QPushButton

def button_clicked(data):
    print("You clicked the button!", data)

app = QApplication()
button = QPushButton("Press Me")
button.setCheckable(True)

button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

#Version 3

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

def respond_to_slider(data):
    print("Slider moved to : ", data)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(50)

slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()