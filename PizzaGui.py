# this is my pizza calculator

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pizza Calculator")
        button_12 = QPushButton("Calculate")
        button_14 = QPushButton("Calculate")
        button_16 = QPushButton("Calculate")
        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.setCentralWidget(button_12)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()



