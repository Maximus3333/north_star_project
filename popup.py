from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton

import student_screen_flow





class AddStudentPopUp(QDialog):
    def __init__(self):
        super(AddStudentPopUp, self).__init__()

        self.title = QLabel(self)
        self.input_box = QLineEdit(self)
        self.btn = QPushButton(self)
        self.btn2 = QPushButton(self)

        self.setup_pop_up_box()

    def setup_pop_up_box(self):

        self.resize(330, 150)

        self.title.setText('Enter new StudentID:')
        self.title.adjustSize()
        print(self.title.height())
        self.title.move(5, 10)
        self.title2 = QLabel(self)
        self.title2.setText('Enter new Student Name:')
        self.title2.adjustSize()
        self.title2.move(5, 75)

        self.window_title = 'Add Student to School Database'
        self.setWindowTitle(self.window_title)

        self.btn.resize(75, 30)
        self.btn.move(165, 100)
        self.btn.setText('Cancel')
        self.btn2.setText('Add')
        self.btn2.resize(75, 30)
        self.btn2.move(245, 100)

        self.input_box.resize(100, 30)
        self.input_box.move(5, 30)
        self.input_box2 = QLineEdit(self)
        self.input_box2.resize(100, 30)
        self.input_box2.move(5, 100)

        self.show()

class UpdateStudentInfo(QDialog):
    def __init__(self):
        super(UpdateStudentInfo, self).__init__()

        self.title = QLabel(self)
        self.input_box = QLineEdit(self)
        self.btn = QPushButton(self)
        self.btn2 = QPushButton(self)
        self.student_current_name = QLabel(self)
        self.student_id = QLabel(self)

        self.setup_pop_up_box()

    def setup_pop_up_box(self):
        self.resize(310, 120)

        self.window_title = 'Update Student Name'
        self.setWindowTitle(self.window_title)

        self.title.setText('Enter new Student Name below')
        self.title.adjustSize()
        self.title.move(5, 20)

        self.input_box.resize(100, 30)
        self.input_box.move(5, 40)

        self.btn.setText('Cancel')
        self.btn.resize(75, 30)
        self.btn.move(145, 80)

        self.btn2.setText('Update')
        self.btn2.resize(75, 30)
        self.btn2.move(225, 80)

        self.student_current_name.adjustSize()
        self.student_current_name.move(230, 20)

        self.student_id.adjustSize()
        self.student_id.move(230, 30)

        self.show()




class AccessStudentPopUp(QDialog):
    def __init__(self, button_clicked):
        super(AccessStudentPopUp, self).__init__()

        self.title = QLabel(self)
        self.input_box = QLineEdit(self)
        self.btn = QPushButton(self)
        self.btn2 = QPushButton(self)

        self.setup_pop_up_box(button_clicked)

    def setup_pop_up_box(self, button_clicked):
        self.resize(310, 120)

        self.window_title = 'Access Student'
        self.setWindowTitle(self.window_title)

        self.title.setText('Enter StudentID to be Accessed:')
        self.title.adjustSize()
        self.title.move(5, 20)

        self.input_box.resize(100, 30)
        self.input_box.move(5, 40)

        self.btn.setText('Cancel')
        self.btn.resize(75, 30)
        self.btn.move(145, 80)

        self.btn2.setText('Access')
        self.btn2.resize(75, 30)
        self.btn2.move(225, 80)

        if button_clicked == 'Update':
            self.btn2.clicked.connect(self.update_student_popup)
        elif button_clicked == 'Maintain':
            self.btn2.clicked.connect(self.maintain_student_popup)

        self.show()

    def update_student_popup(self):
        self.popup = UpdateStudentInfo()
        self.close()

    def maintain_student_popup(self):
        self.popup = student_screen_flow.MaintainStudentAccount()
        self.close()


