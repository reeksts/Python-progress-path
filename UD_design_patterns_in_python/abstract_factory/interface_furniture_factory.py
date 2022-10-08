""" The furniture factory interface """

from abc import ABCMeta, abstractmethod


class IFurnitureFactory(metaclass=ABCMeta):
    """ The furniture factory interface """

    @staticmethod
    @abstractmethod
    def get_furniture(furniture):
        """ A static interface method """
