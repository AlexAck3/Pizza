# this is my pizza calculator

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pizza Calculator")
        button = QPushButton("Calculate")
        button = QPushButton("Calculate")
        button = QPushButton("Calculate")
        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()



# number_of_pies = int(input("enter the number of pies:"))
# size_of_pies = int(input("enter the size: 12, 14, 16:" ))

# total_flour_ratio = 1
# f_0102_ratio = .7
# f_bread_ratio = .2
# f_semoline_ratio = 0.05
# f_wholeweat_ratio = 0.05
# water_ratio_ratio = 0.69
# idy_ratio = 0.004
# sugar_ratio = 0.01
# salt_ratio = 0.02
# evoo_ratio = 0.03
# dought_weight = 0

# if size_of_pies == 14:
#     dough_weight = 300
# elif size_of_pies == 12:
#     dough_weight = 200
# elif size_of_pies ==16:
#     dough_weight = 400
# else:
#     print("please enter a dough weight in the listed sizes")
#     size_of_pies = int(input("enter the size: 12, 14, 16:" ))

