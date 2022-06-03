from collections import Counter
from player import Player


class Pot:
    def __init__(self):
        self._pot = Counter()

    @property
    def pot(self):
        return self._pot

    @property
    def total_chips(self):
        return sum(self._pot.values())

    def add_chips(self, player: Player, chips):
        self._pot[player] += chips

    def reset(self):
        self._pot = Counter()

    @property
    def side_pot(self):
        side_pots = []
        if not len(self._pot):
            return []
        pot = {k: v for k, v in self._pot.items()}
        while len(self._pot):
            side_pot = {}
            min_chips = min(pot.values())
            players_to_pop = []
            for player, chips in pot:
                if chips == min_chips:
                    players_to_pop.append(player)
                pot[player] -= min_chips
                side_pot[player] = min_chips
            for player in players_to_pop:
                pot.pop(player)
            side_pots.append(side_pot)
        return side_pots






