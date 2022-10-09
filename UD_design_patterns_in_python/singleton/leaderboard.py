""""Leaderboard singleton class"""


class Leaderboard:
    """"The leaderboard is a singleton"""
    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def print(cls):
        """"A class level method to print result"""
        print('----------Leaderboard----------')
        for key, value in sorted(cls._table.items()):
            print(f'|\t{key}\t|\t{value}\t|')
        print()

    @classmethod
    def add_winner(cls, position, name):
        """"A class level method to add winner"""
        cls._table[position] = name
