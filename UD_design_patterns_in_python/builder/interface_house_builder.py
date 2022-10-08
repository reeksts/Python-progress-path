""" Interface for HouseBuilder class"""

from abc import ABCMeta, abstractmethod


class IHouseBuilder(metaclass=ABCMeta):
    """ The HouseBuilder interface """

    @abstractmethod
    def set_building_type(self, building_type):
        """ Sets the building type """

    # @staticmethod
    @abstractmethod
    def set_wall_material(self, wall_material):
        """ Sets the number of walls """

    # @staticmethod
    @abstractmethod
    def set_number_windows(self, number):
        """ Sets the number of windows """

    # @staticmethod
    @abstractmethod
    def set_number_doors(self, number):
        """ Sets the number of doors """

    # @staticmethod
    @abstractmethod
    def get_result(self):
        """ Returns the constructed result """
