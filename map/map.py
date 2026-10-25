import random
from typing import TYPE_CHECKING

from entity.entity import Entity

if TYPE_CHECKING:
    from creatures.herbivore import Herbivore
    from creatures.predator import Predator


class Map:
    free_slots = [(vertical, horizontal) for vertical in range(16) for horizontal in range(16)]
    collection: dict[tuple[int, int], Entity | None] = {}
    number_counter_for_instance_names = 0
    
    @classmethod
    def herbivore_eat_on_map(cls, instance: "Herbivore") -> None:
        current_location = Map.find_current_slot(instance)
        Map.map[current_location[0]][current_location[1]] = '.'
        Map.add_free_slot(current_location)
        Map.delete_on_map(current_location)
        Map.collection[instance.nearest_grass[0]] = instance
        Map.map[instance.nearest_grass[0][0]][instance.nearest_grass[0][1]] = instance.herbivore
    
    @classmethod
    def herbivore_move_on_map(cls, instance: "Herbivore", current_location: tuple[int, int], step_to_make: tuple[int, int]) -> None:
        Map.map[current_location[0]][current_location[1]] = '.'
        Map.add_free_slot(current_location)
        Map.delete_on_map(current_location, step_to_make)
        Map.map[step_to_make[0]][step_to_make[1]] = instance.herbivore
        Map.collection[step_to_make] = instance
    
    @classmethod
    def predator_move_on_map(cls, instance: "Predator", current_location: tuple[int, int], step_to_make: tuple[int, int]) -> None:
        Map.map[current_location[0]][current_location[1]] = '.'
        Map.add_free_slot(current_location)
        Map.delete_on_map(current_location, step_to_make)
        Map.map[step_to_make[0]][step_to_make[1]] = instance.predator
        Map.collection[step_to_make] = instance
    
    @classmethod
    def delete_on_map(cls, current_location: tuple[int, int], step_to_make: tuple[int, int] | None = None) -> None:
        if step_to_make:
            del Map.collection[current_location]
            Map.free_slots.remove(step_to_make)
        else:
            del Map.collection[current_location]
    
    @classmethod
    def find_current_slot(cls, instance: Entity) -> tuple[int, int]:
        return next(k for k, v in Map.collection.items() if v == instance)
    
    @classmethod
    def slot_check_for_destination(cls, current_slot: tuple[int, int], vertical: int, horizontal: int, classname: type[Entity]) -> bool:
        return isinstance(Map.collection.get((current_slot[0] + vertical, current_slot[1]  + horizontal)), classname)
    
    @classmethod
    def is_slot_free(cls, current_slot: tuple[int, int], vertical: int, horizontal: int) -> bool:
        return (current_slot[0] + vertical, current_slot[1]  + horizontal) not in Map.collection.keys()
    
    @classmethod
    def find_instance_from_collection(cls, location: tuple[int, int]) -> Entity | None:
        return Map.collection[location]
    
    @classmethod
    def change_instance_on_map_to_nearest_grass(cls, instance: Entity, value: Entity | None = None) -> None:
         Map.collection[instance.nearest_grass[0]] = value
    
    @classmethod
    def delete_instance_on_visual_map(cls, location: tuple[int, int]) -> None:
        Map.map[location[0]][location[1]] = '.'
    
    @classmethod
    def check_location(cls, location: tuple[int, int]) -> bool:
        return location in Map.collection.keys()
    
    @classmethod
    def add_free_slot(cls, location: tuple[int, int]) -> None:
        Map.free_slots.append(location)
    
    @classmethod
    def setup_map_obj(cls, name: Entity, attr: str) -> None:
        position = random.choice(Map.free_slots)
        Map.collection[position] = name
        Map.map[position[0]][position[1]] = attr
        Map.free_slots.remove(position)
    
    @classmethod
    def create_number_for_instance(cls) -> int:
        Map.number_counter_for_instance_names += 1
        return Map.number_counter_for_instance_names