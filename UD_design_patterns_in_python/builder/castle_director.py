""" Director class """

from house_builder import HouseBuilder


class CastleDirector:  # pylint: disable=too-few-public-methods
    """ One of the directors that can build complex representation. """

    @staticmethod
    def construct():
        """
        Constructs and returns the final product.
        All the methods used in the return can also be called separately instead of a chained call.
        """

        return HouseBuilder()\
            .set_building_type('Castle')\
            .set_wall_material('Sandstone')\
            .set_number_doors(100)\
            .set_number_windows(100)\
            .get_result()
