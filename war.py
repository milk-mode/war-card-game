import random
class Deck:
    deckOfCards = []
    user = []
    computer = []

    def __init__(self, SUITE, RANKS, player):
        self.SUITE = SUITE
        self.RANKS = RANKS
        self.player = player

    def createDeckOfCards(self):
        for suit in self.SUITE:
            for rank in self.RANKS:
                self.deckOfCards.append(suit+rank)

        random.shuffle(self.deckOfCards)

    def splitCards(self):
        for i in range(0, 26):
            self.user.append(self.deckOfCards[i])
        for j in range(26, 52):
            self.computer.append(self.deckOfCards[j])

    def getUserCards(self):
        return self.user

    def getComputerCards(self):
        return self.computer

    def __str__(self) -> str:
        return f"suits {self.SUITE} rank {self.RANKS}"


class Hand(Deck):
    def __init__(self):
        super()

    def addCard(self, card, player):
        if player == 'computer':
            self.computer.append(card)
        elif player == 'user':
            self.user.append(card)

    def removeCardFrom(self, player):
        if player == 'computer':
            self.computer.pop
        elif player == 'user':
            self.user.pop

    def popThreeTimesFromBoth(self):
            self.computer=self.computer[3:]
            self.user=self.user[3:]

   

    def dealCard(self):
        cardOfTheUser=self.user[0][1]
        cardOfTheComputer=self.computer[0][1]

        if cardOfTheUser>cardOfTheComputer:
         #remove from computer add to user
             self.removeCardFrom('computer')
             self.addCardTo(user,cardOfTheComputer)

        elif cardOfTheUser< cardOfTheComputer:
         #remove from computer add to user         
             self.removeCardFrom('user')
             self.addCardTo('computer',cardOfTheUser)

        else:
         #equal-deal three times and recursion
         self.popThreeTimesFromBoth
         self.dealCard               


class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"


SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
print('CARD GAME')
print('==== ====')
user = str(input("Enter name:"))
hand = Hand()
play = Player(user)
deck = Deck(SUITE, RANKS, user)
deck.createDeckOfCards()
deck.splitCards()


print('Welcome {}, you have got the following cards'.format(user))
print(deck.getUserCards())

print('\nAnd the computer got the following cards')
print(deck.getComputerCards())
