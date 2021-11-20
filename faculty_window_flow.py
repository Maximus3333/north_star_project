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

class FacultyMainWindow(QWidget):
    def __init__(self):
        super(FacultyMainWindow, self).__init__()

        self.title = QLabel(self)
        self.add_faculty_button = QPushButton(self)
        self.update_faculty_info_button = QPushButton(self)
        self.delete_faculty_button = QPushButton(self)
        #self.access_faculty_button = QPushButton(self)

        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Faculty Main Window")

        # Title
        self.title.setText("Please select a Faculty option")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Add Button
        self.add_faculty_button.resize(100, 50)
        self.add_faculty_button.move(145, 300)
        self.add_faculty_button.setText('Add')

        # Update Button
        self.update_faculty_info_button.resize(100, 50)
        self.update_faculty_info_button.move(250, 300)
        self.update_faculty_info_button.setText('Update')

        # Delete Button
        self.delete_faculty_button.resize(100, 50)
        self.delete_faculty_button.move(355, 300)
        self.delete_faculty_button.setText('Delete')

        # # Access Button
        # self.access_faculty_button.resize(100, 50)
        # self.access_faculty_button.move(355, 300)
        # self.access_faculty_button.setText('Access')

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))

        # Signals/Slots
        self.add_faculty_button.clicked.connect(self.faculty_id_being_added_window)
        # self.update_faculty_info_button.clicked.connect(self.faculty_id_being_updated_pop_up)
        # self.delete_faculty_button.clicked.connect(self.faculty_id_being_deleted_pop_up)
        # self.access_faculty_button.clicked.connect(self.faculty_id_being_accessed_pop_up)
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = gui.MainWindow()
        self.previous_window.show()
        self.close()

    # def faculty_id_being_deleted_pop_up(self):
    #     self.popup = popup.DeleteFacultyPopUp()
    #
    # def faculty_id_being_updated_pop_up(self):
    #     self.popup = popup.UpdateFacultyPopUp()

    def faculty_id_being_added_window(self):
        self.window = AddFacultyWindow()
        self.window.show()
        self.close()



class AddFacultyWindow(QWidget):
    def __init__(self):
        super(AddFacultyWindow, self).__init__()

        self.title = QLabel(self)
        self.new_instructor_id_label = QLabel(self)
        self.new_instructor_name_label = QLabel(self)
        self.new_instructor_id_textbox = QLineEdit(self)
        self.new_instructor_name_textbox = QLineEdit(self)
        self.add_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        self.setWindowTitle("Add Student Window")
        window_width = int(self.frameGeometry().width())

        # Title
        self.title.setText("Enter Student Information")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Student Name Entry
        self.new_instructor_name_label.setText("Enter Instructor Name: ")
        self.new_instructor_name_label.resize(200, 35)
        self.new_instructor_name_label.move(100, 150)
        self.new_instructor_name_textbox.resize(150, 35)
        self.new_instructor_name_textbox.move(250, 150)

        # Student ID Entry
        self.new_instructor_id_label.setText("Enter Instructor ID: ")
        self.new_instructor_id_label.resize(200, 35)
        self.new_instructor_id_label.move(100, 200)
        self.new_instructor_id_textbox.resize(150, 35)
        self.new_instructor_id_textbox.move(250, 200)

        # Add Button
        self.add_button.resize(100, 75)
        self.add_button.move(450, 375)
        self.add_button.setText('Add')
        self.add_button.setFont(QFont('Papyrus', 7, QFont.Bold))

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))

        # Signals/Slots
        self.back_button.clicked.connect(self.back_button_clicked)


    def back_button_clicked(self):
        self.previous_window = FacultyMainWindow()
        self.previous_window.show()
        self.close()

