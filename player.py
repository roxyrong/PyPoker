
class Player:
    def __init__(self, player_id: int, initial_stack: int):
        self.player_id = player_id
        self.stack = initial_stack
        self.status = False
        self.cards = []
        self.round_action_history = self.__init_round_action_histories()

    def update_status(self, status: bool):
        self.status = status

    def update_stack(self, winloss: int):
        self.stack += winloss

    def update_cards(self, cards):
        self.cards = cards

    @staticmethod
    def __init_round_action_histories():
        return [None for _ in range(4)]


class PlayerInfo:
    def __init__(self, num_players: int, buy_in: int):
        self.player_ids = range(num_players)
        self.players = self.register_players(num_players, buy_in)

    @staticmethod
    def register_players(num_players, buy_in):
        return {player_id: Player(player_id=player_id, initial_stack=buy_in) for player_id in range(num_players)}

    def reset_status(self):
        for player_id in self.player_ids:
            self.players[player_id].update_statue(True)

    def update_cards(self, cards):
        for player_id in self.player_ids:
            self.players[player_id].update_cards(cards[player_id])

