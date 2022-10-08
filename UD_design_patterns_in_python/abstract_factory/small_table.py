""" Class of table chair """

from interface_table import ITable


class SmallTable(ITable):
    """ The Small Table concrete class that implements the ITable interface """

    def __init__(self):
        self._height = 80
        self._width = 60
        self._depth = 60

    def get_dimensions(self):
        dimensions = {
            'width': self._height,
            'height': self._width,
            'depth': self._depth,
        }

        return dimensions
