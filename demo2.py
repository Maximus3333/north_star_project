import sys
from pprint import pprint as pp
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QApplication
from PyQt5.QtGui import QFont

class GridDemo(QWidget):
    def __init__(self):
        super().__init__()

        global positions, value, position, values

        values = [  '1', '2', '3',
                    '4', '5', '6',
                    '7', '8', '9'   ]

        positions = [(r, c) for r in range(3) for c in range(3)]

        layoutGrid = QGridLayout()
        self.setLayout(layoutGrid)

        self.buttons = {}

        for position, value in zip(positions, values):
            # print('Coordinate: ' + str(positions) + ' with value of '+ str(value))
            self.buttons[position[0], position[1]] = QPushButton(value)
            self.buttons[position[0], position[1]].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.buttons[position[0], position[1]].resizeEvent = self.resizeText
            layoutGrid.addWidget(self.buttons[position[0], position[1]], *position) # widget, position --> row index, column index

    def resizeText(self, event):
        defaultSize = 9
        for position, value in zip(positions, values):
            if self.rect().width() // 40> defaultSize:
                f = QFont('', self.rect().width() // 40)
            else:
                f = QFont('', defaultSize)

            self.buttons[position[0], position[1]].setFont(f)

def main():
    app = QApplication(sys.argv)
    demo = GridDemo()
    demo.show()
    sys.exit(app.exec_())

main()