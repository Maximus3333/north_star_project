from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton


class InputPopUpBox(QDialog):
    def __init__(self):
        super().__init__()

        self.window_title = None
        self.title = QLabel(self)
        self.input_box = QLineEdit(self)
        self.btn = QPushButton(self)
        self.btn2 = QPushButton(self)




    def setup_pop_up_box(self):


        self.setWindowTitle(self.window_title)

        self.title.adjustSize()
        self.title.move(5, 20)

        self.input_box.resize(100, 30)
        self.input_box.move(5, 40)

        self.btn.resize(75, 30)
        self.btn.move(145, 80)

        self.btn2.resize(75, 30)
        self.btn2.move(225, 80)

class DeleteStudentPopUp(InputPopUpBox):
    def __init__(self):
        super(DeleteStudentPopUp, self).__init__()

        self.resize(310, 120)

        self.title.setText('Enter StudentID to be deleted:')
        self.window_title = 'Enter StudentID to be deleted:'
        self.btn.setText('Cancel')
        self.btn2.setText('Delete')
        self.setup_pop_up_box()
        self.show()