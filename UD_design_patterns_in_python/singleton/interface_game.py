""""A game interface"""

from abc import ABCMeta, abstractmethod


class IGame(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """Interface for game class"""

    @abstractmethod
    def add_winner(self, position, name):
        """"A method to add winner for the game"""
