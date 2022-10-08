""" House class that is called when HouseBuilder is used """


class House:  # pylint: disable=too-few-public-methods
    """ House class that is called when HouseBuilder is used """

    def __init__(self, building_type='Apartment', doors=0,
                 windows=0, wall_material='Brick'):
        self.building_type = building_type
        self.wall_material = wall_material
        self.doors = doors
        self.windows = windows

    def construction(self):
        """ Return a string object with constructed parts """

        house = f'This is a {self.wall_material} {self.building_type} ' \
                f'with {self.doors} door(s) and {self.windows} window(s)'

        return house
