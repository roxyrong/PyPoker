import random
from poker import Card

FULL_DECK = list(Card)


class Deck:
    def __init__(self):
        self.deck = FULL_DECK
        self.shuffle()

    def shuffle(self):
        self.deck = FULL_DECK
        random.shuffle(self.deck)

    def draw(self, n=1):
        if n == 1:
            return self.deck.pop()

        return [self.deck.pop() for __ in range(n)]
