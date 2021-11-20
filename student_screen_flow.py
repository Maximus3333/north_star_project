import sqlite3
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, \
    QMessageBox, QWidget, QDialog, QInputDialog, QToolButton, QSizePolicy
import pandas as pd

import course
import popup
import gui
import sys

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
        self.add_student_button.clicked.connect(self.student_being_added_popup)
        self.update_student_button.clicked.connect(self.student_being_updated)
        self.delete_student_button.clicked.connect(self.student_id_being_deleted_pop_up)
        self.maintain_student_button.clicked.connect(self.student_being_maintained)
        self.back_button.clicked.connect(self.back_button_clicked)


    def student_id_being_deleted_pop_up(self):
        self.window = DeleteStudentWindow()
        self.close()
        self.window.show()

    def student_being_added_popup(self):
        self.window = AddStudentWindow()
        self.close()
        self.window.show()


    def student_being_updated(self):
        self.window = AccessStudentWindow('Update')
        self.close()
        self.window.show()

    def student_being_maintained(self):
        self.window = AccessStudentWindow('Maintain')
        self.close()
        self.window.show()

    def back_button_clicked(self):
        self.previous_window = gui.MainWindow()
        self.previous_window.show()
        self.close()


class MaintainStudentAccount(QDialog):
    def __init__(self):
        super(MaintainStudentAccount, self).__init__()


        self.add_course_to_schedule_btn = QPushButton(self)
        self.access_student_flags_btn = QPushButton(self)
        self.print_student_info_btn = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):

        self.resize(600, 500)

        # self.widget = QWidget(self)
        # self.widget.resize(500, 300)

        self.add_course_to_schedule_btn.setText('Add Course to \n Student Schedule')
        self.add_course_to_schedule_btn.adjustSize()
        self.add_course_to_schedule_btn.move(60, 250)
        self.add_course_to_schedule_btn.resize(130, 60)
        self.add_course_to_schedule_btn.clicked.connect(self.add_course_student_schedule_pop_up)

        self.access_student_flags_btn.setText('Access Student \n Flags')
        self.access_student_flags_btn.adjustSize()
        self.access_student_flags_btn.move(((self.width()-(self.add_course_to_schedule_btn.width()+self.print_student_info_btn.width()+120
                                            +self.access_student_flags_btn.width()))/2)+60+self.add_course_to_schedule_btn.width(), 250)
        self.access_student_flags_btn.resize(130, 60)
        self.access_student_flags_btn.clicked.connect(self.access_student_flags_popup)

        self.print_student_info_btn.setText('Add Preview \n Student Info')
        self.print_student_info_btn.adjustSize()
        self.print_student_info_btn.move(self.width()-(self.print_student_info_btn.width()+60), 250)
        self.print_student_info_btn.resize(130, 60)
        print(self.print_student_info_btn.pos())

        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)


        self.show()

    def print_student_info(self):
        pass

    def add_course_student_schedule_pop_up(self):
        self.window = AddCourseToStudentScheduleWindow()
        self.window.show()
        self.close()

    def access_student_flags_popup(self):
        self.window = AccessStudentCourseFlagsWindow()
        self.window.show()
        self.close()

    def back_button_clicked(self):
        self.previous_window = StudentMainWindow()
        self.previous_window.show()
        self.close()


class CourseFlagsWindow(QWidget):
    def __init__(self):
        super(CourseFlagsWindow, self).__init__()

        self.title = QLabel(self)
        self.course_section_id = 'none'
        self.course_section_id_label = QLabel(self)
        self.credit_flag = QLabel(self)
        self.capacity_flag = QLabel(self)
        self.remove_credit_flag_btn = QPushButton(self)
        self.remove_capacity_flag_btn = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_pop_up_box()

    def setup_pop_up_box(self):
        self.resize(600, 500)

        self.window_title = 'View Section Flags Window'
        self.setWindowTitle(self.window_title)

        self.course_section_id_label.setText('SectionID: ' + self.course_section_id)
        self.course_section_id_label.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.course_section_id_label.move(150, 50)

        self.credit_flag.move(100, 200)
        self.credit_flag.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.remove_credit_flag_btn.setText('Remove')
        self.remove_credit_flag_btn.adjustSize()
        self.remove_credit_flag_btn.move(450, 200)

        self.capacity_flag.move(100, 300)
        self.capacity_flag.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.remove_capacity_flag_btn.setText('Remove')
        self.remove_capacity_flag_btn.adjustSize()
        self.remove_capacity_flag_btn.move(450, 300)

        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))

        self.back_button.clicked.connect(self.back_button_clicked)

        self.show()

    def back_button_clicked(self):
        self.previous_window = MaintainStudentAccount()
        self.previous_window.show()
        self.close()


