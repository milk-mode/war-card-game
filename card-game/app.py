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
deckobj.create_deck_of_cards()
deckobj.split_cards()

print('Welcome {}, you have got the following cards'.format(user))
print(deckobj.get_user_cards())

print('\nAnd the computer got the following cards')
print(deckobj.get_computer_cards())

print('\nInitial Deal')
print('======= ====')

print('\nComputer Deals: ', end='')
print(deckobj.get_computer_cards()[0])
print('User Deals: ', end='')
print(deckobj.get_user_cards()[0])

handobj = Hand(deckobj.get_user_cards()[0], deckobj.get_computer_cards()[0],SUITE,RANKS,playobj)
handobj.dealCard()

print('\nFinal cards')
print('===== =====')
print(handobj)