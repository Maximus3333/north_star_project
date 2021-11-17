import sqlite3
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, \
    QMessageBox, QWidget, QDialog, QInputDialog
import pandas as pd
import gui
import popup
import sys

class CourseMainWindow(QWidget):
    def __init__(self):
        super(CourseMainWindow, self).__init__()

        self.title = QLabel(self)
        self.add_course_or_section_button = QPushButton(self)
        self.update_course_or_section_button = QPushButton(self)
        self.delete_section_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Course Main Window")

        # Title
        self.title.setText("Please select a Course option")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Add Button
        self.add_course_or_section_button.resize(100, 50)
        self.add_course_or_section_button.move(145, 300)
        self.add_course_or_section_button.setText('Add')

        # Update Button
        self.update_course_or_section_button.resize(100, 50)
        self.update_course_or_section_button.move(250, 300)
        self.update_course_or_section_button.setText('Update')

        # Delete Button
        self.delete_section_button.resize(100, 50)
        self.delete_section_button.move(355, 300)
        self.delete_section_button.setText('Delete')

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)

        # Signals/Slots
        # self.add_course_or_section_button.clicked.connect()
        # self.update_course_or_section_button.clicked.connect()
        # self.delete_section_button.clicked.connect()
        self.back_button.clicked.connect(self.back_button_clicked)


    def back_button_clicked(self):
        self.previous_window = gui.MainWindow()
        self.previous_window.show()
        self.close()

class CourseSectionAddWindow(QWidget):
    def __init__(self):
        super(CourseSectionAddWindow, self).__init__()

        self.title = QLabel(self)

        self.setup_ui()

    def setup_ui(self):



class CourseAddWindow(QWidget):
    def __init__(self):
        super(CourseAddWindow, self).__init__()

        self.title = QLabel(self)

        self.setup_ui()

    def setup_ui(self):


class SectionAddWindow(QWidget):
    def __init__(self):
        super(SectionAddWindow, self).__init__()

        self.title = QLabel(self)

        self.setup_ui()

    def setup_ui(self):
