from player import Player
from deck import Deck
from hand import Hand

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
print('CARD GAME')
print('==== ====')
user = str(input("Enter name:"))
playobj = Player(user)
deckobj = Deck(SUITE, RANKS, playobj)
deckobj.createDeckOfCards()
deckobj.splitCards()

print('Welcome {}, you have got the following cards'.format(user))
print(deckobj.getUserCards())

print('\nAnd the computer got the following cards')
print(deckobj.getComputerCards())

print('\nInitial Deal')
print('======= ====')

print('\nComputer Deals: ', end='')
print(deckobj.getComputerCards()[0])
print('User Deals: ', end='')
print(deckobj.getUserCards()[0])

handobj = Hand(deckobj.getUserCards()[0], deckobj.getComputerCards()[0])
handobj.dealCard()

print('\nFinal cards')
print('===== =====')
print(handobj)