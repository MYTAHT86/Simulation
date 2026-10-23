from map.map import Map


class BFS:
    @staticmethod
    def search(instance, classname_to_find):
        current_slot = Map.find_current_slot(instance)
        destination = None
        queue = [current_slot]
        step_options = []
        while not destination and queue:
            current_slot = queue.pop(0) 
            for vertical in range(-1, 2):
                if destination:
                    break
                for horizontal in range(-1, 2):
                    if (0 <= current_slot[0] + vertical <= 15 and 0 <= current_slot[1]  + horizontal <= 15) and ((vertical == 0) != (horizontal == 0)):
                        if Map.slot_check_for_destination(current_slot, vertical, horizontal, classname_to_find):
                            destination = (current_slot[0] + vertical, current_slot[1]  + horizontal)
                            break
                        new_slot = (current_slot[0] + vertical, current_slot[1] + horizontal)
                        if Map.is_slot_free(current_slot, vertical, horizontal) and not any(step[1] == new_slot for step in step_options):   
                            queue.append((current_slot[0] + vertical, current_slot[1]  + horizontal))  
                            step_options.append((current_slot, (current_slot[0] + vertical, current_slot[1]  + horizontal)))
        return destination, step_options, current_slot

    
    @staticmethod
    def path_search(instance, step_variations, eating_slot):
        path = [eating_slot]
        while path[-1] != Map.find_current_slot(instance):
            path.append(next((step[0] for step in step_variations if step[1] == path[-1]), None))
        return path