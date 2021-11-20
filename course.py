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

        # Signals/Slots
        self.add_course_or_section_button.clicked.connect(self.add_button_clicked)
        self.update_course_or_section_button.clicked.connect(self.update_button_clicked)
        self.delete_section_button.clicked.connect(self.delete_section_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = gui.MainWindow()
        self.previous_window.show()
        self.close()

    def add_button_clicked(self):
        self.course_section_window = CourseSectionAddWindow()
        self.course_section_window.show()
        self.close()

    def update_button_clicked(self):
        self.course_section_update_window = CourseSectionUpdateWindow()
        self.course_section_update_window.show()
        self.close()

    def delete_section_button_clicked(self):
        self.delete_section_window = DeleteSectionWindow()
        self.delete_section_window.show()
        self.close()
    # need to add buttons to other screens


class CourseSectionAddWindow(QWidget):
    def __init__(self):
        super(CourseSectionAddWindow, self).__init__()

        self.title = QLabel(self)
        self.add_course_button = QPushButton(self)
        self.add_section_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(400, 300)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Course Management Window")

        # Title
        self.title.setText("Add Course or Section")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Add Course Button
        self.add_course_button.resize(100, 50)
        self.add_course_button.move(50, 200)
        self.add_course_button.setText('Add Course')

        # Add Section Button
        self.add_section_button.resize(100, 50)
        self.add_section_button.move(250, 200)
        self.add_section_button.setText('Add Section')

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))

        # Signals/Slots
        self.add_section_button.clicked.connect(self.add_section_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)
        self.add_course_button.clicked.connect(self.add_course_clicked)

    def back_button_clicked(self):
        self.previous_window = CourseMainWindow()
        self.previous_window.show()
        self.close()

    def add_course_clicked(self):
        self.course_add_window = CourseAddWindow()
        self.course_add_window.show()
        self.close()

    def add_section_clicked(self):
        self.section_add_window = SectionAddWindow()
        self.section_add_window.show()
        self.close()


class CourseAddWindow(QWidget):
    def __init__(self):
        super(CourseAddWindow, self).__init__()

        self.title = QLabel(self)
        self.course_id_label = QLabel(self)
        self.course_desc_label = QLabel(self)
        self.credits_label = QLabel(self)
        self.course_id_textbox = QLineEdit(self)
        self.course_desc_textbox = QLineEdit(self)
        self.credits_textbox = QLineEdit(self)
        self.add_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        self.setWindowTitle("Course Add Window")
        window_width = int(self.frameGeometry().width())

        # Title
        self.title.setText("Enter Course Information")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Course ID Entry
        self.course_id_label.setText("Enter Course ID: ")
        self.course_id_label.resize(200, 35)
        self.course_id_label.move(100, 200)
        self.course_id_textbox.resize(150, 35)
        self.course_id_textbox.move(250, 200)

        # Course Desc Entry
        self.course_desc_label.setText("Add Description: ")
        self.course_desc_label.resize(200, 35)
        self.course_desc_label.move(100, 250)
        self.course_desc_textbox.resize(150, 35)
        self.course_desc_textbox.move(250, 250)

        # Credits Entry
        self.credits_label.setText("Credits: ")
        self.credits_label.resize(200, 35)
        self.credits_label.move(100, 300)
        self.credits_textbox.resize(150, 35)
        self.credits_textbox.move(250, 300)

        # Add Button
        self.add_button.resize(100, 75)
        self.add_button.move(450, 350)
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
        self.previous_window = CourseSectionAddWindow()
        self.previous_window.show()
        self.close()


