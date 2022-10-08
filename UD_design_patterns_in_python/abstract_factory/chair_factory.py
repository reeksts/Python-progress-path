""" The chair factory class """

from small_chair import SmallChair
from medium_chair import MediumChair
from large_chair import LargeChair


class ChairFactory:
    """ The chair factory class that instantiates chair objects """

    @staticmethod
    def get_chair(chair):
        """ A static method to instantiate chair object """
        try:
            if chair == 'SmallChair':
                return SmallChair()
            elif chair == 'MediumChair':
                return MediumChair()
            elif chair == 'LargeChair':
                return LargeChair()
            raise Exception('Chair not found!')
        except Exception as _e:
            print(_e)
        return None
