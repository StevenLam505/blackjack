#################################################
# AUTHOR:   Steven Lam                          #
# DATE:     5/12/20                             #
# FILE:     blackjack.py                        #
# DESC:     Blackjack using python plugin       #
#################################################

#import pygame
import random

allCards = range(1,11)
faceCards = ["Jack", "Queen", "King"]
deck = []
hand = []
dealerHand = []

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


def calculatePoints(cards):
    points = 0
    if (cards[0] == "J" or cards[0] == "Q" or cards[0] == "K"):
        points += 10
    else:
        points += int(cards[0:2])
    return points


def dealer():
    global maxCards
    maxCards = 51
    dealerPoints = 0
    i = 1  # Used to iterate the loop
    cardNum = 0  # Represents the card that is in the hand
    while i <= 2:
        randomCard = random.randint(0, maxCards)
        dealerHand.append(deck[randomCard])
        deck.pop(randomCard)
        maxCards -= 1
        dealerPoints += calculatePoints(dealerHand[cardNum])
        cardNum += 1
        i += 1
        if i == 3:
            print("Dealer has", dealerHand, "in their hand equaling", dealerPoints, "points")
            if dealerPoints < 17:
                i -= 1
        if dealerPoints > 21:
            print("Dealer has", dealerHand, "in their hand equaling", dealerPoints, "points")
            print("Dealer busted, oops.")
            break
    return dealerPoints


def dealCards():
    global maxCards
    points = 0
    i = 1           # Used to iterate the loop
    cardNum = 0     # Represents the card that is in the hand
    while i <= 2:
        randomCard = random.randint(0,maxCards)
        hand.append(deck[randomCard])
        deck.pop(randomCard)
        maxCards -= 1
        points += calculatePoints(hand[cardNum])
        cardNum += 1
        i += 1
        if points > 21:
            print("You have", hand, "in your hand equaling", points, "points")
            print("You busted, oops.")
            break
        if i == 3:
            print("You have", hand, "in your hand equaling", points, "points")
            hitAgain = input("Would you like to hit? (Y/N)")
            if hitAgain == "Y":
                i -= 1
    return points

def findWinner(dPoints, pPoints):
    if dPoints > 21 or dPoints < pPoints:
        print("Player wins!")
    elif pPoints > 21 or dPoints > pPoints:
        print("Dealer wins!")
    else:
        print("Tie!")


createDeck()
dealerPoints = dealer()
points = dealCards()
findWinner(dealerPoints, points)
