from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit)
from PyQt5.QtGui import QIcon, QFont 
from PyQt5.QtCore import Qt
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.st = ""
        self.initUI()

    def initUI(self):
        self.setGeometry(1000, 300, 450, 700)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("pyqt5//pyqt5//image.png"))
        self.setStyleSheet("background-color: black")

        self.kiritish = QLineEdit(self)
        self.kiritish.setPlaceholderText(self.st)
        self.kiritish.setFont(QFont("Arial", 50))
        self.kiritish.setStyleSheet("color: white; border: 3 solid white; border-radius: 10")
        self.kiritish.setAlignment(Qt.AlignRight)
        self.kiritish.setFixedWidth(405)
        self.kiritish.move(20, 100)

        self.createButtons()
        
        self.show()

    def createButtons(self):
        button_styles = "color:white; background-color: #2b2e33; border-radius: 48px"
        operator_styles = "color:white; background-color: #faa907; border-radius: 48px"

        self.buttons = {
            '0': (5, 600, 200, 96, self.f_nol),
            '1': (5, 495, 96, 96, self.f_bir),
            '2': (110, 495, 96, 96, self.f_ikki),
            '3': (215, 495, 96, 96, self.f_uch),
            '4': (5, 390, 96, 96, self.f_tort),
            '5': (110, 390, 96, 96, self.f_besh),
            '6': (215, 390, 96, 96, self.f_olti),
            '7': (5, 284, 96, 96, self.f_yetti),
            '8': (110, 284, 96, 96, self.f_sakkiz),
            '9': (215, 284, 96, 96, self.f_toqqiz),
            '.': (215, 600, 96, 96, self.f_belgi),
            '=': (330, 600, 96, 96, self.jami),
            '+': (330, 495, 96, 96, self.plus_ozgartir),
            '-': (330, 390, 96, 96, self.minus_ozgartir),
            '×': (330, 284, 96, 96, self.kop_ozgartir),
            '÷': (330, 180, 96, 96, self.bolish_ozgartir),
            'AC': (5, 180, 96, 96, self.os),
            '+/-': (110, 180, 96, 96, self.manfiy),
            '%': (215, 180, 96, 96, self.f_foiz)
        }

        for text, (x, y, width, height, func) in self.buttons.items():
            button = QPushButton(text, self)
            button.setFont(QFont("Arial", 45))
            button.setFixedSize(width, height)
            button.setStyleSheet(operator_styles if text in '+-×÷=' else button_styles)
            button.move(x, y)
            button.setCursor(Qt.PointingHandCursor)
            button.clicked.connect(func)
            button.pressed.connect(self.ozgartirish)
            button.released.connect(self.qaytar)

    def os(self):
        self.st = ""
        self.kiritish.clear()

    def jami(self):
        expression = self.st
        try:
            result = eval(expression.replace('÷', '/'))
            self.kiritish.setText(str(result))
        except Exception as e:
            self.kiritish.setText("error")

    def f_nol(self):
        self.st += '0'
        self.kiritish.setText(self.st)

    def f_bir(self):
        self.st += '1'
        self.kiritish.setText(self.st)

    def f_ikki(self):
        self.st += '2'
        self.kiritish.setText(self.st)

    def f_uch(self):
        self.st += '3'
        self.kiritish.setText(self.st)

    def f_tort(self):
        self.st += '4'
        self.kiritish.setText(self.st)

    def f_besh(self):
        self.st += '5'
        self.kiritish.setText(self.st)

    def f_olti(self):
        self.st += '6'
        self.kiritish.setText(self.st)

    def f_yetti(self):
        self.st += '7'
        self.kiritish.setText(self.st)

    def f_sakkiz(self):
        self.st += '8'
        self.kiritish.setText(self.st)

    def f_toqqiz(self):
        self.st += '9'
        self.kiritish.setText(self.st)

    def f_belgi(self):
        self.st += '.'
        self.kiritish.setText(self.st)

    def f_foiz(self):
        self.st += '%'
        self.kiritish.setText(self.st)

    def manfiy(self):
        if self.st and self.st[-1] not in '+-*/%÷':
            self.st = '-' + self.st
        self.kiritish.setText(self.st)

    def plus_ozgartir(self):
        self.st += '+'
        self.kiritish.setText(self.st)

    def minus_ozgartir(self):
        self.st += '-'
        self.kiritish.setText(self.st)

    def kop_ozgartir(self):
        self.st += '*'
        self.kiritish.setText(self.st)

    def bolish_ozgartir(self):
        self.st += '÷'
        self.kiritish.setText(self.st)

    def ozgartirish(self):
        button = self.sender()
        button.setStyleSheet('color: black; background-color: #7a7a78; border-radius: 45')

    def qaytar(self):
        button = self.sender()
        button.setStyleSheet('color: white; background-color: #2b2e33; border-radius: 45')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())
