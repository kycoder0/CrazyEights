import random
from random import randint

class Card:

        def __init__(self, rank, suit):
            self.rank = rank # rank of card
            self.suit = suit # suit of card

            # unique id for a card
            self.id = "{0}{1}".format(self.rank, self.suit)

        def __str__(self):
            # printing the card
            return "{0} of {1}".format(self.rank, self.suit)

            
class Deck:
    # the four suits
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

    # ranks of our cards
    rank_names = ["Ace", "One", "Two", "Three",
                  "Four", "Five", "Six", "Seven",
                  "Eight", "Nine", "Ten", "Jack",
                  "Queen", "King"]
            
    def __init__(self):
        self.newDeck()
        
    def newDeck(self):
        # dictionary of all cards {card id -> card)
        self.deck_dict = {card.id:card for card in self.getDeck()}

        # list of shuffled card ids
        self.deck = [cardId for cardId in self.deck_dict]
        random.shuffle(self.deck)
        self.size = len(self.deck)

    def newEmptyDeck(self):
        self.deck_dict = dict()
        self.deck = list()
        self.size = 0

    def getDeck(self):
        for rank in self.rank_names:
            for suit in self.suits:
                yield Card(rank, suit) # yields all the combinations of cards
    def peekTop(self):
        return self.deck_dict[self.deck[-1]]

    def removeTop(self):
        return self.deck_dict[self.deck.pop()]

    def addCard(self, card):
        self.deck_dict[card.id]  = card
        self.deck.append(card.id)
        self.size += 1

class Hand:

    def __init__(self, player_number):
        self.cards = []
        self.size = 0
        self.player_number = player_number

    def __str__(self):
        hand_str = "Player {0}'s hand: ".format(self.player_number)
        for index, card in enumerate(self.cards):
            hand_str += str(card) + "({0}), ".format(index)

        return hand_str[0 : -2]
    def addCard(self, card):
        self.cards.append(card)
        self.size += 1
    
    def removeCard(self, position):
        self.cards.pop(position)
        self.size -= 1

class Game:

    def __init__(self):
        # make the deck for the game
        self.deck = Deck()

        self.discard = Deck() # discard pile
        self.discard.newEmptyDeck() # empty deck

        # create the players
        self.player1 = Hand(1)
        self.player2 = Hand(2)

        

    def startGame(self):
        self.dealInitialHands() # deal the initial hands to the 2 players

        self.turn = randint(1, 2) # randomly choose player 1 or 2 to go first

        self.currentSuit = self.deck.peekTop().suit # get the suit of the top of the pile

        self.discard.addCard(self.deck.removeTop())

    def dealInitialHands(self):

        # deal each card one at a time to each player
        # each player gets a total of 5 cards
        self.player1.addCard(self.deck.removeTop())
        self.player2.addCard(self.deck.removeTop())
        self.player1.addCard(self.deck.removeTop())
        self.player2.addCard(self.deck.removeTop())
        self.player1.addCard(self.deck.removeTop())
        self.player2.addCard(self.deck.removeTop())
        self.player1.addCard(self.deck.removeTop())
        self.player2.addCard(self.deck.removeTop())
        self.player1.addCard(self.deck.removeTop())
        self.player2.addCard(self.deck.removeTop())

        if self.deck.peekTop().rank == "Eight": # restart the game if an eight is at the top
            self = Game()

    # player number signifies which player is moving
    # card is their move
    # newSuit must be specified if they play an eight
    def makeMove(self, playerNumber, cardIndex, newSuit):
        card = self.deck[cardIndex]
        if card.suit == self.currentSuit:
            self.discard.addCard(card)
        elif card.rank == self.discard.peekTop().rank:
            self.discard.addCard(card)
        elif card.rank == "Eight":
            self.discard.addCard(card)
            self.currentSuit = newSuit
    
    

game = Game()

game.startGame()

while True:
    print("Top of discard: {0}:".format(game.discard.peekTop()))
    if game.turn == 1:
        print(game.player1)
    else:
        print(game.player2)
    print("Player {0}, make your move: ".format(game.turn), end = '')
    move = input()
    game.makeMove(game.turn, move, "")