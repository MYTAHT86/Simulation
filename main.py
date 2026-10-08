from abc import ABC
import random
class Entity(ABC):
    def __init__(self, name):
        self.name = name
    def __init_subclass__(cls):
        cls.obj_collection = []
    def __repr__(self):
        return f'{self.name}'
class Rock(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.rock = '🪨'
class Tree(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.tree = '🌳'
class Grass(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.grass = '🌿'
class Creature(Entity):
    def __init__(self, name, speed=1, hp=5):
        super().__init__(name)
        self.speed = speed
        self.hp = hp
    def make_move(self):
        pass
class Herbivore(Creature):
    def __init__(self, name, speed=1, hp=5):
        super().__init__(name, speed, hp)
        self.herbivore = '🐰'
    def make_move(self):
        pass
class Predator(Creature):
    def __init__(self, name, speed=1, hp=5):
        super().__init__(name, speed, hp)
        self.predator = '🐺'
    def make_move(self):
        pass
class Map:
    free_slots = [(vertical, horizontal) for vertical in range(16) for horizontal in range(16)]
    collection = {}
class Simulation:
    map = [['.' for horizontal in range(16)] for vertical in range(16)]
    @classmethod
    def render(cls):
        for row in Simulation.map:
            print(*row)

class Action:
    def __init__(self):
        init_actions = [MakeDefaultWorld]
        turn_actions = []
class MakeDefaultWorld(Action):
    def __init__(self):
        def generate_map_obj():
            for i in range(1, 6):
                make_map_obj(Rock, i)
                make_map_obj(Tree, i)
                make_map_obj(Grass, i)
                make_map_obj(Herbivore, i)
                make_map_obj(Predator, i)
        def make_map_obj(classname, i):
            name_creator = f'{classname.__name__}{i}'
            name = classname(name_creator)
            position = random.choice(Map.free_slots)
            attr = getattr(name, classname.__name__.lower())
            Map.collection[position] = attr
            Simulation.map[position[0]][position[1]] = attr
            Map.free_slots.remove(position)
            classname.obj_collection.append(name)
        generate_map_obj()


Simulation.render()
MakeDefaultWorld()
print()
Simulation.render()
print(Grass.obj_collection)



