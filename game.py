from constant import BuyIn
from deck import Deck
from player import PlayerInfo
from evaluator import PokerEvaluator


class PokerGame:
    def __init__(self, num_players=6, buy_in=BuyIn):
        self.num_player = num_players
        self.players = PlayerInfo(num_players=num_players,
                                  buy_in=buy_in)

        self.deck = Deck()
        self._pre_flop = {}
        self._flop = []
        self._turn = []
        self._river = []
        self.round = 0

    @property
    def pre_flop(self):
        return self._pre_flop

    @property
    def flop(self):
        return self._flop

    @property
    def turn(self):
        return self._turn

    @property
    def river(self):
        return self._river

    @property
    def board(self):
        if not self._flop:
            return []
        if not self._turn:
            return self._flop
        if not self._river:
            return self._flop + [self._turn]
        return self._flop + [self._turn] + [self.river]

    def start_new_round(self):
        self.players.reset_status()
        self.deck.shuffle()
        self.deal_preflop()
        self.deal_flop()
        self.deal_turn()
        self.deal_river()

    def deal_preflop(self):
        self.round = 0
        cards = {}
        ranks = {}
        for i in range(self.num_player):
            cards[i] = self.deck.draw(2)
            ranks[i] = self.evaluate_hand(hand=cards[i])
        self._pre_flop = cards
        self.players.update_cards(cards)
        self.players.update_hand_ranks(ranks)

    def deal_flop(self):
        self.round = 1
        self._flop = self.deck.draw(3)
        ranks = {}
        for i in range(self.num_player):
            ranks[i] = self.evaluate_hand(hand=self.pre_flop[i])
        self.players.update_hand_ranks(ranks)

    def deal_turn(self):
        self.round = 2
        self._turn = self.deck.draw(1)

    def deal_river(self):
        self.round = 3
        self._river = self.deck.draw(1)

    def evaluate_hand(self, hand):
        if self.round not in range(3):
            raise ValueError("round can only be 0 to 3")
        rank = 0
        if self.round == 0:
            rank = PokerEvaluator.evaluate_preflop(hand)
        if self.round == 1:
            rank = PokerEvaluator.evaluate_flop(hand, self.board)
        if self.round == 2:
            rank = PokerEvaluator.evaluate_turn(hand, self.board)
        if self.round == 3:
            rank = PokerEvaluator.evaluate_river(hand, self.board)
        return rank

