from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from PySide2.QtCore import QSize, Qt
import sys
from random import randint

class MainWindow(QMainWindow):
    '''Stupid 'bataille' like game '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('First signals and slots')
        self.checkButton = checkButton(self, 'Check Winner')

        self.player1 = QLabel(str(randint(1,10)))
        self.player2 = QLabel(str(randint(1,10)))

        self.vLayout = QVBoxLayout()
        self.firstRow = QHBoxLayout()

        self.firstRow.addWidget(self.player1)
        self.firstRow.addWidget(self.player2)

        self.vLayout.addLayout(self.firstRow)
        self.vLayout.addWidget(self.checkButton)

        self.grid = QWidget()
        self.grid.setLayout(self.vLayout)
        self.setCentralWidget(self.grid)

class checkButton(QPushButton):
    def __init__(self, root, *args):
        super().__init__(*args)
        self.root = root
        self.clicked.connect(self.check_winner)
        self.clicked.connect(self.shuffle)

    def check_winner(self):
        '''Check which player win the game'''
        if int(self.root.player1.text()) > int(self.root.player2.text()):
            print("Player 1 Won ! ({} vs {})".format(
                int(self.root.player1.text()), int(self.root.player2.text())))
        else : 
            print("Player 2 Won !({} vs {})".format(
                int(self.root.player1.text()), int(self.root.player2.text())))
    def shuffle(self):
        '''Reset value of player'''
        self.root.player1.setText(str(randint(1,10)))
        self.root.player2.setText(str(randint(1,10)))

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
