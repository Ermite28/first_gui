from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from PySide2.QtCore import QSize, Qt
import sys
from random import randint

class MainWindow(QMainWindow):
    '''Stupid 'bataille' like game '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Battle cards!')
        self.checkButton = checkButton(self, 'Check Winner')


        self.vLayout = QVBoxLayout()
        self.players = Players()
        self.firstRow = self.players.container
        
        self.vLayout.addLayout(self.firstRow)
        self.vLayout.addWidget(self.checkButton)

        self.grid = QWidget()
        self.grid.setLayout(self.vLayout)
        self.setCentralWidget(self.grid)

class Players():
    def __init__(self):
        self.container = QHBoxLayout()
        self.player1 = Player('Ben')
        self.player2 = Player("Manu")
        self.container.addLayout(self.player1.container)
        self.container.addLayout(self.player2.container)
    
    def shuffle_cards(self):
        self.player1.set_value()
        self.player2.set_value()
    
    def compare_cards(self):
        if self.player1.value > self.player2.value:
            print("{} Won ! ({} vs {})".format(self.player1.name,
                self.player1.value, self.player2.value))
        elif self.player1.value < self.player2.value:
            print("{} Won ! ({} vs {})".format(self.player2.name,
                                              self.player1.value, self.player2.value))
        else : 
            print("EQUALITY")

class Player():
    def __init__(self, name):
        self.container = QVBoxLayout()
        self.name = name
        self.nameLabel = QLabel(name)

        self.label = QLabel()
        self.set_value()
    
        self.container.addWidget(self.nameLabel)
        self.container.addWidget(self.label)
    def set_value(self):
        self.value = randint(1,10) # Changer ça
        self.label.setText(str(self.value))

class checkButton(QPushButton):
    def __init__(self, root, *args):
        super().__init__(*args)
        self.root = root
        self.clicked.connect(self.check_winner)
        self.clicked.connect(self.shuffle)

    def check_winner(self):
        '''Check which player win the game'''
        self.root.players.compare_cards()
    def shuffle(self):
        '''Reset value of player'''
        self.root.players.shuffle_cards()

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
