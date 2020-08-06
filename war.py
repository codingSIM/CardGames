"""
War is a self playing game. Once the cards are dealt, the game goes on until a person runs out of cards.
Please see: https://en.wikipedia.org/wiki/War_(card_game)
"""

import General
from time import sleep


class WarCard(General.Card):
    def __init__(self, suit, number):
        self.numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        General.Card.__init__(self, suit, number)


tempDeck = General.Deck(cardObject=WarCard)
tempDeck.generateNewDeck()
tempDeck.shuffleDeck()

you = General.Deck(cardObject=WarCard)
opponent = General.Deck(cardObject=WarCard)

while tempDeck.numberOfCards() > 0:
    tempDeck.takeTopCard(you)
    tempDeck.takeTopCard(opponent)

war = False
yourArmy = General.CardContainer(cardObject=WarCard)
opponentArmy = General.CardContainer(cardObject=WarCard)
while you.numberOfCards() != 0 and opponent.numberOfCards() != 0:
    print("You have {} cards".format(you.numberOfCards()))

    sleep(1)
    you.takeBottomCard(yourArmy)
    opponent.takeBottomCard(opponentArmy)

    print("You pulled out:          ", yourArmy.getCards()[-1].getShortName())
    print("Your opponent pulled out:", opponentArmy.getCards()[-1].getShortName())

    if not war:
        if yourArmy.getCards()[0].getNumNumber() > opponentArmy.getCards()[0].getNumNumber():
            print("You win the battle")
            opponentArmy.takeTopCard(you)
            yourArmy.takeTopCard(you)

        elif yourArmy.getCards()[0].getNumNumber() == opponentArmy.getCards()[0].getNumNumber():
            print("WAR!")
            war = True

        else:
            print("Opponent won the battle")
            yourArmy.takeTopCard(opponent)
            opponentArmy.takeTopCard(opponent)

    else:
        war = False
        if yourArmy.getCards()[-1].getNumNumber() > opponentArmy.getCards()[-1].getNumNumber():
            print("You win the war!")

            print("You take: ")

            for card in yourArmy.getCards():
                print("Your", card.getShortName())

            for card in opponentArmy.getCards():
                print("Their", card.getShortName())

            while opponentArmy.numberOfCards() > 0:
                opponentArmy.takeTopCard(you)
                yourArmy.takeTopCard(you)

        elif yourArmy.getCards()[-1].getNumNumber() < opponentArmy.getCards()[-1].getNumNumber():
            print("Opponent win the war!")

            print("They take: ")

            for card in yourArmy.getCards():
                print("Your", card.getShortName())

            for card in opponentArmy.getCards():
                print("Their", card.getShortName())

            while yourArmy.numberOfCards() > 0:
                yourArmy.takeTopCard(opponent)
                opponentArmy.takeTopCard(opponent)
        else:
            print("Draw! The war continues!")
            war = True

if you.numberOfCards() == 0:
    print("You lose")

else:
    print("You win!")
