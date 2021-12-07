import sqlite3
from functools import partial
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


class Faculty:
    def __init__(self):

        self.facultyid = 0
        self.name = 'none'

    def update_faculty_id(self, facultyid):
        self.facultyid = facultyid

    def update_faculty_name(self, name):
        self.name = name


faculty = Faculty()


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
        self.title.setFont(QFont('Georgia', 16, QFont.Bold))
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
        self.back_button.setFont(QFont('Georgia', 7, QFont.Bold))

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
        self.title.setFont(QFont('Georgia', 16, QFont.Bold))
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
        self.back_button.setFont(QFont('Georgia', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)

        # Signals/Slots
        self.update_faculty_info_button.clicked.connect(self.access_faculty_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = FacultyMainWindow()
        self.previous_window.show()
        self.close()

    def access_faculty_clicked(self):
        conn = sqlite3.connect('north_star_school_database.db')
        cur = conn.cursor()
        try:
            self.check_if_id_exists = cur.execute("""SELECT EXISTS(SELECT 1 FROM instructor WHERE instructor_id = ?)""", (self.input_box.text(),)).fetchone()[0]
            print(self.check_if_id_exists)
            if self.check_if_id_exists == 1:
                faculty.facultyid = self.input_box.text()
                self.next_window = AccessedFacultyUpdatedWindow()
                self.next_window.show()
                self.close()
            else:
                self.error_mes = popup.ErrorPopUp("Id does not exist")
                self.error_mes.show()
                self.input_box.setStyleSheet(
                    "color: #fb0410; border-width: 0px; border-style: solid; border-color: white; border-bottom-color: red; border-bottom-width: 2px;")
        except Exception as e:
            print(e)
        conn.commit()
        conn.close()


class AccessedFacultyUpdatedWindow(QWidget):
    def __init__(self):
        super(AccessedFacultyUpdatedWindow, self).__init__()

        self.title = QLabel(self)
        self.update_accessed_faculty_button = QPushButton(self)
        self.input_box = QLineEdit(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Update faculty Window")

        # Title
        self.title.setText("Enter New Faculty Name:")
        self.title.setFont(QFont('Georgia', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Input Box
        self.input_box.resize(200, 30)
        self.input_box.move(200, 200)


        # Update Button
        self.update_accessed_faculty_button.resize(100, 50)
        self.update_accessed_faculty_button.move(245, 300)
        self.update_accessed_faculty_button.setText("Update")

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Georgia', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)

        #Signals / Slots
        self.back_button.clicked.connect(self.back_button_clicked)
        self.update_accessed_faculty_button.clicked.connect(self.updates_instructor_name)

    def back_button_clicked(self):
        self.previous_window = FacultyUpdateWindow()
        self.previous_window.show()
        self.close()

    def updates_instructor_name(self):
        conn = sqlite3.connect('north_star_school_database.db')
        cur = conn.cursor()

        self.new_instructor_name = self.input_box.text()
        self.input_box.textChanged.connect(self.txt_change)

        try:
            if all((x.isalpha() or x.isspace()) for x in self.new_instructor_name):
                print(self.new_instructor_name.title(), faculty.facultyid)
                cur.execute("""UPDATE instructor SET instructor_name = ?
                    WHERE instructor_id = ?""", (self.new_instructor_name.title(), faculty.facultyid))
                self.success_mes = popup.SuccessPopUp(f"You have successfully updated {faculty.facultyid}'s name to: {self.new_instructor_name.title()}")
                self.success_mes.show()
            else:
                self.error_mes = popup.ErrorPopUp("Please enter a correct Name")
                self.error_mes.show()
                self.input_box.setStyleSheet(
                    "color: #fb0410; border-width: 0px; border-style: solid; border-color: white; border-bottom-color: red; border-bottom-width: 2px;")
        except Exception as e:
            print(e)


        conn.commit()
        conn.close()

    def txt_change(self):
        self.input_box.setStyleSheet(
            "color: black; border: 0px")



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
        self.title.setFont(QFont('Georgia', 16, QFont.Bold))
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
        self.back_button.setFont(QFont('Georgia', 7, QFont.Bold))
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
        cur.execute("""PRAGMA foreign_keys = ON""")
        try:
            self.check_if_id_exists = cur.execute("""SELECT EXISTS(SELECT 1 FROM instructor WHERE instructor_id = ?)""",
                                                  (self.input_box.text(),)).fetchone()[0]
            if self.input_box.text().isnumeric() and self.check_if_id_exists == 1:
                cur.execute("""DELETE FROM instructor WHERE instructor_id = ? """, (self.input_box.text(),))
                self.success_mes = popup.SuccessPopUp(
                    f"You have successfully deleted {self.input_box.text().title()} from the database")
                self.success_mes.show()
            else:
                self.error_mes = popup.ErrorPopUp("Instructor ID doesnt exist!\n\nEnter a new ID")
                self.error_mes.show()
                self.input_box.setStyleSheet("color: #fb0410; border-width: 0px; border-style: solid; border-color: white; border-bottom-color: red; border-bottom-width: 2px;")
        except Exception as e:
            print(e)

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
        self.setWindowTitle("Add Faculty Window")
        window_width = int(self.frameGeometry().width())

        # Title
        self.title.setText("Enter Instructor Information")
        self.title.setFont(QFont('Georgia', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Instructor Name Entry
        self.new_instructor_name_label.setText("Enter Instructor Name: ")
        self.new_instructor_name_label.resize(200, 35)
        self.new_instructor_name_label.move(100, 150)
        self.new_instructor_name_textbox.resize(150, 35)
        self.new_instructor_name_textbox.move(250, 150)

        # Instructor ID Entry
        self.new_instructor_id_label.setText("Enter Instructor ID: ")
        self.new_instructor_id_label.resize(200, 35)
        self.new_instructor_id_label.move(100, 200)
        self.new_instructor_id_textbox.resize(150, 35)
        self.new_instructor_id_textbox.move(250, 200)

        # Add Button
        self.add_button.resize(100, 75)
        self.add_button.move(450, 375)
        self.add_button.setText('Add')
        self.add_button.setFont(QFont('Georgia', 7, QFont.Bold))

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Georgia', 7, QFont.Bold))

        # Signals/Slots
        self.back_button.clicked.connect(self.back_button_clicked)
        self.add_button.clicked.connect(self.add_faculty_to_db)

    def add_faculty_to_db(self):
        conn = sqlite3.connect('north_star_school_database.db')
        cur = conn.cursor()
        self.new_faculty = Faculty()
        self.new_instructor_id_textbox.textChanged.connect(partial(self.txt_change, 0))
        self.new_instructor_name_textbox.textChanged.connect(partial(self.txt_change, 1))
        try:
            if len(self.new_instructor_id_textbox.text()) != 0 and len(self.new_instructor_name_textbox.text()) != 0 and \
                    (self.new_instructor_id_textbox.text().isnumeric() for x in self.new_instructor_name_textbox.text()):

                self.check_if_id_exists_in_db = cur.execute("""SELECT EXISTS(SELECT 1 FROM instructor WHERE instructor_id = ?)""", (self.new_instructor_id_textbox.text(),))
                self.query_result = self.check_if_id_exists_in_db.fetchone()[0]
                if self.query_result == 0:
                    self.add_instructor_to_table = cur.execute("""INSERT INTO instructor (instructor_id, instructor_name) VALUES (?,?)""", (self.new_instructor_id_textbox.text(), self.new_instructor_name_textbox.text().title()))
                    self.success_mes = popup.SuccessPopUp(
                        f"You have successfully added {self.new_instructor_name_textbox.text().title()} \n with the ID: {self.new_instructor_id_textbox.text()} to the database")
                    self.success_mes.show()
                else:
                    self.error_mes = popup.ErrorPopUp("ID already exists!\nPlease enter a new ID")
                    self.error_mes.show()
            elif len(self.new_instructor_id_textbox.text()) == 0 and len(self.new_instructor_name_textbox.text()) == 0:
                self.new_instructor_id_textbox.setStyleSheet("border-width: 0px; border-style: solid; border-color: white; border-bottom-color: red; border-bottom-width: 2px;")
                self.new_instructor_name_textbox.setStyleSheet("border-width: 0px; border-style: solid; border-color: white; border-bottom-color: red; border-bottom-width: 2px;")
            elif len(self.new_instructor_name_textbox.text()) == 0:
                self.new_instructor_name_textbox.setStyleSheet("border-width: 0px; border-style: solid; border-color: white; border-bottom-color: red; border-bottom-width: 2px;")
            elif len(self.new_instructor_id_textbox.text()) == 0:
                self.new_instructor_id_textbox.setStyleSheet("border-width: 0px; border-style: solid; border-color: white; border-bottom-color: red; border-bottom-width: 2px;")
            elif not self.new_instructor_id_textbox.text().isnumeric() and not all((x.isalpha() or x.isspace()) for x in self.new_instructor_name_textbox.text()):
                self.error_mes = popup.ErrorPopUp("Please enter a correct NUMERIC ID\n and a correct Name")
                self.error_mes.show()
                self.new_instructor_id_textbox.setStyleSheet(
                    "border-width: 0px; border-style: solid; border-color: white; border-bottom-color: red; border-bottom-width: 2px;")
                self.new_instructor_name_textbox.setStyleSheet(
                    "border-width: 0px; border-style: solid; border-color: white; border-bottom-color: red; border-bottom-width: 2px;")
            elif not self.new_instructor_id_textbox.text().isnumeric():
                self.error_mes = popup.ErrorPopUp("Please enter a correct NUMERIC ID")
                self.error_mes.show()
                self.new_instructor_id_textbox.setStyleSheet(
                    "border-width: 0px; border-style: solid; border-color: white; border-bottom-color: red; border-bottom-width: 2px;")
            else:
                self.error_mes = popup.ErrorPopUp("Please enter a correct Name")
                self.error_mes.show()
                self.new_instructor_name_textbox.setStyleSheet(
                    "border-width: 0px; border-style: solid; border-color: white; border-bottom-color: red; border-bottom-width: 2px;")



        except Exception as e:
            pass

        conn.commit()
        conn.close()

    def back_button_clicked(self):
        self.previous_window = FacultyMainWindow()
        self.previous_window.show()
        self.close()

    def txt_change(self, bool):
        if bool == 0:
            self.new_instructor_id_textbox.setStyleSheet(
            "color: black; border: 0px")
        else:
            self.new_instructor_name_textbox.setStyleSheet(
                "color: black; border: 0px")