class SectionAddWindow(QWidget):
    def __init__(self):
        super(SectionAddWindow, self).__init__()

        self.title = QLabel(self)
        self.course_id_label = QLabel(self)
        self.section_id_label = QLabel(self)
        self.instructor_label = QLabel(self)
        self.capacity_label = QLabel(self)
        self.course_id_textbox = QLineEdit(self)
        self.section_id_textbox = QLineEdit(self)
        self.instructor_textbox = QLineEdit(self)
        self.capacity_textbox = QLineEdit(self)
        self.add_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        self.setWindowTitle("Section Add Window")
        window_width = int(self.frameGeometry().width())

        # Title
        self.title.setText("Enter Section Information")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Course ID Entry
        self.course_id_label.setText("Enter Section ID: ")
        self.course_id_label.resize(200, 35)
        self.course_id_label.move(100, 150)
        self.course_id_textbox.resize(150, 35)
        self.course_id_textbox.move(250, 150)

        # Section ID Entry
        self.section_id_label.setText("Section ID: ")
        self.section_id_label.resize(200, 35)
        self.section_id_label.move(100, 200)
        self.section_id_textbox.resize(150, 35)
        self.section_id_textbox.move(250, 200)

        # Instructor ID Entry
        self.instructor_label.setText("Instructor ID: ")
        self.instructor_label.resize(200, 35)
        self.instructor_label.move(100, 250)
        self.instructor_textbox.resize(150, 35)
        self.instructor_textbox.move(250, 250)

        # Capacity Entry
        self.capacity_label.setText("Section Capacity: ")
        self.capacity_label.resize(200, 35)
        self.capacity_label.move(100, 300)
        self.capacity_textbox.resize(150, 35)
        self.capacity_textbox.move(250, 300)

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
        self.previous_window = CourseSectionAddWindow()
        self.previous_window.show()
        self.close()


class CourseSectionUpdateWindow(QWidget):
    def __init__(self):
        super(CourseSectionUpdateWindow, self).__init__()

        self.title = QLabel(self)
        self.update_course_button = QPushButton(self)
        self.update_section_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(400, 300)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Course Management Window")

        # Title
        self.title.setText("Update Course or Section")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Update Course Button
        self.update_course_button.resize(100, 50)
        self.update_course_button.move(50, 200)
        self.update_course_button.setText('Update Course')

        # Update Section Button
        self.update_section_button.resize(100, 50)
        self.update_section_button.move(250, 200)
        self.update_section_button.setText('Update Section')

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))

        # Signals/Slots
        self.update_course_button.clicked.connect(self.add_course_clicked)
        self.update_section_button.clicked.connect(self.add_section_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = CourseMainWindow()
        self.previous_window.show()
        self.close()

    def add_course_clicked(self):
        self.course_update_window = CourseUpdateWindow()
        self.course_update_window.show()
        self.close()

    def add_section_clicked(self):
        self.section_update_window = SectionUpdateWindow()
        self.section_update_window.show()
        self.close()

class CourseUpdateWindow(QWidget):
    def __init__(self):
        super(CourseUpdateWindow, self).__init__()

        self.title = QLabel(self)
        self.course_id_label = QLabel(self)
        self.course_desc_label = QLabel(self)
        self.credits_label = QLabel(self)
        self.course_id_textbox = QLineEdit(self)
        self.course_desc_textbox = QLineEdit(self)
        self.credits_textbox = QLineEdit(self)
        self.add_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        self.setWindowTitle("Course Update Window")
        window_width = int(self.frameGeometry().width())

        # Title
        self.title.setText("Update Course Information")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Course ID Entry
        self.course_id_label.setText("Update Course ID: ")
        self.course_id_label.resize(200, 35)
        self.course_id_label.move(100, 200)
        self.course_id_textbox.resize(150, 35)
        self.course_id_textbox.move(250, 200)

        # Course Desc Entry
        self.course_desc_label.setText("Update Description: ")
        self.course_desc_label.resize(200, 35)
        self.course_desc_label.move(100, 250)
        self.course_desc_textbox.resize(150, 35)
        self.course_desc_textbox.move(250, 250)

        # Credits Entry
        self.credits_label.setText("Update Credits: ")
        self.credits_label.resize(200, 35)
        self.credits_label.move(100, 300)
        self.credits_textbox.resize(150, 35)
        self.credits_textbox.move(250, 300)

        # Add Button
        self.add_button.resize(100, 75)
        self.add_button.move(450, 350)
        self.add_button.setText('Update')
        self.add_button.setFont(QFont('Papyrus', 7, QFont.Bold))

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))

        # Signals/Slots
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = CourseSectionUpdateWindow()
        self.previous_window.show()
        self.close()


