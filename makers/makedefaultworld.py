import random
from .makemapobjects import MakeMapObjects
from static_objects.static_objects import Rock, Tree
from grass.grass import Grass
from creatures.herbivore import Herbivore
from creatures.predator import Predator
from actions.actions import Actions


class MakeDefaultWorld(Actions):
    @staticmethod
    def activate() -> None:
        for _ in range(random.randint(7, 10)):
            MakeMapObjects.activate(Rock)
            MakeMapObjects.activate(Tree)
        for _ in range(random.randint(18, 23)):
            MakeMapObjects.activate(Grass)
        for _ in range(random.randint(11, 15)):
            MakeMapObjects.activate(Herbivore)
        for _ in range(random.randint(6, 9)):
            MakeMapObjects.activate(Predator)
