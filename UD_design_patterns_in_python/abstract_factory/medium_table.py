""" Class of medium table """

from interface_table import ITable


class MediumTable(ITable):
    """ The MediumTable concrete class that implements the ITable interface """

    def __init__(self):
        self._height = 80
        self._width = 80
        self._depth = 80

    def get_dimensions(self):
        dimensions = {
            'width': self._height,
            'height': self._width,
            'depth': self._depth,
        }

        return dimensions
