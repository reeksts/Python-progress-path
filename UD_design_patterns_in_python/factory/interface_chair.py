""" The chair interface """


from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):
    """ The chair interface """

    @staticmethod
    @abstractmethod
    def get_dimensions():
        """ A static interface method """
