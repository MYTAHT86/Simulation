from entity.entity import Entity
from map.map import Map


class Creature(Entity):
    def __init__(self, name, speed=1, hp=5):
        super().__init__(name)
        self.speed = speed
        self.hp = hp
    
    def make_move(self):
        pass
    
    def lose_hp(self):
        pass