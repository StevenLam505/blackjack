#################################################
# AUTHOR:   Steven Lam                          #
# DATE:     5/12/20                             #
# FILE:     blackjack.py                        #
# DESC:     Blackjack using python plugins      #
#################################################

#import pygame
import random

allCards = range(1,11)
faceCards = ["Jack", "Queen", "King"]
deck = []
maxCards = 51

class player(object):
    def __init__(self, hand, points):
        self.hand = hand
        self.points = points

    def calculatePoints(self, cards):
        self.points = 0
        for i in range(len(cards)):
            if (cards[i][0] == "J" or cards[i][0] == "Q" or cards[i][0] == "K"):        # Adds 10 points for face cards
                self.points += 10
            elif (cards[i][0:2] == "1 "):                                               # Adds 11 points for ace
                self.points += 11
            else:                                                                       # Adds in the number value                          
                self.points += int(cards[i][0:2])                                       # converted to int from str

        for j in range(len(cards)):                                                     # If an ace was in the hand and 
            if (self.points > 21 and cards[j][0:2] == "1 "):                            # causes it to go over 21 because the
                self.points -= 10                                                       # ace was an 11, it changes it to a 1


    def drawCard(self):
        global maxCards
        randomCard = random.randint(0, maxCards)        # Generates a random number between
        self.hand.append(deck[randomCard])              # 0 - 51 to put that card from
        deck.pop(randomCard)                            # deck into a player's hand then
        maxCards -= 1                                   # removes the card from the deck

    def houseHit(self):
        if self.points < 17:                            # If the dealer has < 17, he hits again
            self.drawCard()                             # otherwise he stands

    def playerHit(self):
        hitAgain = input("Would you like to hit? (Y/N)")        # Asks the player to hit if they want to
        while hitAgain == "Y" and self.points <= 21:            # If the player goes over 21 points
            self.drawCard()                                     # they bust
            print("Player hand:", self.hand)
            self.calculatePoints(self.hand)
            if self.points > 21:
                print("You busted, house wins!")
                return
            hitAgain = input("Would you like to hit? (Y/N)")


def createDeck():
    # Create base 0-10 cards for the 4 suits
    for i in allCards:
        deck.append(str(i) + " of Hearts")
        deck.append(str(i) + " of Diamonds")
        deck.append(str(i) + " of Spades")
        deck.append(str(i) + " of Clubs")

    # Create face cards for the 4 suits
    for j in faceCards:
        deck.append(j + " of Hearts")
        deck.append(j + " of Diamonds")
        deck.append(j + " of Spades")
        deck.append(j + " of Clubs")


def findWinner(dPoints, pPoints):
    if (dPoints > 21 or dPoints < pPoints) and pPoints <= 21:
        print("Player wins!")
    elif (pPoints > 21 or dPoints > pPoints) and dPoints <=21:
        print("House wins!")
    else:
        print("Tie!")


def game():
    createDeck()

    dealer = player([], 0)                                          # Starts the game and gives both the
    user = player([], 0)                                            # player and house an empty hand and 0
    user.drawCard()                                                 # points. They then each draw 2 cards.
    dealer.drawCard()                                               # Only one of the house's cards is displayed
    user.drawCard()                                                 # while the other is hidden.
    dealer.drawCard()
    print("House hand:", dealer.hand[1], "and Unknown Card")
    print("Player hand:", user.hand)
    user.playerHit()                                                # The player is then asked to hit
    if user.points <= 21:                                           # If the player has over 21 points, they
        dealer.houseHit()                                           # bust and the house does not hit. If
    dealer.calculatePoints(dealer.hand)                             # the player has <= 21 points and house
    user.calculatePoints(user.hand)                                 # has less than 17 points, the house hits
    print("\n")
    print("House hand:", dealer.hand)
    print("House points:", dealer.points)
    print("Player hand:", user.hand)
    print("Player points:", user.points)

    findWinner(dealer.points, user.points)

game()
