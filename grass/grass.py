from entity.entity import Entity


class Grass(Entity):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.grass = '🌿'