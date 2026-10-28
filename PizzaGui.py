import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pizza Calculator")
        self.setFixedSize(QSize(400, 300))

        layout = QVBoxLayout()

        self.label = QLabel("Click any button")
        layout.addWidget(self.label)

        self.button_12 = QPushButton(f"12in")
        self.button_12.clicked.connect(self.button12_clicked)
        self.button_14 = QPushButton("14in")
        self.button_14.clicked.connect(self.button14_clicked)
        self.button_16 = QPushButton("16in")
        self.button_16.clicked.connect(self.button16_clicked)

        layout.addWidget(self.button_12)
        layout.addWidget(self.button_14)
        layout.addWidget(self.button_16)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def button12_clicked(self):
        self.button_12.setText("You already clicked me.")
        self.button_12.setEnabled(False)

    def button14_clicked(self):
        self.button_14.setText("You already clicked me.")
        self.button_14.setEnabled(False)

    def button16_clicked(self):
        self.button_16.setText("You already clicked me.")
        self.button_16.setEnabled(False)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()