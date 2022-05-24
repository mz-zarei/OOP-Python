#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Mohammad Zarei
# Created Date: 23 May 2022
# version ='1.0'
# ---------------------------------------------------------------------------
'''Implementation of Black Jack Game'''
# ---------------------------------------------------------------------------
# Imports
from Deck import Deck
from Player import Player, Dealer

class BlackJack:
    def __init__(self) -> None:
        setNumber = int(input('Enter the number of card sets: '))
        playerMoney = int(input('Enter you money: '))

        self.deck = Deck(setNumber)
        self.player = Player(self.deck, playerMoney)
        self.dealer = Dealer(self.deck)
        self.choice = 'menu'
        self.bet = 0
        self.display()

    def play(self):
        self.takeBet()
        self.deal()
        self.showCards()
        balckjack = self.checkBlackJack()

        if balckjack != 1:

            hitOrStand = ""

            while hitOrStand != 's':
                hitOrStand = input('(H)it or (S)tand: ').lower()

                if hitOrStand == 'h':
                    self.player.hit()
                    self.player.show()

                if self.player.status:
                    print(f'You busted and lost {self.bet}!')
                    self.player.updateMoney(self.bet, win=False)
                    self.choice = 'menu'
                    print()
                    break

            if self.player.status == 0:
                print('Dealer hand is:')
                self.dealer.show_one_card = False
                self.dealer.show()
                
                if self.dealer.status == 1:
                    print(f'Dealer got Blackjack! You lost {self.bet}')
                    self.player.updateMoney(self.bet, win=False)
                else:
                    self.dealer.hit()
                    self.showCards()
                    self.checkScores()
            
    def takeBet(self):
        self.bet = int(input('\nEnter the amount of bet: '))
        if self.bet > self.player.money:
            print('Insufficient fund to bet!')
            self.bet = input('\nEnter the amount of bet: ')

    def deal(self):
        self.player.restartHand()
        self.dealer.restartHand()
        self.player.deal()
        self.dealer.deal()

    def showCards(self):
        print('Your hand is:\n')
        self.player.show()
        print()
        print('Dealer hand is:\n')
        self.dealer.show()
    
    def checkBlackJack(self):
        if self.player.score == 21:
            if self.dealer.score == 21:
                print('Dealer and Player got tie!')
                self.choice = 'menu'
                return 1
            else:
                print('You won {self.bet}! Congrats!')
                self.player.updateMoney(self.bet, win=True)
                self.choice = 'menu'   
                return 1

    def checkScores(self):
        if self.dealer.score > 21:
            print("Dealer Busted, Player wins. Congratulations!")
            self.player.updateMoney(self.bet, win=True)
            self.choice = 'menu'
        elif self.dealer.score == self.player.score:
            print("It's a Push (Tie). Better luck next time!")
            self.choice = 'menu'
        elif self.dealer.score > self.player.score:
            print("Dealer wins. Good Game!")
            self.player.updateMoney(self.bet, win=False)
            self.choice = 'menu'
        elif self.dealer.score < self.player.score:
            print("Player wins. Congratulations!")
            self.player.updateMoney(self.bet, win=True)
            self.choice = 'menu'

    def showMenu(self):
        self.choice = input(f'\n(B)et (total:{self.player.money})\n(Q)uit \n> ').lower()
        print()

    def display(self):
        while True:
            if self.choice == 'menu':
                self.showMenu()
            elif self.choice in ['bet', 'b']:
                self.play()
            elif self.choice in ['quit', 'q']:
                print('\nGood Game!\n')
                print(f'You total is {self.player.money}')
                break
            else:
                self.showMenu()
   

game = BlackJack()