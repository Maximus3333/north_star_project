import sqlite3
from PyQt5.QtGui import * 
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, \
    QMessageBox, QWidget, QDialog, QInputDialog
import pandas as pd
import popup
import faculty_window_flow
import sys


"""
!!!!!! Define window classes first then figure out way
       to switch between screens with QStackeWidget
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loadUi("mainScreen.ui", self)
        self.title = QLabel(self)
        self.logo = QLabel(self)
        self.student_button = QPushButton('Papyrus font', self)
        self.course_data_button = QPushButton('Papyrus font', self)
        self.faculty_button = QPushButton('Papyrus font', self)
        self.setup_ui()

    def setup_ui(self):

        # Window
        self.setWindowTitle("NorthStar")
        self.resize(800, 550)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setStyleSheet("QMainWindow{background-color: rgba(35,31,32,255)}")

        # Global variables
        image_size = QSize(45, 45)
        window_width = int(self.frameGeometry().width())

        # Logo
        # pixmap_logo = QPixmap('north_star.png')
        # self.logo.setPixmap(pixmap_logo)
        # self.logo.resize(300, 300)
        # self.logo.move(300, 300)

        # Title
        title_width = 530
        self.title.setText('North Stars Registration System')
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.adjustSize()
        self.title.move(int((window_width - title_width) / 2 + 35), 50)
        self.title.setStyleSheet(
            "background-color: rgba(25,25,39,255); border: 1px solid rgba(197,15,110,255); color: rgb(255, 255, 255)")

        # Student button
        student_button_width = 160
        self.student_button.resize(student_button_width, 70)
        self.student_button.move(150, 350)
        self.student_button.setText('Student')
        self.student_button.setFont(QFont('Papyrus', 12, QFont.Bold))
        pixmap_student = QPixmap('student.png')
        self.student_button.setIcon(QIcon(pixmap_student))
        self.student_button.setIconSize(image_size)
        self.student_button.setStyleSheet(
            "QPushButton {background-color: rgba(247,247,247,255); color: rgba(25,25,39,255);} QPushButton::pressed {background-color : rgba(25,25,39,255); border: 3px solid rgba(197,15,110,255); color: rgba(247,247,247,255)}")

        # Course button
        course_image_size = QSize(20, 30)
        course_data_button_width = 170
        self.course_data_button.resize(course_data_button_width, 70)
        self.course_data_button.move(315, 350)
        self.course_data_button.setText('Course Data')
        self.course_data_button.setFont(QFont('Papyrus', 12, QFont.Bold))
        pixmap_course = QPixmap('course.png')
        self.course_data_button.setIcon(QIcon(pixmap_course))
        self.course_data_button.setIconSize(course_image_size)
        self.course_data_button.setStyleSheet(
            "QPushButton {background-color: rgba(25,25,39,255); color: rgb(255, 255, 255);} QPushButton::pressed {background-color : rgb(255, 255, 255); border: 3px solid rgba(197,15,110,255); color: rgba(25,25,39,255)}")

        # Faculty button
        faculty_button_width = 160
        self.faculty_button.resize(faculty_button_width, 70)
        self.faculty_button.move(490, 350)
        self.faculty_button.setText('Faculty')
        self.faculty_button.setFont(QFont('Papyrus', 12, QFont.Bold))
        pixmap_faculty = QPixmap('faculty.png')
        self.faculty_button.setIcon(QIcon(pixmap_faculty))
        self.faculty_button.setIconSize(image_size)
        self.faculty_button.setStyleSheet(
            "QPushButton {background-color: rgba(246,246,246,255); color: rgba(25,25,39,255)} QPushButton::pressed {background-color : rgba(25,25,39,255); border: 3px solid rgba(197,15,110,255); color: rgba(246,246,246,255);}")

        # Signals/Slots
        self.student_button.clicked.connect(self.student_button_clicked)
        self.course_data_button.clicked.connect(self.course_data_button_clicked)
        self.faculty_button.clicked.connect(self.faculty_button_clicked)


        self.show()


    def student_button_clicked(self):
        self.student_main_window = StudentMainWindow()
        self.student_main_window.show()
        self.close()

    def course_data_button_clicked(self):
        self.course_main_window = CourseMainWindow()
        self.course_main_window.show()
        self.close()

    def faculty_button_clicked(self):
        self.faculty_main_window = faculty_window_flow.FacultyMainWindow()
        self.faculty_main_window.show()
        self.close()


class StudentMainWindow(QWidget):
    def __init__(self):
        super(StudentMainWindow, self).__init__()

        self.title = QLabel(self)
        self.logo = QLabel(self)
        self.delete_student_button = QPushButton(self)
        self.update_student_button = QPushButton(self)
        self.add_student_button = QPushButton(self)
        self.maintain_student_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Student Main Window")

        # Title
        self.title.setText("Please select a Student option")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Add Button
        self.add_student_button.resize(100, 50)
        self.add_student_button.move(93, 300)
        self.add_student_button.setText('Add')

        # Update Button
        self.update_student_button.resize(100, 50)
        self.update_student_button.move(198, 300)
        self.update_student_button.setText('Update')

        # Delete Button
        self.delete_student_button.resize(100, 50)
        self.delete_student_button.move(303, 300)
        self.delete_student_button.setText('Delete')

        # Maintain Button
        self.maintain_student_button.resize(100, 50)
        self.maintain_student_button.move(408, 300)
        self.maintain_student_button.setText('Maintain')

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))

        # Signals/Slots
        # self.add_student_button.clicked.connect()
        # self.update_student_button.clicked.connect(self.)
        self.delete_student_button.clicked.connect(self.student_id_being_deleted_pop_up)
        # self.maintain_student_button.clicked.connect(self.)
        self.back_button.clicked.connect(self.back_button_clicked)


    def student_id_being_deleted_pop_up(self):
        self.popup = popup.DeleteStudentPopUp()

    def back_button_clicked(self):
        self.previous_window = MainWindow()
        self.previous_window.show()
        self.close()


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
        self.previous_window = MainWindow()
        self.previous_window.show()
        self.close()



"""Might need the code below in the future"""







