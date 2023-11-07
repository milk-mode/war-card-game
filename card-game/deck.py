import random


class Deck:
    deck_of_cards = []
    user = []
    computer = []

    def __init__(self, SUITE, RANKS, player):
        self.SUITE = SUITE
        self.RANKS = RANKS
        self.player = player

    def create_deck_of_cards(self):
        for suit in self.SUITE:
            for rank in self.RANKS:
                self.deck_of_cards.append(suit + rank)

        random.shuffle(self.deck_of_cards)

    def split_cards(self):
        for i in range(0, 26):
            self.user.append(self.deck_of_cards[i])
        for j in range(26, 52):
            self.computer.append(self.deck_of_cards[j])

    def get_user_cards(self):
        return self.user

    def get_computer_cards(self):
        return self.computer

    def __str__(self) -> str:
        return f"suits {self.SUITE} rank {self.RANKS}"
