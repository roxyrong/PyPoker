import random
from constant import BuyIn
from player import PlayersInfo
from round_manager import RoundManager


class PokerGame:
    def __init__(self, num_players=6, buy_in=BuyIn, is_interactive=False):
        self.num_player = num_players
        self.players_info = PlayersInfo(num_players=num_players,
                                        buy_in=buy_in,
                                        is_interactive=is_interactive)
        self.round_manager = RoundManager(button=random.choice(range(num_players)),
                                          num_players=num_players,
                                          players_info=self.players_info)

    def start(self):
        print('initate_a new poker game')
        self.round_manager.start_new_round()


PokerGame().start()

