from abc import ABC
class Entity(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
    def __repr__(self) -> str:
        return f'{self.name}'