class AddCoursePopUp(QDialog):
    def __init__(self):
        super(AddCoursePopUp, self).__init__()

        self.title = QLabel(self)
        self.input_box = QLineEdit(self)
        self.btn = QPushButton(self)
        self.btn2 = QPushButton(self)

        self.setup_pop_up_box()

    def setup_pop_up_box(self):
        self.resize(330, 150)

        self.title.setText('Enter new CourseID:')
        self.title.adjustSize()
        print(self.title.height())
        self.title.move(5, 10)
        self.title2 = QLabel(self)
        self.title2.setText('Enter new SectionID:')
        self.title2.adjustSize()
        self.title2.move(5, 75)

        self.window_title = 'Add course to Student Schedule'
        self.setWindowTitle(self.window_title)

        self.btn.resize(75, 30)
        self.btn.move(165, 100)
        self.btn.setText('Cancel')
        self.btn2.setText('Add')
        self.btn2.resize(75, 30)
        self.btn2.move(245, 100)

        self.input_box.resize(100, 30)
        self.input_box.move(5, 30)
        self.input_box2 = QLineEdit(self)
        self.input_box2.resize(100, 30)
        self.input_box2.move(5, 100)

        self.show()

class AccessStudentCourse(QDialog):
    def __init__(self):
        super(AccessStudentCourse, self).__init__()

        self.title = QLabel(self)
        self.input_box = QLineEdit(self)
        self.btn = QPushButton(self)
        self.btn2 = QPushButton(self)

        self.setup_pop_up_box()

    def setup_pop_up_box(self):
        self.resize(330, 150)

        self.title.setText('Enter CourseID:')
        self.title.adjustSize()
        print(self.title.height())
        self.title.move(5, 10)
        self.title2 = QLabel(self)
        self.title2.setText('Enter SectionID:')
        self.title2.adjustSize()
        self.title2.move(5, 75)

        self.window_title = 'Add Course Schedule Flags'
        self.setWindowTitle(self.window_title)

        self.btn.resize(75, 30)
        self.btn.move(165, 100)
        self.btn.setText('Cancel')
        self.btn2.setText('View Section')
        self.btn2.adjustSize()
        self.btn2.move(240, 100)
        self.btn2.clicked.connect(self.section_flags_window)

        self.input_box.resize(100, 30)
        self.input_box.move(5, 30)
        self.input_box2 = QLineEdit(self)
        self.input_box2.resize(100, 30)
        self.input_box2.move(5, 100)

        self.show()

    def section_flags_window(self):
        self.popup = SectionFlags()

class SectionFlags(QDialog):
    def __init__(self):
        super(SectionFlags, self).__init__()

        self.title = QLabel(self)
        self.course_section_id = 'none'
        self.course_section_id_label = QLabel(self)
        self.credit_flag = QLabel(self)
        self.capacity_flag = QLabel(self)
        self.remove_credit_flag_btn = QPushButton(self)
        self.remove_capacity_flag_btn = QPushButton(self)
        self.cancel = QPushButton(self)

        self.setup_pop_up_box()

    def setup_pop_up_box(self):
        self.resize(330, 150)

        self.window_title = 'View Section Flags'
        self.setWindowTitle(self.window_title)

        self.course_section_id_label.setText('SectionID: ' + self.course_section_id)
        self.course_section_id_label.adjustSize()
        self.course_section_id_label.move(10, 15)

        self.credit_flag.move(10, 40)
        self.remove_credit_flag_btn.setText('Remove')
        self.remove_credit_flag_btn.adjustSize()
        self.remove_credit_flag_btn.move(240, 40)

        self.capacity_flag.move(10, 80)
        self.remove_capacity_flag_btn.setText('Remove')
        self.remove_capacity_flag_btn.adjustSize()
        self.remove_capacity_flag_btn.move(240, 80)

        self.cancel.resize(75, 30)
        self.cancel.move(253, 117)
        self.cancel.setText('Cancel')


        self.show()




