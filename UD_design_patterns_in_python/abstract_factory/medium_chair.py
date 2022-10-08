""" Class of medium chair """

from interface_chair import IChair


class MediumChair(IChair):
    """ The MediumChair concrete class that implements the IChair interface """

    def __init__(self):
        self._height = 60
        self._width = 60
        self._depth = 60

    def get_dimensions(self):
        dimensions = {
            'width': self._height,
            'height': self._width,
            'depth': self._depth,
        }

        return dimensions
