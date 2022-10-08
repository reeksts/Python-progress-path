""" Class of large table """

from interface_table import ITable


class LargeTable(ITable):
    """ The LargeTable concrete class that implements the ITable interface """

    def __init__(self):
        self._height = 80
        self._width = 100
        self._depth = 100

    def get_dimensions(self):
        dimensions = {
            'width': self._height,
            'height': self._width,
            'depth': self._depth,
        }

        return dimensions
