# File Is for Creating popups that throw ERRORS!
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton


class ErrorPopUp(QDialog):
    def __init__(self):
        super(ErrorPopUp, self).__init__()


        self.setup_pop_up_box()

    def setup_pop_up_box(self):

        self.resize(330, 140)

        self.title = QLabel(self)

        self.title.setText('Error Adding to the Databse')
        self.title.adjustSize()
        print(self.title.height())
        self.title.move(5, 20)

        self.window_title = 'Error!'
        self.setWindowTitle(self.window_title)

        self.show()
