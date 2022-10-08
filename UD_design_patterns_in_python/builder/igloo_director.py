""" Director class """

from house_builder import HouseBuilder


class IglooDirector:  # pylint: disable=too-few-public-methods
    """ One of the directors that can build complex representation. """

    @staticmethod
    def construct():
        """
        Constructs and returns the final product.
        All the methods used in the return can also be called separately instead of a chained call.
        """

        return HouseBuilder()\
            .set_building_type('Igloo')\
            .set_wall_material('Ice')\
            .set_number_doors(1)\
            .get_result()
