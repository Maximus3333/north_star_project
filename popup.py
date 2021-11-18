from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton






class DeleteStudentPopUp(QDialog):
    def __init__(self):
        super(DeleteStudentPopUp, self).__init__()


        self.setup_pop_up_box()


    def setup_pop_up_box(self):


        self.resize(310, 120)
        self.title = QLabel(self)
        self.input_box = QLineEdit(self)
        self.btn = QPushButton(self)
        self.btn2 = QPushButton(self)
        self.title.setText('Enter StudentID to be deleted:')
        self.window_title = 'Enter StudentID to be deleted:'
        self.btn.setText('Cancel')
        self.btn2.setText('Delete')

        self.setWindowTitle(self.window_title)

        self.title.adjustSize()
        self.title.move(5, 20)

        self.input_box.resize(100, 30)
        self.input_box.move(5, 40)

        self.btn.resize(75, 30)
        self.btn.move(145, 80)

        self.btn2.resize(75, 30)
        self.btn2.move(225, 80)
        self.show()


class AddStudentPopUp(QDialog):
    def __init__(self):
        super(AddStudentPopUp, self).__init__()


        self.setup_pop_up_box()

    def setup_pop_up_box(self):

        self.resize(330, 140)

        self.title = QLabel(self)
        self.input_box = QLineEdit(self)
        self.btn = QPushButton(self)
        self.btn2 = QPushButton(self)

        self.title.setText('Enter StudentID:')
        self.title.adjustSize()
        print(self.title.height())
        self.title.move(5, 20)
        self.title2 = QLabel(self)
        self.title2.setText('Enter Student Name:')
        self.title2.adjustSize()
        self.title2.move(5, 80)

        self.window_title = 'Add Student:'
        self.setWindowTitle(self.window_title)

        self.btn.resize(75, 30)
        self.btn.move(165, 100)
        self.btn.setText('Cancel')
        self.btn2.setText('Add')
        self.btn2.resize(75, 30)
        self.btn2.move(245, 100)

        self.input_box.resize(100, 30)
        self.input_box.move(5, 40)
        self.input_box2 = QLineEdit(self)
        self.input_box2.resize(100, 30)
        self.input_box2.move(5, 100)

        self.show()




