import sqlite3
from PyQt5.QtGui import * 
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, QMessageBox, QWidget, QDialog
import pandas as pd
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
        #MainWindow
        self.setWindowTitle("NorthStar")
        self.setGeometry(50, 50, 800, 550)
        self.setStyleSheet("QMainWindow{background-color: rgba(35,31,32,255)}")


        #Global variables
        image_size = QSize(45, 45)
        window_width = self.frameGeometry().width()

        #Logo
        # pixmap_logo = QPixmap('north_star.png')
        # self.logo.setPixmap(pixmap_logo)
        # self.logo.resize(300, 300)
        # self.logo.move(300, 300)


        # Title
        title_width = 530
        self.title.setText('North Stars Registration System')
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        # self.title.resize(380, 50)
        # self.title.move((window_width+50 - (self.title.width()))/2, 50)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setGeometry((window_width - title_width)/2 + 35, 50, title_width, 60)
        self.title.setStyleSheet("background-color: rgba(25,25,39,255); border: 1px solid rgba(197,15,110,255); color: rgb(255, 255, 255)")


        print(self.title.styleSheet())

        #Student button
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
        print(self.student_button.styleSheet())



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
        self.course_data_button.setStyleSheet("QPushButton {background-color: rgba(25,25,39,255); color: rgb(255, 255, 255);} QPushButton::pressed {background-color : rgb(255, 255, 255); border: 3px solid rgba(197,15,110,255); color: rgba(25,25,39,255)}")



        # Faculty button
        faculty_button_width = 160
        self.faculty_button.resize(faculty_button_width, 70)
        self.faculty_button.move(490, 350)
        self.faculty_button.setText('Faculty')
        self.faculty_button.setFont(QFont('Papyrus', 12, QFont.Bold))
        pixmap_faculty = QPixmap('faculty.png')
        self.faculty_button.setIcon(QIcon(pixmap_faculty))
        self.faculty_button.setIconSize(image_size)
        self.faculty_button.setStyleSheet("QPushButton {background-color: rgba(246,246,246,255); color: rgba(25,25,39,255)} QPushButton::pressed {background-color : rgba(25,25,39,255); border: 3px solid rgba(197,15,110,255); color: rgba(246,246,246,255);}")

        
        # self.show()

def main():
    windows = QtWidgets.QStackedWidget()

    app = QApplication(sys.argv)
    # widget = QtWidgets.QStackedWidget()
    mainwindow = MainWindow()
    windows.addWidget(mainwindow)
    windows.show()

    # print(mainwindow.size())
    # print(widget.currentIndex())
    # print(widget.count())

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

main()


#     def student_button_clicked(self):
#
# class StudentMainWindow(QDialog):
#     def student_main_window(QDialog):
#         def __init__(self):
#             super().__init__()






# app = QApplication(sys.argv)
# windows = QtWidgets.QStackedWidget()
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