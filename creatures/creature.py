from entity.entity import Entity


class Creature(Entity):
    def __init__(self, name: str, speed: int = 1, hp: int = 5) -> None:
        super().__init__(name)
        self.speed = speed
        self.hp = hp
    
    def make_move(self) -> None:
        pass
    
    def lose_hp(self) -> None:
        pass