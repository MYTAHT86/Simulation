from .creature import Creature
from .herbivore import Herbivore
from map.map import Map
from bfs.bfs import BFS


class Predator(Creature):
    def __init__(self, name, speed=1, hp=4, damage=2):
        super().__init__(name, speed, hp)
        self.damage = damage
        self.predator = '🐺'
        self.hunger = 0
        self.full_status = False
    
    def make_move(self):
        def hunger_process(self):
            if not self.full_status:    
                if self.hunger == 3:
                    self.hp -= 1
                else:
                    self.hunger += 1  
            if self.hp <= 0:
                location = Map.find_current_slot(self)
                Map.delete_on_map(location)
                Map.add_free_slot(location)
                Map.delete_instance_on_visual_map(location)
            self.full_status = False
        nearest_herbivore, step_variations, attacking_slot = BFS.search(self, Herbivore)
        if nearest_herbivore == None:
            hunger_process(self)
            return
        current_location = Map.find_current_slot(self)
        if attacking_slot != current_location:
            path = BFS.path_search(self, step_variations, attacking_slot)
            step_to_make = path[-(min(len(path) - 1, self.speed) + 1)]
            Map.predator_move_on_map(self, current_location, step_to_make)
            hunger_process(self)
        else:
            def attack(current_location, nearest_herbivore):
                herbivore = Map.find_instance_from_collection(nearest_herbivore)
                herbivore.lose_hp(self)
                if not Map.check_location(nearest_herbivore):
                    Map.predator_move_on_map(self, current_location, nearest_herbivore)
                    self.hunger = 0
                    self.hp = min(self.hp + 2, 4)
                    self.full_status = True               
            attack(current_location, nearest_herbivore)
            hunger_process(self)