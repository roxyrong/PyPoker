from common import ByDefinitionOrderEnum
from enum import Enum
import functools


class Suit(ByDefinitionOrderEnum):
    CLUBS = "♣", "c", "clubs"
    DIAMONDS = "♦", "d", "diamonds"
    HEARTS = "♥", "h", "hearts"
    SPADES = "♠", "s", "spades"


class Rank(ByDefinitionOrderEnum):
    DEUCE = "2", 2
    THREE = "3", 3
    FOUR = "4", 4
    FIVE = "5", 5
    SIX = "6", 6
    SEVEN = "7", 7
    EIGHT = "8", 8
    NINE = "9", 9
    TEN = "T", 10
    JACK = ("J",)
    QUEEN = ("Q",)
    KING = ("K",)
    ACE = "A", 1


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit
