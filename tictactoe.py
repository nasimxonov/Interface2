import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.board = [['' for _ in range(3)] for _ in range(3)]  

        for row in range(3):
            for col in range(3):
                button = QPushButton('')
                button.setFixedSize(100, 100)
                button.clicked.connect(lambda checked, r=row, c=col: self.on_button_clicked(r, c))
                self.grid.addWidget(button, row, col)
                self.buttons[row][col] = button

        self.setWindowTitle('Tic Tac Toe')
        self.show()

    def on_button_clicked(self, row, col):
        if self.buttons[row][col].text() == '':
            self.buttons[row][col].setText(self.current_player)
            self.board[row][col] = self.current_player  

            if self.check_winner():
                QMessageBox.information(self, 'Galaba!', f'{self.current_player} golib boldi!')
                self.reset_game()
            elif all(cell != '' for row in self.board for cell in row):  
                QMessageBox.information(self, 'Durang', 'Oyin durang!')
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in self.board:
            if all(cell == self.current_player for cell in row):
                return True
        
        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True

        if all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        
        if all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        
        return False

    def reset_game(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText('')
                self.board[row][col] = '' 
        self.current_player = 'X'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToe()
    sys.exit(app.exec_())
