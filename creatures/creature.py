from entity.entity import Entity
from map.map import Map
class Creature(Entity):
    def __init__(self, name, speed=1, hp=5):
        super().__init__(name)
        self.speed = speed
        self.hp = hp
    def make_move(self):
        pass
    def search(self, classname_to_find):
        current_slot = Map.find_current_slot(self)
        destination = None
        queue = [current_slot]
        step_options = []
        while destination == None and queue:
            current_slot = queue.pop(0) 
            for vertical in range(-1, 2):
                if destination:
                    break
                for horizontal in range(-1, 2):
                    if (0 <= current_slot[0] + vertical <= 15 and 0 <= current_slot[1]  + horizontal <= 15) and ((vertical == 0) != (horizontal == 0)):
                        if Map.isinstance_check(current_slot, vertical, horizontal, classname_to_find):
                            destination = (current_slot[0] + vertical, current_slot[1]  + horizontal)
                            break
                        new_slot = (current_slot[0] + vertical, current_slot[1] + horizontal)
                        if Map.slots_check(current_slot, vertical, horizontal) and not any(step[1] == new_slot for step in step_options):   
                            queue.append((current_slot[0] + vertical, current_slot[1]  + horizontal))  
                            step_options.append((current_slot, (current_slot[0] + vertical, current_slot[1]  + horizontal)))
        return destination, step_options, current_slot
    def path_search(self, step_variations, eating_slot):
        path = [eating_slot]
        while path[-1] != Map.find_current_slot(self):
            path.append(next((step[0] for step in step_variations if step[1] == path[-1]), None))
        return path
    def lose_hp(self):
        pass