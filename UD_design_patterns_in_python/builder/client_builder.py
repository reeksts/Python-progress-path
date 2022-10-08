""" Client interface for build design pattern """

from igloo_director import IglooDirector
from castle_director import CastleDirector
from houseboat_director import HouseBoatDirector

igloo = IglooDirector.construct()
castle = CastleDirector.construct()
house_boat = HouseBoatDirector.construct()

print()
print(igloo.__class__)
print(castle.__class__)
print(house_boat.__class__)
print()

print(igloo.construction())
print(castle.construction())
print(house_boat.construction())
