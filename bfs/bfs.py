from map.map import Map
from entity.entity import Entity
from config import MAP_SIZE_HORIZONTAL, MAP_SIZE_VERTICAL


class BFS:
    @staticmethod
    def search(instance: Entity, classname_to_find: type[Entity]) -> tuple[tuple[int, int] | None, list[tuple[tuple[int, int], tuple[int, int]]], tuple[int, int]]:
        current_slot = Map.find_current_slot(instance)
        destination = None
        queue = [current_slot]
        queue_index = 0
        step_options = []
        while not destination and queue_index != len(queue):
            current_slot = queue[queue_index]
            for vertical in range(-1, 2):
                if destination:
                    break
                for horizontal in range(-1, 2):
                    if (0 <= current_slot[0] + vertical < MAP_SIZE_VERTICAL and 0 <= current_slot[1]  + horizontal < MAP_SIZE_HORIZONTAL) and ((vertical == 0) != (horizontal == 0)):
                        if Map.slot_check_for_destination(current_slot, vertical, horizontal, classname_to_find):
                            destination = (current_slot[0] + vertical, current_slot[1]  + horizontal)
                            break
                        new_slot = (current_slot[0] + vertical, current_slot[1] + horizontal)
                        if Map.is_slot_free(current_slot, vertical, horizontal) and not any(step[1] == new_slot for step in step_options):   
                            queue.append((current_slot[0] + vertical, current_slot[1]  + horizontal))  
                            step_options.append((current_slot, (current_slot[0] + vertical, current_slot[1]  + horizontal)))
            queue_index += 1
        return destination, step_options, current_slot

    
    @staticmethod
    def path_search(instance: Entity, step_variations: list[tuple[tuple[int, int], tuple[int, int]]], eating_slot: tuple[int, int]) -> list[tuple[int, int]]:
        path = [eating_slot]
        while path[-1] != Map.find_current_slot(instance):
            path.append(next((step[0] for step in step_variations if step[1] == path[-1])))
        return path