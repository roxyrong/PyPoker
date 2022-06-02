import random

from constant import BuyIn
from deck import Deck
from player import PlayerInfo


class PokerGame:
    def __init__(self, num_players=6, buy_in=BuyIn):
        self.num_player = num_players
        self.players = PlayerInfo(num_players=num_players,
                                  buy_in=buy_in)

        self.deck = Deck()
        self._flop = None
        self._turn = None
        self._river = None

    def start_new_round(self):
        self.players.reset_status()
        self.deck.shuffle()
        self.deal_preflop()
        self.deal_flop()
        self.deal_turn()
        self.deal_river()

    def deal_preflop(self):
        cards = {}
        for i in range(self.num_player):
            cards[i] = self.deck.draw(2)
        self.players.update_cards(cards)

    def deal_flop(self):
        self._flop = self.deck.draw(3)

    def deal_turn(self):
        self._turn = self.deck.draw(1)

    def deal_river(self):
        self._river = self.deck.draw(1)
