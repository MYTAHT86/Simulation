from abc import ABC
import random
from wcwidth import wcswidth
import os 
import time
import msvcrt
random.seed(67)
class Entity(ABC):
    def __init__(self, name):
        self.name = name
    def __init_subclass__(cls):
        cls.obj_collection = []
    def __repr__(self):
        return f'{self.name}'
    def delete_instance(self):
        self.__class__.obj_collection.remove(self)
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
    def search(self, classname_to_find):
        current_slot = Map.find_current_slot(self)
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
                        if Map.isinstance_check(current_slot, vertical, horizontal, classname_to_find):
                            destination = (current_slot[0] + vertical, current_slot[1]  + horizontal)
                            break
                        new_slot = (current_slot[0] + vertical, current_slot[1] + horizontal)
                        if Map.slots_check(current_slot, vertical, horizontal) and not any(step[1] == new_slot for step in step_options):   
                            queue.append((current_slot[0] + vertical, current_slot[1]  + horizontal))  
                            step_options.append((current_slot, (current_slot[0] + vertical, current_slot[1]  + horizontal)))
        return destination, step_options, current_slot
    def path_search(self, step_variations, eating_slot):
        path = [eating_slot]
        while path[-1] != Map.find_current_slot(self):
            path.append(next((step[0] for step in step_variations if step[1] == path[-1]), None))
        return path
    def lose_hp(self):
        pass
class Herbivore(Creature):
    def __init__(self, name, speed=2, hp=4):
        super().__init__(name, speed, hp)
        self.herbivore = '🐰'
        self.eating_status = False
    def make_move(self):
        if self.eating_status:
            Map.herbivore_eat_on_map(self, self.nearest_grass)
            Grass.delete_instance(self.nearest_grass[1])
            del self.nearest_grass
            self.eating_status = False
        else:
            nearest_grass, step_variations, eating_slot = self.search(Grass)
            if nearest_grass == None:
                return
            current_location = Map.find_current_slot(self)
            if eating_slot != current_location:
                path = self.path_search(step_variations, eating_slot)
                step_to_make = path[-(min(len(path) - 1, self.speed) + 1)]
                Map.herbivore_move_on_map(self, current_location, step_to_make)
            else:
                self.nearest_grass = (nearest_grass, Map.find_instance(nearest_grass))
                Map.change_instance_on_map(self)         
                self.eating_status = True       
    def lose_hp(self, instance):
        self.hp -= instance.damage
        if self.hp <= 0:
            if self.eating_status:
                Map.change_instance_on_map(self, self.nearest_grass[1])
            location = Map.find_current_slot(self)  
            Map.delete_on_map(location)
            Map.add_free_slot(location)
            Herbivore.delete_instance(self)         
class Predator(Creature):
    def __init__(self, name, speed=1, hp=4, damage=2):
        super().__init__(name, speed, hp)
        self.damage = damage
        self.predator = '🐺'
        self.hunger = 0
        self.full_status = False
    def make_move(self):
        def hunger_process(self):
            if self.full_status == False:    
                if self.hunger == 3:
                    self.hp -= 1
                else:
                    self.hunger += 1  
            if self.hp <= 0:
                location = Map.find_current_slot(self)
                Map.delete_on_map(location)
                Map.add_free_slot(location)
                Map.delete_instance_on_map(location)
                Predator.delete_instance(self)
            self.full_status = False
        nearest_herbivore, step_variations, attacking_slot = self.search(Herbivore)
        if nearest_herbivore == None:
            hunger_process(self)
            return
        current_location = Map.find_current_slot(self)
        if attacking_slot != current_location:
            path = self.path_search(step_variations, attacking_slot)
            step_to_make = path[-(min(len(path) - 1, self.speed) + 1)]
            Map.predator_move_on_map(self, current_location, step_to_make)
            hunger_process(self)
        else:
            def attack(current_location, nearest_herbivore):
                herbivore = Map.find_instance(nearest_herbivore)
                herbivore.lose_hp(self)
                if not Map.check_location(nearest_herbivore):
                    Map.predator_move_on_map(self, current_location, nearest_herbivore)
                    self.hunger = 0
                    self.hp = min(self.hp + 2, 4)
                    self.full_status = True               
            attack(current_location, nearest_herbivore)
            hunger_process(self)
