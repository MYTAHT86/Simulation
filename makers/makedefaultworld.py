from .makemapobjects import MakeMapObjects
from static_objects.static_objects import Rock, Tree
from grass.grass import Grass
from creatures.herbivore import Herbivore
from creatures.predator import Predator
class MakeDefaultWorld:
    def generate_map_obj():
        for i in range(5):
            MakeMapObjects.process(Rock)
            MakeMapObjects.process(Tree)
            MakeMapObjects.process(Grass)
            MakeMapObjects.process(Herbivore)
            MakeMapObjects.process(Predator)
    generate_map_obj()