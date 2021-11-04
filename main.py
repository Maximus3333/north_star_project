import sqlite3 as sql
from typing import Tuple
import pandas as pd
import gui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, QMessageBox
from PyQt5 import QtWidgets
import sys


def main():
    app = QApplication(sys.argv)
    # widget = QtWidgets.QStackedWidget()
    mainwindow = gui.MainWindow()
    mainwindow.setFixedHeight(601)
    mainwindow.setFixedWidth(665)    
    mainwindow.show()
    # print(widget.currentIndex())
    # print(widget.count())

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

main()