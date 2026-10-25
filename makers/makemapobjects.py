from actions.actions import Actions
from entity.entity import Entity
from map.map import Map


class MakeMapObjects(Actions):
    @staticmethod
    def activate(classname: type[Entity]) -> None:
        name_creator = f'{classname.__name__}{Map.create_number_for_instance() + 1}'
        name = classname(name_creator)
        attr = getattr(name, classname.__name__.lower())
        Map.setup_map_obj(name, attr)     