""" The chair factory class """

from small_table import SmallTable
from medium_table import MediumTable
from large_table import LargeTable


class TableFactory:
    """ The chair factory class that instantiates chair objects """

    @staticmethod
    def get_table(table):
        """ A static method to instantiate chair object """
        try:
            if table == 'SmallTable':
                return SmallTable()
            elif table == 'MediumTable':
                return MediumTable()
            elif table == 'LargeTable':
                return LargeTable()
            raise Exception('Table not found')
        except Exception as _e:
            print(_e)
        return None

