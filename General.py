class Card:
    suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
    numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suitsSymbol = ["♦", "♣", "♥", "♠"]

    def __init__(self, suit, number):
        self.__suit = suit  # We don't want to change the suit half way though the card's life. Especially externally
        self.__number = number  # We don't want to change the card's number, especially externally.
        # please read about variable protection:
        # https://www.tutorialsteacher.com/python/private-and-protected-access-modifiers-in-python

    """
    def getValue(self):
        if self.number == self.numbers[0]:
            value = [11, 1]  # if Ace is valued as 11 the hand is a "soft hand"
            # if Ace is counted as 1 then it is a hard hand
            # therefore initial value should be 11 and if it goes over it should revert to 1
        elif self.number in range(2, 10):
            value = int(self.number)
        else: #Jack, Queen, King
            value = 10
        return value
    """

    def getValue(self):
        if self.__number > 9:
            return 10
        else:
            return self.__number + 1

    def getNumber(self):
        return self.numbers[self.__number]

    def getSuit(self):
        return self.suits[self.__suit]

    def getSymbolSuit(self):
        return self.suitsSymbol[self.__suit]

    def getName(self):
        return self.getNumber() + " of " + self.getSuit()

    def getShortName(self):
        name = self.getNumber()
        return self.getSymbolSuit() + name

    def __lt__(self, other):  # Makes it possible to sort cards according to their value
        return self.getValue() > other.getValue()

    # read https://stackoverflow.com/questions/4932438/how-to-create-a-custom-string-representation-for-a-class-object
    def __str__(self):  # String representation of card
        return self.getShortName()

    def __repr__(self):
        return str(self)


class CardContainer:
    __cardCounter = 0

    # We don't want the number of cards to be changed from the outside so the var is protected/private

    def __init__(self, cards=None):
        if cards is None:
            cards = []

        self.__cards = cards
        # We don't want the cards to be changed from the outside so the var is protected/private

    def getCards(self):
        return self.__cards

    def addCard(self, card):
        self.__cardCounter += 1
        self.__cards.append(card)

    def removeCard(self, card):
        self.__cardCounter -= 1
        self.__cards.remove(card)

    def takeTopCard(self, destination):
        self.moveCard(self.__cards[-1], destination)

    def moveCard(self, card, destination):
        self.removeCard(card)
        destination.addCard(card)

    def numberOfCards(self):
        return self.__cardCounter


class Deck(CardContainer):
    from random import shuffle

    def __init__(self, cards=None):
        CardContainer.__init__(self, cards)

    def shuffleDeck(self):
        self.shuffle(self.getCards())

    def generateNewDeck(self):
        for suit in range(4):
            for number in range(13):
                self.addCard(Card(suit, number))
