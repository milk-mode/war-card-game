from deck import Deck
class Hand(Deck):
    def __init__(self, cardUser, cardComputer):
        super()
        self.cardUser = cardUser
        self.cardComputer = cardComputer

    def addCardTo(self, player, card):
        if player == 'computer':
            self.computer.append(card)
        elif player == 'user':
            self.user.append(card)

    def removeCardFrom(self, player, index):
        if player == 'computer':
            self.computer.pop(index)
        elif player == 'user':
            self.user.pop(index)

    # private method to deal with value of the card, returns int value
    def cardValue(self, value) -> int:
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
        cardValueOfTheUser = self.cardValue(self.cardUser[1:])
        cardValueOfTheComputer = self.cardValue(self.cardComputer[1:])

        # guard conditions
        if len(self.user) > 0 and len(self.computer) == 0:
            print("*** user wins ***")
            return

        if len(self.user) == 0 and len(self.computer) >0:
            print("*** computer wins ***")
            return

        if len(self.user) != 0 and len(self.computer) != 0:
            if int(cardValueOfTheUser) > int(cardValueOfTheComputer):
                # remove from computer add to user
                self.removeCardFrom('computer', 0)
                self.removeCardFrom('user', 0)
                self.addCardTo('user', self.cardComputer)

            elif int(cardValueOfTheUser) < int(cardValueOfTheComputer):
                # remove from computer add to user
                self.removeCardFrom('user', 0)
                self.removeCardFrom('computer', 0)
                self.addCardTo('computer', self.cardUser)

            elif int(cardValueOfTheUser) == int(cardValueOfTheComputer):
                # equal-deal three times and recursion

                # if it gets to last 3 cards #guard condition
                if len(self.user) >= 3 and len(self.computer) < 3:
                    print("*** user wins ***")
                    return

                if len(self.user) < 3 and len(self.computer) >= 3:
                    print("*** computer wins ***")
                    return

                #pop 3 times
                if len(self.computer) > 3:
                    self.computer = self.computer[3:]
                if len(self.user) > 3:
                    self.user = self.user[3:]

            # update hand at the players
            if len(self.user) !=0:
                self.cardUser = self.user[0]
            if len(self.computer) != 0:
                self.cardComputer = self.computer[0]

        # deal again
        self.dealCard()

    def __str__(self):
        return f"User cards: {self.getUserCards()} and Computer cards: {self.getComputerCards()}"