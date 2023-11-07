from deck import Deck


class Hand(Deck):
    def __init__(self, card_user, card_computer, SUITE, RANKS, player):
        super().__init__(SUITE, RANKS, player)
        self.card_user = card_user
        self.card_computer = card_computer

    def add_card_to(self, player, card):
        if player == 'computer':
            self.computer.append(card)
        elif player == 'user':
            self.user.append(card)

    def remove_card_from(self, player, index):
        if player == 'computer':
            self.computer.pop(index)
        elif player == 'user':
            self.user.pop(index)

    # private method to deal with value of the card, returns int value

    def card_value(self, value) -> int:
        if value == 'J':
            return 11
        elif value == 'Q':
            return 12
        elif value == 'K':
            return 13
        elif value == 'A':
            return 14
        else:
            return value

    def dealCard(self):
        card_value_of_the_user = self.card_value(self.card_user[1:])
        card_value_of_the_computer = self.card_value(self.card_computer[1:])

        # guard conditions
        if len(self.user) > 0 and len(self.computer) == 0:
            print("*** user wins ***")
            return

        if len(self.user) == 0 and len(self.computer) > 0:
            print("*** computer wins ***")
            return

        if len(self.user) != 0 and len(self.computer) != 0:
            if int(card_value_of_the_user) > int(card_value_of_the_computer):
                # remove from computer add to user
                self.remove_card_from('computer', 0)
                self.remove_card_from('user', 0)
                self.add_card_to('user', self.card_computer)

            elif int(card_value_of_the_user) < int(card_value_of_the_computer):
                # remove from computer add to user
                self.remove_card_from('user', 0)
                self.remove_card_from('computer', 0)
                self.add_card_to('computer', self.card_user)

            elif int(card_value_of_the_user) == int(card_value_of_the_computer):
                # equal-deal three times and recursion

                # if it gets to last 3 cards #guard condition
                if len(self.user) >= 3 > len(self.computer):
                    print("*** user wins ***")
                    return

                if len(self.user) < 3 <= len(self.computer):
                    print("*** computer wins ***")
                    return

                # pop 3 times
                if len(self.computer) > 3:
                    self.computer = self.computer[3:]
                if len(self.user) > 3:
                    self.user = self.user[3:]

            # update hand at the players
            if len(self.user) != 0:
                self.card_user = self.user[0]
            if len(self.computer) != 0:
                self.card_computer = self.computer[0]

        # deal again
        self.dealCard()

    def __str__(self):
        return f"User cards: {self.get_user_cards()} and Computer cards: {self.get_computer_cards()}"
