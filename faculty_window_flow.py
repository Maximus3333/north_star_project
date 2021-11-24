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

#Test Commit demo
class FacultyMainWindow(QWidget):
    def __init__(self):
        super(FacultyMainWindow, self).__init__()

        self.title = QLabel(self)
        self.add_faculty_button = QPushButton(self)
        self.update_faculty_info_button = QPushButton(self)
        self.delete_faculty_button = QPushButton(self)
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

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))

        # Signals/Slots
        self.update_faculty_info_button.clicked.connect(self.update_button_clicked)
        self.delete_faculty_button.clicked.connect(self.delete_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)
        self.add_faculty_button.clicked.connect(self.faculty_id_being_added_window)

    def back_button_clicked(self):
        self.previous_window = gui.MainWindow()
        self.previous_window.show()
        self.close()

    def update_button_clicked(self):
        self.faculty_update_window = FacultyUpdateWindow()
        self.faculty_update_window.show()
        self.close()

    def delete_button_clicked(self):
        self.delete_faculty_window = DeleteFacultyWindow()
        self.delete_faculty_window.show()
        self.close()

    def faculty_id_being_added_window(self):
        self.window = AddFacultyWindow()
        self.window.show()
        self.close()


class FacultyUpdateWindow(QWidget):
    def __init__(self):
        super(FacultyUpdateWindow, self).__init__()
        self.title = QLabel(self)
        self.update_faculty_info_button = QPushButton(self)
        self.input_box = QLineEdit(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Update Faculty Window")

        # Title
        self.title.setText("Enter Faculty ID")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Input Box
        self.input_box.resize(200, 30)
        self.input_box.move(200, 200)

        # Update Faculty Button
        self.update_faculty_info_button.resize(100, 50)
        self.update_faculty_info_button.move(245, 300)
        self.update_faculty_info_button.setText('Access faculty')

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)

        # Signals/Slots
        self.update_faculty_info_button.clicked.connect(self.access_faculty_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = FacultyMainWindow()
        self.previous_window.show()
        self.close()

    def access_faculty_clicked(self):
        self.faculty_update_window = AccessedFacultyUpdatedWindow()
        self.faculty_update_window.show()
        self.close()


class AccessedFacultyUpdatedWindow(QWidget):
    def __init__(self):
        super(AccessedFacultyUpdatedWindow, self).__init__()

        self.title = QLabel(self)
        self.update_accessed_faculty_button = QPushButton(self)
        self.input_box = QLineEdit(self)
        self.input_box2 = QLineEdit(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Update faculty Window")

        # Title
        self.title.setText("Enter New Faculty ID:")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Input Box
        self.input_box.resize(200, 30)
        self.input_box.move(200, 200)

        # Input Box 2
        self.input_box2.resize(200, 30)
        self.input_box2.move(200, 250)

        # Update Button
        self.update_accessed_faculty_button.resize(100, 50)
        self.update_accessed_faculty_button.move(245, 300)
        self.update_accessed_faculty_button.setText("Update")

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)

        #Signals / Slots
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = FacultyUpdateWindow()
        self.previous_window.show()
        self.close()



class DeleteFacultyWindow(QWidget):
    def __init__(self):
        super(DeleteFacultyWindow, self).__init__()

        self.title = QLabel(self)
        self.delete_faculty_button = QPushButton(self)
        self.input_box = QLineEdit(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Delete faculty Window")

        # Title
        self.title.setText("Enter Faculty ID")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Input Box
        self.input_box.resize(200, 30)
        self.input_box.move(200, 200)

        # Delete faculty Button
        self.delete_faculty_button.resize(100, 50)
        self.delete_faculty_button.move(245, 300)
        self.delete_faculty_button.setText("Delete")

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)


        #Signals/Slots
        self.delete_faculty_button.clicked.connect(self.delete_faculty_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = FacultyMainWindow()
        self.previous_window.show()
        self.close()

    def delete_faculty_button_clicked(self):
        conn = sqlite3.connect('north_star_school_database.db')
        cur = conn.cursor()
        cur.execute("""DELETE FROM instructor WHERE instructor_id = ? """, (self.input_box.text(),))
        conn.commit()
        conn.close()

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
