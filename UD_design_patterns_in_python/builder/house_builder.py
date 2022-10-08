""" HouseBuilder class that implements teh house builder interface """

from interface_house_builder import IHouseBuilder
from house import House


class HouseBuilder(IHouseBuilder):
    """ House builder class that builds the product """

    def __init__(self):
        self._house = House()

    def set_building_type(self, building_type):
        self._house.building_type = building_type
        return self

    def set_wall_material(self, wall_material):
        self._house.wall_material = wall_material
        return self

    def set_number_windows(self, number):
        self._house.windows = number
        return self

    def set_number_doors(self, number):
        self._house.doors = number
        return self

    def get_result(self):
        return self._house
