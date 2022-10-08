""" Class of small chair """

from interface_chair import IChair


class SmallChair(IChair):
    """ The Small Chair concrete class that implements the IChair interface """

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def get_dimensions(self):
        dimensions = {
            'width': self._height,
            'height': self._width,
            'depth': self._depth,
        }

        return dimensions
