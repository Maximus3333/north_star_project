import sqlite3 as sql
from typing import Tuple
import pandas as pd
import gui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, QMessageBox
from PyQt5 import QtWidgets
import sys


def main():
    app = QApplication(sys.argv)
    main_window = gui.MainWindow()
    sys.exit(app.exec_())


main()

