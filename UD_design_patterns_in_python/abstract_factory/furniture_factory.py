""" Furniture factory that implements the furniture factory interface """

from interface_furniture_factory import IFurnitureFactory
from chair_factory import ChairFactory
from table_factory import TableFactory


class FurnitureFactory(IFurnitureFactory):
    """ Furniture factory that implements the furniture factory interface """

    @staticmethod
    def get_furniture(furniture):
        """ Static method to get furniture """
        try:
            if furniture in ['SmallChair', 'MediumChair', 'LargeChair']:
                return ChairFactory.get_chair(furniture)
            elif furniture in ['SmallTable', 'MediumTable', 'LargeTable']:
                return TableFactory.get_table(furniture)
            raise Exception('Furniture not found!')
        except Exception as _e:
            print(_e)
        return None

