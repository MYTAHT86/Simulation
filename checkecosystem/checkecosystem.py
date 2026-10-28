import random

from makers.makemapobjects import MakeMapObjects
from grass.grass import Grass
from creatures.herbivore import Herbivore
from creatures.predator import Predator
from map.map import Map
from actions.actions import Actions
from config import GRASS_RESPAWN_COUNT_RANGE, PREDATOR_RESPAWN_COUNT_RANGE, HERBIVORE_RESPAWN_COUNT_RANGE


class CheckEcoSystem(Actions):
    @classmethod
    def activate(cls) -> None:
        if len(list(filter(lambda x: isinstance(x, Herbivore), Map.collection.values()))) < 6:
            for _ in range(random.randint(*HERBIVORE_RESPAWN_COUNT_RANGE)):
                MakeMapObjects.activate(Herbivore)
        if len(list(filter(lambda x: isinstance(x, Predator), Map.collection.values()))) < 3:
            for _ in range(random.randint(*PREDATOR_RESPAWN_COUNT_RANGE)):
                MakeMapObjects.activate(Predator)
        if len(list(filter(lambda x: isinstance(x, Grass), Map.collection.values()))) < 12:
            for _ in range(random.randint(*PREDATOR_RESPAWN_COUNT_RANGE)):
                MakeMapObjects.activate(Grass)