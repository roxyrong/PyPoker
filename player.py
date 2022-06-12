class Player:
    def __init__(self, player_id: int, initial_stack: int):
        self.player_id = player_id
        self.stack = initial_stack
        self.is_active = False
        self.cards = []
        self.rank = 0
        self.round_action_history = self.__init_round_action_histories()

    def update_status(self, status: bool):
        self.is_active = status

    def update_stack(self, winloss: int):
        self.stack += winloss

    def update_cards(self, cards):
        self.cards = cards

    def update_hand_rank(self, rank):
        self.rank = rank

    @staticmethod
    def __init_round_action_histories():
        return [None for _ in range(4)]


class PlayerInfo:
    def __init__(self, num_players: int, buy_in: int):
        self.player_ids = range(num_players)
        self.players = self.register_players(num_players, buy_in)

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
            self.players[player_id].update_statue(True)

    def update_cards(self, cards):
        for player_id in self.player_ids:
            self.players[player_id].update_cards(cards[player_id])

    def update_hand_ranks(self, ranks):
        for player_id in self.player_ids:
            self.players[player_id].update_hank_rank(ranks)

