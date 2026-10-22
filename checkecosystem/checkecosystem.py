import random
from makers.makemapobjects import MakeMapObjects
from grass.grass import Grass
from creatures.herbivore import Herbivore
from creatures.predator import Predator
class CheckEcoSystem:
    @classmethod
    def activate(cls):
        if len(Herbivore.obj_collection) == 0:
            for _ in range(random.randint(1, 3)):
                MakeMapObjects.process(Herbivore)
        if len(Predator.obj_collection) == 0:
            for _ in range(random.randint(1, 3)):
                MakeMapObjects.process(Predator)
        if len(Grass.obj_collection) == 0:
            for _ in range(random.randint(1, 3)):
                MakeMapObjects.process(Grass)