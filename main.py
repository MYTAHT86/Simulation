from abc import ABC
class Entity(ABC):
    pass
class Rock(Entity):
    def __init__(self):
        self.rock = '🪨'
class Tree(Entity):
    def __init__(self):
        self.tree = '🌳'
class Grass(Entity):
    def __init__(self):
        self.grass = '🌿'
class Creature(Entity):
    def __init__(self, speed=1, hp=5):
        self.speed = speed
        self.hp = hp
    def make_move(self):
        pass
class Herbivore(Creature):
    def __init__(self, speed=1, hp=5):
        super().__init__(speed, hp)
        self.herbivore = '🐰'
    def make_move(self):
        pass
class Preadator(Creature):
    def __init__(self, speed=1, hp=5):
        super().__init__(speed, hp)
        self.predator = '🐺'
    def make_move(self):
        pass
class Map:
    def __init__(self):
        self.map = [['.' for i in range(16)] for p in range(16)]
    def ris(self):
        for row in self.map:
            print(*row)
karta = Map()
karta.ris()

