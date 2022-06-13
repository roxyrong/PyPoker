from enum import Enum

SB = 100
BB = 100
BuyIn = 10000


class Round(Enum):
    PRE_FLOP = 0
    FLOP = 1
    TURN = 2
    RIVER = 3
    SHOWDOWN = 4


class PokerAction:
    FOLD = 0
    CHECK = 1
    CALL = 2
    RAISE = 3
    SMALLBLIND = 4
    BIGBLIND = 5





