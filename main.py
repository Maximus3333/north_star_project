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
    style = """
        QWidget {
                background-color: #0b090a;
            }
        QLabel{
            color: #fb9c20;
            font: Georgia;
        }
        QPushButton {
            background-color: rgba(247,247,247,255);
        }
        QLineEdit {
            background-color: #f5f3f4;
        }
        QTableWidget {
            background-color: #e2ece9;
        }
    """
    app.setStyleSheet(style)
    print(type(app))
    sys.exit(app.exec_())




main()

