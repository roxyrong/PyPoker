import random
from poker import Card as IterCard
from pokereval.card import Card


class PokerCard(IterCard):
    # Combine two poker card packages to work better with poker hand evaluator
    STRING_TO_SUIT = {"s": 1, "h": 2, "d": 3, "c": 4}
    STRING_TO_RANK = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12,
                      'K': 13, 'A': 14}

    @property
    def numerical(self):
        rank = self.rank.value[0]
        suit = self.suit.value[1]
        rank = self.STRING_TO_RANK[rank]
        suit = self.STRING_TO_SUIT[suit]
        return Card(rank, suit)


FULL_DECK = list(PokerCard)


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
