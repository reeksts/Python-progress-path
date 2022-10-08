""" Client app that can instantiate objects with factory class """

from furniture_factory import FurnitureFactory

chair = FurnitureFactory().get_furniture('MediumChair')
table = FurnitureFactory().get_furniture('LargeTable')

print(f'{chair.__class__}: {chair.get_dimensions()}')
print(f'{table.__class__}: {table.get_dimensions()}')

stuff = FurnitureFactory().get_furniture('ddf')
print(type(stuff))
