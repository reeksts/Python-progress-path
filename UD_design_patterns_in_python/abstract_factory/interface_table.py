""" The table interface """


from abc import ABCMeta, abstractmethod


class ITable(metaclass=ABCMeta):
    """ The table interface """

    @staticmethod
    @abstractmethod
    def get_dimensions():
        """ A static interface method """
