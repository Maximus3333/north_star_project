# File Is for Creating popups that throw ERRORS!
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ErrorPopUp(QDialog):
    def __init__(self, error_type):
        super(ErrorPopUp, self).__init__()

        self.error_type = error_type
        self.setup_pop_up_box()

    def setup_pop_up_box(self):
        self.title = QLabel(self)

        self.title.setText(self.error_type + "!")
        self.title.adjustSize()
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout = QGridLayout()
        self.layout.addWidget(self.title, 0, 0)

        self.setLayout(self.layout)

        self.window_title = 'Error!'
        self.setWindowTitle(self.window_title)

        self.show()


class SuccessPopUp(QDialog):
    def __init__(self, success_type):
        super(SuccessPopUp, self).__init__()

        self.success_type = success_type
        self.setup_pop_up_box()

    def setup_pop_up_box(self):
        self.title = QLabel(self)

        self.title.setText(self.success_type + "!")
        self.title.adjustSize()
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.layout = QGridLayout()
        self.layout.addWidget(self.title, 0, 0)

        self.setLayout(self.layout)

        self.window_title = 'Success!'
        self.setWindowTitle(self.window_title)

        self.show()