class AccessStudentCourseFlagsWindow(QWidget):
    def __init__(self):
        super(AccessStudentCourseFlagsWindow, self).__init__()

        self.title = QLabel(self)
        self.course_id_label = QLabel(self)
        self.section_id_label = QLabel(self)
        self.course_id_textbox = QLineEdit(self)
        self.section_id_textbox = QLineEdit(self)
        self.access_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        self.setWindowTitle("Add Course To Schedule Window")
        window_width = int(self.frameGeometry().width())

        # Title
        self.title.setText("Enter Course Information")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Student Name Entry
        self.course_id_label.setText("Enter Course ID: ")
        self.course_id_label.resize(200, 35)
        self.course_id_label.move(100, 150)
        self.course_id_textbox.resize(150, 35)
        self.course_id_textbox.move(250, 150)

        # Student ID Entry
        self.section_id_label.setText("Enter Section ID: ")
        self.section_id_label.resize(200, 35)
        self.section_id_label.move(100, 200)
        self.section_id_textbox.resize(150, 35)
        self.section_id_textbox.move(250, 200)

        # Add Button
        self.access_button.resize(100, 75)
        self.access_button.move(450, 375)
        self.access_button.setText('Access')
        self.access_button.setFont(QFont('Papyrus', 7, QFont.Bold))

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))

        # Signals/Slots
        self.back_button.clicked.connect(self.back_button_clicked)
        self.access_button.clicked.connect(self.course_flags_window)

    def back_button_clicked(self):
        self.previous_window = MaintainStudentAccount()
        self.previous_window.show()
        self.close()

    def course_flags_window(self):
        self.window = CourseFlagsWindow()
        self.window.show()
        self.close()


class AddCourseToStudentScheduleWindow(QWidget):
    def __init__(self):
        super(AddCourseToStudentScheduleWindow, self).__init__()

        self.title = QLabel(self)
        self.course_id_label = QLabel(self)
        self.section_id_label = QLabel(self)
        self.course_id_textbox = QLineEdit(self)
        self.section_id_textbox = QLineEdit(self)
        self.add_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        self.setWindowTitle("Add Course To Schedule Window")
        window_width = int(self.frameGeometry().width())

        # Title
        self.title.setText("Enter Course Information")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Student Name Entry
        self.course_id_label.setText("Enter Course ID: ")
        self.course_id_label.resize(200, 35)
        self.course_id_label.move(100, 150)
        self.course_id_textbox.resize(150, 35)
        self.course_id_textbox.move(250, 150)

        # Student ID Entry
        self.section_id_label.setText("Enter Section ID: ")
        self.section_id_label.resize(200, 35)
        self.section_id_label.move(100, 200)
        self.section_id_textbox.resize(150, 35)
        self.section_id_textbox.move(250, 200)

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
        self.previous_window = MaintainStudentAccount()
        self.previous_window.show()
        self.close()


class AddStudentWindow(QWidget):
    def __init__(self):
        super(AddStudentWindow, self).__init__()

        self.title = QLabel(self)
        self.new_student_id_label = QLabel(self)
        self.new_student_id_label = QLabel(self)
        self.new_student_name_textbox = QLineEdit(self)
        self.new_student_name_textbox = QLineEdit(self)
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
        self.new_student_name_label.setText("Enter Student Name: ")
        self.new_student_name_label.resize(200, 35)
        self.new_student_name_label.move(100, 150)
        self.new_student_name_textbox.resize(150, 35)
        self.new_student_name_textbox.move(250, 150)

        # Student ID Entry
        self.new_student_id_label.setText("Enter Student ID: ")
        self.new_student_id_label.resize(200, 35)
        self.new_student_id_label.move(100, 200)
        self.new_student_id_textbox.resize(150, 35)
        self.new_student_id_textbox.move(250, 200)

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
        self.previous_window = StudentMainWindow()
        self.previous_window.show()
        self.close()


