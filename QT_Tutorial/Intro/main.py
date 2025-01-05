#import components from PySide6
from PySide6.QtWidgets import QApplication, QWidget

# import sys module for command line args
import sys

# create an instance of QApplication
app = QApplication(sys.argv)

# create an instance of QWidget
window = QWidget()
window.show()

# start the event loop
app.exec()