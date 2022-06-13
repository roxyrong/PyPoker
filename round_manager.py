from constant import Round
from deck import Deck
from player import PlayersInfo
from pot import Pot
from evaluator import PokerEvaluator


class RoundManager:
    def __init__(self, button: int, num_players: int, players_info: PlayersInfo):
        self.num_players = num_players
        self.players_info = players_info
        self.player_action_seq = []
        self.button = button
        self.deck = Deck()
        self._pre_flop = {}
        self._flop = []
        self._turn = []
        self._river = []
        self.round = Round.PRE_FLOP
        self.pot = Pot()

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
        self.reset_deck_and_pot()
        self.players_info.reset_status()
        self.player_action_seq = self.generate_action_sequence()
        self.set_small_big_blind()
        self.deal_preflop()
        self.deal_flop()
        self.deal_turn()
        self.deal_river()
        self.evaluate_game()
        self.button = (self.button + 1) % self.num_players

    def generate_action_sequence(self):
        return list(range(self.button, self.num_players)) + list(range(self.button))

    def set_small_big_blind(self):
        sm_blind = (self.button + 1) % self.num_players
        big_blind = (self.button + 2) % self.num_players
        self.players_info.player(sm_blind)

    def deal_preflop(self):
        self.round = Round.PRE_FLOP
        cards = {}
        ranks = {}
        for i in self.player_action_seq:
            cards[i] = self.deck.draw(2)
            ranks[i] = self.evaluate_hand(hand=cards[i])
        self._pre_flop = cards
        self.players_info.update_cards(cards)
        self.players_info.update_hand_ranks(ranks)

    def deal_flop(self):
        self.round = Round.FLOP
        self._flop = self.deck.draw(3)
        ranks = {}
        for player_id in self.player_action_seq:
            ranks[player_id] = self.evaluate_hand(hand=self.pre_flop[player_id])
        self.players_info.update_hand_ranks(ranks)

    def deal_turn(self):
        self.round = Round.TURN
        self._turn = self.deck.draw(1)

    def deal_river(self):
        self.round = Round.RIVER
        self._river = self.deck.draw(1)

    def reset_deck_and_pot(self):
        self.deck.shuffle()
        self._pre_flop = {}
        self._flop = []
        self._turn = []
        self._river = []
        self.round = Round.PRE_FLOP
        self.pot = Pot()

    def evaluate_hand(self, hand):
        if self.round not in Round:
            raise ValueError("round can only be 0 to 3")
        rank = 0
        if self.round == Round.PRE_FLOP:
            rank = PokerEvaluator.evaluate_preflop(hand)
        if self.round == Round.FLOP:
            rank = PokerEvaluator.evaluate_flop(hand, self.board)
        if self.round == Round.TURN:
            rank = PokerEvaluator.evaluate_turn(hand, self.board)
        if self.round == Round.RIVER:
            rank = PokerEvaluator.evaluate_river(hand, self.board)
        return rank

    def evaluate_game(self):
        hand_ranks = {}
        for player_id in range(self.num_players):
            player = self.players_info.player(player_id=player_id)
            if player.is_active:
                hand_ranks[player_id] = player.hand_rank
        hand_ranks = sorted(hand_ranks)
        return hand_ranks







