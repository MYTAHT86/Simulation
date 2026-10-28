from map.map import Map
from actions.actions import Actions
from config import MAP_SIZE_VERTICAL, MAP_SIZE_HORIZONTAL


class MakeMap(Actions):
    @staticmethod
    def activate() -> None:
        Map.map = [['.' for horizontal in range(MAP_SIZE_HORIZONTAL)] for vertical in range(MAP_SIZE_VERTICAL)] 