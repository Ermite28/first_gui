from PySide2.QtWidgets import (QApplication,
 QMainWindow,
QPushButton, QLabel, QHBoxLayout, QVBoxLayout,
QWidget)

from PySide2.QtCore import QSize, Qt
import sys
from random import randint
from os import path
from deck import Deck, Deck_player, Card

class MainWindow(QMainWindow):
    '''Stupid 'bataille' like game '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Battle cards!')
        self.checkButton = checkButton(self, 'Check Winner')

        self.results = QLabel()
        self.results.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.vLayout = QVBoxLayout()
        self.players = Players()
        self.firstRow = self.players.container
        
        self.vLayout.addLayout(self.firstRow)
        self.vLayout.addWidget(self.results)
        self.vLayout.addWidget(self.checkButton)
        

        self.grid = QWidget()
        self.grid.setLayout(self.vLayout)
        self.setCentralWidget(self.grid)

class Players():
    def __init__(self):
        self.container = QHBoxLayout()
        self.deck = Deck()
        self.player1 = Player('Ben', self.deck)
        self.player2 = Player("Manu", self.deck)
        self.players = [self.player1, self.player2]
        self.container.addLayout(self.player1.container)
        self.container.addLayout(self.player2.container)
    
    def compare_cards(self):
        match = '{} vs {}'.format(self.player1.top_card.name, self.player2.top_card.name)
        if self.player1.top_card.value > self.player2.top_card.value:
            self.card_trade([self.player1.top_card, self.player2.top_card], self.player1)
            return '{} Win ! {}'.format(self.player1.name, match)
        elif self.player2.top_card.value > self.player1.top_card.value:
            self.card_trade(
                [self.player1.top_card, self.player2.top_card], self.player2)
            return '{} Win ! {}'.format(self.player2.name,match)
        else : 
            return 'equality!'
            # A mon avis je vais devoir faire une récursion
    
    def card_trade(self, cards, winner):
        '''cards : list of cards'''
        for card in cards : 
            winner.deck.enqueue(card)
    
    def new_round(self):
        for player in self.players:
            player.pick_new_card()
            player.refresh_deck_size()

class Player():
    def __init__(self, name, deck):
        self.container = QVBoxLayout()

        # En faire une classe
        self.name = name
        self.nameLabel = QLabel(name)
        self.font = self.nameLabel.font()
        self.font.setPointSize(20)
        self.nameLabel.setFont(self.font)
        self.nameLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.deckSizeLabel = QLabel()
        self.deckSizeLabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
       
        self.deck = Deck_player(deck)
        self.cardLabel = QLabel()
        self.pick_new_card()
        self.refresh_deck_size()
    
        self.container.addWidget(self.nameLabel)
        self.container.addWidget(self.deckSizeLabel)
        self.container.addWidget(self.cardLabel)

    def pick_new_card(self):
        self.top_card = self.deck.dequeue()
        self.cardLabel.setPixmap(self.top_card.asset)
    
    def refresh_deck_size(self):
        self.deckSizeLabel.setText(str(len(self.deck)))

class checkButton(QPushButton):
    def __init__(self, root, *args):
        super().__init__(*args)
        self.root = root
        self.clicked.connect(self.check_winner)
        self.clicked.connect(self.new_round)

    def check_winner(self):
        '''Check which player win the game'''
        self.root.results.setText(self.root.players.compare_cards())
    def new_round(self):
        '''Reset value of player'''
        self.root.players.new_round()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec_()