class Map:
    free_slots = [(vertical, horizontal) for vertical in range(16) for horizontal in range(16)]
    collection = {}
    @classmethod
    def herbivore_eat_on_map(cls, instance, nearest_grass):
        current_location = Map.find_current_slot(instance)
        Map.map[current_location[0]][current_location[1]] = '.'
        Map.add_free_slot(current_location)
        Map.delete_on_map(current_location)
        Map.collection[instance.nearest_grass[0]] = instance
        Map.map[instance.nearest_grass[0][0]][instance.nearest_grass[0][1]] = instance.herbivore
    @classmethod
    def herbivore_move_on_map(cls, instance, current_location, step_to_make):
        Map.map[current_location[0]][current_location[1]] = '.'
        Map.add_free_slot(current_location)
        Map.delete_on_map(current_location, step_to_make)
        Map.map[step_to_make[0]][step_to_make[1]] = instance.herbivore
        Map.collection[step_to_make] = instance
    @classmethod
    def predator_move_on_map(cls, instance, current_location, step_to_make):
        Map.map[current_location[0]][current_location[1]] = '.'
        Map.add_free_slot(current_location)
        Map.delete_on_map(current_location, step_to_make)
        Map.map[step_to_make[0]][step_to_make[1]] = instance.predator
        Map.collection[step_to_make] = instance
    @classmethod
    def delete_on_map(cls, current_location, step_to_make=None):
        if step_to_make:
            del Map.collection[current_location]
            Map.free_slots.remove(step_to_make)
        else:
            del Map.collection[current_location]
    @classmethod
    def find_current_slot(cls, instance):
        return next(k for k, v in Map.collection.items() if v == instance)
    @classmethod
    def isinstance_check(cls, current_slot, vertical, horizontal, classname):
        return isinstance(Map.collection.get((current_slot[0] + vertical, current_slot[1]  + horizontal)), classname)
    @classmethod
    def slots_check(cls, current_slot, vertical, horizontal):
        return (current_slot[0] + vertical, current_slot[1]  + horizontal) not in Map.collection.keys()
    @classmethod
    def find_instance(cls, location):
        return Map.collection[location]
    @classmethod
    def change_instance_on_map(cls, instance, value=None):
         Map.collection[instance.nearest_grass[0]] = value
    @classmethod
    def delete_instance_on_map(cls, location):
        Map.map[location[0]][location[1]] = '.'
    @classmethod
    def check_location(cls, location):
        return location in Map.collection.keys()
    @classmethod
    def add_free_slot(cls, location):
        Map.free_slots.append(location)
    @classmethod
    def setup_map_obj(cls, name, attr):
        position = random.choice(Map.free_slots)
        Map.collection[position] = name
        Map.map[position[0]][position[1]] = attr
        Map.free_slots.remove(position)
class MakeMap:
    Map.map = [['.' for horizontal in range(16)] for vertical in range(16)] 
class MakeMapObj:
    @classmethod
    def process(cls, classname):
        name_creator = f'{classname.__name__}{len(classname.obj_collection) + 1}'
        name = classname(name_creator)
        attr = getattr(name, classname.__name__.lower())
        Map.setup_map_obj(name, attr)
        classname.obj_collection.append(name)      
class MakeDefaultWorld:
    def generate_map_obj():
        for i in range(5):
            MakeMapObj.process(Rock)
            MakeMapObj.process(Tree)
            MakeMapObj.process(Grass)
            MakeMapObj.process(Herbivore)
            MakeMapObj.process(Predator)
    generate_map_obj()
class CheckEcoSystem:
    @classmethod
    def activate(cls):
        if len(Herbivore.obj_collection) == 0:
            for _ in range(random.randint(1, 3)):
                MakeMapObj.process(Herbivore)
        if len(Predator.obj_collection) == 0:
            for _ in range(random.randint(1, 3)):
                MakeMapObj.process(Predator)
        if len(Grass.obj_collection) == 0:
            for _ in range(random.randint(1, 3)):
                MakeMapObj.process(Grass)
class CheckforPause:
        @classmethod
        def activate(cls):
            if msvcrt.kbhit():
                user_input = msvcrt.getch()
                if user_input == b' ':
                    Simulation.pause_simulation()
                    print("Симуляция приостановлена, для возобновления нажмите Пробел")
                elif user_input == b'e':
                    Simulation.break_status = True
class Simulation:
    simulating = True
    turns_count = 0
    break_status = False
    @classmethod
    def render(cls):
        for row in Map.map:
            print(*((' ' * (4 - wcswidth(el)) + el for el in row)), sep=' ', end='\n\n')
        print(f"Количество проделанных ходов {Simulation.turns_count}")
        print()     
    @classmethod
    def next_turn(cls):
        os.system("cls")
        for ex in Herbivore.obj_collection:
            ex.make_move()
        for ex in Predator.obj_collection:
            ex.make_move()   
        Simulation.turns_count += 1
        Simulation.render()
        time.sleep(2)
    @classmethod
    def start_simulation(cls):
        Simulation.simulating = True
        while Simulation.simulating:
            if len(Herbivore.obj_collection) == 0:
                for _ in range(random.randint(1, 3)):
                    MakeMapObj.process(Herbivore)
            if len(Predator.obj_collection) == 0:
                for _ in range(random.randint(1, 3)):
                    MakeMapObj.process(Predator)
            if len(Grass.obj_collection) == 0:
                for _ in range(random.randint(1, 3)):
                    MakeMapObj.process(Grass)
            Simulation.next_turn()
            if msvcrt.kbhit() and msvcrt.getch() == b' ':
                Simulation.pause_simulation()
    @classmethod
    def pause_simulation(cls):
        Simulation.simulating = False
        print('Симуляция приостановлена')
Simulation.init_actions = [MakeMap, MakeDefaultWorld, Simulation.start_simulation]
Simulation.turn_actions = [Simulation.render, Simulation.next_turn, CheckEcoSystem.activate, CheckforPause.activate]

if __name__ == "__main__":
    print("Добро пожаловать в симуляцию животного мира. В ходе симуляции вы можете остановить процесс, нажав на Пробел")
    for action in Simulation.init_actions:
        action()
    while Simulation.break_status == False:
        if Simulation.simulating:
            for action in Simulation.turn_actions:
                action()
        else:
            if msvcrt.kbhit():
                user_input = msvcrt.getch()
                if user_input == b' ':
                    Simulation.start_simulation()
                elif user_input == b'e':
                    Simulation.break_status = True
    print("Симуляция закончена")
    print("До скорых встреч ребятки")