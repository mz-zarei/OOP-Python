from xmlrpc.client import Boolean
from Deck import Deck

class Player:
    def __init__(self, Deck, money) -> None:
        self.hand = []
        self.deck = Deck
        self.score = 0
        self.money = money
        self.status = 0   # becomes 1 if score pass 21
    
    # update score
    def updateScore(self) -> None:
        aces = 0
        self.score = 0
        for card in self.hand:
            if card.value in ['Q', 'J', 'K']:
                self.score += 10
            elif card.value == 'A':
                self.score += 11
                aces += 1
            else:
                self.score += int(card.value)

        while aces>0 and self.score>21:
            self.score -= 10
            aces -= 1
    
    # hit the palyer from deck
    def hit(self) -> int:
        self.hand.append(self.deck.draw())
        self.updateScore()
        if self.score > 21:
            self.status = 1
    
    # deal two cards to player
    def deal(self) -> int:
        self.hand.append(self.deck.draw())
        self.hand.append(self.deck.draw())
        self.updateScore()
        if self.score > 21:
            self.status = 1

    # print player hand and score
    def show(self) -> None:
        for card in self.hand:
            card.show()
        
        print(f"Score: {str(self.score)}")

    # update money given a bet and win(True)/lose(False)
    def updateMoney(self, bet, win) -> None:
        if win:    
            self.money += bet
        else:
            self.money -= bet

    # restart status, hand, score of player
    def restartHand(self):
        self.hand = []
        self.score = 0
        self.status = 0



class Dealer(Player):
    def __init__(self, deck):
        Player.__init__(self, deck, 0)
        self.show_one_card = True

    # over-ride the hit() function in the parent class
    def hit(self) -> None:
        self.show_one_card = False
        while (self.score < 17):
            self.hand.append(self.deck.draw())
            self.updateScore()

    # override show method to just one card if not hit yet
    def show(self):
        if (self.show_one_card):
            return self.hand[0].show()
        else:
            return Player.show(self)
     # override restartHand method to include show_one_card
    def restartHand(self):
        self.hand = []
        self.score = 0
        self.status = 0
        self.show_one_card = True





# deck = Deck()

# player = Dealer(deck)
# player.deal()
# player.show()
# player.show_one_card = False
# player.show()
# player.hit()
# player.show()
        

            

