from abc import ABC
import random
from wcwidth import wcswidth
random.seed(67)
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
        self.rock = '🗿'
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
    def __init__(self, name, speed=2, hp=4):
        super().__init__(name, speed, hp)
        self.herbivore = '🐰'
        self.eating_status = False
    def make_move(self):
        if self.eating_status:
            current_location = next(k for k, v in Map.collection.items() if v == self)
            Simulation.map[current_location[0]][current_location[1]] = '.'
            Map.free_slots.append(current_location)
            Grass.obj_collection.remove(self.nearest_grass[1])
            del Map.collection[current_location]
            Map.collection[self.nearest_grass[0]] = self
            Simulation.map[self.nearest_grass[0][0]][self.nearest_grass[0][1]] = self.herbivore
            del self.nearest_grass
            self.eating_status = False
        else:
            def search():
                current_slot = next(k for k, v in Map.collection.items() if v == self)
                destination = None
                queue = [current_slot]
                step_options = []
                while destination == None and queue:
                    current_slot = queue.pop(0) 
                    for vertical in range(-1, 2):
                        if destination:
                            break
                        for horizontal in range(-1, 2):
                            if (0 <= current_slot[0] + vertical <= 15 and 0 <= current_slot[1]  + horizontal <= 15) and ((vertical == 0) != (horizontal == 0)):
                                if isinstance(Map.collection.get((current_slot[0] + vertical, current_slot[1]  + horizontal)), Grass):
                                    destination = (current_slot[0] + vertical, current_slot[1]  + horizontal)
                                    break
                                new_slot = (current_slot[0] + vertical, current_slot[1] + horizontal)
                                if (current_slot[0] + vertical, current_slot[1]  + horizontal) not in Map.collection.keys() and not any(step[1] == new_slot for step in step_options):   
                                    queue.append((current_slot[0] + vertical, current_slot[1]  + horizontal))  
                                    step_options.append((current_slot, (current_slot[0] + vertical, current_slot[1]  + horizontal)))  
                return destination, step_options, current_slot
            def path_search(step_variations, eating_slot):
                path = [eating_slot]
                while path[-1] != next(k for k, v in Map.collection.items() if v == self):
                    path.append(next((step[0] for step in step_variations if step[1] == path[-1]), None))
                return path
            nearest_grass, step_variations, eating_slot = search()
            if nearest_grass == None:
                return
            current_location = next(k for k, v in Map.collection.items() if v == self)
            if eating_slot != current_location:
                path = path_search(step_variations, eating_slot)
                step_to_make = path[-(min(len(path) - 1, self.speed) + 1)]
                Simulation.map[current_location[0]][current_location[1]] = '.'
                Map.free_slots.append(current_location)
                del Map.collection[current_location]
                Simulation.map[step_to_make[0]][step_to_make[1]] = self.herbivore
                Map.collection[step_to_make] = self
                Map.free_slots.remove(step_to_make)
            else:
                self.nearest_grass = (nearest_grass, Map.collection[nearest_grass])
                Map.collection[self.nearest_grass[0]] = None          
                self.eating_status = True       
    


class Predator(Creature):
    def __init__(self, name, speed=1, hp=4, damage=2):
        super().__init__(name, speed, hp)
        self.damage = damage
        self.predator = '🐺'
    def make_move(self):
        def search():
            current_slot = next(k for k, v in Map.collection.items() if v == self)
            destination = None
            queue = [current_slot]
            step_options = []
            while destination == None and queue:
                current_slot = queue.pop(0) 
                for vertical in range(-1, 2):
                    if destination:
                        break
                    for horizontal in range(-1, 2):
                        if (0 <= current_slot[0] + vertical <= 15 and 0 <= current_slot[1]  + horizontal <= 15) and ((vertical == 0) != (horizontal == 0)):
                            if isinstance(Map.collection.get((current_slot[0] + vertical, current_slot[1]  + horizontal)), Herbivore):
                                destination = (current_slot[0] + vertical, current_slot[1]  + horizontal)
                                break
                            new_slot = (current_slot[0] + vertical, current_slot[1] + horizontal)
                            if (current_slot[0] + vertical, current_slot[1]  + horizontal) not in Map.collection.keys() and not any(step[1] == new_slot for step in step_options):   
                                queue.append((current_slot[0] + vertical, current_slot[1]  + horizontal))  
                                step_options.append((current_slot, (current_slot[0] + vertical, current_slot[1]  + horizontal)))  
            return destination, step_options, current_slot
        def path_search(step_variations, eating_slot):
            path = [eating_slot]
            while path[-1] != next(k for k, v in Map.collection.items() if v == self):
                path.append(next((step[0] for step in step_variations if step[1] == path[-1]), None))
            return path
        nearest_herbivore, step_variations, attacking_slot = search()
        if nearest_herbivore == None:
            return
        current_location = next(k for k, v in Map.collection.items() if v == self)
        if attacking_slot != current_location:
            path = path_search(step_variations, attacking_slot)
            step_to_make = path[-(min(len(path) - 1, self.speed) + 1)]
            Simulation.map[current_location[0]][current_location[1]] = '.'
            Map.free_slots.append(current_location)
            del Map.collection[current_location]
            Simulation.map[step_to_make[0]][step_to_make[1]] = self.predator
            Map.collection[step_to_make] = self
            Map.free_slots.remove(step_to_make)
        else:
            def attack(current_location, nearest_herbivore):
                herbivore = Map.collection[nearest_herbivore]
                herbivore.hp -= self.damage
                if herbivore.hp <= 0:
                    Simulation.map[current_location[0]][current_location[1]] = '.'
                    Map.free_slots.append(current_location)
                    del Map.collection[current_location]
                    Simulation.map[nearest_herbivore[0]][nearest_herbivore[1]] = self.predator
                    Map.collection[nearest_herbivore] = self
                    if herbivore.eating_status:
                        Map.collection[herbivore.nearest_grass[0]] = herbivore.nearest_grass[1]
                    Herbivore.obj_collection.remove(herbivore)
            attack(current_location, nearest_herbivore)
        
class Map:
    free_slots = [(vertical, horizontal) for vertical in range(16) for horizontal in range(16)]
    collection = {}
class Simulation:
    map = [['.' for horizontal in range(16)] for vertical in range(16)]
    @classmethod
    def render(cls):
        for row in Simulation.map:
            print(*((' ' * (4 - wcswidth(el)) + el for el in row)), sep=' ', end='\n\n')
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
            Map.collection[position] = name
            Simulation.map[position[0]][position[1]] = attr
            Map.free_slots.remove(position)
            classname.obj_collection.append(name)
        generate_map_obj()