class DeleteStudentWindow(QDialog):
    def __init__(self):
        super(DeleteStudentWindow, self).__init__()

        self.title = QLabel(self)
        self.delete_student_button = QPushButton(self)
        self.input_box = QLineEdit(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Delete Student From Database")

        # Title
        self.title.setText("Enter Student ID:")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(15, 100)

        # Input Box
        self.input_box.resize(200, 30)
        self.input_box.move(350, 107)

        # Delete Button
        self.delete_student_button.resize(100, 50)
        self.delete_student_button.move(245, 300)
        self.delete_student_button.setText("Delete")

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)

        # Signals / Slots
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = StudentMainWindow()
        self.previous_window.show()
        self.close()

class AccessStudentWindow(QWidget):
    def __init__(self, button_clicked):
        super(AccessStudentWindow, self).__init__()

        self.title = QLabel(self)
        self.access_student_button = QPushButton(self)
        self.input_box = QLineEdit(self)
        self.back_button = QPushButton(self)
        self.button_clicked = button_clicked

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Access Student Window")

        # Title
        self.title.setText("Enter Existing Student:")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(15, 100)

        # Input Box
        self.input_box.resize(200, 30)
        self.input_box.move(350, 107)

        # Access Sections Button
        self.access_student_button.resize(100, 50)
        self.access_student_button.move(245, 300)
        self.access_student_button.setText("Access Student")

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)

        # Signals / Slots
        self.back_button.clicked.connect(self.back_button_clicked)

        if self.button_clicked == 'Update':
            self.access_student_button.clicked.connect(self.update_student_window)
            self.close()
        elif self.button_clicked == 'Maintain':
            self.access_student_button.clicked.connect(self.maintain_student_window)
            self.close()

        self.show()

    def update_student_window(self):
        self.window = UpdateStudentWindow()
        self.close()
        self.window.show()

    def maintain_student_window(self):
        self.window = MaintainStudentAccount()
        self.close()
        self.window.show()

    def back_button_clicked(self):
        self.previous_window = StudentMainWindow()
        self.previous_window.show()
        self.close()

class AddStudentWindow(QWidget):
    def __init__(self):
        super(AddStudentWindow, self).__init__()

        self.title = QLabel(self)
        self.new_student_name_label = QLabel(self)
        self.new_student_id_label = QLabel(self)
        self.new_student_name_textbox = QLineEdit(self)
        self.new_student_id_textbox = QLineEdit(self)
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
        self.new_student_name_label.setText("Enter Student Name: ")
        self.new_student_name_label.resize(200, 35)
        self.new_student_name_label.move(100, 150)
        self.new_student_name_textbox.resize(150, 35)
        self.new_student_name_textbox.move(250, 150)

        # Student ID Entry
        self.new_student_id_label.setText("Enter Student ID: ")
        self.new_student_id_label.resize(200, 35)
        self.new_student_id_label.move(100, 200)
        self.new_student_id_textbox.resize(150, 35)
        self.new_student_id_textbox.move(250, 200)

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
        self.previous_window = StudentMainWindow()
        self.previous_window.show()
        self.close()

class UpdateStudentWindow(QDialog):
    def __init__(self):
        super(UpdateStudentWindow, self).__init__()

        self.title = QLabel(self)
        self.Update_student_button = QPushButton(self)
        self.input_box = QLineEdit(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Update Student Window")

        # Title
        self.title.setText("Enter new Student Name:")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(15, 100)

        # Input Box
        self.input_box.resize(200, 30)
        self.input_box.move(350, 107)

        # Delete Button
        self.Update_student_button.resize(100, 50)
        self.Update_student_button.move(245, 300)
        self.Update_student_button.setText("Update")

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)

        # Signals / Slots
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = StudentMainWindow()
        self.previous_window.show()
        self.close()