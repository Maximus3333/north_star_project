import sqlite3
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, QMessageBox
import pandas as pd
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("mainScreen.ui", self)
        self.button.setFixedWidth(600)

# app = QApplication(sys.argv)
# widget = QtWidgets.QStackedWidget()
# mainwindow = MainWindow()
# widget.addWidget(mainwindow)
# widget.setFixedHeight(700)
# widget.setFixedWidth(600)
# widget.show()
# # print(widget.currentIndex())
# # print(widget.count())

# try:
#     sys.exit(app.exec_())
# except:
#     print("Exiting")