"""
Blackjack rules:
All players get 2 cards, including the dealer, however one of the dealers cards is turned face up.
In casinos dealers have to play until they hit 16+ as a hard hand.
*If you get 2 of the same card you have the option to split into 2 different hands?

Initial options: 1st Bet.
when it's the players turn they can either:
stand or hit
maybe split their hands too but idk about that one

after all players stand or go bust the dealer has to play.

then the payout happens.


Special rules:
21 = natural or blackjack = tie with dealer or win 
(^ if dealer doesn't have blackjack then the payouts are 3:2 instead of 1:1)
CHECK (dealer has blackjack then bets remain in the box and you play again?)
if a player has 5 cards they win 


https://www.qfit.com/basic-blackjack-rules.htm
"""

import General

# Card class: getValue shouldn't be in the card class since the value the cards have depends on what game is played
# Card container class looks fine
# Class hand maybe should be renamed to like blackjack hand and moved in the blackjack file?
# class deck looks fine


# should we just have an engine which already contains everything? like a blackjack function in hand and what not?
# or different py files for different games? more elegant?


"""other games to implement:
-poker (Lukasz <3 ?)
-Old maid/popa-prostul (i wanna do this)
-big 2
"""


class BJCard(General.Card):
    def __init__(self, suit, number):
        General.Card.__init__(self, suit, number)

    def getValue(self):
        numNumber = self.getNumNumber()
        if numNumber > 9:
            return 10
        else:
            return numNumber + 1

    def __lt__(self, other):  # Makes it possible to sort cards according to their value
        return self.getValue() > other.getValue()


def value(hand):
    total = 0
    blackJack = 21
    sortedCards = sorted(hand)  # Sorting an array of cards shouldn't take too long

    index = 0
    while index < len(sortedCards):
        cardValue = sortedCards[index].getValue()
        if cardValue == 1:  # Handle aces here
            if index + 1 == len(sortedCards) and total + 11 <= blackJack:
                total += 11
            else:
                total += 1
        else:
            total += cardValue

        index += 1

    return total


class Dealer(General.CardContainer):
    def __init__(self):
        General.CardContainer.__init__(self, cardObject=BJCard)

    def show(self):
        hand = self.getCards()
        print("Dealer: {} and Unknown".format(hand[0].getName()))

    def play(self, deck):
        while value(self.getCards()) <= 16:
            deck.takeTopCard(self)
            print("The dealer took a card. ({})".format(self.getCards()[-1].getShortName()))


        if value(self.getCards()) > 21:
            print("Dealer's gone bust...")


def cardArray(hand):
    st = ""
    for i in hand:
        st += i.getShortName() + " "
    return st


def bet():
    while True:
        try:
            return int(input("\nHow much do you want to bet? £"))
        except:  # TODO fix
            print("Bad value, enter a number.")


class Player(General.CardContainer):
    def __init__(self):
        General.CardContainer.__init__(self, cardObject=BJCard)

    def play(self, deck):
        while True:
            print("Your cards: {}".format(cardArray(self.getCards())))
            valueP = value(self.getCards())
            print("Your calculated value: {} ".format(valueP))

            hitStandChoice = input("\nHit[h] or Stand[s]? ").lower()

            if hitStandChoice == "h":
                deck.takeTopCard(self)
                print("You got a", self.getCards()[-1].getShortName())
                if value(self.getCards()) > 21:
                    print("Sorry, you've gone bust.")
                    break
                if value(self.getCards()) == 21:
                    print("Blackjack!")
                    break
            elif hitStandChoice == "s":
                break

            else:
                print("Bad input, you must enter 'h' or 's'.")


class Game:
    def __init__(self):
        self.deck = General.Deck(cardObject=BJCard)
        self.deck.generateNewDeck()

    def play(self):
        self.deck.shuffleDeck()
        player = Player()
        dealer = Dealer()
        for i in 2 * [player, dealer]:
            self.deck.takeTopCard(i)

        playerBet = bet()

        dealer.show()

        player.play(self.deck)

        dealer.play(self.deck)

        # compare
        dealerValue = value(dealer.getCards())
        playerValue = value(player.getCards())

        print( "\n"+"=" * 20)
        print("The dealer has:")
        for card in dealer.getCards():
            print(card.getName())

        print("=" * 20)

        print("You have:")
        for card in player.getCards():
            print(card.getName())

        print("=" * 20, "\n")
        # print("")
        print("The dealer's value:", dealerValue)
        print("Your value: ", playerValue)
        print("The player bet:", playerBet)

        if playerValue > 21:
            print("Player loses.")

        elif dealerValue > 21:
            print("Dealer loses, Player wins.")

        elif playerValue == dealerValue:
            print("Dealer pushes, draw.")

        elif playerValue > dealerValue:
            print("Player wins.")

        else:  # playerValue < dealerValue:
            print("Dealer wins.")


if __name__ == "__main__":
    # execute only if run as a script
    # see https://docs.python.org/3/library/__main__.html
    play = True
    print("Blackjack")
    while play:
        Game().play()

        while True:
            # by convention capital letters mean default selection.
            choice = input("\nWould you like to play again ? [Y/n] ").lower()
            if choice == "n":
                play = False
                break
            elif choice == "y" or choice == "":
                break

            else:
                print("Please select a valid option.")
