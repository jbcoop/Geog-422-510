from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar

class MainWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom MainWindow")
        self.setGeometry(100, 100, 800, 600)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        toolbar.addAction(quit_action)

        action1 = QAction("Some Action", self)
        action1.setStatusTip("This is some action")
        action1.triggered.connect(self.tool_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("QT_Tutorial\MainWindow\start.png"), "Another Action", self)
        action2.setStatusTip("This is another action")
        action2.triggered.connect(self.tool_button_click)
        action2.setCheckable(True)
        toolbar.addAction(action2)

    def tool_button_click(self):
        print("Tool button clicked")

    def quit_app(self):
        self.app.quit()

    