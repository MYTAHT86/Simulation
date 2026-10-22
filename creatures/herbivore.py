from .creature import Creature
from map.map import Map
from grass.grass import Grass
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