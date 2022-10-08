""" Client app that can instantiate objects with factory class """

from chair_factory import ChairFactory

chair = ChairFactory().get_chair('MediumChair')
print(chair.get_dimensions())
