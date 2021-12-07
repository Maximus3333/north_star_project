import sqlite3
from PyQt5.QtGui import * 
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, \
    QMessageBox, QWidget, QDialog, QInputDialog, QSizePolicy
import pandas as pd
import os
import course
import faculty_window_flow
import student_screen_flow
import popup
import sys


"""
!!!!!! Define window classes first then figure out way
       to switch between screens with QStackeWidget
"""


class Student:
    def __init__(self):

        self.studentid = 0
        self.name = 'none'

    def update_student_id(self, studentid):
        self.studentid = studentid

    def update_student_name(self, name):
        self.name = name

class Course:
    def __init__(self):

        self.course_id = 0
        self.description = 'none'
        self.course_credits = 0

class CourseSection:
    def __init__(self, course_id):

        self.course_id = course_id
        self.section_id = 0
        self.instructor_id = 0
        self.section_capacity = 0

class Instructor:
    def __init__(self):

        self.instructor_id = 0
        self.instructor_name = 'none'

class Enrollment:
    def __init__(self):

        self.student_id = 'none'
        self.course_section_id = 'none'
        self.over_cred_flag = 0
        self.over_cap_flag = 0

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # loadUi("mainScreen.ui", self)
        self.title = QLabel(self)
        self.logo = QLabel(self)
        self.student_button = QPushButton('Georgia font', self)
        self.course_data_button = QPushButton('Georgia font', self)
        self.faculty_button = QPushButton('Georgia font', self)
        self.setup_ui()

    def setup_ui(self):

        # Window
        self.setWindowTitle("NorthStar")
        self.resize(800, 500)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setStyleSheet("QMainWindow{background-color: #000202}")

        # Global variables
        image_size = QSize(30, 40)
        window_width = int(self.frameGeometry().width())

        # Logo
        pixmap_logo = QPixmap('logo.png')
        self.logo.setPixmap(pixmap_logo)
        self.logo.adjustSize()
        self.logo.move(30, 20)

        # Title

        self.title.setText('North Stars Registration System')
        self.title.setFont(QFont('Georgia', 22, QFont.Bold))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.adjustSize()
        self.title.move(int((window_width - self.title.width()) / 2), 50)
        self.title.adjustSize()
        self.title.setStyleSheet(
            "color: #fb9c20")

        # Student button
        student_button_width = 160
        self.student_button.resize(student_button_width, 70)
        self.student_button.move(150, 300)
        self.student_button.setText('Student')
        self.student_button.setFont(QFont('Georgia', 12, QFont.Bold))
        pixmap_student = QPixmap('student.png')
        self.student_button.setIcon(QIcon(pixmap_student))
        self.student_button.setIconSize(image_size)
        self.student_button.setStyleSheet(
            "QPushButton {background-color: rgba(247,247,247,255); color: rgba(25,25,39,255);} QPushButton::pressed {background-color : rgba(25,25,39,255); border: 3px solid rgba(197,15,110,255); color: rgba(247,247,247,255)}")
        # Course button
        course_data_button_width = 170
        self.course_data_button.resize(course_data_button_width, 70)
        self.course_data_button.move(315, 300)
        self.course_data_button.setText('Course Data')
        self.course_data_button.setFont(QFont('Georgia', 12, QFont.Bold))
        pixmap_course = QPixmap('course.png')
        self.course_data_button.setIcon(QIcon(pixmap_course))
        self.course_data_button.setIconSize(image_size)
        self.course_data_button.setStyleSheet(
            "QPushButton {background-color: rgba(247,247,247,255); color: rgba(25,25,39,255);} QPushButton::pressed {background-color : rgb(255, 255, 255); border: 3px solid rgba(197,15,110,255); color: rgba(25,25,39,255)}")


        # Faculty button
        faculty_button_width = 160
        self.faculty_button.resize(faculty_button_width, 70)
        self.faculty_button.move(490, 300)
        self.faculty_button.setText('Faculty')
        self.faculty_button.setFont(QFont('Georgia', 12, QFont.Bold))
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
        self.student_main_window = student_screen_flow.StudentMainWindow()
        self.student_main_window.show()
        self.close()


    def course_data_button_clicked(self):
        self.course_main_window = course.CourseMainWindow()
        self.course_main_window.show()
        self.close()

    def faculty_button_clicked(self):
        self.faculty_main_window = faculty_window_flow.FacultyMainWindow()
        self.faculty_main_window.show()
        self.close()









"""Might need the code below in the future"""







