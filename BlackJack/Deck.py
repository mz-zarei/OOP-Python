from math import fabs
import random
from Card import Card

class Deck:
    def __init__(self, setNumber=1) -> None:
        self.cards = []
        self.generate(setNumber)
        self.count = len(self.cards)
        self.shuffle()

    def generate(self, setNumber=1) -> None:
        for i in range(setNumber):
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                for suit in ['s', 'c', 'h', 'd']:
                    self.cards.append(Card(value, suit))

    def show(self, byShape=True) -> None:
        if byShape == True:
            for card in self.cards:
                card.show()
        else:
            for card in self.cards:
                print(card)
    
    def shuffle(self) -> None:
        for i in range(self.count-1, 0, -1):
            r = random.randint(0, i)
            self.cards[r], self.cards[i], = self.cards[i], self.cards[r]

    def draw(self) -> object:
        card = self.cards.pop()
        self.count = len(self.cards)
        return card




# deck = Deck()
# deck.draw().show()