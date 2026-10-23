import random

from makers.makemapobjects import MakeMapObjects
from grass.grass import Grass
from creatures.herbivore import Herbivore
from creatures.predator import Predator
from map.map import Map


class CheckEcoSystem:
    @classmethod
    def activate(cls):
        if len(list(filter(lambda x: isinstance(x, Herbivore), Map.collection.values()))) == 0:
            for _ in range(random.randint(1, 3)):
                MakeMapObjects.process(Herbivore)
        if len(list(filter(lambda x: isinstance(x, Predator), Map.collection.values()))) == 0:
            for _ in range(random.randint(1, 3)):
                MakeMapObjects.process(Predator)
        if len(list(filter(lambda x: isinstance(x, Grass), Map.collection.values()))) == 0:
            for _ in range(random.randint(1, 3)):
                MakeMapObjects.process(Grass)