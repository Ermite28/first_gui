from PySide2.QtGui import QPixmap
from random import shuffle
from os import path
from PySide2.QtCore import Qt
class Deck():
    def __init__(self):
        self.cards = []
        for i in range(1, 14):
            for c in ['C', 'D', 'H', 'S']:
                self.cards.append(Card(i, c))  # Faire refference à classe Card
        shuffle(self.cards)

    def distribute(self):
        if len(self.cards) >= 27:
            cards = self.cards[0:int(len(self.cards)/2)]
            self.cards = self.cards[int(len(self.cards)/2):]
        else:
            cards = self.cards
        return cards


class Deck_player():
    DEFAULT_CAPACITY = 26
    '''Player Deck'''

    def __init__(self, Deck):
        self._cards = Deck.distribute()
        self._size = len(self._cards)
        self._front = 0

    def __len__(self):
        '''return the len of the deck'''
        return self._size

    def enqueue(self, card):
        '''add card to the end of the deck'''
        if len(self._cards) == self._size:
            self._resize(2*len(self._cards))
        endQueue = (self._front + self._size) % len(self._cards)
        self._cards[endQueue] = card
        self._size += 1

    def dequeue(self):
        '''remove and return the first card'''
        if self.is_empty():
            raise Empty('Deck is empty')
        card = self._cards[self._front]
        self._cards[self._front] = None
        self._front = (self._front + 1) % len(self._cards)
        self._size -= 1
        return card

    def is_empty(self):
        '''return True if deck does not contains any element'''
        return self._size == 0

    def _resize(self, cap):
        ''' Resize to a new list capacity '''
        old = self._cards
        self._cards = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._cards[k] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0


class Card():
    cards_colors = {"C": "clubs", 'D': 'diamonds',
                    'H': 'hearts', 'S': 'spades'}
    cards_values = {1: "2", 2: "3", 3: "4", 4: "5", 5: "6", 6: "7", 7: "8",
                    8: "9", 9: "10", 10: "jack", 11: "queen", 12: "king", 13: "ace"}

    def __init__(self, value, color):
        self.value = value
        self.card_value = Card.cards_values[self.value]
        self.card_color = Card.cards_colors[color]
        self.name = '{}_of_{}'.format(self.card_value, self.card_color)
        self.asset = QPixmap(path.join('cards_assets', self.name+'.png' ))
        self.asset = self.asset.scaled(200, 200, Qt.KeepAspectRatio)


class Empty(Exception):
    pass