class SectionUpdateWindow(QWidget):
    def __init__(self):
        super(SectionUpdateWindow, self).__init__()

        self.title = QLabel(self)
        self.course_id_label = QLabel(self)
        self.section_id_label = QLabel(self)
        self.instructor_label = QLabel(self)
        self.capacity_label = QLabel(self)
        self.course_id_textbox = QLineEdit(self)
        self.section_id_textbox = QLineEdit(self)
        self.instructor_textbox = QLineEdit(self)
        self.capacity_textbox = QLineEdit(self)
        self.add_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        self.setWindowTitle("Section Update Window")
        window_width = int(self.frameGeometry().width())

        # Title
        self.title.setText("Update Section Information")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Course ID Entry
        self.course_id_label.setText("Existing Course ID: ")
        self.course_id_label.resize(200, 35)
        self.course_id_label.move(100, 150)
        self.course_id_textbox.resize(150, 35)
        self.course_id_textbox.move(250, 150)

        # Section ID Entry
        self.section_id_label.setText("Section ID to Update: ")
        self.section_id_label.resize(200, 35)
        self.section_id_label.move(100, 200)
        self.section_id_textbox.resize(150, 35)
        self.section_id_textbox.move(250, 200)

        # Instructor ID Entry
        self.instructor_label.setText("Update Instructor ID: ")
        self.instructor_label.resize(200, 35)
        self.instructor_label.move(100, 250)
        self.instructor_textbox.resize(150, 35)
        self.instructor_textbox.move(250, 250)

        # Capacity Entry
        self.capacity_label.setText("Update Capacity: ")
        self.capacity_label.resize(200, 35)
        self.capacity_label.move(100, 300)
        self.capacity_textbox.resize(150, 35)
        self.capacity_textbox.move(250, 300)

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
        self.previous_window = CourseSectionUpdateWindow()
        self.previous_window.show()
        self.close()

class DeleteSectionWindow(QWidget):
    def __init__(self):
        super(DeleteSectionWindow, self).__init__()

        self.title = QLabel(self)
        self.delete_section_button = QPushButton(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Delete Section Window")

        # Title
        self.title.setText("Delete Section")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(int((window_width - self.title.width()) / 2), 100)

        # Delete Section Button
        self.delete_section_button.resize(100, 50)
        self.delete_section_button.move(245, 300)
        self.delete_section_button.setText("Delete Section")

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)

        #Signals/Slots
        self.delete_section_button.clicked.connect(self.delete_section_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = gui.MainWindow()
        self.previous_window.show()
        self.close()

    def delete_section_button_clicked(self):
        self.access_sections_window = AccessSectionsWindow()
        self.access_sections_window.show()
        self.close()

class AccessSectionsWindow(QWidget):
    def __init__(self):
        super(AccessSectionsWindow, self).__init__()

        self.title = QLabel(self)
        self.access_sections_button = QPushButton(self)
        self.input_box = QLineEdit(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Access Sections Window")

        # Title
        self.title.setText("Enter Existing Course:")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(15, 100)

        # Input Box
        self.input_box.resize(200, 30)
        self.input_box.move(350, 107)

        # Access Sections Button
        self.access_sections_button.resize(100, 50)
        self.access_sections_button.move(245, 300)
        self.access_sections_button.setText("Access Sections")

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)

        #Signals / Slots
        self.access_sections_button.clicked.connect(self.access_sections_button_clicked)
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = DeleteSectionWindow()
        self.previous_window.show()
        self.close()

    def access_sections_button_clicked(self):
        self.section_deletion_window = SectionDeletionWindow()
        self.section_deletion_window.show()
        self.close()

class SectionDeletionWindow(QWidget):
    def __init__(self):
        super(SectionDeletionWindow, self).__init__()

        self.title = QLabel(self)
        self.section_deletion_button = QPushButton(self)
        self.input_box = QLineEdit(self)
        self.back_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        # Window
        self.resize(600, 500)
        window_width = int(self.frameGeometry().width())
        self.setWindowTitle("Section Deletion Window")

        # Title
        self.title.setText("Enter Section ID:")
        self.title.setFont(QFont('Papyrus', 16, QFont.Bold))
        self.title.adjustSize()
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.move(15, 100)

        # Input Box
        self.input_box.resize(200, 30)
        self.input_box.move(350, 107)

        # Delete Button
        self.section_deletion_button.resize(100, 50)
        self.section_deletion_button.move(245, 300)
        self.section_deletion_button.setText("Delete")

        # Back Button
        self.back_button.resize(50, 35)
        self.back_button.move(30, 30)
        self.back_button.setText('Back')
        self.back_button.setFont(QFont('Papyrus', 7, QFont.Bold))
        self.back_button.clicked.connect(self.back_button_clicked)

        #Signals / Slots
        self.back_button.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        self.previous_window = AccessSectionsWindow()
        self.previous_window.show()
        self.close()
