"""Class for game 3 that uses the game interface"""

from interface_game import IGame
from leaderboard import Leaderboard


class Game3(IGame):  # pylint: disable=too-few-public-methods
    """"Game 1 that implements IGame interface"""

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)
