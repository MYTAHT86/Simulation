from entity.entity import Entity
class Rock(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.rock = '🗿'
class Tree(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.tree = '🌳'