import random
from .makemapobjects import MakeMapObjects
from static_objects.static_objects import Rock, Tree
from grass.grass import Grass
from creatures.herbivore import Herbivore
from creatures.predator import Predator
from actions.actions import Actions
from config import ROCK_TREE_SPAWN_COUNT_RANGE, GRASS_SPAWN_COUNT_RANGE, HERBIVORE_SPAWN_COUNT_RANGE, PREDATOR_SPAWN_COUNT_RANGE


class MakeDefaultWorld(Actions):
    @staticmethod
    def activate() -> None:
        for _ in range(random.randint(*ROCK_TREE_SPAWN_COUNT_RANGE)):
            MakeMapObjects.activate(Rock)
            MakeMapObjects.activate(Tree)
        for _ in range(random.randint(*GRASS_SPAWN_COUNT_RANGE)):
            MakeMapObjects.activate(Grass)
        for _ in range(random.randint(*HERBIVORE_SPAWN_COUNT_RANGE)):
            MakeMapObjects.activate(Herbivore)
        for _ in range(random.randint(*PREDATOR_SPAWN_COUNT_RANGE)):
            MakeMapObjects.activate(Predator)
