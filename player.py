from constant import PokerAction


class Player:
    def __init__(self, player_id: int, initial_stack: int):
        self.player_id = player_id
        self._stack = initial_stack
        self.is_active = False
        self.cards = []
        self._hand_rank = 0
        self.round_action_history = self.__init_round_action_histories()
        self.round_rank_history = self.__init_round_hand_rank_histories()

    @property
    def stack(self):
        return self._stack

    @property
    def hand_rank(self):
        return self._hand_rank

    def update_status(self, status: bool):
        self.is_active = status

    def update_cards(self, cards):
        self.cards = cards

    def update_hand_rank(self, hand_rank):
        self._hand_rank = hand_rank

    def append_chips(self, amount):
        self._stack += amount

    def collect_bets(self, amount):
        ## TODO: handle not enough amount
        self._stack -= amount

    def bet(self, amount):
        self.collect_bets(amount)

    def declare_action(self, action: PokerAction, amount):
        if action == PokerAction.FOLD:
            self.is_active = False
        elif action == PokerAction.CHECK:
            pass
        else:
            self.bet(amount)

    @staticmethod
    def __init_round_action_histories():
        return [None for _ in range(4)]

    @staticmethod
    def __init_round_hand_rank_histories():
        return [None for _ in range(4)]


class PlayersInfo:
    def __init__(self, num_players: int, buy_in: int, is_interactive=False):
        self.player_ids = range(num_players)
        self.players = self.register_players(num_players, buy_in)

    def player(self, player_id):
        return self.players[player_id]

    @property
    def cards(self):
        cards = {}
        for player_id, player in self.players:
            cards[player_id] = player.cards
        return cards

    @staticmethod
    def register_players(num_players, buy_in):
        return {player_id: Player(player_id=player_id, initial_stack=buy_in) for player_id in range(num_players)}

    def reset_status(self):
        for player_id in self.player_ids:
            self.players[player_id].update_status(True)

    def update_cards(self, cards):
        for player_id in self.player_ids:
            self.players[player_id].update_cards(cards[player_id])

    def update_hand_ranks(self, hand_ranks):
        for player_id in self.player_ids:
            self.players[player_id].update_hand_rank(hand_ranks)

