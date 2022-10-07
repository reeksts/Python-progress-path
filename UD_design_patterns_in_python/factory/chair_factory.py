""" The factory class """

from small_chair import SmallChair
from medium_chair import MediumChair
from large_chair import LargeChair


class ChairFactory:
    """ The factory class that instantiates chair objects """

    @staticmethod
    def get_chair(chair):
        """ A static method to instantiate chair object """
        if chair == 'SmallChair':
            return SmallChair()
        elif chair == 'MediumChair':
            return MediumChair()
        elif chair == 'LargeChair':
            return LargeChair()
        else:
            return None
