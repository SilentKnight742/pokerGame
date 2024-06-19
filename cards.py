import random

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    suitDict = {
        0 : "Spades",
        1 : "Diamonds",
        2 : "Clubs",
        3 : "Hearts"
    }
    valueDict = {
        0 : "Two",
        1 : "Three",
        2 : "Four",
        3 : "Five",
        4 : "Six",
        5 : "Seven",
        6 : "Eight",
        7 : "Nine",
        8 : "Ten",
        9 : "Jack",
        10 : "Queen",
        11 : "King",
        12 : "Ace"
    }
    def __repr__(self):
        valueName = self.valueDict[self.value]
        suitName = self.suitDict[self.suit]
        return valueName + " of " + suitName
    
class StandardDeck(list):
    def __init__(self):
        super().__init__()
        suits = list(range(4))
        values = list(range(13))
        [[self.append(Card(value, suit) ) for suit in suits] for value in values]
    
    def shuffle(self):
        random.shuffle(self)
        print("shuffled deck")
    
    def deal(self, location):
        location.cards.append(self.pop(0))

deck = StandardDeck()

