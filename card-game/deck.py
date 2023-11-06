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
                self.deckOfCards.append(suit + rank)

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