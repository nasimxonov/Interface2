from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout
import sys

class TetrisGame(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tetris Figures')
        self.setGeometry(100, 100, 400, 400)

        self.main_layout = QVBoxLayout()

        self.button_layout = QGridLayout()

        self.figure_layout = QGridLayout()

        self.btn1 = QPushButton('Figure 1', self)
        self.btn2 = QPushButton('Figure 2', self)
        self.btn3 = QPushButton('Figure 3', self)
        self.btn4 = QPushButton('Figure 4', self)

        self.btn1.clicked.connect(self.draw_figure_1)
        self.btn2.clicked.connect(self.draw_figure_2)
        self.btn3.clicked.connect(self.draw_figure_3)
        self.btn4.clicked.connect(self.draw_figure_4)

        self.button_layout.addWidget(self.btn1, 0, 0)
        self.button_layout.addWidget(self.btn2, 0, 1)
        self.button_layout.addWidget(self.btn3, 0, 2)
        self.button_layout.addWidget(self.btn4, 0, 3)

        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addLayout(self.figure_layout)

        self.setLayout(self.main_layout)

    def draw_figure_1(self):
        self.clear_figure_layout()
        for i in range(3):
            btn = QPushButton()
            btn.setStyleSheet("background-color: red;")
            self.figure_layout.addWidget(btn, i, 1)
        btn = QPushButton()
        btn.setStyleSheet("background-color: red;")
        self.figure_layout.addWidget(btn, 1, 0)

    def draw_figure_2(self):
        self.clear_figure_layout()
        for i in range(2):
            for j in range(2):
                btn = QPushButton()
                btn.setStyleSheet("background-color: green;")
                self.figure_layout.addWidget(btn, i, j)

    def draw_figure_3(self):
        self.clear_figure_layout()
        for i in range(4):
            btn = QPushButton()
            btn.setStyleSheet("background-color: blue;")
            self.figure_layout.addWidget(btn, 0, i)

    def draw_figure_4(self):
        self.clear_figure_layout()
        btn = QPushButton()
        btn.setStyleSheet("background-color: yellow;")
        self.figure_layout.addWidget(btn, 0, 0)
        btn = QPushButton()
        btn.setStyleSheet("background-color: yellow;")
        self.figure_layout.addWidget(btn, 0, 1)
        btn = QPushButton()
        btn.setStyleSheet("background-color: yellow;")
        self.figure_layout.addWidget(btn, 1, 1)
        btn = QPushButton()
        btn.setStyleSheet("background-color: yellow;")
        self.figure_layout.addWidget(btn, 1, 2)

    def clear_figure_layout(self):
        for i in reversed(range(self.figure_layout.count())):
            widget = self.figure_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tetris = TetrisGame()
    tetris.show()
    sys.exit(app.exec_())
