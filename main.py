from cards import deck
from players import player1

deck.shuffle()
print(len(deck))
deck.deal(player1)
print(player1.name, player1.cards)
print(len(deck))