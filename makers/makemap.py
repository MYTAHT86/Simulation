from map.map import Map
from actions.actions import Actions


class MakeMap(Actions):
    @staticmethod
    def activate() -> None:
        Map.map = [['.' for horizontal in range(16)] for vertical in range(16)] 