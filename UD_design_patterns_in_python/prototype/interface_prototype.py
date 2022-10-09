""" Interface for the Document class """

from abc import ABCMeta, abstractmethod


class IPrototype(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """ Interface that is used for creating the Document class """

    @abstractmethod
    def clone(self, mode):
        """ The clone method that can be implemented as shallow or deep """
